🗺️ 切换模式
---

本示例演示如何使用 `WebPage` 在控制浏览器和收发数据包之间切换。

通常，切换模式用于处理具有严格登录检查的网站。登录可以由浏览器处理，然后可以切换到收发数据包模式来收集数据。

但是，这种场景需要相应的账号，这对演示目的来说不太方便。在本示例中，我们使用浏览器在 gitee 上搜索，然后切换到收发数据包模式来读取数据。虽然本示例实际意义不大，但可以帮助理解其工作模式。

## ✅️️ 页面分析

URL: [https://gitee.com/explore](https://gitee.com/explore)

当我们打开 URL 并按 `F12` 时，可以看到页面的 HTML 如下：

![](../../imgs/change1.png)

输入框 `<input>` 元素的 `id` 属性为 `'q'`，搜索按钮 `<button>` 元素的 `text` 包含文本 `'搜索'`，这可以作为查找元素的条件。

输入关键词并搜索后，我们可以再次查看页面的 HTML：

![](../../imgs/change2.png)

通过分析 HTML 代码，我们可以看到每个结果的标题都在 `id` 为 `'hits-list'` 且 `class` 为 `'item'` 的元素内。因此，我们可以在页面中检索所有这些元素，然后遍历获取它们的信息。

---

## ✅️️ 示例代码

您可以直接运行以下代码：

```python
from DrissionPage import WebPage

# 创建页面对象
page = WebPage()
# 访问 URL
page.get('https://gitee.com/explore')
# 查找文本框元素并输入关键词
page('#q').input('DrissionPage')
# 点击搜索按钮
page('t:button@tx():搜索').click()
# 等待页面加载
page.wait.load_start()
# 切换到数据包模式
page.change_mode()
# 获取所有行元素
items = page('#hits-list').eles('.item')
# 遍历检索到的元素
for item in items:
    # 打印元素的文本
    print(item('.title').text)
    print(item('.desc').text)
    print()
```

**输出：**

```shell
g1879/DrissionPage
A web automation tool based on Python. It can control the browser and send/receive packets. It can combine the convenience of browser automation and the efficiency of requests. It has powerful features and built-in humanized designs and convenient functions. The syntax is concise and elegant, with minimal code.

mirrors_g1879/DrissionPage
DrissionPage

g1879/DrissionPageDocs
Documentation for DrissionPage
```

---

## ✅️️ 示例说明

让我们逐行分析代码：

```python
from DrissionPage import WebPage
```

↑ 首先，我们从 `DrissionPage` 模块导入 `WebPage` 类。

```python
page = WebPage()
```

↑ 然后，我们创建一个 `WebPage` 对象。

```python
page.get('https://gitee.com/explore')
```

↑ 接下来，我们控制浏览器访问 gitee。

```python
page('#q').input('DrissionPage')
page('t:button@tx():搜索').click()
page.wait.load_start()
```

↑ 我们模拟输入关键词并点击搜索按钮。

此代码中用于查找元素的方法已在之前的示例中解释过，这里不再详细讨论。

`wait.load_start()` 方法用于等待页面进入加载状态，避免因操作过快而导致的异常。

```python
page.change_mode()
```

↑ `change_mode()` 方法用于将工作模式从控制浏览器切换到收发数据包。

切换时，程序将在新模式中重新访问当前 URL。

```python
items = page('#hits-list').eles('.item')
```

↑ 切换后，我们可以使用与控制浏览器相同的语法来检索页面元素。这里，我们检索页面上的所有结果行，它返回这些元素对象的列表。

```python
for item in items:
    print(item('.title').text)
    print(item('.desc').text)
    print()
```

↑ 最后，我们遍历这些元素并打印它们包含的文本。
