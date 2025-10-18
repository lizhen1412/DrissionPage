🌏 基础概念
---

## 📚 什么是 DrissionPage？

DrissionPage 是一个 Python 网页自动化库，它结合了浏览器自动化和 HTTP 请求两种模式，让您能够：

- 🎭 **控制浏览器**：模拟用户操作，如点击、输入、滚动等
- 🌐 **发送请求**：像 requests 一样发送 HTTP 请求获取数据
- 🔄 **模式切换**：在两种模式间自由切换，享受各自的优势

---

## 🏗️ 核心架构

### 三种页面对象

DrissionPage 提供了三种主要的页面对象：

#### 1. SessionPage - 请求模式
```python
from DrissionPage import SessionPage

# 创建请求页面对象
page = SessionPage()
page.get('https://www.example.com')
title = page.title
print(title)
```

**特点：**
- 🚀 速度快，适合数据采集
- 💾 内存占用少
- 🎯 无法处理 JavaScript 动态内容

#### 2. ChromiumPage - 浏览器模式
```python
from DrissionPage import ChromiumPage

# 创建浏览器页面对象
page = ChromiumPage()
page.get('https://www.example.com')
page.ele('#search').input('Python')
page.ele('#submit').click()
```

**特点：**
- 🎭 完整的浏览器功能
- 🔧 可以处理 JavaScript
- 📱 支持复杂的用户交互

#### 3. WebPage - 混合模式
```python
from DrissionPage import WebPage

# 创建混合页面对象
page = WebPage()
page.get('https://www.example.com')

# 切换到浏览器模式
page.change_mode('d')
page.ele('#login').click()

# 切换到请求模式
page.change_mode('s')
data = page.html
```

**特点：**
- 🔄 两种模式自由切换
- 🍪 自动同步 Cookies
- 🎯 最佳的使用体验

---

## 🎯 元素定位

### 基本语法

DrissionPage 提供了简洁的元素定位语法：

```python
# 通过 ID 查找
element = page.ele('#id')

# 通过 class 查找
element = page.ele('.class')

# 通过标签查找
element = page.ele('tag:div')

# 通过文本查找
element = page.ele('text:登录')

# 通过属性查找
element = page.ele('@name=username')
```

### 查找多个元素

```python
# 查找所有匹配的元素
elements = page.eles('.item')

# 遍历元素
for element in elements:
    print(element.text)
```

---

## ⏰ 等待机制

### 智能等待

DrissionPage 内置了智能等待机制：

```python
# 等待元素出现
page.wait.ele_displayed('#loading', timeout=10)

# 等待元素消失
page.wait.ele_hidden('#loading')

# 等待页面加载完成
page.wait.doc_loaded()

# 等待 URL 变化
page.wait.url_change('success')
```

### 元素等待

```python
element = page.ele('#button')

# 等待元素可点击
element.wait.clickable()

# 等待元素显示
element.wait.displayed()

# 等待元素隐藏
element.wait.hidden()
```

---

## 🔧 配置管理

### 基本配置

```python
from DrissionPage import ChromiumOptions

# 创建配置对象
options = ChromiumOptions()

# 设置浏览器路径
options.set_browser_path('C:/Program Files/Google/Chrome/Application/chrome.exe')

# 设置无头模式
options.headless(True)

# 设置代理
options.set_proxy('http://proxy.example.com:8080')

# 创建页面对象
page = ChromiumPage(options)
```

### 配置文件

DrissionPage 支持使用 INI 配置文件：

```ini
[chromium_options]
address = 127.0.0.1:9222
browser_path = chrome
arguments = ['--no-default-browser-check', '--disable-suggestions-ui']

[timeouts]
base = 10
page_load = 30
script = 30
```

---

## 🎨 元素操作

### 基本操作

```python
element = page.ele('#input')

# 输入文本
element.input('Hello World')

# 点击元素
element.click()

# 清空内容
element.clear()

# 获取文本
text = element.text

# 获取属性
href = element.attr('href')
```

### 高级操作

```python
# 悬停
element.hover()

# 拖拽
element.drag(100, 100)

# 执行 JavaScript
result = element.run_js('return this.value;')

# 截图
element.get_screenshot('element.png')
```

---

## 📁 文件操作

### 文件上传

```python
# 上传单个文件
page.ele('#file-input').upload('path/to/file.txt')

# 上传多个文件
page.ele('#file-input').upload(['file1.txt', 'file2.txt'])
```

### 文件下载

```python
# 下载文件
page.ele('#download-link').click.to_download('downloads/')

# 等待下载完成
page.wait.download_begin()
```

---

## 🔍 调试技巧

### 查看页面信息

```python
# 查看当前 URL
print(f"当前 URL: {page.url}")

# 查看页面标题
print(f"页面标题: {page.title}")

# 查看页面 HTML
print(page.html)
```

### 截图调试

```python
# 保存页面截图
page.get_screenshot('debug.png')

# 保存元素截图
page.ele('#button').get_screenshot('button.png')
```

---

## 🚨 错误处理

### 常见错误

```python
from DrissionPage.errors import ElementNotFoundError, WaitTimeoutError

try:
    element = page.ele('#non-existent-element')
    element.click()
except ElementNotFoundError:
    print("元素未找到")
except WaitTimeoutError:
    print("等待超时")
```

### 错误处理最佳实践

```python
# 检查元素是否存在
if page.ele('#button', timeout=0):
    page.ele('#button').click()
else:
    print("按钮不存在")

# 使用等待机制
if page.wait.ele_displayed('#loading', timeout=5):
    print("页面加载完成")
else:
    print("页面加载超时")
```

---

## 💡 最佳实践

### 1. 选择合适的模式

- **数据采集**：使用 SessionPage 或 WebPage 的请求模式
- **用户交互**：使用 ChromiumPage 或 WebPage 的浏览器模式
- **复杂场景**：使用 WebPage 混合模式

### 2. 合理使用等待

```python
# 好的做法
page.wait.ele_displayed('#content')
content = page.ele('#content').text

# 避免的做法
import time
time.sleep(5)  # 固定等待时间
```

### 3. 异常处理

```python
# 好的做法
try:
    page.ele('#button').click()
except ElementNotFoundError:
    print("按钮未找到，跳过点击")
except Exception as e:
    print(f"其他错误: {e}")
```

### 4. 资源管理

```python
# 好的做法
page = ChromiumPage()
try:
    # 执行操作
    page.get('https://www.example.com')
    # ...
finally:
    page.quit()  # 确保关闭浏览器
```

---

## 🎯 学习建议

### 学习路径

1. **基础阶段**：了解 Python 基础和 HTML/CSS 基础
2. **入门阶段**：学习基本用法，完成简单示例
3. **进阶阶段**：掌握元素定位和等待机制
4. **高级阶段**：学习性能优化和错误处理

### 实践项目

1. **简单爬虫**：爬取新闻标题
2. **表单自动化**：自动填写表单
3. **数据采集**：批量获取商品信息
4. **测试自动化**：网页功能测试

---

## 📖 下一步

现在您已经了解了 DrissionPage 的基础概念，可以：

1. [安装 DrissionPage](installation.md)
2. [查看示例](examples/)
3. [学习元素定位](get_elements/)
4. [探索高级功能](advance/)

祝您使用愉快！🎉
