---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#financial-product-dual-investment
anchor_id: financial-product-dual-investment
api_type: API
updated_at: 2026-07-08 19:29:36.907390
---

# Dual investment

### GET / Currency pairs  
  
Returns available dual investment currency pairs.

#### Rate Limit: 1 request per second

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/finance/sfp/dcd/currency-pair`

> Request Example
    
    
    GET /api/v5/finance/sfp/dcd/currency-pair
    

#### Request Parameters

None

> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "baseCcy": "BTC",
                "quoteCcy": "USDT",
                "optType": "C",
                "uly": "BTC-USD"
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
baseCcy | String | Base currency  
quoteCcy | String | Quote currency  
optType | String | Option type  
`C`: Call  
`P`: Put  
uly | String | Underlying  
  
### GET / Product info

Return dual investment product list.

#### Rate Limit: 1 request per second

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/finance/sfp/dcd/products`

> Request Example
    
    
    GET /api/v5/finance/sfp/dcd/products?baseCcy=BTC&quoteCcy=USDT&optType=C
    

#### Request Parameters

**Parameter** | **Type** | **Required** | **Description**  
---|---|---|---  
baseCcy | String | Yes | Base currency  
quoteCcy | String | Yes | Quote currency  
optType | String | Yes | Option type  
`C`: Call  
`P`: Put  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "absYield": "0.00232413",
                "annualizedYield": "0.0541",
                "baseCcy": "BTC",
                "quoteCcy": "USDT",
                "expTime": "1774598400000",
                "interestAccrualTime": "1773244800000",
                "listTime": "1743150759000",
                "maxSize": "6000000",
                "minSize": "10",
                "notionalCcy": "USDT",
                "optType": "P",
                "productId": "BTC-USDT-260327-54500-P",
                "quoteTime": "1773243808703",
                "redeemEndTime": "1774594800000",
                "redeemStartTime": "1773244800000",
                "stepSz": "1",
                "tradeEndTime": "1774584000000",
                "strike": "54500",
                "uly": "BTC-USD"
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
absYield | String | Absolute yield  
annualizedYield | String | Annualized yield  
baseCcy | String | Base currency  
quoteCcy | String | Quote currency  
notionalCcy | String | Investment currency. If `C`, then baseCcy; if `P`, then quoteCcy.  
expTime | String | Expiry time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
interestAccrualTime | String | Interest accrual start time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
listTime | String | Product launch time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
minSize | String | Minimum trade size in notional currency  
maxSize | String | Maximum trade size in notional currency  
optType | String | Option type  
`C`: Call  
`P`: Put  
productId | String | Product ID  
quoteTime | String | When product was quoted, Unix timestamp format in milliseconds, e.g. `1597026383085`  
redeemStartTime | String | Earliest time to request early redemption, Unix timestamp format in milliseconds, e.g. `1597026383085`  
redeemEndTime | String | Latest time to request early redemption, Unix timestamp format in milliseconds, e.g. `1597026383085`  
stepSz | String | Trade step size in notional currency  
tradeEndTime | String | Trade end time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
uly | String | Underlying  
strike | String | Strike price  
  
### POST / Request for quote

Requests a real-time quote for a dual investment product. The quote has a TTL and must be used before expiry.

#### Rate Limit: 10 requests per 60 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/finance/sfp/dcd/quote`

> Request Example
    
    
    POST /api/v5/finance/sfp/dcd/quote
    body
    {
        "productId": "BTC-USDT-260327-77000-C",
        "notionalSz": "1.5",
        "notionalCcy": "BTC"
    }
    

#### Request Parameters

**Parameter** | **Type** | **Required** | **Description**  
---|---|---|---  
productId | String | Yes | Product ID  
notionalSz | String | Yes | Investment size  
notionalCcy | String | Yes | Investment currency  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "absYield": "0.00135182",
                "annualizedYield": "69.65",
                "interestAccrualTime": "1773241200000",
                "notionalSz": "0.001",
                "notionalCcy": "BTC",
                "productId": "BTC-USDT-260312-72000-C",
                "quoteId": "qtbcDCD-QUOTE17732395560537636",
                "validUntil": "1774584000000",
                "idxPx": "69000"
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
absYield | String | Absolute yield  
annualizedYield | String | Annualized yield  
interestAccrualTime | String | Interest accrual start time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
notionalSz | String | Investment size  
notionalCcy | String | Investment currency  
productId | String | Product ID  
quoteId | String | Quote ID  
validUntil | String | Quote valid until, Unix timestamp format in milliseconds, e.g. `1597026383085`  
idxPx | String | Index price  
  
