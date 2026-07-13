---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#block-trading
anchor_id: block-trading
api_type: API
updated_at: 2026-07-13 19:28:17.393656
---

# Block Trading

## Block Trading Workflow

A block trade is a **large sized, privately negotiated** transaction that allows traders to execute spot, perpetuals, futures, options and a combination of instruments (multi leg) which are traded **outside the order book** and at a **mutually agreed price** between the counter-parties. Once the transaction economics have been agreed upon, it will be submitted to OKX to be seamlessly margined, cleared and executed.

**Basic Concepts**

  1. **RFQs** \- Request for Quote sent by the Taker to Maker(s). It captures the quantity, instrument or multi instrument strategy that a Taker wants to trade.
  2. **Quotes** \- Quotes are created by the _Maker_  in response to a requested RFQ.
  3. **Trades** \- Trades occur when the _Taker_ successfully _executes_ upon a makers quote to an RFQ.

**High Level Workflow**

To trade as either Taker or Maker, users need to deposit at least 100,000 USD into their trading account. In addition, to become a Maker, [Please complete the form to access block trading](https://share.hsforms.com/1mYdfKtJJR3CC03IyCeC6hg3a1fq).

  1. Taker creates an RFQ and selects which counterparties to broadcast the RFQ to.
  2. Multiple Maker(s) send a two way quote as a response to the RFQ.
  3. Taker chooses to execute upon the best quote and the trade is sent to OKX for clearing & settlement.
  4. Taker & Maker receive confirmation of the trade's execution. 
  5. Trade economics are published to market feed. (minus counterparty info) 

**Self-trade Prevention** Users cannot send RFQ requests to themselves.

**Taker's Perspective**

  1. Taker creates an RFQ using `POST /api/v5/rfq/create-rfq`. Taker can pull available instruments via `GET /api/v5/public/instruments` and available counterparties from `GET /api/v5/rfq/counterparties`.
  2. Taker can cancel an RFQ anytime until it becomes inactive with `POST /api/v5/rfq/cancel-rfq`.
  3. Maker, who is a requested counterparty to the RFQ, and is notified over the `rfqs` WebSocket channel, can provide a Quote to the RFQ.
  4. Taker, who will be notified of quotes from the `quotes` WebSocket channel, can execute upon the best Quote with `POST /api/v5/rfq/execute-quote`.
  5. Taker will receive confirmation of the trade's successful execution on the `struc-block-trades` and `rfqs` WebSocket channel.
  6. Taker will also receive confirmation of the trade being completed on the `public-struc-block-trades` WebSocket channel as well as all other block trades on OKX.

**Maker's Perspective**

  1. Maker is notified about a new RFQ who they are a counterparty to, on the `rfqs` WebSocket channel.
  2. Maker can create a one way or two way Quote using `POST /api/v5/rfq/create-quote`.
  3. Maker can cancel an existing quote anytime until it becomes inactive with `POST /api/v5/rfq/cancel-quote`.
  4. Taker chooses to execute upon an available Quote.
  5. Maker will receive updates of their Quote from the `quotes` WebSocket channel.
  6. Maker will receive confirmation of the successful execution of their Quote from the `struc-block-trades` and `quotes` WebSocket channel.
  7. Maker will receive confirmation of the trade being completed on the `public-struc-block-trades` WebSocket channel as well as all other block trades on OKX.

## REST API

Block trading is not supported under spot mode. 

### Get Counterparties

Retrieves the list of counterparties that the user is permitted to trade with. 

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/rfq/counterparties`

> Request Example
    
    
    GET /api/v5/rfq/counterparties
    
    
    
    
    import okx.BlockTrading as BlockTrading
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading:0 , demo trading:1
    
    blockTradingAPI = BlockTrading.BlockTradingAPI(apikey, secretkey, passphrase, False, flag)
    
    # Get counterparts
    result = blockTradingAPI.counterparties()
    print(result)
    

#### Request parameters

None

> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "traderName" : "Satoshi Nakamoto",
                "traderCode" : "SATOSHI",
                "type" : "" 
            }
        ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
traderName | String | The long formative username of trader or entity on the platform.  
traderCode | String | A unique identifier of maker which will be publicly visible on the platform. All RFQ and Quote endpoints will use this as the unique counterparty identifier.  
type | String | The counterparty type. `LP` refers to API connected auto market makers.  
  
### Create RFQ

Creates a new RFQ

  
Please select trading bot "WAGMI" as the counterparty when submitting RFQs in demo trading.  
Prices provided on RFQs by the trading bot are for reference only.   

To learn more, please visit [Support center > FAQ > Trading > Liquid marketplace > Demo trading](/help/demo-trading)

#### Rate Limit: 5 requests per 2 seconds; 80 requests per 12 hours

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/rfq/create-rfq`

> Request Example
    
    
    POST /api/v5/rfq/create-rfq
    
    {
        "anonymous": true,
        "counterparties":[
            "Trader1",
            "Trader2"
        ],
        "allowPartialExecution":false,
        "clRfqId":"rfq01",
        "tag":"123456",
        "legs":[
            {
                "sz":"25",
                "side":"buy",
                "posSide": "long",
                "tdMode":"cross",
                "ccy":"USDT",
                "instId":"BTC-USD-221208-100000-C"
            },
            {
                "sz":"150",
                "side":"buy",
                "posSide": "long",
                "tdMode":"cross",
                "ccy":"USDT",
                "instId":"ETH-USDT",
                "tgtCcy":"base_ccy"
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
    
    # Create RFQ
    result = blockTradingAPI.create_rfq(
        anonymous=True,
        counterparties=[
            "Trader1",
            "Trader2"
        ],
        clRfqId= "rfq01",
        legs=[
            {
                "sz":"25",
                "side":"buy",
                "posSide": "long",
                "tdMode":"cross",
                "ccy":"USDT",
                "instId":"BTC-USD-221208-100000-C"
            },
            {
                "sz":"150",
                "side":"buy",
                "posSide": "long",
                "tdMode":"cross",
                "ccy":"USDT",
                "instId":"ETH-USDT",
                "tgtCcy":"base_ccy"
            }
        ]
    )
    print(result)
    

#### Request parameters

Parameter | Type | Required | Description  
---|---|---|---  
counterparties | Array of strings | Yes | The trader code(s) of the counterparties who receive the RFQ. Can be found via /api/v5/rfq/counterparties/  
anonymous | Boolean | No | Submit RFQ on a disclosed or anonymous basis. Valid values are `true` or `false`.   
If not specified, the default value is `false`.   
When anonymous = true, the taker’s identify is not disclosed to maker even after trade execution.  
clRfqId | String | No | Client-supplied RFQ ID.   
A combination of case-sensitive alpha-numeric, all numbers, or all letters of up to 32 characters.  
tag | String | No | RFQ tag.   
The block trade associated with the RFQ will have the same tag.   
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 16 characters.  
allowPartialExecution | Boolean | No | Whether the RFQ can be partially filled provided that the shape of legs stays the same. Valid values are `true` or `false`.   
`false` by default.  
legs | Array of objects | Yes | An Array of objects containing each leg of the RFQ. Maximum 15 legs can be placed per request  
> instId | String | Yes | The Instrument ID of each leg. Example : "BTC-USDT-SWAP"  
> tdMode | String | No | Trade mode   
Margin mode: `cross` `isolated`   
Non-Margin mode: `cash`.   
If not provided, tdMode will inherit default values set by the system shown below:   
Futures mode & SPOT: `cash`   
Buy options in Futures mode and Multi-currency Margin: `isolated`   
Other cases: `cross`  
> ccy | String | No | Margin currency.   
Only applicable to `cross` `MARGIN` orders in `Futures mode`. The parameter will be ignored in other scenarios.  
> sz | String | Yes | The size of each leg  
> lmtPx | String | No | Taker expected price for the RFQ  
  
If provided, RFQ trade will be automatically executed if the price from the quote is better than or equal to the price specified until the RFQ is canceled or expired.  
This field has to be provided for all legs to have the RFQ automatically executed, or leave empty for all legs, otherwise request will be rejected.  
The auto execution side depends on the leg side of the RFQ.  
For `SPOT/MARGIN/FUTURES/SWAP`, lmtPx will be in unit of the quote ccy.  
For `OPTION`, lmtPx will be in unit of settle ccy.  
The field will not be disclosed to counterparties.  
> side | String | Yes | The direction of each leg. Valid values can be `buy` or `sell`.  
> posSide | String | No | Position side.   
The default is `net` in the net mode. It can only be `long` or `short` in the long/short mode.   
If not specified, users in long/short mode always open new positions.   
Only applicable to `FUTURES`/`SWAP`.  
> tgtCcy | String | No | Defines the unit of the “sz” attribute.   
Only applicable to instType = SPOT.   
The valid enumerations are `base_ccy` and `quote_ccy`. When not specified, this is equal to `base_ccy` by default.  
> tradeQuoteCcy | String | No | The quote currency used for trading. Only applicable to SPOT.   
The default value is the quote currency of the instId, for example: for `BTC-USD`, the default is `USD`.  
acctAlloc | Array of objects | No | Account level allocation of the RFQ  
> acct | String | Yes | The name of the allocated account of the RFQ.  
> legs | Array of objects | Yes | The allocated legs of the account.  
>> sz | String | Yes | The allocated size of each leg  
>> instId | String | Yes | The Instrument ID of each leg. Example : "BTC-USDT-SWAP"  
>> tdMode | String | No | Trade mode  
>> ccy | String | No | Margin currency  
>> posSide | String | No | Position side  
  
> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "cTime":"1611033737572",
                "uTime":"1611033737572",
                "traderCode":"SATOSHI",
                "tag":"123456",
                "rfqId":"22534",
                "clRfqId":"rfq01",
                "allowPartialExecution":false,
                "state":"active",
                "validUntil":"1611033857557",
                "counterparties":[
                    "Trader1",
                    "Trader2"
                ],
                "legs":[
                    {
                        "instId":"BTC-USD-221208-100000-C",
                        "tdMode":"cross",
                        "ccy":"USDT",
                        "sz":"25",
                        "side":"buy",
                        "posSide": "long",
                        "tgtCcy":""
                    },
                    {
                        "instId":"ETH-USDT",
                        "tdMode":"cross",
                        "ccy":"USDT",
                        "sz":"150",
                        "side":"buy",
                        "posSide": "long",
                        "tgtCcy":"base_ccy",
                        "tradeQuoteCcy": "USDT"
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
data | Array of objects | Array of objects containing the results of the RFQ creation.  
> cTime | String | The timestamp the RFQ was created. Unix timestamp format in milliseconds.  
> uTime | String | The timestamp the RFQ was last updated. Unix timestamp format in milliseconds.  
> state | String | The status of the RFQ.   
Valid values can be `active` `canceled` `pending_fill` `filled` `expired` `traded_away` `failed`.   
`filled` indicates the RFQ was successfully executed against the maker's quote.   
`traded_away` only applies to Maker. The same RFQ can appear as `filled` to one maker and `traded_away` to another.   
Example: taker creates RFQ → makerA quotes pxA, makerB quotes pxB → pxA is better than pxB → taker executes quoteA → makerA sees `filled`, makerB sees `traded_away`.  
> counterparties | Array of strings | The list of counterparties traderCode the RFQ was broadcast to.  
> validUntil | String | The timestamp the RFQ expires. Unix timestamp format in milliseconds.   
If all legs are options, the RFQ will expire after 10 minutes; otherwise, the RFQ will expire after 2 minutes.  
> clRfqId | String | Client-supplied RFQ ID. This attribute is treated as client sensitive information. It will not be exposed to the Maker, only return empty string.  
> tag | String | RFQ tag. The block trade associated with the RFQ will have the same tag.  
> allowPartialExecution | Boolean | Whether the RFQ can be partially filled provided that the shape of legs stays the same.  
> traderCode | String | A unique identifier of taker.  
> rfqId | String | The unique identifier of the RFQ generated by system.  
> legs | Array of objects | An Array of objects containing each leg of the RFQ.  
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
Only applicable to FUTURES/SWAP.  
>> tgtCcy | String | Defines the unit of the “sz” attribute.   
Only applicable to instType = SPOT.   
The valid enumerations are `base_ccy` and `quote_ccy`. When not specified this is equal to `base_ccy` by default.  
>> tradeQuoteCcy | String | The quote currency used for trading. Only applicable to SPOT.   
The default value is the quote currency of the instId, for example: for `BTC-USD`, the default is `USD`.  
> groupId | String | Group RFQ ID  
Only applicable to group RFQ, return "" for normal RFQ  
> acctAlloc | Array of objects | Account level allocation of the RFQ  
>> acct | String | The name of the allocated account of the RFQ  
>> sCode | String | The code of the event execution result, 0 means success  
>> sMsg | String | Rejection message if the request is unsuccessful  
>> legs | Array of objects | The allocated legs of the account  
>>> instId | String | Instrument ID  
>>> sz | String | The calculated size of each leg of allocated account  
>>> tdMode | String | Trade mode  
>>> ccy | String | Margin currency  
>>> posSide | String | Position side  
Group RFQ introduction  
  
1\. Only a master account can conduct group RFQ and the available scope of allocated subaccounts is its normal and managed subaccounts.  
2\. Users will pass in acctAlloc request parameter to indicate the details of group RFQ account allocation, account name, instrument ID, allocated size, etc. master account is also allowed and should be indicated as "0". For tdMode, ccy and posSide fields, they will inherit the system default value if you leave them empty.  
3\. Add groupId, acctAlloc as a new response parameter.  
4\. The upper limit of the number of allocated subaccounts is 10. You will receive error code 70516 if you exceed the upper limit.  
5\. For each symbol, the total size of RFQ legs in all accounts should be equal to its combined amount in the group RFQ. If not, you will receive error code 70514.  
6\. For each sub-account, the ratio of a leg's size to the group RFQ must be the same across all symbols. If not, you will receive error code 70515. Here is an example:  
    1\. Parent RFQ legs  
        1\. Symbol: BTC-USDT, size: 50, symbol: ETH-USDT, size: 100  
    2\. Child RFQ legs, happy case  
        1\. Acct1: symbol: BTC-USDT, size: 30, symbol: ETH-USDT, size: 60 (ratio: 0.6)  
        2\. Acct2: symbol: BTC-USDT, size: 20, symbol: ETH-USDT, size: 40 (ratio: 0.4)  
    3\. Child RFQ legs, bad case  
        1\. Acct1: symbol: BTC-USDT, size: 30, symbol: ETH-USDT, size: 50  
        2\. Acct2: symbol: BTC-USDT, size: 20, symbol: ETH-USDT, size: 50  
        3\. The total size is equal. But the ratio is not equal for different legs per subaccount.  
7\. For allowPartialExecution field, it will be ignored even though users pass it in. For a group RFQ, allowPartialExecution will always be true, since taker can not determine whether the RFQ can be partially or fully filled if any subaccount fails. Thus, makers should regard it as a RFQ that can be partially filled.  
8\. Group RFQ will not be created if any subaccount fails.  

### Cancel RFQ

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
  
### Cancel multiple RFQs

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
  
### Cancel all RFQs

Cancels all active RFQs.

#### Rate Limit: 2 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/rfq/cancel-all-rfqs`

> Request Example
    
    
    POST /api/v5/rfq/cancel-all-rfqs
    
    
    
    
    import okx.BlockTrading as BlockTrading
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading:0 , demo trading:1
    
    blockTradingAPI = BlockTrading.BlockTradingAPI(apikey, secretkey, passphrase, False, flag)
    
    # Cancel all RFQs
    result = blockTradingAPI.cancel_all_rfqs()
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
> ts | String | The timestamp of successful cancellation. Unix timestamp format in milliseconds, e.g. 1597026383085.  
  
### Execute Quote

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

### Get Quote products

Retrieve the products which makers want to quote and receive RFQs for, and the corresponding price and size limit. 

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/rfq/maker-instrument-settings`

> Request Example
    
    
    GET /api/v5/rfq/maker-instrument-settings
    

#### Request parameters

None

> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "instType": "OPTION",
                "includeAll": true,
                "data": [
                    {
                        "instFamily": "BTC-USD",
                        "maxBlockSz": "10000",
                        "makerPxBand": "5"
                    },
                    {
                        "instFamily": "SOL-USD",
                        "maxBlockSz": "100000",
                        "makerPxBand": "15"
                    }
                ]
            },
            {
                "instType": "FUTURES",
                "includeAll": false,
                "data": [
                    {
                        "instFamily": "BTC-USD",
                        "maxBlockSz": "10000",
                        "makerPxBand": "5"
                    },
                    {
                        "instFamily": "ETH-USDT",
                        "maxBlockSz": "100000",
                        "makerPxBand": "15"
                    }
                ]
            },
            {
                "instType:": "SWAP",
                "includeAll": false,
                "data": [
                    {
                        "instFamily": "BTC-USD",
                        "maxBlockSz": "10000",
                        "makerPxBand": "5"
                    },
                    {
                        "instFamily": "ETH-USDT"
                    }
                ]
            },
            {
                "instType:": "SPOT",
                "includeAll": false,
                "data": [
                    {
                        "instId": "BTC-USDT"
                    },
                    {
                        "instId": "TRX-USDT"
                    }
                ]
            }
        ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
code | String | The result code, `0` means success.  
msg | String | The error message, not empty if the code is not `0`.  
data | Array of objects | Return data of the request.  
> instType | String | Type of instrument. Valid value can be `FUTURES`, `OPTION`, `SWAP` or `SPOT`.  
> includeAll | Boolean | Receive all instruments or not under specific instType setting.   
Valid value can be boolean (`True`/`False`). By default, the value will be `false`.  
> data | Array of objects | Elements of the instType.  
>> instFamily | String | Instrument family. Required for `FUTURES`, `OPTION` and `SWAP` only.  
>> instId | String | Instrument ID. Required for `SPOT` only.  
>> maxBlockSz | String | Max trade quantity for the product(s).   
For `FUTURES`, `OPTION` and `SWAP`, the max quantity of the RFQ/Quote is in unit of contracts. For `SPOT`, this parameter is in base currency.  
>> makerPxBand | String | Price bands in unit of ticks, measured against mark price.   
Setting makerPxBand to 1 tick means:   
If Bid price > Mark + 1 tick, it will be stopped   
If Ask price < Mark - 1 tick, It will be stopped  
  
### Set Quote products

Customize the products which makers want to quote and receive RFQs for, and the corresponding price and size limit. 

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/rfq/maker-instrument-settings`

> Request Example
    
    
    POST /api/v5/rfq/maker-instrument-settings
    body
    [
        {
         "instType": "OPTION",
         "data":
            [{
                "instFamily": "BTC-USD",
                "maxBlockSz": "10000",
                "makerPxBand": "5"
            },
            {
                "instFamily": "SOL-USD",
                "maxBlockSz": "100000",
                "makerPxBand": "15"
            }]
        },
        {
         "instType": "FUTURES",
         "data":
            [{
                "instFamily": "BTC-USD",
                "maxBlockSz": "10000",
                "makerPxBand": "5"
            },
            {
                "instFamily": "ETH-USDT",
                "maxBlockSz": "100000",
                "makerPxBand": "15"
            }]
        },
        {
         "instType": "SWAP",
         "data":
            [{
                "instFamily": "BTC-USD",
                "maxBlockSz": "10000",
                "makerPxBand": "5"
             },
            {
                "instFamily": "ETH-USDT"
            }]
        },
        {
        "instType": "SPOT",
         "data":
            [{
                "instId": "BTC-USDT"
             },
            {
                "instId": "TRX-USDT"
            }]
        }
    ]
    
    
    
    import okx.BlockTrading as BlockTrading
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading:0 , demo trading:1
    
    blockTradingAPI = BlockTrading.BlockTradingAPI(apikey, secretkey, passphrase, False, flag)
    
    # Set quote products
    data =[{
        "instType": "OPTION",
        "data": [{
                "uly": "BTC-USD",
                "maxBlockSz": "10000",
                "makerPxBand": "5"
            },
            {
                "uly": "SOL-USD",
                "maxBlockSz": "100000",
                "makerPxBand": "15"
            }
        ]
    }]
    
    result = blockTradingAPI.set_marker_instrument(
        data
    )
    print(result)
    

#### Request parameters

Parameter | Type | Required | Description  
---|---|---|---  
instType | String | Yes | Type of instrument. Valid value can be `FUTURES`, `OPTION`, `SWAP` or `SPOT`.  
includeAll | Boolean | No | Receive all instruments or not under specific instType setting.   
Valid value can be boolean (`True`/`False`). By default, the value will be `false`.  
data | Array of objects | Yes | Elements of the instType.  
> instFamily | String | Conditional | Instrument family. Required for `FUTURES`, `OPTION` and `SWAP` only.  
> instId | String | Conditional | Instrument ID. Required for `SPOT` only.  
> maxBlockSz | String | No | Max trade quantity for the product(s).   
For `FUTURES`, `OPTION` and `SWAP`, the max quantity of the RFQ/Quote is in unit of contracts. For `SPOT`, this parameter is in base currency.  
> makerPxBand | String | No | Price bands in unit of ticks, measured against mark price.   
Setting makerPxBand to 1 tick means:   
If Bid price > Mark + 1 tick, it will be stopped   
If Ask price < Mark - 1 tick, It will be stopped  
  
> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "result":true
            }
        ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
code | String | The result code, `0` means success.  
msg | String | The error message, not empty if the code is not `0`.  
data | Array of objects | Array of objects containing the results.  
> result | Boolean | Result of the request  
Valid value is `true` or `false`.  
  
### Reset MMP status

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
  
### Set MMP

This endpoint is used to set MMP configure and only applicable to block trading makers  

#### Rate Limit: 1 request per 10 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/rfq/mmp-config`

> Request Example
    
    
    POST /api/v5/rfq/mmp-config
    body
    {
        "timeInterval":"5000",
        "frozenInterval":"2000",
        "countLimit": "100"
    }
    
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
timeInterval | String | Yes | Time window (ms). MMP interval where monitoring is done.  
"0" means disable MMP. Maximum time interval is 600,000.  
frozenInterval | String | Yes | Frozen period (ms).   
"0" means the trade will remain frozen until you request "Reset MMP Status" to unfrozen.  
countLimit | String | Yes | Limit in number of execution attempts.  
  
> Response Example
    
    
    {
      "code": "0",
      "msg": "",
      "data": [
        {
            "frozenInterval":"2000",
            "countLimit": "100",
            "timeInterval":"5000"
        }
      ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
timeInterval | String | Time window (ms). MMP interval where monitoring is done  
frozenInterval | String | Frozen period (ms).  
countLimit | String | Limit in number of execution attempts  
Group RFQ introduction  
  
For RFQ makers, the execution attempt of group RFQ will only count once towards MMP regardless of how many account allocations involved. 

### Get MMP Config

This endpoint is used to get MMP configure information and only applicable to block trading market makers  

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/rfq/mmp-config`

> Request Example
    
    
    GET /api/v5/rfq/mmp-config
    
    

#### Request Parameters

none

> Response Example
    
    
    {
      "code": "0",
      "data": [
        {
          "frozenInterval": "2000",
          "mmpFrozen": true,
          "mmpFrozenUntil": "1000",
          "countLimit": "10",
          "timeInterval": "5000"
        }
      ],
      "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
timeInterval | String | Time window (ms). MMP interval where monitoring is done  
"0" means MMP is diabled  
frozenInterval | String | Frozen period (ms). If it is "0", the trade will remain frozen until manually reset and `mmpFrozenUntil` will be "".  
countLimit | String | Limit in number of execution attempts  
mmpFrozen | Boolean | Whether MMP is currently triggered. `true` or `false`  
mmpFrozenUntil | String | If frozenInterval is not "0" and mmpFrozen = True, it is the time interval (in ms) when MMP is no longer triggered, otherwise ""  
  
### Create Quote

Allows the user to Quote an RFQ that they are a counterparty to. The user MUST quote the entire RFQ and not part of the legs or part of the quantity. Partial quoting is not allowed.

Only one active quote is allowed per RFQ at a time. Submitting a new quote for the same `rfqId` will automatically cancel the existing active quote before the new one is created.

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
  
### Cancel Quote

Cancels an existing active Quote you have created in response to an RFQ.

If a new `create-quote` for the same `rfqId` is processed before this cancel request arrives, the original quote will already be in `canceled` state and this request will return error `70400`. This can occur when requests are sent from different connections or processes, which do not guarantee ordering. To ensure strict create→cancel sequencing, wait for the create-quote response before issuing the cancel, using a single connection.

#### Rate Limit: 50 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/rfq/cancel-quote`

> Request Example
    
    
    POST /api/v5/rfq/cancel-quote
    {
        "quoteId": "007",
        "clQuoteId":"Bond007"
    }
    
    
    
    import okx.BlockTrading as BlockTrading
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading:0 , demo trading:1
    
    blockTradingAPI = BlockTrading.BlockTradingAPI(apikey, secretkey, passphrase, False, flag)
    
    # Cancel quote
    result = blockTradingAPI.cancel_quote(
        quoteId="007",
        clQuoteId="Bond007"
    )
    print(result)
    

#### Request parameters

Parameter | Type | Required | Description  
---|---|---|---  
quoteId | String | Conditional | Quote ID.  
clQuoteId | String | Conditional | Client-supplied Quote ID. Either `quoteId` or `clQuoteId` is required. If both `clQuoteId` and `quoteId` are passed, `quoteId` will be treated as primary identifier.  
rfqId | String | No | RFQ ID.  
  
> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "quoteId":"007",
                "clQuoteId":"Bond007",
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
> quoteId | String | Quote ID  
> clQuoteId | String | Client-supplied Quote ID.  
> sCode | String | The code of the event execution result, `0` means success.  
> sMsg | String | Rejection message if the request is unsuccessful.  
  
### Cancel multiple Quotes

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
  
### Cancel all Quotes

Cancels all active Quotes.

#### Rate Limit: 2 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Trade

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
  
### Cancel All After

Cancel all quotes after the countdown timeout.

#### Rate Limit: 1 request per second

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/rfq/cancel-all-after`

> Request Example
    
    
    POST /api/v5/rfq/cancel-all-after
    body
    {
       "timeOut":"60"
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
timeOut | String | Yes | The countdown for quotes cancellation, with second as the unit.  
Range of value can be 0, [10, 120].   
Setting timeOut to 0 disables Cancel All After.  
  
> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "triggerTime":"1587971460",
                "ts":"1587971400"
            }
        ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
triggerTime | String | The time the cancellation is triggered.  
triggerTime=0 means Cancel All After is disabled.  
ts | String | The time the request is received.  
Users are recommended to send a request to the exchange every second. When the cancel all after is triggered, the trading engine will cancel quotes on behalf of the client one by one and this operation may take up to a few seconds. This feature is intended as a protection mechanism for clients only and clients should not use this feature as part of their trading strategies. 

### Get rfqs

Retrieves details of RFQs that the user is a counterparty to (either as the creator or the receiver of the RFQ). 

#### Rate Limit: 2 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

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

### Get quotes

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
  
### Get trades

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

### Get block tickers

Retrieve the latest block trading volume in the last 24 hours.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/market/block-tickers`

> Request Example
    
    
    GET /api/v5/market/block-tickers?instType=SWAP
    
    
    
    import okx.MarketData as MarketData
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    marketDataAPI =  MarketData.MarketAPI(flag=flag)
    
    # Retrieve the latest block trading volume in the last 24 hours
    result = marketDataAPI.get_block_tickers(
        instType="SPOT"
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instType | String | Yes | Instrument type  
`SPOT`  
`SWAP`  
`FUTURES`  
`OPTION`  
instFamily | String | No | Instrument family, e.g. `BTC-USD`  
Applicable to `FUTURES`/`SWAP`/`OPTION`  
  
> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
         {
            "instType":"SWAP",
            "instId":"LTC-USD-SWAP",
            "volCcy24h":"2222",
            "vol24h":"2222",
            "ts":"1597026383085"
         },
         {
            "instType":"SWAP",
            "instId":"BTC-USD-SWAP",
            "volCcy24h":"2222",
            "vol24h":"2222",
            "ts":"1597026383085"
        }
      ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
instId | String | Instrument ID  
instType | String | Instrument type  
volCcy24h | String | 24h trading volume, with a unit of `currency`.   
If it is a `derivatives` contract, the value is the number of base currency.   
If it is `SPOT`/`MARGIN`, the value is the quantity in quote currency.  
vol24h | String | 24h trading volume, with a unit of `contract`.   
If it is a `derivatives` contract, the value is the number of contracts.   
If it is `SPOT`/`MARGIN`, the value is the quantity in base currency.  
ts | String | Block ticker data generation time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
### Get block ticker

Retrieve the latest block trading volume in the last 24 hours.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/market/block-ticker`

> Request Example
    
    
    GET /api/v5/market/block-ticker?instId=LTC-USD-SWAP
    
    
    
    import okx.MarketData as MarketData
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    marketDataAPI =  MarketData.MarketAPI(flag=flag)
    
    # Retrieve the latest block trading volume in the last 24 hours
    result = marketDataAPI.get_block_ticker(
        instId="BTC-USDT"
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instId | String | Yes | Instrument ID, e.g. `BTC-USD-SWAP`  
  
> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
         {
            "instType":"SWAP",
            "instId":"LTC-USD-SWAP",
            "volCcy24h":"2222",
            "vol24h":"2222",
            "ts":"1597026383085"
         }
      ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
instId | String | Instrument ID  
instType | String | Instrument type  
volCcy24h | String | 24h trading volume, with a unit of `currency`.   
If it is a `derivatives` contract, the value is the number of base currency.   
If it is `SPOT`/`MARGIN`, the value is the quantity in quote currency.  
vol24h | String | 24h trading volume, with a unit of `contract`.   
If it is a `derivatives` contract, the value is the number of contracts.   
If it is `SPOT`/`MARGIN`, the value is the quantity in base currency.  
ts | String | Block ticker data generation time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
### Get public multi-leg transactions of block trades

Retrieves the executed block trades. The data will be updated 15 minutes after the block trade execution.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/rfq/public-trades`

> Request Example
    
    
    GET /api/v5/rfq/public-trades
    
    
    
    import okx.BlockTrading as BlockTrading
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading: 0, Demo trading: 1
    
    blockTradingAPI = BlockTrading.BlockTradingAPI(apikey, secretkey, passphrase, False, flag)
    
    # Retrieves the executed block trades
    result = blockTradingAPI.get_public_trades()
    print(result)
    

#### Request parameters

Parameter | Type | Required | Description  
---|---|---|---  
beginId | String | No | The starting blockTdId the request to begin with. Pagination of data to return records newer than the requested `blockTdId`, not including beginId.  
endId | String | No | The last blockTdId the request to end with. Pagination of data to return records earlier than the requested `blockTdId`, not including endId.  
limit | String | No | Number of results per request. The maximum is 100 which is also the default value.  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "blockTdId": "439161457415012352",
                "groupId": "",
                "legs": [
                    {
                        "instId": "BTC-USD-210826",
                        "side": "sell",
                        "sz": "100",
                        "px": "11000",
                        "tradeId": "439161457415012354"
                    },
                    {
                        "instId": "BTC-USD-SWAP",
                        "side": "sell",
                        "sz": "100",
                        "px": "50",
                        "tradeId": "439161457415012355"
                    },
                    {
                        "instId": "BTC-USDT",
                        "side": "buy",
                        "sz": "0.1", //for public feed, spot "sz" is in baseccy
                        "px": "10.1",
                        "tradeId": "439161457415012356"
                    },
                    {
                        "instId": "BTC-USD-210326-60000-C",
                        "side": "buy",
                        "sz": "200",
                        "px": "0.008",
                        "tradeId": "439161457415012357"
                    },
                    {
                        "instId": "BTC-USD-220930-5000-P",
                        "side": "sell",
                        "sz": "200",
                        "px": "0.008",
                        "tradeId": "439161457415012360"
                    },
                    {
                        "instId": "BTC-USD-220930-10000-C",
                        "side": "sell",
                        "sz": "200",
                        "px": "0.008",
                        "tradeId": "439161457415012361"
                    },
                    {
                        "instId": "BTC-USD-220930-10000-P",
                        "side": "sell",
                        "sz": "200",
                        "px": "0.008",
                        "tradeId": "439161457415012362"
                    },
                    {
                        "instId": "ETH-USD-220624-100100-C",
                        "side": "sell",
                        "sz": "100",
                        "px": "0.008",
                        "tradeId": "439161457415012363"
                    }
                ],
                "strategy":"CALL_CALENDAR_SPREAD",
                "cTime": "1650976251241"
            }
        ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
code | String | The result code, `0` means success.  
msg | String | The error message, not empty if the code is not 0.  
data | Array of objects | Array of objects containing the results of the public block trade.  
> strategy | String | Option strategy, e.g. CALL_CALENDAR_SPREAD  
> cTime | String | The time the trade was executed. Unix timestamp in milliseconds.  
> blockTdId | String | Block trade ID.  
> groupId | String | Group RFQ ID  
Only applicable to group RFQ, return "" for normal RFQ  
> legs | Array of objects | Legs of trade  
>> instId | String | Instrument ID, e.g. BTC-USDT-SWAP  
>> px | String | The price the leg executed  
>> sz | String | Trade quantity   
For spot trading, the unit is base currency  
For `FUTURES`/`SWAP`/`OPTION`, the unit is contract.  
>> side | String | The direction of the leg from the Takers perspective. Valid value can be buy or sell.  
>> tradeId | String | Last traded ID.  
Group RFQ introduction  
  
1\. Add new response parameter groupId, facilitating clients to map subaccount execution to group RFQ. Only applicable to group RFQ, return "" for normal RFQ.  
2\. Data return by this endpoint should be at **parent RFQ level** regardless of the subaccounts allocation. blockTdId and tradeId will be empty.  

### Get public single-leg transactions of block trades

Retrieve the recent block trading transactions of an instrument. Descending order by tradeId. The data will be updated 15 minutes after the block trade execution.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/public/block-trades`

> Request Example
    
    
    GET /api/v5/public/block-trades?instId=BTC-USDT
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instId | String | Yes | Instrument ID, e.g. `BTC-USDT`  
  
> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "fillVol": "5",
                "fwdPx": "26857.86591585",
                "groupId": "",
                "idxPx": "26889.7",
                "instId": "BTC-USD-231013-22000-P",
                "markPx": "0.0000000000000001",
                "px": "0.0026",
                "side": "buy",
                "sz": "1",
                "tradeId": "632960608383700997",
                "ts": "1697181568974"
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
instId | String | Instrument ID  
tradeId | String | Trade ID  
px | String | Trade price  
sz | String | Trade quantity   
For spot trading, the unit is base currency  
For `FUTURES`/`SWAP`/`OPTION`, the unit is contract.  
side | String | Trade side   
`buy`   
`sell`  
fillVol | String | Implied volatility   
Only applicable to `OPTION`  
fwdPx | String | Forward price   
Only applicable to `OPTION`  
idxPx | String | Index price   
Applicable to `FUTURES`, `SWAP`, `OPTION`  
markPx | String | Mark price   
Applicable to `FUTURES`, `SWAP`, `OPTION`  
groupId | String | Group RFQ ID  
Only applicable to group RFQ, return "" for normal RFQ  
ts | String | Trade time, Unix timestamp format in milliseconds, e.g. `1597026383085`.  
Up to 500 most recent historical public transaction data can be retrieved.  Group RFQ introduction  
  
1\. Add new response parameter groupId, facilitating clients to map subaccount execution to group RFQ. Only applicable to group RFQ, return "" for normal RFQ.  
2\. Data return by this endpoint should be at **child RFQ execution level** but split into a single leg. tradeId will be populated. 

## WebSocket Private Channel

### Rfqs channel

Retrieve the RFQs sent or received by the user. Data will be pushed whenever the user sends or receives an RFQ.

#### URL Path

/ws/v5/business (required login)

> Request Example
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "rfqs"
        }
      ]
    }
    
    
    
    import asyncio
    
    from okx.websocket.WsPrivateAsync import WsPrivateAsync
    
    
    def callbackFunc(message):
        print(message)
    
    async def main():
    
        ws = WsPrivateAsync(
            apiKey = "YOUR_API_KEY",
            passphrase = "YOUR_PASSPHRASE",
            secretKey = "YOUR_SECRET_KEY",
            url = "wss://ws.okx.com:8443/ws/v5/business",
            useServerTime=False
        )
        await ws.start()
        args = [
            {
              "channel": "rfqs"
            }
        ]
    
        await ws.subscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
        await ws.unsubscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
    
    asyncio.run(main())
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
id | String | No | Unique identifier of the message   
Provided by client. It will be returned in response message for identifying the corresponding request.   
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
op | String | Yes | Operation  
`subscribe`  
`unsubscribe`  
  
args | Array of objects | Yes | List of subscribed channels  
> channel | String | Yes | Channel name  
`rfqs`  
  
> Successful Response Example 
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
        "channel": "rfqs"
      },
      "connId": "a4d3ae55"
    }
    

> Failure Response Example
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"rfqs\"}]}",
      "connId": "a4d3ae55"
    }
    

#### Response parameters

Parameter | Type | Required | Description  
---|---|---|---  
id | String | No | Unique identifier of the message  
event | String | Yes | Operation  
`subscribe`  
`unsubscribe`  
`error`  
arg | Object | No | Subscribed channel  
> channel | String | Yes | Channel name  
`rfqs`  
code | String | No | Error code  
msg | String | No | Error message  
connId | String | Yes | WebSocket connection ID  
  
> Push Data Example
    
    
    {
        "arg":{
            "channel":"rfqs",
            "uid": "77982378738415879"
        },
        "data":[
            {
                "cTime":"1611033737572",
                "uTime":"1611033737572",
                "traderCode":"DSK2",
                "rfqId":"22534",
                "clRfqId":"",
                "tag":"123456",
                "state":"active",
                "flowType":"",
                "validUntil":"1611033857557",
                "allowPartialExecution": false,
                "counterparties":[
                    "DSK4",
                    "DSK5"
                ],
                "legs":[
                    {
                        "instId":"BTCUSD-211208-36000-C",
                        "tdMode":"cross",
                        "ccy":"USDT",
                        "sz":"25.0",
                        "side":"buy",
                        "posSide": "long",
                        "tgtCcy":""
                    },
                    {
                        "instId":"ETHUSD-211208-45000-C",
                        "tdMode":"cross",
                        "ccy":"USDT",
                        "sz":"25.0",
                        "side":"sell",
                        "posSide": "long",
                        "tgtCcy":""
                    }
                ]
            }
        ]
    }
    

#### Push data parameters

**Parameters** | **Types** | **Description**  
---|---|---  
arg | Object | Successfully subscribed channel  
> channel | String | Channel name  
> uid | String | User Identifier  
data | Array of objects | Subscribed data  
> cTime | String | The timestamp the RFQ was created, Unix timestamp format in milliseconds.  
> uTime | String | The timestamp the RFQ was updated latest, Unix timestamp format in milliseconds.  
> state | String | The status of the RFQ. Valid values can be `active`, `canceled`, `filled`, `expired` `traded_away` or `failed`.   
`filled` indicates the RFQ was successfully executed against the maker's quote.   
`traded_away` only applies to Maker. The same RFQ can appear as `filled` to one maker and `traded_away` to another.   
Example: taker creates RFQ → makerA quotes pxA, makerB quotes pxB → pxA is better than pxB → taker executes quoteA → makerA sees `filled`, makerB sees `traded_away`.  
> counterparties | Array of Strings | The list of counterparties traderCode the RFQ was broadcasted to.  
> validUntil | String | The timestamp the RFQ expires. Unix timestamp format in milliseconds.  
> clRfqId | String | Client-supplied RFQ ID. This attribute is treated as client sensitive information. It will not be exposed to the Maker. Return empty for Maker, eg. "".  
> tag | String | RFQ tag. The block trade associated with the RFQ will have the same tag.  
> flowType | String | Identify the type of the RFQ.   
Only applicable to Makers, return "" for Takers  
> traderCode | String | A unique identifier of taker. Empty If anonymous mode is `True`.  
> rfqId | String | RFQ ID  
> allowPartialExecution | Boolean | Whether the RFQ can be partially filled provided that the shape of legs stays the same.   
Valid value is `true` or `false`.   
`false` by default.  
> legs | Array of objects | An Array of objects containing each leg of the RFQ.  
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
>> sz | String | Size of the leg.  
>> side | String | The direction of the leg. Valid values can be buy or sell.  
>> posSide | String | Position side.   
The default is `net` in the net mode. If not specified, return "", which is equivalent to net.   
It can only be `long` or `short` in the long/short mode. If not specified, return "", which corresponds to the direction that opens new positions for the trade (buy => long, sell => short).   
Only applicable to `FUTURES`/`SWAP`.  
>> tgtCcy | String | Defines the unit of the “sz” attribute.   
Only applicable to instType = SPOT.   
The valid enumerations are `base_ccy` and `quote_ccy`. When not specified this is equal to `base_ccy` by default.  
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
state: pending_fill is a kind of moment state, and this channel doesn't update it.  Group RFQ introduction  
  
1\. allowPartialExecution field is always true for group RFQ for taker and maker.  
2\. Add a new response parameter acctAlloc with all account allocation the same as the initial request, but it is only applicable to takers.  
3\. Add a new response parameter groupId, applicable to both takers and makers.  
4\. For group RFQ state,  
        1\. if any allocated account is pending execution, then pending_fill  
        2\. otherwise,  
                1\. if any allocated account is filled, then filled  
                2\. if all allocated accounts are failed, then failed  

### Quotes channel

Retrieve the Quotes sent or received by the user. Data will be pushed whenever the user sends or receives a Quote.

#### URL Path

/ws/v5/business (required login)

> Request Example
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "quotes"
        }
      ]
    }
    
    
    
    import asyncio
    
    from okx.websocket.WsPrivateAsync import WsPrivateAsync
    
    
    def callbackFunc(message):
        print(message)
    
    async def main():
    
        ws = WsPrivateAsync(
            apiKey = "YOUR_API_KEY",
            passphrase = "YOUR_PASSPHRASE",
            secretKey = "YOUR_SECRET_KEY",
            url = "wss://ws.okx.com:8443/ws/v5/business",
            useServerTime=False
        )
        await ws.start()
        args = [
            {
              "channel": "quotes"
            }
        ]
    
        await ws.subscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
        await ws.unsubscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
    
    asyncio.run(main())
    
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
id | String | No | Unique identifier of the message   
Provided by client. It will be returned in response message for identifying the corresponding request.   
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
op | String | Yes | Operation  
`subscribe`  
`unsubscribe`  
  
args | Array of objects | Yes | List of subscribed channels  
> channel | String | Yes | Channel name  
`quotes`  
  
> Successful Response Example
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
        "channel": "quotes"
      },
      "connId": "a4d3ae55"
    }
    

> Failure Response Example
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"quotes\"}]}",
      "connId": "a4d3ae55"
    }
    

#### Response parameters

Parameter | Type | Required | Description  
---|---|---|---  
id | String | No | Unique identifier of the message  
event | String | Yes | Operation  
`subscribe`  
`unsubscribe`  
`error`  
arg | Object | No | Subscribed channel  
> channel | String | Yes | Channel name  
`quotes`  
code | String | No | Error code  
msg | String | No | Error message  
connId | String | Yes | WebSocket connection ID  
  
> Push Data Example
    
    
    {
        "arg":{
            "channel":"quotes",
            "uid": "77982378738415879"
        },
        "data":[
            {
                "validUntil":"1608997227854",
                "uTime":"1608267227834",
                "cTime":"1608267227834",
                "legs":[
                    {
                        "px":"0.0023",
                        "sz":"25.0",
                        "instId":"BTC-USD-220114-25000-C",
                        "tdMode":"cross",
                        "ccy":"USDT",
                        "side":"sell",
                        "posSide": "long",
                        "tgtCcy":""
    
                    },
                    {
                        "px":"0.0045",
                        "sz":"25",
                        "instId":"BTC-USD-220114-35000-C",
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
                "traderCode":"SATS",
                "quoteSide":"sell",
                "state":"canceled",
                "reason":"mmp_canceled",
                "clQuoteId":""
            }
        ]
    }
    

#### Push data parameters

**Parameters** | **Types** | **Description**  
---|---|---  
arg | Object | Successfully subscribed channel  
> channel | String | Channel name  
> uid | String | User Identifier  
data | Array of objects | Subscribed data  
> cTime | String | The timestamp the Quote was created, Unix timestamp format in milliseconds.  
> uTime | String | The timestamp the Quote was updated latest, Unix timestamp format in milliseconds.  
> state | String | The status of the quote. Valid values can be `active` `canceled` `filled` `expired` or `failed`.  
> reason | String | Reasons of state. Valid values can be mmp_canceled.  
> validUntil | String | The timestamp the Quote expires. Unix timestamp format in milliseconds.  
> rfqId | String | RFQ ID.  
> clRfqId | String | Client-supplied RFQ ID. This attribute is treated as client sensitive information. It will not be exposed to the Maker, just return empty string "" for Maker.  
> quoteId | String | Quote ID  
> clQuoteId | String | Client-supplied Quote ID. This attribute is treated as client sensitive information. It will not be exposed to the Taker, just return empty string "" for Taker.  
> tag | String | Quote tag. The block trade associated with the Quote will have the same tag.  
> traderCode | String | A unique identifier of maker. Empty If anonymous mode of Quote is `True`.  
> quoteSide | String | Top level side of Quote. Its value can be buy or sell.  
> legs | Array of objects | The legs of the Quote.  
>> instId | String | The instrument name of quoted leg.  
>> tdMode | String | Trade mode   
Margin mode: `cross` `isolated`   
Non-Margin mode: `cash`.   
If not provided, tdMode will inherit default values set by the system shown below:   
Futures mode & SPOT: `cash`   
Buy options in Futures mode and Multi-currency Margin: `isolated`   
Other cases: `cross`  
>> ccy | String | Margin currency.   
Only applicable to `cross` `MARGIN` orders in `Futures mode`. The parameter will be ignored in other scenarios.  
>> sz | String | The size of the quoted leg in contracts or spot.  
>> px | String | The price of the leg.  
>> side | String | The direction of the leg. Valid values can be buy or sell.  
>> posSide | String | Position side.   
The default is `net` in the net mode. If not specified, return "", which is equivalent to net.   
It can only be `long` or `short` in the long/short mode. If not specified, return "", which corresponds to the direction that opens new positions for the trade (buy => long, sell => short).   
Only applicable to `FUTURES`/`SWAP`.  
>> tgtCcy | String | Defines the unit of the “sz” attribute.   
Only applicable to instType = SPOT.   
The valid enumerations are `base_ccy` and `quote_ccy`. When not specified this is equal to `base_ccy` by default.  
>> tradeQuoteCcy | String | The quote currency used for trading. Only applicable to SPOT.   
The default value is the quote currency of the instId, for example: for `BTC-USD`, the default is `USD`.  
  
### Structure block trades channel

Retrieve user's block trades data. All the legs in the same block trade are included in the same update. Data will be pushed whenever there is a block trade that the user is a counterparty for (i.e. the taker or the executing maker). Makers who received a `traded_away` status will not receive data from this channel.

#### URL Path

/ws/v5/business (required login)

> Request Example
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "struc-block-trades"
        }
      ]
    }
    
    
    
    import asyncio
    
    from okx.websocket.WsPrivateAsync import WsPrivateAsync
    
    
    def callbackFunc(message):
        print(message)
    
    async def main():
    
        ws = WsPrivateAsync(
            apiKey = "YOUR_API_KEY",
            passphrase = "YOUR_PASSPHRASE",
            secretKey = "YOUR_SECRET_KEY",
            url = "wss://ws.okx.com:8443/ws/v5/business",
            useServerTime=False
        )
        await ws.start()
        args = [
            {
              "channel": "struc-block-trades"
            }
        ]
    
        await ws.subscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
        await ws.unsubscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
    
    asyncio.run(main())
    
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
id | String | No | Unique identifier of the message   
Provided by client. It will be returned in response message for identifying the corresponding request.   
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
op | String | Yes | Operation  
`subscribe`  
`unsubscribe`  
  
args | Array of objects | Yes | List of subscribed channels  
> channel | String | Yes | Channel name  
`struc-block-trades`  
  
> Successful Response Example
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
        "channel": "struc-block-trades"
      },
      "connId": "a4d3ae55"
    }
    

> Failure Response Example
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"struc-block-trades\""}]}",
      "connId": "a4d3ae55"
    }
    

#### Response parameters

Parameter | Type | Required | Description  
---|---|---|---  
id | String | No | Unique identifier of the message  
event | String | Yes | Operation  
`subscribe`  
`unsubscribe`  
`error`  
arg | Object | No | Subscribed channel  
> channel | String | Yes | Channel name  
`struc-block-trades`  
code | String | No | Error code  
msg | String | No | Error message  
connId | String | Yes | WebSocket connection ID  
  
> Push Data Example
    
    
    {
        "arg":{
            "channel":"struc-block-trades",
            "uid": "77982378738415879"
        },
        "data":[
            {
                "cTime":"1608267227834",
                "rfqId":"18753",
                "clRfqId":"",
                "quoteId":"25092",
                "clQuoteId":"",
                "blockTdId":"180184",
                "tag":"123456",
                "tTraderCode":"ANAND",
                "mTraderCode":"WAGMI",
                "isSuccessful": true,
                "errorCode": "",
                "legs":[
                    {
                        "px":"0.0023",
                        "sz":"25.0",
                        "instId":"BTC-USD-20220630-60000-C",
                        "side":"sell",
                        "fee":"0.1001",
                        "feeCcy":"BTC",
                        "tradeId":"10211",
                        "tgtCcy":""
    
                    },
                    {
                        "px":"0.0033",
                        "sz":"25",
                        "instId":"BTC-USD-20220630-50000-C",
                        "side":"buy",
                        "fee":"0.1001",
                        "feeCcy":"BTC",
                        "tradeId":"10212",
                        "tgtCcy":""
    
                    }
                ]
            }
        ]
    }
    

#### Push data parameters

**Parameters** | **Types** | **Description**  
---|---|---  
arg | Object | Successfully subscribed channel  
> channel | String | Channel name  
> uid | String | User Identifier  
data | Array of objects | Subscribed data  
> cTime | String | The time the trade was executed. Unix timestamp in milliseconds.  
> rfqId | String | RFQ ID.  
> clRfqId | String | Client-supplied RFQ ID. This attribute is treated as client sensitive information. It will not be exposed to the Maker, just return empty string "" for Maker.  
> quoteId | String | Quote ID.  
> clQuoteId | String | Client-supplied Quote ID. This attribute is treated as client sensitive information. It will not be exposed to the Taker, just return empty string "" for Taker.  
> blockTdId | String | Block trade ID.  
> tag | String | Trade tag. The block trade will have the tag of the RFQ or Quote it corresponds to.  
> tTraderCode | String | A unique identifier of the Taker. Empty If anonymous mode of RFQ is `True`.  
> mTraderCode | String | A unique identifier of the Maker. Empty If anonymous mode of Quote is `True`.  
> isSuccessful | Boolean | Whether the trade is filled successfully  
> errorCode | String | Error code for unsuccessful trades.   
It is "" for successful trade.  
> legs | Array of objects | Legs of trade  
>> instId | String | Instrument ID, e.g. BTC-USDT-SWAP  
>> px | String | The price the leg executed  
>> sz | String | Size of the leg.  
>> side | String | The direction of the leg. Valid value can be buy or sell.  
>> tgtCcy | String | Defines the unit of the “sz” attribute.   
Only applicable to instType = SPOT.   
The valid enumerations are `base_ccy` and `quote_ccy`. When not specified this is equal to `base_ccy` by default.  
>> fee | String | Fee. Negative number represents the user transaction fee charged by the platform. Positive fee represents rebate.  
>> feeCcy | String | Fee currency  
>> tradeId | String | Last traded ID.  
> acctAlloc | Array of objects | Applicable to both taker, maker  
>> blockTdId | String | Block trade ID  
>> errorCode | String | Error code for unsuccessful trades.It is "0" for successful trade.  
>> acct | String | The name of the allocated account of the RFQOnly applicable to taker, return "" to makers  
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
6\. Parent RFQ blockTdId or legs tradeId will be empty. However, account allocation breakdown will be offered and tradeId will be attached.  

## WebSocket Public Channel

### Public structure block trades channel

Retrieve the recent block trades data in OKX. All the legs in the same block trade are included in the same update. The data will be pushed 15 minutes after the block trade execution.

#### URL Path

/ws/v5/business

> Request Example
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "public-struc-block-trades"
        }
      ]
    }
    
    
    
    import asyncio
    from okx.websocket.WsPublicAsync import WsPublicAsync
    
    def callbackFunc(message):
        print(message)
    
    async def main():
        ws = WsPublicAsync(url="wss://wspap.okx.com:8443/ws/v5/business")
        await ws.start()
        args = [
            {
              "channel": "public-struc-block-trades"
            }
        ]
    
        await ws.subscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
        await ws.unsubscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
    asyncio.run(main())
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
id | String | No | Unique identifier of the message   
Provided by client. It will be returned in response message for identifying the corresponding request.   
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
op | String | Yes | Operation  
`subscribe`  
`unsubscribe`  
  
args | Array of objects | Yes | List of subscribed channels  
> channel | String | Yes | Channel name  
`public-struc-block-trades`  
  
> Successful Response Example
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
        "channel": "public-struc-block-trades"
      },
      "connId": "a4d3ae55"
    }
    

> Failure Response Example
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"public-struc-block-trades\""}]}",
      "connId": "a4d3ae55"
    }
    

#### Response parameters

Parameter | Type | Required | Description  
---|---|---|---  
id | String | No | Unique identifier of the message  
event | String | Yes | Operation  
`subscribe`  
`unsubscribe`  
`error`  
arg | Object | No | Subscribed channel  
> channel | String | Yes | Channel name  
`public-struc-block-trades`  
code | String | No | Error code  
msg | String | No | Error message  
connId | String | Yes | WebSocket connection ID  
  
> Push Data Example
    
    
    {
        "arg":{
            "channel":"public-struc-block-trades"
        },
        "data":[
            {
    
                "cTime":"1608267227834",
                "blockTdId":"1802896",
                "groupId":"",
                "legs":[
                    {
                        "px":"0.323",
                        "sz":"25.0",
                        "instId":"BTC-USD-20220114-13250-C",
                        "side":"sell",
                        "tradeId":"15102"
                    },
                    {
                        "px":"0.666",
                        "sz":"25",
                        "instId":"BTC-USD-20220114-21125-C",
                        "side":"buy",
                        "tradeId":"15103"
                    }
                ]
            }
        ]
    }
    

#### Push data parameters

**Parameters** | **Types** | **Description**  
---|---|---  
arg | Object | Successfully subscribed channel  
> channel | String | Channel name  
data | Array of objects | Subscribed data  
> cTime | String | The time the trade was executed. Unix timestamp in milliseconds.  
> blockTdId | String | Block trade ID.  
> groupId | String | Group RFQ ID  
Only applicable to group RFQ, return "" for normal RFQ  
> legs | Array of objects | Legs of trade  
>> instId | String | Instrument ID, e.g. BTC-USDT-SWAP  
>> px | String | The price the leg executed  
>> sz | String | Trade quantity   
For spot trading, the unit is base currency  
For `FUTURES`/`SWAP`/`OPTION`, the unit is contract.  
>> side | String | The direction of the leg from the Takers perspective. Valid value can be `buy` or `sell`.  
>> tradeId | String | Last traded ID.  
Group RFQ introduction  
  
1\. Add new response parameter groupId, facilitating clients to map subaccount execution to group RFQ. Only applicable to group RFQ, return "" for normal RFQ.  
2\. Data return by this endpoint should be at **parent RFQ level** regardless of the subaccounts allocation. blockTdId and tradeId will be empty.  Mapping blockTdId to rfqId  
  
For normal RFQs, each `blockTdId` has a 1:1 relationship with an `rfqId`. For Group RFQs, one `rfqId` may correspond to multiple `blockTdId`s.  
  
This channel does not include `rfqId` directly. Users who are counterparties to the trade (taker and executing maker) can subscribe to the private [Structure block trades channel](/docs-v5/en/#block-trading-websocket-private-channel-structure-block-trades-channel), which provides both `rfqId` and `blockTdId`, enabling cross-referencing between the two channels. 

### Public block trades channel

Retrieve the recent block trades data by individual legs. Each leg in a block trade is pushed in a separate update. The data will be pushed 15 minutes after the block trade execution.

#### URL Path

/ws/v5/business

> Request Example
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "public-block-trades",
          "instId": "BTC-USDT-SWAP"
        }
      ]
    }
    
    
    
    import asyncio
    from okx.websocket.WsPublicAsync import WsPublicAsync
    
    def callbackFunc(message):
        print(message)
    
    async def main():
        ws = WsPublicAsync(url="wss://wspap.okx.com:8443/ws/v5/business")
        await ws.start()
        args = [
            {
              "channel": "public-block-trades",
              "instId": "BTC-USDT-SWAP"
            }
        ]
    
        await ws.subscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
        await ws.unsubscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
    asyncio.run(main())
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
id | String | No | Unique identifier of the message   
Provided by client. It will be returned in response message for identifying the corresponding request.   
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
op | String | Yes | Operation  
`subscribe`  
`unsubscribe`  
  
args | Array of objects | Yes | List of subscribed channels  
> channel | String | Yes | Channel name  
`public-block-trades`  
> instId | String | Yes | Instrument ID, e.g. BTC-USDT-SWAP.  
  
> Successful Response Example
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
        "channel": "public-block-trades",
        "instId": "BTC-USDT-SWAP",
        "connId": "a4d3ae55"
      }
    }
    

> Failure Response Example
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"args\":[{ \"channel\" : \"public-block-trades\""}]}",
      "connId": "a4d3ae55"
    }
    

#### Response parameters

Parameter | Type | Required | Description  
---|---|---|---  
id | String | No | Unique identifier of the message  
event | String | Yes | Operation  
`subscribe`  
`unsubscribe`  
`error`  
arg | Object | No | Subscribed channel  
> channel | String | Yes | Channel name  
`public-block-trades`  
> instId | String | Yes | Instrument ID, e.g. BTC-USDT-SWAP.  
code | String | No | Error code  
msg | String | No | Error message  
connId | String | Yes | WebSocket connection ID  
  
> Push Data Example
    
    
    {
       "arg":{
          "channel":"public-block-trades",
          "instId":"BTC-USD-231020-5000-P"
       },
       "data":[
          {
             "fillVol":"5",
             "fwdPx":"26808.16",
             "groupId":"",
             "idxPx":"27222.5",
             "instId":"BTC-USD-231020-5000-P",
             "markPx":"0.0022406326071111",
             "px":"0.0048",
             "side":"buy",
             "sz":"1",
             "tradeId":"633971452580106242",
             "ts":"1697422572972"
          }
       ]
    }
    

#### Push data parameters

**Parameters** | **Types** | **Description**  
---|---|---  
arg | Object | Successfully subscribed channel  
> channel | String | Channel name  
> instId | String | Instrument ID, e.g. BTC-USDT-SWAP.  
data | Array of objects | Information of the public trade object.  
> instId | String | Instrument ID, e.g. BTC-USDT-SWAP.  
> tradeId | String | Trade ID, generated by counter.  
> px | String | The price the leg executed.  
> sz | String | Trade quantity   
For spot trading, the unit is base currency  
For `FUTURES`/`SWAP`/`OPTION`, the unit is contract.  
> side | String | Trade direction, buy, sell, from taker perspective.  
> fillVol | String | Implied volatility   
Only applicable to `OPTION`  
> fwdPx | String | Forward price   
Only applicable to options  
> idxPx | String | Index price   
Applicable to `FUTURES`, `SWAP`, `OPTION`  
> markPx | String | Mark price   
Applicable to `FUTURES`, `SWAP`, `OPTION`  
> groupId | String | Group RFQ ID  
Only applicable to group RFQ, return "" for normal RFQ  
> ts | String | Filled time, Unix timestamp format in milliseconds, e.g. 1597026383085.  
Group RFQ introduction  
  
1\. Add new response parameter groupId, facilitating clients to map subaccount execution to group RFQ. Only applicable to group RFQ, return "" for normal RFQ.  
2\. Data return by this endpoint should be at **child RFQ execution level** but split into a single leg. tradeId will be populated.  

### Block tickers channel

Retrieve the latest block trading volume in the last 24 hours.

The data will be pushed when triggered by transaction execution event. In addition, it will also be pushed in 5 minutes interval according to subscription granularity.

#### URL Path

/ws/v5/business

> Request Example
    
    
    {
        "id": "1512",
        "op": "subscribe",
        "args": [{
            "channel": "block-tickers",
            "instId": "BTC-USDT"
        }]
    }
    
    
    
    import asyncio
    from okx.websocket.WsPublicAsync import WsPublicAsync
    
    def callbackFunc(message):
        print(message)
    
    async def main():
        ws = WsPublicAsync(url="wss://wspap.okx.com:8443/ws/v5/business")
        await ws.start()
        args = [{
            "channel": "block-tickers",
            "instId": "BTC-USDT"
        }]
    
        await ws.subscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
        await ws.unsubscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
    asyncio.run(main())
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
id | String | No | Unique identifier of the message   
Provided by client. It will be returned in response message for identifying the corresponding request.   
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
op | String | Yes | Operation  
`subscribe`  
`unsubscribe`  
  
args | Array of objects | Yes | List of subscribed channels  
> channel | String | Yes | Channel name  
`block-tickers`  
> instId | String | Yes | Instrument ID e.g. BTC-USDT-SWAP  
  
> Successful Response Example
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
        "channel": "block-tickers",
        "instId": "LTC-USD-200327"
      },
      "connId": "a4d3ae55"
    }
    

> Failure Response Example
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"block-tickers\", \"instId\" : \"LTC-USD-200327\"}]}",
      "connId": "a4d3ae55"
    }
    

#### Response parameters

Parameter | Type | Required | Description  
---|---|---|---  
id | String | No | Unique identifier of the message  
event | String | Yes | Event  
`subscribe`  
`unsubscribe`  
`error`  
arg | Object | No | Subscribed channel  
> channel | String | Yes | Channel name  
`block-tickers`  
> instId | String | Yes | Instrument ID  
code | String | No | Error code  
msg | String | No | Error message  
connId | String | Yes | WebSocket connection ID  
  
> Push Data Example
    
    
    {
        "arg": {
            "channel": "block-tickers"
        },
        "data": [
            {
                "instType": "SWAP",
                "instId": "LTC-USD-SWAP",
                "volCcy24h": "0",
                "vol24h": "0",
                "ts": "1597026383085"
            }
        ]
    }
    

#### Push data parameters

**Parameter** | **Type** | **Description**  
---|---|---  
arg | Object | Successfully subscribed channel  
> channel | String | Channel name  
> instId | String | Instrument ID  
data | Array of objects | Subscribed data  
> instId | String | Instrument ID  
> instType | String | Instrument type  
> volCcy24h | String | 24h trading volume, with a unit of `currency`.   
If it is a `derivatives` contract, the value is the number of base currency.   
If it is `SPOT`/`MARGIN`, the value is the quantity in quote currency.  
> vol24h | String | 24h trading volume, with a unit of `contract`.   
If it is a `derivatives` contract, the value is the number of contracts.   
If it is `SPOT`/`MARGIN`, the value is the quantity in base currency.  
> ts | String | Block ticker data generation time, Unix timestamp format in milliseconds, e.g. `1597026383085`

---

# 大宗交易

## 大宗交易工作流程 

大宗交易时指在非公开市场进行的、私下议定的、满足规定最小交易手数的期货、期权、交割、永续或混合产品的大单交易。 交易细节一经确认，此笔交易会被提交到OKX以进行保证金计算，清算和执行。

**基本概念**

  1. **询价单（RFQs） -** 询价单，由询价方发给报价方. 询价单包括询价方希望交易的一种或多种产品及其数量。
  2. **报价单 -** 报价单，由报价方发给询价方对询价单的报价。
  3. **交易** \- 当询价方接受并执行报价方的报价单，一笔交易就由此产生。

**基本工作流程**

要以询价方或报价方身份进行交易，用户需要在交易账户中存入至少100,000美元。 此外，要成为报价方[请填写表格以访问大宗交易](https://share.hsforms.com/1mYdfKtJJR3CC03IyCeC6hg3a1fq).

  1. 询价方创建一个询价单（RFQ），并选择希望收到此询价单的报价方。 
  2. 不同报价方发送报价单回应此询价单。
  3. 询价方选择执行最好的报价单产生交易。OKX收到此笔交易并做结算。
  4. 询价方和报价方收到交易执行的确认。
  5. 交易详情发布在公共市场数据频道上（不包含交易方信息）。

**询价方角度**

  1. 询价方使用`POST /api/v5/rfq/create-rfq`创建询价单。询价方可通过`GET /api/v5/public/instruments`查询可询价产品信息，并通过`GET /api/v5/rfq/counterparties`查询可选择报价方信息。
  2. 询价方可以在询价单有效的任何时候通过`POST /api/v5/rfq/cancel-rfq`取消询价单。
  3. 报价方，如果是询价方选择的报价方之一，会在`rfqs`推送频道收到询价单信息，并可作出相应报价。
  4. 询价方，在`quotes`推送频道收到报价信息后，可以选择最优报价并通过`POST /api/v5/rfq/execute-quote`执行。
  5. 询价方会在`struc-block-trades`和`rfqs`推送频道收到交易成功执行确认。
  6. 询价方也会在`public-struc-block-trades`推送频道收到此笔交易以及其他OKX大宗交易的确认信息。

**报价方角度**

  1. 当有一个新的询价单发出，并且报价方是被选择的报价方之一时，报价方会在rfqs推送频道接收到此询价单信息。
  2. 报价方创建一个单向或者双向的报价单并通过`POST /api/v5/rfq/create-quote`发出。
  3. 报价方可以通过`POST /api/v5/rfq/cancel-quote`任意取消一个有效的报价单。
  4. 询价方选择执行最优报价单。
  5. 报价方通过`quotes`推送频道接收他们报价单的状态更新。
  6. 报价方会在`struc-block-trades`和`quotes`推送频道收到他们报价单的交易成功执行确认。
  7. 报价方也会在`public-struc-block-trades`推送频道收到此笔交易以及其他OKX大宗交易的确认信息。

## REST API 

现货模式下不支持大宗交易 

### 获取报价方信息 

查询可以参与交易的报价方信息。

#### 限速: 5次/2s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/rfq/counterparties`

> 请求示例
    
    
    GET /api/v5/rfq/counterparties
    
    
    
    
    import okx.BlockTrading as BlockTrading
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘：1
    
    blockTradingAPI = BlockTrading.BlockTradingAPI(apikey, secretkey, passphrase, False, flag)
    
    # 获取报价方信息
    result = blockTradingAPI.counterparties()
    print(result)
    

#### 请求参数

无

> 响应示例
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "traderName" : "Satoshi Nakamoto",
                "traderCode" : "SATOSHI",
                "type" : "" 
            }
        ]
    }
    

#### 响应参数

参数名 | 类型 | 描述  
---|---|---  
traderName | String | 报价方名称  
traderCode | String | 报价方唯一标识代码，公开可见；报价和询价的相关接口都使用该代码代表报价方。  
type | String | 报价方类型。`LP`指通过API连接的自动做市商。  
  
### 询价 

创建一个询价单。

  
在模拟交易中询价时，请选择交易机器人“WAGMI”作为交易对手。  
交易机器人提供的报价仅供参考。 

了解更多，请访问[帮助中心 > 常见问题 > 交易 > 流动性市场 > 模拟交易](/cn/help/demo-trading)

#### 限速: 5次/2s；80次/12h

#### 限速规则：User ID

#### 权限：交易

#### HTTP Requests

`POST /api/v5/rfq/create-rfq`

> 请求示例
    
    
    POST /api/v5/rfq/create-rfq
    
    {
        "anonymous": true,
        "counterparties":[
            "Trader1",
            "Trader2"
        ],
        "allowPartialExecution":false,
        "clRfqId":"rfq01",
        "tag":"123456",
        "legs":[
            {
                "sz":"25",
                "side":"buy",
                "posSide": "long",
                "tdMode":"cross",
                "ccy":"USDT",
                "instId":"BTC-USD-221208-100000-C"
            },
            {
                "sz":"150",
                "side":"buy",
                "posSide": "long",
                "tdMode":"cross",
                "ccy":"USDT",
                "instId":"ETH-USDT",
                "tgtCcy":"base_ccy"
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
    
    # 询价
    result = blockTradingAPI.create_rfq(
        anonymous=True,
        counterparties=[
            "Trader1",
            "Trader2"
        ],
        clRfqId= "rfq01",
        legs=[
            {
                "sz":"25",
                "side":"buy",
                "posSide": "long",
                "tdMode":"cross",
                "ccy":"USDT",
                "instId":"BTC-USD-221208-100000-C"
            },
            {
                "sz":"150",
                "side":"buy",
                "posSide": "long",
                "tdMode":"cross",
                "ccy":"USDT",
                "instId":"ETH-USDT",
                "tgtCcy":"base_ccy"
            }
        ]
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
counterparties | Array of strings | 是 | 希望收到询价的报价方列表，可通过`/api/v5/rfq/counterparties/`获取。  
anonymous | Boolean | 否 | 是否匿名询价，`true`表示匿名询价，`false`表示公开询价，默认值为 `false`，为`true`时，即使在交易执行之后，身份也不会透露给报价方。  
clRfqId | String | 否 | 询价单自定义ID，字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度要在1-32位之间。  
tag | String | 否 | 询价单标签，与此询价单关联的大宗交易将有相同的标签。   
字母（区分大小写）与数字的组合，可以是纯字母、纯数字，且长度在1-16位之间。  
allowPartialExecution | Boolean | 否 | RFQ是否可以被部分执行，如果腿的比例和原RFQ一致。有效值为`true`或`false`。默认为`false`。  
legs | Array of objects | 是 | 组合交易，每次最多可以提交15组交易信息  
> instId | String | 是 | 产品ID  
> tdMode | String | 否 | 交易模式   
保证金模式：`cross`全仓 `isolated`逐仓   
非保证金模式：`cash`非保证金.   
如未提供，tdMode 将继承系统设置的默认值：   
合约模式 & 现货: `cash`   
`合约模式`和`跨币种保证金模式`下买入期权： `isolated`   
其他情况: `cross`  
> ccy | String | 否 | 保证金币种，仅适用于`合约模式`下的`全仓杠杆`订单   
在其他情况下该参数将被忽略。  
> sz | String | 是 | 委托数量  
> lmtPx | String | 否 | 询价方期望的报价价格  
若提供了该字段，在报价价格优于或等于所指定价格，询价将自动被执行，直到该询价单被取消或过期为止。  
该字段必须提供所有组合交易的价格，以便自动执行询价；或者对所有组合交易留空，否则请求将被拒绝。  
自动执行的方向取决于询价单的腿方向。  
对于`币币/币币杠杆/交割/永续`，lmtPx将以计价货币单位计算。  
对于`期权`，lmtPx将以结算货币单位计算。  
该字段不会被披露给交易对手方。  
> side | String | 是 | 询价单方向  
> posSide | String | 否 | 持仓方向   
买卖模式下默认为`net`。在开平仓模式下仅可选择`long`或`short`。   
如未指定，则处于开平仓模式下的用户始终会开新仓位。   
仅适用交割、永续。  
> tgtCcy | String | 否 | 委托数量的类型   
定义`sz`属性的单位。仅适用于 instType=`SPOT`。有效值为`base_ccy`和`quote_ccy`。未指定时，默认为`base_ccy`。  
> tradeQuoteCcy | String | 否 | 交易使用的计价币种。仅适用于 SPOT。  
默认值为 instId 的报价币种，例如：对于 `BTC-USD`，默认值为 `USD`。  
acctAlloc | Array of objects | No | 组合询价单的账户分配  
> acct | String | Yes | 账户名  
> legs | Array of objects | Yes | 组合交易  
>> sz | String | Yes | 委托数量  
>> instId | String | Yes | 产品ID  
>> tdMode | String | No | 交易模式  
>> ccy | String | No | 保证金币种  
>> posSide | String | No | 持仓方向  
  
> 返回示例
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "cTime":"1611033737572",
                "uTime":"1611033737572",
                "traderCode":"SATOSHI",
                "tag":"123456",
                "rfqId":"22534",
                "clRfqId":"rfq01",
                "allowPartialExecution":false,
                "state":"active",
                "validUntil":"1611033857557",
                "counterparties":[
                    "Trader1",
                    "Trader2"
                ],
                "legs":[
                    {
                        "instId":"BTC-USD-221208-100000-C",
                        "sz":"25",
                        "side":"buy",
                        "posSide": "long",
                        "tdMode":"cross",
                        "ccy":"USDT",
                        "tgtCcy":""
                    },
                    {
                        "instId":"ETH-USDT",
                        "sz":"150",
                        "side":"buy",
                        "posSide": "long",
                        "tdMode":"cross",
                        "ccy":"USDT",
                        "tgtCcy":"base_ccy",
                        "tradeQuoteCcy": "USDT"
                    }
                ]
            }
        ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
code | String | 结果代码，0 表示成功。  
msg | String | 错误信息，如果代码不为 0，则不为空。  
data | Array of objects | 询价单结果  
> cTime | String | 询价单创建时间，Unix时间戳的毫秒数格式。  
> uTime | String | 询价单状态更新时间，Unix时间戳的毫秒数格式。  
> state | String | 询价单的状态  
有效值为 `active` `canceled` `pending_fill` `filled` `expired` `traded_away` `failed`   
`filled` 表示询价单已成功按照做市商的报价成交。  
`traded_away` 仅适用于报价方。同一笔询价单可能对一个报价方显示为 `filled`，而对另一个报价方显示为 `traded_away`。  
示例：询价方创建询价单 → 做市商A报价 pxA，做市商B报价 pxB → pxA 优于 pxB → 询价方执行做市商A的报价 → 做市商A看到 `filled`，做市商B看到 `traded_away`。  
> counterparties | Array of strings | 报价方列表  
> validUntil | String | 询价单的过期时间，Unix时间戳的毫秒数格式。  
若所有腿都为期权，则询价单将在10分钟后过期；其他情况，询价单将在2分钟后过期。  
> clRfqId | String | 询价单自定义ID，为客户端敏感信息，不会公开，对报价方返回""。  
> tag | String | RFQ标签，与此RFQ关联的大宗交易将有相同的标签。  
> allowPartialExecution | Boolean | RFQ是否可以被部分执行，如果腿的比例和原RFQ一致。有效值为`true`或`false`。未指定时，默认为`false`。  
> traderCode | String | 询价方唯一标识代码。  
> rfqId | String | 询价单ID  
> legs | Array of objects | 组合交易，每个请求最多可放置15条腿  
>> instId | String | 产品ID，如 "BTC-USDT-SWAP"  
>> tdMode | String | 交易模式   
保证金模式：`cross`全仓 `isolated`逐仓   
非保证金模式：`cash`非保证金.   
如未提供，tdMode 将继承系统设置的默认值：   
合约模式 & 现货: `cash`   
`合约模式`和`跨币种保证金模式`下买入期权： `isolated`   
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
>> acct | String | 账户名  
>> sCode | String | 事件执行结果的code，0代表成功  
>> sMsg | String | 事件执行失败或成功时的msg  
>> legs | Array of objects | 组合交易  
>>> instId | String | 产品ID  
>>> sz | String | 委托数量  
>>> tdMode | String | 交易模式  
>>> ccy | String | 保证金币种  
>>> posSide | String | 持仓方向  
组合询价单功能介绍  
  
1\. 只有母账户能创建组合询价单，可分配的子账户范围为其普通子账户和资管子账户。  
2\. 用户将传入 acctAlloc 请求参数来指示组合询价单的账户分配详情，包括账户名称、产品ID、分配的数量等。母账户也允许参与，并应标识为 "0"。对于 tdMode、ccy 和 posSide 字段，如果留空，则继承系统默认值。  
3\. 新增 groupId，acctAlloc 作为响应参数。  
4\. 分配子账户的上限为 10 个。如果超过上限，将收到错误代码 70516。  
5\. 对于每个交易产品，所有账户中腿数量的总和应等于组合询价单中的总量。如果不相等，将收到错误代码 70514。  
6\. 对于每个子账户，腿数量与组合询价单的比例必须在所有交易产品中保持一致。如果不一致，将收到错误代码 70515。以下是一个示例：  
    1\. 父级询价单腿  
        1\. 产品：BTC-USDT，数量：50；产品：ETH-USDT，数量：100  
    2\. 子级询价单腿，正常情况  
        1\. 账户1：产品：BTC-USDT，数量：30；产品：ETH-USDT，数量：60（比例：0.6）  
        2\. 账户2：产品：BTC-USDT，数量：20；产品：ETH-USDT，数量：40（比例：0.4）  
    3\. 子级询价单腿，异常情况  
        1\. 账户1：产品：BTC-USDT，数量：30；产品：ETH-USDT，数量：50  
        2\. 账户2：产品：BTC-USDT，数量：20；产品：ETH-USDT，数量：50  
        3\. 总数量相等，但不同子账户的比例不一致。  
7\. 对于 allowPartialExecution 字段，即使用户传入，也将被忽略。对于组合询价单，allowPartialExecution 始终为 true，因为任何子账户都有可能执行失败， Taker 无法确定询价单是否可以部分或完全成交。因此，Maker 应将其视为可以部分成交的询价单。  
8\. 若任何子账户执行失败，则不会创建组合询价单。  

### 取消询价单 

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
  
### 批量取消询价单 

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
  
### 取消所有询价单 

取消所有询价单

#### 限速: 2次/2s

#### 限速规则：User ID

#### 权限：交易

#### HTTP Requests

`POST /api/v5/rfq/cancel-all-rfqs`

> 请求示例
    
    
    POST /api/v5/rfq/cancel-all-rfqs
    
    
    
    
    import okx.BlockTrading as BlockTrading
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘：1
    
    blockTradingAPI = BlockTrading.BlockTradingAPI(apikey, secretkey, passphrase, False, flag)
    
    # 取消所有询价单
    result = blockTradingAPI.cancel_all_rfqs()
    print(result)
    
    

#### 请求参数

无

> 返回示例
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "ts":"1697026383085"
            }
        ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
code | String | 结果代码，0 表示成功。  
msg | String | 错误信息，如果代码不为 0，则不为空。  
data | Array of objects | 包含结果的对象数组  
> ts | String | 成功取消时间，Unix时间戳的毫秒数格式，如 1597026383085。  
  
### 执行报价

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

### 获取可报价产品 

用于maker查询特定的接受询价和报价的产品, 以及数量和价格范围。

#### 限速: 5次/2s

#### 限速规则：User ID

#### 权限：读取

#### HTTP Requests

`GET /api/v5/rfq/maker-instrument-settings`

> 请求示例
    
    
    GET /api/v5/rfq/maker-instrument-settings
    

#### 请求参数

无

> 返回示例
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "instType": "OPTION",
                "includeAll": true,
                "data": [
                    {
                        "instFamily": "BTC-USD",
                        "maxBlockSz": "10000",
                        "makerPxBand": "5"
                    },
                    {
                        "instFamily": "SOL-USD",
                        "maxBlockSz": "100000",
                        "makerPxBand": "15"
                    }
                ]
            },
            {
                "instType": "FUTURES",
                "includeAll": false,
                "data": [
                    {
                        "instFamily": "BTC-USD",
                        "maxBlockSz": "10000",
                        "makerPxBand": "5"
                    },
                    {
                        "instFamily": "ETH-USDT",
                        "maxBlockSz": "100000",
                        "makerPxBand": "15"
                    }
                ]
            },
            {
                "instType:": "SWAP",
                "includeAll": false,
                "data": [
                    {
                        "instFamily": "BTC-USD",
                        "maxBlockSz": "10000",
                        "makerPxBand": "5"
                    },
                    {
                        "instFamily": "ETH-USDT"
                    }
                ]
            },
            {
                "instType:": "SPOT",
                "includeAll": false,
                "data": [
                    {
                        "instId": "BTC-USDT"
                    },
                    {
                        "instId": "TRX-USDT"
                    }
                ]
            }
        ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
code | String | 结果代码，`0` 表示成功  
msg | String | 错误信息，如果代码不为`0`，则不为空  
data | Array of objects | 请求返回值，包含请求结果  
> instType | String | 产品类别，枚举值包括`FUTURES`,`OPTION`,`SWAP`和`SPOT`  
> includeAll | Boolean | 是否接收该instType下所有产品。有效值为`true`或`false`。默认`false`。  
> data | Array of objects | instType的元素  
>> instFamily | String | 交易品种  
`交割`/`永续`/`期权`情况下必填  
>> instId | String | 产品ID，如 `BTC-USDT`。对`SPOT`产品类别有效且必须。  
>> maxBlockSz | String | 该种产品最大可交易数量。FUTURES, OPTION and SWAP 的单位是合约数量。SPOT的单位是交易货币。  
>> makerPxBand | String | 价格限制以价格精度tick为单位，以标记价格为基准。  
设置makerPxBand为1个tick代表:   
如果买一价 > 标记价格 + 1 tick, 操作将被拦截   
如果 买一价 < 标记价格 - 1 tick, 操作将被拦截  
  
### 设置可报价产品 

用于maker设置特定的接受询价和报价的产品, 以及数量和价格范围。

#### 限速: 5次/2s

#### 限速规则：User ID

#### 权限：交易

#### HTTP Requests

`POST /api/v5/rfq/maker-instrument-settings`

> 请求示例
    
    
    POST /api/v5/rfq/maker-instrument-settings
    [
        {
         "instType": "OPTION",
         "data":
            [{
                "instFamily": "BTC-USD",
                "maxBlockSz": "10000",
                "makerPxBand": "5"
            },
            {
                "instFamily": "SOL-USD",
                "maxBlockSz": "100000",
                "makerPxBand": "15"
            }]
        },
        {
         "instType": "FUTURES",
         "data":
            [{
                "instFamily": "BTC-USD",
                "maxBlockSz": "10000",
                "makerPxBand": "5"
            },
            {
                "instFamily": "ETH-USDT",
                "maxBlockSz": "100000",
                "makerPxBand": "15"
            }]
        },
        {
         "instType": "SWAP",
         "data":
            [{
                "instFamily": "BTC-USD",
                "maxBlockSz": "10000",
                "makerPxBand": "5"
             },
            {
                "instFamily": "ETH-USDT"
            }]
        },
        {
        "instType": "SPOT",
         "data":
            [{
                "instId": "BTC-USDT"
             },
            {
                "instId": "TRX-USDT"
            }]
        }
    ]
    
    
    
    import okx.BlockTrading as BlockTrading
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘：1
    
    blockTradingAPI = BlockTrading.BlockTradingAPI(apikey, secretkey, passphrase, False, flag)
    
    # 设置可报价产品
    data =[{
        "instType": "OPTION",
        "data": [{
                "uly": "BTC-USD",
                "maxBlockSz": "10000",
                "makerPxBand": "5"
            },
            {
                "uly": "SOL-USD",
                "maxBlockSz": "100000",
                "makerPxBand": "15"
            }
        ]
    }]
    
    result = blockTradingAPI.set_marker_instrument(
        data
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instType | String | 是 | 产品类别，枚举值包括`FUTURES`,`OPTION`,`SWAP`和`SPOT`  
includeAll | Boolean | 否 | 是否接收该instType下所有产品。有效值为`true`或`false`。默认`false`。  
data | Array of objects | 是 | instType的元素  
> instFamily | String | 可选 | 交易品种  
`交割`/`永续`/`期权`情况下必填  
> instId | String | 可选 | 产品ID，如 `BTC-USDT`。对`SPOT`产品类别有效且必须。  
> maxBlockSz | String | 否 | 该种产品最大可交易数量。FUTURES, OPTION and SWAP 的单位是合约数量。SPOT的单位是交易货币。  
> makerPxBand | String | 否 | 价格限制以价格精度tick为单位，以标记价格为基准。  
以设置makerPxBand为1个tick为例:   
如果买价 > 标记价格 + 1 tick, 操作将被拦截   
如果卖价 < 标记价格 - 1 tick, 操作将被拦截  
  
> 返回示例
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "result":true
            }
        ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
code | String | 结果代码，`0` 表示成功  
msg | String | 错误信息，如果代码不为`0`，则不为空  
data | Array of objects | 请求返回值，包含请求结果  
> result | Boolean | 请求结果，枚举值为`true`,`false`  
  
### 重设MMP状态 

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
  
### 设置 MMP 

该接口用于设置 MMP 的配置，仅适用于大宗交易中的maker。

#### 限速：1次/10s

#### 限速规则：User ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/rfq/mmp-config`

> 请求示例
    
    
    POST /api/v5/rfq/mmp-config
    body
    {
        "timeInterval":"5000",
        "frozenInterval":"2000",
        "countLimit": "100"
    }
    
    
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
timeInterval | String | 是 | 时间窗口 (毫秒)。  
"0" 代表不使用 MMP。最大为 600,000。  
frozenInterval | String | 是 | 冻结时间长度 (毫秒)。  
"0" 代表一直冻结，直到调用 "重置 MMP 状态" 接口解冻  
countLimit | String | 是 | 尝试执行次数限制  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "frozenInterval": "2000",
                "countLimit": "100",
                "timeInterval": "5000"
            }
        ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
timeInterval | String | 时间窗口 (毫秒)  
frozenInterval | String | 冻结时间长度 (毫秒)  
countLimit | String | 尝试执行次数限制  
组合询价单介绍  
  
对于 Maker，组合询价单的执行尝试将只计入一次 MMP，无论涉及多少账户分配。 

### 查看 MMP 配置 

该接口用于获取 MMP 的配置信息，仅适用于大宗交易中的maker。

#### 限速：5次/2s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/rfq/mmp-config`

> 请求示例
    
    
    GET /api/v5/rfq/mmp-config
    
    

#### 请求参数

none

> 返回结果
    
    
    {
      "code": "0",
      "data": [
        {
          "frozenInterval": "2000",
          "mmpFrozen": true,
          "mmpFrozenUntil": "1000",
          "countLimit": "10",
          "timeInterval": "5000"
        }
      ],
      "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
timeInterval | String | 时间窗口 (毫秒)。  
"0" 代表不使用 MMP。  
frozenInterval | String | 冻结时间长度 (毫秒)。   
如果为"0"，代表一直冻结，直到调用 "重置 MMP 状态" 接口解冻，且`mmpFrozenUntil`为 ""。  
countLimit | String | 尝试执行次数限制  
mmpFrozen | Boolean | MMP 是否被触发。 `true` 或者 `false`  
mmpFrozenUntil | String | 如果配置了 frozenInterval 且 mmpFrozen = `true`，则为不再触发MMP时的时间窗口（单位为ms），否则为""。  
  
### 报价 

允许询价单指定的报价方进行报价，需要对整个询价单报价，不允许部分报价。

同一询价单（`rfqId`）下同一时间只能有一个有效报价单。针对同一 `rfqId` 提交新的报价单，会自动取消当前已有的有效报价单。

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
  
### 取消报价单 

取消一个报价单。

如果在本次取消请求到达之前，系统已处理了针对同一 `rfqId` 的新建报价单请求，则原报价单将已处于 `canceled` 状态，本请求将返回错误 `70400`。当请求通过不同连接或进程发出时可能发生此情况，因为不同连接间不保证请求的处理顺序。如需确保严格的创建→取消顺序，请在收到创建报价单的响应后，通过同一连接再发出取消请求。

#### 限速: 50次/2s

#### 限速规则：User ID

#### 权限：交易

#### HTTP Requests

`POST /api/v5/rfq/cancel-quote`

> 请求示例
    
    
    POST /api/v5/rfq/cancel-quote
    {
        "quoteId": "007",
        "clQuoteId":"Bond007"
    }
    
    
    
    import okx.BlockTrading as BlockTrading
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘：1
    
    blockTradingAPI = BlockTrading.BlockTradingAPI(apikey, secretkey, passphrase, False, flag)
    
    # 取消报价单
    result = blockTradingAPI.cancel_quote(
        quoteId="007",
        clQuoteId="Bond007"
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
quoteId | String | 可选 | 报价单ID  
clQuoteId | String | 可选 | 报价单自定义ID，字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度要在1-32位之间，当 clRfqId 和 rfqId 都传时，以 rfqId 为准。  
rfqId | String | 否 | 询价单ID  
  
> 返回示例
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "quoteId":"007",
                "clQuoteId":"Bond007",
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
> quoteId | String | 报价单ID  
> clQuoteId | String | 询价单自定义ID  
> sCode | String | 事件执行结果的code，0代表成功  
> sMsg | String | 事件执行失败时的msg  
  
### 批量取消报价单 

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
  
### 取消所有报价单 

取消所有报价单

#### 限速: 2次/2s

#### 限速规则：User ID

#### 权限：交易

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
  
### 倒计时全部撤单 

在倒计时结束后，取消所有报价单。

#### 限速：1次/s

#### 限速规则：User ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/rfq/cancel-all-after`

> 请求示例
    
    
    POST /api/v5/rfq/cancel-all-after
    body
    {
       "timeOut":"60"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
timeOut | String | 是 | 取消报价单的倒计时，单位为秒。  
取值范围为 0, [10, 120]  
0 代表不使用该功能。  
  
> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "triggerTime":"1587971460",
                "ts":"1587971400"
            }
        ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
triggerTime | String | 触发撤单的时间.  
triggerTime=0 代表未使用该功能。  
ts | String | 请求被接收到的时间  
建议用户每一秒调用接口一次。当倒计时全部撤单被触发时，交易引擎将为用户逐一取消报价单，该操作可能持续数秒。该功能起到保护用户的作用，不应作为交易策略使用。 

### 获取询价单信息 

获取用户发出的或收到的询价单信息

#### 限速: 2次/2s

#### 限速规则：User ID

#### 权限：读取

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

### 获取报价单信息 

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
  
### 获取大宗交易信息 

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

### 获取大宗交易所有产品行情信息 

获取最近24小时大宗交易量

#### 限速：20次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/market/block-tickers`

> 请求示例
    
    
    GET /api/v5/market/block-tickers?instType=SWAP
    
    
    
    
    import okx.MarketData as MarketData
    
    flag = "0"  # 实盘:0 , 模拟盘：1
    
    marketDataAPI =  MarketData.MarketAPI(flag=flag)
    
    # 获取大宗交易所有产品行情信息
    result = marketDataAPI.get_block_tickers(
        instType="SPOT"
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instType | String | 是 | 产品类型  
`SPOT`：币币  
`SWAP`：永续合约  
`FUTURES`：交割合约  
`OPTION`：期权  
instFamily | String | 否 | 交易品种  
适用于`交割`/`永续`/`期权`，如 `BTC-USD`  
  
> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
         {
            "instType":"SWAP",
            "instId":"LTC-USD-SWAP",
            "volCcy24h":"2222",
            "vol24h":"2222",
            "ts":"1597026383085"
         },
         {
            "instType":"SWAP",
            "instId":"BTC-USD-SWAP",
            "volCcy24h":"2222",
            "vol24h":"2222",
            "ts":"1597026383085"
        }
      ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
instId | String | 产品ID  
instType | String | 产品类型  
volCcy24h | String | 24小时成交量，以`币`为单位  
如果是`衍生品`合约，数值为交易货币的数量。  
如果是`币币/币币杠杆`，数值为计价货币的数量。  
vol24h | String | 24小时成交量，以`张`为单位  
如果是`衍生品`合约，数值为合约的张数。  
如果是`币币/币币杠杆`，数值为交易货币的数量。  
ts | String | 数据产生时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
  
### 获取大宗交易单个产品行情信息 

获取最近24小时大宗交易量

#### 限速：20次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/market/block-ticker`

> 请求示例
    
    
    GET /api/v5/market/block-ticker?instId=BTC-USD-SWAP
    
    
    
    
    import okx.MarketData as MarketData
    
    flag = "0"  # 实盘:0 , 模拟盘：1
    
    marketDataAPI =  MarketData.MarketAPI(flag=flag)
    
    # 获取大宗交易单个产品行情信息
    result = marketDataAPI.get_block_ticker(
        instId="BTC-USDT"
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instId | String | 是 | 产品ID，如 `BTC-USD-SWAP`  
  
> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
         {
            "instType":"SWAP",
            "instId":"LTC-USD-SWAP",
            "volCcy24h":"2222",
            "vol24h":"2222",
            "ts":"1597026383085"
         }
      ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
instId | String | 产品ID  
instType | String | 产品类型  
volCcy24h | String | 24小时成交量，以`币`为单位  
如果是`衍生品`合约，数值为交易货币的数量。  
如果是`币币/币币杠杆`，数值为计价货币的数量。  
vol24h | String | 24小时成交量，以`张`为单位  
如果是`衍生品`合约，数值为合约的张数。  
如果是`币币/币币杠杆`，数值为交易货币的数量。  
ts | String | 数据产生时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
  
### 获取大宗交易公共多腿成交数据 

获取已经执行的大宗交易。数据将在大宗交易执行15分钟后更新。

#### 限速: 5次/2s

#### 限速规则：IP

#### HTTP Requests

`GET /api/v5/rfq/public-trades`

> 请求示例
    
    
    GET /api/v5/rfq/public-trades
    
    
    
    import okx.BlockTrading as BlockTrading
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘：1
    
    blockTradingAPI = BlockTrading.BlockTradingAPI(apikey, secretkey, passphrase, False, flag)
    
    # 获取大宗交易公共成交数据
    result = blockTradingAPI.get_public_trades()
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
beginId | String | 否 | 请求的起始大宗交易ID，请求此ID之后（更新的数据）的分页内容，不包括 beginId  
endId | String | 否 | 请求的结束大宗交易ID，请求此ID之前（更旧的数据）的分页内容，不包括 endId  
limit | String | 否 | 返回结果的数量，最大为100，默认100条  
  
> 返回示例
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "blockTdId": "439161457415012352",
                "groupId": "",
                "legs": [
                    {
                        "instId": "BTC-USD-210826",
                        "side": "sell",
                        "sz": "100",
                        "px": "11000",
                        "tradeId": "439161457415012354"
                    },
                    {
                        "instId": "BTC-USD-SWAP",
                        "side": "sell",
                        "sz": "100",
                        "px": "50",
                        "tradeId": "439161457415012355"
                    },
                    {
                        "instId": "BTC-USDT",
                        "side": "buy",
                        "sz": "0.1", //for public feed, spot "sz" is in baseccy
                        "px": "10.1",
                        "tradeId": "439161457415012356"
                    },
                    {
                        "instId": "BTC-USD-210326-60000-C",
                        "side": "buy",
                        "sz": "200",
                        "px": "0.008",
                        "tradeId": "439161457415012357"
                    },
                    {
                        "instId": "BTC-USD-220930-5000-P",
                        "side": "sell",
                        "sz": "200",
                        "px": "0.008",
                        "tradeId": "439161457415012360"
                    },
                    {
                        "instId": "BTC-USD-220930-10000-C",
                        "side": "sell",
                        "sz": "200",
                        "px": "0.008",
                        "tradeId": "439161457415012361"
                    },
                    {
                        "instId": "BTC-USD-220930-10000-P",
                        "side": "sell",
                        "sz": "200",
                        "px": "0.008",
                        "tradeId": "439161457415012362"
                    },
                    {
                        "instId": "ETH-USD-220624-100100-C",
                        "side": "sell",
                        "sz": "100",
                        "px": "0.008",
                        "tradeId": "439161457415012363"
                    }
                ],
                "strategy":"CALL_CALENDAR_SPREAD",
                "cTime": "1650976251241"
            }
        ]
    }
    
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
code | String | 结果代码，0 表示成功。  
msg | String | 错误信息，如果代码不为 0，则不为空。  
data | Array of objects | 包含结果的对象数组.  
> strategy | String | 期权策略, 如 `CALL_CALENDAR_SPREAD`  
> cTime | String | 成交时间，Unix时间戳的毫秒数格式。  
> blockTdId | String | 大宗交易ID  
> groupId | String | 组合询价单ID  
只适用于组合询价单，普通询价单返回 ""  
> legs | Array of objects | 组合交易  
>> instId | String | 产品ID  
>> px | String | 成交价格  
>> sz | String | 成交数量  
对于币币交易，成交数量的单位为交易货币  
对于交割、永续以及期权，单位为张。  
>> side | String | 询价单方向，从 Taker的视角看  
>> tradeId | String | 最新成交ID  
组合询价单介绍  
  
1\. 新增返回参数 groupId，协助用户将子账户执行映射到组合询价单。仅适用于组合询价单，对普通询价单返回 ""。  
2\. 该接口返回的交易数据应为父级询价单，而不是子级询价单，与子账户分配无关。blockTdId 及 tradeId 为空。  

### 获取大宗交易公共单腿成交数据 

查询市场上交易产品维度的大宗交易公共成交数据，根据 tradeId 倒序排序。数据将在大宗交易执行15分钟后更新。

#### 限速：20次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/public/block-trades`

> 请求示例
    
    
    GET /api/v5/public/block-trades?instId=BTC-USDT
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instId | String | 是 | 产品ID，如 `BTC-USDT`  
  
> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "fillVol": "5",
                "fwdPx": "26857.86591585",
                "groupId": "",
                "idxPx": "26889.7",
                "instId": "BTC-USD-231013-22000-P",
                "markPx": "0.0000000000000001",
                "px": "0.0026",
                "side": "buy",
                "sz": "1",
                "tradeId": "632960608383700997",
                "ts": "1697181568974"
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
instId | String | 产品ID  
tradeId | String | 成交ID  
px | String | 成交价格  
sz | String | 成交数量  
对于币币交易，成交数量的单位为交易货币  
对于交割、永续以及期权，单位为张。  
side | String | 成交方向   
`buy`：买   
`sell`：卖  
fillVol | String | 成交时的隐含波动率   
仅适用于 `期权`  
fwdPx | String | 成交时的远期价格   
仅适用于 `期权`  
idxPx | String | 成交时的指数价格   
适用于 `交割`, `永续`, `期权`  
markPx | String | 成交时的标记价格   
适用于 `交割`, `永续`, `期权`  
groupId | String | 组合询价单ID  
只适用于组合询价单，普通询价单返回 ""  
ts | String | 成交时间，Unix时间戳的毫秒数格式， 如`1597026383085`  
最多获取最近500条历史公共成交数据  组合询价单介绍  
  
1\. 新增返回参数 groupId，协助用户将子账户执行映射到组合询价单。仅适用于组合询价单，对普通询价单返回 ""。  
2\. 该接口返回的交易数据应为子级询价单，但拆分为单腿，tradeId 有值 

## WebSocket 私有频道 

### 询价频道 

获取用户自身发送或接收的询价信息。每当用户自身发送或接收询价时，数据都将被推送。

#### 服务地址

/ws/v5/business (需要登录)

> 请求示例
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "rfqs"
        }
      ]
    }
    
    
    
    import asyncio
    
    from okx.websocket.WsPrivateAsync import WsPrivateAsync
    
    
    def callbackFunc(message):
        print(message)
    
    async def main():
    
        ws = WsPrivateAsync(
            apiKey = "YOUR_API_KEY",
            passphrase = "YOUR_PASSPHRASE",
            secretKey = "YOUR_SECRET_KEY",
            url = "wss://ws.okx.com:8443/ws/v5/business",
            useServerTime=False
        )
        await ws.start()
        args = [
            {
              "channel": "rfqs"
            }
        ]
    
        await ws.subscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
        await ws.unsubscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
    
    asyncio.run(main())
    

#### 请求参数

参数名 | 类型 | 是否必填 | 描述  
---|---|---|---  
id | String | 否 | 消息的唯一标识。  
用户提供，返回参数中会返回以便于找到相应的请求。  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度必须要在1-32位之间。  
op | String | 是 | 操作  
`subscribe`  
`unsubscribe`  
  
args | Array of objects | 是 | 请求订阅的频道列表  
> channel | String | 是 | 频道名  
`rfqs`  
  
> 成功返回示例 
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
        "channel": "rfqs"
      },
      "connId": "a4d3ae55"
    }
    

