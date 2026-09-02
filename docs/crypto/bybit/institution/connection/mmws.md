---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/institution/connection/mmws
api_type: REST
updated_at: 2026-09-02 18:44:12.866536
---

# Get ADL Alert

Query for [ADL](https://www.bybit.com/en/help-center/article/Auto-Deleveraging-ADL) (auto-deleveraging mechanism) alerts and insurance pool information.

> **Covers: USDT Perpetual / USDT Delivery / USDC Perpetual / USDC Delivery / Inverse Contracts**

tip

Data update frequency: every 1 minute.

info

  * **ADL trigger and stop conditions are based on the following three cases:**


  1. **Contract PnL drawdown ADL (based on the new grouped insurance pool mechanism, see examples 1 and 2)**

     * **Trigger condition** :  
`balance` (insurance fund balance) > `adlTriggerThreshold` (trigger threshold for contract PnL drawdown ADL)  
and `pnlRatio` < `insurancePnlRatio` (PnL ratio threshold for triggering ADL)

Where:

       * **pnlRatio** : drawdown ratio of the symbol in the last 8 hours  
Formula: `pnlRatio` = (Symbol's current PnL - Symbol's 8h max PnL) / Insurance pool's 8h max balance (`maxBalance`)  
_Note: the symbol's Current PnL and 8h Max PnL are not provided by the API_.
       * **Insurance pool 8h max balance (`maxBalance`)**: the maximum balance of the grouped insurance pool in the last 8 hours
     * **Stop condition** : `pnlRatio` > `adlStopRatio` (stop ratio threshold for ADL)

  2. **Insurance pool equity drawdown ADL (original mechanism, see example 3)**

     * **Trigger condition** : `balance` (insurance fund balance) ≤ 0
     * **Stop condition** : `balance` (insurance fund balance) > 0
  3. **Excessive margin loss of a symbol after removing it from a grouped insurance pool (can be regarded as a special case of pool equity drawdown ADL)**

     * To ensure pool safety, the risk control team may remove a symbol from its grouped pool and temporarily establish it as a new independent insurance pool.
     * **Trigger condition** : `balance` (insurance fund balance) ≤ 0
     * **Stop condition** : `balance` (insurance fund balance) > 0



ADL examples: Triggered by PnL Drawdown and Insurance Pool Balance

  1. **Example 1: Pool has no significant profit in the last 8 hours, then symbol loss exceeds the PnL ratio threshold (`insurancePnlRatio`), ADL will be triggered**

     * Assume symbols A, B, and C share the same pool with an initial 8h `balance` of **1M USDT**
     * A incurs a loss of **350K**
     * Calculation:
       * `pnlRatio` = -35%
       * `balance` = 1M
       * `adlTriggerThreshold` = 1 (a constant set by Bybit)
       * `insurancePnlRatio` = -0.3 (a constant set by Bybit)
     * Condition check:
       * `balance` (1M) > `adlTriggerThreshold` (1)
       * `pnlRatio` (-0.35) < `insurancePnlRatio` (-0.3)
     * → Contract PnL drawdown ADL is triggered
     * The system calculates the bankruptcy price at **-30% drawdown** so ADL closes **50K** worth of user positions to keep A's `pnlRatio` at -30%
     * **Stop condition** : ADL stops if A's `pnlRatio` > `adlStopRatio` (-0.25, a constant set by Bybit)

**Recovery methods** :

     1. Platform injects funds into the pool and adjusts A's PnL
     2. Pool continues to take A's positions and earns maintenance margin through liquidation on the market



* * *

  2. **Example 2: Pool has significant profit in the last 8 hours, but symbol loss exceeds the PnL ratio threshold (`insurancePnlRatio`), ADL will still be triggered**

     * Assume symbols A, B, C share the same pool, initial `balance` = **1M USDT**
     * A gains profit through liquidation, pool 8h Max Balance = **2M USDT** (A's PnL = +1M)
     * Later A incurs a loss of **600K**
     * Calculation:
       * `pnlRatio` = -30%
       * `balance` = 2M
       * `adlTriggerThreshold` = 1 (a constant set by Bybit)
       * `insurancePnlRatio` = -0.3 (a constant set by Bybit)
     * Condition check:
       * `balance` (2M) > `adlTriggerThreshold` (1)
       * `pnlRatio` (-0.30) ≤ `insurancePnlRatio` (-0.3)
     * → Contract PnL drawdown ADL is triggered
     * The system calculates the bankruptcy price at **-30% drawdown**
     * **Stop condition** : ADL stops if A's `pnlRatio` > `adlStopRatio` (-0.25, a constant set by Bybit)

**Recovery methods** :

     1. Platform injects funds into the pool and adjusts A's PnL
     2. Pool continues to take A's positions and earns maintenance margin through liquidation on the market



* * *

  3. **Example 3: Pool balance reaches zero which triggers ADL**
     * Assume symbols A, B, C, D share the same pool, initial `balance` = **1M USDT**
     * Although none of the `pnlRatio` values for the symbols reach -30%, the pool `balance` drops to 0
     * Condition check:
       * `balance` (0) ≤ 0
     * → Insurance pool equity ADL is triggered
     * The system redistributes bankruptcy loss across symbols based on their PnL when pool balance = 0
     * **Stop condition** : ADL stops if `balance` > 0



Subscribe to the [ADL WebSocket topic](/docs/v5/websocket/public/adl-alert) for faster updates.

### HTTP Request

GET`/v5/market/adlAlert`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
symbol| false| string| Contract name, e.g. `BTCUSDT`. Uppercase only  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
updateTime| string| Latest data update timestamp (ms)  
list| array| Object  
> coin| string| Token of the insurance pool  
> symbol| string| Trading pair name  
> balance| string| Balance of the insurance fund. Used to determine if ADL is triggered. For shared insurance pool, the "balance" field will follow a T+1 refresh mechanism and will be updated daily at 00:00 UTC.  
> maxBalance| string| Deprecated, always return "". Maximum balance of the insurance pool in the last 8 hours  
> insurancePnlRatio| string| PnL ratio threshold for triggering **contract PnL drawdown ADL**

  * ADL is triggered when the symbol's PnL drawdown ratio in the last 8 hours exceeds this value

  
> pnlRatio| string| Symbol's PnL drawdown ratio in the last 8 hours. Used to determine whether ADL is triggered or stopped  
> adlTriggerThreshold| string| Trigger threshold for **contract PnL drawdown ADL**

  * This condition is only effective when the insurance pool balance is greater than this value; if so, an 8 hours drawdown exceeding n% may trigger ADL

  
> adlStopRatio| string| Stop ratio threshold for **contract PnL drawdown ADL**

  * ADL stops when the symbol's 8 hours drawdown ratio falls below this value

  
  
* * *

### Request Example

  * HTTP
  * Python
  * Go
  * Java
  * Node.js


    
    
    GET /v5/market/adlAlert&symbol=BTCUSDT HTTP/1.1  
    Host: api-testnet.bybit.com  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_adl_alert(  
        symbol="BTCUSDT"  
    ))  
    
    
    
      
    
    
    
      
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "updatedTime": "1757733960000",  
            "list": [  
                {  
                    "coin": "USDT",  
                    "symbol": "BTCUSDT",  
                    "balance": "92203504694.99632",  
                    "maxBalance": "92231510324.75948",  
                    "insurancePnlRatio": "-0.3",  
                    "pnlRatio": "-0.560973",  
                    "adlTriggerThreshold": "10000",  
                    "adlStopRatio": "-0.25"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1757734022014  
    }

---

# 查詢ADL告警

查詢按組劃分保險池 ADL 告警及相關資訊

> **覆蓋範圍：USDT 永續 / USDT 交割 / USDC 永續 / USDC 交割 / 反向合約**

提示

響應數據基於每分鐘快照

信息

  * **ADL 觸發與停止條件基於以下三種情況:**


  1. **合約盈虧回撤 ADL (基於分組保險池的新機制, 詳見用例 1, 2)**

     * **觸發條件** :  
`balance` (保險基金餘額) > `adlTriggerThreshold` (合約盈虧回撤 ADL 的觸發閾值)  
且 `pnlRatio` < `insurancePnlRatio` (觸發 ADL 的盈虧比例閾值)

其中:

       * **pnlRatio** : symbol 在 8 小時內的回撤比例  
計算公式: `pnlRatio` = (symbol 當前 PnL - symbol 8h 最大 PnL) / 保險池 8h 最大餘額(`maxBalance`)  
_注意: symbol 當前 PnL 與 symbol 8h 最大 PnL 的具體數值未在 API 中直接提供_
       * **保險池 8h 最大餘額(`maxBalance`)**: 最近 8 小時內, 該分組保險池的最大餘額
     * **停止條件** : `pnlRatio` > `adlStopRatio` (ADL 停止回撤比例閾值)

  2. **保險池整體淨值 (equity) 虧損觸發 ADL (原有機制, 詳見用例 3)**

     * **觸發條件** : `balance` (保險基金餘額) ≤ 0
     * **停止條件** : `balance` (保險基金餘額) > 0
  3. **symbol 在分組保險池中出現過於劇烈的保證金虧損 (可視作保險池整體淨值虧損的一種特殊情況)**

     * 為確保資金池整體安全性, 風控團隊可將該幣對自分組保險池中移出, 並臨時設立為獨立保險池
     * **觸發條件** : 當虧損的 symbol 被移出所屬保險池, 且 `balance` (保險基金餘額) ≤ 0 時, 觸發 ADL
     * **停止條件** : `balance` (保險基金餘額) > 0



ADL 示例: 按百分比回撤及保險池餘額觸發

  1. **場景 1: 保險池在 8 小時內未產生大額盈利, 當symbol 虧損超過盈虧比閾值(`insurancePnlRatio`)時，將觸發 ADL**

     * 假設 A、B、C 三個 symbol 共用保險池, 8h 初始 `balance` (保險基金餘額) = **1M USDT**
     * A 持倉發生虧損, 虧損金額 = **350K**
     * 此時計算:
       * `pnlRatio` = -35%
       * `balance` = 1M
       * `adlTriggerThreshold` = 1 (Bybit配置常數)
       * `insurancePnlRatio` = -0.3 (Bybit配置常數)
     * 條件判斷:
       * `balance` (1M) > `adlTriggerThreshold` (1) 
       * `pnlRatio` (-0.35) < `insurancePnlRatio` (-0.3) 
     * → 觸發合約盈虧回撤 ADL
     * 系統依據 **-30% 回撤比例** 計算破產價格, 用戶需補貼 **50K** , 使 A 的 `pnlRatio` 控制在 -30%
     * **停止條件** : 若 A 的 `pnlRatio` > `adlStopRatio` (-0.25, Bybit配置常數), 則停止 ADL

**恢復方式** :

     1. 平台向保險池注資並調整 A 的盈虧值
     2. 保險池繼續承接 A 的倉位, 並透過甩賣賺取維持保證金



* * *

  2. **場景 2: 保險池在 8 小時內產生大額盈利, 但symbol 虧損超過盈虧比閾值(`insurancePnlRatio`)時，仍將觸發 ADL**

     * 假設 A、B、C 三個 symbol 共用保險池, 初始 `balance` = **1M USDT**
     * A 持倉甩賣獲得利潤, 使保險池 8h 最大餘額 = **2M USDT** (A 的 PnL = +1M)
     * 隨後 A 發生虧損, 虧損金額 = **600K**
     * 此時計算:
       * `pnlRatio` = -30%
       * `balance` = 2M
       * `adlTriggerThreshold` = 1 (Bybit配置常數)
       * `insurancePnlRatio` = -0.3 (Bybit配置常數)
     * 條件判斷:
       * `balance` (2M) > `adlTriggerThreshold` (1)
       * `pnlRatio` (-0.30) ≤ `insurancePnlRatio` (-0.3)
     * → 觸發合約盈虧回撤 ADL
     * 系統依據 **-30% 回撤比例** 計算破產價格
     * **停止條件** : 若 A 的 `pnlRatio` > `adlStopRatio` (-0.25, Bybit配置常數), 則停止 ADL

**恢復方式** :

     1. 平台向保險池注資並調整 A 的盈虧值
     2. 保險池繼續承接 A 的倉位, 並透過甩賣賺取維持保證金



* * *

  3. **場景 3: 保險池餘額歸零觸發 ADL**
     * 假設 A、B、C、D 四個 symbol 共用保險池, 初始 `balance` = **1M USDT**
     * 雖然各 symbol 的 `pnlRatio` 均未達 -30%, 但保險池 `balance` 已降至 0
     * 條件判斷:
       * `balance` (0) ≤ 0
     * → 觸發保險池整體淨值 ADL
     * 系統依據各 symbol 的盈虧情況進行破產分攤, 計算保險池為 0 時的破產價格
     * **停止條件** : 若 `balance` > 0, 則停止 ADL



訂閱 [ADL告警](/docs/zh-TW/v5/websocket/public/adl-alert) 以獲取更快速的更新

### HTTP 請求

GET`/v5/market/adlAlert`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
symbol| false| string| 合約名稱，例如 `BTCUSDT`，僅限大寫  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
updateTime| string| 數據最近更新的時間戳 (毫秒)  
list| array| Object  
> coin| string| 保險池所屬幣種  
> symbol| string| 交易對名稱  
> balance| string| 保險基金餘額，用於判斷是否觸發 ADL。對於共用保險池，balance 將採用 T+1 刷新機制，並於每日 UTC 時間 00:00 更新。  
> maxBalance| string| 被棄用，並將傳回空字串。最近 8 小時內的保險池最大餘額  
> insurancePnlRatio| string| 觸發 **合約盈虧回撤 ADL** 的盈虧比例閾值 

  * 當 symbol 在 8 小時內的盈虧回撤比例大於該值時，觸發 ADL

  
> pnlRatio| string| symbol 在 8 小時內的回撤比例，用於判斷 ADL 是否觸發或停止  
> adlTriggerThreshold| string| **合約盈虧回撤 ADL** 的觸發閾值 

  * 僅當保險池餘額大於該值時，8 小時內回撤 n% 的觸發條件才會生效

  
> adlStopRatio| string| **合約盈虧回撤 ADL** 的停止比例閾值 

  * 當 symbol 在 8 小時內的回撤比例小於該值時，ADL 停止

  
  
* * *

### 請求示例

  * HTTP
  * Python
  * Go
  * Java
  * Node.js


    
    
    GET /v5/market/adlAlert&symbol=BTCUSDT HTTP/1.1  
    Host: api-testnet.bybit.com  
    
    
    
      
    
    
    
      
    
    
    
      
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "updatedTime": "1757733960000",  
            "list": [  
                {  
                    "coin": "USDT",  
                    "symbol": "BTCUSDT",  
                    "balance": "92203504694.99632",  
                    "maxBalance": "92231510324.75948",  
                    "insurancePnlRatio": "-0.3",  
                    "pnlRatio": "-0.560973",  
                    "adlTriggerThreshold": "10000",  
                    "adlStopRatio": "-0.25"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1757734022014  
    }