### POST / Trade

Places a dual investment order using a valid quote.

#### Rate Limit: 2 requests per 60 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/finance/sfp/dcd/trade`

> Request Example
    
    
    POST /api/v5/finance/sfp/dcd/trade
    body
    {
        "quoteId": "quoterbpDCD-QUOTE17732116652401234"
    }
    

#### Request Parameters

**Parameter** | **Type** | **Required** | **Description**  
---|---|---|---  
quoteId | String | Yes | Quote ID  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "quoteId": "quoterbpDCD-QUOTE17732116652401234",
                "ordId": "987654321",
                "state": "live"
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
quoteId | String | Quote ID  
ordId | String | Order ID  
state | String | Order state  
`initial`: request has been received by system, will further process  
`pending_book`: trade received by liquidity provider, pending further processing  
`live`: trade is live  
`rejected`: trade has been rejected  
  
### POST / Request for redeem quote

Requests an early redemption quote for a live dual investment order. This is step 1 of the two-step early redemption flow; call POST / Redeem to confirm.

#### Rate Limit: 10 requests per 60 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/finance/sfp/dcd/redeem-quote`

> Request Example
    
    
    POST /api/v5/finance/sfp/dcd/redeem-quote
    body
    {
        "ordId": "987654321"
    }
    

#### Request Parameters

**Parameter** | **Type** | **Required** | **Description**  
---|---|---|---  
ordId | String | Yes | Order ID  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "ordId": "987654321",
                "quoteId": "quoterbcDCD-REDEEM17732116652401234",
                "redeemCcy": "BTC",
                "redeemSz": "1.4856",
                "termRate": "-0.50",
                "validUntil": "1774598400000"
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
ordId | String | Order ID  
quoteId | String | Quote ID  
redeemSz | String | Redeem size  
redeemCcy | String | Redeem currency  
termRate | String | Term rate  
validUntil | String | Redeem quote valid until, Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
### POST / Redeem

Confirms early redemption using a valid redeem quote. This is step 2 of the two-step early redemption flow.

#### Rate Limit: 2 requests per 60 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/finance/sfp/dcd/redeem`

> Request Example
    
    
    POST /api/v5/finance/sfp/dcd/redeem
    body
    {
        "ordId": "987654321",
        "quoteId": "quoterbcDCD-REDEEM17732116652401234"
    }
    

#### Request Parameters

**Parameter** | **Type** | **Required** | **Description**  
---|---|---|---  
ordId | String | Yes | Order ID  
quoteId | String | Yes | Quote ID  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "ordId": "987654321",
                "state": "pending_redeem_booking"
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
ordId | String | Order ID  
state | String | order state  
`pending_redeem_booking`: redeem received, waiting for liquidity provider further processing  
`pending_redeem`: liquidity provider booked, waiting for transfer  
`redeeming`: redemption in progress  
`redeemed`: redemption completed  
  
### GET / Order state

Returns the current state of a dual investment order.

#### Rate Limit: 3 requests per second

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/finance/sfp/dcd/order-status`

> Request Example
    
    
    GET /api/v5/finance/sfp/dcd/order-status?ordId=987654321
    

#### Request Parameters

**Parameter** | **Type** | **Required** | **Description**  
---|---|---|---  
ordId | String | Yes | Order ID  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "ordId": "987654321",
                "state": "live"
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
ordId | String | Order ID  
state | String | Order state  
`initial`  
`live`  
`pending_settle`  
`settled`  
`pending_redeem`  
`redeemed`  
`rejected`  
  
### GET / Order history

Return dual investment history orders

#### Rate Limit: 1 request per second

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/finance/sfp/dcd/order-history`

> Request Example
    
    
    GET /api/v5/finance/sfp/dcd/order-history
    

#### Request Parameters

