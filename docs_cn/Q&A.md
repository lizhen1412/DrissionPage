# ❓ 常见问题
hide:
  - navigation
---

本页面收集了用户在使用过程中经常遇到的问题。

欢迎开发者通过提交 issue、PR 或撰写博客文章并将链接发送给本仓库作者来贡献内容。

## ❓ 如何在无头 Linux 上使用？

**回答：**

对于 CentOS，请参考这篇文章：[Linux 部署说明](https://blog.csdn.net/sinat_39327967/article/details/132181129?spm=1001.2014.3001.5501)

对于 Ubuntu，请参考这篇文章：[DrissionPage 在 Ubuntu Linux 上的使用](https://zhuanlan.zhihu.com/p/674687748)

---

## ❓ 为什么浏览器无法退出无头模式？

> 为什么在之前设置无头模式后，下次运行时即使没有设置 `headless()`，浏览器仍然进入无头模式？

**回答：**

这是因为之前打开的浏览器没有关闭，只是由于无头模式而不可见。程序继续控制它。

要关闭浏览器，您可以在程序末尾使用 `page.quit()` 语句。

您也可以设置 `co.headless(False)`，程序将自动关闭之前的无头浏览器并启动新的浏览器。

还要注意，`page.close()` 函数关闭当前标签页，而不是浏览器，除非浏览器只有一个标签页。

---

## ❓ 如何禁用浏览器的弹出提示，例如是否保存密码或恢复页面？

**回答：**

当浏览器弹出提示出现时，您可以手动关闭它们。不关闭它们不会影响自动操作。也可以在代码中防止它们显示。
添加一些浏览器配置代码来禁用相应的提示。您需要添加如下代码：

```python
co = ChromiumOptions()

# 禁用"保存密码"的提示气泡
co.set_pref('credentials_enable_service', False)

# 禁用"您是否要恢复此页面？Chrome 未正确关闭。"的提示气泡
co.set_argument('--hide-crash-restore-bubble')

page = ChromiumPage(co)
```

---

## ❓ 使用 `.click()` 时报告错误"元素没有位置和大小"。如何解决？

**回答：**

元素没有位置和大小是正常的，因为许多元素都没有它们。

此时，您需要检查页面中是否有同名元素，以及定位器是否准确并检索到另一个元素。

如果您要点击的元素确实没有位置，可以通过使用 JavaScript 强制点击，用法是 `.click(by_js=True)`，可以简化为 `.click('js')`。

---

## ❓ 其他自动化工具似乎能够使用浏览器的高级功能（启动选项、用户偏好、实验性标志）。如何在 DrissionPage 中使用它们？

**回答：**

### 启动选项 (arguments)
- 用法参考：[https://g1879.gitee.io/drissionpagedocs/ChromiumPage/browser_opt#-set_argument](https://g1879.gitee.io/drissionpagedocs/ChromiumPage/browser_opt#-set_argument)
- 参数详情：[https://peter.sh/experiments/chromium-command-line-switches/](https://peter.sh/experiments/chromium-command-line-switches/)

### 用户偏好 (prefs)
- 用法参考：[https://g1879.gitee.io/drissionpagedocs/ChromiumPage/browser_opt#-set_pref](https://g1879.gitee.io/drissionpagedocs/ChromiumPage/browser_opt#-set_pref)
- 参数详情：[https://src.chromium.org/viewvc/chrome/trunk/src/chrome/common/pref_names.cc](https://src.chromium.org/viewvc/chrome/trunk/src/chrome/common/pref_names.cc)

### 实验性标志 (flags)
- 用法参考：[https://g1879.gitee.io/drissionpagedocs/ChromiumPage/browser_opt#-set_flag](https://g1879.gitee.io/drissionpagedocs/ChromiumPage/browser_opt#-set_flag)
- 参数详情：[chrome://flags](chrome://flags)

:::warning 注意
    外部链接仅供参考。请谨慎使用任何高级功能，只有在您完全控制的情况下才使用，因为使用这些功能可能会导致浏览器数据丢失或损害安全和隐私。
