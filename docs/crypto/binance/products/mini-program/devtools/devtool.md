---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/devtools/devtool
api_type: Guide
updated_at: 2026-11-18 02:20:31.273601
---

# How to Use Devtools

## Login

![img](https://bin.bnbstatic.com/image/julia/docs/mini-program/ide-login.png)
![img](https://bin.bnbstatic.com/image/julia/docs/mini-program/ide-login-2.png)
![img](https://bin.bnbstatic.com/image/julia/docs/mini-program/ide-login-3.png)

## Inspect Tool

1. Use `Open inspect tool` to add a request header.

![img](https://bin.bnbstatic.com/image/julia/docs/mini-program/ide-devtools-1.png)

Write your request (It won't work if the request URL is incorrect).

```ts
async onRequest(){
  await bn.request({
    url: 'https://www.devfdg.net/en/js-sdk-demo-ui/request'
  })
},
```

2. Add your header.

![img](https://bin.bnbstatic.com/image/julia/docs/mini-program/ide-devtools-2.png)

![img](https://bin.bnbstatic.com/image/julia/docs/mini-program/ide-devtools-3.png)

## How to Debug WebView

Click the `Devtool` menu and select `Open Current Webview Component Devtools`. A devtool dialog will
then appear.

![webview-devtool-menu](https://bin.bnbstatic.com/image/julia/docs/mp-ide/webview-devtool-menu.png)

Ensure there's a webview component when you select `Open Current Webview Component Devtools`. If
there isn't, nothing will happen.

---

# How to Use Devtools

## Login

![img](https://bin.bnbstatic.com/image/julia/docs/mini-program/ide-login.png)
![img](https://bin.bnbstatic.com/image/julia/docs/mini-program/ide-login-2.png)
![img](https://bin.bnbstatic.com/image/julia/docs/mini-program/ide-login-3.png)

## Inspect Tool

1. Use `Open inspect tool` to add a request header.

![img](https://bin.bnbstatic.com/image/julia/docs/mini-program/ide-devtools-1.png)

Write your request (It won't work if the request URL is incorrect).

```ts
async onRequest(){
  await bn.request({
    url: 'https://www.devfdg.net/en/js-sdk-demo-ui/request'
  })
},
```

2. Add your header.

![img](https://bin.bnbstatic.com/image/julia/docs/mini-program/ide-devtools-2.png)

![img](https://bin.bnbstatic.com/image/julia/docs/mini-program/ide-devtools-3.png)

## How to Debug WebView

Click the `Devtool` menu and select `Open Current Webview Component Devtools`. A devtool dialog will
then appear.

![webview-devtool-menu](https://bin.bnbstatic.com/image/julia/docs/mp-ide/webview-devtool-menu.png)

Ensure there's a webview component when you select `Open Current Webview Component Devtools`. If
there isn't, nothing will happen.