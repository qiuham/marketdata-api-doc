---
exchange: binance
source_url: https://developers.binance.com/docs/binance-spot-api-docs/demo-mode/general-info
api_type: REST
updated_at: 2026-06-30 19:04:29.012246
---

# Demo Mode for SPOT Trading

This page explains how to use [Demo Mode Trading](https://www.binance.com/en/support/faq/detail/9be58f73e5e14338809e3b705b9687dd) via the API.

## How can I trade on Demo Mode using the API?[​](/docs/binance-spot-api-docs/demo-mode/general-info#how-can-i-trade-on-demo-mode-using-the-api "Direct link to How can I trade on Demo Mode using the API?")

  1. After logging into your Binance account, click on Binance Demo Trading and then you can create an API key in the [API Key Management page](https://demo.binance.com/en/my/settings/api-management).
  2. Follow the official documentation of the SPOT API, replacing the URLs of the endpoints/methods with the following values:

Service | Spot API URLs | Demo Mode URLs  
---|---|---  
REST API  | 

  * https://api.binance.com/api
  * https://api-gcp.binance.com/api
  * https://api1.binance.com/api
  * https://api2.binance.com/api
  * https://api3.binance.com/api
  * https://api4.binance.com/api

| 

  * **https://demo-api.binance.com/api**

  
WebSocket API  | 

  * wss://ws-api.binance.com/ws-api/v3
  * wss://ws-api.binance.com:9443/ws-api/v3

| 

  * **wss://demo-ws-api.binance.com/ws-api/v3**

  
WebSocket Market Streams  | 

  * wss://stream.binance.com/ws
  * wss://stream.binance.com:9443/ws

| 

  * **wss://demo-stream.binance.com/ws**
  * **wss://demo-stream.binance.com:9443/ws**

  
  
  * wss://stream.binance.com/stream
  * wss://stream.binance.com:9443/stream

| 

  * **wss://demo-stream.binance.com/stream**
  * **wss://demo-stream.binance.com:9443/stream**

  
WebSocket Market Streams (SBE)  | 

  * wss://stream-sbe.binance.com/ws
  * wss://stream-sbe.binance.com:9443/ws

| 

  * **wss://demo-stream-sbe.binance.com/ws**
  * **wss://demo-stream-sbe.binance.com:9443/ws**

  
  
  * wss://stream-sbe.binance.com/stream
  * wss://stream-sbe.binance.com:9443/stream

| 

  * **wss://demo-stream-sbe.binance.com/stream**
  * **wss://demo-stream-sbe.binance.com:9443/stream**

  
FIX   
(Send FIX requests; receive FIX responses)  | 

  * tcp+tls://fix-oe.binance.com:9000

| 

  * **tcp+tls://demo-fix-oe.binance.com:9000**

  
  
  * tcp+tls://fix-dc.binance.com:9000

| 

  * **tcp+tls://demo-fix-dc.binance.com:9000**

  
  
  * tcp+tls://fix-md.binance.com:9000

| 

  * **tcp+tls://demo-fix-md.binance.com:9000**

  
FIX SBE   
(Send FIX requests; receive FIX SBE responses)  | 

  * tcp+tls://fix-oe.binance.com:9001

| 

  * **tcp+tls://demo-fix-oe.binance.com:9001**

  
  
  * tcp+tls://fix-dc.binance.com:9001

| 

  * **tcp+tls://demo-fix-dc.binance.com:9001**

  
  
  * tcp+tls://fix-md.binance.com:9001

| 

  * **tcp+tls://demo-fix-md.binance.com:9001**

  
FIX SBE   
(Send FIX SBE requests; receive FIX SBE responses)  | 

  * tcp+tls://fix-oe.binance.com:9002

| 

  * **tcp+tls://demo-fix-oe.binance.com:9002**

  
  
  * tcp+tls://fix-dc.binance.com:9002

| 

  * **tcp+tls://demo-fix-dc.binance.com:9002**

  
  
  * tcp+tls://fix-md.binance.com:9002

| 

  * **tcp+tls://demo-fix-md.binance.com:9002**

  
  
## What is the difference between SPOT Testnet and SPOT Demo Mode?[​](/docs/binance-spot-api-docs/demo-mode/general-info#what-is-the-difference-between-spot-testnet-and-spot-demo-mode "Direct link to What is the difference between SPOT Testnet and SPOT Demo Mode?")

SPOT Testnet| SPOT Demo Mode  
---|---  
Balances are reset every month.| You can reset your balance whenever you want via the UI.  
SPOT Testnet sometimes has new features before the live exchange.| Demo Mode always has the same features as the live exchange.  
Testnet's prices and order books are independent from the live exchange.| Demo Mode's prices and order books are similar to the live exchange.  
IP Limits, Unfilled Order Count, Exchange Filters are generally the same as the live exchange.| IP Limits, Unfilled Order Count, Exchange Filters are exactly the same as the live exchange.  
  
**In summary** :

  * SPOT Testnet is useful to integrate with upcoming features not yet available on the live exchange.
  * Demo Mode is useful to test against _realistic_ market data.



> [!WARNING] Realistic market data is not equal to "real" market data. Do not assume trading strategies that work in Demo Mode will work in the live exchange.

## What happens when Demo Mode is under maintenance?[​](/docs/binance-spot-api-docs/demo-mode/general-info#what-happens-when-demo-mode-is-under-maintenance "Direct link to What happens when Demo Mode is under maintenance?")

  * There will be an announcement on the [CHANGELOG](/docs/binance-spot-api-docs/demo-mode/CHANGELOG) page prior to downtime.
  * During maintenance, you will not be able to place or cancel orders.

---

# 现货模拟交易

本页面说明如何通过 API 使用[模拟交易](https://www.binance.com/zh-CN/support/faq/detail/9be58f73e5e14338809e3b705b9687dd)。

## 如何通过 API 进行模拟交易？[​](/docs/zh-CN/binance-spot-api-docs/demo-mode/general-info#如何通过-api-进行模拟交易 "如何通过 API 进行模拟交易？的直接链接")

  1. 登录您的 Binance 账户后，点击 Binance 模拟交易，然后您可以在[API 密钥管理页面](https://demo.binance.com/en/my/settings/api-management)创建 API 密钥。
  2. 按照现货 API 的官方文档操作，将接口/方法的 URL 替换为以下值：

服务 | 现货 API URL | 模拟交易 URL  
---|---|---  
REST接口  | 

  * https://api.binance.com/api
  * https://api-gcp.binance.com/api
  * https://api1.binance.com/api
  * https://api2.binance.com/api
  * https://api3.binance.com/api
  * https://api4.binance.com/api

| 

  * **https://demo-api.binance.com/api**

  
WebSocket API  | 

  * wss://ws-api.binance.com/ws-api/v3
  * wss://ws-api.binance.com:9443/ws-api/v3

| 

  * **wss://demo-ws-api.binance.com/ws-api/v3**

  
WebSocket 行情接口  | 

  * wss://stream.binance.com/ws
  * wss://stream.binance.com:9443/ws

| 

  * **wss://demo-stream.binance.com/ws**
  * **wss://demo-stream.binance.com:9443/ws**

  
  
  * wss://stream.binance.com/stream
  * wss://stream.binance.com:9443/stream

| 

  * **wss://demo-stream.binance.com/stream**
  * **wss://demo-stream.binance.com:9443/stream**

  
WebSocket 行情接口 (SBE)  | 

  * wss://stream-sbe.binance.com/ws
  * wss://stream-sbe.binance.com:9443/ws

| 

  * **wss://demo-stream-sbe.binance.com/ws**
  * **wss://demo-stream-sbe.binance.com:9443/ws**

  
  
  * wss://stream-sbe.binance.com/stream
  * wss://stream-sbe.binance.com:9443/stream

| 

  * **wss://demo-stream-sbe.binance.com/stream**
  * **wss://demo-stream-sbe.binance.com:9443/stream**

  
FIX   
（发送 FIX 请求；接收 FIX 响应）  | 

  * tcp+tls://fix-oe.binance.com:9000

| 

  * **tcp+tls://demo-fix-oe.binance.com:9000**

  
  
  * tcp+tls://fix-dc.binance.com:9000

| 

  * **tcp+tls://demo-fix-dc.binance.com:9000**

  
  
  * tcp+tls://fix-md.binance.com:9000

| 

  * **tcp+tls://demo-fix-md.binance.com:9000**

  
FIX SBE   
（发送 FIX 请求；接收 FIX SBE 响应）  | 

  * tcp+tls://fix-oe.binance.com:9001

| 

  * **tcp+tls://demo-fix-oe.binance.com:9001**

  
  
  * tcp+tls://fix-dc.binance.com:9001

| 

  * **tcp+tls://demo-fix-dc.binance.com:9001**

  
  
  * tcp+tls://fix-md.binance.com:9001

| 

  * **tcp+tls://demo-fix-md.binance.com:9001**

  
FIX SBE   
（发送 FIX SBE 请求；接收 FIX SBE 响应）  | 

  * tcp+tls://fix-oe.binance.com:9002

| 

  * **tcp+tls://demo-fix-oe.binance.com:9002**

  
  
  * tcp+tls://fix-dc.binance.com:9002

| 

  * **tcp+tls://demo-fix-dc.binance.com:9002**

  
  
  * tcp+tls://fix-md.binance.com:9002

| 

  * **tcp+tls://demo-fix-md.binance.com:9002**

  
  
## 现货测试网（Testnet）和现货模拟交易（Demo Mode）的区别是什么？[​](/docs/zh-CN/binance-spot-api-docs/demo-mode/general-info#现货测试网testnet和现货模拟交易demo-mode的区别是什么 "现货测试网（Testnet）和现货模拟交易（Demo Mode）的区别是什么？的直接链接")

现货测试网（Testnet）| 现货模拟交易（Demo Mode）  
---|---  
余额每月重置一次。| 你可以通过界面随时重置余额。  
测试网有时会先于正式交易所推出新功能。| 模拟交易始终拥有与正式交易所相同的功能。  
测试网的价格和订单簿与正式交易所独立。| 模拟交易的价格和订单簿与正式交易所相似。  
IP 限制、未成交订单数量、交易所过滤器通常与正式交易所相同。| IP 限制、未成交订单数量、交易所过滤器与正式交易所完全相同。  
  
**总结** ：

  * 现货测试网适合集成尚未在正式交易所上线的新功能。
  * 模拟交易适合基于 _类似真实的_ 市场数据进行测试。



> [!WARNING] 类似真实的市场数据不等同于“真实”市场数据。在模拟交易中有效的交易策略在正式交易所未必有效。

## 模拟交易维护期间会发生什么？[​](/docs/zh-CN/binance-spot-api-docs/demo-mode/general-info#模拟交易维护期间会发生什么 "模拟交易维护期间会发生什么？的直接链接")

  * 维护前会在 [更新日志](/docs/zh-CN/binance-spot-api-docs/demo-mode/CHANGELOG) 页面发布公告。
  * 维护期间，您将无法下单或取消订单。