> 失败返回示例
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"rfqs\"}]}",
      "connId": "a4d3ae55"
    }
    

#### 返回参数

参数名 | 类型 | 是否必填 | 描述  
---|---|---|---  
id | String | 否 | 消息的唯一标识  
event | String | 是 | 操作  
`subscribe`  
`unsubscribe`  
`error`  
arg | Object | 否 | 订阅的频道  
> channel | String | 是 | 频道名  
`rfqs`  
code | String | 否 | 错误码  
msg | String | 否 | 错误消息  
connId | String | 是 | WebSocket连接ID  
  
> 推送示例
    
    
    {
        "arg":{
            "channel":"rfqs",
            "uid": "77982378738415879"
        },
        "data":[
            {
                "cTime":"1611033737572",
                "uTime":"1611033737572",
                "traderCode":"DSK2",
                "rfqId":"22534",
                "clRfqId":"",
                "tag":"123456",
                "state":"active",
                "flowType": "",
                "validUntil":"1611033857557",
                "allowPartialExecution": false,
                "counterparties":[
                    "DSK4",
                    "DSK5"
                ],
                "legs":[
                    {
                        "instId":"BTCUSD-211208-36000-C",
                        "tdMode":"cross",
                        "ccy":"USDT",
                        "sz":"25.0",
                        "side":"buy",
                        "posSide": "long",
                        "tgtCcy":""
                    },
                    {
                        "instId":"ETHUSD-211208-45000-C",
                        "tdMode":"cross",
                        "ccy":"USDT",
                        "sz":"25.0",
                        "side":"sell",
                        "posSide": "long",
                        "tgtCcy":""
                    }
                ]
            }
        ]
    }
    

