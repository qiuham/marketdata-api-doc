---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-trade-get-easy-convert-history
anchor_id: order-book-trading-trade-get-easy-convert-history
api_type: API
updated_at: 2026-07-16 19:19:45.527324
---

# GET / Easy convert history

Get the history and status of easy convert trades in the past 7 days.  
  
#### Rate Limit: 1 request per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/trade/easy-convert-history`

> Request Example
    
    
    GET /api/v5/trade/easy-convert-history
    
    
    
    import okx.Trade as Trade
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading: 0, Demo trading: 1
    
    tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)
    
    # Get the history of easy convert trades
    result = tradeAPI.get_easy_convert_history()
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
after | String | No | Pagination of data to return records earlier than the requested time (exclude), Unix timestamp format in milliseconds, e.g. `1597026383085`  
before | String | No | Pagination of data to return records newer than the requested time (exclude), Unix timestamp format in milliseconds, e.g. `1597026383085`  
limit | String | No | Number of results per request. The maximum is 100. The default is 100.  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "fillFromSz": "0.1761712511667539",
                "fillToSz": "6.7342205900000000",
                "fromCcy": "OKB",
                "status": "filled",
                "toCcy": "ADA",
                "acct": "18",
                "uTime": "1661313307979"
            },
            {
                "fillFromSz": "0.1722106121112177",
                "fillToSz": "2.9971018300000000",
                "fromCcy": "OKB",
                "status": "filled",
                "toCcy": "USDC",
                "acct": "18",
                "uTime": "1661313307979"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
fromCcy | String | Type of small payment currency convert from  
fillFromSz | String | Amount of small payment currency convert from  
toCcy | String | Type of mainstream currency convert to  
fillToSz | String | Amount of mainstream currency convert to  
acct | String | The account where the mainstream currency is located  
`6`: Funding account   
`18`: Trading account  
status | String | Current status of easy convert   
`running`: Running   
`filled`: Filled   
`failed`: Failed  
uTime | String | Trade time, Unix timestamp format in milliseconds, e.g. `1597026383085`

---

# GET / 获取一键兑换主流币历史记录

查询一键兑换主流币过去7天内的历史记录与进度状态。  
  
#### 限速：1次/2s

#### 限速规则：User ID

#### HTTP 请求

`GET /api/v5/trade/easy-convert-history`

> 请求示例
    
    
    GET /api/v5/trade/easy-convert-history
    
    
    
    import okx.Trade as Trade
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘: 0, 模拟盘: 1
    
    tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)
    
    # 获取一键兑换主流币历史记录
    result = tradeAPI.get_easy_convert_history()
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
after | String | 否 | 查询在此之前(不包含)的内容，值为时间戳，Unix时间戳为毫秒数格式，如`1597026383085`  
before | String | 否 | 查询在此之后(不包含)的内容，值为时间戳，Unix时间戳为毫秒数格式，如`1597026383085`  
limit | String | 否 | 返回的结果集数量，默认为100，最大为100  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "fillFromSz": "0.1761712511667539",
                "fillToSz": "6.7342205900000000",
                "fromCcy": "OKB",
                "status": "filled",
                "toCcy": "ADA",
                "acct": "18",
                "uTime": "1661313307979"
            },
            {
                "fillFromSz": "0.1722106121112177",
                "fillToSz": "2.9971018300000000",
                "fromCcy": "OKB",
                "status": "filled",
                "toCcy": "USDC",
                "acct": "18",
                "uTime": "1661313307979"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
fromCcy | String | 小币支付币种  
fillFromSz | String | 对应的小币支付数量  
toCcy | String | 兑换到的主流币  
fillToSz | String | 兑换到的主流币数量  
acct | String | 兑换到的主流币所在的账户  
`6`：资金账户   
`18`：交易账户  
status | String | 当前兑换进度/状态   
`running`: 进行中   
`filled`: 已完成   
`failed`: 失败  
uTime | String | 交易时间戳，Unix时间戳为毫秒数格式，如 1597026383085