---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/finance/advanced-earn/smart-lvg/product-info
api_type: REST
updated_at: 2026-07-14 18:53:05.339059
---

# Dual Asset Offers

### WebSocket public URL

  * **Mainnet:**  
Earn: `wss://stream.bybit.com/v5/public/fp`  


  * **Testnet:**  
Earn: `wss://stream-testnet.bybit.com/v5/public/fp`  





### Desc

  * Subscribe to the `earn.dualassets.offers` topic to receive real-time quote updates for all online Dual Assets products.

  * Push scope: **Full snapshot of all online product quotes**

  * Recommended usage pattern:

    1. Call [Get Product Quote](/docs/v5/finance/advanced-earn/dual-asset/product-quote) to get initial quotes
    2. Subscribe to the WebSocket topic for real-time updates
    3. Use the latest selectPrice + apyE8 from WebSocket when placing orders
    4. If WebSocket disconnects, fallback to the REST endpoint 



### Topic: `earn.dualassets.offers`

### Response Parameters

Parameter| Type| Comments  
---|---|---  
topic| string| Topic name  
data| array| Object  
> p| int64| Product ID  
> c| string| Current price  
> b| array of objects| Buy low price list  
>> s| string| Selected price  
>> a| int64| Annualized yield, e8 precision  
>> m| string| Max investment amount at this price point  
>> x| string| Quote expiration time,Unix timestamp in ms  
> s| array of objects| Sell high price list  
>> s| string| Selected price  
>> a| int64| Annualized yield, e8 precision  
>> m| string| Max investment amount at this price point  
>> x| string| Quote expiration time,Unix timestamp in ms  
  
### Subscribe Example
    
    
    {  
        "op": "subscribe",  
        "args": [  
            "earn.dualassets.offers"  
        ]  
    }  
    

### Stream Example
    
    
    {  
      "topic": "earn.dualassets.offers",  
      "data": [  
        {  
          "p": "36352",  
          "c": "74168.46",  
          "b": [  
            {  
              "s": "74142",  
              "a": "979209000",  
              "m": "2000",  
              "x": "1773825237781"  
            }  
          ],  
          "s": [  
            {  
              "s": "74142",  
              "a": "979209000",  
              "m": "0.02697492",  
              "x": "1773825237781"  
            }  
          ]  
        },  
        {  
          "p": "36382",  
          "c": "74168.46",  
          "b": [  
            {  
              "s": "74142",  
              "a": "890190000",  
              "m": "2000",  
              "x": "1773825237781"  
            }  
          ],  
          "s": [  
            {  
              "s": "74142",  
              "a": "890190000",  
              "m": "0.02697492",  
              "x": "1773825237781"  
            }  
          ]  
        }  
      ]  
    }

---

# 雙幣投資報價

### WebSocket URL

  * **主網 (Mainnet):**  
理財 (Earn): `wss://stream.bybit.com/v5/public/fp`  


  * **測試網 (Testnet):**  
理財 (Earn): `wss://stream-testnet.bybit.com/v5/public/fp`  





### 描述 (Desc)

  * 訂閱 `earn.dualassets.offers` 主題，以接收所有上線雙幣投資產品的即時報價更新。

  * 推播範圍：**所有上線產品報價的完整快照**

  * 建議使用方式：

    1. 使用 [獲取產品報價](/docs/zh-TW/v5/finance/advanced-earn/dual-asset/product-quote) 以獲取初始報價
    2. 訂閱 WebSocket 主題以獲取即時更新
    3. 下單時，請使用來自 WebSocket 的最新 selectPrice 與 apyE8
    4. 若 WebSocket 斷線，請改用 REST 介面 (fallback)



### 主題 (Topic): `earn.dualassets.offers`

### 回應參數

參數| 類型| 說明  
---|---|---  
topic| string| 主題名稱  
data| array| 列表  
> p| int64| 產品 ID  
> c| string| 當前價格  
> b| array of objects| 低買價格列表  
>> s| string| 所選價格  
>> a| int64| 年化收益率，e8 精度  
>> m| string| 該價位的最大投資金額  
>> x| string| 報價過期時間，Unix 時間戳 (毫秒)  
> s| array of objects| 高賣價格列表  
>> s| string| 所選價格  
>> a| int64| 年化收益率，e8 精度  
>> m| string| 該價位的最大投資金額  
>> x| string| 報價過期時間，Unix 時間戳 (毫秒)  
  
### 訂閱範例
    
    
    {  
        "op": "subscribe",  
        "args": [  
            "earn.dualassets.offers"  
        ]  
    }  
    

### 推播範例
    
    
    {  
      "topic": "earn.dualassets.offers",  
      "data": [  
        {  
          "p": "36352",  
          "c": "74168.46",  
          "b": [  
            {  
              "s": "74142",  
              "a": "979209000",  
              "m": "2000",  
              "x": "1773825237781"  
            }  
          ],  
          "s": [  
            {  
              "s": "74142",  
              "a": "979209000",  
              "m": "0.02697492",  
              "x": "1773825237781"  
            }  
          ]  
        },  
        {  
          "p": "36382",  
          "c": "74168.46",  
          "b": [  
            {  
              "s": "74142",  
              "a": "890190000",  
              "m": "2000",  
              "x": "1773825237781"  
            }  
          ],  
          "s": [  
            {  
              "s": "74142",  
              "a": "890190000",  
              "m": "0.02697492",  
              "x": "1773825237781"  
            }  
          ]  
        }  
      ]  
    }