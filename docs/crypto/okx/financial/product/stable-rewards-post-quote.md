---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#financial-product-stable-rewards-post-quote
anchor_id: financial-product-stable-rewards-post-quote
api_type: API
updated_at: 2026-07-13 19:29:30.949802
---

# POST / Quote

Request a quote before subscribing or redeeming. Only the assets in the funding account can be used. The returned `quoteId` must be submitted via `POST /trade` before `ttlMs` expires.  
  
#### Rate Limit: 2 requests per second

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/finance/stable-rewards/quote`

> Request Example
    
    
    POST /api/v5/finance/stable-rewards/quote
    body
    {
        "ccy": "USDG",
        "settleCcy": "USDT",
        "action": "subscribe",
        "amt": "1000"
    }
    

#### Request Parameters

**Parameter** | **Type** | **Required** | **Description**  
---|---|---|---  
ccy | String | Yes | Stablecoin to subscribe or redeem, e.g. `USDG`  
settleCcy | String | Yes | Settlement currency, e.g. `USDC`, `USDT`  
action | String | Yes | Action type  
`subscribe`  
`redeem`  
amt | String | Yes | Transaction amount  
For `subscribe`: denominated in `settleCcy`  
For `redeem`: denominated in `ccy`  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "quoteId": "1234567890",
                "quoteAmt": "998.88",
                "quoteCcy": "USDG",
                "exchRate": "0.99888110",
                "feeRate": "0.0003",
                "quoteTime": "1620282889345",
                "ttlMs": "10000"
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
quoteId | String | Quote ID. Submit this value via `POST /trade` before `ttlMs` expires to execute the transaction  
quoteAmt | String | Target amount denominated in `quoteCcy`  
quoteCcy | String | Currency of `quoteAmt`  
For `subscribe`: returns `ccy` (the stablecoin received)  
For `redeem`: returns `settleCcy` (the settlement currency received)  
exchRate | String | Exchange rate, 8 decimals  
For `subscribe`: units of `ccy` received per unit of `settleCcy`  
For `redeem`: units of `settleCcy` received per unit of `ccy`  
feeRate | String | Fee rate applied to this quote, e.g. `0.0003` represents `0.03%`  
quoteTime | String | Quotation generation time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
ttlMs | String | Quotation validity period in milliseconds, e.g. `10000` means the quote is valid for 10 seconds

---

# POST / 询价

在订阅或赎回前发起询价。仅资金账户中的资产可用于订阅。返回的 `quoteId` 须在 `ttlMs` 过期前通过 `POST /trade` 接口提交以完成交易。  
  
#### 限速：2次/s

#### 限速规则：User ID

#### 权限：交易

#### HTTP 请求

`POST /api/v5/finance/stable-rewards/quote`

> 请求示例
    
    
    POST /api/v5/finance/stable-rewards/quote
    body
    {
        "ccy": "USDG",
        "settleCcy": "USDT",
        "action": "subscribe",
        "amt": "1000"
    }
    

#### 请求参数

**参数名** | **类型** | **是否必须** | **描述**  
---|---|---|---  
ccy | String | 是 | 订阅或赎回的稳定币，如 `USDG`  
settleCcy | String | 是 | 结算币种，如 `USDC`、`USDT`  
action | String | 是 | 操作类型  
`subscribe`：订阅  
`redeem`：赎回  
amt | String | 是 | 交易数量  
`subscribe` 时以 `settleCcy` 计价  
`redeem` 时以 `ccy` 计价  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "quoteId": "1234567890",
                "quoteAmt": "998.88",
                "quoteCcy": "USDG",
                "exchRate": "0.99888110",
                "feeRate": "0.0003",
                "quoteTime": "1620282889345",
                "ttlMs": "10000"
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
quoteId | String | 报价 ID。须在 `ttlMs` 过期前通过 `POST /trade` 提交以完成交易  
quoteAmt | String | 报价数量，以 `quoteCcy` 计价  
quoteCcy | String | `quoteAmt` 对应的币种  
`subscribe` 时返回 `ccy`（用户获得的稳定币）  
`redeem` 时返回 `settleCcy`（用户获得的结算币种）  
exchRate | String | 兑换汇率，精度为 8 位小数  
`subscribe` 时：1 单位 `settleCcy` 可兑换的 `ccy` 数量  
`redeem` 时：1 单位 `ccy` 可兑换的 `settleCcy` 数量  
feeRate | String | 本次报价的手续费率，如 `0.0003` 代表 `0.03%`  
quoteTime | String | 报价生成时间，Unix 时间戳，单位为毫秒，如 `1597026383085`  
ttlMs | String | 报价有效期，单位为毫秒，如 `10000` 代表报价 10 秒内有效