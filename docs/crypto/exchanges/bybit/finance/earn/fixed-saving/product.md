---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/finance/earn/fixed-saving/product
api_type: REST
updated_at: 2026-05-27 19:17:36.418075
---

# Get Product Info

info

Does not need authentication. **Up to 50 requests** per second per IP .

### HTTP Request

GET`/v5/earn/fixed-term/product`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
coin| false| string| Filter by coin, e.g. `BTC`, `ETH`. Returns all coins if omitted  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
list| array| Product list  
> productId| string| Product ID  
> category| string| Product sub-type: `FixedTermSaving`, `FundPool`, `FundPoolPremium`  
> coin| string| Staking coin  
> duration| string| Fixed term duration, e.g. `1d`, `8h`, `2m`  
> status| string| Product status: `Available`, `SoldOut`, `NotStarted`  
> tieredApyList| array| Tiered APY list (if applicable)  
>> min| string| Minimum amount for this tier  
>> max| string| Maximum amount for this tier. `"-1"` means no upper limit  
>> apy| string| APY for this tier  
> minStakeAmount| string| Minimum staking amount  
> maxStakeAmount| string| Maximum staking amount  
> precision| integer| Coin trading precision  
> subscribeStartAt| string| Subscription start time, unix timestamp in ms  
> subscribeEndAt| string| Subscription end time, unix timestamp in ms  
> allowEarlyRedemption| boolean| Whether early redemption is supported  
> earlyRedemptionApy| string| Discounted APY applied on early redemption  
> redemptionLimitDuration| string| Minimum hold time before early redemption is allowed, e.g. `1d`, `8h`, `2m`  
> allowAutoReinvest| boolean| Whether auto-reinvest is supported  
> interestCoinApyList| array| Multi-coin reward APY list  
>> coin| string| Reward coin  
>> apy| string| Reward APY  
>> expectUnitEarning| string| Expected reward per unit invested (influenced by spot price of reward coin)  
>> currentPrice| string| Current price of the reward coin  
> isVip| boolean| Whether this is a VIP-only product  
> creditTime| string| Estimated time for earnings to be credited, unix timestamp in ms  
> specialUserGroupRequired| boolean| Whether purchase is restricted to a specific user group  
> specialUserGroupInfo| string| Description of the restricted user group  
  
* * *

### Request Example
    
    
    GET /v5/earn/fixed-term/product?coin=BTC HTTP/1.1  
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
                    "productId": "427",  
                    "category": "FixedTermSaving",  
                    "coin": "USDT",  
                    "duration": "30d",  
                    "status": "Available",  
                    "tieredApyList": [],  
                    "minStakeAmount": "50",  
                    "maxStakeAmount": "10000",  
                    "precision": 4,  
                    "subscribeStartAt": "1686704400000",  
                    "subscribeEndAt": "1909094399000",  
                    "allowEarlyRedemption": false,  
                    "earlyRedemptionApy": "",  
                    "redemptionLimitDuration": "",  
                    "allowAutoReinvest": false,  
                    "interestCoinApyList": [  
                        {  
                            "coin": "USDT",  
                            "apy": "2.50%",  
                            "expectUnitEarning": "0.002",  
                            "currentPrice": "1.00"  
                        }  
                    ],  
                    "isVip": false,  
                    "creditTime": "1778718600000",  
                    "specialUserGroupRequired": false,  
                    "specialUserGroupInfo": ""  
                },  
                {  
                    "productId": "27",  
                    "category": "FundPool",  
                    "coin": "USDT",  
                    "duration": "3d",  
                    "status": "Available",  
                    "tieredApyList": [],  
                    "minStakeAmount": "100",  
                    "maxStakeAmount": "10000",  
                    "precision": 4,  
                    "subscribeStartAt": "1722448800000",  
                    "subscribeEndAt": "0",  
                    "allowEarlyRedemption": true,  
                    "earlyRedemptionApy": "0.30%",  
                    "redemptionLimitDuration": "1d",  
                    "allowAutoReinvest": false,  
                    "interestCoinApyList": [  
                        {  
                            "coin": "USDT",  
                            "apy": "9.99%",  
                            "expectUnitEarning": "0.0008",  
                            "currentPrice": "1.00"  
                        }  
                    ],  
                    "isVip": false,  
                    "creditTime": "1776391500000",  
                    "specialUserGroupRequired": true,  
                    "specialUserGroupInfo": "Limited Offer"  
                },  
                {  
                    "productId": "12",  
                    "category": "FundPoolPremium",  
                    "coin": "USDT",  
                    "duration": "3d",  
                    "status": "Available",  
                    "tieredApyList": [],  
                    "minStakeAmount": "1",  
                    "maxStakeAmount": "300",  
                    "precision": 4,  
                    "subscribeStartAt": "1751500800000",  
                    "subscribeEndAt": "0",  
                    "allowEarlyRedemption": false,  
                    "earlyRedemptionApy": "",  
                    "redemptionLimitDuration": "",  
                    "allowAutoReinvest": false,  
                    "interestCoinApyList": [  
                        {  
                            "coin": "USDT",  
                            "apy": "19.70%",  
                            "expectUnitEarning": "0.0016",  
                            "currentPrice": "1.00"  
                        }  
                    ],  
                    "isVip": true,  
                    "creditTime": "1776391200000",  
                    "specialUserGroupRequired": false,  
                    "specialUserGroupInfo": ""  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1776067553433  
    }

