---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#block-trading-rest-api-create-quote
anchor_id: block-trading-rest-api-create-quote
api_type: REST
updated_at: 2026-06-29 19:56:50.626999
---

# Create Quote

Allows the user to Quote an RFQ that they are a counterparty to. The user MUST quote the entire RFQ and not part of the legs or part of the quantity. Partial quoting is not allowed.   
  
#### Rate Limit: 50 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/rfq/create-quote`

> Request Example
    
    
    POST /api/v5/rfq/create-quote
    {
        "rfqId":"22539",
        "clQuoteId":"q001",
        "tag":"123456",
        "quoteSide":"buy",
        "anonymous": true,
        "expiresIn":"30",
        "legs":[
            {
                "px":"39450.0",
                "sz":"200000",
                "instId":"BTC-USDT-SWAP",
                "tdMode":"cross",
                "ccy":"USDT",
                "side":"buy",
                "posSide": "long"
            },
            {
                "px":"39450.0",
                "sz":"200000",
                "instId":"BTC-USDT-SWAP",
                "tdMode":"cross",
                "ccy":"USDT",
                "side":"buy",
                "posSide": "long"
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
    
    # Create quote
    result = blockTradingAPI.create_quote(
        rfqId="22539",
        clQuoteId="q001",
        anonymous=True,
        quoteSide="buy",
        expiresIn="30",
        legs=[
            {
                "px": "39450.0",
                "sz": "200000",
                "instId": "BTC-USDT-SWAP",
                "side": "buy"
            }
        ]
    )
    print(result)
    

#### Request parameters

Parameter | Type | Required | Description  
---|---|---|---  
rfqId | String | Yes | RFQ ID .  
clQuoteId | String | No | Client-supplied Quote ID.   
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
tag | String | No | Quote tag.   
The block trade associated with the Quote will have the same tag.   
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 16 characters.  
anonymous | Boolean | No | Submit Quote on a disclosed or anonymous basis.   
Valid value is `true` or `false`. `false` by default.  
quoteSide | String | Yes | The trading direction of the Quote. Its value can be `buy` or `sell`.   
For example, if quoteSide is `buy`, all the legs are executed in their leg sides; otherwise, all the legs are executed in the opposite of their leg sides.  
expiresIn | String | No | Seconds that a quote expires in.   
Must be an integer between 10-120. Default is 60.  
legs | Array of objects | Yes | The legs of the Quote.  
> instId | String | Yes | The instrument ID of quoted leg.  
> tdMode | String | No | Trade mode   
Margin mode: `cross` `isolated`   
Non-Margin mode: `cash`.   
If not provided, tdMode will inherit default values set by the system shown below:   
Futures mode mode & SPOT: `cash`   
Buy options in Futures mode and Multi-currency Margin: `isolated`   
Other cases: `cross`  
> ccy | String | No | Margin currency.   
Only applicable to `cross` `MARGIN` orders in `Futures mode`. The parameter will be ignored in other scenarios.  
> sz | String | Yes | Size of the leg in contracts or spot.  
> px | String | Yes | The price of the leg.  
> side | String | Yes | The direction of the leg. Valid values can be buy or sell.  
> posSide | String | No | Position side.   
The default is `net` in the net mode. It can only be `long` or `short` in the long/short mode.   
If not specified, users in long/short mode always open new positions.   
Only applicable to `FUTURES`/`SWAP`.  
> tgtCcy | String | No | Defines the unit of the “sz” attribute.   
Only applicable to instType = SPOT.   
The valid enumerations are `base_ccy` and `quote_ccy`. When not specified this is equal to `base_ccy` by default.  
> tradeQuoteCcy | String | No | The quote currency used for trading. Only applicable to SPOT.   
The default value is the quote currency of the instId, for example: for `BTC-USD`, the default is `USD`.  
  
> Response Example
    
    
    {
        "code":"",
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
                        "px":"4000",
                        "sz":"25",
                        "instId":"ETH-USD-220114-25000-C",
                        "tdMode":"cross",
                        "ccy":"USDT",
                        "side":"buy",
                        "posSide": "long",
                        "tgtCcy":""
                    }
                ],
                "quoteId":"25092",
                "rfqId":"18753",
                "tag":"123456",
                "quoteSide":"sell",
                "state":"active",
                "reason": "mmp_canceled",
                "clQuoteId":"",
                "clRfqId":"",
                "traderCode":"Aksha"
            }
        ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
code | String | The result code, `0` means success.  
msg | String | The error message, not empty if the code is not 0.  
data | Array of objects | Array of objects containing the results  
> cTime | String | The timestamp the Quote was created, Unix timestamp format in milliseconds.  
> uTime | String | The timestamp the Quote was last updated, Unix timestamp format in milliseconds.  
> state | String | The status of the quote. Valid values can be `active` `canceled` `pending_fill` `filled` `expired` or `failed`.  
> reason | String | Reasons of state. Valid values can be `mmp_canceled`.  
> validUntil | String | The timestamp the Quote expires. Unix timestamp format in milliseconds.  
> rfqId | String | RFQ ID  
> clRfqId | String | Client-supplied RFQ ID.   
This attribute is treated as client sensitive information. It will not be exposed to the Maker, only return empty string.  
> quoteId | String | Quote ID.  
> clQuoteId | String | Client-supplied Quote ID.   
This attribute is treated as client sensitive information. It will not be exposed to the Taker, only return empty string.  
> tag | String | Quote tag.   
The block trade associated with the Quote will have the same tag.  
> traderCode | String | A unique identifier of maker.  
> quoteSide | String | The trading direction of the Quote.   
Its value can be `buy` or `sell`. For example, if quoteSide is `buy`, all the legs are executed in their leg sides; otherwise, all the legs are executed in the opposite of their leg sides.  
> legs | Array of objects | The legs of the Quote.  
>> instId | String | Instrument ID, e.g. `BTC-USDT-SWAP`  
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
Only applicable to FUTURES/SWAP.  
>> tgtCcy | String | Defines the unit of the “sz” attribute.   
Only applicable to instType = SPOT.   
The valid enumerations are `base_ccy` and `quote_ccy`. When not specified this is equal to `base_ccy` by default.  
>> tradeQuoteCcy | String | The quote currency used for trading. Only applicable to SPOT.   
The default value is the quote currency of the instId, for example: for `BTC-USD`, the default is `USD`.

---

# 报价

允许询价单指定的报价方进行报价，需要对整个询价单报价，不允许部分报价。  
  
#### 限速: 50次/2s

#### 限速规则：User ID

#### 权限：交易

#### HTTP Requests

`POST /api/v5/rfq/create-quote`

> 请求示例
    
    
    POST /api/v5/rfq/create-quote
    {
        "rfqId":"22539",
        "clQuoteId":"q001",
        "tag":"123456",
        "quoteSide":"buy",
        "anonymous": true,
        "expiresIn":"30",
        "legs":[
            {
                "px":"39450.0",
                "sz":"200000",
                "instId":"BTC-USDT-SWAP",
                "tdMode":"cross",
                "ccy":"USDT",
                "side":"buy",
                "posSide": "long"
            },
            {
                "px":"39450.0",
                "sz":"200000",
                "instId":"BTC-USDT-SWAP",
                "tdMode":"cross",
                "ccy":"USDT",
                "side":"buy",
                "posSide": "long"
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
    
    # 报价
    result = blockTradingAPI.create_quote(
        rfqId="22539",
        clQuoteId="q001",
        anonymous=True,
        quoteSide="buy",
        expiresIn="30",
        legs=[
            {
                "px": "39450.0",
                "sz": "200000",
                "instId": "BTC-USDT-SWAP",
                "side": "buy"
            }
        ]
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
rfqId | String | 是 | 询价单ID  
clQuoteId | String | 否 | 报价单自定义ID  
tag | String | 否 | 报价单标签，与此报价单关联的大宗交易将有相同的标签。   
字母（区分大小写）与数字的组合，可以是纯字母、纯数字，且长度在1-16位之间。  
anonymous | Boolean | 否 | 是否匿名报价，`true`表示匿名报价，`false`表示公开报价，默认值为`false`，为`true`时，即使在交易执行之后，身份也不会透露给询价方。  
quoteSide | String | 是 | 报价单方向，`buy`或者`sell`。当报价单方向为`buy`，对maker来说，执行方向与legs里的方向相同，对taker来说相反。反之同理  
expiresIn | String | 否 | 报价单的有效时长（以秒为单位）。 10到120之间的任何整数。 默认值为60  
legs | Array of objects | 是 | 组合交易  
> instId | String | 是 | 产品ID  
> tdMode | String | 否 | 交易模式   
保证金模式：`cross`全仓 `isolated`逐仓   
非保证金模式：`cash`非保证金.   
如未提供，tdMode 将继承系统设置的默认值：   
合约模式 & 现货: `cash`   
合约模式和跨币种保证金模式下买入期权： `isolated`   
其他情况: `cross`  
> ccy | String | 否 | 保证金币种，仅适用于`合约模式`下的`全仓杠杆`订单   
在其他情况下该参数将被忽略。  
> sz | String | 是 | 委托数量  
> px | String | 是 | 委托价格  
> side | String | 是 | 报价单方向  
> posSide | String | 否 | 持仓方向   
买卖模式下默认为`net`。在开平仓模式下仅可选择`long`或`short`。   
如未指定，则处于开平仓模式下的用户始终会开新仓位。   
仅适用交割、永续。  
> tgtCcy | String | 否 | 委托数量的类型   
定义`sz`属性的单位。仅适用于 instType=`SPOT`。有效值为`base_ccy`和`quote_ccy`。未指定时，默认为`base_ccy`。  
> tradeQuoteCcy | String | 否 | 交易使用的计价币种。仅适用于 SPOT。  
默认值为 instId 的报价币种，例如：对于 `BTC-USD`，默认值为 `USD`。  
  
> 返回示例
    
    
    {
        "code": "",
        "msg": "",
        "data": [
            {
                "validUntil": "1608997227834",
                "uTime": "1608267227834",
                "cTime": "1608267227834",
                "legs": [
                    {
                        "px": "46000",
                        "sz": "25",
                        "instId": "BTC-USD-220114-25000-C",
                        "tdMode": "cross",
                        "ccy": "USDT",
                        "side": "sell",
                        "posSide": "long",
                        "tgtCcy": ""
                    },
                    {
                        "px": "4000",
                        "sz": "25",
                        "instId": "ETH-USD-220114-25000-C",
                        "tdMode": "cross",
                        "ccy": "USDT",
                        "side": "buy",
                        "posSide": "long",
                        "tgtCcy": ""
                    }
                ],
                "quoteId": "25092",
                "rfqId": "18753",
                "tag": "123456",
                "quoteSide": "sell",
                "state": "active",
                "reason": "mmp_canceled",
                "clQuoteId": "",
                "clRfqId": "",
                "traderCode": "Aksha"
            }
        ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
code | String | 结果代码，0表示成功。  
msg | String | 错误信息，如果代码不为0，则不为空。  
data | Array of objects | 包含结果的对象数组  
> cTime | String | 报价单创建时间，Unix时间戳的毫秒数格式。  
> uTime | String | 报价单状态更新时间，Unix时间戳的毫秒数格式。  
> state | String | 报价单的状态  
有效值为 `active` `canceled` `pending_fill` `filled` `expired` `failed`  
> reason | String | 状态原因. 有效值包括 `mmp_canceled`.  
> validUntil | String | 报价单的过期时间，Unix时间戳的毫秒数格式。  
> rfqId | String | 询价单ID  
> clRfqId | String | 询价单自定义ID，为客户敏感信息，不会公开，对报价方返回""。  
> quoteId | String | 报价单ID  
> clQuoteId | String | 报价单自定义ID，为客户敏感信息，不会公开，对询价方返回""。  
> tag | String | 报价单标签，与此报价单关联的大宗交易将有相同的标签。  
> traderCode | String | 报价方唯一标识代码。  
> quoteSide | String | 报价单方向，有效值为`buy`或者`sell`。当报价单方向为`buy`，对maker来说，执行方向与legs里的方向相同，对taker来说相反。反之同理。  
> legs | Array of objects | 组合交易  
>> instId | String | 产品ID  
>> tdMode | String | 交易模式   
保证金模式：`cross`全仓 `isolated`逐仓   
非保证金模式：`cash`非保证金.   
如未提供，tdMode 将继承系统设置的默认值：   
`合约模式`/`现货模式`: `cash`   
`合约模式`/`跨币种保证金模式`下买入期权： `isolated`   
其他情况: `cross`  
>> ccy | String | 保证金币种，仅适用于`合约模式`下的`全仓杠杆`订单   
在其他情况下该参数将被忽略。  
>> sz | String | 委托数量  
>> px | String | 委托价格  
>> side | String | 腿的方向，有效值为`buy`或者`sell`。  
>> posSide | String | 持仓方向   
买卖模式下默认为`net`。如未指定，则返回""，相当于`net`。   
在开平仓模式下仅可选择`long`或`short`。 如未指定，则返回""，对应于为交易开新仓位的方向（买入=>`long`，卖出=>`short`）。  
仅适用交割、永续。  
>> tgtCcy | String | 委托数量的类型   
定义`sz`属性的单位。仅适用于 instType=`SPOT`。有效值为`base_ccy`和`quote_ccy`。未指定时，默认为`base_ccy`。  
>> tradeQuoteCcy | String | 交易使用的计价币种。仅适用于 SPOT。  
默认值为 instId 的报价币种，例如：对于 `BTC-USD`，默认值为 `USD`。