---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/websocket/private/dcp
api_type: WebSocket
updated_at: 2026-10-10 18:50:22.424448
---

# Execution

Subscribe to the execution stream to see your executions in **real-time**.

tip

You may have multiple executions for one order in a single message.

**All-In-One Topic:** `execution`  
**Categorised Topic:** `execution.spot`, `execution.linear`, `execution.inverse`, `execution.option`

info

  * All-In-One topic and Categorised topic **cannot** be in the same subscription request
  * All-In-One topic: Allow you to listen to all categories (spot, linear, inverse, option) websocket updates
  * Categorised Topic: Allow you to listen only to specific category websocket updates



### Response Parameters

Parameter| Type| Comments  
---|---|---  
id| string| Message ID  
topic| string| Topic name  
creationTime| number| Data created timestamp (ms)  
data| array| Object  
> [category](/docs/v5/enum#category)| string| Product type `spot`, `linear`, `inverse`, `option`  
> symbol| string| Symbol name  
> isLeverage| string| Whether to borrow. `0`: false, `1`: true  
> orderId| string| Order ID  
> orderLinkId| string| User customized order ID  
> side| string| Side. `Buy`,`Sell`  
> orderPrice| string| Order price  
> orderQty| string| Order qty  
> leavesQty| string| The remaining qty not executed  
> [createType](/docs/v5/enum#createtype)| string| Order create type 

  * Spot, Option do not have this key

  
> [orderType](/docs/v5/enum#ordertype)| string| Order type. `Market`,`Limit`  
> [stopOrderType](/docs/v5/enum#stopordertype)| string| Stop order type. If the order is not stop order, any type is not returned  
> execFee| string| Executed trading fee. You can get spot fee currency instruction [here](/docs/v5/enum#spot-fee-currency-instruction)  
  
> execId| string| Execution ID  
> execPrice| string| Execution price  
> execQty| string| Execution qty  
> execPnl| string| Profit and Loss for each close position execution. The value keeps consistent with the field "cashFlow" in the [Get Transaction Log](/docs/v5/account/transaction-log)  
> [execType](/docs/v5/enum#exectype)| string| Executed type  
> execValue| string| Executed order value  
> execTime| string| Executed timestamp (ms)  
> isMaker| boolean| Is maker order. `true`: maker, `false`: taker  
> feeRate| string| Trading fee rate  
> tradeIv| string| Implied volatility. valid for `option`  
> markIv| string| Implied volatility of mark price. valid for `option`  
> markPrice| string| The mark price of the symbol when executing. valid for `option`  
> indexPrice| string| The index price of the symbol when executing. valid for `option`  
> underlyingPrice| string| The underlying price of the symbol when executing. valid for `option`  
> blockTradeId| string| Paradigm block trade ID  
> closedSize| string| Closed position size  
> extraFees| List| Extra trading fee information. Currently, this data is returned only for kyc=Indian user or spot orders placed on the Indonesian site or spot fiat currency orders placed on the EU site. In other cases, an empty string is returned. Enum: [feeType](/docs/v5/enum#extrafeesfeetype), [subFeeType](/docs/v5/enum#extrafeessubfeetype)  
> seq| long| Cross sequence, used to associate each fill and each position update

  * The seq will be the same when conclude multiple transactions at the same time
  * Different symbols may have the same seq, please use seq + symbol to check unique

  
> feeCurrency| string| Trading fee currency  
  
### Subscribe Example
    
    
    {  
        "op": "subscribe",  
        "args": [  
            "execution"  
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
    ws.execution_stream(callback=handle_message)  
    while True:  
        sleep(1)  
    

### Stream Example
    
    
    {  
        "topic": "execution",  
        "id": "386825804_BTCUSDT_140612148849382",  
        "creationTime": 1746270400355,  
        "data": [  
            {  
                "category": "linear",  
                "symbol": "BTCUSDT",  
                "closedSize": "0.5",  
                "execFee": "26.3725275",  
                "execId": "0ab1bdf7-4219-438b-b30a-32ec863018f7",  
                "execPrice": "95900.1",  
                "execQty": "0.5",  
                "execType": "Trade",  
                "execValue": "47950.05",  
                "feeRate": "0.00055",  
                "tradeIv": "",  
                "markIv": "",  
                "blockTradeId": "",  
                "markPrice": "95901.48",  
                "indexPrice": "",  
                "underlyingPrice": "",  
                "leavesQty": "0",  
                "orderId": "9aac161b-8ed6-450d-9cab-c5cc67c21784",  
                "orderLinkId": "",  
                "orderPrice": "94942.5",  
                "orderQty": "0.5",  
                "orderType": "Market",  
                "stopOrderType": "UNKNOWN",  
                "side": "Sell",  
                "execTime": "1746270400353",  
                "isLeverage": "0",  
                "isMaker": false,  
                "seq": 140612148849382,  
                "marketUnit": "",  
                "execPnl": "0.05",  
                "createType": "CreateByUser",  
                "extraFees":[{"feeCoin":"USDT","feeType":"GST","subFeeType":"IND_GST","feeRate":"0.0000675","fee":"0.006403779"}],  
                "feeCurrency": "USDT"  
            }  
        ]  
    }

---

# 個人成交

訂閱個人成交的推送

提示

單筆訂單可能有多次成交

**All-In-One Topic:** `execution`  
**Categorised Topic:** `execution.spot`, `execution.linear`, `execution.inverse`, `execution.option`

信息

  * All-In-One topic 和 Categorised topic **不能** 放在同一個訂閱請求裡
  * All-In-One topic: 允許您監聽所有業務線的websocket更新(現貨, 正向合約, 反向合約, 期權)
  * Categorised Topic: 您只能監聽您指定的那個業務的websocket更新



### 響應參數

參數| 類型| 說明  
---|---|---  
id| string| 消息id  
topic| string| Topic名  
creationTime| number| 消息數據創建時間  
data| array| Object  
> [category](/docs/zh-TW/v5/enum#category)| string| 產品類型 `spot`, `linear`, `iverse`, `option`  
> symbol| string| 合約名稱  
> isLeverage| string| 是否自動借貸. 僅`spot`有效. `0`: 否, 幣幣交易, `1`: 是, 槓桿交易  
> orderId| string| 訂單ID  
> orderLinkId| string| 用戶自定義訂單ID  
> side| string| 訂單方向.買：`Buy`,賣：`Sell`  
> orderPrice| string| 訂單價格  
> orderQty| string| 訂單數量  
> leavesQty| string| 剩餘委託未成交數量  
> [createType](/docs/zh-TW/v5/enum#createtype)| string| 訂單創建類型. 現貨、期權不返回該字段  
> [orderType](/docs/zh-TW/v5/enum#ordertype)| string| 訂單類型. 市價單：`Market`,限價單：`Limit`  
> [stopOrderType](/docs/zh-TW/v5/enum#stopordertype)| string| 条件单的订单类型。如果该订单不是条件单，则不会返回任何类型  
> execFee| string| 交易手續費. 您可以從[這裡](/docs/zh-TW/v5/enum#%E7%8F%BE%E8%B2%A8%E4%BA%A4%E6%98%93%E6%89%8B%E7%BA%8C%E8%B2%BB%E5%B9%A3%E7%A8%AE%E8%AA%AA%E6%98%8E)了解現貨手續費幣種信息  
> execId| string| 成交Id  
> execPrice| string| 成交價格  
> execQty| string| 成交數量  
> execPnl| string| 每筆平倉成交的盈虧. 該值和[交易日誌(統一帳戶)](/docs/zh-TW/v5/account/transaction-log)中的"cashFlow"字段一致  
> [execType](/docs/zh-TW/v5/enum#exectype)| string| 成交類型  
> execValue| string| 成交價值  
> execTime| string| 成交時間（毫秒）  
> isMaker| Bool| 是否是 Maker 訂單,`true` 為 maker 訂單，`false` 為 taker 訂單  
> feeRate| string| 手續費率  
> tradeIv| string| 隱含波動率，僅期權有效  
> markIv| string| 標記價格的隱含波動率，僅期權有效  
> markPrice| string| 成交執行時，該 symbol 當時的標記價格  
> indexPrice| string| 成交執行時，該 symbol 當時的指數價格，僅對期權有效  
> underlyingPrice| string| 成交執行時，該 symbol 當時的底層資產價格，僅期權有效  
> blockTradeId| string| 大宗交易的订单 ID ，使用 paradigm 进行大宗交易时生成的 ID  
> closedSize| string| 平倉數量  
> extraFees| List| 交易費率。目前，僅針對kyc=Indian用戶或在印尼網站的現貨訂單或在歐盟站的現貨法定貨幣訂單返回此數據。在其他情況下，傳回空字串。字段枚舉: [feeType](/docs/zh-TW/v5/enum#extrafeesfeetype), [subFeeType](/docs/zh-TW/v5/enum#extrafeessubfeetype)  
> seq| long| 序列號, 用於關聯成交和倉位的更新

  * 同一時間有多筆成交, seq相同
  * 不同的幣對會存在相同seq, 可以使用seq + symbol來做唯一性識別

  
> feeCurrency| string| 交易費用貨幣  
  
### 訂閱示例
    
    
    {  
        "op": "subscribe",  
        "args": [  
            "execution"  
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
    ws.execution_stream(callback=handle_message)  
    while True:  
        sleep(1)  
    

### 推送示例
    
    
    {  
        "id": "592324803b2785-26fa-4214-9963-bdd4727f07be",  
        "topic": "execution",  
        "creationTime": 1672364174455,  
        "data": [  
            {  
                "category": "linear",  
                "symbol": "XRPUSDT",  
                "execFee": "0.005061",  
                "execId": "7e2ae69c-4edf-5800-a352-893d52b446aa",  
                "execPrice": "0.3374",  
                "execQty": "25",  
                "execType": "Trade",  
                "execValue": "8.435",  
                "execPnl": "0",  
                "isMaker": false,  
                "feeRate": "0.0006",  
                "tradeIv": "",  
                "markIv": "",  
                "blockTradeId": "",  
                "markPrice": "0.3391",  
                "indexPrice": "",  
                "underlyingPrice": "",  
                "leavesQty": "0",  
                "orderId": "f6e324ff-99c2-4e89-9739-3086e47f9381",  
                "orderLinkId": "",  
                "orderPrice": "0.3207",  
                "orderQty": "25",  
                "orderType": "Market",  
                "stopOrderType": "UNKNOWN",  
                "side": "Sell",  
                "execTime": "1672364174443",  
                "isLeverage": "0",  
                "closedSize": "25",  
                "extraFees":[{"feeCoin":"USDT","feeType":"GST","subFeeType":"IND_GST","feeRate":"0.0000675","fee":"0.006403779"}],  
                "seq": 4688002127,  
                "feeCurrency": "USDT"  
            }  
        ]  
    }