---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#block-trading-rest-api-get-rfqs
anchor_id: block-trading-rest-api-get-rfqs
api_type: REST
updated_at: 2026-07-16 19:20:42.672295
---

# Get rfqs

Retrieves details of RFQs that the user is a counterparty to (either as the creator or the receiver of the RFQ). 

#### Rate Limit: 2 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/rfq/rfqs`

> Request Example
    
    
    GET /api/v5/rfq/rfqs
    
    
    
    import okx.BlockTrading as BlockTrading
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading: 0, Demo trading: 1
    
    blockTradingAPI = BlockTrading.BlockTradingAPI(apikey, secretkey, passphrase, False, flag)
    
    # Retrieves details of RFQs that the user is a counterparty to
    result = blockTradingAPI.get_rfqs()
    print(result)
    

#### Request parameters

Parameter | Type | Required | Description  
---|---|---|---  
rfqId | String | No | RFQ ID .  
clRfqId | String | No | Client-supplied RFQ ID. If both `clRfqId` and `rfqId` are passed, `rfqId` will be treated as primary identifier  
state | String | No | The status of the RFQ.   
Valid values can be `active` `canceled` `pending_fill` `filled` `expired` `failed` `traded_away`.   
`filled` indicates the RFQ was successfully executed against the maker's quote.   
`traded_away` only applies to Maker. The same RFQ can appear as `filled` to one maker and `traded_away` to another.   
Example: taker creates RFQ → makerA quotes pxA, makerB quotes pxB → pxA is better than pxB → taker executes quoteA → makerA sees `filled`, makerB sees `traded_away`.  
beginId | String | No | Start rfq id the request to begin with. Pagination of data to return records newer than the requested rfqId, not including beginId  
endId | String | No | End rfq id the request to end with. Pagination of data to return records earlier than the requested rfqId, not including endId  
limit | String | No | Number of results per request. The maximum is 100 which is also the default value.  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "rfqId": "123456",
                "clRfqId": "",
                "tag": "123456",
                "traderCode": "VITALIK",
                "validUntil": "1650969031817",
                "allowPartialExecution": false,
                "state": "filled",
                "flowType": "",
                "counterparties": [
                    "SATOSHI"
                ],
                "legs": [
                    {
                        "instId": "BTC-USDT",
                        "tdMode": "cross",
                        "ccy": "USDT",
                        "side": "buy",
                        "posSide": "long",
                        "sz": "25",
                        "tgtCcy": "base_ccy",
                        "tradeQuoteCcy": "USDT"
                    }
                ],
                "cTime": "1650968131817",
                "uTime": "1650968164944"
            },
            {
                "rfqId": "1234567",
                "clRfqId": "",
                "tag": "1234567",
                "traderCode": "VITALIK",
                "validUntil": "1650967623729",
                "state": "filled",
                "flowType": "",
                "counterparties": [
                    "SATOSHI"
                ],
                "legs": [
                    {
                        "instId": "BTC-USDT",
                        "tdMode": "cross",
                        "ccy": "USDT",
                        "side": "buy",
                        "posSide": "long",
                        "sz": "1500000",
                        "tgtCcy": "quote_ccy",
                        "tradeQuoteCcy": "USDT"
                    }
                ],
                "cTime": "1650966723729",
                "uTime": "1650966816577"
            }
        ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
