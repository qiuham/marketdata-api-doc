---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/finance/pwm/investment-plan/detail
api_type: REST
updated_at: 2026-11-13 19:23:32.013303
---

# Get Investment Plan Detail

### HTTP Request

GET`/v5/earn/pwm/investment-plan/detail`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
planId| **true**|  string| Investment plan ID. Must be in `Active` or `Closed` status  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
planId| string| Unique identifier of the investment plan  
planName| string| Investment plan name  
planType| string| Plan type: `stable` / `advanced`  
status| string| Plan status: `Active` / `Closed`  
currentAssetUsd| string| Total current assets (USD valuation)  
accumulateYieldUsd| string| Total accumulated yield (USD valuation)  
weightedAvgApr| string| Weighted average annualized return rate (decimal form, e.g. `0.086` means 8.6%)  
currentAssets| array| List of currently held coin assets  
> coin| string| Coin name  
> amount| string| Holding amount (in base coin)  
positions| object| Position details by product category  
> multiCoinsEarning| object| Flexible savings positions  
>> totalInvestmentUsd| string| Total investment for this category (USD)  
>> accumulateYieldUsd| string| Accumulated yield for this category (USD)  
>> weightedAvgApr| string| Weighted average APR for this category  
>> items| array| Flexible product position details  
>>> category| string| Product category  
>>> productId| string| Product ID  
>>> coin| string| Coin  
>>> currentAmount| string| Current holding amount  
>>> accumulateYield| string| Accumulated yield (base coin)  
>>> apr| string| Current annualized return rate  
>>> positionId| string| Position ID  
>>> status| string| Product status: `0`-Processing / `1`-Active / `2`-Redeeming / `3`-PendingSubscription / `4`-Closed  
> fixedYield| object| Fixed yield positions (Classic/Premium WM)  
>> totalInvestmentUsd| string| Total investment for this category (USD)  
>> accumulateYieldUsd| string| Accumulated yield for this category (USD)  
>> weightedAvgApr| string| Weighted average APR for this category  
>> items| array| Fixed yield product position details  
>>> category| string| Product category  
>>> productId| string| Product ID  
>>> coin| string| Coin  
>>> currentAmount| string| Current holding amount  
>>> accumulateYield| string| Accumulated yield (base coin)  
>>> apr| string| Annualized return rate  
>>> duration| int| Lock-up period in days  
>>> maturityTime| string| Maturity timestamp (milliseconds)  
>>> autoReinvest| boolean| Whether auto-reinvest is enabled  
>>> positionId| string| Position ID  
>>> status| string| Product status: `0`-Processing / `1`-Active / `2`-Redeeming / `3`-PendingSubscription / `4`-Closed  
> equityFunds| object| Equity fund positions  
>> totalInvestmentUsd| string| Total investment for this category (USD)  
>> accumulateYieldUsd| string| Accumulated yield for this category (USD)  
>> weightedAvgApr| string| Weighted average APR for this category  
>> items| array| Fund position details  
>>> category| string| Product category  
>>> productId| string| Fund unique identifier  
>>> fundName| string| Fund name  
>>> coin| string| Fund denomination coin  
>>> tags| array[string]| Fund tags  
>>> nav| string| Current net asset value  
>>> userShares| string| Number of shares held by user  
>>> shareValue| string| Current value per share  
>>> holdingValue| string| Total holding value of user  
>>> accumulateYield| string| Accumulated yield (base coin)  
>>> apr30d| string| 30-day annualized return rate  
>>> aprTotal| string| Annualized return since inception  
>>> sharpRatio| string| Sharpe ratio  
>>> maxDrawdown| string| Maximum drawdown (negative value)  
>>> createdTime| string| Fund inception timestamp (milliseconds)  
>>> runningDays| int| Number of days the fund has been running  
>>> positionId| string| Position ID  
>>> status| string| Product status: `0`-Processing / `1`-Active / `2`-Redeeming / `3`-PendingSubscription / `4`-Closed  
> onchainEarn| object| On-chain earn positions  
>> totalInvestmentUsd| string| Total investment for this category (USD)  
>> accumulateYieldUsd| string| Accumulated yield for this category (USD)  
>> items| array| On-chain product position list  
>>> category| string| Product category  
>>> productId| string| Product ID  
>>> coin| string| Coin  
>>> stakeAmount| string| Staked amount  
>>> apr| string| Current annualized return rate  
>>> positionId| string| Position ID  
>>> status| string| Product status: `0`-Processing / `1`-Active / `2`-Redeeming / `3`-PendingSubscription / `4`-Closed  
> fundingAccount| array| Idle funds in WM Vendor sub-account  
>> coin| string| Coin  
>> amount| string| Idle amount  
createdTime| string| Investment plan creation timestamp (milliseconds)  
  
