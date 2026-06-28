---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#block-trading-rest-api-get-trades
anchor_id: block-trading-rest-api-get-trades
api_type: REST
updated_at: 2026-06-28 19:37:33.821244
---

# Get trades

Retrieves the executed trades that the user is a counterparty to (either as the creator or the receiver).  
  
#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/rfq/trades`

> Request Example
    
    
    GET /api/v5/rfq/trades
    
    
    
    import okx.BlockTrading as BlockTrading
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading: 0, Demo trading: 1
    
    blockTradingAPI = BlockTrading.BlockTradingAPI(apikey, secretkey, passphrase, False, flag)
    
    # Retrieves the executed trades that the user is a counterparty to
    result = blockTradingAPI.get_trades()
    print(result)
    

#### Request parameters

Parameter | Type | Required | Description  
---|---|---|---  
rfqId | String | No | RFQ ID .  
clRfqId | String | No | Client-supplied RFQ ID. If both `clRfqId` and `rfqId` are passed, `rfqId` will be treated as primary identifier  
quoteId | String | No | Quote ID  
blockTdId | String | No | Block trade ID  
clQuoteId | String | No | Client-supplied Quote ID. If both `clQuoteId` and `quoteId` are passed, `quoteId` will be treated as primary identifier  
beginId | String | No | The starting rfq id the request to begin with. Pagination of data to return records newer than the requested blockTdId, not including beginId.  
endId | String | No | The last rfq id the request to end withPagination of data to return records earlier than the requested blockTdId, not including endId.  
beginTs | String | No | Filter trade execution time with a begin timestamp (UTC timezone). Unix timestamp format in milliseconds, e.g. 1597026383085  
endTs | String | No | Filter trade execution time with an end timestamp (UTC timezone). Unix timestamp format in milliseconds, e.g. 1597026383085  
limit | String | No | Number of results per request. The maximum is 100 which is also the default value.   
If the number of trades in the requested range is bigger than 100, the latest 100 trades in the range will be returned.  
isSuccessful | Boolean | No | Whether the trade is filled successfully.  
`true`: the default value. `false`.  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "rfqId": "123456",
                "clRfqId": "",
                "quoteId": "0T5342O",
                "clQuoteId": "",
                "blockTdId": "439127542058958848",
                "tag": "123456",
                "isSuccessful": true,
                "errorCode": "",
                "legs": [
                    {
                        "instId": "BTC-USDT",
                        "side": "sell",
                        "sz": "0.666",
                        "px": "100",
                        "tradeId": "439127542058958850",
                        "fee": "-0.0333",
                        "feeCcy": "USDT",
                        "tradeQuoteCcy": "USDT"
                    }
                ],
                "cTime": "1650968164900",
                "tTraderCode": "SATS",
                "mTraderCode": "MIKE"
            },
            {
                "rfqId": "1234567",
                "clRfqId": "",
                "quoteId": "0T533T0",
                "clQuoteId": "",
                "blockTdId": "439121886014849024",
                "tag": "123456",
                "isSuccessful": true,
                "errorCode": "",
                "legs": [
                    {
                        "instId": "BTC-USDT",
                        "side": "sell",
                        "sz": "0.532",
                        "px": "100",
                        "tradeId": "439121886014849026",
                        "fee": "-0.0266",
                        "feeCcy": "USDT",
                        "tradeQuoteCcy": "USDT"
                    }
                ],
                "cTime": "1650966816550",
                "tTraderCode": "SATS",
                "mTraderCode": "MIKE"
            }
        ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
