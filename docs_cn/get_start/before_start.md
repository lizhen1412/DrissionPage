🌏 准备工作
---

在开始之前，让我们进行一些简单的设置。

如果您只需要收发数据包，则无需任何准备。

如果您想控制浏览器，需要设置浏览器路径。默认情况下，程序设置为控制 Chrome，因此以下演示将使用 Chrome。同样的方法可用于设置 Edge 或其他基于 Chromium 的浏览器。

:::warning 注意
    作者发现 Chrome 92 版本存在一些奇怪的问题，在某些计算机环境中无法启动。如果可能，请避免使用此版本。
:::

## ✅️️ 操作步骤

### 1️⃣ 尝试启动浏览器

默认情况下，程序会自动在系统中搜索 Chrome 路径。

执行以下代码。如果浏览器启动并访问项目文档，说明您可以直接使用并跳过以下步骤。

```python
from DrissionPage import ChromiumPage

page = ChromiumPage()
page.get('http://g1879.gitee.io/DrissionPageDocs')
```

---

### 2️⃣ 设置路径

如果上一步提示错误，说明程序在系统中未找到 Chrome 浏览器。

您可以使用以下方法之一来设置路径。设置将记录在默认配置文件中，程序将在以后的启动中使用。

:::tip 如何获取浏览器路径
    这里的浏览器路径不一定是 Chrome；可以是任何基于 Chromium 的浏览器，如 Edge。
    打开浏览器，在地址栏输入 `chrome://version`（Edge 输入 `edge://version`），然后按回车。
    ![](../imgs/find_browser_path.png)  
    图片中的红框显示了您需要获取的路径。  
    此方法不仅限于 Windows；您也可以在具有图形界面的 Linux 上使用它来获取路径。    
:::

**🔸 方法一：**

创建一个临时 Python 文件并输入以下代码，将路径替换为您计算机上 Chrome 的可执行文件路径。然后运行该文件。

```python
from DrissionPage import ChromiumOptions

path = r'D:\Chrome\Chrome.exe'  # 请更改为您计算机上 Chrome 的可执行文件路径
ChromiumOptions().set_browser_path(path).save()
```

此代码将在配置文件中记录浏览器路径，将来将使用新路径启动浏览器。

此外，如果您想临时切换浏览器路径以测试其是否正常运行，可以删除 `.save()` 并与步骤 1️⃣ 的代码结合使用以下代码。

```python
from DrissionPage import ChromiumPage, ChromiumOptions

path = r'D:\Chrome\Chrome.exe'  # 请更改为您计算机上 Chrome 的可执行文件路径
co = ChromiumOptions().set_browser_path(path)
page = ChromiumPage(co)
page.get('http://g1879.gitee.io/DrissionPageDocs')
```

**🔸 方法二：**

在命令行中输入以下命令（将路径替换为您计算机上的路径）：

```shell
dp -p D:\Chrome\chrome.exe
```

:::warning 注意
    - 确保命令行中的 Python 环境与项目环境相同。
    - 确保首先使用 `cd` 命令导航到项目路径。
:::

---

### 3️⃣ 重新尝试控制浏览器

现在，请重新执行步骤 1️⃣ 的代码。如果成功访问项目文档，说明设置完成。

```python
from DrissionPage import ChromiumPage

page = ChromiumPage()
page.get('http://g1879.gitee.io/DrissionPageDocs')
```

---

## ✅️️ 说明

完成准备工作后，无需关闭浏览器。您可以继续使用当前浏览器进行后续示例。
