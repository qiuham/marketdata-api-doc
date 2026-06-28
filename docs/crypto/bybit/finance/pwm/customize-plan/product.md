---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/finance/pwm/customize-plan/product
api_type: REST
updated_at: 2026-05-27 19:17:53.557042
---

# Get Subscribable Product Info

info

Does not need authentication.

### HTTP Request

GET`/v5/earn/pwm/customize-plan/product`

### Request Parameters

None

### Response Parameters

Parameter| Type| Comments  
---|---|---  
products| array| Product card list grouped by category  
> type| string| Product category: `equityFund` / `multiCoinEarning` / `onchainEarn` / `fixedYield`  
> cards| array| Product card list for this category  
>> category| string| Product type  
>> productId| string| Underlying product ID (available for flexible savings / fixed yield / on-chain earn products)  
>> fundName| string| Fund name in English (fund products)  
>> coin| string| Product coin  
>> apr| string| Current annualized return rate (flexible savings / fixed yield products)  
>> aprRangeLow| string| APR lower bound (fund products)  
>> aprRangeHigh| string| APR upper bound (fund products)  
>> tags| array[string]| Product tags  
>> introduction| string| Product introduction in English (fund products)  
>> aum| string| Assets under management (base coin)  
>> minInvestmentAmount| string| Minimum subscription amount  
>> maxInvestmentAmount| string| Maximum subscription amount  
>> duration| int| Lock-up period in days. `0` means flexible (fixed yield products)  
>> maxDrawdown| string| Historical maximum drawdown (fund products)  
>> sharpRatio| string| Sharpe ratio (fund products)  
>> estAPR| string| Estimated APR for the product  
  
* * *

### Request Example
    
    
    GET /v5/earn/pwm/customize-plan/product HTTP/1.1  
    Host: api.bybit.com  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "result": {  
            "products": [  
                {  
                    "type": "equityFund",  
                    "cards": [  
                        {  
                            "category": "equityFund",  
                            "fundName": "Market Neutral Alpha",  
                            "coin": "USDT",  
                            "aprRangeLow": "0.08",  
                            "aprRangeHigh": "0.15",  
                            "tags": ["Delta Neutral"],  
                            "introduction": "A market-neutral strategy fund",  
                            "aum": "5000000",  
                            "minInvestmentAmount": "100000",  
                            "maxInvestmentAmount": "5000000",  
                            "maxDrawdown": "-0.035",  
                            "sharpRatio": "2.3",  
                            "estAPR": "0.06"  
                        }  
                    ]  
                },  
                {  
                    "type": "multiCoinEarning",  
                    "cards": [  
                        {  
                            "category": "flexibleSavings",  
                            "productId": "430",  
                            "coin": "USDT",  
                            "apr": "0.05",  
                            "duration": 0,  
                            "minInvestmentAmount": "10000",  
                            "maxInvestmentAmount": "10000000",  
                            "estAPR": "0.02"  
                        }  
                    ]  
                }  
            ]  
        }  
    }

---

# 查詢可申購產品卡片（直客模式）

信息

無需身份驗證。

### HTTP 請求

GET`/v5/earn/pwm/customize-plan/product`

### 請求參數

無

### 響應參數

參數| 類型| 說明  
---|---|---  
products| array| 按產品類別分組的卡片列表  
> type| string| 產品類別：`equityFund` / `multiCoinEarning` / `onchainEarn` / `fixedYield`  
> cards| array| 該類別下的產品卡片列表  
>> category| string| 產品類型  
>> productId| string| 對應的底層產品ID（活期 / 固收 / 鏈上賺幣產品有此字段）  
>> fundName| string| 基金名稱英文（基金產品）  
>> coin| string| 產品幣種  
>> apr| string| 當前年化收益率（活期 / 固收產品）  
>> aprRangeLow| string| 年化收益率下界（基金產品）  
>> aprRangeHigh| string| 年化收益率上界（基金產品）  
>> tags| array[string]| 產品標籤  
>> introduction| string| 產品簡介英文（基金產品）  
>> aum| string| 基金管理規模（本位幣）  
>> minInvestmentAmount| string| 最小申購金額  
>> maxInvestmentAmount| string| 最大申購金額  
>> duration| int| 鎖定期天數，`0` 表示活期（固收產品）  
>> maxDrawdown| string| 歷史最大回撤（基金產品）  
>> sharpRatio| string| 夏普比率（基金產品）  
>> estAPR| string| 產品預估APR  
  
* * *

### 請求示例
    
    
    GET /v5/earn/pwm/customize-plan/product HTTP/1.1  
    Host: api.bybit.com  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "result": {  
            "products": [  
                {  
                    "type": "equityFund",  
                    "cards": [  
                        {  
                            "category": "equityFund",  
                            "fundName": "Market Neutral Alpha",  
                            "coin": "USDT",  
                            "aprRangeLow": "0.08",  
                            "aprRangeHigh": "0.15",  
                            "tags": ["Delta Neutral"],  
                            "introduction": "A market-neutral strategy fund",  
                            "aum": "5000000",  
                            "minInvestmentAmount": "100000",  
                            "maxInvestmentAmount": "5000000",  
                            "maxDrawdown": "-0.035",  
                            "sharpRatio": "2.3",  
                            "estAPR": "0.06"  
                        }  
                    ]  
                },  
                {  
                    "type": "multiCoinEarning",  
                    "cards": [  
                        {  
                            "category": "flexibleSavings",  
                            "productId": "430",  
                            "coin": "USDT",  
                            "apr": "0.05",  
                            "duration": 0,  
                            "minInvestmentAmount": "10000",  
                            "maxInvestmentAmount": "10000000",  
                            "estAPR": "0.02"  
                        }  
                    ]  
                }  
            ]  
        }  
    }