#### 推送数据参数

**参数名** | **类型** | **描述**  
---|---|---  
arg | Object | 订阅成功的频道  
> channel | String | 频道名  
> uid | String | 用户标识  
data | Array of objects | 订阅的数据  
> cTime | String | 询价单创建时间，Unix时间戳的毫秒数格式。  
> uTime | String | 询价单状态更新时间，Unix时间戳的毫秒数格式。  
> state | String | 询价单的状态  
有效值有 `active` `canceled` `filled` `expired` `traded_away` `failed`  
`filled` 表示询价单已成功按照做市商的报价成交。  
`traded_away` 仅适用于报价方。同一笔询价单可能对一个报价方显示为 `filled`，而对另一个报价方显示为 `traded_away`。  
示例：询价方创建询价单 → 做市商A报价 pxA，做市商B报价 pxB → pxA 优于 pxB → 询价方执行做市商A的报价 → 做市商A看到 `filled`，做市商B看到 `traded_away`。  
> counterparties | Array of Strings | 报价方列表  
> validUntil | String | 询价单的过期时间，Unix时间戳的毫秒数格式。  
> clRfqId | String | 询价单自定义ID，为客户敏感信息，不会公开，对报价方返回""。  
> tag | String | 询价单标签，与此询价单关联的大宗交易将有相同的标签。  
> flowType | String | 识别询价单的类型。   
仅适用于报价方，返回""给询价方。  
> traderCode | String | 询价方唯一标识代码，询价时 Anonymous 设置为 `True` 时不可见  
> rfqId | String | 询价单ID  
> allowPartialExecution | Boolean | RFQ是否可以被部分执行，如果腿的比例和原RFQ一致。>有效值为`true`或`false`。  
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
>> side | String | 询价单方向  
>> posSide | String | 持仓方向   
买卖模式下默认为`net`。如未指定，则返回""，相当于`net`。   
在开平仓模式下仅可选择`long`或`short`。 如未指定，则返回""，对应于为交易开新仓位的方向（买入=>`long`，卖出=>`short`）。  
仅适用交割、永续。  
>> tgtCcy | String | 委托数量的类型   
定义`sz`属性的单位。仅适用于 instType=`SPOT`。有效值为`base_ccy`和`quote_ccy`。未指定时，默认为`base_ccy`。  
>> tradeQuoteCcy | String | 交易使用的计价币种。仅适用于 SPOT。  
默认值为 instId 的报价币种，例如：对于 `BTC-USD`，默认值为 `USD`.  
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
state: pending_fill 是一个瞬间状态，该频道不会推送。  组合询价单介绍  
  