code | String | The result code, `0` means success.  
msg | String | The error message, not empty if the code is not 0.  
data | Array of objects | Array of objects containing the results of the RFQ creation.  
> cTime | String | The timestamp the RFQ was created. Unix timestamp format in milliseconds.  
> uTime | String | The timestamp the RFQ was last updated. Unix timestamp format in milliseconds.  
> state | String | The status of the RFQ.   
Valid values can be `active` `canceled` `pending_fill` `filled` `expired` `failed` `traded_away`.   
`filled` indicates the RFQ was successfully executed against the maker's quote.   
`traded_away` only applies to Maker. The same RFQ can appear as `filled` to one maker and `traded_away` to another.   
Example: taker creates RFQ → makerA quotes pxA, makerB quotes pxB → pxA is better than pxB → taker executes quoteA → makerA sees `filled`, makerB sees `traded_away`.  
> counterparties | Array of strings | The list of counterparties traderCode the RFQ was broadcasted to.  
> validUntil | String | The timestamp the RFQ expires. Unix timestamp format in milliseconds.  
> clRfqId | String | Client-supplied RFQ ID.   
This attribute is treated as client sensitive information. It will not be exposed to the Maker, only return empty string.  
> tag | String | RFQ tag.   
The block trade associated with the RFQ will have the same tag.  
> flowType | String | Identify the type of the RFQ.   
Only applicable to Makers, return "" for Takers  
> traderCode | String | A unique identifier of taker. Empty if the anonymous parameter of the RFQ is set to be `true`.  
> rfqId | String | RFQ ID.  
> allowPartialExecution | Boolean | Whether the RFQ can be partially filled provided that the shape of legs stays the same.   
Valid value is `true` or `false`. `false` by default.  
> legs | Array of objects | Legs of RFQ  
>> instId | String | Instrument ID, e.g. BTC-USDT-SWAP  
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
> groupId | String | Group RFQ ID  
Only applicable to group RFQ, return "" for normal RFQ  
> acctAlloc | Array of objects | Account level allocation of the RFQ  
This is only applicable to the taker.  
>> acct | String | The name of the allocated account of the RFQ.  
>> legs | Array of objects | The allocated legs of the account.  
>>> instId | String | The Instrument ID of each leg. Example : "BTC-USDT-SWAP"  
>>> sz | String | The allocated size of each leg.  
>>> tdMode | String | Trade mode  
>>> ccy | String | Margin currency  
>>> posSide | String | Position side  
Group RFQ introduction  
  
1\. allowPartialExecution field is always true for group RFQ for taker and maker.  
2\. Add a new response parameter acctAlloc with all account allocation the same as the initial request, but it is only applicable to takers.  
3\. Add a new response parameter groupId, applicable to both takers and makers.  
4\. For group RFQ state,  
    1\. if any allocated account is pending execution, then pending_fill  
    2\. otherwise,  
        1\. if any allocated account is filled, then filled  
        2\. if all allocated accounts are failed, then failed

---

# 获取询价单信息

获取用户发出的或收到的询价单信息

#### 限速: 2次/2s

#### 限速规则：User ID

#### HTTP Requests

`GET /api/v5/rfq/rfqs`

> 请求示例
    
    
    GET /api/v5/rfq/rfqs
    
    
    
    import okx.BlockTrading as BlockTrading
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘：1
    
    blockTradingAPI = BlockTrading.BlockTradingAPI(apikey, secretkey, passphrase, False, flag)
    
    # 获取询价单信息
    result = blockTradingAPI.get_rfqs()
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
rfqId | String | 否 | 询价单ID .  
clRfqId | String | 否 | 客户询价单自定义ID，当 clRfqId 和 rfqId 都传时，以 rfqId 为准  
state | String | 否 | 询价单的状态  
`active` `canceled` `pending_fill` `filled` `expired` `failed` `traded_away`  
`filled` 表示询价单已成功按照做市商的报价成交。  
`traded_away` 仅适用于报价方。同一笔询价单可能对一个报价方显示为 `filled`，而对另一个报价方显示为 `traded_away`。  
示例：询价方创建询价单 → 做市商A报价 pxA，做市商B报价 pxB → pxA 优于 pxB → 询价方执行做市商A的报价 → 做市商A看到 `filled`，做市商B看到 `traded_away`。  
beginId | String | 否 | 请求的起始询价单ID，请求此ID之后（更新的数据）的分页内容，不包括 beginId  
endId | String | 否 | 请求的结束询价单ID，请求此ID之前（更旧的数据）的分页内容，不包括 endId  
limit | String | 否 | 返回结果的数量，最大为100，默认100条  
  
> 返回示例
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "rfqId": "123456",
                "clRfqId": "",
                "tag": "123456",
                "traderCode": "VITALIK",
                "validUntil": "1650969031817",
                "allowPartialExecution": false,
                "state": "filled",
                "flowType": "",
                "counterparties": [
                    "SATOSHI"
                ],
                "legs": [
                    {
                        "instId": "BTC-USDT",
                        "tdMode": "cross",
                        "ccy": "USDT",
                        "side": "buy",
                        "posSide": "long",
                        "sz": "25",
                        "tgtCcy": "base_ccy",
                        "tradeQuoteCcy": "USDT"
                    }
                ],
                "cTime": "1650968131817",
                "uTime": "1650968164944"
            },
            {
                "rfqId": "1234567",
                "clRfqId": "",
                "tag": "1234567",
                "traderCode": "VITALIK",
                "validUntil": "1650967623729",
                "state": "filled",
                "flowType": "",
                "counterparties": [
                    "SATOSHI"
                ],
                "legs": [
                    {
                        "instId": "BTC-USDT",
                        "tdMode": "cross",
                        "ccy": "USDT",
                        "side": "buy",
                        "posSide": "long",
                        "sz": "1500000",
                        "tgtCcy": "quote_ccy",
                        "tradeQuoteCcy": "USDT"
                    }
                ],
                "cTime": "1650966723729",
                "uTime": "1650966816577"
            }
        ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
