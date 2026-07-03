---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#block-trading-rest-api-cancel-rfq
anchor_id: block-trading-rest-api-cancel-rfq
api_type: REST
updated_at: 2026-07-03 19:40:02.703062
---

# Cancel RFQ

Cancel an existing active RFQ that you have created previously.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/rfq/cancel-rfq`

> Request Example
    
    
    POST /api/v5/rfq/cancel-rfq
    {
        "rfqId":"22535",
        "clRfqId":"rfq001"
    }
    
    
    
    import okx.BlockTrading as BlockTrading
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading:0 , demo trading:1
    
    blockTradingAPI = BlockTrading.BlockTradingAPI(apikey, secretkey, passphrase, False, flag)
    
    # Cancel RFQ
    result = blockTradingAPI.cancel_rfq(
        rfqId="22535",
        clRfqId="rfq001"
    )
    print(result)
    

#### Request parameters

Parameter | Type | Required | Description  
---|---|---|---  
rfqId | String | Conditional | RFQ ID created .  
clRfqId | String | Conditional | Client-supplied RFQ ID.   
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.   
Either rfqId or clRfqId is required. If both are passed, rfqId will be used.  
  
> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "rfqId":"22535",
                "clRfqId":"rfq001",
                "sCode":"0",
                "sMsg":""
            }
        ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
code | String | The result code, `0` means success.  
msg | String | The error message, not empty if the code is not 0.  
data | Array of objects | Array of objects containing the results  
> rfqId | String | RFQ ID  
> clRfqId | String | Client-supplied RFQ ID.  
> sCode | String | The code of the event execution result, `0` means success.  
> sMsg | String | Rejection message if the request is unsuccessful.

---

# 取消询价单

取消一个询价单。

#### 限速: 5次/2s

#### 限速规则：User ID

#### 权限：交易

#### HTTP Requests

`POST /api/v5/rfq/cancel-rfq`

> 请求示例
    
    
    POST /api/v5/rfq/cancel-rfq
    {
        "rfqId":"22535",
        "clRfqId":"rfq001"
    }
    
    
    
    import okx.BlockTrading as BlockTrading
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘：1
    
    blockTradingAPI = BlockTrading.BlockTradingAPI(apikey, secretkey, passphrase, False, flag)
    
    # 取消询价单
    result = blockTradingAPI.cancel_rfq(
        rfqId="22535",
        clRfqId="rfq001"
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
rfqId | String | 可选 | 询价单ID  
clRfqId | String | 可选 | 询价单自定义ID，字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度要在1-32位之间。  
当 clRfqId 和 rfqId 都传时，以 rfqId 为准。  
  
> 返回示例
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "rfqId":"22535",
                "clRfqId":"rfq001",
                "sCode":"0",
                "sMsg":""
            }
        ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
code | String | 结果代码，0 表示成功。  
msg | String | 错误信息，如果代码不为 0，则不为空。  
data | Array of objects | 包含结果的对象数组  
> rfqId | String | RFQ ID  
> clRfqId | String | 由用户设置的 RFQ ID  
> sCode | String | 事件执行结果的code，0代表成功  
> sMsg | String | 事件执行失败时的msg