**Parameter** | **Type** | **Required** | **Description**  
---|---|---|---  
ordId | String | No | Order ID. When provided, returns that specific order directly (ignores other filters)  
productId | String | No | Product ID, e.g. `BTC-USDT-260327-77000-C`  
uly | String | No | Underlying index, e.g. `BTC-USD`  
state | String | No | Order state filter  
`initial`  
`live`  
`pending_settle`  
`settled`  
`pending_redeem`  
`redeemed`  
`rejected`  
beginId | String | No | Return records newer than this order ID  
endId | String | No | Return records earlier than this order ID  
begin | String | No | Begin timestamp filter, Unix timestamp format in milliseconds, e.g. `1597026383085`  
end | String | No | End timestamp filter, Unix timestamp format in milliseconds, e.g. `1597026383085`  
limit | String | No | Number of results per request, max 100  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "ordId": "987654321",
                "quoteId": "quoterbpDCD-QUOTE17732116652401234",
                "state": "settled",
                "productId": "BTC-USDT-260327-77000-C",
                "baseCcy": "BTC",
                "quoteCcy": "USDT",
                "uly": "BTC-USD",
                "strike": "77000",
                "notionalSz": "1.5",
                "notionalCcy": "BTC",
                "absYield": "0.00806038",
                "annualizedYield": "0.1834",
                "yieldSz": "0.01209057",
                "yieldCcy": "BTC",
                "settleSz": "1.51209057",
                "settleCcy": "BTC",
                "settlePx": "76500",
                "settleTime": "1774598400000",
                "expTime": "1774598400000",
                "redeemStartTime" : "1774598400000",
                "redeemEndime": "1774598400000",
                "cTime": "1773212400000",
                "uTime": "1773212400000"
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
ordId | String | Order ID  
quoteId | String | Quote ID  
state | String | Order state  
`initial`  
`live`  
`pending_settle`  
`settled`  
`pending_redeem`  
`redeemed`  
`rejected`  
productId | String | Product ID, e.g. `BTC-USDT-260327-77000-C`  
baseCcy | String | Base currency, e.g. `BTC`  
quoteCcy | String | Quote currency, e.g. `USDT`  
uly | String | Underlying index, e.g. `BTC-USD`  
strike | String | Strike price  
notionalSz | String | Notional size  
notionalCcy | String | Notional currency  
absYield | String | Absolute yield rate  
annualizedYield | String | Annual yield rate  
yieldSz | String | Yield size  
yieldCcy | String | Yield currency  
settleSz | String | Settlement size ("" if not yet settled)  
settleCcy | String | Settlement currency ("" if not yet settled)  
settlePx | String | Settlement price ("" if not yet settled)  
expTime | String | Product expiration time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
settleTime | String | Actual settled time, Unix timestamp format in milliseconds, e.g. `1597026383085` ("" if not yet settled)  
redeemStartTime | String | Earliest time to request early redemption, Unix timestamp format in milliseconds, e.g. `1597026383085`  
redeemEndTime | String | Latest time to request early redemption, Unix timestamp format in milliseconds, e.g. `1597026383085`  
cTime | String | Order creation time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
uTime | String | Last update time, Unix timestamp format in milliseconds, e.g. `1597026383085`

---

# 双币赢

### GET / 获取币对   
  
获取双币赢币对

#### 限速：1次/s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/finance/sfp/dcd/currency-pair`

> 请求示例
    
    
    GET /api/v5/finance/sfp/dcd/currency-pair
    

#### 请求参数

无

> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "baseCcy": "BTC",
                "quoteCcy": "USDT",
                "optType": "C",
                "uly": "BTC-USD"
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
baseCcy | String | 基础币种  
quoteCcy | String | 报价币种  
optType | String | 期权类型  
`C`：看涨  
`P`：看跌  
uly | String | 标的  
  
### GET / 获取产品信息 

获取双币赢产品列表

#### 限速：1次/s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/finance/sfp/dcd/products`

> 请求示例
    
    
    GET /api/v5/finance/sfp/dcd/products?baseCcy=BTC&quoteCcy=USDT&optType=C
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
baseCcy | String | 是 | 基础币种  
quoteCcy | String | 是 | 报价币种  
optType | String | 是 | 期权类型  
`C`：看涨  
`P`：看跌  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "absYield": "0.00232413",
                "annualizedYield": "0.0541",
                "baseCcy": "BTC",
                "quoteCcy": "USDT",
                "expTime": "1774598400000",
                "interestAccrualTime": "1773244800000",
                "listTime": "1743150759000",
                "maxSize": "6000000",
                "minSize": "10",
                "notionalCcy": "USDT",
                "optType": "P",
                "productId": "BTC-USDT-260327-54500-P",
                "quoteTime": "1773243808703",
                "redeemEndTime": "1774594800000",
                "redeemStartTime": "1773244800000",
                "stepSz": "1",
                "tradeEndTime": "1774584000000",
                "strike": "54500",
                "uly": "BTC-USD"
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
absYield | String | 绝对收益率  
annualizedYield | String | 年化收益率  
baseCcy | String | 基础币种  
quoteCcy | String | 报价币种  
notionalCcy | String | 投资币种。若 `C`，则为 baseCcy；若 `P`，则为 quoteCcy。  
expTime | String | 到期时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
interestAccrualTime | String | 利息开始计算时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
listTime | String | 产品上架时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
minSize | String | 最小交易规模（以投资币种计）  
maxSize | String | 最大交易规模（以投资币种计）  
optType | String | 期权类型  
`C`：看涨  
`P`：看跌  
productId | String | 产品ID  
quoteTime | String | 产品报价时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
redeemStartTime | String | 最早可申请提前赎回的时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
redeemEndTime | String | 最晚可申请提前赎回的时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
stepSz | String | 交易步长（以投资币种计）  
tradeEndTime | String | 交易截止时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
uly | String | 标的  
strike | String | 行权价  
  