code | String | The result code, `0` means success.  
msg | String | The error message, not empty if the code is not 0.  
data | Array of objects | Array of objects containing the results of the block trade.  
> cTime | String | The time the trade was executed. Unix timestamp in milliseconds.  
> rfqId | String | RFQ ID.  
> clRfqId | String | Client-supplied RFQ ID. This attribute is treated as client sensitive information. It will not be exposed to the Maker, only return empty string.  
> quoteId | String | Quote ID.  
> clQuoteId | String | Client-supplied Quote ID. This attribute is treated as client sensitive information. It will not be exposed to the Taker, only return empty string.  
> blockTdId | String | Block trade ID.  
> tag | String | Trade tag. The block trade will have the tag of the RFQ or Quote it corresponds to.  
> tTraderCode | String | A unique identifier of the Taker. Empty if the anonymous parameter of the RFQ is set to be `true`.  
> mTraderCode | String | A unique identifier of the Maker. Empty if the anonymous parameter of the Quote is set to be `true`.  
> isSuccessful | Boolean | Whether the trade is filled successfully  
> errorCode | String | Error code for unsuccessful trades.   
It is "" for successful trade.  
> legs | Array of objects | Legs of trade  
>> instId | String | Instrument ID, e.g. `BTC-USDT-SWAP`  
>> px | String | The price the leg executed  
>> sz | String | Size of the leg in contracts or spot.  
>> side | String | The direction of the leg. Valid value can be buy or sell.  
>> fee | String | Fee. Negative number represents the user transaction fee charged by the platform. Positive number represents rebate.  
>> feeCcy | String | Fee currency  
>> tradeId | String | Last traded ID.  
>> tradeQuoteCcy | String | The quote currency used for trading. Only applicable to SPOT.   
The default value is the quote currency of the instId, for example: for `BTC-USD`, the default is `USD`.  
> acctAlloc | Array of objects | Applicable to both taker, maker  
>> blockTdId | String | Block trade ID  
>> errorCode | String | Error code for unsuccessful trades.  
It is "0" for successful trade.  
>> acct | String | The name of the allocated account of the RFQ  
Only applicable to taker, return "" to makers  
>> legs | Array of objects | The allocated legs of the account.  
>>> instId | String | The Instrument ID of each leg. Example : "BTC-USDT-SWAP"  
>>> sz | String | Filled size  
>>> tradeId | String | Trade ID  
>>> fee | String | Fee  
>>> feeCcy | String | Fee currency  
Group RFQ introduction  
  
1\. This endpoint is at parent RFQ level and contains account allocation. For parent RFQ, we should return the actual executed size, i.e. failed execution size should not be included in the parent RFQ level.  
2\. For account allocation, we should include both filled and failed child RFQ but add an errorCode to indicate whether a child RFQ is filled.  
3\. Trade results will only be returned to group RFQ creator. Allocated subaccounts and MSAs will not see trade results. Allocated accounts are expected to get these trades through trading bills.  
4\. Trades data will only be returned after all child RFQs are execuated.  
5\. For parent RFQ isSuccessful field,  
    1\. it will return true if any child RFQs are filled  
    2\. otherwise, if all child RFQ fails, it will return false  
6\. Parent RFQ blockTdId or legs tradeId will be empty. However, account allocation breakdown will be offered and blockTdId/tradeId will be attached.

---

# 获取大宗交易信息

获取该用户大宗交易成交信息  
  
#### 限速: 5次/2s

#### 限速规则：User ID

#### 权限：读取

#### HTTP Requests

`GET /api/v5/rfq/trades`

> 请求示例
    
    
    GET /api/v5/rfq/trades
    
    
    
    import okx.BlockTrading as BlockTrading
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘：1
    
    blockTradingAPI = BlockTrading.BlockTradingAPI(apikey, secretkey, passphrase, False, flag)
    
    # 获取大宗交易信息
    result = blockTradingAPI.get_trades()
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
rfqId | String | 否 | 询价单ID  
clRfqId | String | 否 | 由用户设置的询价单ID. 如果 `clRfqId` 和 `rfqId` 都通过了，rfqId 将被视为主要  
quoteId | String | 否 | 报价单ID  
blockTdId | String | 否 | 大宗交易ID  
clQuoteId | String | 否 | 由用户设置的报价单ID。如果同时传递了 `clQuoteId` 和 `quoteId`，则 quoteId 将被视为主要标识符  
beginId | String | 否 | 请求的起始大宗交易ID，请求此ID之后（更新的数据）的分页内容，不包括 beginId  
endId | String | 否 | 请求的结束大宗交易ID，请求此ID之前（更旧的数据）的分页内容，不包括 endId  
beginTs | String | 否 | 用开始时间戳筛选交易执行时间（UTC时区）。Unix时间戳的毫秒数格式，如 1597026383085。  
endTs | String | 否 | 用结束时间戳筛选交易执行时间（UTC时区）。Unix时间戳的毫秒数格式，如 1597026383085。  
limit | String | 否 | 返回结果的数量，最大为100，默认100条。  
如果请求范围内的交易数量大于100，则返回该范围内最近的100笔交易。  
isSuccessful | Boolean | 否 | 交易是否成功。  
`true`: 成功，默认值。  
`false`: 未成功。  
  
