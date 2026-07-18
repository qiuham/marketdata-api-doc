---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/finance/earn/fixed-saving/place-order
api_type: REST
updated_at: 2026-07-18 18:59:19.808299
---

# Get Position Info

API ker permission: `Earn`  
API rate limit: 10 reqs / sec

info

  * Only active positions are returned. Settled positions (status `REVENUE_DISTRIBUTED`) are excluded.
  * All filters are optional — omit them to return all active positions.



### HTTP Request

GET`/v5/earn/fixed-term/position`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
productId| false| string| Filter by product ID  
category| false| string| Filter by product sub-type: `FixedTermSaving`, `FundPool`, `FundPoolPremium`  
coin| false| string| Filter by coin, e.g. `BTC`, `ETH`  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
list| array| Position list  
> positionId| string| Position ID  
> productId| string| Product ID  
> category| string| Product sub-type: `FixedTermSaving`, `FundPool`, `FundPoolPremium`  
> coin| string| Staking coin  
> amount| string| Position amount  
> effectiveAmount| string| Effective amount earning interest (takes effect T+1)  
> duration| string| Fixed term duration, e.g. `1d`, `8h`, `2m`  
> status| string| Position status: `Active`, `EarlyRedemptionProcessing`  
> settlementTime| string| Maturity time, unix timestamp in ms  
> createdAt| string| Position creation time, unix timestamp in ms  
> orderId| string| Associated order ID  
> earlyRedeemInfo| object| Early redemption info  
>> allowEarlyRedeem| boolean| Whether early redemption is available  
>> earlyRedeemEarning| string| Estimated earnings if redeemed early now  
>> returnCoin| string| Coin returned upon redemption  
>> redemptionLimitDuration| string| Minimum hold time required before early redemption, e.g. `1d`, `8h`, `2m`  
> allowAutoReinvest| boolean| Whether the product supports auto-reinvest  
> autoReinvest| string| User's current auto-reinvest setting: `Enable`, `Disable`  
> interestCoinApyList| array| Multi-coin reward APY list  
>> coin| string| Reward coin  
>> apy| string| Reward APY  
>> expectReturnEarning| string| Expected earnings for this position  
>> price| string| Locked price of the reward coin  
  
* * *

### Request Example
    
    
    GET /v5/earn/fixed-term/position?category=FixedTermSaving HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1741651200000  
    X-BAPI-RECV-WINDOW: 5000  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "list": [  
                {  
                    "positionId": "4064",  
                    "productId": "724",  
                    "category": "FixedTermSaving",  
                    "coin": "USDT",  
                    "amount": "201",  
                    "effectiveAmount": "201",  
                    "duration": "3d",  
                    "status": "Active",  
                    "settlementTime": "1776385800000",  
                    "createdAt": "1776068177000",  
                    "orderId": "86468516-5497-4a2b-8c4c-f9c58e01e12c",  
                    "earlyRedeemInfo": null,  
                    "allowAutoReinvest": false,  
                    "autoReinvest": "Disable",  
                    "interestCoinApyList": [  
                        {  
                            "coin": "USDT",  
                            "apy": "555.00%",  
                            "expectReturnEarning": "9.1689",  
                            "price": "1.00"  
                        }  
                    ]  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1776070463687  
    }

---

# 取得持倉資訊

API key權限：`Earn`  
API 頻率限制：每秒10次

信息

  * 僅返回活躍持倉。已結算持倉（狀態 `REVENUE_DISTRIBUTED`）不在返回範圍內。
  * 所有過濾條件均為可選，省略時返回所有活躍持倉。



### HTTP 請求

GET`/v5/earn/fixed-term/position`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
productId| false| string| 依產品ID篩選  
category| false| string| 依產品子類型篩選：`FixedTermSaving`、`FundPool`、`FundPoolPremium`  
coin| false| string| 依幣種篩選，例如 `BTC`、`ETH`  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
list| array| 持倉列表  
> positionId| string| 持倉ID  
> productId| string| 產品ID  
> category| string| 產品子類型：`FixedTermSaving`、`FundPool`、`FundPoolPremium`  
> coin| string| 質押幣種  
> amount| string| 持倉金額  
> effectiveAmount| string| 有效計息金額（T+1生效）  
> duration| string| 固定期限，例如 `1d`、`8h`、`2m`  
> status| string| 持倉狀態：`Active`、`EarlyRedemptionProcessing`  
> settlementTime| string| 到期時間，毫秒級unix時間戳  
> createdAt| string| 持倉創建時間，毫秒級unix時間戳  
> orderId| string| 關聯訂單ID  
> earlyRedeemInfo| object| 提前贖回資訊  
>> allowEarlyRedeem| boolean| 是否可以提前贖回  
>> earlyRedeemEarning| string| 當前提前贖回的預計收益  
>> returnCoin| string| 贖回時返還的幣種  
>> redemptionLimitDuration| string| 允許提前贖回前的最短持有時間，例如 `1d`、`8h`、`2m`  
> allowAutoReinvest| boolean| 產品是否支持自動續投  
> autoReinvest| string| 用戶當前的自動續投設置：`Enable`、`Disable`  
> interestCoinApyList| array| 多幣種獎勵APY列表  
>> coin| string| 獎勵幣種  
>> apy| string| 獎勵APY  
>> expectReturnEarning| string| 此持倉的預計收益  
>> price| string| 獎勵幣種鎖定價格  
  
* * *

### 請求示例
    
    
    GET /v5/earn/fixed-term/position?category=FixedTermSaving HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1741651200000  
    X-BAPI-RECV-WINDOW: 5000  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "list": [  
                {  
                    "positionId": "4064",  
                    "productId": "724",  
                    "category": "FixedTermSaving",  
                    "coin": "USDT",  
                    "amount": "201",  
                    "effectiveAmount": "201",  
                    "duration": "3d",  
                    "status": "Active",  
                    "settlementTime": "1776385800000",  
                    "createdAt": "1776068177000",  
                    "orderId": "86468516-5497-4a2b-8c4c-f9c58e01e12c",  
                    "earlyRedeemInfo": null,  
                    "allowAutoReinvest": false,  
                    "autoReinvest": "Disable",  
                    "interestCoinApyList": [  
                        {  
                            "coin": "USDT",  
                            "apy": "555.00%",  
                            "expectReturnEarning": "9.1689",  
                            "price": "1.00"  
                        }  
                    ]  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1776070463687  
    }