### POST / 获取报价 

为双币赢产品请求实时报价。报价有有效期，须在到期前使用。

#### 限速：10次/60s

#### 限速规则：User ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/finance/sfp/dcd/quote`

> 请求示例
    
    
    POST /api/v5/finance/sfp/dcd/quote
    body
    {
        "productId": "BTC-USDT-260327-77000-C",
        "notionalSz": "1.5",
        "notionalCcy": "BTC"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
productId | String | 是 | 产品ID  
notionalSz | String | 是 | 投资数量  
notionalCcy | String | 是 | 投资币种  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "absYield": "0.00135182",
                "annualizedYield": "69.65",
                "interestAccrualTime": "1773241200000",
                "notionalSz": "0.001",
                "notionalCcy": "BTC",
                "productId": "BTC-USDT-260312-72000-C",
                "quoteId": "qtbcDCD-QUOTE17732395560537636",
                "validUntil": "1774584000000",
                "idxPx": "69000"
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
absYield | String | 绝对收益率  
annualizedYield | String | 年化收益率  
interestAccrualTime | String | 利息开始计算时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
notionalSz | String | 投资数量  
notionalCcy | String | 投资币种  
productId | String | 产品ID  
quoteId | String | 报价ID  
validUntil | String | 报价有效期，Unix时间戳的毫秒数格式，如 `1597026383085`  
idxPx | String | 指数价格  
  
### POST / 下单 

使用有效报价下单双币赢。

#### 限速：2次/60s

#### 限速规则：User ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/finance/sfp/dcd/trade`

> 请求示例
    
    
    POST /api/v5/finance/sfp/dcd/trade
    body
    {
        "quoteId": "quoterbpDCD-QUOTE17732116652401234"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
quoteId | String | 是 | 报价ID  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "quoteId": "quoterbpDCD-QUOTE17732116652401234",
                "ordId": "987654321",
                "state": "live"
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
quoteId | String | 报价ID  
ordId | String | 订单ID  
state | String | 订单状态  
`initial`：系统已接收请求，待处理  
`pending_book`：流动性提供商已接收请求，待处理  
`live`：交易已生效  
`rejected`：交易已拒绝  
  
### POST / 获取赎回报价 

为生效中的双币赢订单申请提前赎回报价。这是两步赎回流程的第一步，之后需调用 POST / 赎回 确认。

#### 限速：10次/60s

#### 限速规则：User ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/finance/sfp/dcd/redeem-quote`

> 请求示例
    
    
    POST /api/v5/finance/sfp/dcd/redeem-quote
    body
    {
        "ordId": "987654321"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
ordId | String | 是 | 订单ID  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "ordId": "987654321",
                "quoteId": "quoterbcDCD-REDEEM17732116652401234",
                "redeemCcy": "BTC",
                "redeemSz": "1.4856",
                "termRate": "-0.50",
                "validUntil": "1774598400000"
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
ordId | String | 订单ID  
quoteId | String | 报价ID  
redeemSz | String | 赎回数量  
redeemCcy | String | 赎回币种  
termRate | String | 期限利率  
validUntil | String | 赎回报价有效期，Unix时间戳的毫秒数格式，如 `1597026383085`  
  
### POST / 赎回 

使用有效的赎回报价确认提前赎回。这是两步赎回流程的第二步。

#### 限速：2次/60s

#### 限速规则：User ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/finance/sfp/dcd/redeem`

> 请求示例
    
    
    POST /api/v5/finance/sfp/dcd/redeem
    body
    {
        "ordId": "987654321",
        "quoteId": "quoterbcDCD-REDEEM17732116652401234"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
ordId | String | 是 | 订单ID  
quoteId | String | 是 | 报价ID  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "ordId": "987654321",
                "state": "pending_redeem_booking"
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
ordId | String | 订单ID  
state | String | 订单状态  
`pending_redeem_booking`：赎回请求已接收，等待流动性提供商确认  
`pending_redeem`：流动性提供商已确认，等待资金划转  
`redeeming`：赎回处理中  
`redeemed`：赎回完成  
  
### GET / 获取订单状态 

返回双币赢订单的当前状态。

#### 限速：3次/s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/finance/sfp/dcd/order-status`

> 请求示例
    
    
    GET /api/v5/finance/sfp/dcd/order-status?ordId=987654321
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
ordId | String | 是 | 订单ID  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "ordId": "987654321",
                "state": "live"
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
ordId | String | 订单ID  
state | String | 订单状态  
`initial`  
`live`  
`pending_settle`  
`settled`  
`pending_redeem`  
`redeemed`  
`rejected`  
  
### GET / 获取历史订单 

返回双币赢历史订单列表

#### 限速：1次/s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/finance/sfp/dcd/order-history`

> 请求示例
    
    
    GET /api/v5/finance/sfp/dcd/order-history
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
ordId | String | 否 | 订单ID。传入时直接返回该订单（忽略其他筛选条件）  
productId | String | 否 | 产品ID，如 `BTC-USDT-260327-77000-C`  
uly | String | 否 | 标的指数，如 `BTC-USD`  
state | String | 否 | 订单状态筛选  
`initial`  
`live`  
`pending_settle`  
`settled`  
`pending_redeem`  
`redeemed`  
`rejected`  
beginId | String | 否 | 返回比该订单ID更新的记录  
endId | String | 否 | 返回比该订单ID更早的记录  
begin | String | 否 | 开始时间戳筛选，Unix时间戳的毫秒数格式，如 `1597026383085`  
end | String | 否 | 结束时间戳筛选，Unix时间戳的毫秒数格式，如 `1597026383085`  
limit | String | 否 | 每次请求返回的结果数量，最大100  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "ordId": "987654321",
                "quoteId": "quoterbpDCD-QUOTE17732116652401234",
                "state": "settled",
                "productId": "BTC-USDT-260327-77000-C",
                "baseCcy": "BTC",
                "quoteCcy": "USDT",
                "uly": "BTC-USD",
                "strike": "77000",
                "notionalSz": "1.5",
                "notionalCcy": "BTC",
                "absYield": "0.00806038",
                "annualizedYield": "0.1834",
                "yieldSz": "0.01209057",
                "yieldCcy": "BTC",
                "settleSz": "1.51209057",
                "settleCcy": "BTC",
                "settlePx": "76500",
                "settleTime": "1774598400000",
                "expTime": "1774598400000",
                "redeemStartTime" : "1774598400000",
                "redeemEndime": "1774598400000",
                "cTime": "1773212400000",
                "uTime": "1773212400000"
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
ordId | String | 订单ID  
quoteId | String | 报价ID  
state | String | 订单状态  
`initial`  
`live`  
`pending_settle`  
`settled`  
`pending_redeem`  
`redeemed`  
`rejected`  
productId | String | 产品ID，如 `BTC-USDT-260327-77000-C`  
baseCcy | String | 基础币种，如 `BTC`  
quoteCcy | String | 计价币种，如 `USDT`  
uly | String | 标的指数，如 `BTC-USD`  
strike | String | 行权价  
notionalSz | String | 投资数量  
notionalCcy | String | 投资币种  
absYield | String | 绝对收益率  
annualizedYield | String | 年化收益率  
yieldSz | String | 收益金额  
yieldCcy | String | 收益币种  
settleSz | String | 结算金额（未结算时为""）  
settleCcy | String | 结算币种（未结算时为""）  
settlePx | String | 结算价格（未结算时为""）  
expTime | String | 产品到期时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
settleTime | String | 实际结算时间，Unix时间戳的毫秒数格式，如 `1597026383085`（未结算时为""）  
redeemStartTime | String | 最早可申请提前赎回的时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
redeemEndTime | String | 最晚可申请提前赎回的时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
cTime | String | 订单创建时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
uTime | String | 最后更新时间，Unix时间戳的毫秒数格式，如 `1597026383085`