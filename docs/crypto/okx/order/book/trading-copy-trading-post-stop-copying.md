---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-copy-trading-post-stop-copying
anchor_id: order-book-trading-copy-trading-post-stop-copying
api_type: API
updated_at: 2026-07-20 19:36:09.220264
---

# POST / Stop copying

You need to use this endpoint to stop copy trading  
  
#### Rate limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP request

`POST /api/v5/copytrading/stop-copy-trading`

> Request example
    
    
    POST /api/v5/copytrading/stop-copy-trading
    body
    {
        "instType": "SWAP",
        "uniqueCode": "25CD5A80241D6FE6",
        "subPosCloseType": "manual_close"
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instType | String | No | Instrument type  
`SWAP`  
uniqueCode | String | Yes | Lead trader unique code  
A combination of case-sensitive alphanumerics, all numbers and the length is 16 or 18 characters, e.g. 213E8C92DC61EFAC (16 characters) or 381749205163847291 (18 characters)  
subPosCloseType | String | Yes | Action type for open positions, it is required if you have related copy position  
`market_close`: immediately close at market price  
`copy_close`：close when trader closes  
`manual_close`: close manually  
  
> Response example
    
    
    {
        "code": "0",
        "data": [
            {
                "result": true
            }
        ],
        "msg": ""
    }
    

#### Response parameters

**Parameter** | **Type** | **Description**  
---|---|---  
result | Boolean | The result of setting   
`true`

---

# POST / 停止跟单

该接口用来停止跟单  
  
  
#### 限速：5次/2s

#### 限速规则：User ID

#### HTTP请求

`POST /api/v5/copytrading/stop-copy-trading`

> 请求示例
    
    
    POST /api/v5/copytrading/stop-copy-trading
    body
    {
        "instType": "SWAP",
        "uniqueCode": "25CD5A80241D6FE6",
        "subPosCloseType": "manual_close"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instType | String | 否 | 产品类型  
`SWAP`：永续合约，默认值  
uniqueCode | String | 是 | 带单交易员唯一标识码。  
数字加字母组合 长度为16或18位，如：213E8C92DC61EFAC（16位）或381749205163847291（18位）  
subPosCloseType | String | 可选 | 剩余仓位处理方式，有相关的跟单条目时必填  
`market_close`: 立即市价全平  
`copy_close`：跟随交易员平仓  
`manual_close`: 手动处理  
  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "result": true
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
result | Boolean | 设置结果  
`true`：设置成功