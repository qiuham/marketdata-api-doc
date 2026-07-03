---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#block-trading-rest-api-execute-quote
anchor_id: block-trading-rest-api-execute-quote
api_type: REST
updated_at: 2026-07-03 19:40:03.646897
---

# Execute Quote

Executes a Quote. It is only used by the creator of the RFQ  
  
#### Rate Limit: 2 requests per 3 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/rfq/execute-quote`

> Request Example
    
    
    POST /api/v5/rfq/execute-quote
    {
        "rfqId":"22540",
        "quoteId":"84073",
        "legs":[
            {
                "sz":"25",
                "instId":"BTC-USD-20220114-13250-C"
            },
            {
                "sz":"25",
                "instId":"BTC-USDT"
            }
         ]
    }
    
    
    
    import okx.BlockTrading as BlockTrading
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading:0 , demo trading:1
    
    blockTradingAPI = BlockTrading.BlockTradingAPI(apikey, secretkey, passphrase, False, flag)
    
    # Execute quote
    result = blockTradingAPI.execute_quote(
        rfqId="22540",
        quoteId="84073"
    )
    print(result)
    
    

#### Request parameters

Parameter | Type | Required | Description  
---|---|---|---  
rfqId | String | Yes | RFQ ID .  
quoteId | String | Yes | Quote ID.  
legs | Array of objects | No | An Array of objects containing the execution size of each leg of the RFQ.   
The ratio of the leg sizes needs to be the same as the RFQ.   
*Note: `tgtCcy` and `side` of each leg will be same as ones in the RFQ. `px` will be the same as the ones in the Quote.  
> instId | String | Yes | The Instrument ID, for example: "BTC-USDT-SWAP".  
> sz | String | Yes | The size of each leg  
  