> 返回示例
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "rfqId": "123456",
                "clRfqId": "",
                "quoteId": "0T5342O",
                "clQuoteId": "",
                "blockTdId": "439127542058958848",
                "tag": "123456",
                "isSuccessful": true,
                "errorCode": "",
                "legs": [
                    {
                        "instId": "BTC-USDT",
                        "side": "sell",
                        "sz": "0.666",
                        "px": "100",
                        "tradeId": "439127542058958850",
                        "fee": "-0.0333",
                        "feeCcy": "USDT",
                        "tradeQuoteCcy": "USDT"
                    }
                ],
                "cTime": "1650968164900",
                "tTraderCode": "SATS",
                "mTraderCode": "MIKE"
            },
            {
                "rfqId": "1234567",
                "clRfqId": "",
                "quoteId": "0T533T0",
                "clQuoteId": "",
                "blockTdId": "439121886014849024",
                "tag": "123456",
                "isSuccessful": true,
                "errorCode": "",
                "legs": [
                    {
                        "instId": "BTC-USDT",
                        "side": "sell",
                        "sz": "0.532",
                        "px": "100",
                        "tradeId": "439121886014849026",
                        "fee": "-0.0266",
                        "feeCcy": "USDT",
                        "tradeQuoteCcy": "USDT"
                    }
                ],
                "cTime": "1650966816550",
                "tTraderCode": "SATS",
                "mTraderCode": "MIKE"
            }
        ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
code | String | 结果代码，0 表示成功。  
msg | String | 错误信息，如果代码不为 0，则不为空。  
data | Array of objects | 包含结果的对象数组  
> cTime | String | 执行创建的时间，Unix时间戳的毫秒数格式。  
> rfqId | String | 询价单ID  
> clRfqId | String | 询价单自定义ID，为客户敏感信息，不会公开，对报价方返回""。  
> quoteId | String | 报价单ID  
> clQuoteId | String | 报价单自定义ID，为客户敏感信息，不会公开，对询价方返回""。  
> blockTdId | String | 大宗交易ID  
> tag | String | 交易标签，大宗交易将有与其对应的询价单或报价单相同的标签。  
> tTraderCode | String | 询价方唯一标识代码，询价时 anonymous 设置为 `true` 时不可见  
> mTraderCode | String | 报价方唯一标识代码。报价时 anonymous 设置为 `true` 时不可见  
> isSuccessful | Boolean | 交易是否成功  
> errorCode | String | 未成功交易的错误码。  
对于成功交易为 ""。  
> legs | Array of objects | 组合交易  
>> instId | String | 产品ID  
>> px | String | 成交价格  
>> sz | String | 成交数量  
>> side | String | 询价单方向，buy 或者 sell。  
>> fee | String | 手续费，正数代表平台返佣 ，负数代表平台扣除  
>> feeCcy | String | 手续费币种  
>> tradeId | String | 最新的成交Id  
>> tradeQuoteCcy | String | 交易使用的计价币种。仅适用于 SPOT。  
默认值为 instId 的报价币种，例如：对于 `BTC-USD`，默认值为 `USD`。  
> acctAlloc | Array of objects | 组合询价单的账户分配  
>> blockTdId | String | 大宗交易ID  
>> errorCode | String | 事件执行结果的code，0代表成功  
>> acct | String | 账户名  
只适用于 Taker，对于 Maker 返回""  
>> legs | Array of objects | 组合交易  
>>> instId | String | 产品ID  
>>> sz | String | 成交数量  
>>> tradeId | String | 最新的成交Id  
>>> fee | String | 手续费  
>>> feeCcy | String | 手续费币种  
组合询价单介绍  
  
1\. 该接口返回的交易数据应为父级询价单级别，而不是子级询价单执行级别。  
2\. 对于账户分配，包含所有已成交和未成交的子级询价单，但添加 errorCode 来指示子级询价单是否已成交。  
3\. 交易结果将仅返回给组合询价单 Taker 及 Maker。分配的子账户和资管账户将无法看到交易结果。分配的账户应通过交易账单获取这些交易。  
4\. 交易数据仅在所有子级询价单执行后返回。  
5\. 对于父级询价单的 isSuccessful 字段，  
    1\. 如果任何子级询价单已成交，则返回 true  
    2\. 否则，如果所有子级询价单均失败，则返回 false  
6\. 父级询价单的 blockTdId 或 legs 的 tradeId 将为空。但将提供账户分配的详细信息，并附带 blockTdId 以及 tradeId。