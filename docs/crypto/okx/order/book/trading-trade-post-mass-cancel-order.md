---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-trade-post-mass-cancel-order
anchor_id: order-book-trading-trade-post-mass-cancel-order
api_type: API
updated_at: 2026-07-11 19:12:32.870661
---

# POST / Mass cancel order

Cancel all the MMP pending orders of an instrument family.  
  
  
Only applicable to Option in Portfolio Margin mode, and MMP privilege is required.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/trade/mass-cancel`

> Request Example
    
    
    POST /api/v5/trade/mass-cancel
    body
    {
        "instType":"OPTION",
        "instFamily":"BTC-USD"
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instType | String | Yes | Instrument type  
`OPTION`  
instFamily | String | Yes | Instrument family  
lockInterval | String | No | Lock interval(ms)  
The range should be [0, 10 000]  
The default is 0. You can set it as "0" if you want to unlock it immediately.  
Error 54008 will be returned when placing order during lock interval, it is different from 51034 which is thrown when MMP is triggered  
  
> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "result":true
            }
        ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
result | Boolean | Result of the request `true`, `false`

---

# POST / 撤销 MMP 订单

撤销同一交易品种下用户所有的 MMP 挂单  
仅适用于组合保证金账户模式下的期权订单，且有 MMP 权限。  
  
#### 限速：5次/2s

#### 限速规则：User ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/trade/mass-cancel`

> 请求示例
    
    
    POST /api/v5/trade/mass-cancel
    body
    {
        "instType":"OPTION",
        "instFamily":"BTC-USD"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instType | String | 是 | 交易产品类型  
`OPTION`:期权  
instFamily | String | 是 | 交易品种  
lockInterval | String | 否 | 锁定时长(毫秒)  
范围应为[0, 10 000]  
默认为 0. 如果想要立即解锁，您可以设置为 "0"  
下单时，如果在该锁定期间，会报错 54008，如果在 MMP 触发期间，会报错 51034  
  
> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "result":true
            }
        ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
result | Boolean | 撤单结果  
`true`：全部撤单成功  
`false`：全部撤单失败