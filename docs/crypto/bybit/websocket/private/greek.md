---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/websocket/private/greek
api_type: WebSocket
updated_at: 2026-07-05 19:12:57.074623
---

# Position

Subscribe to the position stream to see changes to your position data in **real-time**.

**All-In-One Topic:** `position`  
**Categorised Topic:** `position.linear`, `position.inverse`, `position.option`

info

  * All-In-One topic and Categorised topic **cannot** be in the same subscription request
  * All-In-One topic: Allow you to listen to all categories (linear, inverse, option) websocket updates
  * Categorised Topic: Allow you to listen only to specific category websocket updates



tip

Every time when you create/amend/cancel an order, the position topic will generate a new message (regardless if there's any actual change)

### Response Parameters

Parameter| Type| Comments  
---|---|---  
id| string| Message ID  
topic| string| Topic name  
creationTime| number| Data created timestamp (ms)  
data| array| Object  
> [category](/docs/v5/enum#category)| string| Product type `linear`, `inverse`, `option`  
> symbol| string| Symbol name  
> side| string| Position side. `Buy`: long, `Sell`: short  
return an empty string `""` for an empty position  
> size| string| Position size  
> [positionIdx](/docs/v5/enum#positionidx)| integer| Used to identify positions in different position modes  
> positionValue| string| Position value  
> riskId| integer| Risk tier ID  
 _for portfolio margin mode, this field returns 0, which means risk limit rules are invalid_  
> riskLimitValue| string| Risk limit value, become meaningless when auto risk-limit tier is applied  
 _for portfolio margin mode, this field returns 0, which means risk limit rules are invalid_  
> entryPrice| string| Average entry price 

  * For USDC Perp & Futures, it indicates average entry price, and it will not be changed with 8-hour session settlement

  
> markPrice| string| Mark price  
> leverage| string| Position leverage  
 _for portfolio margin mode, this field returns "", which means leverage rules are invalid_  
> breakEvenPrice| string| Break even price, only for `linear`,`inverse`. 

  * breakeven_price = (entry_price _qty - realized_pnl) / (qty - abs(qty)_ max(taker fee rate, 0.00055))

  
> autoAddMargin| integer| Whether to add margin automatically when using isolated margin mode 

  * `0`: false
  * `1`: true

  
> positionIM| string| Initial margin, the same value as `positionIMByMp`, please note this change [The New Margin Calculation: Adjustments and Implications](https://www.bybit.com/en/help-center/article/Understanding-the-Adjustment-and-Impact-of-the-New-Margin-Calculation)

  * Portfolio margin mode: returns ""

  
> positionMM| string| Maintenance margin, the same value as `positionMMByMp`

  * Portfolio margin mode: returns ""

  
> liqPrice| string| Position liquidation price 

  * Isolated margin:   
it is the real price for isolated and cross positions, and keeps `""` when liqPrice <= minPrice or liqPrice >= maxPrice
  * Cross margin:  
it is an **estimated** price for cross positions(because the unified mode controls the risk rate according to the account), and keeps `""` when liqPrice <= minPrice or liqPrice >= maxPrice

 _this field is empty for Portfolio Margin Mode, and no liquidation price will be provided_  
> takeProfit| string| Take profit price  
> stopLoss| string| Stop loss price  
> trailingStop| string| Trailing stop  
> unrealisedPnl| string| Unrealised profit and loss  
> curRealisedPnl| string| The realised PnL for the current holding position  
> sessionAvgPrice| string| USDC contract session avg price, it is the same figure as avg entry price shown in the web UI  
> delta| string| Delta. It is only pushed when you subscribe to the option position.  
> gamma| string| Gamma. It is only pushed when you subscribe to the option position.  
> vega| string| Vega. It is only pushed when you subscribe to the option position.  
> theta| string| Theta. It is only pushed when you subscribe to the option position.  
> cumRealisedPnl| string| Cumulative realised pnl 

  * Futures & Perp: it is the all time cumulative realised P&L
  * Option: it is the realised P&L when you hold that position

  
> [positionStatus](/docs/v5/enum#positionstatus)| string| Position status. `Normal`, `Liq`, `Adl`  
> [adlRankIndicator](/docs/v5/enum#adlrankindicator)| integer| Auto-deleverage rank indicator. [What is Auto-Deleveraging?](https://www.bybit.com/en-US/help-center/s/article/What-is-Auto-Deleveraging-ADL)  
> isReduceOnly| boolean| Useful when Bybit lower the risk limit 

  * `true`: Only allowed to reduce the position. You can consider a series of measures, e.g., lower the risk limit, decrease leverage or reduce the position, add margin, or cancel orders, after these operations, you can call [confirm new risk limit](/docs/v5/position/confirm-mmr) endpoint to check if your position can be removed the reduceOnly mark
  * `false`: There is no restriction, and it means your position is under the risk when the risk limit is systematically adjusted
  * Only meaningful for isolated margin & cross margin of USDT Perp, USDC Perp, USDC Futures, Inverse Perp and Inverse Futures, meaningless for others

  
> createdTime| string| Timestamp of the first time a position was created on this symbol (ms)  
> updatedTime| string| Position data updated timestamp (ms)  
> openTime| integer| Position open timestamp (ms), default: `0`  
> seq| long| Cross sequence, used to associate each fill and each position update

  * Different symbols may have the same seq, please use seq + symbol to check unique
  * Returns `"-1"` if the symbol has never been traded
  * Returns the seq updated by the last transaction when there are setting like leverage, risk limit

  
> mmrSysUpdatedTime| string| Useful when Bybit lower the risk limit 

  * When isReduceOnly=`true`: the timestamp (ms) when the MMR will be forcibly adjusted by the system
When isReduceOnly=`false`: the timestamp when the MMR had been adjusted by system
    * It returns the timestamp when the system operates, and if you manually operate, there is no timestamp
    * Keeps `""` by default, if there was a lower risk limit system adjustment previously, it shows that system operation timestamp
    * Only meaningful for isolated margin & cross margin of USDT Perp, USDC Perp, USDC Futures, Inverse Perp and Inverse Futures, meaningless for others

  
> leverageSysUpdatedTime| string| Useful when Bybit lower the risk limit 

  * When isReduceOnly=`true`: the timestamp (ms) when the leverage will be forcibly adjusted by the system
When isReduceOnly=`false`: the timestamp when the leverage had been adjusted by system
    * It returns the timestamp when the system operates, and if you manually operate, there is no timestamp
    * Keeps `""` by default, if there was a lower risk limit system adjustment previously, it shows that system operation timestamp
    * Only meaningful for isolated margin & cross margin of USDT Perp, USDC Perp, USDC Futures, Inverse Perp and Inverse Futures, meaningless for others

  
> positionIMByMp| string| Initial margin calculated by mark price, the same value as `positionIM`

  * Portfolio margin mode: returns ""

  
> positionMMByMp| string| Maintenance margin calculated by mark price, the same value as `positionMM`

  * Portfolio margin mode: returns ""

  
> tpslMode| string| **Deprecated** , always "Full"  
> bustPrice| string| **Deprecated** , always `""`  
> positionBalance| string| **Deprecated** , can refer to `positionIM` or `positionIMByMp` field  
> tradeMode| integer| **Deprecated** , always `0`, check [Get Account Info](/docs/v5/account/account-info) to know the margin mode  
  
### Subscribe Example
    
    
    {  
        "op": "subscribe",  
        "args": [  
            "position"  
        ]  
    }  
    
    
    
    from pybit.unified_trading import WebSocket  
    from time import sleep  
    ws = WebSocket(  
        testnet=True,  
        channel_type="private",  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    def handle_message(message):  
        print(message)  
    ws.position_stream(callback=handle_message)  
    while True:  
        sleep(1)  
    

### Stream Example
    
    
    {  
        "id": "1003076014fb7eedb-c7e6-45d6-a8c1-270f0169171a",  
        "topic": "position",  
        "creationTime": 1697682317044,  
        "data": [  
            {  
                "positionIdx": 2,  
                "tradeMode": 0,  
                "riskId": 1,  
                "riskLimitValue": "2000000",  
                "symbol": "BTCUSDT",  
                "side": "",  
                "size": "0",  
                "entryPrice": "0",  
                "leverage": "10",  
                "breakEvenPrice":"93556.73034991",  
                "positionValue": "0",  
                "positionBalance": "0",  
                "markPrice": "28184.5",  
                "positionIM": "0",  
                "positionIMByMp": "0",  
                "positionMM": "0",  
                "positionMMByMp": "0",  
                "takeProfit": "0",  
                "stopLoss": "0",  
                "trailingStop": "0",  
                "unrealisedPnl": "0",  
                "curRealisedPnl": "1.26",  
                "cumRealisedPnl": "-25.06579337",  
                "sessionAvgPrice": "0",  
                "createdTime": "1694402496913",  
                "updatedTime": "1697682317038",  
                "tpslMode": "Full",  
                "liqPrice": "0",  
                "bustPrice": "",  
                "category": "linear",  
                "positionStatus": "Normal",  
                "adlRankIndicator": 0,  
                "autoAddMargin": 0,  
                "leverageSysUpdatedTime": "",  
                "mmrSysUpdatedTime": "",  
                "seq": 8327597863,  
                "isReduceOnly": false  
            }  
        ]  
    }

---

# 持倉

訂閱持倉數據的推送

**All-In-One Topic:** `position`  
**Categorised Topic:** `position.linear`, `position.inverse`, `position.option`

信息

  * All-In-One topic 和 Categorised topic **不能** 放在同一個訂閱請求裡
  * All-In-One topic: 允許您監聽所有業務線的websocket倉位更新(正向合約, 反向合約, 期權)
  * Categorised Topic: 您只能監聽您指定的那個業務的websocket更新



提示

在下/改/撤一個訂單的時候, 無論倉位是否發生實質的變化, 您都會收到一條倉位數據的推送

### 響應參數

參數| 類型| 說明  
---|---|---  
id| string| 消息id  
topic| string| Topic名  
creationTime| number| 消息數據創建時間  
data| array| Object  
> [category](/docs/zh-TW/v5/enum#category)| string| 產品類型  
> symbol| string| 合約名稱  
> side| string| 持倉方向. `Buy`,`Sell`  
> size| string| 當前倉位的合约數量, 總是正數  
> [positionIdx](/docs/zh-TW/v5/enum#positionidx)| integer| 倉位標識  
> positionValue| string| 倉位價值  
> riskId| integer| 风险限额ID, 參見[風險限額](/docs/zh-TW/v5/websocket/v5/market/risk-limit)接口   
_若賬戶為組合保證金模式(PM), 該字段返回0, 風險限額規則失效_  
> riskLimitValue| string| 由於自動升降檔機制, 該字段變得**無意義**   
_若賬戶為組合保證金模式(PM)，該字段返回"", 風險限額規則失效_  
> entryPrice| string| 當前倉位的平均入場價格 
* 對於8小時結算的USDC合約倉位, 該字段表示的是平均開倉價格, 不隨著結算而改變  
> markPrice| string| 標記價  
> leverage| string| 槓桿. _注意: 組合保證金模式下，該字段返回""，槓桿規則失效_  
> breakEvenPrice| string| 損益平衡價，**仅适用于合约**. 

  * breakeven_price = (entry_price _qty - realized_pnl) / (qty - abs(qty)_ max(taker fee rate, 0.00055))

  
> autoAddMargin| integer| 是否自動追加保證金, _反向合約不支持設置自動追加保證金_

  * `0`: 否
  * `1`: 是

  
> positionIM| string| 倉位起始保證金(用mark price計算), 值和`positionIMByMp`保持相同, 请看这个这则[调整](https://www.bybit.com/zh-TW/help-center/article/Understanding-the-Adjustment-and-Impact-of-the-New-Margin-Calculation)

  * 組合保證金模式(PM)下, 該字段返回為空字符串

  
> positionIMByMp| string| 倉位起始保證金(過渡期字段, 用mark price計算), 值和`positionIM`保持相同 

  * 組合保證金模式(PM)下, 該字段返回為空字符串

  
> positionMM| string| 倉位維持保證金(用mark price計算) 

  * 組合保證金模式(PM)下, 該字段返回為空字符串

  
> positionMMByMp| string| 倉位維持保證金(過渡期字段, 用mark price計算) 

  * 組合保證金模式(PM)下, 該字段返回為空字符串

  
> liqPrice| string| 倉位強平價格

  * 逐倉保證金:  
是持仓的真實價格, 當強平價 <= minPrice或者 強平價 >= maxPrice, 則為`""`。
  * 全倉保證金:  
請注意, 這是預計強平價格僅供參考。僅當帳戶維持保證金率達到100%時會觸發強平, 當強平價 <= minPrice或者 強平價 >= maxPrice, 則為`""`

_對於組合保證金模式, 此字段為空, 不會提供強平價格_  
> takeProfit| string| 止盈價格  
> stopLoss| string| 止損價格  
> trailingStop| string| 追蹤止損  
> unrealisedPnl| string| 未結盈虧  
> sessionAvgPrice| string| USDC合約平均持倉價格, 會隨著8小時結算而變動  
> delta| string| Delta. 只有訂閱期權的position時才會推送這個字段  
> gamma| string| Gamma. 只有訂閱期權的position時才會推送這個字段  
> vega| string| Vega. 只有訂閱期權的position時才會推送這個字段  
> theta| string| Theta. 只有訂閱期權的position時才會推送這個字段  
> curRealisedPnl| string| 當前持倉的已結盈虧  
> cumRealisedPnl| string| 累计已结盈亏 

  * 期貨: 是從第一次開始有持倉加總的已結盈虧
  * 期權: 它是本次持倉的加總已結盈虧

  
> [positionStatus](/docs/zh-TW/v5/enum#positionstatus)| string| 倉位狀態. `Normal`,`Liq`, `Adl`  
> [adlRankIndicator](/docs/zh-TW/v5/enum#adlrankindicator)| integer| 自動減倉燈. [什麼是自動減倉機制?](https://www.bybit.com/zh-TW/help-center/s/article/What-is-Auto-Deleveraging-ADL)  
> createdTime| string| 倉位創建時間戳 (毫秒)  
> updatedTime| string| 倉位數據更新時間戳 (毫秒)  
> openTime| integer| 開倉時間, 默認: `0`  
> seq| long| 序列號, 用於關聯成交和倉位的更新

  * 不同的幣對會存在相同seq, 可以使用seq + symbol來做唯一性識別
  * 如果該幣對從未被交易過, 查詢時則會返回`"-1"`
  * 對於更新槓桿、更新風險限額等非交易行為, 將會返回上一次成交時更新的seq

  
> isReduceOnly| boolean| 僅當Bybit需要降低某個Symbol的風險限額時有用 

  * `true`: 僅允許減倉操作. 您可以考慮一系列的方式, 比如, 降低risk limit檔位, 或者同檔位修改槓桿或減少倉位, 或者增加保證金, 或者撤單, 這些操作做完後, 可以主動調用[確認新的風險限額](/docs/zh-TW/v5/position/confirm-mmr)接口
  * `false`(默認): 沒有交易限制, 表示您的倉位在系統調整時處於風險水平之下
  * 僅對逐倉和全倉的期貨倉位有意義

  
> mmrSysUpdatedTime| string| 僅當Bybit需要降低某個Symbol的風險限額時有用 

  * 當isReduceOnly=`true`: 這個時間戳表示系統強制修改MMR的時間
當isReduceOnly=`false`: 若不為空, 則表示系統已經完成了MMR調整的時間
    * 僅當系統調整才會賦值, 對於主動的調整, 不會在這裡展示時間戳
    * 默認為`""`, 但如果曾經這個symbol有過系統降檔的操作, 那麼這裡會顯示上一次操作的時間
    * 僅對逐倉和全倉的期貨倉位有意義

  
> leverageSysUpdatedTime| string| 僅當Bybit需要降低某個Symbol的風險限額時有用 

  * 當isReduceOnly=`true`: 這個時間戳表示系統強制修改槓桿的時間
當isReduceOnly=`false`: 若不為空, 則表示系統已經完成了槓桿調整的時間
    * 僅當系統調整才會賦值, 對於主動的調整, 不會在這裡展示時間戳
    * 默認為`""`, 但如果曾經這個symbol有過系統降檔的操作, 那麼這裡會顯示上一次操作的時間
    * 僅對逐倉和全倉的期貨倉位有意義

  
> tradeMode| integer| 該字段**廢棄** , 總是 `0`, 請通過接口[查詢賬戶配置](/docs/zh-TW/v5/account/account-info)查詢帳戶保證金模式  
> positionBalance| string| 該字段**廢棄** , 請使用`positionIM`或者`positionIMByMp`  
> bustPrice| string| 該字段**廢棄** , 將始終返回空值  
> tpslMode| string| 該字段**廢棄** , 無意義, 總是返回"Full". 期權總是返回""  
  
### 訂閱示例
    
    
    {  
        "op": "subscribe",  
        "args": [  
            "position"  
        ]  
    }  
    
    
    
    from pybit.unified_trading import WebSocket  
    from time import sleep  
    ws = WebSocket(  
        testnet=True,  
        channel_type="private",  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    def handle_message(message):  
        print(message)  
    ws.position_stream(callback=handle_message)  
    while True:  
        sleep(1)  
    

### 推送示例
    
    
    {  
        "id": "1003076014fb7eedb-c7e6-45d6-a8c1-270f0169171a",  
        "topic": "position",  
        "creationTime": 1697682317044,  
        "data": [  
            {  
                "positionIdx": 2,  
                "tradeMode": 0,  
                "riskId": 1,  
                "riskLimitValue": "2000000",  
                "symbol": "BTCUSDT",  
                "side": "",  
                "size": "0",  
                "entryPrice": "0",  
                "leverage": "10",  
                "breakEvenPrice":"93556.73034991",  
                "positionValue": "0",  
                "positionBalance": "0",  
                "markPrice": "28184.5",  
                "positionIM": "0",  
                "positionIMByMp": "0",  
                "positionMM": "0",  
                "positionMMByMp": "0",  
                "takeProfit": "0",  
                "stopLoss": "0",  
                "trailingStop": "0",  
                "sessionAvgPrice": "0",  
                "unrealisedPnl": "0",  
                "curRealisedPnl": "-2.06",  
                "cumRealisedPnl": "-25.06579337",  
                "createdTime": "1694402496913",  
                "updatedTime": "1697682317038",  
                "tpslMode": "Full",  
                "liqPrice": "0",  
                "bustPrice": "",  
                "category": "linear",  
                "positionStatus": "Normal",  
                "adlRankIndicator": 0,  
                "autoAddMargin": 0,  
                "leverageSysUpdatedTime": "",  
                "mmrSysUpdatedTime": "",  
                "seq": 8327597863,  
                "isReduceOnly": false  
            }  
        ]  
    }