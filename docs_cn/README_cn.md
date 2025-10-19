# ✨️ 概述

DrissionPage 是一个基于 Python 的网页自动化工具。

它既能控制浏览器，也能收发数据包，还能把两者合而为一。

可兼顾浏览器自动化的便利性和 requests 的高效率。

它功能强大，内置无数人性化设计和便捷功能。

它的语法简洁而优雅，代码量少，对新手友好。

---

<a href='https://gitee.com/g1879/DrissionPage/stargazers'><img src='https://gitee.com/g1879/DrissionPage/badge/star.svg?theme=dark' alt='star'></img></a> <a href='https://gitee.com/g1879/DrissionPage/members'><img src='https://gitee.com/g1879/DrissionPage/badge/fork.svg?theme=dark' alt='fork'></img></a>

项目地址：[gitee](https://gitee.com/g1879/DrissionPage)    |    [github](https://github.com/g1879/DrissionPage) 

您的星星是对我最大的支持💖

---

支持系统：Windows、Linux、Mac

Python 版本：3.6 及以上

支持浏览器：Chromium 内核浏览器(如 Chrome 和 Edge)，electron 应用

---

**📖 使用文档：**  [点击查看](https://DrissionPage.cn)

**交流 QQ 群：**  见使用文档

**📖 英文文档：**  [点击查看](https://github.com/y0un9kane/DrissionPage/tree/master/docs_en)

**Telegram 群：**   [@DrissionPage](https://t.me/DrissionPage)

---

# 🔥 即将发布版本预览

查看下一个开发计划：[即将发布版本预览](https://DrissionPage.cn/whatsnew/3_3/)

---

# 📕 背景

在使用 requests 进行数据采集时，遇到需要登录的网站，需要分析数据包和 JS 源码，构造复杂的请求，还要应对验证码、JS 混淆、签名参数等反爬措施，门槛较高，开发效率不高。

使用浏览器可以绕过很多这些障碍，但浏览器操作的效率不高。

因此，本库的初衷是将它们合并，既保留浏览器自动化的便利性，又保证数据采集的高效率，做到"写快"和"跑快"兼顾。它可以在需要时切换到相应模式，并提供人性化的使用方法，提高开发和运行效率。

除了合并两者，本库还以网页为单位封装了常用功能，提供非常便利的操作语句，让用户减少考虑细节，专注功能实现。用简单的方式实现强大的功能，使代码更优雅。

之前的版本是通过重新封装 selenium 实现的。从 3.0 版本开始，作者从零开始，重新开发底层框架，摆脱了对 selenium 的依赖，增强了功能，提高了运行效率。

---

# 💡 理念

简洁而强大！

--- 

# ☀️ 特性和亮点

作者经过长期实践，踩过无数坑，总结出的经验全写到这个库里了。

## 🎇 强大的自研内核

本库采用全自研的内核，内置无数实用功能，对常用功能作了整合和优化，对比 selenium，有以下优点：

- 不基于 webdriver
- 无需为不同版本的浏览器下载不同的驱动
- 运行速度更快
- 可以跨 iframe 查找元素，无需切入切出
- 把 iframe 看作普通元素，逻辑更清晰
- 可同时操作多个标签页，无需切换
- 可以直接读取浏览器缓存保存图片，无需用 GUI 点击另存
- 可以对整个网页截图，包括视口外的部分
- 可处理非`open`状态的 shadow-root

## 🎇 亮点功能

除了以上优点，本库还内置了无数人性化设计。

- 极简的定位语法，查找元素更加容易
- 集成大量常用功能，代码更优雅，功能强大稳定
- 无处不在的等待和自动重试，使不稳定的网络变得易于控制，程序更稳定，编写更省心
- 提供强大的下载工具，操作浏览器时也能享受快捷可靠的下载功能
- 允许反复使用已经打开的浏览器，无需每次运行从头启动浏览器，调试方便
- 使用 ini 文件保存常用配置，自动调用，提供便捷的设置，远离繁杂的配置项
- 内置 lxml 作为解析引擎，解析速度成几个数量级提升
- 使用 POM 模式封装，可直接用于测试，便于扩展
- 高度集成的便利功能，从每个细节中体现
- 还有很多细节，这里不一一列举，欢迎实际使用中体验：D

---

# 🛠 如何使用

**📖 使用文档：**  [点击查看](https://DrissionPage.cn)

**交流 QQ 群：**  见使用文档

![](https://drissionpage.cn/codes.png)

---

# 🔖 版本历史

[点击查看版本历史](https://DrissionPage.cn/history/3.x/)

---

# 🖐🏻 免责声明

请勿将 DrissionPage 用于任何可能违反当地法律规定和道德约束的项目中。请友好使用 DrissionPage，遵守爬虫协议。请勿将 DrissionPage 用于任何非法用途。选择使用 DrissionPage 即表示您同意本协议，作者不承担因您违反本协议而产生的任何法律风险和损失。您需自行承担所有后果。

---

# ☕ 请我喝咖啡

作者是个人开发者，开发和写文档工作量较为繁重。

如果本项目对您有所帮助，不妨打赏一下作者 ：）

![](https://drissionpage.cn/code2.jpg)

### 目录
* [快速开始](#section1)
    + [安装](get_start/installation.md)
    + [导入](#section3)
    + [开始前](#section4)
    + [示例](#section5)
* [SessionPage](#SessionPage)
    + [介绍](#intro)
    + [创建页面对象](#create page obj)
    + [打开网页](#open web)
    + [获取页面信息](#get page info)
    + [获取元素信息](#get element info)
    + [页面设置](#page settings)
    + [启动配置](#startup configuration)
* [ChromiumPage](#ChromiumPage)
    + [介绍](#intro)
    + [创建页面对象](#create page obj)
    + [打开网页](#open web)
    + [页面操作](#page operation)
    + [获取元素信息](#get element info)
    + [元素操作](#element operation)
    + [自动等待](#Auto waiting)
    + [文件上传](#File upload)
    + [标签页操作](#tab operation)
    + [iframe 操作](#iframe operation)
    + [监听网络数据](#listen in network data)
    + [动作链](#Action chains)
    + [截图和录制](#Screenshot and recording)
    + [浏览器启动设置](#Browser startup settings)
* [WebPage](#WebPage)
    + [介绍](#intro)
    + [创建页面对象](#create page obj)
    + [模式切换](#Mode switching)
    + [独有功能](#Exclusive features)
* [查找元素](#Find element)
    + [介绍](#intro)
    + [基本用法](#Basic Usage)
    + [更多用法](#More Usages)
    + [简化写法](#Simplified)
    + [元素未找到时](#When Element Not Found)
    + [语法速查表](#Syntax Quick Reference Table)
* [下载文件](#Download file)
    + [介绍](#intro)
    + [DownloadKit](#DownloadKit)
    + [下载](#downloads)
* [高级用法](#Advanced usage)
    + [配置文件用法](#Usage of Configuration Files)
    + [全局设置](#Global Settings)
    + [CMD 用法](#CMD Usage)
    + [使用异常](#Usage Exceptions)
    + [加速数据读取](#Accelerated Data Reading)
    + [程序打包](#Packaging the Program)
    + [小工具](#Small Tools)
