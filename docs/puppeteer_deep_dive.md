# 🎭 Puppeteer 深度分析文档

## 📋 目录

1. [Puppeteer 简介](#puppeteer-简介)
2. [核心概念与架构](#核心概念与架构)
3. [安装与配置](#安装与配置)
4. [核心 API 详解](#核心-api-详解)
5. [高级功能](#高级功能)
6. [性能优化](#性能优化)
7. [最佳实践](#最佳实践)
8. [调试技巧](#调试技巧)
9. [常见问题与解决方案](#常见问题与解决方案)
10. [实战案例](#实战案例)
11. [与其他工具对比](#与其他工具对比)

---

## Puppeteer 简介

### 🎯 什么是 Puppeteer？

**Puppeteer** 是由 **Google Chrome 团队**开发和维护的 Node.js 库，提供了一套高级 API 来控制 Chrome/Chromium 浏览器。

**核心特点**：
- 🏢 **官方出品**：Google Chrome DevTools 团队维护
- 🚀 **功能强大**：基于 Chrome DevTools Protocol (CDP)
- 📦 **开箱即用**：自动下载配套的 Chromium
- 🎭 **无头模式**：默认无头运行，也支持有头模式
- 🔥 **生态成熟**：GitHub 87k+ Stars

### 📊 Puppeteer 基本信息

| 项目 | 信息 |
|------|------|
| **开发者** | Google Chrome Team |
| **首次发布** | 2017 年 8 月 |
| **编程语言** | JavaScript/TypeScript |
| **运行环境** | Node.js 14+ |
| **许可证** | Apache-2.0 |
| **GitHub** | https://github.com/puppeteer/puppeteer |
| **官方文档** | https://pptr.dev |
| **NPM 周下载** | 3M+ |

### 🌟 主要功能

1. **页面自动化**
   - 模拟用户操作（点击、输入、滚动等）
   - 表单填写和提交
   - 键盘和鼠标事件

2. **内容提取**
   - 抓取动态网页内容
   - 提取 DOM 元素
   - 执行 JavaScript 获取数据

3. **截图和 PDF**
   - 生成页面截图（PNG、JPEG）
   - 导出 PDF 文档
   - 支持全页截图

4. **性能分析**
   - 记录页面加载时间
   - 分析网络请求
   - CPU 和内存分析

5. **自动化测试**
   - E2E 测试
   - UI 回归测试
   - 集成测试

6. **网络控制**
   - 拦截和修改请求
   - 模拟网络条件
   - 缓存控制

### 🎯 典型应用场景

| 场景 | 描述 | 适用性 |
|------|------|--------|
| **Web 爬虫** | 抓取动态渲染的 SPA 页面 | ⭐⭐⭐⭐⭐ |
| **自动化测试** | E2E 测试、回归测试 | ⭐⭐⭐⭐⭐ |
| **性能监控** | 页面性能分析和监控 | ⭐⭐⭐⭐⭐ |
| **截图服务** | 生成网页截图和 PDF | ⭐⭐⭐⭐⭐ |
| **预渲染** | SSR 服务端渲染 | ⭐⭐⭐⭐ |
| **自动化办公** | 填表、数据录入 | ⭐⭐⭐⭐ |
| **爬虫反检测** | 绕过反爬虫机制 | ⭐⭐⭐ |

---

## 核心概念与架构

### 🏗️ Puppeteer 架构图

```
┌─────────────────────────────────────────────────┐
│           Node.js 应用程序                        │
│  ┌───────────────────────────────────────────┐  │
│  │         Puppeteer API                      │  │
│  │  ┌──────────┬──────────┬──────────────┐   │  │
│  │  │ Browser  │  Page    │  ElementHandle│   │  │
│  │  └────┬─────┴────┬─────┴──────┬───────┘   │  │
│  └───────┼──────────┼────────────┼───────────┘  │
└──────────┼──────────┼────────────┼──────────────┘
           │          │            │
           ▼          ▼            ▼
    ┌─────────────────────────────────────┐
    │   Chrome DevTools Protocol (CDP)    │
    │        WebSocket 连接                │
    └──────────────┬──────────────────────┘
                   │
                   ▼
    ┌─────────────────────────────────────┐
    │      Chrome/Chromium 浏览器          │
    │  ┌───────────────────────────────┐  │
    │  │    渲染引擎 (Blink)            │  │
    │  │    JavaScript 引擎 (V8)        │  │
    │  │    网络层 (Network)            │  │
    │  └───────────────────────────────┘  │
    └─────────────────────────────────────┘
```

### 🔑 核心类和概念

#### 1. Browser（浏览器实例）

**作用**：代表一个浏览器进程

```javascript
const browser = await puppeteer.launch({
    headless: true,        // 无头模式
    defaultViewport: {     // 默认视口
        width: 1920,
        height: 1080
    }
});

// 获取浏览器信息
console.log(await browser.version());  // Chrome/111.0.5563.0
console.log(browser.wsEndpoint());     // WebSocket 地址

// 关闭浏览器
await browser.close();
```

**主要方法**：
- `newPage()`: 创建新页面
- `pages()`: 获取所有页面
- `close()`: 关闭浏览器
- `disconnect()`: 断开连接但不关闭
- `targets()`: 获取所有目标（页面、worker 等）

#### 2. BrowserContext（浏览器上下文）

**作用**：隔离的浏览器会话（类似隐身模式）

```javascript
// 创建隔离的上下文
const context = await browser.createIncognitoBrowserContext();
const page = await context.newPage();

// 设置 cookies
await context.setCookie({
    name: 'session',
    value: 'abc123',
    domain: 'example.com'
});

// 清理
await context.close();
```

**应用场景**：
- 多账号登录
- 测试隔离
- Cookie 隔离

#### 3. Page（页面）

**作用**：代表一个标签页

```javascript
const page = await browser.newPage();

// 导航
await page.goto('https://example.com');

// 获取内容
const title = await page.title();
const html = await page.content();

// 执行 JavaScript
const result = await page.evaluate(() => {
    return document.querySelector('h1').textContent;
});

// 截图
await page.screenshot({ path: 'page.png' });
```

**生命周期**：
```
created → initialized → loaded → interactive → complete
```

#### 4. Frame（框架）

**作用**：代表页面中的 iframe

```javascript
// 获取主框架
const mainFrame = page.mainFrame();

// 获取所有框架
const frames = page.frames();

// 在框架中查找元素
for (const frame of frames) {
    const element = await frame.$('#target');
    if (element) {
        await element.click();
    }
}
```

#### 5. ElementHandle（元素句柄）

**作用**：代表 DOM 元素的引用

```javascript
// 获取元素
const button = await page.$('#submit-btn');

// 元素操作
await button.click();
await button.type('text');
await button.focus();

// 获取属性
const className = await button.getProperty('className');
const value = await className.jsonValue();

// 截图元素
await button.screenshot({ path: 'button.png' });
```

#### 6. JSHandle（JavaScript 句柄）

**作用**：代表 JavaScript 对象的引用

```javascript
// 在页面上下文中执行
const jsHandle = await page.evaluateHandle(() => {
    return { foo: 'bar', count: 42 };
});

// 获取属性
const fooHandle = await jsHandle.getProperty('foo');
const fooValue = await fooHandle.jsonValue();
console.log(fooValue); // 'bar'
```

### 🔄 Puppeteer 工作流程

```
1. 启动浏览器
   puppeteer.launch()
   ↓
2. 建立 WebSocket 连接
   CDP 协议连接
   ↓
3. 创建页面
   browser.newPage()
   ↓
4. 发送 CDP 命令
   Page.navigate, DOM.querySelector 等
   ↓
5. 接收 CDP 事件
   Page.loadEventFired, Network.requestWillBeSent 等
   ↓
6. 返回结果给用户
   API Promise 解析
```

### 📡 CDP 通信机制

Puppeteer 底层使用 Chrome DevTools Protocol：

```javascript
// 原始 CDP 命令（不推荐直接使用）
const client = await page.target().createCDPSession();
await client.send('Network.enable');
await client.send('Page.navigate', { url: 'https://example.com' });

// Puppeteer 封装后的 API（推荐）
await page.goto('https://example.com');
```

**CDP 消息类型**：
- **命令（Commands）**：发送给浏览器的指令
- **事件（Events）**：浏览器发送的通知
- **响应（Responses）**：命令的返回结果

---

## 安装与配置

### 📦 安装方式

#### 方式 1：标准安装（推荐）

```bash
npm install puppeteer
```

**特点**：
- ✅ 自动下载 Chromium（~300MB）
- ✅ 版本匹配，兼容性好
- ✅ 开箱即用

#### 方式 2：使用系统 Chrome

```bash
npm install puppeteer-core
```

```javascript
const puppeteer = require('puppeteer-core');

const browser = await puppeteer.launch({
    executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    // Linux: '/usr/bin/google-chrome'
    // Windows: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
});
```

**特点**：
- ✅ 不下载 Chromium，节省空间
- ⚠️ 需要手动指定浏览器路径
- ⚠️ 版本兼容性需要自己保证

#### 方式 3：Docker 安装

```dockerfile
FROM node:18-slim

# 安装 Chrome 依赖
RUN apt-get update && apt-get install -y \
    chromium \
    fonts-ipafont-gothic fonts-wqy-zenhei fonts-thai-tlwg fonts-kacst fonts-freefont-ttf \
    libxss1 \
    --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY package*.json ./
RUN npm ci

COPY . .

ENV PUPPETEER_SKIP_CHROMIUM_DOWNLOAD=true
ENV PUPPETEER_EXECUTABLE_PATH=/usr/bin/chromium

CMD ["node", "index.js"]
```

### ⚙️ 配置选项

#### Launch Options（启动选项）

```javascript
const browser = await puppeteer.launch({
    // === 基础配置 ===
    headless: 'new',             // 推荐使用新无头模式（'new' | true | false）
    executablePath: '/path',     // 浏览器路径
    protocol: 'cdp',             // 'cdp' | 'webDriverBiDi' (实验性)
    
    // === 性能配置 ===
    args: [
        '--no-sandbox',          // 禁用沙箱（Docker 需要）
        '--disable-setuid-sandbox',
        '--disable-dev-shm-usage', // 解决共享内存不足
        '--disable-accelerated-2d-canvas',
        '--no-first-run',
        '--no-zygote',
        '--disable-gpu',         // 禁用 GPU
    ],
    
    // === 代理配置 ===
    args: [
        '--proxy-server=http://proxy.com:8080'
    ],
    
    // === 窗口配置 ===
    defaultViewport: {
        width: 1920,
        height: 1080,
        deviceScaleFactor: 1,
        isMobile: false,
        hasTouch: false,
    },
    
    // === 调试配置 ===
    devtools: false,             // 自动打开 DevTools
    slowMo: 0,                   // 减慢操作（毫秒）
    dumpio: false,               // 打印浏览器日志
    
    // === 网络配置 ===
    ignoreHTTPSErrors: true,     // 忽略 HTTPS 错误
    
    // === 用户数据 ===
    userDataDir: './user-data',  // 用户数据目录
    
    // === 超时配置 ===
    timeout: 30000,              // 启动超时（毫秒）
    
    // === 环境配置 ===
    env: {
        TZ: 'Asia/Shanghai'      // 时区
    }
});
```

#### Page Options（页面选项）

```javascript
const page = await browser.newPage();

// 设置视口
await page.setViewport({
    width: 1920,
    height: 1080,
    deviceScaleFactor: 2,  // Retina 屏幕
});

// 设置 User-Agent
await page.setUserAgent('Mozilla/5.0...');

// 设置额外 HTTP 头
await page.setExtraHTTPHeaders({
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'
});

// 设置超时
page.setDefaultTimeout(30000);       // 默认超时
page.setDefaultNavigationTimeout(60000); // 导航超时

// 设置缓存
await page.setCacheEnabled(false);

// 设置 Cookie
await page.setCookie({
    name: 'session',
    value: 'abc123',
    domain: 'example.com',
    path: '/',
    expires: Date.now() / 1000 + 3600,
    httpOnly: true,
    secure: true,
    sameSite: 'Strict'
});
```

### 🔧 环境变量

```bash
# 跳过 Chromium 下载
export PUPPETEER_SKIP_CHROMIUM_DOWNLOAD=true

# 指定 Chromium 下载地址
export PUPPETEER_DOWNLOAD_HOST=https://npm.taobao.org/mirrors

# 指定可执行文件路径
export PUPPETEER_EXECUTABLE_PATH=/usr/bin/chromium

# 指定下载路径
export PUPPETEER_DOWNLOAD_PATH=/path/to/chromium

# 指定产品（chrome 或 firefox）
export PUPPETEER_PRODUCT=chrome
```

---

## 核心 API 详解

### 🚀 Browser API

#### 1. 启动和连接

```javascript
// 启动新浏览器
const browser = await puppeteer.launch(options);

// 连接已有浏览器
const browser = await puppeteer.connect({
    browserWSEndpoint: 'ws://127.0.0.1:9222/devtools/browser/...'
});

// 连接到 BrowserBase URL
const browser = await puppeteer.connect({
    browserURL: 'http://127.0.0.1:9222'
});
```

#### 2. 页面管理

```javascript
// 创建新页面
const page = await browser.newPage();

// 获取所有页面
const pages = await browser.pages();

// 等待目标创建（新页面）
const newPagePromise = new Promise(resolve => 
    browser.once('targetcreated', target => resolve(target.page()))
);
await someElement.click(); // 触发新页面
const newPage = await newPagePromise;
```

#### 3. 上下文管理

```javascript
// 创建隐身上下文
const context = await browser.createIncognitoBrowserContext();

// 获取默认上下文
const defaultContext = browser.defaultBrowserContext();

// 获取所有上下文
const contexts = browser.browserContexts();
```

### 📄 Page API

#### 1. 导航

```javascript
// 基础导航
await page.goto('https://example.com');

// 带选项的导航
await page.goto('https://example.com', {
    waitUntil: 'networkidle2',  // 或 'load', 'domcontentloaded', 'networkidle0'
    timeout: 30000
});

// 前进和后退
await page.goBack();
await page.goForward();

// 刷新
await page.reload({ waitUntil: 'networkidle0' });
```

**waitUntil 选项说明**：
- `load`: 等待 load 事件
- `domcontentloaded`: 等待 DOMContentLoaded 事件
- `networkidle0`: 网络空闲（0个连接）
- `networkidle2`: 网络空闲（≤2个连接）

#### 2. 选择器

```javascript
// 单个元素
const element = await page.$('#id');            // querySelector
const element = await page.$('div.class');

// 多个元素
const elements = await page.$$('li');           // querySelectorAll

// XPath
const elements = await page.$x('//button[@type="submit"]');

// 等待选择器
await page.waitForSelector('#target');
await page.waitForSelector('#target', {
    visible: true,    // 等待可见
    hidden: false,
    timeout: 5000
});

// 等待 XPath
await page.waitForXPath('//div[@class="loaded"]');
```

#### 3. 页面交互

```javascript
// 点击
await page.click('#button');
await page.click('#button', {
    button: 'right',   // 'left', 'right', 'middle'
    clickCount: 2,     // 双击
    delay: 100        // 按下和释放之间的延迟
});

// 输入
await page.type('#input', 'Hello World', { delay: 100 });

// 聚焦
await page.focus('#input');

// 悬停
await page.hover('#menu-item');

// 选择下拉框
await page.select('#country', 'US');
await page.select('#multi-select', 'value1', 'value2');

// 上传文件
const fileInput = await page.$('input[type="file"]');
await fileInput.uploadFile('/path/to/file.pdf');

// 键盘操作
await page.keyboard.press('Enter');
await page.keyboard.type('Hello');
await page.keyboard.down('Shift');
await page.keyboard.up('Shift');

// 鼠标操作
await page.mouse.move(100, 200);
await page.mouse.click(100, 200);
await page.mouse.down();
await page.mouse.up();

// 滚动
await page.evaluate(() => window.scrollTo(0, document.body.scrollHeight));
```

#### 4. 执行 JavaScript

```javascript
// 在页面上下文执行
const result = await page.evaluate(() => {
    return document.title;
});

// 传递参数
const result = await page.evaluate((x, y) => {
    return x + y;
}, 2, 3); // result = 5

// 使用 DOM 元素
const bodyHandle = await page.$('body');
const result = await page.evaluate(body => {
    return body.innerHTML;
}, bodyHandle);

// 获取句柄
const jsHandle = await page.evaluateHandle(() => document);
const element = jsHandle.asElement();
```

#### 5. 等待

```javascript
// 等待导航
await page.waitForNavigation({ waitUntil: 'networkidle0' });

// 等待函数
await page.waitForFunction(() => {
    return document.querySelector('#loaded') !== null;
}, { timeout: 5000 });

// 等待超时
await page.waitForTimeout(1000);  // 不推荐

// 等待请求
const request = await page.waitForRequest('https://api.example.com/data');

// 等待响应
const response = await page.waitForResponse('https://api.example.com/data');
const response = await page.waitForResponse(res => 
    res.url().includes('/api/') && res.status() === 200
);
```

#### 6. 截图和 PDF

```javascript
// 截图
await page.screenshot({
    path: 'screenshot.png',
    type: 'png',        // 'png' | 'jpeg' | 'webp'
    quality: 80,        // 仅 jpeg/webp
    fullPage: true,     // 全页截图
    clip: {             // 截取区域
        x: 0,
        y: 0,
        width: 800,
        height: 600
    },
    omitBackground: true // 透明背景
});

// 元素截图
const element = await page.$('#target');
await element.screenshot({ path: 'element.png' });

// PDF
await page.pdf({
    path: 'page.pdf',
    format: 'A4',       // 或指定 width/height
    printBackground: true,
    margin: {
        top: '20px',
        right: '20px',
        bottom: '20px',
        left: '20px'
    },
    displayHeaderFooter: true,
    headerTemplate: '<div style="font-size:10px;">Header</div>',
    footerTemplate: '<div style="font-size:10px;">Page <span class="pageNumber"></span></div>'
});
```

#### 7. 网络拦截

```javascript
// 启用拦截
await page.setRequestInterception(true);

// 拦截请求
page.on('request', async (request) => {
    // 阻止图片
    if (request.resourceType() === 'image') {
        request.abort();
    }
    // 修改请求
    else if (request.url().includes('/api/')) {
        request.continue({
            headers: {
                ...request.headers(),
                'Authorization': 'Bearer token'
            }
        });
    }
    // 返回模拟数据
    else if (request.url() === 'https://api.example.com/data') {
        request.respond({
            status: 200,
            contentType: 'application/json',
            body: JSON.stringify({ data: 'mocked' })
        });
    }
    // 继续请求
    else {
        request.continue();
    }
});

// 监听响应
page.on('response', async (response) => {
    console.log(response.url(), response.status());
    if (response.url().includes('/api/')) {
        const data = await response.json();
        console.log(data);
    }
});

// 监听请求失败
page.on('requestfailed', request => {
    console.log(request.url(), request.failure().errorText);
});
```

#### 8. 性能监控

```javascript
// 性能指标
const metrics = await page.metrics();
console.log(metrics);
/*
{
  Timestamp: 123456.789,
  Documents: 1,
  Frames: 1,
  JSEventListeners: 10,
  Nodes: 100,
  LayoutCount: 5,
  RecalcStyleCount: 5,
  LayoutDuration: 0.1,
  RecalcStyleDuration: 0.05,
  ScriptDuration: 0.2,
  TaskDuration: 0.5,
  JSHeapUsedSize: 10000000,
  JSHeapTotalSize: 20000000
}
*/

// 追踪
await page.tracing.start({ path: 'trace.json', screenshots: true });
await page.goto('https://example.com');
await page.tracing.stop();

// 覆盖率
await Promise.all([
    page.coverage.startJSCoverage(),
    page.coverage.startCSSCoverage()
]);
await page.goto('https://example.com');
const [jsCoverage, cssCoverage] = await Promise.all([
    page.coverage.stopJSCoverage(),
    page.coverage.stopCSSCoverage()
]);

// 性能时间轴
const performanceTiming = JSON.parse(
    await page.evaluate(() => JSON.stringify(window.performance.timing))
);
console.log('Page load time:', performanceTiming.loadEventEnd - performanceTiming.navigationStart);
```

### 🎯 ElementHandle API

```javascript
const element = await page.$('#button');

// 点击
await element.click();

// 获取属性
const id = await element.getProperty('id');
const value = await id.jsonValue();

// 执行 evaluate
const text = await element.evaluate(el => el.textContent);

// 获取边界框
const box = await element.boundingBox();
console.log(box); // { x, y, width, height }

// 截图
await element.screenshot({ path: 'element.png' });

// 滚动到视图
await element.scrollIntoView();

// 检查可见性
const isVisible = await element.isIntersectingViewport();

// 拖拽
await element.drag('#target');
await element.drop();
```

---

## 高级功能

### 🔌 扩展程序测试

```javascript
const browser = await puppeteer.launch({
    headless: false,
    args: [
        `--disable-extensions-except=/path/to/extension`,
        `--load-extension=/path/to/extension`
    ]
});
```

### 📱 移动设备模拟

```javascript
const puppeteer = require('puppeteer');
const devices = puppeteer.KnownDevices;

// 使用预定义设备（新 API）
const iPhone = devices['iPhone 13 Pro'];
await page.emulate(iPhone);

// 自定义设备
await page.emulate({
    name: 'Custom Device',
    userAgent: 'Mozilla/5.0...',
    viewport: {
        width: 375,
        height: 812,
        deviceScaleFactor: 3,
        isMobile: true,
        hasTouch: true,
        isLandscape: false
    }
});

// 地理位置
await page.setGeolocation({
    latitude: 37.7749,
    longitude: -122.4194
});
```

### 🌐 网络条件模拟

```javascript
// 模拟慢网络
const client = await page.target().createCDPSession();
await client.send('Network.emulateNetworkConditions', {
    offline: false,
    downloadThroughput: 500 * 1024 / 8,  // 500kb/s
    uploadThroughput: 500 * 1024 / 8,
    latency: 400  // ms
});

// 离线模式
await page.setOfflineMode(true);
```

### 🍪 Cookie 管理

```javascript
// 设置 Cookie
await page.setCookie(
    { name: 'session', value: 'abc123', domain: 'example.com' },
    { name: 'token', value: 'xyz789', domain: 'example.com' }
);

// 获取 Cookie
const cookies = await page.cookies();
const cookies = await page.cookies('https://example.com');

// 删除 Cookie
await page.deleteCookie({ name: 'session', domain: 'example.com' });

// 清除所有 Cookie
const cookies = await page.cookies();
await page.deleteCookie(...cookies);
```

### 🎬 录屏

Puppeteer 本身不支持录屏，但可以配合其他库：

```javascript
// 使用 puppeteer-screen-recorder
const { PuppeteerScreenRecorder } = require('puppeteer-screen-recorder');

const recorder = new PuppeteerScreenRecorder(page);
await recorder.start('./recording.mp4');

// 进行操作...
await page.goto('https://example.com');

await recorder.stop();
```

### 🔐 认证处理

```javascript
// HTTP 基本认证
await page.authenticate({
    username: 'user',
    password: 'pass'
});

// 弹窗认证
page.on('dialog', async dialog => {
    console.log(dialog.message());
    await dialog.accept('input value');
    // await dialog.dismiss();
});
```

---

## 性能优化

### ⚡ 启动优化

```javascript
const browser = await puppeteer.launch({
    // 禁用不需要的功能
    args: [
        '--disable-gpu',
        '--disable-dev-shm-usage',
        '--disable-setuid-sandbox',
        '--no-first-run',
        '--no-sandbox',
        '--no-zygote',
        '--single-process',  // 单进程模式（谨慎使用）
        '--disable-extensions',
        '--disable-background-timer-throttling',
        '--disable-backgrounding-occluded-windows',
        '--disable-renderer-backgrounding'
    ]
});
```

### 🚫 资源过滤

```javascript
await page.setRequestInterception(true);

page.on('request', (req) => {
    const resourceType = req.resourceType();
    const url = req.url();
    
    // 阻止不需要的资源
    if (['image', 'stylesheet', 'font', 'media'].includes(resourceType)) {
        req.abort();
    }
    // 阻止第三方脚本
    else if (resourceType === 'script' && !url.includes('example.com')) {
        req.abort();
    }
    else {
        req.continue();
    }
});
```

### 🔄 浏览器复用

```javascript
// 不好的做法：每次都启动新浏览器
for (let i = 0; i < 100; i++) {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    // ...
    await browser.close();
}

// 好的做法：复用浏览器
const browser = await puppeteer.launch();
for (let i = 0; i < 100; i++) {
    const page = await browser.newPage();
    // ...
    await page.close();
}
await browser.close();

// 更好的做法：页面池
class PagePool {
    constructor(browser, size = 5) {
        this.browser = browser;
        this.size = size;
        this.pages = [];
        this.available = [];
    }
    
    async init() {
        for (let i = 0; i < this.size; i++) {
            const page = await this.browser.newPage();
            this.pages.push(page);
            this.available.push(page);
        }
    }
    
    async acquire() {
        while (this.available.length === 0) {
            await new Promise(resolve => setTimeout(resolve, 100));
        }
        return this.available.shift();
    }
    
    release(page) {
        this.available.push(page);
    }
    
    async destroy() {
        await Promise.all(this.pages.map(p => p.close()));
    }
}
```

### 💾 内存优化

```javascript
// 及时关闭页面
const page = await browser.newPage();
try {
    await page.goto('https://example.com');
    // ...
} finally {
    await page.close();  // 确保关闭
}

// 清理大对象
await page.evaluate(() => {
    // 清理页面内存
    if (window.gc) {
        window.gc();
    }
});

// 限制并发
const pLimit = require('p-limit');
const limit = pLimit(5);  // 最多 5 个并发

const promises = urls.map(url => 
    limit(() => processPage(url))
);
await Promise.all(promises);
```

### 📊 性能监控

```javascript
async function measurePageLoad(page, url) {
    const start = Date.now();
    
    await page.goto(url, { waitUntil: 'networkidle2' });
    
    const metrics = await page.evaluate(() => {
        const timing = performance.timing;
        return {
            dns: timing.domainLookupEnd - timing.domainLookupStart,
            tcp: timing.connectEnd - timing.connectStart,
            ttfb: timing.responseStart - timing.requestStart,
            download: timing.responseEnd - timing.responseStart,
            domInteractive: timing.domInteractive - timing.navigationStart,
            domComplete: timing.domComplete - timing.navigationStart,
            loadComplete: timing.loadEventEnd - timing.navigationStart
        };
    });
    
    const totalTime = Date.now() - start;
    
    return { ...metrics, totalTime };
}
```

---

## 最佳实践

### ✅ 错误处理

```javascript
// 1. 使用 try-catch
async function safeScrape(url) {
    const browser = await puppeteer.launch();
    let page;
    
    try {
        page = await browser.newPage();
        await page.goto(url, { timeout: 30000 });
        const data = await page.evaluate(() => /* ... */);
        return data;
    } catch (error) {
        console.error(`Error scraping ${url}:`, error.message);
        // 截图保存错误状态
        if (page) {
            await page.screenshot({ path: 'error.png' });
        }
        throw error;
    } finally {
        if (page) await page.close();
        await browser.close();
    }
}

// 2. 超时处理
await page.goto(url, { 
    timeout: 30000,
    waitUntil: 'networkidle2' 
}).catch(err => {
    console.error('Navigation timeout:', err);
});

// 3. 元素存在性检查
const button = await page.$('#submit');
if (button) {
    await button.click();
} else {
    console.warn('Button not found');
}

// 4. 等待元素with默认值
try {
    await page.waitForSelector('#element', { timeout: 5000 });
} catch {
    console.log('Element not found, using default behavior');
}
```

### 🔒 安全实践

```javascript
// 1. 输入验证
function isValidURL(url) {
    try {
        const parsed = new URL(url);
        return ['http:', 'https:'].includes(parsed.protocol);
    } catch {
        return false;
    }
}

// 2. 沙箱模式
const browser = await puppeteer.launch({
    args: ['--no-sandbox']  // 仅在必要时使用
});

// 3. 限制页面权限
await page.setJavaScriptEnabled(false);  // 禁用 JS
await page.setBypassCSP(false);  // 不绕过 CSP

// 4. 清理敏感数据
await page.evaluate(() => {
    localStorage.clear();
    sessionStorage.clear();
});
```

### 📝 代码组织

```javascript
// 使用 Page Object 模式
class LoginPage {
    constructor(page) {
        this.page = page;
        this.usernameInput = '#username';
        this.passwordInput = '#password';
        this.loginButton = '#login-btn';
    }
    
    async navigate() {
        await this.page.goto('https://example.com/login');
    }
    
    async login(username, password) {
        await this.page.type(this.usernameInput, username);
        await this.page.type(this.passwordInput, password);
        await this.page.click(this.loginButton);
        await this.page.waitForNavigation();
    }
}

// 使用
const loginPage = new LoginPage(page);
await loginPage.navigate();
await loginPage.login('user', 'pass');
```

### 🎯 等待策略

```javascript
// 1. 等待特定条件
await page.waitForFunction(() => {
    const el = document.querySelector('#data');
    return el && el.textContent.length > 0;
});

// 2. 组合等待
await Promise.all([
    page.waitForNavigation(),
    page.click('#submit')
]);

// 3. 竞态等待
await Promise.race([
    page.waitForSelector('#success'),
    page.waitForSelector('#error')
]);

// 4. 自定义等待助手
async function waitForText(page, selector, text, timeout = 5000) {
    await page.waitForFunction(
        (selector, text) => {
            const el = document.querySelector(selector);
            return el && el.textContent.includes(text);
        },
        { timeout },
        selector,
        text
    );
}
```

---

## 调试技巧

### 🐛 开发环境调试

```javascript
// 1. 有头模式 + 慢动作
const browser = await puppeteer.launch({
    headless: false,
    slowMo: 50,  // 每个操作延迟 50ms
    devtools: true  // 自动打开 DevTools
});

// 2. 保持浏览器打开
const browser = await puppeteer.launch({
    headless: false,
    devtools: true
});

// 不关闭浏览器
// await browser.close();  // 注释掉

// 3. 调试特定步骤
await page.evaluate(() => debugger);  // 在浏览器中触发断点

// 4. 截图调试
await page.screenshot({ path: 'debug-1.png' });
await page.click('#button');
await page.screenshot({ path: 'debug-2.png' });
```

### 📋 日志记录

```javascript
// 1. 监听控制台
page.on('console', msg => {
    console.log('PAGE LOG:', msg.text());
});

// 2. 监听页面错误
page.on('pageerror', error => {
    console.error('PAGE ERROR:', error.message);
});

// 3. 监听请求
page.on('request', request => {
    console.log('>', request.method(), request.url());
});

page.on('response', response => {
    console.log('<', response.status(), response.url());
});

// 4. 详细日志
const browser = await puppeteer.launch({
    dumpio: true  // 打印浏览器进程的 stdout 和 stderr
});
```

### 🔍 网络调试

```javascript
// 使用 chrome://inspect
console.log('Open chrome://inspect in Chrome');
console.log('WebSocket URL:', browser.wsEndpoint());

// 暂停执行以便手动检查
await new Promise(resolve => setTimeout(resolve, 60000));
```

### 📊 性能分析

```javascript
// 生成追踪文件
await page.tracing.start({ 
    path: 'trace.json',
    screenshots: true,
    categories: ['devtools.timeline']
});

await page.goto('https://example.com');

await page.tracing.stop();
// 在 chrome://tracing 中打开 trace.json
```

---

## 常见问题与解决方案

### ❌ 常见错误

#### 1. 超时错误

```
Error: Navigation timeout of 30000 ms exceeded
```

**解决方案**：
```javascript
// 增加超时时间
await page.goto(url, { timeout: 60000 });

// 或改变等待策略
await page.goto(url, { waitUntil: 'domcontentloaded' });

// 或分步等待
await page.goto(url, { waitUntil: 'load' });
await page.waitForSelector('#loaded', { timeout: 10000 });
```

#### 2. 元素不可点击

```
Error: Node is either not visible or not an HTMLElement
```

**解决方案**：
```javascript
// 等待元素可见
await page.waitForSelector('#button', { visible: true });

// 滚动到视图
const element = await page.$('#button');
await element.scrollIntoView();
await element.click();

// 使用 JavaScript 点击
await page.$eval('#button', el => el.click());
```

#### 3. 内存泄漏

**解决方案**：
```javascript
// 及时关闭页面
for (const url of urls) {
    const page = await browser.newPage();
    try {
        await page.goto(url);
        // 处理...
    } finally {
        await page.close();  // 重要！
    }
}

// 限制并发数
const limit = pLimit(5);
```

#### 4. Chromium 下载失败

**解决方案**：
```bash
# 使用国内镜像
npm config set puppeteer_download_host=https://npm.taobao.org/mirrors

# 或跳过下载，使用系统 Chrome
npm install puppeteer-core
```

### 🔧 疑难杂症

#### 1. Docker 中运行失败

```javascript
const browser = await puppeteer.launch({
    args: [
        '--no-sandbox',
        '--disable-setuid-sandbox',
        '--disable-dev-shm-usage'  // 共享内存不足
    ]
});
```

#### 2. 检测 Puppeteer

某些网站会检测 Puppeteer，解决方案：

```javascript
// 隐藏 webdriver 特征
await page.evaluateOnNewDocument(() => {
    Object.defineProperty(navigator, 'webdriver', {
        get: () => false
    });
});

// 使用 puppeteer-extra + stealth 插件
const puppeteer = require('puppeteer-extra');
const StealthPlugin = require('puppeteer-extra-plugin-stealth');
puppeteer.use(StealthPlugin());

const browser = await puppeteer.launch();
```

#### 3. 中文乱码

```javascript
await page.setExtraHTTPHeaders({
    'Accept-Language': 'zh-CN,zh;q=0.9'
});

// PDF 中文字体
await page.pdf({
    path: 'output.pdf',
    format: 'A4',
    printBackground: true,
    // 确保系统有中文字体
});
```

---

## 实战案例

### 📰 案例 1：新闻网站爬虫

```javascript
const puppeteer = require('puppeteer');

async function scrapeNews(url) {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    
    // 阻止图片加载以提高速度
    await page.setRequestInterception(true);
    page.on('request', req => {
        req.resourceType() === 'image' ? req.abort() : req.continue();
    });
    
    await page.goto(url, { waitUntil: 'networkidle2' });
    
    // 提取新闻列表
    const news = await page.evaluate(() => {
        return Array.from(document.querySelectorAll('.news-item')).map(item => ({
            title: item.querySelector('.title')?.textContent.trim(),
            summary: item.querySelector('.summary')?.textContent.trim(),
            link: item.querySelector('a')?.href,
            date: item.querySelector('.date')?.textContent.trim()
        }));
    });
    
    await browser.close();
    return news;
}

// 使用
scrapeNews('https://news.example.com')
    .then(news => console.log(news))
    .catch(err => console.error(err));
```

### 🔐 案例 2：自动登录

```javascript
async function autoLogin(username, password) {
    const browser = await puppeteer.launch({ headless: false });
    const page = await browser.newPage();
    
    // 导航到登录页
    await page.goto('https://example.com/login');
    
    // 填写表单
    await page.type('#username', username, { delay: 50 });
    await page.type('#password', password, { delay: 50 });
    
    // 处理验证码（假设是图片验证码）
    const captchaImage = await page.$('#captcha-image');
    await captchaImage.screenshot({ path: 'captcha.png' });
    
    // 这里可以集成 OCR 或人工输入
    const captchaText = await getCaptchaText('captcha.png');
    await page.type('#captcha', captchaText);
    
    // 点击登录
    await Promise.all([
        page.waitForNavigation({ waitUntil: 'networkidle0' }),
        page.click('#login-btn')
    ]);
    
    // 保存登录状态（Cookies）
    const cookies = await page.cookies();
    require('fs').writeFileSync('cookies.json', JSON.stringify(cookies));
    
    return browser;
}
```

### 📸 案例 3：批量截图服务

```javascript
const express = require('express');
const puppeteer = require('puppeteer');

const app = express();
let browser;

// 初始化浏览器
(async () => {
    browser = await puppeteer.launch({
        headless: true,
        args: ['--no-sandbox']
    });
})();

// 截图接口
app.get('/screenshot', async (req, res) => {
    const { url, width = 1920, height = 1080 } = req.query;
    
    if (!url) {
        return res.status(400).json({ error: 'URL is required' });
    }
    
    try {
        const page = await browser.newPage();
        await page.setViewport({ width: parseInt(width), height: parseInt(height) });
        await page.goto(url, { waitUntil: 'networkidle2', timeout: 30000 });
        
        const screenshot = await page.screenshot({ 
            type: 'png',
            fullPage: false
        });
        
        await page.close();
        
        res.contentType('image/png');
        res.send(screenshot);
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

app.listen(3000, () => {
    console.log('Screenshot service running on http://localhost:3000');
});

// 优雅关闭
process.on('SIGINT', async () => {
    await browser.close();
    process.exit();
});
```

### 🧪 案例 4：E2E 测试

```javascript
const puppeteer = require('puppeteer');
const assert = require('assert');

describe('User Login Flow', () => {
    let browser, page;
    
    before(async () => {
        browser = await puppeteer.launch();
        page = await browser.newPage();
    });
    
    after(async () => {
        await browser.close();
    });
    
    it('should load login page', async () => {
        await page.goto('https://example.com/login');
        const title = await page.title();
        assert.strictEqual(title, 'Login - Example');
    });
    
    it('should show error for invalid credentials', async () => {
        await page.type('#username', 'invalid');
        await page.type('#password', 'wrong');
        await page.click('#login-btn');
        
        await page.waitForSelector('.error-message', { visible: true });
        const errorText = await page.$eval('.error-message', el => el.textContent);
        assert(errorText.includes('Invalid credentials'));
    });
    
    it('should login successfully with valid credentials', async () => {
        await page.goto('https://example.com/login');
        await page.type('#username', 'testuser');
        await page.type('#password', 'testpass');
        
        await Promise.all([
            page.waitForNavigation({ waitUntil: 'networkidle0' }),
            page.click('#login-btn')
        ]);
        
        const url = page.url();
        assert(url.includes('/dashboard'));
    });
});
```

### 📊 案例 5：性能监控

```javascript
async function performanceAudit(url) {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    
    // 启动追踪
    await page.tracing.start({ path: 'trace.json' });
    
    // 记录网络请求
    const requests = [];
    page.on('request', req => {
        requests.push({
            url: req.url(),
            resourceType: req.resourceType(),
            startTime: Date.now()
        });
    });
    
    page.on('response', res => {
        const req = requests.find(r => r.url === res.url());
        if (req) {
            req.endTime = Date.now();
            req.status = res.status();
            req.size = res.headers()['content-length'];
        }
    });
    
    // 导航并测量
    const startTime = Date.now();
    await page.goto(url, { waitUntil: 'networkidle2' });
    const loadTime = Date.now() - startTime;
    
    // 获取性能指标
    const metrics = await page.metrics();
    const performanceTiming = JSON.parse(
        await page.evaluate(() => JSON.stringify(window.performance.timing))
    );
    
    // 停止追踪
    await page.tracing.stop();
    
    await browser.close();
    
    return {
        url,
        loadTime,
        metrics,
        performanceTiming,
        requests: requests.filter(r => r.endTime),
        totalRequests: requests.length,
        totalSize: requests.reduce((sum, r) => sum + parseInt(r.size || 0), 0)
    };
}

// 使用
performanceAudit('https://example.com')
    .then(report => {
        console.log('Load Time:', report.loadTime, 'ms');
        console.log('Total Requests:', report.totalRequests);
        console.log('Total Size:', (report.totalSize / 1024).toFixed(2), 'KB');
        console.log('JS Heap Size:', (report.metrics.JSHeapUsedSize / 1024 / 1024).toFixed(2), 'MB');
    });
```

---

## 与其他工具对比

### 🆚 Puppeteer vs Selenium

| 特性 | Puppeteer | Selenium |
|------|-----------|----------|
| **维护者** | Google | OpenQA |
| **支持浏览器** | Chrome/Chromium | Chrome/Firefox/Safari/Edge |
| **编程语言** | JavaScript/TypeScript | 多语言 |
| **性能** | 快（原生 CDP）| 较慢（WebDriver）|
| **安装复杂度** | 简单 | 复杂（需要 driver）|
| **API 设计** | 现代（Promise/async）| 传统（同步风格）|
| **文档** | 优秀 | 一般 |
| **社区** | 活跃 | 非常活跃 |
| **调试** | 容易 | 较难 |
| **最佳用途** | Chrome 自动化、爬虫 | 跨浏览器测试 |

### 🆚 Puppeteer vs Playwright

| 特性 | Puppeteer | Playwright |
|------|-----------|------------|
| **维护者** | Google | Microsoft |
| **支持浏览器** | Chrome/Chromium | Chrome/Firefox/WebKit |
| **多浏览器** | ❌ | ✅ |
| **自动等待** | 需手动 | 内置 |
| **网络拦截** | 复杂 | 简单 |
| **移动模拟** | 支持 | 更好支持 |
| **多 Tab** | 支持 | 更好支持 |
| **学习曲线** | 较低 | 中等 |
| **生态** | 更成熟 | 快速发展 |
| **最佳用途** | Chrome 专项 | 跨浏览器测试 |

### 🆚 Puppeteer vs DrissionPage

| 特性 | Puppeteer | DrissionPage |
|------|-----------|--------------|
| **语言** | JavaScript | Python |
| **官方支持** | ✅ Google | ❌ 社区 |
| **上手难度** | 中等 | 简单 |
| **代码简洁** | 中等 | 非常简洁 |
| **性能** | 优秀 | 良好 |
| **并发** | 原生异步 | 多标签页 |
| **数据处理** | 需其他库 | Pandas 集成 |
| **中文文档** | 一般 | 优秀 |
| **最佳用途** | 企业级应用 | 快速开发 |

---

## Puppeteer 新特性（2024-2025）

### 🆕 Chrome Headless 新模式

从 Puppeteer 19.0 开始，引入了新的 Headless 模式，提供更好的性能和兼容性：

```javascript
// 旧的 headless 模式（逐渐废弃）
const browser = await puppeteer.launch({ headless: true });

// 新的 headless 模式（推荐）
const browser = await puppeteer.launch({ headless: 'new' });

// 有头模式
const browser = await puppeteer.launch({ headless: false });
```

**新 Headless 模式优势**：
- ✅ 与有头模式行为完全一致
- ✅ 更好的 CSS 渲染
- ✅ 支持 Chrome Extensions
- ✅ 更少的 Bug 和兼容性问题
- ✅ 更接近真实浏览器

### 🦊 Firefox 支持（实验性）

Puppeteer 从 v23.0 开始实验性支持 Firefox：

```javascript
const puppeteer = require('puppeteer');

const browser = await puppeteer.launch({
    product: 'firefox',
    // Firefox 特定选项
    extraPrefsFirefox: {
        'browser.cache.disk.enable': false,
        'browser.cache.memory.enable': false
    }
});
```

**注意事项**：
- ⚠️ Firefox 支持仍处于实验阶段
- ⚠️ 某些 API 可能不可用
- ⚠️ 建议用于测试，不建议生产环境

### 🎯 WebDriver BiDi 支持（实验性）

新的 WebDriver BiDi 协议支持：

```javascript
const browser = await puppeteer.launch({
    protocol: 'webDriverBiDi',  // 实验性
    headless: 'new'
});
```

**WebDriver BiDi 优势**：
- 双向通信协议
- 更好的跨浏览器支持
- 更标准化的 API
- 与 W3C 标准兼容

### 📦 ESM 模块支持

Puppeteer 现在完全支持 ESM：

```javascript
// ESM 导入
import puppeteer from 'puppeteer';

// 动态导入
const { default: puppeteer } = await import('puppeteer');
const browser = await puppeteer.launch();
```

### 🎨 更好的 TypeScript 支持

```typescript
import puppeteer, { Browser, Page, ElementHandle } from 'puppeteer';

const browser: Browser = await puppeteer.launch();
const page: Page = await browser.newPage();

// 类型安全的选项
await page.goto('https://example.com', {
    waitUntil: 'networkidle0',  // 类型检查
    timeout: 30000
});

// 类型推导
const element: ElementHandle<HTMLButtonElement> | null = await page.$('#button');
```

---

## 常见误区与陷阱

### ❌ 误区 1：忘记关闭页面导致内存泄漏

```javascript
// ❌ 错误：会造成内存泄漏
for (let i = 0; i < 100; i++) {
    const page = await browser.newPage();
    await page.goto(`https://example.com/page${i}`);
    // 忘记关闭页面！
}

// ✅ 正确：确保关闭
for (let i = 0; i < 100; i++) {
    const page = await browser.newPage();
    try {
        await page.goto(`https://example.com/page${i}`);
        // 处理数据...
    } finally {
        await page.close();  // 确保关闭
    }
}
```

### ❌ 误区 2：并发数过高导致系统崩溃

```javascript
// ❌ 错误：可能导致系统资源耗尽
const promises = urls.map(url => scrapeUrl(url));
await Promise.all(promises);  // 如果 urls 有 1000 个...

// ✅ 正确：限制并发数
const pLimit = require('p-limit');
const limit = pLimit(10);  // 最多 10 个并发

const promises = urls.map(url => limit(() => scrapeUrl(url)));
await Promise.all(promises);
```

### ❌ 误区 3：等待固定时间不可靠

```javascript
// ❌ 错误：不可靠且浪费时间
await page.goto('https://example.com');
await page.waitForTimeout(5000);  // 盲等 5 秒

// ✅ 正确：等待特定条件
await page.goto('https://example.com');
await page.waitForSelector('#content', { visible: true });

// ✅ 更好：等待网络空闲
await page.goto('https://example.com', { waitUntil: 'networkidle2' });
```

### ❌ 误区 4：忽略错误处理

```javascript
// ❌ 错误：一个失败导致全部失败
const results = await Promise.all(
    urls.map(url => page.goto(url))
);

// ✅ 正确：独立处理错误
const results = await Promise.allSettled(
    urls.map(async url => {
        try {
            await page.goto(url);
            return { success: true, url };
        } catch (error) {
            return { success: false, url, error: error.message };
        }
    })
);

// 处理结果
results.forEach(result => {
    if (result.status === 'fulfilled' && result.value.success) {
        console.log('Success:', result.value.url);
    } else {
        console.error('Failed:', result.value.url, result.value.error);
    }
});
```

### ❌ 误区 5：在 evaluate 中访问外部变量

```javascript
// ❌ 错误：selector 在浏览器上下文中不可用
const selector = '#button';
await page.evaluate(() => {
    document.querySelector(selector).click();  // ReferenceError: selector is not defined
});

// ✅ 正确：传递参数
const selector = '#button';
await page.evaluate((sel) => {
    document.querySelector(sel).click();
}, selector);

// ✅ 也可以传递多个参数
const selector = '#input';
const value = 'Hello';
await page.evaluate((sel, val) => {
    document.querySelector(sel).value = val;
}, selector, value);
```

### ❌ 误区 6：混淆 page.$ 和 page.$$

```javascript
// ❌ 错误：$ 只返回第一个元素
const links = await page.$('a');  // 只得到一个元素
for (const link of links) {  // TypeError: links is not iterable
    // ...
}

// ✅ 正确：使用 $$ 获取所有元素
const links = await page.$$('a');
for (const link of links) {
    const href = await link.getProperty('href');
    console.log(await href.jsonValue());
}
```

---

## Puppeteer 生态系统

### 🔌 推荐插件

#### 1. puppeteer-extra-plugin-stealth

**用途**：绕过反爬虫检测

```javascript
const puppeteer = require('puppeteer-extra');
const StealthPlugin = require('puppeteer-extra-plugin-stealth');

puppeteer.use(StealthPlugin());

const browser = await puppeteer.launch({ headless: 'new' });
```

**特性**：
- ✅ 隐藏 `navigator.webdriver`
- ✅ 修改浏览器指纹
- ✅ 伪造 Chrome 对象
- ✅ 修改权限API
- ✅ 伪造插件列表

#### 2. puppeteer-extra-plugin-recaptcha

**用途**：自动解决 reCAPTCHA

```javascript
const RecaptchaPlugin = require('puppeteer-extra-plugin-recaptcha');

puppeteer.use(
    RecaptchaPlugin({
        provider: {
            id: '2captcha',
            token: 'YOUR_API_KEY'
        }
    })
);

// 使用
await page.goto('https://example.com');
await page.solveRecaptchas();  // 自动解决验证码
```

#### 3. puppeteer-cluster

**用途**：大规模并发管理

```javascript
const { Cluster } = require('puppeteer-cluster');

const cluster = await Cluster.launch({
    concurrency: Cluster.CONCURRENCY_CONTEXT,
    maxConcurrency: 5,
    puppeteerOptions: { headless: 'new' }
});

// 定义任务
await cluster.task(async ({ page, data: url }) => {
    await page.goto(url);
    const title = await page.title();
    return { url, title };
});

// 添加任务
cluster.queue('https://example1.com');
cluster.queue('https://example2.com');
cluster.queue('https://example3.com');

// 等待完成
await cluster.idle();
await cluster.close();
```

#### 4. puppeteer-screen-recorder

**用途**：录制浏览器操作

```javascript
const { PuppeteerScreenRecorder } = require('puppeteer-screen-recorder');

const recorder = new PuppeteerScreenRecorder(page, {
    followNewTab: true,
    fps: 25,
    videoFrame: {
        width: 1920,
        height: 1080
    },
    aspectRatio: '16:9'
});

await recorder.start('./recording.mp4');
// 进行操作...
await recorder.stop();
```

### 📚 常用工具库对比

| 工具 | 用途 | GitHub Stars | 更新频率 | 推荐度 |
|------|------|-------------|---------|--------|
| **puppeteer-extra** | 插件系统 | 6k+ | 高 | ⭐⭐⭐⭐⭐ |
| **puppeteer-cluster** | 并发管理 | 3k+ | 中 | ⭐⭐⭐⭐⭐ |
| **puppeteer-recorder** | 录制操作 | 2k+ | 低 | ⭐⭐⭐ |
| **puppeteer-har** | 生成 HAR 文件 | 500+ | 低 | ⭐⭐⭐⭐ |
| **puppeteer-screen-recorder** | 录屏 | 400+ | 中 | ⭐⭐⭐⭐ |
| **puppeteer-mass-screenshots** | 批量截图 | 300+ | 低 | ⭐⭐⭐ |

---

## 企业级应用指南

### 📈 监控和告警系统

```javascript
const puppeteer = require('puppeteer');
const prometheus = require('prom-client');

// Prometheus 指标
const register = new prometheus.Registry();

const pageLoadDuration = new prometheus.Histogram({
    name: 'puppeteer_page_load_duration_seconds',
    help: 'Page load duration in seconds',
    buckets: [0.1, 0.5, 1, 2, 5, 10],
    registers: [register]
});

const errorCounter = new prometheus.Counter({
    name: 'puppeteer_errors_total',
    help: 'Total number of errors',
    labelNames: ['type', 'url'],
    registers: [register]
});

const activePages = new prometheus.Gauge({
    name: 'puppeteer_active_pages',
    help: 'Number of active pages',
    registers: [register]
});

// 监控包装函数
async function monitoredScrape(url) {
    const end = pageLoadDuration.startTimer();
    activePages.inc();
    
    try {
        const browser = await puppeteer.launch();
        const page = await browser.newPage();
        
        await page.goto(url, { timeout: 30000 });
        const data = await page.evaluate(() => document.title);
        
        await browser.close();
        end({ status: 'success' });
        return data;
    } catch (error) {
        errorCounter.inc({ type: error.name, url });
        end({ status: 'error' });
        throw error;
    } finally {
        activePages.dec();
    }
}

// Express 端点暴露指标
const express = require('express');
const app = express();

app.get('/metrics', async (req, res) => {
    res.set('Content-Type', register.contentType);
    res.end(await register.metrics());
});

app.listen(9090, () => {
    console.log('Metrics server running on :9090');
});
```

### 🔄 队列系统集成（Bull）

```javascript
const puppeteer = require('puppeteer');
const Bull = require('bull');

// 创建队列
const scrapeQueue = new Bull('scrape', {
    redis: {
        host: '127.0.0.1',
        port: 6379
    },
    defaultJobOptions: {
        attempts: 3,
        backoff: {
            type: 'exponential',
            delay: 2000
        }
    }
});

// 全局浏览器实例
let browser;

async function initBrowser() {
    browser = await puppeteer.launch({
        headless: 'new',
        args: ['--no-sandbox', '--disable-setuid-sandbox']
    });
}

initBrowser();

// 处理任务
scrapeQueue.process(5, async (job) => {
    const { url, selector } = job.data;
    
    job.progress(10);
    
    const page = await browser.newPage();
    
    try {
        await page.goto(url, { timeout: 30000 });
        job.progress(50);
        
        const data = await page.evaluate((sel) => {
            return document.querySelector(sel)?.textContent;
        }, selector);
        
        job.progress(100);
        return { url, data, timestamp: Date.now() };
    } catch (error) {
        console.error(`Failed to scrape ${url}:`, error);
        throw error;  // 让 Bull 处理重试
    } finally {
        await page.close();
    }
});

// 添加任务
async function addScrapeJob(url, selector, options = {}) {
    const job = await scrapeQueue.add(
        { url, selector },
        {
            priority: options.priority || 5,
            timeout: options.timeout || 60000,
            ...options
        }
    );
    
    return job.id;
}

// 监听事件
scrapeQueue.on('completed', (job, result) => {
    console.log(`Job ${job.id} completed:`, result);
});

scrapeQueue.on('failed', (job, err) => {
    console.error(`Job ${job.id} failed:`, err.message);
});

scrapeQueue.on('progress', (job, progress) => {
    console.log(`Job ${job.id} is ${progress}% complete`);
});

// 使用示例
addScrapeJob('https://example.com', 'h1', { priority: 1 });
addScrapeJob('https://example.com/page2', '.title', { priority: 10 });
```

### 💾 数据持久化（MongoDB）

```javascript
const puppeteer = require('puppeteer');
const { MongoClient } = require('mongodb');

class ScraperWithDB {
    constructor(mongoUrl, dbName) {
        this.mongoUrl = mongoUrl;
        this.dbName = dbName;
        this.browser = null;
        this.db = null;
    }
    
    async init() {
        // 初始化浏览器
        this.browser = await puppeteer.launch({ headless: 'new' });
        
        // 初始化数据库
        const client = await MongoClient.connect(this.mongoUrl);
        this.db = client.db(this.dbName);
        
        // 创建索引
        await this.db.collection('pages').createIndex({ url: 1 });
        await this.db.collection('pages').createIndex({ timestamp: -1 });
    }
    
    async scrapeAndSave(url, ttl = 86400000) {
        // 检查缓存
        const existing = await this.db.collection('pages').findOne({ url });
        if (existing && Date.now() - existing.timestamp < ttl) {
            console.log(`Cache hit for ${url}`);
            return existing.data;
        }
        
        const page = await this.browser.newPage();
        
        try {
            await page.goto(url, { waitUntil: 'networkidle2', timeout: 30000 });
            
            const data = await page.evaluate(() => ({
                title: document.title,
                description: document.querySelector('meta[name="description"]')?.content,
                h1: document.querySelector('h1')?.textContent,
                links: Array.from(document.querySelectorAll('a'))
                    .map(a => ({ text: a.textContent, href: a.href }))
                    .slice(0, 100)  // 限制数量
            }));
            
            // 保存到数据库
            await this.db.collection('pages').updateOne(
                { url },
                {
                    $set: {
                        url,
                        data,
                        timestamp: Date.now(),
                        ttl: ttl
                    }
                },
                { upsert: true }
            );
            
            console.log(`Scraped and saved: ${url}`);
            return data;
            
        } catch (error) {
            // 记录失败
            await this.db.collection('failures').insertOne({
                url,
                error: error.message,
                timestamp: Date.now()
            });
            throw error;
        } finally {
            await page.close();
        }
    }
    
    async getStats() {
        const total = await this.db.collection('pages').countDocuments();
        const failures = await this.db.collection('failures').countDocuments();
        const cacheHitRate = total > 0 ? ((total - failures) / total * 100).toFixed(2) : 0;
        
        return { total, failures, cacheHitRate };
    }
    
    async close() {
        if (this.browser) await this.browser.close();
    }
}

// 使用示例
const scraper = new ScraperWithDB('mongodb://localhost:27017', 'scraper');
await scraper.init();

const urls = [
    'https://example.com',
    'https://example.com/page1',
    'https://example.com/page2'
];

for (const url of urls) {
    try {
        const data = await scraper.scrapeAndSave(url);
        console.log(data);
    } catch (error) {
        console.error(`Failed: ${url}`, error.message);
    }
}

const stats = await scraper.getStats();
console.log('Stats:', stats);

await scraper.close();
```

---

## 总结与推荐

### ✅ 何时选择 Puppeteer

1. **首选场景**：
   - ✅ 需要 Google 官方支持
   - ✅ 只需要 Chrome/Chromium
   - ✅ Node.js 技术栈
   - ✅ 企业级应用
   - ✅ 需要最新 Chrome 特性

2. **优势**：
   - 官方维护，更新及时
   - 性能优秀
   - 文档完善
   - 生态成熟
   - 社区活跃

3. **劣势**：
   - 仅支持 Chrome
   - 异步编程复杂
   - 不支持 Python

### 📚 学习路径

1. **入门**（1-2 周）
   - 安装和基础配置
   - 基本 API（goto、click、type）
   - 选择器和等待

2. **进阶**（2-4 周）
   - 网络拦截
   - 性能优化
   - 错误处理
   - 实战项目

3. **高级**（1-2 月）
   - CDP 协议
   - 大规模部署
   - 反检测技术
   - 性能调优

### 🔗 参考资源

**官方资源**：
- [Puppeteer 官网](https://pptr.dev/)
- [GitHub 仓库](https://github.com/puppeteer/puppeteer)
- [API 文档](https://pptr.dev/api)

**社区资源**：
- [Stack Overflow](https://stackoverflow.com/questions/tagged/puppeteer)
- [Discord 社区](https://discord.gg/puppeteer)
- [Awesome Puppeteer](https://github.com/transitive-bullshit/awesome-puppeteer)

**相关工具**：
- [puppeteer-extra](https://github.com/berstend/puppeteer-extra) - 插件系统
- [puppeteer-cluster](https://github.com/thomasdondorf/puppeteer-cluster) - 集群管理
- [puppeteer-screen-recorder](https://github.com/prasanaworld/puppeteer-screen-recorder) - 录屏

---

**文档版本**：v1.0  
**最后更新**：2025-10-18  
**作者**：AI 技术分析  
**适用版本**：Puppeteer 21.x+, Node.js 18+

**反馈**：如有问题或建议，欢迎提交 Issue。