---

# 查詢產品資訊

信息

無需身份驗證。每個IP每秒最多 **50次** 請求。

### HTTP 請求

GET`/v5/earn/fixed-term/product`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
coin| false| string| 依幣種篩選，例如 `BTC`、`ETH`。若省略則返回所有幣種  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
list| array| 產品列表  
> productId| string| 產品ID  
> category| string| 產品子類型：`FixedTermSaving`、`FundPool`、`FundPoolPremium`  
> coin| string| 質押幣種  
> duration| string| 固定期限，例如 `1d`、`8h`、`2m`  
> status| string| 產品狀態：`Available`、`SoldOut`、`NotStarted`  
> tieredApyList| array| 分層APY列表（如適用）  
>> min| string| 此層最低金額  
>> max| string| 此層最高金額，`"-1"` 表示無上限  
>> apy| string| 此層APY  
> minStakeAmount| string| 最低質押金額  
> maxStakeAmount| string| 最高質押金額  
> precision| integer| 幣種交易精度  
> subscribeStartAt| string| 訂閱開始時間，毫秒級unix時間戳  
> subscribeEndAt| string| 訂閱結束時間，毫秒級unix時間戳  
> allowEarlyRedemption| boolean| 是否支持提前贖回  
> earlyRedemptionApy| string| 提前贖回時適用的折扣APY  
> redemptionLimitDuration| string| 允許提前贖回前的最短持有時間，例如 `1d`、`8h`、`2m`  
> allowAutoReinvest| boolean| 是否支持自動續投  
> interestCoinApyList| array| 多幣種獎勵APY列表  
>> coin| string| 獎勵幣種  
>> apy| string| 獎勵APY  
>> expectUnitEarning| string| 每單位投資預期獎勵（受獎勵幣種現貨價格影響）  
>> currentPrice| string| 獎勵幣種當前價格  
> isVip| boolean| 是否為VIP專屬產品  
> creditTime| string| 預計收益到賬時間，毫秒級unix時間戳  
> specialUserGroupRequired| boolean| 是否限制特定用戶群體購買  
> specialUserGroupInfo| string| 限制用戶群體的描述  
  
* * *

### 請求示例
    
    
    GET /v5/earn/fixed-term/product?coin=BTC HTTP/1.1  
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
                    "productId": "427",  
                    "category": "FixedTermSaving",  
                    "coin": "USDT",  
                    "duration": "30d",  
                    "status": "Available",  
                    "tieredApyList": [],  
                    "minStakeAmount": "50",  
                    "maxStakeAmount": "10000",  
                    "precision": 4,  
                    "subscribeStartAt": "1686704400000",  
                    "subscribeEndAt": "1909094399000",  
                    "allowEarlyRedemption": false,  
                    "earlyRedemptionApy": "",  
                    "redemptionLimitDuration": "",  
                    "allowAutoReinvest": false,  
                    "interestCoinApyList": [  
                        {  
                            "coin": "USDT",  
                            "apy": "2.50%",  
                            "expectUnitEarning": "0.002",  
                            "currentPrice": "1.00"  
                        }  
                    ],  
                    "isVip": false,  
                    "creditTime": "1778718600000",  
                    "specialUserGroupRequired": false,  
                    "specialUserGroupInfo": ""  
                },  
                {  
                    "productId": "27",  
                    "category": "FundPool",  
                    "coin": "USDT",  
                    "duration": "3d",  
                    "status": "Available",  
                    "tieredApyList": [],  
                    "minStakeAmount": "100",  
                    "maxStakeAmount": "10000",  
                    "precision": 4,  
                    "subscribeStartAt": "1722448800000",  
                    "subscribeEndAt": "0",  
                    "allowEarlyRedemption": true,  
                    "earlyRedemptionApy": "0.30%",  
                    "redemptionLimitDuration": "1d",  
                    "allowAutoReinvest": false,  
                    "interestCoinApyList": [  
                        {  
                            "coin": "USDT",  
                            "apy": "9.99%",  
                            "expectUnitEarning": "0.0008",  
                            "currentPrice": "1.00"  
                        }  
                    ],  
                    "isVip": false,  
                    "creditTime": "1776391500000",  
                    "specialUserGroupRequired": true,  
                    "specialUserGroupInfo": "Limited Offer"  
                },  
                {  
                    "productId": "12",  
                    "category": "FundPoolPremium",  
                    "coin": "USDT",  
                    "duration": "3d",  
                    "status": "Available",  
                    "tieredApyList": [],  
                    "minStakeAmount": "1",  
                    "maxStakeAmount": "300",  
                    "precision": 4,  
                    "subscribeStartAt": "1751500800000",  
                    "subscribeEndAt": "0",  
                    "allowEarlyRedemption": false,  
                    "earlyRedemptionApy": "",  
                    "redemptionLimitDuration": "",  
                    "allowAutoReinvest": false,  
                    "interestCoinApyList": [  
                        {  
                            "coin": "USDT",  
                            "apy": "19.70%",  
                            "expectUnitEarning": "0.0016",  
                            "currentPrice": "1.00"  
                        }  
                    ],  
                    "isVip": true,  
                    "creditTime": "1776391200000",  
                    "specialUserGroupRequired": false,  
                    "specialUserGroupInfo": ""  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1776067553433  
    }