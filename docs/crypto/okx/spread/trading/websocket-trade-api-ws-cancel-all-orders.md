---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#spread-trading-websocket-trade-api-ws-cancel-all-orders
anchor_id: spread-trading-websocket-trade-api-ws-cancel-all-orders
api_type: WebSocket
updated_at: 2026-05-27 19:36:02.925852
---

# WS / Cancel all orders

#### URL Path

/ws/v5/business (required login)

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

> Request Example
    
    
    {
        "id": "1512",
        "op": "sprd-mass-cancel",
        "args": [{
            "sprdId": "BTC-USDT_BTC-USDT-SWAP"
        }]
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
id | String | Yes | Unique identifier of the message provided by client. It will be returned in response message to identify the corresponding request.   
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
op | String | Yes | Operation  
`sprd-mass-cancel`  
args | Array of objects | Yes | Request parameters  
> sprdId | String | No | spread ID  
  
> ##### Successful Response Example
    
    
    {
        "id": "1512",
        "op": "sprd-mass-cancel",
        "data": [
            {
                "result": true
            }
        ],
        "code": "0",
        "msg": ""
    } 
    

> Response Example When Format Error
    
    
    {
      "id": "1512",
      "op": "sprd-mass-cancel",
      "data": [],
      "code": "60013",
      "msg": "Invalid args"
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
id | String | Unique identifier of the message  
op | String | Operation  
code | String | Error Code  
msg | String | Error message  
data | Array of objects | Data  
> result | Boolean | Result of the request `true`, `false`

---

# WS / 全部撤单

#### 服务地址

/ws/v5/business (需要登录)

#### 限速：5次/2s

#### 限速规则：User ID

> 请求示例
    
    
    {
        "id": "1512",
        "op": "sprd-mass-cancel",
        "args": [{
            "sprdId":"BTC-USDT_BTC-USDT-SWAP"
        }]
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
id | String | 是 | 消息的唯一标识   
用户提供，返回参数中会返回以便于找到相应的请求。  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度必须要在1-32位之间。  
op | String | 是 | 支持的业务操作，`sprd-mass-cancel`  
args | Array of objects | 是 | 请求参数  
> sprdId | String | 否 | 价差ID  
  
> 成功返回示例
    
    
    {
        "id": "1512",
        "op": "sprd-mass-cancel",
        "data": [
            {
                "result": true
            }
        ],
        "code": "0",
        "msg": ""
    } 
    

> 格式错误返回示例
    
    
    {
        "id": "1512",
        "op": "sprd-mass-cancel",
        "data": [],
        "code": "60013",
        "msg": "Invalid args"
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
id | String | 消息的唯一标识  
op | String | 业务操作  
code | String | 代码  
msg | String | 消息  
data | Array of objects | 请求成功后返回的数据  
> result | Boolean | 撤单结果  
`true`：全部撤单成功  
`false`：全部撤单失败