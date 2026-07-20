---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-trade-get-one-click-repay-currency-list-new
anchor_id: order-book-trading-trade-get-one-click-repay-currency-list-new
api_type: API
updated_at: 2026-07-20 19:35:32.736021
---

# GET / One-click repay currency list (New)

Get list of debt currency data and repay currencies. Only applicable to `SPOT mode`/`Multi-currency margin mode`/`Portfolio margin mode`.  
  
#### Rate Limit: 1 request per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/trade/one-click-repay-currency-list-v2`

> Request Example
    
    
    GET /api/v5/trade/one-click-repay-currency-list-v2
    
    
    
    import okx.Trade as Trade
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    flag = "1"  # Production trading: 0, Demo trading: 1
    
    tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag,debug=True) 
    result = tradeAPI.get_oneclick_repay_list_v2()
    print(result)
    

> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "debtData": [
                    {
                        "debtAmt": "100",
                        "debtCcy": "USDC"
                    }
                ],
                "repayData": [
                    {
                        "repayAmt": "1.000022977",
                        "repayCcy": "BTC"
                    },
                    {
                        "repayAmt": "4998.0002397",
                        "repayCcy": "USDT"
                    },
                    {
                        "repayAmt": "100",
                        "repayCcy": "OKB"
                    },
                    {
                        "repayAmt": "1",
                        "repayCcy": "ETH"
                    },
                    {
                        "repayAmt": "100",
                        "repayCcy": "USDC"
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
repayData | Array of objects | Repay currency data list  
> repayCcy | String | Repay currency  
> repayAmt | String | Repay currency's available balance amount

---

# GET / 获取一键还债币种列表(新)

查询一键还债币种列表。仅适用于`现货模式`/`跨币种保证金模式`/`组合保证金模式`。  
  
#### 限速：1次/2s

#### 限速规则：User ID

#### HTTP 请求

`GET /api/v5/trade/one-click-repay-currency-list-v2`

> 请求示例
    
    
    GET /api/v5/trade/one-click-repay-currency-list-v2
    
    
    
    import okx.Trade as Trade
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    flag = "1"  # 实盘: 0, 模拟盘: 1
    
    tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag,debug=True) 
    result = tradeAPI.get_oneclick_repay_list_v2()
    print(result)
    

> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "debtData": [
                    {
                        "debtAmt": "100",
                        "debtCcy": "USDC"
                    }
                ],
                "repayData": [
                    {
                        "repayAmt": "1.000022977",
                        "repayCcy": "BTC"
                    },
                    {
                        "repayAmt": "4998.0002397",
                        "repayCcy": "USDT"
                    },
                    {
                        "repayAmt": "100",
                        "repayCcy": "OKB"
                    },
                    {
                        "repayAmt": "1",
                        "repayCcy": "ETH"
                    },
                    {
                        "repayAmt": "100",
                        "repayCcy": "USDC"
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
repayData | Array of objects | 偿还币种信息  
> repayCcy | String | 可偿还负债的币种  
> repayAmt | String | 可偿还负债的币种可用资产数量