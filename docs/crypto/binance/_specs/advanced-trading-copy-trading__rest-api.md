---
exchange: binance
source_url: https://developers.binance.com/en/docs/catalog/advanced-trading-copy-trading/api/rest-api/1.0.0/schema.yaml
api_type: spec
updated_at: 2026-11-13 20:40:12.342166
---

# advanced-trading-copy-trading__rest-api spec

Source: https://developers.binance.com/en/docs/catalog/advanced-trading-copy-trading/api/rest-api/1.0.0/schema.yaml

```yaml
openapi: 3.0.2
info:
  title: Copy Trading REST API
  description: Automate lead trading via the Copy Trading API.
  x-description-cn: 通过 Copy Trading API 自动化进行带单交易。
  version: 1.0.0
  termsOfService: https://www.binance.com/en/terms
  contact:
    name: Binance API Support
    url: https://www.binance.com/en/support
x-product-type: rest-api
x-rate-limits-guide: products/copy-trading/general-info#limits
x-rate-limits-guide-cn: products/copy-trading/general-info#访问限制
x-security-guide: products/copy-trading/general-info#request-security
x-security-guide-cn: products/copy-trading/general-info#请求鉴权类型
x-api-key-guide: https://www.binance.com/en/support/faq/detail/360002502072
x-api-key-guide-cn: https://www.binance.com/cn/support/faq/detail/360002502072
externalDocs:
  description: Copy Trading docs
  url: https://developers.binance.com/en/docs/products/copy-trading/Introduction
tags:
  - name: future-copy-trading
    x-displayName: Future Copy Trading
    x-displayName-cn: 合约跟单交易
servers:
  - url: https://api.binance.com
  - url: https://api-gcp.binance.com
  - url: https://api1.binance.com
  - url: https://api2.binance.com
  - url: https://api3.binance.com
  - url: https://api4.binance.com
paths:
  /sapi/v1/copyTrading/futures/userStatus:
    get:
      summary: Get Futures Lead Trader Status (TRADE)
      x-summary-cn: 查询是否为带单员身份 (TRADE)
      description: Get Futures Lead Trader Status
      x-description-cn: 查询是否为带单员身份
      tags:
        - future-copy-trading
      operationId: getFuturesLeadTraderStatus
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-copy-trading/api/rest-api/future-copy-trading#get-futures-lead-trader-status
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/copy-trading/examples/rest-api/FutureCopyTradingApi/getFuturesLeadTraderStatus.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/copy_trading/rest_api/future_copy_trading_api/get_futures_lead_trader_status.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/copy_trading/examples/rest_api/FutureCopyTrading/get_futures_lead_trader_status.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/copy-trading/src/main/java/com/binance/connector/client/copy_trading/rest/futurecopytrading/GetFuturesLeadTraderStatusExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/copytrading/examples/restapi/FutureCopyTradingAPI/GetFuturesLeadTraderStatus/GetFuturesLeadTraderStatus.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/copy-trading/futurecopytrading/GetFuturesLeadTraderStatusExample.php
      x-ip-weight: 1
      x-security-type: TRADE
      x-signed: true
      parameters:
        - name: X-MBX-APIKEY
          in: header
          required: true
          description: >-
            An API Key is required to access this endpoint and must be included in the request headers. To create an API
            Key, refer to:
            [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).
          x-description-cn: >-
            访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API
            Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。
          schema:
            type: string
            example: API_KEY
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
            maximum: 60000
          description: Request validity window in milliseconds
          x-description-cn: 请求有效时间窗口（毫秒）
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: |-
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Get Futures Lead Trader Status
          x-description-cn: 查询是否为带单员身份
          content:
            application/json:
              schema:
                type: object
                properties:
                  code:
                    type: string
                    example: "000000"
                    description: API response code. "000000" indicates success.
                    x-description-cn: API 响应码。"000000" 表示成功。
                  message:
                    type: string
                    example: success
                    description: Response message.
                    x-description-cn: 响应消息。
                  data:
                    type: object
                    properties:
                      isLeadTrader:
                        type: boolean
                        example: true
                        description: Whether the user is a futures lead trader
                        x-description-cn: 用户是否为合约带单员
                      time:
                        type: integer
                        example: 1717382310843
                        format: int64
                        description: Server timestamp in milliseconds
                        x-description-cn: 服务器时间戳（毫秒）
                  success:
                    type: boolean
                    example: true
                    description: Whether request is successful
                    x-description-cn: 请求是否成功
  /sapi/v1/copyTrading/futures/leadSymbol:
    get:
      summary: Get Futures Lead Trading Symbol Whitelist (USER_DATA)
      x-summary-cn: 查询带单币种白名单 (USER_DATA)
      description: Get Futures Lead Trading Symbol Whitelist
      x-description-cn: 查询带单币种白名单
      tags:
        - future-copy-trading
      operationId: getFuturesLeadTradingSymbolWhitelist
      externalDocs:
        url: >-
          https://developers.binance.com/en/docs/catalog/advanced-trading-copy-trading/api/rest-api/future-copy-trading#get-futures-lead-trading-symbol-whitelist
      x-connectors-examples:
        ts: >-
          https://raw.githubusercontent.com/binance/binance-connector-js/master/clients/copy-trading/examples/rest-api/FutureCopyTradingApi/getFuturesLeadTradingSymbolWhitelist.ts
        rust: >-
          https://raw.githubusercontent.com/binance/binance-connector-rust/main/examples/copy_trading/rest_api/future_copy_trading_api/get_futures_lead_trading_symbol_whitelist.rs
        python: >-
          https://raw.githubusercontent.com/binance/binance-connector-python/master/clients/copy_trading/examples/rest_api/FutureCopyTrading/get_futures_lead_trading_symbol_whitelist.py
        java: >-
          https://raw.githubusercontent.com/binance/binance-connector-java/master/examples/copy-trading/src/main/java/com/binance/connector/client/copy_trading/rest/futurecopytrading/GetFuturesLeadTradingSymbolWhitelistExample.java
        go: >-
          https://raw.githubusercontent.com/binance/binance-connector-go/main/clients/copytrading/examples/restapi/FutureCopyTradingAPI/GetFuturesLeadTradingSymbolWhitelist/GetFuturesLeadTradingSymbolWhitelist.go
        php: >-
          https://raw.githubusercontent.com/binance/binance-connector-php/master/examples/copy-trading/futurecopytrading/GetFuturesLeadTradingSymbolWhitelistExample.php
      x-ip-weight: 1
      x-security-type: USER_DATA
      x-signed: true
      parameters:
        - name: X-MBX-APIKEY
          in: header
          required: true
          description: >-
            An API Key is required to access this endpoint and must be included in the request headers. To create an API
            Key, refer to:
            [https://www.binance.com/en/support/faq/detail/360002502072](https://www.binance.com/en/support/faq/detail/360002502072).
          x-description-cn: >-
            访问此接口需要 API Key，并且必须在请求头中携带。关于如何创建 API
            Key，请参考：[https://www.binance.com/cn/support/faq/detail/360002502072](https://www.binance.com/cn/support/faq/detail/360002502072)。
          schema:
            type: string
            example: API_KEY
        - name: recvWindow
          in: query
          required: false
          schema:
            type: integer
            example: 5000
            format: int64
            maximum: 60000
          description: Request validity window in milliseconds
          x-description-cn: 请求有效时间窗口（毫秒）
        - name: timestamp
          in: query
          required: true
          schema:
            type: integer
            example: 1770736694138
            format: int64
          description: |-
            Unix timestamp in milliseconds used to sign the request. The value must reflect the current client time and
            is validated by the server for signed endpoints.
          x-description-cn: 用于请求签名的 Unix 时间戳，单位为毫秒. 该值必须反映客户端当前时间，并会在签名接口中由服务器进行校验.
      responses:
        "200":
          description: Get Futures Lead Trading Symbol Whitelist
          x-description-cn: 查询带单币种白名单
          content:
            application/json:
              schema:
                type: object
                properties:
                  code:
                    type: string
                    example: "000000"
                    description: API response code. "000000" indicates success.
                    x-description-cn: API 响应码。"000000" 表示成功。
                  message:
                    type: string
                    example: success
                    description: Response message.
                    x-description-cn: 响应消息。
                  data:
                    type: array
                    description: Whitelisted symbols for futures lead trading
                    x-description-cn: 合约带单白名单交易对
                    items:
                      type: object
                      properties:
                        symbol:
                          type: string
                          example: BTCUSDT
                          description: Trading symbol
                          x-description-cn: 交易对
                        baseAsset:
                          type: string
                          example: BTC
                          description: Base asset
                          x-description-cn: 基础资产
                        quoteAsset:
                          type: string
                          example: USDT
                          description: Quote asset
                          x-description-cn: 计价资产
```