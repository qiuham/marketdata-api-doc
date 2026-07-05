---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#block-trading-rest-api-get-quotes
anchor_id: block-trading-rest-api-get-quotes
api_type: REST
updated_at: 2026-07-05 19:34:31.496316
---

# Get quotes

Retrieve all Quotes that the user is a counterparty to (either as the creator or the receiver).

#### Rate Limit: 2 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/rfq/quotes`

> Request Example
    
    
    GET /api/v5/rfq/quotes
    
    
    
    import okx.BlockTrading as BlockTrading
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading: 0, Demo trading: 1
    
    blockTradingAPI = BlockTrading.BlockTradingAPI(apikey, secretkey, passphrase, False, flag)
    
    # Retrieve all Quotes that the user is a counterparty to
    result = blockTradingAPI.get_quotes()
    print(result)
    

#### Request parameters

Parameter | Type | Required | Description  
---|---|---|---  
rfqId | String | No | RFQ ID .  
clRfqId | String | No | Client-supplied RFQ ID. If both `clRfqId` and `rfqId` are passed, `rfqId` will be be treated as primary identifier.  
quoteId | String | No | Quote ID  
clQuoteId | String | No | Client-supplied Quote ID. If both clQuoteId and quoteId are passed, quoteId will be treated as primary identifier  
state | String | No | The status of the quote. Valid values can be `active` `canceled` `pending_fill` `filled` `expired` or `failed`.  
beginId | String | No | Start quote id the request to begin with. Pagination of data to return records newer than the requested quoteId, not including beginId  
endId | String | No | End quote id the request to end with. Pagination of data to return records earlier than the requested quoteId, not including endId  
limit | String | No | Number of results per request. The maximum is 100 which is also the default value.  
  
> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "validUntil":"1608997227834",
                "uTime":"1608267227834",
                "cTime":"1608267227834",
                "legs":[
                    {
                        "px":"46000",
                        "sz":"25",
                        "instId":"BTC-USD-220114-25000-C",
                        "tdMode":"cross",
                        "ccy":"USDT",
                        "side":"sell",
                        "posSide": "long",
                        "tgtCcy":""
                    },
                    {
                        "px":"45000",
                        "sz":"25",
                        "instId":"BTC-USDT",
                        "tdMode":"cross",
                        "ccy":"USDT",
                        "side":"buy",
                        "posSide": "long",
                        "tgtCcy":"base_ccy",
                        "tradeQuoteCcy": "USDT"
                    }
                ],
                "quoteId":"25092",
                "rfqId":"18753",
                "quoteSide":"sell",
                "state":"canceled",
                "reason":"mmp_canceled",
                "clQuoteId":"cq001",
                "clRfqId":"cr001",
                "tag":"123456",
                "traderCode":"Trader1"
            }
        ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
code | String | The result code, `0` means success.  
msg | String | The error message, not empty if the code is not 0.  
data | Array of objects | Array of objects containing the results of the Quote creation.  
> cTime | String | The timestamp the Quote was created, Unix timestamp format in milliseconds.  
> uTime | String | The timestamp the Quote was last updated, Unix timestamp format in milliseconds.  
> state | String | The status of the quote. Valid values can be `active` `canceled` `pending_fill` `filled` `expired` or `failed`.  
> reason | String | Reasons of state. Valid values can be `mmp_canceled`.  
> validUntil | String | The timestamp the Quote expires. Unix timestamp format in milliseconds.  
> rfqId | String | RFQ ID.  
> clRfqId | String | Client-supplied RFQ ID. This attribute is treated as client sensitive information. It will not be exposed to the Maker, only return empty string.  
> quoteId | String | Quote ID.  
> clQuoteId | String | Client-supplied Quote ID. This attribute is treated as client sensitive information. It will not be exposed to the Taker, only return empty string.  
> tag | String | Quote tag. The block trade associated with the Quote will have the same tag.  
> traderCode | String | A unique identifier of maker. Empty If the anonymous parameter of the Quote is set to be `true`.  
> quoteSide | String | Top level direction of Quote. Its value can be buy or sell.  
> legs | Array of objects | The legs of the Quote.  
>> instId | String | The instrument ID of the quoted leg.  
>> tdMode | String | Trade mode   
Margin mode: `cross` `isolated`   
Non-Margin mode: `cash`.   
If not provided, tdMode will inherit default values set by the system shown below:   
Futures mode & SPOT: `cash`   
Buy options in Futures mode and Multi-currency Margin: `isolated`   
Other cases: `cross`  
>> ccy | String | Margin currency.   
Only applicable to `cross` `MARGIN` orders in `Futures mode`. The parameter will be ignored in other scenarios.  
>> sz | String | Size of the leg in contracts or spot.  
>> px | String | The price of the leg.  
>> side | String | The direction of the leg. Valid values can be buy or sell.  
>> posSide | String | Position side.   
The default is `net` in the net mode. If not specified, return "", which is equivalent to net.   
It can only be `long` or `short` in the long/short mode. If not specified, return "", which corresponds to the direction that opens new positions for the trade (buy => long, sell => short).   
Only applicable to `FUTURES`/`SWAP`.  
>> tgtCcy | String | Defines the unit of the “sz” attribute.   
Only applicable to instType = SPOT.   
The valid enumerations are base_ccy and quote_ccy. When not specified this is equal to base_ccy by default.  
>> tradeQuoteCcy | String | The quote currency used for trading. Only applicable to SPOT.   
The default value is the quote currency of the instId, for example: for `BTC-USD`, the default is `USD`.

