---
exchange: binance
source_url: https://developers.binance.com/docs/alpha/market-data/general-info
api_type: Market Data
updated_at: 2026-05-27 19:01:44.387453
---

# General Info

This is the documentation for the Binance Alpha Trade. All endpoints use HTTP GET requests and return data in JSON format. No authentication is required as they are public endpoints.

## Important Note[​](/docs/alpha/market-data/general-info#important-note "Direct link to Important Note")

To use the endpoints that require a symbol parameter (e.g., for trading volume, historical trades, or Kline data), first call the Token List endpoint to retrieve the list of available tokens. From the response, identify the corresponding ALPHA token ID based on the symbol name (e.g., "ZKJ" or "QUQ"). Then, construct the symbol parameter in the format ALPHA_<token_id><quote_asset> (e.g., ALPHA_173USDT for token ID 173 with USDT).

---

# 通用信息

这是关于币安Alpha交易的文档。所有接口均使用HTTP GET请求，返回JSON格式的数据。因为是公共接口，所以无需身份验证。

## 重要提示[​](/docs/zh-CN/alpha/market-data/general-info#重要提示 "重要提示的直接链接")

对于需要symbol参数的接口（例如，交易量、历史交易或K线数据），请先调用Token列表接口以获取可用代币列表。在响应中，根据代币符号名称（例如 "ZKJ" 或 "QUQ"）确定对应的ALPHA代币ID。然后，按格式ALPHA_<token_id><quote_asset>构造symbol参数（例如，ALPHA_173USDT表示代币ID为173，计价资产为USDT的代币）。