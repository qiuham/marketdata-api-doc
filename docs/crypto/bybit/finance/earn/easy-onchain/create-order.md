---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/finance/earn/easy-onchain/create-order
api_type: REST
updated_at: 2026-11-13 19:23:12.750192
---

# Stake / Redeem

info

API key needs "Earn" permission, custody accounts are not supported for now

note

In times of high demand for loans in the market for a specific cryptocurrency, the redemption of the principal may encounter delays and is expected to be processed within 48 hours. The redemption of on-chain products may take up to a few days to complete. Once the redemption request is initiated, it cannot be cancelled.

### HTTP Request

POST`/v5/earn/place-order`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
category| **true**|  string| `FlexibleSaving`,`OnChain`   
**Remarks** : currently, only flexible savings and on chain is supported  
orderType| **true**|  string| `Stake`, `Redeem`  
accountType| **true**|  string| `FUND`, `UNIFIED`. Onchain only supports FUND  
amount| **true**|  string| 

  * Stake amount needs to satisfy minStake and maxStake
  * Both stake and redeem amount need to satify precision requirement

  
coin| **true**|  string| Coin name  
productId| **true**|  string| Product ID  
orderLinkId| **true**|  string| Customised order ID, used to prevent from replay

  * support up to 36 characters
  * The same orderLinkId can't be used in 30 mins

  
redeemPositionId| false| string| The position ID that the user needs to redeem. Only is required in Onchain non-LST mode  
toAccountType| false| string| `FUND`, `UNIFIED`. Onchain LST mode supports `FUND` and `UNIFIED`(Private wealth management custodial subaccount only supports `UNIFIED`). Onchain non-LST mode only supports `FUND`  
interestCard| false| Object| Interest bonus card. Only applicable to `FlexibleSaving` `Stake` orders. Obtain `awardId` and `specCode` from [Get Coupon List](/docs/v5/finance/earn/easy-onchain/coupons)  
> awardId| **true**|  int64| Interest bonus card unique ID  
> specCode| **true**|  string| Spec code of the interest bonus card  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
orderId| string| Order ID  
orderLinkId| string| Order link ID  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/earn/place-order HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1739936605822  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 190  
      
    {  
        "category": "FlexibleSaving",  
        "orderType": "Redeem",  
        "accountType": "FUND",  
        "amount": "0.35",  
        "coin": "BTC",  
        "productId": "430",  
        "orderLinkId": "btc-earn-001"  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.stake_or_redeem(  
        category="FlexibleSaving",  
        orderType="Redeem",  
        accountType="FUND",  
        amount="0.35",  
        coin="BTC",  
        productId="430",  
        orderLinkId="btc-earn-001"  
    ))  
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "orderId": "0572b030-6a0b-423f-88c4-b6ce31c0c82d",  
            "orderLinkId": "btc-earn-001"  
        },  
        "retExtInfo": {},  
        "time": 1739936607117  
    }

---

# 質押/贖回

信息

API key需要"理財""權限, 三方託管帳戶暫不支援

備註

在極端情況下，當相應代幣的市場需求極高，本金贖回可能會出現延遲，預計需要 48 小時處理完畢。鏈上賺幣產品的贖回可能需要幾天的時間才能完成。一旦發動贖回請求，不能被取消。

### HTTP 請求

POST`/v5/earn/place-order`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
category| **true**|  string| `FlexibleSaving`,`OnChain`   
**備註** : 本期僅支持活期理財和鏈上賺幣  
orderType| **true**|  string| 訂單類型 `Stake`, `Redeem`  
accountType| **true**|  string| 選擇帳戶類型 `FUND`, `UNIFIED`. OnChain 只支持FUND  
amount| **true**|  string| 

  * 質押數量需要滿足最小/最大質押額
  * 質押和贖回需要滿足幣種精度要求

  
coin| **true**|  string| 幣種名稱  
productId| **true**|  string| 產品ID  
orderLinkId| **true**|  string| 自定義訂單號, 同時用於冪等校驗

  * 支持最長36位字符
  * 30分鐘內無法使用相同的orderLinkId

  
redeemPositionId| false| string| 用戶需要贖回的持倉ID：只有非LST 產品需要在贖回時傳  
toAccountType| false| string| `FUND`, `UNIFIED`. 鏈上賺幣LST模式支持`FUND`和`UNIFIED`（私人理財託管子帳戶僅支持`UNIFIED`）. 鏈上賺幣非LST模式僅支持`FUND`  
interestCard| false| Object| 利率優惠券。僅適用於 `FlexibleSaving` 質押訂單。`awardId` 和 `specCode` 可通過 [查詢優惠券列表](/docs/zh-TW/v5/finance/earn/easy-onchain/coupons) 獲取  
> awardId| **true**|  int64| 利率優惠券唯一ID  
> specCode| **true**|  string| 利率優惠券規格碼  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
orderId| string| Order ID  
orderLinkId| string| Order link ID  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/earn/place-order HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1739936605822  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 190  
      
    {  
        "category": "FlexibleSaving",  
        "orderType": "Redeem",  
        "accountType": "FUND",  
        "amount": "0.35",  
        "coin": "BTC",  
        "productId": "430",  
        "orderLinkId": "btc-earn-001"  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.stake_or_redeem(  
        category="FlexibleSaving",  
        orderType="Redeem",  
        accountType="FUND",  
        amount="0.35",  
        coin="BTC",  
        productId="430",  
        orderLinkId="btc-earn-001"  
    ))  
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "orderId": "0572b030-6a0b-423f-88c4-b6ce31c0c82d",  
            "orderLinkId": "btc-earn-001"  
        },  
        "retExtInfo": {},  
        "time": 1739936607117  
    }