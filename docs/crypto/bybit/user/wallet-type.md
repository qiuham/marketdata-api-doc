---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/user/wallet-type
api_type: REST
updated_at: 2026-07-01 19:33:09.550139
---

# Fast Execution

Fast execution stream significantly reduces data latency compared original "execution" stream. However, it pushes limited execution type of trades, and fewer data fields.

**All-In-One Topic:** `execution.fast`  
**Categorised Topic:** `execution.fast.linear`, `execution.fast.inverse`, `execution.fast.spot`, `execution.fast.option`  


info

  * Supports all Perps, Futures, Spot and Options exceution
  * You can only receive [execType](/docs/v5/enum#exectype)=Trade update



### Response Parameters

Parameter| Type| Comments  
---|---|---  
topic| string| Topic name  
creationTime| number| Data created timestamp (ms)  
data| array| Object  
> [category](/docs/v5/enum#category)| string| Product type `linear`, `inverse`, `spot`, `option`  
> symbol| string| Symbol name  
> orderId| string| Order ID  
> isMaker| boolean| `true`: Maker, `false`: Taker  
> orderLinkId| string| User customized order ID 

  * maker trade is always `""`
  * If a maker order in the orderbook is converted to taker (by price amend), orderLinkId is also `""`
  * For option: maker trade is always `""`, taker trade is always orderLinkId

  
> execId| string| Execution ID  
> execPrice| string| Execution price  
> execQty| string| Execution qty  
> side| string| Side. `Buy`,`Sell`  
> execTime| string| Executed timestamp (ms)  
> seq| long| Cross sequence, used to associate each fill and each position update

  * The seq will be the same when conclude multiple transactions at the same time
  * Different symbols may have the same seq, please use seq + symbol to check unique

  
  
### Subscribe Example
    
    
    {  
        "op": "subscribe",  
        "args": [  
            "execution.fast"  
        ]  
    }  
    

### Stream Example
    
    
    {  
        "topic": "execution.fast",  
        "creationTime": 1716800399338,  
        "data": [  
            {  
                "category": "linear",  
                "symbol": "ICPUSDT",  
                "execId": "3510f361-0add-5c7b-a2e7-9679810944fc",  
                "execPrice": "12.015",  
                "execQty": "3000",  
                "orderId": "443d63fa-b4c3-4297-b7b1-23bca88b04dc",  
                "isMaker": false,  
                "orderLinkId": "test-00001",  
                "side": "Sell",  
                "execTime": "1716800399334",  
                "seq": 34771365464  
            }  
        ]  
    }

---

# 個人成交 (Fast)

精簡版本的個人成交推送, 相比原始的快速成交流, 延遲更加低

提示

  * 支持USDT永續, USDC永續, USDC交割, 反向永續, 反向交割, 現貨和期權的成交推送
  * 僅推送[execType](/docs/zh-TW/v5/enum#exectype)=Trade的消息



**All-In-One Topic:** `execution.fast`  
**Categorised Topic:** `execution.fast.linear`, `execution.fast.inverse`, `execution.fast.spot`, `execution.fast.option`  


### 響應參數

參數| 類型| 說明  
---|---|---  
topic| string| Topic名  
creationTime| number| 消息數據創建時間  
data| array| Object  
> [category](/docs/zh-TW/v5/enum#category)| string| 產品類型 `linear`, `inverse`, `spot`, `option`  
> symbol| string| 合約名稱  
> orderId| string| 訂單ID  
> isMaker| boolean| `true`: maker成交, `false`: taker成交  
> orderLinkId| string| 用戶自定義訂單ID 

  * maker成交總是返回`""`
  * 當maker訂單在訂單簿中轉化成了taker單(比如修改了價格), 這種情況orderLinkId也是`""`
  * 期權: maker成交永遠返回`""`, taker成交永遠返回orderLinkId

  
> side| string| 訂單方向.買：`Buy`,賣：`Sell`  
> execId| string| 成交Id  
> execPrice| string| 成交價格  
> execQty| string| 成交數量  
> execTime| string| 成交時間（毫秒）  
> seq| long| 序列號, 用於關聯成交和倉位的更新

  * 同一時間有多筆成交, seq相同
  * 不同的幣對會存在相同seq, 可以使用seq + symbol來做唯一性識別

  
  
### 訂閱示例
    
    
    {  
        "op": "subscribe",  
        "args": [  
            "execution.fast"  
        ]  
    }  
    
    
    
      
    

### 推送示例
    
    
    {  
        "topic": "execution.fast",  
        "creationTime": 1716800399338,  
        "data": [  
            {  
                "category": "linear",  
                "symbol": "ICPUSDT",  
                "execId": "3510f361-0add-5c7b-a2e7-9679810944fc",  
                "execPrice": "12.015",  
                "execQty": "3000",  
                "orderId": "443d63fa-b4c3-4297-b7b1-23bca88b04dc",  
                "isMaker": false,  
                "orderLinkId": "test-00001",  
                "side": "Sell",  
                "execTime": "1716800399334",  
                "seq": 34771365464  
            }  
        ]  
    }