> Response Example
    
    
    {  
       "code":"0",
       "msg":"",
       "data":[
           {
                "blockTdId":"180184",
                "rfqId":"1419",
                "clRfqId":"r0001",
                "quoteId":"1046",
                "clQuoteId":"q0001",
                "tag":"123456",
                "tTraderCode":"Trader1",
                "mTraderCode":"Trader2",
                "cTime":"1649670009",
                "legs":[
                    {
                        "px":"0.1",
                        "sz":"25",
                        "instId":"BTC-USD-20220114-13250-C",
                        "side":"sell",
                        "fee":"-1.001",
                        "feeCcy":"BTC",
                        "tradeId":"10211"
                    },
                    {
                        "px":"0.2",
                        "sz":"25",
                        "instId":"BTC-USDT",
                        "side":"buy",
                        "fee":"-1.001",
                        "feeCcy":"BTC",
                        "tradeId":"10212"
                    }
                ]
            }
       ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
code | String | The result code, `0` means success.  
msg | String | The error message, not empty if the code is not 0.  
data | Array of objects | Array of objects containing the results  
> cTime | String | The execution time for the trade. Unix timestamp in milliseconds.  
> rfqId | String | RFQ ID.  
> clRfqId | String | Client-supplied RFQ ID. This attribute is treated as client sensitive information. It will not be exposed to the Maker, only return empty string.  
> quoteId | String | Quote ID.  
> clQuoteId | String | Client-supplied Quote ID. This attribute is treated as client sensitive information. It will not be exposed to the Taker, only return empty string.  
> blockTdId | String | Block trade ID.  
> tag | String | RFQ tag.  
> tTraderCode | String | A unique identifier of the taker. Empty if the anonymous parameter of the RFQ is set to be `true`.  
> mTraderCode | String | A unique identifier of the maker. Empty if the anonymous parameter of the Quote is set to be `true`.  
> legs | Array of objects | Legs of trade  
>> instId | String | Instrument ID, e.g. BTC-USDT-SWAP  
>> px | String | The price the leg executed  
>> sz | String | Size of the leg in contracts or spot.  
>> side | String | The direction of the leg from the Takers perspective. Valid value can be buy or sell.  
>> fee | String | Fee for the individual leg.   
Negative fee represents the user transaction fee charged by the platform. Positive fee represents rebate.  
>> feeCcy | String | Fee currency. To be read in conjunction with fee  
>> tradeId | String | Last traded ID.  
> acctAlloc | Array of objects | Account level allocation of the RFQ  
>> acct | String | The name of the allocated account of the RFQ.  
>> blockTdId | String | Block trade ID  
>> sCode | String | The code of the event execution result, 0 means success  
>> sMsg | String | Rejection message if the request is unsuccessful  
>> legs | Array of objects | The allocated legs of the account.  
>>> instId | String | The Instrument ID of each leg. Example : "BTC-USDT-SWAP"  
>>> sz | String | The size of each account leg is filled.  
>>> fee | String | The fee of each account level leg  
>>> feeCcy | String | Fee currency. To be read in conjunction with fee  
>>> tradeId | String | Last traded ID of each account leg  
Group RFQ introduction  
  
1\. Takers are not allowed to partially execuate the quote for group RFQ. You will receive error code 70507 if you don't pass in the full leg size.  
2\. Parent RFQ leg size will be the summation of the filled size of each child RFQ leg size while fee should also be the summation.  
3\. The blockTdId of parent RFQ and the tradeId of parent RFQ legs will be emoty. But there will be subaccount breakdown attached with blockTdId and tradeId populated.

---

# 执行报价

执行报价，仅限询价的创建者使用  
  
#### 限速: 2次/3s

#### 限速规则：User ID

#### 权限：交易

#### HTTP Requests

`POST /api/v5/rfq/execute-quote`

> 请求示例
    
    
    {
        "rfqId":"22540",
        "quoteId":"84073",
        "legs": [
            {
                "sz":"25",
                "instId":"BTC-USD-20220114-13250-C"
            },
            {
                "sz":"25",
                "instId":"BTC-USDT"
            }
        ]
    }
    
    
    
    import okx.BlockTrading as BlockTrading
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘：1
    
    blockTradingAPI = BlockTrading.BlockTradingAPI(apikey, secretkey, passphrase, False, flag)
    
    # 执行报价
    result = blockTradingAPI.execute_quote(
        rfqId="22540",
        quoteId="84073"
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
rfqId | String | 是 | 询价单ID  
quoteId | String | 是 | 报价单ID  
legs | Array of objects | 否 | 用于部分执行的腿的数量。腿的数量比例必须与原RFQ相同。注意：每条腿的`tgtCcy`和`side`和原RFQ一致，`px`和对应Quote一致。  
> instId | String | 是 | 产品ID, 如 "BTC-USDT-SWAP".  
> sz | String | 是 | 该条腿的部分执行数量  
  
> 响应示例
    
    
    {  
       "code":"0",
       "msg":"",
       "data":[
           {
                "blockTdId":"180184",
                "rfqId":"1419",
                "clRfqId":"r0001",
                "quoteId":"1046",
                "clQuoteId":"q0001",
                "tag":"123456",
                "tTraderCode":"Trader1",
                "mTraderCode":"Trader2",
                "cTime":"1649670009",
                "legs":[
                    {
                        "px":"43000",
                        "sz":"25",
                        "instId":"BTC-USD-20220114-13250-C",
                        "side":"sell",
                        "fee":"-1.001",
                        "feeCcy":"BTC",
                        "tradeId":"10211"
                    },
                    {
                        "px":"42800",
                        "sz":"25",
                        "instId":"BTC-USDT",
                        "side":"buy",
                        "fee":"-1.001",
                        "feeCcy":"BTC",
                        "tradeId":"10212"
                    }
                ]
            }
       ]
    }
    

#### 响应参数

参数名 | 类型 | 描述  
---|---|---  
code | String | 结果代码，0 表示成功。  
msg | String | 错误信息，如果代码不为 0，则不为空。  
data | Array of objects | 包含结果的对象数组  
> cTime | String | 交易执行的时间，Unix时间戳的毫秒数格式。  
> rfqId | String | 询价单ID  
> clRfqId | String | 询价单自定义ID，为客户敏感信息，不会公开，对报价方返回""。  
> quoteId | String | 报价单ID  
> clQuoteId | String | 报价单自定义ID，为客户敏感信息，不会公开，对询价方返回""。  
> blockTdId | String | 大宗交易ID  
> tag | String | 询价单标签  
> tTraderCode | String | 询价价方唯一标识代码。询价时 anonymous 设置为 `true` 时不可见。  
> mTraderCode | String | 报价方唯一标识代码。 报价时 anonymous 设置为 `true` 时不可见。  
> legs | Array of objects | 组合交易  
>> instId | String | 产品ID  
>> px | String | 成交价格  
>> sz | String | 成交数量  
>> side | String | 询价单方向，`buy` 或者 `sell`。  
>> fee | String | 手续费，正数代表平台返佣 ，负数代表平台扣除  
>> feeCcy | String | 手续费币种  
>> tradeId | String | 最新的成交Id.  
> acctAlloc | Array of objects | 组合询价单的账户分配  
>> acct | String | 账户名  
>> blockTdId | String | 大宗交易ID  
>> sCode | String | 事件执行结果的code，0代表成功  
>> sMsg | String | 事件执行失败或成功时的msg  
>> legs | Array of objects | 组合交易  
>>> instId | String | 产品ID  
>>> sz | String | 成交数量  
>>> fee | String | 手续费  
>>> feeCcy | String | 手续费币种  
>>> tradeId | String | 最新的成交ID  
组合询价单介绍  
  
1\. Taker 不能部分执行组合询价单。如果没有传入完整的腿数量，将收到错误代码 70507。  
2\. 父级询价单的腿数量将是每个子级询价单腿数量的总和，同时费用也应为总和。  
3\. 父级询价单的 blockTdId 和 tradeId 将为空。但将附带子账户分配的详情，提供blockTdId 和 tradeId。