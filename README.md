# Markdown语言

**这是一种超轻量标记语言**

## 段落
这是一段关于Markdown的段落  

## 换行
两个空格后回车实现换行效果  

## 粗斜体
这是**粗体**  
这是*斜体*  
这是***粗斜体***

## 引用块
>这是一段引用块
>
>可以包含一整个***段落***

## 列表
### 有序列表
1. First item
2. Second item

### 无序列表
- First item
- Second item
- Third item
- Fourth item

### 列表中嵌套引用块
*   This is the first list item.
*   Here's the second list item.
    > A blockquote would look great below the second list item.
*   And here's the third list item.

### 列表嵌套代码块(俩缩进)
1. Open the file.
2. Find the following code block on line 21:

        <html>
          <head>
            <title>Test</title>
          </head>

3. Update the title to match the name of your website.

### 有序列表嵌套无序（反之亦然）
1. First item
2. Second item
3. Third item
    - Indented item
    - Indented item
4. Fourth item

## 代码语法
### 将单词或者短语表示为代码
At the command prompt, type `nano`.

### 使用引号的方法
``这是使用`引号`的方法``

### 代码块（1缩进）
    <html>
      <head>
      </head>
    </html>

## 分隔线
Try to put a blank line before...

---

...and after a horizontal rule.

## 链接
### 基础链接语法
>``[超链接显示名](超链接地址 "超链接title")``  

这是一个链接 [Markdown语法](https://markdown.com.cn "最好的markdown教程")。

### 网址和email地址(使用尖括号)
<https://markdown.com.cn>  
<fake@example.com>

### 带格式化的链接
I love supporting the **[EFF](https://eff.org)**.  
This is the *[Markdown Guide](https://www.markdownguide.org)*.  
See the section on [`code`](#code).

## 转义字符
\* Without the backslash, this would be a bullet in an unordered list.

## 表格

| Syntax | Description |
| --- | ----------- |
| Header | Title |
| Paragraph | Text |