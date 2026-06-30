---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#block-trading-rest-api-reset-mmp-status
anchor_id: block-trading-rest-api-reset-mmp-status
api_type: REST
updated_at: 2026-06-30 19:55:21.748198
---

# Reset MMP status

Reset the MMP status to be inactive.  
  
#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/rfq/mmp-reset`

> Request Example
    
    
    POST /api/v5/rfq/mmp-reset
    
    
    
    
    import okx.BlockTrading as BlockTrading
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading:0 , demo trading:1
    
    blockTradingAPI = BlockTrading.BlockTradingAPI(apikey, secretkey, passphrase, False, flag)
    
    # Reset MMP status
    result = blockTradingAPI.reset_mmp()
    print(result)
    

#### Request parameters

None

> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "ts":"1597026383085"
            }
        ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
code | String | The result code, `0` means success.  
msg | String | The error message, not empty if the code is not `0`.  
data | Array of objects | Array of objects containing the results.  
> ts | String | The timestamp of re-setting successfully. Unix timestamp format in milliseconds, e.g. `1597026383085`.

---

# 重设MMP状态

重设MMP状态为无效。  
  
#### 限速: 5次/2s

#### 限速规则：User ID

#### 权限：交易

#### HTTP Requests

`POST /api/v5/rfq/mmp-reset`

> 请求示例
    
    
    POST /api/v5/rfq/mmp-reset
    
    
    
    
    import okx.BlockTrading as BlockTrading
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘：1
    
    blockTradingAPI = BlockTrading.BlockTradingAPI(apikey, secretkey, passphrase, False, flag)
    
    # 重设MMP状态
    result = blockTradingAPI.reset_mmp()
    print(result)
    

#### 请求参数

None

> 
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "ts":"1597026383085"
            }
        ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
code | String | 结果代码，`0` 表示成功  
msg | String | 错误信息，如果代码不为`0`，则不为空  
data | Array of objects | 请求返回值，包含请求结果  
> ts | String | 重设时间. Unix 时间戳的毫秒数格式，如 `1597026383085`.