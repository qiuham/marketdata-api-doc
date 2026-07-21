---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#block-trading-rest-api-cancel-all-quotes
anchor_id: block-trading-rest-api-cancel-all-quotes
api_type: REST
updated_at: 2026-07-21 19:26:34.513708
---

# Cancel all Quotes

Cancels all active Quotes.  
  
#### Rate Limit: 2 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/rfq/cancel-all-quotes`

> Request Example
    
    
    POST /api/v5/rfq/cancel-all-quotes
    
    
    
    
    import okx.BlockTrading as BlockTrading
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading:0 , demo trading:1
    
    blockTradingAPI = BlockTrading.BlockTradingAPI(apikey, secretkey, passphrase, False, flag)
    
    # Cancel all quotes
    result = blockTradingAPI.cancel_all_quotes()
    print(result)
    

#### Request parameters

None

> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "ts":"1697026383085"
            }
        ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
code | String | The result code, `0` means success.  
msg | String | The error message, not empty if the code is not 0.  
data | Array of objects | Array of objects containing the results  
> ts | String | The timestamp of cancellation successfully. Unix timestamp format in milliseconds, e.g. 1597026383085.

---

# 取消所有报价单

取消所有报价单  
  
#### 限速: 2次/2s

#### 限速规则：User ID

#### HTTP Requests

`POST /api/v5/rfq/cancel-all-quotes`

> 请求示例
    
    
    POST /api/v5/rfq/cancel-all-quotes
    
    
    
    
    import okx.BlockTrading as BlockTrading
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘：1
    
    blockTradingAPI = BlockTrading.BlockTradingAPI(apikey, secretkey, passphrase, False, flag)
    
    # 取消所有报价单
    result = blockTradingAPI.cancel_all_quotes()
    print(result)
    

#### 请求参数

无

> 响应示例
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "ts":"1697026383085"
            }
        ]
    }
    

#### 响应参数

参数名 | 类型 | 描述  
---|---|---  
code | String | 结果代码，0 表示成功。  
msg | String | 错误信息，如果代码不为 0，则不为空。  
data | Array of objects | 包含结果的对象数组  
> ts | String | 成功取消时间，Unix时间戳的毫秒数格式，如 1597026383085。