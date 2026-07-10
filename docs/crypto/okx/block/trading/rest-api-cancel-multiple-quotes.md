---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#block-trading-rest-api-cancel-multiple-quotes
anchor_id: block-trading-rest-api-cancel-multiple-quotes
api_type: REST
updated_at: 2026-07-10 19:31:32.867709
---

# Cancel multiple Quotes

Cancel one or multiple active Quote(s) in a single batch. Maximum 100 quote orders can be canceled per request.  
  
#### Rate Limit: 2 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/rfq/cancel-batch-quotes`

> Request Example
    
    
    POST /api/v5/rfq/cancel-batch-quotes
    {
        "quoteIds": ["1150","1151","1152"],
        "clQuoteIds": ["q1","q2","q3"]
    }
    
    
    
    import okx.BlockTrading as BlockTrading
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading:0 , demo trading:1
    
    blockTradingAPI = BlockTrading.BlockTradingAPI(apikey, secretkey, passphrase, False, flag)
    
    # Cancel multiple quotes
    result = blockTradingAPI.cancel_batch_quotes(
        quoteIds=["1150","1151","1152"],
        clQuoteIds=["q1","q2","q3"]
    )
    print(result)
    

#### Request parameters

Parameter | Type | Required | Description  
---|---|---|---  
quoteIds | Array of strings | Conditional | Quote IDs .  
clQuoteIds | Array of strings | Conditional | Client-supplied Quote IDs. Either `quoteIds` or `clQuoteIds` is required.If both attributes are sent, `quoteIds` will be used as primary identifier.  
  
> Success - All requested Quotes canceled 
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "quoteId":"1150",
                "clQuoteId":"q1",
                "sCode":"0",
                "sMsg":""
            },
            {
                "quoteId":"1151",
                "clQuoteId":"q2",
                "sCode":"0",
                "sMsg":""
            },
            {
                "quoteId":"1152",
                "clQuoteId":"q3",
                "sCode":"0",
                "sMsg":""
            }
        ]
    }
    
    

> Partial cancellation 
    
    
    {
        "code":"2",
        "msg":"Bulk operation partially succeeded.",
        "data":[
            {
                "quoteId":"1150",
                "clQuoteId":"q1",
                "sCode":"0",
                "sMsg":""
            },
            {
                "quoteId":"1151",
                "clQuoteId":"q2",
                "sCode":"70001",
                "sMsg":"Quote does not exist."
            },
            {
                "quoteId":"1152",
                "clQuoteId":"q3",
                "sCode":"70001",
                "sMsg":"Quote does not exist."
            }
        ]
    }
    
    

> Failure example
    
    
    {
        "code":"1",
        "msg":"Operation failed.",
        "data":[
            {
                "quoteId":"1150",
                "clQuoteId":"q1",
                "sCode":"70001",
                "sMsg":"Quote does not exist."
            },
            {
                "quoteId":"1151",
                "clQuoteId":"q2",
                "sCode":"70001",
                "sMsg":"Quote does not exist."
            },
            {
                "quoteId":"1151",
                "clQuoteId":"q3",
                "sCode":"70001",
                "sMsg":"Quote does not exist."
            }
        ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
code | String | The result code, `0` means success.  
msg | String | The error message, not empty if the code is not 0.  
data | Array of objects | Array of objects containing the results  
> quoteId | String | Quote ID  
> clQuoteId | String | Client-supplied Quote ID.  
> sCode | String | The code of the event execution result, `0` means success.  
> sMsg | String | Rejection message if the request is unsuccessful.

---

# 批量取消报价单

取消一个或多个报价单，每次最多可以撤销100个订单。  
  
#### 限速: 2次/2s

#### 限速规则：User ID

#### 权限：交易

#### HTTP Requests

`POST /api/v5/rfq/cancel-batch-quotes`

> 请求示例
    
    
    POST /api/v5/rfq/cancel-batch-quotes
    {
        "quoteIds": ["1150","1151","1152"],
        "clQuoteIds": ["q1","q2","q3"]
    }
    
    
    
    import okx.BlockTrading as BlockTrading
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘：1
    
    blockTradingAPI = BlockTrading.BlockTradingAPI(apikey, secretkey, passphrase, False, flag)
    
    # 批量取消报价单
    result = blockTradingAPI.cancel_batch_quotes(
        quoteIds=["1150","1151","1152"],
        clQuoteIds=["q1","q2","q3"]
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
quoteIds | Array of strings | 可选 | 报价单ID  
clQuoteIds | Array of strings | 可选 | 报价单自定义ID，当 clQuoteIds 和 quoteIds 都传时，以 quoteIds 为准。  
  
> 全部成功的示例
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "quoteId":"1150",
                "clQuoteId":"q1",
                "sCode":"0",
                "sMsg":""
            },
            {
                "quoteId":"1151",
                "clQuoteId":"q2",
                "sCode":"0",
                "sMsg":""
            },
            {
                "quoteId":"1152",
                "clQuoteId":"q3",
                "sCode":"0",
                "sMsg":""
            }
        ]
    }
    
    

> 部分成功的示例 
    
    
    {
        "code":"2",
        "msg":"Bulk operation partially succeeded.",
        "data":[
            {
                "quoteId":"1150",
                "clQuoteId":"q1",
                "sCode":"0",
                "sMsg":""
            },
            {
                "quoteId":"1151",
                "clQuoteId":"q2",
                "sCode":"70001",
                "sMsg":"Quote does not exist."
            },
            {
                "quoteId":"1152",
                "clQuoteId":"q3",
                "sCode":"70001",
                "sMsg":"Quote does not exist."
            }
        ]
    }
    
    

> 失败示例
    
    
    {
        "code":"1",
        "msg":"Operation failed.",
        "data":[
            {
                "quoteId":"1150",
                "clQuoteId":"q1",
                "sCode":"70001",
                "sMsg":"Quote does not exist."
            },
            {
                "quoteId":"1151",
                "clQuoteId":"q2",
                "sCode":"70001",
                "sMsg":"Quote does not exist."
            },
            {
                "quoteId":"1151",
                "clQuoteId":"q3",
                "sCode":"70001",
                "sMsg":"Quote does not exist."
            }
        ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
code | String | 结果代码，0 表示成功。  
msg | String | 错误信息，如果代码不为 0，则不为空。  
data | Array of objects | 包含结果的对象数组  
> quoteId | String | 报价单ID  
> clQuoteId | String | 报价单自定义ID  
> sCode | String | 事件执行结果的code，0代表成功  
> sMsg | String | 事件执行失败时的msg