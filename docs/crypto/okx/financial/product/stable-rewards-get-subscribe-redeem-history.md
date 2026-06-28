---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#financial-product-stable-rewards-get-subscribe-redeem-history
anchor_id: financial-product-stable-rewards-get-subscribe-redeem-history
api_type: API
updated_at: 2026-05-27 19:36:54.659588
---

# GET / Subscribe redeem history

Retrieve subscription and redemption records. Results are returned in reverse chronological order.  
  
#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/finance/stable-rewards/subscribe-redeem-history`

> Request Example
    
    
    GET /api/v5/finance/stable-rewards/subscribe-redeem-history?ccy=USDG
    

#### Request Parameters

**Parameter** | **Type** | **Required** | **Description**  
---|---|---|---  
ccy | String | Yes | Stablecoin, e.g. `USDG`  
type | String | No | Record type  
`subscribe`  
`redeem`  
Returns both types if not specified  
status | String | No | Order status  
`pending`  
`success`  
`failed`  
Returns all statuses if not specified  
after | String | No | Pagination of data to return records earlier than the requested `ordId`  
before | String | No | Pagination of data to return records newer than the requested `ordId`  
limit | String | No | Number of results per request. The default is `100`. The maximum is `100`  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "type": "subscribe",
                "status": "success",
                "ccy": "USDG",
                "settleCcy": "USDT",
                "ccyAmt": "998.88",
                "settleCcyAmt": "1000",
                "fee": "0.3",
                "quoteId": "1234567890",
                "ordId": "987654321",
                "ts": "1718035200000"
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
type | String | Record type  
`subscribe`  
`redeem`  
status | String | Order status  
`pending`  
`success`  
`failed`  
ccy | String | Stablecoin subscribed or redeemed, e.g. `USDG`  
settleCcy | String | Settlement currency, e.g. `USDC`, `USDT`  
ccyAmt | String | Amount denominated in `ccy`  
settleCcyAmt | String | Amount denominated in `settleCcy`  
fee | String | Fee charged, denominated in `settleCcy`  
quoteId | String | Quote ID  
ordId | String | Order ID  
ts | String | Order creation time, Unix timestamp format in milliseconds, e.g. `1597026383085`

---

# GET / 获取订阅赎回历史

查询订阅与赎回记录，按时间倒序返回。  
  
#### 限速：5次/2s

#### 限速规则：User ID

#### 权限：读取

#### HTTP 请求

`GET /api/v5/finance/stable-rewards/subscribe-redeem-history`

> 请求示例
    
    
    GET /api/v5/finance/stable-rewards/subscribe-redeem-history?ccy=USDG
    

#### 请求参数

**参数名** | **类型** | **是否必须** | **描述**  
---|---|---|---  
ccy | String | 是 | 稳定币，如 `USDG`  
type | String | 否 | 记录类型  
`subscribe`：订阅  
`redeem`：赎回  
不传则返回全部类型  
status | String | 否 | 订单状态  
`pending`：处理中  
`success`：成功  
`failed`：失败  
不传则返回全部状态  
after | String | 否 | 请求此 `ordId` 之前（更早时间）的分页内容  
before | String | 否 | 请求此 `ordId` 之后（更新时间）的分页内容  
limit | String | 否 | 分页返回的结果数量。默认 `100`，最大 `100`  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "type": "subscribe",
                "status": "success",
                "ccy": "USDG",
                "settleCcy": "USDT",
                "ccyAmt": "998.88",
                "settleCcyAmt": "1000",
                "fee": "0.3",
                "quoteId": "1234567890",
                "ordId": "987654321",
                "ts": "1718035200000"
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
type | String | 记录类型  
`subscribe`：订阅  
`redeem`：赎回  
status | String | 订单状态  
`pending`：处理中  
`success`：成功  
`failed`：失败  
ccy | String | 订阅/赎回的稳定币，如 `USDG`  
settleCcy | String | 结算币种，如 `USDC`、`USDT`  
ccyAmt | String | 以 `ccy` 计价的数量  
settleCcyAmt | String | 以 `settleCcy` 计价的数量  
fee | String | 订阅/赎回手续费，以 `settleCcy` 计价  
quoteId | String | 报价 ID  
ordId | String | 订单 ID  
ts | String | 订单创建时间，Unix 时间戳，单位为毫秒，如 `1597026383085`