code | String | 结果代码，0 表示成功。  
msg | String | 错误信息，如果代码不为 0，则不为空。  
data | Array of objects | 包含结果的对象数组  
> cTime | String | 询价单创建时间，Unix时间戳的毫秒数格式。  
> uTime | String | 询价单状态更新时间，Unix时间戳的毫秒数格式。  
> state | String | 询价单的状态  
`active` `canceled` `pending_fill` `filled` `expired` `failed` `traded_away`  
`filled` 表示询价单已成功按照做市商的报价成交。  
`traded_away` 仅适用于报价方。同一笔询价单可能对一个报价方显示为 `filled`，而对另一个报价方显示为 `traded_away`。  
示例：询价方创建询价单 → 做市商A报价 pxA，做市商B报价 pxB → pxA 优于 pxB → 询价方执行做市商A的报价 → 做市商A看到 `filled`，做市商B看到 `traded_away`。  
> counterparties | Array of strings | 报价方列表  
> validUntil | String | 询价单的过期时间，Unix时间戳的毫秒数格式。  
> clRfqId | String | 询价单自定义ID，为客户敏感信息，不会公开，对报价方返回""。  
> tag | String | 询价单标签，与此询价单关联的大宗交易将有相同的标签。  
> flowType | String | 识别询价单的类型。   
仅适用于报价方，返回""给询价方。  
> traderCode | String | 询价方唯一标识代码，询价时 anonymous 设置为 `true` 时不可见  
> rfqId | String | 询价单ID  
> allowPartialExecution | Boolean | RFQ是否可以被部分执行，如果腿的比例和原RFQ一致。有效值为`true`或`false`。未指定时，默认为`false`。  
> legs | Array of objects | 组合交易，每个请求最多可放置15条腿  
>> instId | String | 产品ID，如 "BTC-USDT-SWAP"  
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
>> side | String | 询价单方向   
有效值为`buy`和`sell`。  
>> posSide | String | 持仓方向   
买卖模式下默认为`net`。如未指定，则返回""，相当于`net`。   
在开平仓模式下仅可选择`long`或`short`。 如未指定，则返回""，对应于为交易开新仓位的方向（买入=>`long`，卖出=>`short`）。  
仅适用交割、永续。  
>> tgtCcy | String | 委托数量的类型   
定义`sz`属性的单位。仅适用于 instType=`SPOT`。有效值为`base_ccy`和`quote_ccy`。未指定时，默认为`base_ccy`。  
>> tradeQuoteCcy | String | 交易使用的计价币种。仅适用于 SPOT。  
默认值为 instId 的报价币种，例如：对于 `BTC-USD`，默认值为 `USD`。  
> groupId | String | 组合询价单ID  
只适用于组合询价单，普通询价单返回 ""  
> acctAlloc | Array of objects | 组合询价单的账户分配  
只适用于 Taker  
>> acct | String | 账户名  
>> legs | Array of objects | 组合交易  
>>> instId | String | 产品ID  
>>> sz | String | 委托数量  
>>> tdMode | String | 交易模式  
>>> ccy | String | 保证金币种  
>>> posSide | String | 持仓方向  
组合询价单介绍  
  
1\. allowPartialExecution 字段始终为 true，适用于 Taker 和 Maker 的组合询价单。  
2\. 新增返回参数 acctAlloc ，包含所有账户分配信息，但仅适用于 Taker。  
3\. 新增返回参数 groupId，适用于 Taker 和 Maker。  
4\. 对于组合询价单状态  
    1\. 如果任何分配账户处于待执行状态，则状态为 pending_fill  
    2\. 否则，  
        1\. 如果任何分配账户已成交，则状态为 filled  
        2\. 如果所有分配账户均失败，则状态为 failed