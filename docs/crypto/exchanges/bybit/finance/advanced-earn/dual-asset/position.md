---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/finance/advanced-earn/dual-asset/position
api_type: REST
updated_at: 2026-05-27 19:16:50.888542
---

# Get Product Quote

info

Does not need authentication. **Up to 50 requests** per second per IP.

### HTTP Request

GET `/v5/earn/advance/product-extra-info`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
productId| **true**|  string| Product ID  
[category](/docs/v5/enum#advanced-earn-category)| **true**|  string| Product category,`DualAssets`  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
[category](/docs/v5/enum#advanced-earn-category)| string| `DualAssets`  
list| array| Object  
> productId| string| Product ID  
> currentPrice| string| Current market price  
> buyLowPrice| array| List of available prices for Buy Low direction  
>> selectPrice| string| Optional target price  
>> apyE8| string| Annual Percentage Yield (e8 precision, i.e. APY × 10^8)  
>> maxInvestmentAmount| string| Maximum investment amount at this price  
>> expiredAt| string| The expiry time,Unix timestamp in ms  
> sellHighPrice| array| List of available prices for Sell High direction  
>> selectPrice| string| Optional target price  
>> apyE8| string| Annual Percentage Yield (e8 precision)  
>> maxInvestmentAmount| string| Maximum investment amount at this price  
>> expiredAt| string| The expiry time,Unix timestamp in ms  
  
### Request Example

  * HTTP


    
    
    GET /v5/earn/advance/product-extra-info?category=DualAssets&productId=36340 HTTP/1.1  
    Host: api-testnet.bybit.com  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "category": "DualAssets",  
            "list": [  
                {  
                    "productId": "36340",  
                    "currentPrice": "1.5275",  
                    "buyLowPrice": [  
                        {  
                            "selectPrice": "1.52",  
                            "apyE8": "810810000",  
                            "maxInvestmentAmount": "2000",  
                            "expiredAt": "1773814863140"  
                        },  
                        {  
                            "selectPrice": "1.51",  
                            "apyE8": "770310000",  
                            "maxInvestmentAmount": "2000",  
                            "expiredAt": "1773814863140"  
                        },  
                        {  
                            "selectPrice": "1.5",  
                            "apyE8": "729810000",  
                            "maxInvestmentAmount": "2000",  
                            "expiredAt": "1773814863140"  
                        },  
                        {  
                            "selectPrice": "1.4",  
                            "apyE8": "33927427",  
                            "maxInvestmentAmount": "15982.7136",  
                            "expiredAt": "1773814764000"  
                        },  
                        {  
                            "selectPrice": "1.45",  
                            "apyE8": "47326344",  
                            "maxInvestmentAmount": "15982.7136",  
                            "expiredAt": "1773814764000"  
                        },  
                        {  
                            "selectPrice": "1.527398",  
                            "apyE8": "259263094",  
                            "maxInvestmentAmount": "15982.7136",  
                            "expiredAt": "1773814770000"  
                        }  
                    ],  
                    "sellHighPrice": [  
                        {  
                            "selectPrice": "1.54",  
                            "apyE8": "729810000",  
                            "maxInvestmentAmount": "1309.92",  
                            "expiredAt": "1773814863140"  
                        },  
                        {  
                            "selectPrice": "1.55",  
                            "apyE8": "49979611",  
                            "maxInvestmentAmount": "10480",  
                            "expiredAt": "1773814764000"  
                        },  
                        {  
                            "selectPrice": "1.52",  
                            "apyE8": "810810000",  
                            "maxInvestmentAmount": "1309.92",  
                            "expiredAt": "1773814863140"  
                        },  
                        {  
                            "selectPrice": "1.53",  
                            "apyE8": "770310000",  
                            "maxInvestmentAmount": "1309.92",  
                            "expiredAt": "1773814863140"  
                        }  
                    ]  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1773814753684  
    }

---

# 查詢產品報價

信息

無需身份驗證。每個 IP 每秒**最多 50 次請求** 。

### HTTP 請求

GET `/v5/earn/advance/product-extra-info`

### 請求參數

參數| 必填| 類型| 說明  
---|---|---|---  
productId| **true**|  string| 產品 ID  
[category](/docs/zh-TW/v5/enum#advanced-earn-category)| **true**|  string| 產品類別，`DualAssets`  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
[category](/docs/zh-TW/v5/enum#advanced-earn-category)| string| `DualAssets`  
list| array| 列表  
> productId| string| 產品 ID  
> currentPrice| string| 當前市場價格  
> buyLowPrice| array| 低買 (Buy Low) 方向的可用價格列表  
>> selectPrice| string| 可選目標價格（掛鉤價）  
>> apyE8| string| 年化收益率（e8 精度，即 APY × 10^8）  
>> maxInvestmentAmount| string| 該價格下的最大投資額度  
>> expiredAt| string| 過期時間，毫秒級 Unix 時間戳  
> sellHighPrice| array| 高賣 (Sell High) 方向的可用價格列表  
>> selectPrice| string| 可選目標價格（掛鉤價）  
>> apyE8| string| 年化收益率（e8 精度）  
>> maxInvestmentAmount| string| 該價格下的最大投資額度  
>> expiredAt| string| 過期時間，毫秒級 Unix 時間戳  
  
### 請求示例

  * HTTP


    
    
    GET /v5/earn/advance/product-extra-info?category=DualAssets&productId=36340 HTTP/1.1  
    Host: api-testnet.bybit.com  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "category": "DualAssets",  
            "list": [  
                {  
                    "productId": "36340",  
                    "currentPrice": "1.5275",  
                    "buyLowPrice": [  
                        {  
                            "selectPrice": "1.52",  
                            "apyE8": "810810000",  
                            "maxInvestmentAmount": "2000",  
                            "expiredAt": "1773814863140"  
                        },  
                        {  
                            "selectPrice": "1.51",  
                            "apyE8": "770310000",  
                            "maxInvestmentAmount": "2000",  
                            "expiredAt": "1773814863140"  
                        },  
                        {  
                            "selectPrice": "1.5",  
                            "apyE8": "729810000",  
                            "maxInvestmentAmount": "2000",  
                            "expiredAt": "1773814863140"  
                        },  
                        {  
                            "selectPrice": "1.4",  
                            "apyE8": "33927427",  
                            "maxInvestmentAmount": "15982.7136",  
                            "expiredAt": "1773814764000"  
                        },  
                        {  
                            "selectPrice": "1.45",  
                            "apyE8": "47326344",  
                            "maxInvestmentAmount": "15982.7136",  
                            "expiredAt": "1773814764000"  
                        },  
                        {  
                            "selectPrice": "1.527398",  
                            "apyE8": "259263094",  
                            "maxInvestmentAmount": "15982.7136",  
                            "expiredAt": "1773814770000"  
                        }  
                    ],  
                    "sellHighPrice": [  
                        {  
                            "selectPrice": "1.54",  
                            "apyE8": "729810000",  
                            "maxInvestmentAmount": "1309.92",  
                            "expiredAt": "1773814863140"  
                        },  
                        {  
                            "selectPrice": "1.55",  
                            "apyE8": "49979611",  
                            "maxInvestmentAmount": "10480",  
                            "expiredAt": "1773814764000"  
                        },  
                        {  
                            "selectPrice": "1.52",  
                            "apyE8": "810810000",  
                            "maxInvestmentAmount": "1309.92",  
                            "expiredAt": "1773814863140"  
                        },  
                        {  
                            "selectPrice": "1.53",  
                            "apyE8": "770310000",  
                            "maxInvestmentAmount": "1309.92",  
                            "expiredAt": "1773814863140"  
                        }  
                    ]  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1773814753684  
    }