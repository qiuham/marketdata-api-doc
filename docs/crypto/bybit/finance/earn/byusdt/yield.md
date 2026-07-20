---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/finance/earn/byusdt/yield
api_type: REST
updated_at: 2026-07-20 19:10:01.889009
---

# Get Coupon List

info

  * Authentication required.
  * **Rate Limit:** 10 req/s (UID)



Query the user's interest-rate coupons (`interestCards`) and Dual Assets reward cards (`awardCards`, e.g. trial funds / zero-cost vouchers) for the given product category.

Returned cards include all states: `InUse`, `NotUse`, `Expired`, and `AlreadyUsed`.

To apply a coupon when placing an order, pass its `awardId` and `specCode` in the `interestCard` field of the corresponding place-order request:

  * `FlexibleSaving` → [Place Order](/docs/v5/finance/earn/easy-onchain/create-order)
  * `DualAssets` → [Place Order](/docs/v5/finance/advanced-earn/dual-asset/create-order)



### HTTP Request

GET`/v5/earn/coupons`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
category| **true**|  string| Product category: `FlexibleSaving`, `DualAssets`  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
interestCards| array| Interest-rate coupon list  
> awardId| integer| Coupon unique ID  
> specCode| string| Coupon spec code  
> coin| string| Coin name, e.g. `USDT`, `BTC`  
> apy| string| Bonus APY rate as a decimal string, e.g. `"0.03"` = 3%  
> duration| integer| Coupon validity period (days)  
> claimedAt| integer| Claim time (Unix seconds)  
> expireAt| integer| Expiry time (Unix seconds)  
> usedAt| integer| Use time (Unix seconds); `0` if not yet used  
> status| string| Coupon status. `InUse`: currently in use, `NotUse`: claimed but not yet used, `Expired`: expired without being used, `AlreadyUsed`: used and settled  
> currentPnl| string| Bonus interest accrued so far  
> limitPnl| string| Bonus interest cap  
> positionEffectiveAmount| string| Effective principal amount for the bonus calculation  
> productId| integer| Linked product ID; populated for `InUse` / `AlreadyUsed`, `0` otherwise  
> category| string| Product category the coupon applies to: `FlexibleSaving`, `DualAssets`  
awardCards| array| Dual Assets reward card list (trial fund / zero-cost voucher)  
> awardId| integer| Reward card unique ID  
> specCode| string| Reward card spec code  
> claimedAt| integer| Claim time (Unix seconds)  
> usedAt| integer| Use time (Unix seconds); `0` if not yet used  
> expireAt| integer| Expiry time (Unix seconds)  
> status| string| Card status. Same semantics as `interestCards > status`  
> amount| string| Trial / zero-cost voucher amount  
> limitPnlPercentage| string| PnL percentage cap, e.g. `"0.23"` = 23%  
> baseCoin| string| Base coin name  
> quoteCoin| string| Quote coin name  
> direction| integer| Dual Assets direction: `1` = BuyLow, `2` = SellHigh  
> category| string| Product category the card applies to: `FlexibleSaving`, `DualAssets`  
  
* * *

### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/earn/coupons?category=FlexibleSaving HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1759983699446  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
      
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "interestCards": [  
                {  
                    "awardId": 1001,  
                    "specCode": "FS_APY_3PCT_30D",  
                    "coin": "USDT",  
                    "apy": "0.03",  
                    "duration": 30,  
                    "claimedAt": 1759900800,  
                    "expireAt": 1762492800,  
                    "usedAt": 0,  
                    "status": "NotUse",  
                    "currentPnl": "0",  
                    "limitPnl": "100",  
                    "positionEffectiveAmount": "0",  
                    "productId": 0,  
                    "category": "FlexibleSaving"  
                }  
            ],  
            "awardCards": []  
        },  
        "retExtInfo": {},  
        "time": 1759983699446  
    }

---

# 查詢優惠券列表

信息

  * 需要身份驗證。
  * **頻率限制：** 10 次/秒（UID）



查詢用戶在指定產品類別下的利率優惠券（`interestCards`）和雙幣投資獎勵卡（`awardCards`，如體驗金/零成本券）。

返回所有狀態的卡券：`InUse`（使用中）、`NotUse`（未使用）、`Expired`（已過期）、`AlreadyUsed`（已使用）。

下單時如需使用優惠券，請在對應下單請求的 `interestCard` 字段中傳入 `awardId` 和 `specCode`：

  * `FlexibleSaving` → [下單](/docs/zh-TW/v5/finance/earn/easy-onchain/create-order)
  * `DualAssets` → [下單](/docs/zh-TW/v5/finance/advanced-earn/dual-asset/create-order)



### HTTP 請求

GET`/v5/earn/coupons`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
category| **true**|  string| 產品類別：`FlexibleSaving`、`DualAssets`  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
interestCards| array| 利率優惠券列表  
> awardId| integer| 優惠券唯一ID  
> specCode| string| 優惠券規格碼  
> coin| string| 幣種名稱，如 `USDT`、`BTC`  
> apy| string| 加成APY（小數字符串），如 `"0.03"` = 3%  
> duration| integer| 優惠券有效期（天）  
> claimedAt| integer| 領取時間（Unix秒）  
> expireAt| integer| 到期時間（Unix秒）  
> usedAt| integer| 使用時間（Unix秒）；未使用時為 `0`  
> status| string| 狀態。`InUse`：使用中，`NotUse`：未使用，`Expired`：已過期，`AlreadyUsed`：已使用  
> currentPnl| string| 已累計加成利息  
> limitPnl| string| 加成利息上限  
> positionEffectiveAmount| string| 計算加成的有效本金  
> productId| integer| 關聯產品ID；`InUse`/`AlreadyUsed` 時有值，否則為 `0`  
> category| string| 優惠券適用的產品類別：`FlexibleSaving`、`DualAssets`  
awardCards| array| 雙幣投資獎勵卡列表（體驗金/零成本券）  
> awardId| integer| 獎勵卡唯一ID  
> specCode| string| 獎勵卡規格碼  
> claimedAt| integer| 領取時間（Unix秒）  
> usedAt| integer| 使用時間（Unix秒）；未使用時為 `0`  
> expireAt| integer| 到期時間（Unix秒）  
> status| string| 狀態，語義同 `interestCards > status`  
> amount| string| 體驗金/零成本券金額  
> limitPnlPercentage| string| 收益上限比例，如 `"0.23"` = 23%  
> baseCoin| string| 標的幣種  
> quoteCoin| string| 計價幣種  
> direction| integer| 雙幣方向：`1` = 低買（BuyLow），`2` = 高賣（SellHigh）  
> category| string| 獎勵卡適用的產品類別：`FlexibleSaving`、`DualAssets`  
  
* * *

### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/earn/coupons?category=FlexibleSaving HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1759983699446  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
      
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "interestCards": [  
                {  
                    "awardId": 1001,  
                    "specCode": "FS_APY_3PCT_30D",  
                    "coin": "USDT",  
                    "apy": "0.03",  
                    "duration": 30,  
                    "claimedAt": 1759900800,  
                    "expireAt": 1762492800,  
                    "usedAt": 0,  
                    "status": "NotUse",  
                    "currentPnl": "0",  
                    "limitPnl": "100",  
                    "positionEffectiveAmount": "0",  
                    "productId": 0,  
                    "category": "FlexibleSaving"  
                }  
            ],  
            "awardCards": []  
        },  
        "retExtInfo": {},  
        "time": 1759983699446  
    }