* * *

### Request Example
    
    
    GET /v5/earn/pwm/investment-plan/detail?planId=10001 HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1741651200000  
    X-BAPI-RECV-WINDOW: 5000  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "result": {  
            "planId": "10001",  
            "planName": "Conservative Growth Plan",  
            "planType": "conservative",  
            "status": "Active",  
            "currentAssetUsd": "200137.50",  
            "accumulateYieldUsd": "2137.50",  
            "weightedAvgApr": "0.086",  
            "currentAssets": [  
                {  
                    "coin": "USDT",  
                    "amount": "150000.00"  
                }  
            ],  
            "positions": {  
                "multiCoinsEarning": {  
                    "totalInvestmentUsd": "60000.00",  
                    "accumulateYieldUsd": "500.00",  
                    "weightedAvgApr": "0.052",  
                    "items": [  
                        {  
                            "category": "flexibleSavings",  
                            "productId": "430",  
                            "coin": "USDT",  
                            "currentAmount": "30000.00",  
                            "accumulateYield": "250.00",  
                            "apr": "0.05",  
                            "positionId": "123"  
                        }  
                    ]  
                },  
                "fixedYield": {  
                    "totalInvestmentUsd": "50000.00",  
                    "accumulateYieldUsd": "800.00",  
                    "weightedAvgApr": "0.08",  
                    "items": [  
                        {  
                            "category": "fundPool",  
                            "productId": "430",  
                            "coin": "USDT",  
                            "currentAmount": "50000.00",  
                            "accumulateYield": "800.00",  
                            "apr": "0.08",  
                            "duration": 30,  
                            "maturityTime": "1700500000000",  
                            "autoReinvest": true,  
                            "positionId": "123"  
                        }  
                    ]  
                },  
                "equityFunds": {  
                    "totalInvestmentUsd": "70000.00",  
                    "accumulateYieldUsd": "700.00",  
                    "weightedAvgApr": "0.12",  
                    "items": [  
                        {  
                            "category": "equityFund",  
                            "productId": "2001",  
                            "fundName": "Market Neutral Alpha",  
                            "coin": "USDT",  
                            "tags": ["Delta Neutral", "Funding Rate"],  
                            "nav": "1.035",  
                            "userShares": "68000.00",  
                            "shareValue": "1.029",  
                            "holdingValue": "69972.00",  
                            "accumulateYield": "700.00",  
                            "apr30d": "0.12",  
                            "aprTotal": "0.105",  
                            "sharpRatio": "2.5",  
                            "maxDrawdown": "-0.032",  
                            "createdTime": "1695000000000",  
                            "runningDays": 58  
                        }  
                    ]  
                },  
                "onchainEarn": {  
                    "totalInvestmentUsd": "18000.00",  
                    "accumulateYieldUsd": "137.50",  
                    "items": [  
                        {  
                            "category": "onchainEarn",  
                            "productId": "430",  
                            "coin": "USDT",  
                            "stakeAmount": "18000.00",  
                            "apr": "0.075",  
                            "positionId": "123"  
                        }  
                    ]  
                },  
                "fundingAccount": [  
                    {  
                        "coin": "USDT",  
                        "amount": "165.50"  
                    }  
                ]  
            },  
            "createdTime": "1700000000000"  
        }  
    }

---

# 查詢已投資計劃詳情

### HTTP 請求

