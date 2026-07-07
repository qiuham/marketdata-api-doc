---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/finance/earn/easy-onchain/hourly-yield
api_type: REST
updated_at: 2026-07-07 19:12:38.499762
---

# Get Staked Position

info

API key needs "Earn" permission

note

For Flexible Saving, fully redeemed position is also returned in the response For Onchain, only active position will be returned in the response

### HTTP Request

GET`/v5/earn/position`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
category| **true**|  string| `FlexibleSaving`,`OnChain`  
productId| false| string| Product ID  
coin| false| string| Coin name  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
list| array| Object  
> coin| string| Coin name  
> productId| string| Product ID  
> amount| string| Total staked amount  
> totalPnl| string| Return the profit of the current position. Only has value in Onchain non-LST mode  
> claimableYield| string| Yield accrues on an hourly basis and is distributed at 00:30 UTC daily. If you unstake your assets before yield distribution, any undistributed yield will be credited to your account along with your principal. Onchain products do not return values  
> id| string| Position Id. Only for Onchain  
> status| string| `Processing`,`Active`. Only for Onchain  
> orderId| string| Order Id. Only for Onchain  
> estimateRedeemTime| string| Estimate redeem time, in milliseconds. Only for Onchain  
> estimateStakeTime| string| Estimate stake time, in milliseconds. Only for Onchain  
> estimateInterestCalculationTime| string| Estimated Interest accrual time, in milliseconds. Only for Onchain  
> settlementTime| string| Settlement time, in milliseconds. Only has value for Onchain `Fixed` product  
> autoReinvest| string| Auto-reinvest status. `Enable`: enabled, `Disable`: disabled. See [Modify Position](/docs/v5/finance/earn/easy-onchain/modify-position)  
> availableAmount| string| Redeemable amount  
> freezeDetails| array| Freeze detail list  
>> amount| string| Frozen amount  
>> description| string| Reason for freeze  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/earn/position?category=FlexibleSaving&coin=USDT HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1739944576277  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_staked_position(  
        category="FlexibleSaving",  
        coin="USDT",  
    ))  
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "list": [  
                {  
                    "coin": "BTC",  
                    "productId": "8",  
                    "amount": "0.1",  
                    "totalPnl": "0.000027397260273973",  
                    "claimableYield": "0",  
                    "id": "326",  
                    "status": "Active",  
                    "orderId": "1a5a8945-e042-4dd5-a93f-c0f0577377ad",  
                    "estimateRedeemTime": "",  
                    "estimateStakeTime": "",  
                    "estimateInterestCalculationTime": "1744243200000",  
                    "settlementTime": "1744675200000",  
                    "autoReinvest": "Enable",  
                    "availableAmount": "4900",  
                    "freezeDetails": [  
                        {  
                            "amount": "100",  
                            "description": "Locked in Fixed-Rate Loan"  
                        }  
                    ]  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1739944577575  
    }

---

# 查詢理財持倉

信息

API key需要"理財""權限

備註

對於活期儲蓄，返回訊息裡也返回完全贖回的部分 對於鏈上賺幣，返回訊息中僅返回當前的部分

### HTTP 請求

GET`/v5/earn/position`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
category| **true**|  string| 產品類別：`FlexibleSaving`,`OnChain`  
productId| false| string| 持倉對應的產品 ID  
coin| false| string| 幣種名稱  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
list| array| Object  
> coin| string| 幣種名稱  
> productId| string| 持倉對應的產品 ID  
> amount| string| 持倉金額  
> totalPnl| string| 持倉總收益。僅在 OnChain 非 LST 模式下有價值  
> claimableYield| string| 收益按小時累計，並於每天 UTC 時間 00:30 分發。如果您在收益分配之前取消質押資產，任何未分配的收益將與您的本金一起記入您的帳戶。  
> id| string| 持倉ID. 僅適用於 OnChain  
> status| string| `Processing`,`Active`. 僅適用於 OnChain  
> orderId| string| 訂單編號. 僅適用於 OnChain  
> estimateRedeemTime| string| 預計贖回時間。以毫秒為單位.僅適用於 OnChain  
> estimateStakeTime| string| 預計質押時間。以毫秒為單位.僅適用於 OnChain  
> estimateInterestCalculationTime| string| 預計計息時間。以毫秒為單位.僅適用於 OnChain  
> settlementTime| string| 結算時間。以毫秒為單位.僅對 OnChain `Fixed`產品有價值  
> autoReinvest| string| 自動複投狀態。`Enable`：已開啟，`Disable`：已關閉。參考 [修改持倉設置](/docs/zh-TW/v5/finance/earn/easy-onchain/modify-position)  
> availableAmount| string| 可贖回金額  
> freezeDetails| array| 凍結明細列表  
>> amount| string| 凍結金額  
>> description| string| 凍結原因  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/earn/position?category=FlexibleSaving&coin=USDT HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1739944576277  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_staked_position(  
        category="FlexibleSaving",  
        coin="USDT",  
    ))  
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "list": [  
                {  
                    "coin": "BTC",  
                    "productId": "8",  
                    "amount": "0.1",  
                    "totalPnl": "0.000027397260273973",  
                    "claimableYield": "0",  
                    "id": "326",  
                    "status": "Active",  
                    "orderId": "1a5a8945-e042-4dd5-a93f-c0f0577377ad",  
                    "estimateRedeemTime": "",  
                    "estimateStakeTime": "",  
                    "estimateInterestCalculationTime": "1744243200000",  
                    "settlementTime": "1744675200000",  
                    "autoReinvest": "Enable",  
                    "availableAmount": "4900",  
                    "freezeDetails": [  
                        {  
                            "amount": "100",  
                            "description": "Locked in Fixed-Rate Loan"  
                        }  
                    ]  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1739944577575  
    }