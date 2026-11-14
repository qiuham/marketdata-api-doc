---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/finance/advanced-earn/liquidity-mining/product-info
api_type: REST
updated_at: 2026-11-13 19:22:56.193528
---

# Get Product Info

info

No authentication required. **Up to 50 requests** per second per IP.

### HTTP Request

GET`/v5/earn/liquidity-mining/product`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
baseCoin| false| string| Filter by base coin, e.g. `BTC`, `ETH`  
quoteCoin| false| string| Filter by quote coin, e.g. `USDT`  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
products| array| Product list  
> productId| string| Product ID  
> baseCoin| string| Base coin, e.g. `BTC`  
> quoteCoin| string| Quote coin, e.g. `USDT`  
> status| string| Product status: `Available`, `NotAvailable`  
> maxLeverage| integer| Maximum leverage multiplier  
> minInvestmentQuote| string| Minimum investment amount in quoteCoin  
> minInvestmentBase| string| Minimum investment amount in baseCoin  
> maxInvestmentQuote| string| Maximum investment amount in quoteCoin  
> maxInvestmentBase| string| Maximum investment amount in baseCoin  
> minWithdrawalAmount| string| Minimum withdrawal amount (in quoteCoin)  
> minReinvestAmount| string| Minimum reinvestment amount (in quoteCoin)  
> baseCoinPrecision| integer| Decimal precision for baseCoin amounts  
> quoteCoinPrecision| integer| Decimal precision for quoteCoin amounts  
> yieldCoins| array| List of yield coins, e.g. `["BTC", "USDT"]`  
> apyE8| integer| Current APY in e8 precision. Divide by 10^8 to get the actual rate  
> apy7dE8| integer| 7-day APY in e8 precision. Divide by 10^8 to get the actual rate  
> poolLiquidityValue| string| Total pool liquidity value (quoted in quoteCoin)  
> dailyYield| string| Daily yield  
> slippageLevels| array| Investment amount thresholds for each slippage tier  
> slippageRateE8List| array| Slippage rates for each tier in e8 precision  
> apyBreakdown| array| APY breakdown by coin  
>> coin| string| Coin name  
>> apy| string| APY for this coin  
> apy7dBreakdown| array| 7-day APY breakdown by coin  
>> coin| string| Coin name  
>> apy| string| 7-day APY for this coin  
  
* * *

### Request Example
    
    
    GET /v5/earn/liquidity-mining/product?baseCoin=BTC HTTP/1.1  
    Host: api-testnet.bybit.com  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "products": [  
                {  
                    "productId": "5",  
                    "baseCoin": "ETH",  
                    "quoteCoin": "USDT",  
                    "status": "Available",  
                    "maxLeverage": 3,  
                    "minInvestmentQuote": "1",  
                    "minInvestmentBase": "0.01",  
                    "maxInvestmentQuote": "150000",  
                    "maxInvestmentBase": "50",  
                    "minWithdrawalAmount": "20",  
                    "baseCoinPrecision": 8,  
                    "quoteCoinPrecision": 4,  
                    "minReinvestAmount": "10",  
                    "yieldCoins": [  
                        "USDT"  
                    ],  
                    "apyE8": "13714946",  
                    "apy7dE8": "338344880",  
                    "poolLiquidityValue": "1361221.17",  
                    "dailyYield": "1028.3745",  
                    "slippageLevels": [  
                        "0",  
                        "500",  
                        "100000",  
                        "500000"  
                    ],  
                    "apyBreakdown": [],  
                    "apy7dBreakdown": [],  
                    "slippageRateE8List": [  
                        "0",  
                        "100000",  
                        "300000",  
                        "500000"  
                    ]  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1775121766407  
    }

---

# 查詢產品資訊

信息

無需身份驗證。每個 IP 每秒**最多 50 次請求** 。

### HTTP 請求

GET`/v5/earn/liquidity-mining/product`

### 請求參數

參數| 必填| 類型| 說明  
---|---|---|---  
baseCoin| false| string| 按基礎幣種篩選，僅限大寫，例如：`BTC`, `ETH`  
quoteCoin| false| string| 按計價幣種篩選，僅限大寫，例如：`USDT`  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
products| array| 產品列表  
> productId| string| 產品 ID  
> baseCoin| string| 基礎幣種，例如：`BTC`  
> quoteCoin| string| 計價幣種，例如：`USDT`  
> status| string| 產品狀態：`Available`（可用），`NotAvailable`（不可用）  
> maxLeverage| integer| 最大槓桿倍數  
> minInvestmentQuote| string| 計價幣種最小投資金額  
> minInvestmentBase| string| 基礎幣種最小投資金額  
> maxInvestmentQuote| string| 計價幣種最大投資金額  
> maxInvestmentBase| string| 基礎幣種最大投資金額  
> minWithdrawalAmount| string| 最小提取金額（以計價幣種計）  
> minReinvestAmount| string| 最小再投資金額（以計價幣種計）  
> baseCoinPrecision| integer| 基礎幣種金額小數精度  
> quoteCoinPrecision| integer| 計價幣種金額小數精度  
> yieldCoins| array| 收益幣種列表，例如：`["BTC", "USDT"]`  
> apyE8| integer| 當前年化收益率（e8 精度）。除以 10^8 可得實際利率  
> apy7dE8| integer| 7 日年化收益率（e8 精度）。除以 10^8 可得實際利率  
> poolLiquidityValue| string| 流動性池總價值（以計價幣種計）  
> dailyYield| string| 每日收益  
> slippageLevels| array| 各滑點檔位對應的投資金額閾值  
> slippageRateE8List| array| 各檔位滑點率（e8 精度）  
> apyBreakdown| array| 按幣種拆分的年化收益率  
>> coin| string| 幣種名稱  
>> apy| string| 該幣種的年化收益率  
> apy7dBreakdown| array| 按幣種拆分的 7 日年化收益率  
>> coin| string| 幣種名稱  
>> apy| string| 該幣種的 7 日年化收益率  
  
* * *

### 請求示例
    
    
    GET /v5/earn/liquidity-mining/product?baseCoin=BTC HTTP/1.1  
    Host: api-testnet.bybit.com  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "products": [  
                {  
                    "productId": "5",  
                    "baseCoin": "ETH",  
                    "quoteCoin": "USDT",  
                    "status": "Available",  
                    "maxLeverage": 3,  
                    "minInvestmentQuote": "1",  
                    "minInvestmentBase": "0.01",  
                    "maxInvestmentQuote": "150000",  
                    "maxInvestmentBase": "50",  
                    "minWithdrawalAmount": "20",  
                    "baseCoinPrecision": 8,  
                    "quoteCoinPrecision": 4,  
                    "minReinvestAmount": "10",  
                    "yieldCoins": [  
                        "USDT"  
                    ],  
                    "apyE8": "13714946",  
                    "apy7dE8": "338344880",  
                    "poolLiquidityValue": "1361221.17",  
                    "dailyYield": "1028.3745",  
                    "slippageLevels": [  
                        "0",  
                        "500",  
                        "100000",  
                        "500000"  
                    ],  
                    "apyBreakdown": [],  
                    "apy7dBreakdown": [],  
                    "slippageRateE8List": [  
                        "0",  
                        "100000",  
                        "300000",  
                        "500000"  
                    ]  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1775121766407  
    }