1\. allowPartialExecution 字段始终为 true，适用于 Taker 和 Maker 的组合询价单。  
2\. 新增返回参数 acctAlloc ，包含所有账户分配信息，但仅适用于 Taker。  
3\. 新增返回参数 groupId，适用于 Taker 和 Maker。  
4\. 对于组合询价单状态  
        1\. 如果任何分配账户处于待执行状态，则状态为 pending_fill  
        2\. 否则，  
                1\. 如果任何分配账户已成交，则状态为 filled  
                2\. 如果所有分配账户均失败，则状态为 failed  

### 报价频道 

获取用户自身发送或接收的报价信息。每当用户自身发送或接收报价时，数据都将被推送。

#### 服务地址

/ws/v5/business (需要登录)

> 请求示例
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "quotes"
        }
      ]
    }
    
    
    
    import asyncio
    
    from okx.websocket.WsPrivateAsync import WsPrivateAsync
    
    
    def callbackFunc(message):
        print(message)
    
    async def main():
    
        ws = WsPrivateAsync(
            apiKey = "YOUR_API_KEY",
            passphrase = "YOUR_PASSPHRASE",
            secretKey = "YOUR_SECRET_KEY",
            url = "wss://ws.okx.com:8443/ws/v5/business",
            useServerTime=False
        )
        await ws.start()
        args = [
            {
              "channel": "quotes"
            }
        ]
    
        await ws.subscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
        await ws.unsubscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
    
    asyncio.run(main())
    
    
    

