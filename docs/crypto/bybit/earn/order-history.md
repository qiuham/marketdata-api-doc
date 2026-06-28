---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/earn/order-history
api_type: REST
updated_at: 2026-01-16T09:39:16.618192
---

# Get Stake/Redeem Order History

info

API key needs "Earn" permission

### HTTP Request

GET `/v5/earn/order`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
category| **true**|  string| `FlexibleSaving`,`OnChain`   
**Remarks** : currently, only flexible savings and OnChain is supported  
orderId| false| string| Order ID. 
* For category = `OnChain`, either orderId or orderLinkId is **required**
* if both are passed, make sure they're matched, otherwise returning empty result  
orderLinkId| false| string| Order link ID  
**Remarks** : Always return the latest one if order link id is ever reused when querying by orderLinkId only  
productId| false| string| Product ID  
startTime| false| integer| The start timestamp (ms).
* 1\. If both are not provided, the default is to return data from the last 7 days.
* 2\. If both are provided, the difference between the endTime and startTime must be less than or equal to 7 days.   
endTime| false| integer| The endTime timestamp (ms)  
limit| false| integer| Limit for data size per page. Range: [1, 100]. Default: 50  
cursor| false| string| Cursor, use the returned `nextPageCursor` to query data for the next page.  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
nextPageCursor| string| Refer to the `cursor` request parameter  
list| array| Object  
> coin| string| Coin name  
> orderValue| string| amount  
> orderType| string| `Redeem`, `Stake`  
> orderId| string| Order ID  
> orderLinkId| string| Order link ID  
> status| string| Order status `Success`, `Fail`, `Pending`  
> createdAt| string| Order created time, in milliseconds  
> productId| string| Product ID  
> updatedAt| string| Order updated time, in milliseconds  
> swapOrderValue| string| Swap order value. Only for LST Onchain.  
> estimateRedeemTime| string| Estimate redeem time, in milliseconds. Only for Onchain  
> estimateStakeTime| string| Estimate stake time, in milliseconds. Only for Onchain  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/earn/order?orderId=9640dc23-df1a-448a-ad24-e1a48028a51f&category=OnChain HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1739937044221  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_stake_or_redemption_history(  
        category="OnChain",  
        orderId="9640dc23-df1a-448a-ad24-e1a48028a51f",  
    ))  
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "list": [  
                {  
                    "coin": "USDT",  
                    "orderValue": "1000",  
                    "orderType": "Stake",  
                    "orderId": "ad98d473-4e17-46da-ab30-5563f62a97fa",  
                    "orderLinkId": "",  
                    "status": "Success",  
                    "createdAt": "1759983689000",  
                    "productId": "428",  
                    "updatedAt": "1759983689000",  
                    "swapOrderValue": "",  
                    "estimateRedeemTime": "",  
                    "estimateStakeTime": ""  
                }  
            ],  
            "nextPageCursor": ""  
        },  
        "retExtInfo": {},  
        "time": 1759983699446  
    }

---

# 查詢質押/贖回訂單歷史

信息

API key需要"理財""權限

### HTTP 請求

GET `/v5/earn/order`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
category| **true**|  string| `FlexibleSaving`,`OnChain`   
**備註** : 本期僅支持活期理財和鏈上賺幣  
orderId| false| string| 系統生成的訂單ID 
* 對於category = `OnChain`, orderId和orderLinkId二者 _必須_ 傳其一
* 如果都傳入, 確保二者是來自同一筆訂單, 否則返回空  
orderLinkId| false| string| 自定義訂單ID  
**備註** : 如果orderLinkId有復用, 則僅用orderLinkId查詢時, 總是返回最近的那筆訂單  
productId| false| string| 產品ID  
startTime| false| integer| 開始時間戳 (毫秒)

  * startTime 和 endTime都不傳入, 則默認返回最近7天的數據
  * startTime 和 endTime都傳入的話, 則確保endTime - startTime <= 7天

  
endTime| false| integer| 結束時間戳 (毫秒)  
limit| false| integer| 每頁數量限制. [`1`, `100`]. 默認: `50`  
cursor| false| string| 游標，用於翻頁  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
nextPageCursor| string| 游標，用於翻頁  
list| array| Object  
> coin| string| 幣種名稱  
> orderValue| string| 質押/贖回數量  
> orderType| string| `Redeem`, `Stake`  
> orderId| string| 系統生成的訂單ID  
> orderLinkId| string| 自定義訂單ID  
> status| string| 訂單狀態 `Success`, `Fail`, `Pending`  
> createdAt| string| 訂單創建時間 (毫秒)  
> productId| string| 產品ID  
> updatedAt| string| 訂單更新時間 (毫秒)  
> swapOrderValue| string| 到手金額. 僅適用於 LST OnChain  
> estimateRedeemTime| string| 預計贖回時間 毫秒級（只有贖回訂單展示）. 僅適用於 OnChain  
> estimateStakeTime| string| 預計質押時間 毫秒級（只有質押訂單展示）.僅適用於 OnChain  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/earn/order?orderId=0572b030-6a0b-423f-88c4-b6ce31c0c82d&category=FlexibleSaving HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1739937044221  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_stake_or_redemption_history(  
        category="FlexibleSaving",  
        orderId="0572b030-6a0b-423f-88c4-b6ce31c0c82d",  
    ))  
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "list": [  
                {  
                    "coin": "USDT",  
                    "orderValue": "1000",  
                    "orderType": "Stake",  
                    "orderId": "ad98d473-4e17-46da-ab30-5563f62a97fa",  
                    "orderLinkId": "",  
                    "status": "Success",  
                    "createdAt": "1759983689000",  
                    "productId": "428",  
                    "updatedAt": "1759983689000",  
                    "swapOrderValue": "",  
                    "estimateRedeemTime": "",  
                    "estimateStakeTime": ""  
                }  
            ],  
            "nextPageCursor": ""  
        },  
        "retExtInfo": {},  
        "time": 1759983796197  
    }