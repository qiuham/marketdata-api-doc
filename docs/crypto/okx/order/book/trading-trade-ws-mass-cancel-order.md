---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-trade-ws-mass-cancel-order
anchor_id: order-book-trading-trade-ws-mass-cancel-order
api_type: WebSocket
updated_at: 2026-07-04 19:37:39.698682
---

# WS / Mass cancel order

Cancel all the MMP pending orders of an instrument family.  

Only applicable to Option in Portfolio Margin mode, and MMP privilege is required.

#### URL Path

/ws/v5/private (required login)

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

Rate limit is shared with the `Mass Cancel Order` REST API endpoints 

> Request Example
    
    
    {
        "id": "1512",
        "op": "mass-cancel",
        "args": [{
            "instType":"OPTION",
            "instFamily":"BTC-USD"
        }]
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
id | String | Yes | Unique identifier of the message   
Provided by client. It will be returned in response message for identifying the corresponding request.   
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
op | String | Yes | Operation  
`mass-cancel`  
args | Array of objects | Yes | Request parameters  
> instType | String | Yes | Instrument type  
`OPTION`  
> instFamily | String | Yes | Instrument family  
> lockInterval | String | No | Lock interval(ms)  
The range should be [0, 10 000]  
The default is 0. You can set it as "0" if you want to unlock it immediately.  
Error 54008 will be returned when placing order during lock interval, it is different from 51034 which is thrown when MMP is triggered  
  
> ##### Successful Response Example
    
    
    {
        "id": "1512",
        "op": "mass-cancel",
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
      "op": "mass-cancel",
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

# WS / 撤销 MMP 订单

撤销同一交易品种下用户所有的 MMP 挂单  
仅适用于组合保证金账户模式下的期权订单，且有 MMP 权限。  
  
#### 服务地址

/ws/v5/private (需要登录)

#### 限速：5次/2s

#### 限速规则：User ID

同`撤销 MMP 订单` REST API 共享限速 

> 请求示例
    
    
    {
        "id": "1512",
        "op": "mass-cancel",
        "args": [{
            "instType":"OPTION",
            "instFamily":"BTC-USD"
        }]
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
id | String | 是 | 消息的唯一标识   
用户提供，返回参数中会返回以便于找到相应的请求。  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度必须要在1-32位之间。  
op | String | 是 | 支持的业务操作，如 `mass-cancel`  
args | Array of objects | 是 | 请求参数  
> instType | String | 是 | 交易产品类型  
`OPTION`:期权  
> instFamily | String | 是 | 交易品种  
> lockInterval | String | 否 | 锁定时长(毫秒)  
范围应为[0, 10 000]  
默认为 0. 如果想要立即解锁，您可以设置为 "0"  
下单时，如果在该锁定期间，会报错 54008，如果在 MMP 触发期间，会报错 51034  
  
> 成功返回示例
    
    
    {
        "id": "1512",
        "op": "mass-cancel",
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
        "op": "mass-cancel",
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