GET`/v5/earn/pwm/investment-plan/detail`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
planId| **true**|  string| 投資計劃ID（須為 `Active` 或 `Closed` 狀態）  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
planId| string| 投資計劃唯一標識  
planName| string| 投資計劃名稱  
planType| string| 計劃類型：`stable` / `advanced`  
status| string| 計劃狀態：`Active` / `Closed`  
currentAssetUsd| string| 當前總資產（USD估值）  
accumulateYieldUsd| string| 累計總收益（USD估值）  
weightedAvgApr| string| 加權平均年化收益率（小數形式，如 `0.086` 表示8.6%）  
currentAssets| array| 當前持有的幣種資產列表  
> coin| string| 幣種名稱  
> amount| string| 持有數量（本位幣）  
positions| object| 各產品類別持倉詳情  
> multiCoinsEarning| object| 活期理財持倉  
>> totalInvestmentUsd| string| 該類別總投資（USD）  
>> accumulateYieldUsd| string| 該類別累計收益（USD）  
>> weightedAvgApr| string| 該類別加權平均年化  
>> items| array| 活期產品持倉明細列表  
>>> category| string| 產品類別  
>>> productId| string| 產品ID  
>>> coin| string| 幣種  
>>> currentAmount| string| 當前持有數量  
>>> accumulateYield| string| 累計收益（本位幣）  
>>> apr| string| 當前年化收益率  
>>> positionId| string| 產品的倉位ID  
>>> status| string| 產品狀態：`0`-Processing（申購中）/ `1`-Active / `2`-Redeeming（贖回中）/ `3`-PendingSubscription / `4`-Closed  
> fixedYield| object| 固定收益持倉（Classic/Premium WM）  
>> totalInvestmentUsd| string| 該類別總投資（USD）  
>> accumulateYieldUsd| string| 該類別累計收益（USD）  
>> weightedAvgApr| string| 該類別加權平均年化  
>> items| array| 固定收益產品持倉明細列表  
>>> category| string| 產品類別  
>>> productId| string| 產品ID  
>>> coin| string| 幣種  
>>> currentAmount| string| 當前持有金額  
>>> accumulateYield| string| 累計收益（本位幣）  
>>> apr| string| 年化收益率  
>>> duration| int| 鎖定期天數  
>>> maturityTime| string| 到期時間戳（毫秒）  
>>> autoReinvest| boolean| 是否自動續投  
>>> positionId| string| 產品的倉位ID  
>>> status| string| 產品狀態：`0`-Processing（申購中）/ `1`-Active / `2`-Redeeming（贖回中）/ `3`-PendingSubscription / `4`-Closed  
> equityFunds| object| 淨值型基金持倉  
>> totalInvestmentUsd| string| 該類別總投資（USD）  
>> accumulateYieldUsd| string| 該類別累計收益（USD）  
>> weightedAvgApr| string| 該類別加權平均年化  
>> items| array| 基金持倉明細列表  
>>> category| string| 產品類別  
>>> productId| string| 基金唯一標識  
>>> fundName| string| 基金名稱  
>>> coin| string| 基金計價幣種  
>>> tags| array[string]| 基金標籤  
>>> nav| string| 當前基金淨值  
>>> userShares| string| 用戶持有份額數量  
>>> shareValue| string| 當前每份價值  
>>> holdingValue| string| 用戶持倉總價值  
>>> accumulateYield| string| 累計收益（本位幣）  
>>> apr30d| string| 近30日年化收益率  
>>> aprTotal| string| 成立以來年化收益率  
>>> sharpRatio| string| 夏普比率  
>>> maxDrawdown| string| 最大回撤（負數）  
>>> createdTime| string| 基金成立時間戳（毫秒）  
>>> runningDays| int| 基金運行天數  
>>> positionId| string| 產品的倉位ID  
>>> status| string| 產品狀態：`0`-Processing（申購中）/ `1`-Active / `2`-Redeeming（贖回中）/ `3`-PendingSubscription / `4`-Closed  
> onchainEarn| object| 鏈上賺幣持倉  
>> totalInvestmentUsd| string| 該類別總投資（USD）  
>> accumulateYieldUsd| string| 該類別累計收益（USD）  
>> items| array| 鏈上產品持倉列表  
>>> category| string| 產品類別  
>>> productId| string| 產品ID  
>>> coin| string| 幣種  
>>> stakeAmount| string| 質押數量  
>>> apr| string| 當前年化收益率  
>>> positionId| string| 產品的倉位ID  
>>> status| string| 產品狀態：`0`-Processing（申購中）/ `1`-Active / `2`-Redeeming（贖回中）/ `3`-PendingSubscription / `4`-Closed  
> fundingAccount| array| WM Vendor子賬戶中的閒置資金列表  
>> coin| string| 幣種  
>> amount| string| 閒置金額  
createdTime| string| 投資計劃創建時間戳（毫秒）  
  
