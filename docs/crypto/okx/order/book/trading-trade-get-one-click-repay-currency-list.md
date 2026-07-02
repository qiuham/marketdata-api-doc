---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-trade-get-one-click-repay-currency-list
anchor_id: order-book-trading-trade-get-one-click-repay-currency-list
api_type: API
updated_at: 2026-07-02 19:43:13.340709
---

# GET / One-click repay currency list

Get list of debt currency data and repay currencies. Debt currencies include both cross and isolated debts. Only applicable to `Multi-currency margin`/`Portfolio margin`.  
  
#### Rate Limit: 1 request per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/trade/one-click-repay-currency-list`

> Request Example
    
    
    GET /api/v5/trade/one-click-repay-currency-list
    
    
    
    import okx.Trade as Trade
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading: 0, Demo trading: 1
    
    tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)
    
    # Get list of debt currency data and repay currencies
    result = tradeAPI.get_oneclick_repay_list()
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
debtType | String | No | Debt type   
`cross`: cross   
`isolated`: isolated  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "debtData": [
                    {
                        "debtAmt": "29.653478",
                        "debtCcy": "LTC"
                    },
                    {
                        "debtAmt": "237803.6828295906051002",
                        "debtCcy": "USDT"
                    }
                ],
                "debtType": "cross",
                "repayData": [
                    {
                        "repayAmt": "0.4978335419825104",
                        "repayCcy": "ETH"
                    }
                ]
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
debtData | Array of objects | Debt currency data list  
> debtCcy | String | Debt currency  
> debtAmt | String | Debt currency amount   
Including principal and interest  
debtType | String | Debt type   
`cross`: cross   
`isolated`: isolated  
repayData | Array of objects | Repay currency data list  
> repayCcy | String | Repay currency  
> repayAmt | String | Repay currency's available balance amount

---

# GET / 获取一键还债币种列表

查询一键还债币种列表。负债币种包括全仓负债和逐仓负债。仅适用于`跨币种保证金模式`/`组合保证金模式`。  
  
#### 限速：1次/2s

#### 限速规则：User ID

#### 权限：读取

#### HTTP 请求

`GET /api/v5/trade/one-click-repay-currency-list`

> 请求示例
    
    
    GET /api/v5/trade/one-click-repay-currency-list
    
    
    
    import okx.Trade as Trade
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘: 0, 模拟盘: 1
    
    tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)
    
    # 查询一键还债币种列表
    result = tradeAPI.get_oneclick_repay_list()
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
debtType | String | 否 | 负债类型   
`cross`: 全仓负债   
`isolated`: 逐仓负债  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "debtData": [
                    {
                        "debtAmt": "29.653478",
                        "debtCcy": "LTC"
                    },
                    {
                        "debtAmt": "237803.6828295906051002",
                        "debtCcy": "USDT"
                    }
                ],
                "debtType": "cross",
                "repayData": [
                    {
                        "repayAmt": "0.4978335419825104",
                        "repayCcy": "ETH"
                    }
                ]
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
debtData | Array of objects | 负债币种信息  
> debtCcy | String | 负债币种  
> debtAmt | String | 可负债币种数量  
包括本金和利息  
debtType | String | 负债类型   
`cross`: 全仓负债   
`isolated`: 逐仓负债  
repayData | Array of objects | 偿还币种信息  
> repayCcy | String | 可偿还负债的币种  
> repayAmt | String | 可偿还负债的币种可用资产数量