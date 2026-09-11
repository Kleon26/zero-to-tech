# backend/main.py
import os
import uuid
from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pypinyin import lazy_pinyin, Style
from snownlp import SnowNLP
from datetime import datetime, timezone

from storage import init_db, save_record, get_history      # ← 新增：跟存储层打交道，只经过这一行

init_db()  # 初始化数据库

app = FastAPI()

# CORS：浏览器只放行"名单里"的来源，名单外的请求会被拦下，
# 前端 fetch 拿不到响应，控制台只会看到一句没有细节的 "Failed to fetch"。
# 这里原来写死了 "http://192.168.10.83:3000"，那是当时这台电脑的局域网 IP；
# 后来路由器重新分配，IP 变成 192.168.10.23，用新 IP 打开页面就被 CORS 拦掉了。
# 所以局域网 IP 不再写死，改用正则兜住整段私网地址，换 IP、换端口都不用再改代码。
CORS_ORIGINS = [
    origin.strip()
    for origin in os.environ.get("CORS_ORIGINS", "").split(",")
    if origin.strip()
] or [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

CORS_ORIGIN_REGEX = (
    r"^http://("
    r"localhost"
    r"|127\.0\.0\.1"
    r"|192\.168\.\d{1,3}\.\d{1,3}"          # 家用路由器最常见的一段
    r"|10\.\d{1,3}\.\d{1,3}\.\d{1,3}"
    r"|172\.(?:1[6-9]|2\d|3[01])\.\d{1,3}\.\d{1,3}"
    r")(?::\d+)?$"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_origin_regex=CORS_ORIGIN_REGEX,
    allow_methods=["GET", "POST"],
     allow_credentials=True,          # ← 新增：允许跨源请求带上 cookie
)

def get_session_id(request: Request, response: Response) -> str:
    sid = request.cookies.get("session_id")      # 先看有没有纸条
    if not sid:                                  # 第一次来，没有——发一张
        sid = uuid.uuid4().hex                    # 一串随机、不重复的 id
        response.set_cookie(
            "session_id", sid,
            httponly=True, samesite="lax",
            max_age=60 * 60 * 24 * 30,            # 记 30 天
        )
    return sid

profile = {
    "heroTitle": "关于我",
    "heroSubtitle": "项目，创意，灵感，心得，我的作品",
    "featuredWork": {
        "kicker": "作品",
        "title": "文字实验室",
        "copy": "拼音和情绪，挖掘中文里的细节",
        "linkLabel": "打开作品",
    },
    "identity": {
        "motto": "已识乾坤大，尤怜草木青",
        "learning": "零到全栈",
    },
}

class AnalyzeRequest(BaseModel):
    text: str

def score_label(score):
    if score >= 0.6:
        return "偏积极"
    elif score <= 0.4:
        return "偏消极"
    else:
        return "中性"

@app.get("/api/profile")
def get_profile():
    return profile

@app.post("/api/analyze")
def analyze(req: AnalyzeRequest, request: Request, response: Response):
    sid = get_session_id(request, response)
    text = req.text
    score = round(SnowNLP(text).sentiments, 2)
    result = {
        "text": text,
        "score": score,
        "label": score_label(score),
        "pinyin": " ".join(lazy_pinyin(text, style=Style.TONE)),
        "created_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    save_record(sid, result)          # 存的时候盖上这个会话的记号
    return result                     # ← 返回体一个字没变，session_id 只走 cookie

@app.get("/api/history")
def history(request: Request, response: Response, limit: int = 10):
    sid = get_session_id(request, response)
    return get_history(sid, limit)    # 只回这个会话自己的