* * *

### 請求示例
    
    
    GET /v5/earn/pwm/investment-plan/detail?planId=10001 HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1741651200000  
    X-BAPI-RECV-WINDOW: 5000  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "result": {  
            "planId": "10001",  
            "planName": "Conservative Growth Plan",  
            "planType": "conservative",  
            "status": "Active",  
            "currentAssetUsd": "200137.50",  
            "accumulateYieldUsd": "2137.50",  
            "weightedAvgApr": "0.086",  
            "currentAssets": [  
                {  
                    "coin": "USDT",  
                    "amount": "150000.00"  
                }  
            ],  
            "positions": {  
                "multiCoinsEarning": {  
                    "totalInvestmentUsd": "60000.00",  
                    "accumulateYieldUsd": "500.00",  
                    "weightedAvgApr": "0.052",  
                    "items": [  
                        {  
                            "category": "flexibleSavings",  
                            "productId": "430",  
                            "coin": "USDT",  
                            "currentAmount": "30000.00",  
                            "accumulateYield": "250.00",  
                            "apr": "0.05",  
                            "positionId": "123"  
                        }  
                    ]  
                },  
                "fixedYield": {  
                    "totalInvestmentUsd": "50000.00",  
                    "accumulateYieldUsd": "800.00",  
                    "weightedAvgApr": "0.08",  
                    "items": [  
                        {  
                            "category": "fundPool",  
                            "productId": "430",  
                            "coin": "USDT",  
                            "currentAmount": "50000.00",  
                            "accumulateYield": "800.00",  
                            "apr": "0.08",  
                            "duration": 30,  
                            "maturityTime": "1700500000000",  
                            "autoReinvest": true,  
                            "positionId": "123"  
                        }  
                    ]  
                },  
                "equityFunds": {  
                    "totalInvestmentUsd": "70000.00",  
                    "accumulateYieldUsd": "700.00",  
                    "weightedAvgApr": "0.12",  
                    "items": [  
                        {  
                            "category": "equityFund",  
                            "productId": "2001",  
                            "fundName": "Market Neutral Alpha",  
                            "coin": "USDT",  
                            "tags": ["Delta Neutral", "Funding Rate"],  
                            "nav": "1.035",  
                            "userShares": "68000.00",  
                            "shareValue": "1.029",  
                            "holdingValue": "69972.00",  
                            "accumulateYield": "700.00",  
                            "apr30d": "0.12",  
                            "aprTotal": "0.105",  
                            "sharpRatio": "2.5",  
                            "maxDrawdown": "-0.032",  
                            "createdTime": "1695000000000",  
                            "runningDays": 58  
                        }  
                    ]  
                },  
                "onchainEarn": {  
                    "totalInvestmentUsd": "18000.00",  
                    "accumulateYieldUsd": "137.50",  
                    "items": [  
                        {  
                            "category": "onchainEarn",  
                            "productId": "430",  
                            "coin": "USDT",  
                            "stakeAmount": "18000.00",  
                            "apr": "0.075",  
                            "positionId": "123"  
                        }  
                    ]  
                },  
                "fundingAccount": [  
                    {  
                        "coin": "USDT",  
                        "amount": "165.50"  
                    }  
                ]  
            },  
            "createdTime": "1700000000000"  
        }  
    }