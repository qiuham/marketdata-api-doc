---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#block-trading-rest-api-get-public-multi-leg-transactions-of-block-trades
anchor_id: block-trading-rest-api-get-public-multi-leg-transactions-of-block-trades
api_type: REST
updated_at: 2026-07-16 19:20:44.253924
---

# Get public multi-leg transactions of block trades

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

---

# 获取大宗交易公共多腿成交数据

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