#### 请求参数

参数名 | 类型 | 是否必填 | 描述  
---|---|---|---  
id | String | 否 | 消息的唯一标识。  
用户提供，返回参数中会返回以便于找到相应的请求。  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度必须要在1-32位之间。  
op | String | 是 | 操作  
`subscribe`  
`unsubscribe`  
  
args | Array of objects | 是 | 请求订阅的频道列表  
> channel | String | 是 | 频道名  
`quotes`  
  
> 成功返回示例
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
        "channel": "quotes"
      },
      "connId": "a4d3ae55"
    }
    

> 失败返回示例
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"quotes\"}]}",
      "connId": "a4d3ae55"
    }
    

#### 返回参数

参数名 | 类型 | 是否必填 | 描述  
---|---|---|---  
id | String | 否 | 消息的唯一标识  
event | String | 是 | 操作  
`subscribe`  
`unsubscribe`  
`error`  
arg | Object | 否 | 订阅的频道  
> channel | String | 是 | 频道名  
`quotes`  
code | String | 否 | 错误码  
msg | String | 否 | 错误消息  
connId | String | 是 | WebSocket连接ID  
  
> 推送示例
    
    
    {
        "arg":{
            "channel":"quotes",
            "uid": "77982378738415879"
        },
        "data":[
            {
                "validUntil":"1608997227854",
                "uTime":"1608267227834",
                "cTime":"1608267227834",
                "legs":[
                    {
                        "px":"0.0023",
                        "sz":"25.0",
                        "instId":"BTC-USD-220114-25000-C",
                        "tdMode":"cross",
                        "ccy":"USDT",
                        "side":"sell",
                        "posSide": "long",
                        "tgtCcy":""
    
                    },
                    {
                        "px":"0.0045",
                        "sz":"25",
                        "instId":"BTC-USD-220114-35000-C",
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
                "traderCode":"SATS",
                "quoteSide":"sell",
                "state":"canceled",
                "reason":"mmp_canceled",
                "clQuoteId":""
            }
        ]
    }
    

#### 推送数据参数

**参数名** | **类型** | **描述**  
---|---|---  
arg | Object | 订阅成功的频道  
> channel | String | 频道名  
> uid | String | 账户ID，账户uid和app上的一致  
data | Array of objects | 订阅的数据  
> cTime | String | 报价单创建时间，Unix时间戳的毫秒数格式。  
> uTime | String | 报价单状态更新时间，Unix时间戳的毫秒数格式。  
> state | String | 报价单的状态  
`active`  
`canceled`  
`filled`  
`expired`  
`failed`  
> reason | String | 状态原因  
`mmp_canceled`  
> validUntil | String | 报价单的过期时间，Unix时间戳的毫秒数格式。  
> rfqId | String | 询价单ID  
> clRfqId | String | 询价单自定义ID，为客户敏感信息，不会公开，对报价方返回""。  
> quoteId | String | 报价单ID  
> clQuoteId | String | 报价单自定义ID，为客户敏感信息，不会公开，对询价方返回""。  
> tag | String | 报价单标签，与此报价单关联的大宗交易将有相同的标签。  
> traderCode | String | 报价方唯一标识代码，报价时 Anonymous 设置为 `True` 时不可见。  
> quoteSide | String | 报价单方向  
`buy`  
`sell`  
当报价单方向为`buy`，对maker来说，执行方向与legs里的方向相同，对taker来说相反。反之同理。  
> legs | Array of objects | 组合交易  
>> instId | String | 产品ID  
>> tdMode | String | 交易模式  
保证金模式 `cross`：全仓 `isolated`：逐仓   
非保证金模式 `cash`：非保证金  
如未提供，tdMode 将继承系统设置的默认值：   
合约模式 & 现货模式: `cash`   
合约模式和跨币种保证金模式下买入期权： `isolated`   
其他情况: `cross`  
>> ccy | String | 保证金币种，仅适用于`合约模式`下的`全仓杠杆`订单   
在其他情况下该参数将被忽略。  
>> sz | String | 委托数量  
>> px | String | 委托价格  
>> side | String | 报价单方向  
>> posSide | String | 持仓方向  
买卖模式下默认为`net`。如未指定，则返回""，相当于`net`。   
在开平仓模式下仅可选择`long`或`short`。 如未指定，则返回""，对应于为交易开新仓位的方向（买入=>`long`，卖出=>`short`）。  
仅适用交割、永续。  
>> tgtCcy | String | 委托数量的类型   
定义`sz`属性的单位。仅适用于 instType=`SPOT`。有效值为`base_ccy`和`quote_ccy`。未指定时，默认为`base_ccy`。  
>> tradeQuoteCcy | String | 交易使用的计价币种。仅适用于 SPOT。  
默认值为 instId 的报价币种，例如：对于 `BTC-USD`，默认值为 `USD`.  
  
### 大宗交易频道 

获取用户自身的大宗交易信息。同一大宗交易中的所有腿都包含在同一更新中。只要用户自身作为交易对手（即询价方或成交的报价方）进行大宗交易，数据都将被推送。状态为 `traded_away` 的报价方将不会收到本频道的推送。

#### 服务地址

/ws/v5/business (需要登录)

> 请求示例
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "struc-block-trades"
        }
      ]
    }
    
    
    
    import asyncio
    
    from okx.websocket.WsPrivateAsync import WsPrivateAsync
    
    
    def callbackFunc(message):
        print(message)
    
    async def main():
    
        ws = WsPrivateAsync(
            apiKey = "YOUR_API_KEY",
            passphrase = "YOUR_PASSPHRASE",
            secretKey = "YOUR_SECRET_KEY",
            url = "wss://ws.okx.com:8443/ws/v5/business",
            useServerTime=False
        )
        await ws.start()
        args = [
            {
              "channel": "struc-block-trades"
            }
        ]
    
        await ws.subscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
        await ws.unsubscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
    
    asyncio.run(main())
    
    
    

