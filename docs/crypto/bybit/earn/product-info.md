---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/earn/product-info
api_type: REST
updated_at: 2026-01-16T09:39:16.747144
---

# Get Product Info

info

Does not need authentication.

[Bybit Saving FAQ](https://www.bybit.com/en/help-center/article/FAQ-Bybit-Savings)

### HTTP Request

GET `/v5/earn/product`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
category| **true**|  string| `FlexibleSaving`,`OnChain`  
**Remarks** : currently, only flexible savings and on chain is supported  
coin| false| string| Coin name, uppercase only  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
list| array| Object  
> category| string| `FlexibleSaving`,`OnChain`  
> estimateApr| string| Estimated APR, e.g., `3%`, `4.25%`  
**Remarks** : 1)The Est. APR provides a dynamic preview of your potential returns, updated every 10 minutes in response to market conditions.   
2) Please note that this is an estimate and may differ from the actual APR you will receive.  
3) Platform Reward APRs are not shown  
> coin| string| Coin name  
> minStakeAmount| string| Minimum stake amount  
> maxStakeAmount| string| Maximum stake amount  
> precision| string| Amount precision  
> productId| string| Product ID  
> status| string| `Available`, `NotAvailable`  
> bonusEvents| Array| Bonus  
>> apr| string| Yesterday's Rewards APR  
>> coin| string| Reward coin  
>> announcement| string| Announcement link  
> minRedeemAmount| string| Minimum redemption amount. Only has value in Onchain LST mode  
> maxRedeemAmount| string| Maximum redemption amount. Only has value in Onchain LST mode  
> duration| string| `Fixed`,`Flexible`. Product Type  
> term| int| Unit: Day. Only when duration = `Fixed` for OnChain  
> swapCoin| string| swap coin. Only has value in Onchain LST mode  
> swapCoinPrecision| string| swap coin precision. Only has value in Onchain LST mode  
> stakeExchangeRate| string| Estimated stake exchange rate. Only has value in Onchain LST mode  
> redeemExchangeRate| string| Estimated redeem exchange rate. Only has value in Onchain LST mode  
> rewardDistributionType| string| `Simple`: Simple interest, `Compound`: Compound interest, `Other`: LST. Only has value for Onchain  
> rewardIntervalMinute| int| Frequency of reward distribution (minutes)  
> redeemProcessingMinute| string| Estimated redemption minutes  
> stakeTime| string| Staking on-chain time, in milliseconds  
> interestCalculationTime| string| Interest accrual time, in milliseconds  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/earn/product?category=FlexibleSaving&coin=BTC HTTP/1.1  
    Host: api-testnet.bybit.com  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
    )  
    print(session.get_earn_product_info(  
        category="FlexibleSaving",  
        coin="BTC",  
    ))  
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "list": [  
                {  
                    "category": "FlexibleSaving",  
                    "estimateApr": "3%",  
                    "coin": "BTC",  
                    "minStakeAmount": "0.001",  
                    "maxStakeAmount": "10",  
                    "precision": "8",  
                    "productId": "430",  
                    "status": "Available",  
                    "bonusEvents": [],  
                    "minRedeemAmount": "",  
                    "maxRedeemAmount": "",  
                    "duration": "",  
                    "term": 0,  
                    "swapCoin": "",  
                    "swapCoinPrecision": "",  
                    "stakeExchangeRate": "",  
                    "redeemExchangeRate": "",  
                    "rewardDistributionType": "",  
                    "rewardIntervalMinute": 0,  
                    "redeemProcessingMinute": 0,  
                    "stakeTime": "",  
                    "interestCalculationTime": ""  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1739935669110  
    }

---

# 查询产品信息

信息

不需要鑒權

[Bybit儲蓄 - 常見問題](https://www.bybit.com/zh-TW/help-center/article/FAQ-Bybit-Savings)

### HTTP 請求

GET `/v5/earn/product`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
category| **true**|  string| `FlexibleSaving`,`OnChain`   
**備註** : 本期僅支持活期理財和鏈上賺幣  
coin| false| string| 幣種名稱  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
list| array| Object  
> category| string| `FlexibleSaving`,`OnChain`  
> estimateApr| string| 預估年化利率, e.g., `3%`, `4.25%`  
**備註** : 1)預估年化收益率提供潛在收益的動態預覽，根據市場行情每 10 分鐘更新一次.   
2) 請注意，該數值僅為估算值，可能會與您獲得的實際年化收益率有所不同.  
3) 不展示部分幣種支持的平台獎勵年化收益率  
> coin| string| 幣種名稱  
> minStakeAmount| string| 最小質押額  
> maxStakeAmount| string| 最大質押額  
> precision| string| 金額的精度  
> productId| string| 產品ID  
> status| string| 產品狀態 `Available`, `NotAvailable`  
> bonusEvents| Array| 獎勵  
>> apr| string| 昨日獎勵 APR  
>> coin| string| 獎勵幣種  
>> announcement| string| 公告連結  
> minRedeemAmount| string| 最小贖回額度. 只有 OnChain LST 模式有值  
> maxRedeemAmount| string| 最大押額度 （返回可購買金額）. 只有 OnChain LST 模式有值  
> duration| string| 產品類型：`Fixed`,`Flexible`.  
> term| int| 單位：天。只有 OnChain 定期產品類型使用  
> swapCoin| string| 兌換幣種. 只有 OnChain LST 模式有值  
> swapCoinPrecision| string| 贖回可支援的精確度. 只有 OnChain LST 模式有值  
> stakeExchangeRate| string| 預計質押兌換率. 只有 OnChain LST 模式有值  
> redeemExchangeRate| string| 預計赎回兑换率. 只有 OnChain LST 模式有值  
> rewardDistributionType| string| 收益發放模式：`Simple`: 单利, `Compound`: 复利, `Other`: LST. 只有 OnChain 模式有值  
> rewardIntervalMinute| int| 收益發放的頻率（分鐘）  
> redeemProcessingMinute| string| 預計贖回分鐘  
> stakeTime| string| 質押上鍊時間. 以毫秒為單位  
> interestCalculationTime| string| 開始計息時間. 以毫秒為單位  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/earn/product?category=FlexibleSaving&coin=BTC HTTP/1.1  
    Host: api-testnet.bybit.com  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
    )  
    print(session.get_earn_product_info(  
        category="FlexibleSaving",  
        coin="BTC",  
    ))  
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "list": [  
                {  
                    "category": "FlexibleSaving",  
                    "estimateApr": "0.3%",  
                    "coin": "BTC",  
                    "minStakeAmount": "0.001",  
                    "maxStakeAmount": "200",  
                    "precision": "8",  
                    "productId": "3",  
                    "status": "Available",  
                    "bonusEvents": [],  
                    "minRedeemAmount": "",  
                    "maxRedeemAmount": "",  
                    "duration": "",  
                    "term": 0,  
                    "swapCoin": "",  
                    "swapCoinPrecision": "",  
                    "stakeExchangeRate": "",  
                    "redeemExchangeRate": "",  
                    "rewardDistributionType": "",  
                    "rewardIntervalMinute": 0,  
                    "redeemProcessingMinute": 0,  
                    "stakeTime": "",  
                    "interestCalculationTime": ""  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1739935669110  
    }