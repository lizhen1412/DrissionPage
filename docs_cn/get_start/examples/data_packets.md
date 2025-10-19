🗺️ 收发数据包
---

本示例演示如何使用 `SessionPage` 通过收发数据包从 gitee 网站收集数据。

本示例不使用浏览器。

## ✅️️ 页面分析

URL: [https://gitee.com/explore/all](https://gitee.com/explore/all)

本示例的目标是检索所有仓库的名称和链接。为了避免给网站造成压力，我们只收集 3 页的数据。

打开 URL，按 `F12`，我们可以看到页面的 HTML 如下：

![](../../imgs/gitee_2.jpg)

从 HTML 代码中，我们可以看到所有开源项目的标题都是 `class` 属性为 `'title project-namespace-path'` 的 `<a>` 元素。我们可以遍历这些 `<a>` 元素来检索它们的信息。

同时，我们观察到列表页面的 URL 是通过页码作为参数访问的。例如，第一页的 URL 是 `https://gitee.com/explore/all?page=1`，其中页码是 `page` 参数。因此，我们可以通过修改此参数来访问不同的页面。

---

## ✅️️ 示例代码

以下代码可以直接运行以查看结果：

```python
from DrissionPage import SessionPage

# 创建页面对象
page = SessionPage()

# 爬取 3 页
for i in range(1, 4):
    # 访问特定页面
    page.get(f'https://gitee.com/explore/all?page={i}')
    # 获取所有仓库 <a> 元素的列表
    links = page.eles('.title project-namespace-path')
    # 遍历所有 <a> 元素
    for link in links:
        # 打印链接信息
        print(link.text, link.link)
```

**输出：**

```shell
小熊派开源社区/BearPi-HM_Nano https://gitee.com/bearpi/bearpi-hm_nano
明月心/PaddleSegSharp https://gitee.com/raoyutian/PaddleSegSharp
RockChin/QChatGPT https://gitee.com/RockChin/QChatGPT
TopIAM/eiam https://gitee.com/topiam/eiam

...省略...
```

---

## ✅️️ 示例说明

让我们逐行分析代码：

```python
from DrissionPage import SessionPage
```

↑ 首先，我们导入用于收发数据包的 `SessionPage` 类。

```python
page = SessionPage()
```

↑ 接下来，我们创建一个 `SessionPage` 对象。

```python
for i in range(1, 4):
    page.get(f'https://gitee.com/explore/all?page={i}')
```

↑ 然后，我们迭代 3 次来构造每页的 URL，并使用 `get()` 方法访问页面 URL。

```python
links = page.eles('.title project-namespace-path')
```

↑ 访问 URL 后，我们使用页面对象的 `eles()` 方法获取所有 `class` 属性为 `'title project-namespace-path'` 的元素。

`eles()` 方法用于查找满足条件的多个元素，它返回元素列表。

这里，搜索的条件是 `class` 属性，`.` 表示搜索基于 `class` 属性。

```python
for link in links:
    print(link.text, link.link)
```

↑ 最后，我们遍历获得的元素列表，检索并打印每个元素的属性。

`.text` 检索元素的文本，`.link` 检索元素的 `href` 或 `src` 属性。
