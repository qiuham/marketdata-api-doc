---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-trade-get-one-click-repay-history
anchor_id: order-book-trading-trade-get-one-click-repay-history
api_type: API
updated_at: 2026-07-20 19:35:32.423215
---

# GET / One-click repay history

Get the history and status of one-click repay trades in the past 7 days. Only applicable to `Multi-currency margin`/`Portfolio margin`.  
  
#### Rate Limit: 1 request per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/trade/one-click-repay-history`

> Request Example
    
    
    GET /api/v5/trade/one-click-repay-history
    
    
    
    import okx.Trade as Trade
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading: 0, Demo trading: 1
    
    tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)
    
    # Get the history of one-click repay trades
    result = tradeAPI.oneclick_repay_history()
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
after | String | No | Pagination of data to return records earlier than the requested time, Unix timestamp format in milliseconds, e.g. 1597026383085  
before | String | No | Pagination of data to return records newer than the requested time, Unix timestamp format in milliseconds, e.g. 1597026383085  
limit | String | No | Number of results per request. The maximum is 100. The default is 100.  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "debtCcy": "USDC",
                "fillDebtSz": "6950.4865447900000000",
                "fillRepaySz": "4.3067975995094930",
                "repayCcy": "ETH",
                "status": "filled",
                "uTime": "1661256148746"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
debtCcy | String | Debt currency type  
fillDebtSz | String | Amount of debt currency transacted  
repayCcy | String | Repay currency type  
fillRepaySz | String | Amount of repay currency transacted  
status | String | Current status of one-click repay   
`running`: Running   
`filled`: Filled   
`failed`: Failed  
uTime | String | Trade time, Unix timestamp format in milliseconds, e.g. 1597026383085

---

# GET / 获取一键还债历史记录

查询一键还债近7天的历史记录与进度状态。仅适用于`跨币种保证金模式`/`组合保证金模式`。  
  
#### 限速：1次/2s

#### 限速规则：User ID

#### HTTP 请求

`GET /api/v5/trade/one-click-repay-history`

> 请求示例
    
    
    GET /api/v5/trade/one-click-repay-history
    
    
    
    import okx.Trade as Trade
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘: 0, 模拟盘: 1
    
    tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)
    
    # 获取一键还债历史记录
    result = tradeAPI.oneclick_repay_history()
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
after | String | 否 | 查询在此之前的内容，值为时间戳，Unix时间戳为毫秒数格式，如`1597026383085`  
before | String | 否 | 查询在此之后的内容，值为时间戳，Unix时间戳为毫秒数格式，如`1597026383085`  
limit | String | 否 | 返回的结果集数量，默认为100，最大为100  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "debtCcy": "USDC",
                "fillDebtSz": "6950.4865447900000000",
                "fillRepaySz": "4.3067975995094930",
                "repayCcy": "ETH",
                "status": "filled",
                "uTime": "1661256148746"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
debtCcy | String | 负债币种  
fillDebtSz | String | 对应的负债币种成交数量  
repayCcy | String | 偿还币种  
fillRepaySz | String | 偿还币种实际支付数量  
status | String | 当前还债进度/状态   
`running`: 进行中   
`filled`: 已完成   
`failed`: 失败  
uTime | String | 交易时间戳，Unix时间戳为毫秒数格式，如 1597026383085