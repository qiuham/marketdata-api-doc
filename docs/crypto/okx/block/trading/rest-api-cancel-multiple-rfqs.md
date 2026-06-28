---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#block-trading-rest-api-cancel-multiple-rfqs
anchor_id: block-trading-rest-api-cancel-multiple-rfqs
api_type: REST
updated_at: 2026-06-28 19:37:29.146064
---

# Cancel multiple RFQs

Cancel one or multiple active RFQ(s) in a single batch. Maximum 100 RFQ orders can be canceled per request.  
  
#### Rate Limit: 2 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/rfq/cancel-batch-rfqs`

> Request Example
    
    
    POST /api/v5/rfq/cancel-batch-rfqs
    {
        "rfqIds":[
            "2201",
            "2202",
            "2203"
        ],
        "clRfqIds":[
            "r1",
            "r2",
            "r3"
        ]
    }
    
    
    
    import okx.BlockTrading as BlockTrading
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading:0 , demo trading:1
    
    blockTradingAPI = BlockTrading.BlockTradingAPI(apikey, secretkey, passphrase, False, flag)
    
    # Cancel multiple RFQs
    result = blockTradingAPI.cancel_batch_rfqs(
        rfqIds=[
            "2201",
            "2202",
            "2203"
        ],
        clRfqIds=[
            "r1",
            "r2",
            "r3"
        ],
    )
    print(result)
    
    

#### Request parameters

Parameter | Type | Required | Description  
---|---|---|---  
rfqIds | Array of strings | Conditional | RFQ IDs .  
clRfqIds | Array of strings | Conditional | Client-supplied RFQ IDs.   
Either `rfqIds` or `clRfqIds` is required.   
If both attributes are sent, `rfqIds` will be used as primary identifier.  
  
> Success - All requested RFQs canceled 
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "rfqId":"2201",
                "clRfqId":"r1",
                "sCode":"0",
                "sMsg":""
            },
            {
                "rfqId":"2202",
                "clRfqId":"r2",
                "sCode":"0",
                "sMsg":""
            },
            {
                "rfqId":"2203",
                "clRfqId":"r3",
                "sCode":"0",
                "sMsg":""
            }
        ]
    }
    
    

> Partial cancellation 
    
    
    {
        "code":"2",
        "msg":"Bulk operation partially ",
        "data":[
            {
                "rfqId":"2201",
                "clRfqId":"r1",
                "sCode":"70000",
                "sMsg":"RFQ does not exist."
            },
            {
                "rfqId":"2202",
                "clRfqId":"r2",
                "sCode":"0",
                "sMsg":""
            },
            {
                "rfqId":"2203",
                "clRfqId":"r3",
                "sCode":"0",
                "sMsg":""
            }
        ]
    }
    
    

> Failure example
    
    
    {
        "code":"1",
        "msg":"Operation failed.",
        "data":[
            {
                "rfqId":"2201",
                "clRfqId":"r1",
                "sCode":"70000",
                "sMsg":"RFQ does not exist."
            },
            {
                "rfqId":"2202",
                "clRfqId":"r2",
                "sCode":"70000",
                "sMsg":"RFQ does not exist."
            },
            {
                "rfqId":"2203",
                "clRfqId":"r3",
                "sCode":"70000",
                "sMsg":"RFQ does not exist."
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

# 批量取消询价单

取消一个或多个询价单，每次最多可以撤销100个询价单。  
  
#### 限速: 2次/2s

#### 限速规则：User ID

#### 权限：交易

#### HTTP Requests

`POST /api/v5/rfq/cancel-batch-rfqs`

> 请求示例
    
    
    POST /api/v5/rfq/cancel-batch-rfqs
    {
        "rfqIds":[
            "2201",
            "2202",
            "2203"
        ],
        "clRfqIds":[
            "r1",
            "r2",
            "r3"
        ]
    }
    
    
    
    import okx.BlockTrading as BlockTrading
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘：1
    
    blockTradingAPI = BlockTrading.BlockTradingAPI(apikey, secretkey, passphrase, False, flag)
    
    # 批量取消询价单
    result = blockTradingAPI.cancel_batch_rfqs(
        rfqIds=[
            "2201",
            "2202",
            "2203"
        ],
        clRfqIds=[
            "r1",
            "r2",
            "r3"
        ],
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
rfqIds | Array of strings | 可选 | 询价单IDs  
clRfqIds | Array of strings | 可选 | 询价单自定义ID，当 clRfqIds 和 rfqIds 都传时，以 rfqIds 为准。  
  
> 全部成功示例 
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "rfqId":"2201",
                "clRfqId":"r1",
                "sCode":"0",
                "sMsg":""
            },
            {
                "rfqId":"2202",
                "clRfqId":"r2",
                "sCode":"0",
                "sMsg":""
            },
            {
                "rfqId":"2203",
                "clRfqId":"r3",
                "sCode":"0",
                "sMsg":""
            }
        ]
    }
    
    

> 部分成功示例
    
    
    {
        "code":"2",
        "msg":"Bulk operation partially ",
        "data":[
            {
                "rfqId":"2201",
                "clRfqId":"r1",
                "sCode":"70000",
                "sMsg":"RFQ does not exist."
            },
            {
                "rfqId":"2202",
                "clRfqId":"r2",
                "sCode":"0",
                "sMsg":""
            },
            {
                "rfqId":"2203",
                "clRfqId":"r3",
                "sCode":"0",
                "sMsg":""
            }
        ]
    }
    
    

> 失败示例
    
    
    {
        "code":"1",
        "msg":"Operation failed.",
        "data":[
            {
                "rfqId":"2201",
                "clRfqId":"r1",
                "sCode":"70000",
                "sMsg":"RFQ does not exist."
            },
            {
                "rfqId":"2202",
                "clRfqId":"r2",
                "sCode":"70000",
                "sMsg":"RFQ does not exist."
            },
            {
                "rfqId":"2203",
                "clRfqId":"r3",
                "sCode":"70000",
                "sMsg":"RFQ does not exist."
            }
        ]
    }
    
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
code | String | 结果代码，0 表示成功。  
msg | String | 错误信息，如果代码不为 0，则不为空。  
data | Array of objects | 包含结果的对象数组  
> rfqId | String | 询价单ID  
> clRfqId | String | 询价单自定义ID.  
> sCode | String | 事件执行结果的code，0代表成功  
> sMsg | String | 事件执行失败时的msg