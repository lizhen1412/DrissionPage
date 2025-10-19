🌏 快速示例
---

## 🚀 基础示例

### 示例 1：简单网页访问

```python
from DrissionPage import ChromiumPage

# 创建页面对象
page = ChromiumPage()

# 访问网页
page.get('https://www.baidu.com')

# 获取页面标题
print(f"页面标题: {page.title}")

# 关闭浏览器
page.quit()
```

### 示例 2：搜索功能

```python
from DrissionPage import ChromiumPage

page = ChromiumPage()
page.get('https://www.baidu.com')

# 输入搜索关键词
page.ele('#kw').input('Python')

# 点击搜索按钮
page.ele('#su').click()

# 等待搜索结果加载
page.wait.ele_displayed('#content_left')

# 获取搜索结果
results = page.eles('.result')
for i, result in enumerate(results[:5], 1):
    title = result.ele('h3 a').text
    print(f"{i}. {title}")

page.quit()
```

---

## 🎭 浏览器模式示例

### 示例 3：登录自动化

```python
from DrissionPage import ChromiumPage

page = ChromiumPage()
page.get('https://www.example.com/login')

# 输入用户名和密码
page.ele('#username').input('your_username')
page.ele('#password').input('your_password')

# 点击登录按钮
page.ele('#login-btn').click()

# 等待登录成功
page.wait.url_change('dashboard')

print("登录成功！")
page.quit()
```

### 示例 4：表单填写

```python
from DrissionPage import ChromiumPage

page = ChromiumPage()
page.get('https://www.example.com/form')

# 填写表单
page.ele('#name').input('张三')
page.ele('#email').input('zhangsan@example.com')
page.ele('#phone').input('13800138000')

# 选择下拉框
page.ele('#city').select.by_text('北京')

# 选择复选框
page.ele('#agree').check()

# 提交表单
page.ele('#submit').click()

# 等待提交成功
page.wait.ele_displayed('.success-message')

print("表单提交成功！")
page.quit()
```

---

## 🌐 请求模式示例

### 示例 5：数据采集

```python
from DrissionPage import SessionPage

page = SessionPage()
page.get('https://www.example.com/news')

# 获取所有新闻标题
news_titles = []
for news in page.eles('.news-item'):
    title = news.ele('h2').text
    link = news.ele('a').attr('href')
    news_titles.append({'title': title, 'link': link})

# 打印结果
for i, news in enumerate(news_titles, 1):
    print(f"{i}. {news['title']}")
    print(f"   链接: {news['link']}")
    print()
```

### 示例 6：API 调用

```python
from DrissionPage import SessionPage

page = SessionPage()

# 发送 POST 请求
response = page.post('https://api.example.com/data', 
                    json={'key': 'value'})

# 获取响应数据
data = response.json()
print(f"API 响应: {data}")

# 发送带参数的 GET 请求
response = page.get('https://api.example.com/search', 
                   params={'q': 'Python', 'limit': 10})
data = response.json()
print(f"搜索结果: {data}")
```

---

## 🔄 混合模式示例

### 示例 7：模式切换

```python
from DrissionPage import WebPage

page = WebPage()
page.get('https://www.example.com')

# 使用请求模式获取基本信息
print(f"页面标题: {page.title}")
print(f"页面URL: {page.url}")

# 切换到浏览器模式进行交互
page.change_mode('d')
page.ele('#search').input('Python')
page.ele('#search-btn').click()

# 等待搜索结果
page.wait.ele_displayed('.search-results')

# 切换回请求模式获取数据
page.change_mode('s')
results = page.eles('.result-item')
for result in results:
    title = result.ele('h3').text
    print(f"结果: {title}")

page.quit()
```

### 示例 8：Cookies 同步

```python
from DrissionPage import WebPage

page = WebPage()
page.get('https://www.example.com')

# 在浏览器模式中登录
page.change_mode('d')
page.ele('#username').input('user')
page.ele('#password').input('pass')
page.ele('#login').click()
page.wait.url_change('dashboard')

# 切换到请求模式，Cookies 自动同步
page.change_mode('s')

# 现在可以访问需要登录的页面
page.get('https://www.example.com/profile')
profile_data = page.ele('.profile-info').text
print(f"用户信息: {profile_data}")

page.quit()
```

---

## 📁 文件操作示例

### 示例 9：文件上传

```python
from DrissionPage import ChromiumPage

page = ChromiumPage()
page.get('https://www.example.com/upload')

# 上传单个文件
page.ele('#file-input').upload('path/to/file.txt')

# 上传多个文件
page.ele('#file-input').upload(['file1.txt', 'file2.txt'])

# 等待上传完成
page.wait.ele_displayed('.upload-success')

print("文件上传成功！")
page.quit()
```

### 示例 10：文件下载

```python
from DrissionPage import ChromiumPage

page = ChromiumPage()
page.get('https://www.example.com/download')

# 点击下载链接
page.ele('#download-link').click.to_download('downloads/')

# 等待下载开始
page.wait.download_begin()

# 等待下载完成
page.wait.downloads_done()

print("文件下载完成！")
page.quit()
```

---

## 🎯 高级示例

### 示例 11：多标签页操作

```python
from DrissionPage import ChromiumPage

page = ChromiumPage()
page.get('https://www.example.com')

# 打开新标签页
new_tab = page.new_tab('https://www.google.com')

# 在新标签页中操作
new_tab.ele('#search').input('Python')
new_tab.ele('#search-btn').click()

# 切换回原标签页
page.activate_tab(0)
page.ele('#button').click()

# 关闭新标签页
new_tab.close()

page.quit()
```