#### 请求参数

参数名 | 类型 | 是否必填 | 描述  
---|---|---|---  
id | String | 否 | 消息的唯一标识。  
用户提供，返回参数中会返回以便于找到相应的请求。  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度必须要在1-32位之间。  
op | String | 是 | 操作  
`subscribe`  
`unsubscribe`  
  
args | Array of objects | 是 | 请求订阅的频道列表  
> channel | String | 是 | 频道名  
`struc-block-trades`  
  
> 成功返回示例
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
        "channel": "struc-block-trades"
      },
      "connId": "a4d3ae55"
    }
    

> 失败返回示例
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"struc-block-trades\"}]}",
      "connId": "a4d3ae55"
    }
    

#### 返回参数

参数名 | 类型 | 是否必填 | 描述  
---|---|---|---  
id | String | 否 | 消息的唯一标识  
event | String | 是 | 操作  
`subscribe`  
`unsubscribe`  
`error`  
arg | Object | 否 | 订阅的频道  
> channel | String | 是 | 频道名  
`struc-block-trades`  
code | String | 否 | 错误码  
msg | String | 否 | 错误消息  
connId | String | 是 | WebSocket连接ID  
  
> 推送示例
    
    
    {
        "arg":{
            "channel":"struc-block-trades",
            "uid": "77982378738415879"
        },
        "data":[
            {
                "cTime":"1608267227834",
                "rfqId":"18753",
                "clRfqId":"",
                "quoteId":"25092",
                "clQuoteId":"",
                "blockTdId":"180184",
                "tag":"123456",
                "tTraderCode":"ANAND",
                "mTraderCode":"WAGMI",
                "isSuccessful": true,
                "errorCode": "",
                "legs":[
                    {
                        "px":"0.0023",
                        "sz":"25.0",
                        "instId":"BTC-USD-20220630-60000-C",
                        "side":"sell",
                        "fee":"0.1001",
                        "feeCcy":"BTC",
                        "tradeId":"10211",
                        "tgtCcy":""
    
                    },
                    {
                        "px":"0.0033",
                        "sz":"25",
                        "instId":"BTC-USD-20220630-50000-C",
                        "side":"buy",
                        "fee":"0.1001",
                        "feeCcy":"BTC",
                        "tradeId":"10212",
                        "tgtCcy":""
    
                    }
                ]
            }
        ]
    }
    