---

# 获取报价单信息

获取用户发出的或收到的报价单信息

#### 限速: 2次/2s

#### 限速规则：User ID

#### 权限：读取

#### HTTP Requests

`GET /api/v5/rfq/quotes`

> 请求示例
    
    
    GET /api/v5/rfq/quotes
    
    
    
    import okx.BlockTrading as BlockTrading
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘：1
    
    blockTradingAPI = BlockTrading.BlockTradingAPI(apikey, secretkey, passphrase, False, flag)
    
    # 获取报价单信息
    result = blockTradingAPI.get_quotes()
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
rfqId | String | 否 | 询价单ID  
clRfqId | String | 否 | 询价单自定义ID， 当 clRfqId 和 rfqId 都传时，以 rfqId 为准。  
quoteId | String | 否 | 报价单ID  
clQuoteId | String | 否 | 报价单自定义ID，当 clRfqId 和 rfqId 都传时，以 rfqId 为准。  
state | String | 否 | 报价单的状态  
有效值为 `active` `canceled` `pending_fill` `filled` `expired` `failed`  
beginId | String | 否 | 请求的起始报价单ID，请求此ID之后（更新的数据）的分页内容，不包括 beginId  
endId | String | 否 | 请求的结束报价单ID，请求此ID之前（更旧的数据）的分页内容，不包括 endId  
limit | String | 否 | 返回结果的数量，最大为100，默认100条  
  
> 返回示例
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "validUntil":"1608997227834",
                "uTime":"1608267227834",
                "cTime":"1608267227834",
                "legs":[
                    {
                        "px":"46000",
                        "sz":"25",
                        "instId":"BTC-USD-220114-25000-C",
                        "tdMode":"cross",
                        "ccy":"USDT",
                        "side":"sell",
                        "posSide": "long",
                        "tgtCcy":"",
                        "tradeQuoteCcy": ""
                    },
                    {
                        "px":"45000",
                        "sz":"25",
                        "instId":"BTC-USDT",
                        "tdMode":"cross",
                        "ccy":"USDT",
                        "side":"buy",
                        "posSide": "long",
                        "tgtCcy":"base_ccy",
                        "tradeQuoteCcy": "USDT"
                    }
                ],
                "quoteId":"25092",
                "rfqId":"18753",
                "quoteSide":"sell",
                "state":"canceled",
                "reason":"mmp_canceled",
                "clQuoteId":"cq001",
                "clRfqId":"cr001",
                "tag":"123456",
                "traderCode":"Trader1"
            }
        ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
code | String | 结果代码，0 表示成功。  
msg | String | 错误信息，如果代码不为 0，则不为空。  
data | Array of objects | 包含结果的数组  
> cTime | String | 报价单创建时间，Unix时间戳的毫秒数格式  
> uTime | String | 报价单状态更新时间，Unix时间戳的毫秒数格式。  
> state | String | 报价单的状态  
`active` `canceled` `pending_fill` `filled` `expired` `failed`  
> reason | String | 状态原因. 有效值包括 `mmp_canceled`.  
> validUntil | String | 报价单的过期时间，Unix时间戳的毫秒数格式。  
> rfqId | String | 询价单ID  
> clRfqId | String | 询价单自定义ID，为客户敏感信息，不会公开，对报价方返回""。  
> quoteId | String | 报价单ID  
> clQuoteId | String | 报价单自定义ID，为客户敏感信息，不会公开，对询价方返回""。  
> tag | String | 报价单标签，与此报价单关联的大宗交易将有相同的标签。  
> traderCode | String | 报价方唯一标识代码，报价时 Anonymous 设置为 `True` 时不可见。  
> quoteSide | String | 报价单方向，`buy`或者`sell`。当报价单方向为`buy`，对maker来说，执行方向与legs里的方向相同，对taker来说相反。反之同理  
> legs | Array of objects | 组合交易  
>> instId | String | 产品ID  
>> tdMode | String | 交易模式   
保证金模式：`cross`全仓 `isolated`逐仓   
非保证金模式：`cash`非保证金.   
如未提供，tdMode 将继承系统设置的默认值：   
合约模式 & 现货: `cash`   
合约模式和跨币种保证金模式下买入期权： `isolated`   
其他情况: `cross`  
>> ccy | String | 保证金币种，仅适用于`合约模式`下的`全仓杠杆`订单   
在其他情况下该参数将被忽略。  
>> sz | String | 委托数量  
>> px | String | 委托价格.  
>> side | String | 报价单方向  
>> posSide | String | 持仓方向   
买卖模式下默认为`net`。如未指定，则返回""，相当于`net`。   
在开平仓模式下仅可选择`long`或`short`。 如未指定，则返回""，对应于为交易开新仓位的方向（买入=>`long`，卖出=>`short`）。  
仅适用交割、永续。  
>> tgtCcy | String | 委托数量的类型   
定义`sz`属性的单位。仅适用于 instType=`SPOT`。有效值为`base_ccy`和`quote_ccy`。未指定时，默认为`base_ccy`。  
>> tradeQuoteCcy | String | 交易使用的计价币种。仅适用于 SPOT。  
默认值为 instId 的报价币种，例如：对于 `BTC-USD`，默认值为 `USD`。