🗺️ 控制浏览器
---

现在，让我们通过一些示例来了解 DrissionPage 的工作原理。

本示例演示使用 `ChromiumPage` 控制浏览器登录 gitee 网站。

## ✅️️ 页面分析

URL: [https://gitee.com/login](https://gitee.com/login)

当我们打开 URL 并按 F12 时，可以看到页面的 HTML 如下：

![](../../imgs/gitee_1.jpg)

用户名输入框的 `id` 为 `'user_login'`，密码输入框的 `id` 为 `'user_password'`，登录按钮的 `value` 为 `'登录'`。

我们可以使用这三个属性来定位这三个元素，然后输入数据并点击它们。

---

## ✅️️ 示例代码

您可以将以下代码复制到编辑器中，将账号和密码更改为您自己的，然后直接执行以查看结果。

```python
from DrissionPage import ChromiumPage

# 创建页面对象并启动或接管浏览器
page = ChromiumPage()
# 导航到登录页面
page.get('https://gitee.com/login')

# 定位用户名文本框并获取元素
ele = page.ele('#user_login')
# 将账号输入到文本框中
ele.input('您的账号')
# 定位密码文本框并输入密码
page.ele('#user_password').input('您的密码')
# 点击登录按钮
page.ele('@value=登录').click()
```

---

## ✅️️ 示例说明

让我们逐行分析代码：

```python
from DrissionPage import ChromiumPage
```

↑ 首先，我们导入用于控制浏览器的 `ChromiumPage` 类。

```python
page = ChromiumPage()
```

↑ 接下来，我们创建一个 `ChromiumPage` 对象。

```python
page.get('https://gitee.com/login')
```

↑ `get()` 方法用于访问给定的 URL。它将等待页面完全加载后再执行后续代码。您也可以修改等待策略，例如通过停止加载来等待 DOM 加载而不等待资源下载。这将在后面的章节中解释。

```python
ele = page.ele('#user_login')
```

↑ `ele()` 方法用于查找元素，它返回一个 `ChromiumElement` 对象来操作元素。

`'#user_login'` 是定位器文本，`#` 表示通过 `id` 属性定位元素。

值得一提的是，`ele()` 具有内置等待功能。如果元素未加载，它将等待直到元素出现或达到时间限制。默认超时为 10 秒。

```python
ele.input('您的账号')
```

↑ `input()` 方法用于向元素输入文本。

```python
page.ele('#user_password').input('您的密码')
```

↑ 我们也可以执行链式操作，直接获取元素并输入文本。

```python
page.ele('@value=登录').click()
```

↑ 输入账号和密码后，我们使用相同的方法获取按钮元素并对其执行点击操作。

不同的是，这次我们通过其 `value` 属性进行搜索。`@` 表示按属性名搜索。

通过这样做，我们完成了在 gitee 网站上的自动登录操作。
