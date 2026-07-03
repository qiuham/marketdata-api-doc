---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#spread-trading-rest-api-get-trades-last-7-days
anchor_id: spread-trading-rest-api-get-trades-last-7-days
api_type: REST
updated_at: 2026-07-03 19:40:19.373121
---

# Get trades (last 7 days)

Retrieve historical transaction details **for the last 7 days**. Results are returned in counter chronological order.  
  
#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/sprd/trades`

> Request Example
    
    
    GET /api/v5/sprd/trades
    
    
    
    import okx.SpreadTrading as SpreadTrading
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading:0 , demo trading:1
    
    spreadAPI = SpreadTrading.SpreadTradingAPI(apikey, secretkey, passphrase, False, flag)
    
    # get private trades
    result = spreadAPI.get_trades()
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
sprdId | String | No | spread ID, e.g.  
tradeId | String | No | Trade ID  
ordId | String | No | Order ID  
beginId | String | No | Start trade ID the request to begin with. Pagination of data to return records newer than the requested tradeId, not including beginId  
endId | String | No | End trade ID the request to end with. Pagination of data to return records earlier than the requested tradeId, not including endId  
begin | String | No | Filter with a begin timestamp. Unix timestamp format in milliseconds, e.g. `1597026383085`  
end | String | No | Filter with an end timestamp. Unix timestamp format in milliseconds, e.g. `1597026383085`  
limit | String | No | Number of results per request. The maximum is 100. The default is 100  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "sprdId": "BTC-USDT-SWAP_BTC-USDT-200329",
                "tradeId": "123",
                "ordId": "123445",
                "clOrdId": "b16",
                "tag": "",
                "fillPx": "999",
                "fillSz": "3",
                "state": "filled",
                "side": "buy",
                "execType": "M",
                "ts": "1597026383085",
                "legs": [
                    {
                        "instId": "BTC-USDT-SWAP",
                        "px": "20000",
                        "sz": "3",
                        "szCont": "0.03",
                        "side": "buy",
                        "fillPnl": "",
                        "fee": "",
                        "feeCcy": "",
                        "tradeId": "1232342342"
                    },
                    {
                        "instId": "BTC-USDT-200329",
                        "px": "21000",
                        "sz": "3",
                        "szCont": "0.03",
                        "side": "sell",
                        "fillPnl": "",
                        "fee": "",
                        "feeCcy": "",
                        "tradeId": "5345646634"
                    }
                ],
                "code": "",
                "msg": ""
            }
        ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
sprdId | String | spread ID  
tradeId | String | Trade ID  
ordId | String | Order ID  
clOrdId | String | Client Order ID as assigned by the client  
tag | String | Order tag  
fillPx | String | Filled price  
fillSz | String | Filled quantity  
side | String | Order side, `buy` `sell`  
state | String | Trade state.   
Valid values are `filled` and `rejected`  
execType | String | Liquidity taker or maker, `T`: taker `M`: maker  
ts | String | Data generation time, Unix timestamp format in milliseconds, e.g. `1597026383085`.  
legs | Array of objects | Legs of trade  
> instId | String | Instrument ID, e.g. BTC-USDT-SWAP  
> px | String | The price the leg executed  
> sz | String | The size of each leg  
> szCont | String | Filled amount of the contract   
Only applicable to contracts, return "" for spot  
> side | String | The direction of the leg. Valid value can be `buy` or `sell`.  
> fillPnl | String | Last filled profit and loss, applicable to orders which have a trade and aim to close position. It always is 0 in other conditions  
> fee | String | Fee. Negative number represents the user transaction fee charged by the platform. Positive number represents rebate.  
> feeCcy | String | Fee currency  
> tradeId | String | Traded ID in the OKX orderbook.  
code | String | Error Code, the default is 0  
msg | String | Error Message, the default is ""

---

# 获取历史成交数据（近七天）

获取近7天的订单成交明细信息. 结果按时间倒序返回。  
  
#### 限速：20次/2s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/sprd/trades`

> 请求示例
    
    
    GET /api/v5/sprd/trades
    
    
    
    
    import okx.SpreadTrading as SpreadTrading
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘:1
    
    spreadAPI = SpreadTrading.SpreadTradingAPI(apikey, secretkey, passphrase, False, flag)
    
    # 获取私有交易
    result = spreadAPI.get_trades()
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
sprdId | String | 否 | spread ID，如BTC-USDT_BTC-USDT-SWAP  
tradeId | String | 否 | 交易 ID  
ordId | String | 否 | 订单 ID  
beginId | String | 否 | 请求的起始交易ID，请求此ID之后（更新的数据）的分页内容，不包括 beginId  
endId | String | 否 | 请求的结束交易ID，请求此ID之前（更旧的数据）的分页内容，不包括 endId  
begin | String | 否 | 筛选的开始时间戳，Unix 时间戳为毫秒数格式，如 `1597026383085`  
end | String | 否 | 筛选的结束时间戳，Unix 时间戳为毫秒数格式，如 `1597027383085`  
limit | String | 否 | 返回结果的数量，最大为100，默认100条  
  
> 返回示例
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "sprdId": "BTC-USDT-SWAP_BTC-USDT-200329",
                "tradeId": "123",
                "ordId": "123445",
                "clOrdId": "b16",
                "tag": "",
                "fillPx": "999",
                "fillSz": "3",
                "state": "filled",
                "side": "buy",
                "execType": "M",
                "ts": "1597026383085",
                "legs": [
                    {
                        "instId": "BTC-USDT-SWAP",
                        "px": "20000",
                        "sz": "3",
                        "szCont": "0.03",
                        "side": "buy",
                        "fillPnl": "",
                        "fee": "",
                        "feeCcy": "",
                        "tradeId": "1232342342"
                    },
                    {
                        "instId": "BTC-USDT-200329",
                        "px": "21000",
                        "sz": "3",
                        "szCont": "0.03",
                        "side": "sell",
                        "fillpnl": "",
                        "fee": "",
                        "feeCcy": "",
                        "tradeId": "5345646634"
                    }
                ],
                "code": "",
                "msg": ""
            }
        ]
    }
    
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
sprdId | String | spread ID，如BTC-USDT_BTC-USDT-SWAP  
tradeId | String | 交易ID  
ordId | String | 订单ID  
clOrdId | String | 客户自定义订单ID  
tag | String | 订单标签  
fillPx | String | 成交价格  
fillSz | String | 成交数量  
side | String | 交易方向   
`buy`：买   
`sell`：卖  
state | String | 交易状态   
`filled`：已成交   
`rejected`：被拒绝  
execType | String | 流动性方向 `T`：taker `M`：maker  
ts | String | 成交明细产生时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
legs | Array of objects | 交易的腿  
> instId | String | 产品 ID  
> px | String | 价格  
> sz | String | 数量  
> szCont | String | 成交合约数量   
仅适用于合约，现货将返回""  
> side | String | 交易方向 `buy`：买 `sell`：卖  
> fillPnl | String | 最新成交收益，适用于有成交的平仓订单。其他情况均为0。  
> fee | String | 手续费金额或者返佣金额，手续费扣除为‘负数’，如-0.01；手续费返佣为‘正数’，如 0.01  
> feeCcy | String | 交易手续费币种或者返佣金币种  
> tradeId | String | 交易ID  
code | String | 错误码，默认0  
msg | String | 错误提示，默认 ""