### 示例 12：iframe 操作

```python
from DrissionPage import ChromiumPage

page = ChromiumPage()
page.get('https://www.example.com')

# 获取 iframe
iframe = page.get_frame('#iframe-id')

# 在 iframe 中操作
iframe.ele('#input').input('Hello')
iframe.ele('#button').click()

# 返回主页面
page.ele('#main-button').click()

page.quit()
```

### 示例 13：网络监听

```python
from DrissionPage import ChromiumPage

page = ChromiumPage()
page.get('https://www.example.com')

# 开始监听网络请求
page.listen.start()

# 执行操作触发网络请求
page.ele('#button').click()

# 获取监听到的请求
requests = page.listen.wait()
for req in requests:
    print(f"请求URL: {req.url}")
    print(f"请求方法: {req.method}")
    print(f"响应状态: {req.response.status_code}")

page.quit()
```

---

## 🎨 元素操作示例

### 示例 14：复杂元素操作

```python
from DrissionPage import ChromiumPage

page = ChromiumPage()
page.get('https://www.example.com')

# 悬停操作
page.ele('#menu').hover()

# 拖拽操作
page.ele('#draggable').drag(100, 100)

# 右键点击
page.ele('#button').click.right()

# 双击
page.ele('#button').click.multi(2)

# 执行 JavaScript
result = page.ele('#input').run_js('return this.value;')
print(f"输入框的值: {result}")

# 截图
page.ele('#button').get_screenshot('button.png')

page.quit()
```

### 示例 15：元素筛选

```python
from DrissionPage import ChromiumPage

page = ChromiumPage()
page.get('https://www.example.com')

# 获取所有链接
links = page.eles('tag:a')

# 筛选可见的链接
visible_links = links.filter.displayed()

# 筛选包含特定文本的链接
python_links = visible_links.filter.text('Python')

# 筛选特定属性的链接
external_links = python_links.filter.attr('target', '_blank')

# 操作筛选后的元素
for link in external_links:
    print(f"外部链接: {link.attr('href')}")

page.quit()
```

---

## 🔧 配置示例

### 示例 16：自定义配置

```python
from DrissionPage import ChromiumOptions, ChromiumPage

# 创建配置对象
options = ChromiumOptions()

# 设置浏览器路径
options.set_browser_path('C:/Program Files/Google/Chrome/Application/chrome.exe')

# 设置无头模式
options.headless(True)

# 设置代理
options.set_proxy('http://proxy.example.com:8080')

# 设置下载路径
options.set_download_path('./downloads')

# 禁用图片加载
options.no_imgs(True)

# 设置用户代理
options.set_user_agent('Mozilla/5.0 Custom Browser')

# 创建页面对象
page = ChromiumPage(options)
page.get('https://www.example.com')

print("页面加载完成！")
page.quit()
```

### 示例 17：配置文件使用

```python
from DrissionPage import ChromiumPage

# 使用配置文件
page = ChromiumPage('config.ini')
page.get('https://www.example.com')

print("使用配置文件加载页面！")
page.quit()
```

---

## 🚨 错误处理示例

### 示例 18：异常处理

```python
from DrissionPage import ChromiumPage
from DrissionPage.errors import ElementNotFoundError, WaitTimeoutError

page = ChromiumPage()

try:
    page.get('https://www.example.com')
    
    # 尝试查找元素
    element = page.ele('#button')
    element.click()
    
    # 等待元素出现
    page.wait.ele_displayed('#success', timeout=10)
    
except ElementNotFoundError:
    print("元素未找到")
except WaitTimeoutError:
    print("等待超时")
except Exception as e:
    print(f"其他错误: {e}")
finally:
    page.quit()
```

---

## 💡 最佳实践示例

### 示例 19：完整的数据采集流程

```python
from DrissionPage import WebPage
import json

def scrape_news():
    page = WebPage()
    
    try:
        # 访问新闻网站
        page.get('https://news.example.com')
        
        # 等待页面加载
        page.wait.ele_displayed('.news-list')
        
        # 收集新闻数据
        news_data = []
        for news in page.eles('.news-item'):
            title = news.ele('h2').text
            link = news.ele('a').attr('href')
            time = news.ele('.time').text
            
            news_data.append({
                'title': title,
                'link': link,
                'time': time
            })
        
        # 保存数据
        with open('news.json', 'w', encoding='utf-8') as f:
            json.dump(news_data, f, ensure_ascii=False, indent=2)
        
        print(f"成功采集 {len(news_data)} 条新闻")
        
    except Exception as e:
        print(f"采集失败: {e}")
    finally:
        page.quit()

# 运行采集
scrape_news()
```

---

## 🎯 总结

这些示例涵盖了 DrissionPage 的主要功能：

1. **基础操作**：页面访问、元素查找、基本交互
2. **模式切换**：浏览器模式和请求模式的灵活使用
3. **文件操作**：文件上传和下载
4. **高级功能**：多标签页、iframe、网络监听
5. **配置管理**：自定义配置和配置文件使用
6. **错误处理**：异常处理和最佳实践

建议您：
1. 从简单示例开始
2. 逐步尝试复杂功能
3. 根据实际需求选择合适的模式
4. 注意错误处理和资源管理

祝您使用愉快！🎉