#### 推送数据参数

**参数名** | **类型** | **描述**  
---|---|---  
arg | Object | 订阅成功的频道  
> channel | String | 频道名  
> uid | String | 用户标识  
data | Array of objects | 订阅的数据  
> cTime | String | 执行创建的时间戳，Unix 时间戳格式，以毫秒为单位。  
> rfqId | String | RFQ ID.  
> clRfqId | String | 由用户设置的 RFQ ID。 此属性被视为客户端敏感信息。 不会暴露给 Maker，只返回空字符串“”给 Maker。  
> quoteId | String | Quote ID.  
> clQuoteId | String | 由用户设置的 Quote ID。 此属性被视为客户端敏感信息。 不会暴露给 Taker，只为 Taker 返回空字符串“”。  
> blockTdId | String | 大宗交易ID  
> tag | String | 交易标签，大宗交易将有与其对应的询价单或报价单相同的标签。  
> tTraderCode | String | 报价方唯一标识代码。询价时 Anonymous 设置为 `True` 时不可见。  
> mTraderCode | String | 询价方唯一标识代码。报价时 Anonymous 设置为 `True` 时不可见。  
> isSuccessful | Boolean | 交易是否成功  
> errorCode | String | 未成功交易的错误码。  
对于成功交易为 ""。  
> legs | Array of objects | 组合交易  
>> instId | String | 产品ID  
>> px | String | 成交价格  
>> sz | String | 成交数量  
>> side | String | 询价单方向  
>> tgtCcy | String | 委托数量的类型   
定义`sz`属性的单位。仅适用于 instType=`SPOT`。有效值为`base_ccy`和`quote_ccy`。未指定时，默认为`base_ccy`。  
>> fee | String | 手续费，正数代表平台返佣 ，负数代表平台扣除。  
>> feeCcy | String | 手续费币种  
>> tradeId | String | 最新成交Id  
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
  
