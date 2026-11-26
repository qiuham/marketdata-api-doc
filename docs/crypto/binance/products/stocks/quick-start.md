---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/stocks/quick-start
api_type: Guide
updated_at: 2026-11-26 18:29:16.894587
---

# Quick Start

## Prerequisites

1. A Binance account with SAPI access. If you don't have one, start at the root
   [Quick Start](../quick-start.md).
2. An API key + secret with **Enable Trading** permission for the endpoints that require `TRADE`
   authority; `USER_DATA` permission suffices for query-only endpoints.

## Sign a Request

All trade endpoints require an HMAC-SHA256 or Ed25519 signature over the query string, identical to
other SAPI endpoints. See the root
[General Info](../general-info.md#signed-trade-and-user_data-endpoint-security) for the signing
procedure.

## Place a Limit Buy Order (curl example)

```bash
BASE_URL="https://api.binance.com"
API_KEY="<your api key>"
SECRET="<your api secret>"
TIMESTAMP=$(($(date +%s%N)/1000000))

QUERY="symbol=AAPL&side=BUY&orderType=LIMIT&price=180.50&quantity=1&tradingSession=RTH&timeInForce=DAY&timestamp=${TIMESTAMP}"
SIGNATURE=$(echo -n "$QUERY" | openssl dgst -sha256 -hmac "$SECRET" | awk '{print $2}')

curl -X POST \
  -H "X-MBX-APIKEY: $API_KEY" \
  "${BASE_URL}/sapi/v1/equity/order/place?${QUERY}&signature=${SIGNATURE}"
```

Sample response:

```javascript
{
  "status": "S",
  "orderId": "c3c58f49-7b0d-4b9e-a2db-1a2f9a3b8c71",
  "clientOrderId": "web_2c9c92b74f1e4a7c8f3b9e1a2d3c4b5a"
}
```

## Next Steps

- Read [General Info](./general-info.md) for URL prefix, symbol format, default quote asset, and the
  UPPERCASE enum contract.
- Read [Common Definition](./common-definition.md) for the full enum sets (side / orderType /
  orderStatus / tradingSession / …).
- Read [Error Code](./error-code.md) for how errors from this module are structured.

---

# 快速开始

## 准备工作

1. 已开通 SAPI 权限的 Binance 账号。如无，请先阅读根级 [快速开始](../quick-start_zh-CN.md)。
2. 一对 API Key + Secret，且对需要 `TRADE` 权限的接口开启"启用交易"；仅调用 `USER_DATA`
   查询类接口只需 `USER_DATA` 权限即可。

## 请求签名

所有交易接口都需要对 query
string 做 HMAC-SHA256 或 Ed25519 签名，方式与其他 SAPI 接口完全一致。签名细节参见根级
[基本信息](../general-info_zh-CN.md#signed-trade-and-user_data-endpoint-security)。

## 限价买入示例（curl）

```bash
BASE_URL="https://api.binance.com"
API_KEY="<你的 api key>"
SECRET="<你的 api secret>"
TIMESTAMP=$(($(date +%s%N)/1000000))

QUERY="symbol=AAPL&side=BUY&orderType=LIMIT&price=180.50&quantity=1&tradingSession=RTH&timeInForce=DAY&timestamp=${TIMESTAMP}"
SIGNATURE=$(echo -n "$QUERY" | openssl dgst -sha256 -hmac "$SECRET" | awk '{print $2}')

curl -X POST \
  -H "X-MBX-APIKEY: $API_KEY" \
  "${BASE_URL}/sapi/v1/equity/order/place?${QUERY}&signature=${SIGNATURE}"
```

响应示例：

```javascript
{
  "status": "S",
  "orderId": "c3c58f49-7b0d-4b9e-a2db-1a2f9a3b8c71",
  "clientOrderId": "web_2c9c92b74f1e4a7c8f3b9e1a2d3c4b5a"
}
```

## 下一步

- 阅读
  [基本信息](./general-info_zh-CN.md)，了解 URL 前缀、Symbol 格式、默认报价资产、枚举 UPPERCASE 契约。
- 阅读 [通用枚举定义](./common-definition_zh-CN.md)，查看完整的枚举值集合（side / orderType /
  orderStatus / tradingSession 等）。
- 阅读 [错误代码](./error-code_zh-CN.md)，了解本模块的错误码层次。