1\. 该频道返回的数据应为父级询价单级别，而不是子级询价单执行级别。  
2\. 对于账户分配，包含所有已成交和未成交的子级询价单，但添加 errorCode 来指示子级询价单是否已成交。  
3\. 交易结果将仅返回给组合询价单 Taker 及 Maker。分配的子账户和资管账户将无法看到交易结果。分配的账户应通过交易账单获取这些交易。  
4\. 交易数据仅在所有子级询价单执行后返回。  
5\. 对于父级询价单的 isSuccessful 字段，  
        1\. 如果任何子级询价单已成交，则返回 true  
        2\. 否则，如果所有子级询价单均失败，则返回 false  
6\. 父级询价单的 blockTdId 或 legs 的 tradeId 将为空。但将提供账户分配的详细信息，并附带 blockTdId 以及 tradeId。  

## WebSocket 公共频道 

### 公共大宗交易频道 

获取欧易的最新大宗交易信息。同一大宗交易中的所有腿都包含在同一更新中。数据将在大宗交易执行15分钟后被推送。

#### URL Path

/ws/v5/business

> 请求示例
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "public-struc-block-trades"
        }
      ]
    }
    
    
    
    import asyncio
    from okx.websocket.WsPublicAsync import WsPublicAsync
    
    def callbackFunc(message):
        print(message)
    
    async def main():
        ws = WsPublicAsync(url="wss://wspap.okx.com:8443/ws/v5/business")
        await ws.start()
        args = [
            {
              "channel": "public-struc-block-trades"
            }
        ]
    
        await ws.subscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
        await ws.unsubscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
    asyncio.run(main())
    

#### 请求参数

参数名 | 类型 | 是否必填 | 描述  
---|---|---|---  
id | String | 否 | 消息的唯一标识。  
用户提供，返回参数中会返回以便于找到相应的请求。  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度必须要在1-32位之间。  
op | String | 是 | 操作  
`subscribe`  
`unsubscribe`  
  
args | Array of objects | 是 | 请求订阅的频道列表  
> channel | String | 是 | 频道名  
`public-struc-block-trades`  
  
> 成功返回示例
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
        "channel": "public-struc-block-trades"
      },
      "connId": "a4d3ae55"
    }
    

> 失败返回示例
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"public-struc-block-trades\""}]}",
      "connId": "a4d3ae55"
    }
    

#### 返回参数

参数名 | 类型 | 是否必填 | 描述  
---|---|---|---  
id | String | 否 | 消息的唯一标识  
event | String | 是 | 操作  
`subscribe`  
`unsubscribe`  
`error`  
arg | Object | 否 | 订阅的频道  
> channel | String | 是 | 频道名  
`public-struc-block-trades`  
code | String | 否 | 错误码  
msg | String | 否 | 错误消息  
connId | String | 是 | WebSocket连接ID  
  
> 推送示例
    
    
    {
        "arg":{
            "channel":"public-struc-block-trades"
        },
        "data":[
            {
    
                "cTime":"1608267227834",
                "blockTdId":"1802896",
                "groupId":"",
                "legs":[
                    {
                        "px":"0.323",
                        "sz":"25.0",
                        "instId":"BTC-USD-20220114-13250-C",
                        "side":"sell",
                        "tradeId":"15102"
                    },
                    {
                        "px":"0.666",
                        "sz":"25",
                        "instId":"BTC-USD-20220114-21125-C",
                        "side":"buy",
                        "tradeId":"15103"
                    }
                ]
            }
        ]
    }
    

#### 推送数据参数

**参数名** | **类型** | **描述**  
---|---|---  
arg | Object | 订阅成功的频道  
> channel | String | 频道名  
data | Array of objects | 订阅的数据  
> cTime | String | 执行创建的时间戳，Unix 时间戳格式，以毫秒为单位。  
> blockTdId | String | 大宗交易ID  
> groupId | String | 组合询价单ID  
只适用于组合询价单，普通询价单返回 ""  
> legs | Array of objects | 组合交易  
>> instId | String | 产品名Id  
>> px | String | 成交价格  
>> sz | String | 成交数量  
对于币币交易，成交数量的单位为交易货币  
对于交割、永续以及期权，单位为张。  
>> side | String | 询价单方向，从 Taker的视角看  
>> tradeId | String | 最新成交Id  
组合询价单介绍  
  
1\. 新增返回参数 groupId，协助用户将子账户执行映射到组合询价单。仅适用于组合询价单，对普通询价单返回 ""。  
2\. 该接口返回的交易数据应为父级询价单，而不是子级询价单，与子账户分配无关，blockTdId 及 tradeId 为空  blockTdId 与 rfqId 的对应关系  
  
对于普通询价单，每个 `blockTdId` 与一个 `rfqId` 一一对应。对于组合询价单，一个 `rfqId` 可能对应多个 `blockTdId`。  
  
本频道不直接返回 `rfqId`。作为交易对手方（询价方或成交的报价方）的用户，可订阅私有[大宗交易频道](/docs-v5/zh/#block-trading-websocket-private-channel-structure-block-trades-channel)，该频道同时包含 `rfqId` 和 `blockTdId`，可用于两个频道之间的关联查询。 

### 公共大宗交易单腿交易频道 

获取欧易的最新大宗交易单腿交易信息。大宗交易中的每条腿都在单独的更新中推送。数据将在大宗交易执行15分钟后被推送。

#### URL Path

/ws/v5/business

> 请求示例
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "public-block-trades",
          "instId": "BTC-USDT-SWAP"
        }
      ]
    }
    
    
    
    import asyncio
    from okx.websocket.WsPublicAsync import WsPublicAsync
    
    def callbackFunc(message):
        print(message)
    
    async def main():
        ws = WsPublicAsync(url="wss://wspap.okx.com:8443/ws/v5/business")
        await ws.start()
        args = [
            {
              "channel": "public-block-trades",
              "instId": "BTC-USDT-SWAP"
            }
        ]
    
        await ws.subscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
        await ws.unsubscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
    asyncio.run(main())
    

#### 请求参数

参数名 | 类型 | 是否必填 | 描述  
---|---|---|---  
id | String | 否 | 消息的唯一标识。  
用户提供，返回参数中会返回以便于找到相应的请求。  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度必须要在1-32位之间。  
op | String | 是 | 操作  
`subscribe`  
`unsubscribe`  
  
args | Array of objects | 是 | 请求订阅的频道列表  
> channel | String | 是 | 频道名  
`public-block-trades`  
> instId | String | 是 | 产品 ID, 如 `BTC-USDT-SWAP`  
  
> 成功返回示例
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
        "channel": "public-block-trades",
        "instId": "BTC-USDT-SWAP"
      },
      "connId": "a4d3ae55"
    }
    

> 失败返回示例
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"args\":[{ \"channel\" : \"public-block-trades\""}]}",
      "connId": "a4d3ae55"
    }
    

#### 返回参数

参数名 | 类型 | 是否必需 | 描述  
---|---|---|---  
id | String | 否 | 消息的唯一标识  
event | String | 是 | 操作  
`subscribe`  
`unsubscribe`  
`error`  
arg | Object | 否 | 订阅的频道  
> channel | String | 是 | 频道名  
`public-block-trades`  
> instId | String | 是 | 产品 ID, 如 `BTC-USDT-SWAP`  
code | String | 否 | 错误码  
msg | String | 否 | 错误消息  
connId | String | 是 | WebSocket连接ID  
  
> 推送示例
    
    
    {
       "arg":{
          "channel":"public-block-trades",
          "instId":"BTC-USD-231020-5000-P"
       },
       "data":[
          {
             "fillVol":"5",
             "fwdPx":"26808.16",
             "groupId":"",
             "idxPx":"27222.5",
             "instId":"BTC-USD-231020-5000-P",
             "markPx":"0.0022406326071111",
             "px":"0.0048",
             "side":"buy",
             "sz":"1",
             "tradeId":"633971452580106242",
             "ts":"1697422572972"
          }
       ]
    }
    

#### 推送数据参数

**参数名** | **类型** | **描述**  
---|---|---  
arg | Object | 订阅成功的频道  
> channel | String | 频道名  
> instId | String | 产品 ID, 如 `BTC-USDT-SWAP`  
data | Array of objects | 公共大宗交易单腿交易信息  
> instId | String | 产品 ID, 如 `BTC-USDT-SWAP`  
> tradeId | String | 交易 ID, 由柜台提供.  
> px | String | 该单腿交易价格.  
> sz | String | 成交数量  
对于币币交易，成交数量的单位为交易货币  
对于交割、永续以及期权，单位为张。  
> side | String | 交易方向, buy, sell, 从taker角度看.  
> fillVol | String | 成交时的隐含波动率   
仅适用于 `期权`  
> fwdPx | String | 成交时的远期价格   
仅适用于 `期权`  
> idxPx | String | 成交时的指数价格   
适用于 `交割`, `永续`, `期权`  
> markPx | String | 成交时的标记价格   
适用于 `交割`, `永续`, `期权`  
> groupId | String | 组合询价单ID  
只适用于组合询价单，普通询价单返回 ""  
> ts | String | 成交时间, 时间戳格式，以毫秒为单位. 如 1597026383085.  
组合询价单介绍  
  
1\. 新增返回参数 groupId，协助用户将子账户执行映射到组合询价单。仅适用于组合询价单，对普通询价单返回 ""。  
2\. 该接口返回的交易数据应为子级询价单，但拆分为单腿，tradeId 有值。  

### 大宗交易行情频道 

获取最近24小时大宗交易量  

当发生成交事件时触发推送，此外，也会根据订阅维度每隔5分钟推送一次

#### 服务地址

/ws/v5/business

> 请求示例
    
    
    {
        "id": "1512",
        "op": "subscribe",
        "args": [{
            "channel": "block-tickers",
            "instId": "BTC-USDT"
        }]
    }
    
    
    
    import asyncio
    from okx.websocket.WsPublicAsync import WsPublicAsync
    
    def callbackFunc(message):
        print(message)
    
    async def main():
        ws = WsPublicAsync(url="wss://wspap.okx.com:8443/ws/v5/business")
        await ws.start()
        args = [{
            "channel": "block-tickers",
            "instId": "BTC-USDT"
        }]
    
        await ws.subscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
        await ws.unsubscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
    asyncio.run(main())
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
id | String | 否 | 消息的唯一标识。  
用户提供，返回参数中会返回以便于找到相应的请求。  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度必须要在1-32位之间。  
op | String | 是 | 操作  
`subscribe`  
`unsubscribe`  
args | Array of objects | 是 | 请求订阅的频道列表  
> channel | String | 是 | 频道名  
`block-tickers`  
> instId | String | 是 | 产品ID  
  
> 成功返回示例
    
    
    {
        "id": "1512",
        "event": "subscribe",
        "arg": {
            "channel": "block-tickers",
            "instId": "LTC-USD-200327"
        },
        "connId": "a4d3ae55"
    }
    

> 失败返回示例
    
    
    {
        "id": "1512",
        "event": "error",
        "code": "60012",
        "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"block-tickers\", \"instId\" : \"LTC-USD-200327\"}]}",
        "connId": "a4d3ae55"
    }
    

#### 返回参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
id | String | 否 | 消息的唯一标识  
event | String | 是 | 事件  
`subscribe`  
`unsubscribe`  
`error`  
arg | Object | 否 | 订阅的频道  
> channel | String | 是 | 频道名 `block-tickers`  
> instId | String | 是 | 产品ID  
code | String | 否 | 错误码  
msg | String | 否 | 错误消息  
connId | String | 是 | WebSocket连接ID  
  
> 推送示例
    
    
    {
        "arg": {
            "channel": "block-tickers"
        },
        "data": [
            {
                "instType": "SWAP",
                "instId": "LTC-USD-SWAP",
                "volCcy24h": "0",
                "vol24h": "0",
                "ts": "1597026383085"
            }
        ]
    }
    

#### 推送数据参数

**参数名** | **类型** | **描述**  
---|---|---  
arg | Object | 订阅成功的频道  
> channel | String | 频道名  
> instId | String | 产品ID  
data | Array of objects | 订阅的数据  
> instId | String | 产品ID  
> instType | String | 产品类型  
> volCcy24h | String | 24小时成交量，以`币`为单位  
如果是`衍生品`合约，数值为交易货币的数量。  
如果是`币币/币币杠杆`，数值为计价货币的数量。  
> vol24h | String | 24小时成交量，以`张`为单位  
如果是`衍生品`合约，数值为合约的张数。  
如果是`币币/币币杠杆`，数值为交易货币的数量。  
> ts | String | 数据产生时间，Unix时间戳的毫秒数格式，如 `1597026383085`