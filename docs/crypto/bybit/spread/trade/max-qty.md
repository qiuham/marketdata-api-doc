---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/spread/trade/max-qty
api_type: Trading
updated_at: 2026-07-14 18:57:19.216020
---

# Execution

**Topic:** `spread.execution`  


### Response Parameters

Parameter| Type| Comments  
---|---|---  
id| string| Message ID  
topic| string| Topic name  
creationTime| number| Data created timestamp (ms)  
data| array<object>|   
> category| string| Combo or single leg, `combination`, `spot_leg`, `future_leg`  
> symbol| string| Combo or leg symbol name  
> isLeverage| string| Account-wide, if Spot Margin is enabled, the spot_leg field in the execution message shows 1, combo is "", and future_leg is 0.  
> orderId| string| Order ID, leg is ""  
> orderLinkId| string| User customized order ID, leg is ""  
> side| string| Side. `Buy`,`Sell`  
> orderPrice| string| Order price  
> orderQty| string| Order qty  
> leavesQty| string| The remaining qty not executed  
> [createType](/docs/v5/enum#createtype)| string| Order create type  
> orderType| string| Order type. `Market`,`Limit`  
> execFee| string| Leg exec fee, deprecated for Spot leg  
> execFeeV2| string| Leg exec fee, used for Spot leg only  
> feeCoin| string| Leg fee currency  
> parentExecId| string| Combo's Execution ID, leg's event has the value  
> execId| string| Execution ID  
> execPrice| string| Execution price  
> execQty| string| Execution qty  
> execPnl| string| Profit and Loss for each close position execution  
> [execType](/docs/v5/enum#exectype)| string| Executed type  
> execValue| string| Executed order value  
> execTime| string| Executed timestamp (ms)  
> isMaker| boolean| Is maker order. `true`: maker, `false`: taker  
> feeRate| string| Trading fee rate  
> markPrice| string| The mark price of the symbol when executing  
> closedSize| string| Closed position size  
> seq| long| Cross sequence  
  
### Subscribe Example
    
    
    {  
        "op": "subscribe",  
        "args": [  
            "spread.execution"  
        ]  
    }  
    

### Stream Example
    
    
    // Combo execution  
    {  
         "topic": "spread.execution",  
         "id": "cvqes8141ilt347i9l20",  
         "creationTime": 1744104992226,  
         "data": [  
              {  
                   "category": "combination",  
                   "symbol": "SOLUSDT_SOL/USDT",  
                   "closedSize": "",  
                   "execFee": "",  
                   "execId": "82c82077-0caa-5304-894d-58a50a342bd7",  
                   "parentExecId": "",  
                   "execPrice": "20.9848",  
                   "execQty": "2",  
                   "execType": "Trade",  
                   "execValue": "",  
                   "feeRate": "",  
                   "markPrice": "",  
                   "leavesQty": "0",  
                   "orderId": "5e010c35-2b44-4f03-8081-8fa31fb73376",  
                   "orderLinkId": "",  
                   "orderPrice": "21",  
                   "orderQty": "2",  
                   "orderType": "Limit",  
                   "side": "Buy",  
                   "execTime": "1744104992220",  
                   "isLeverage": "",  
                   "isMaker": false,  
                   "seq": 241321,  
                   "createType": "CreateByUser",  
                   "execPnl": ""  
              }  
         ]  
    }  
      
    //Future leg execution  
    {  
         "topic": "spread.execution",  
         "id": "1448939_SOLUSDT_28731107101",  
         "creationTime": 1744104992229,  
         "data": [  
              {  
                   "category": "future_leg",  
                   "symbol": "SOLUSDT",  
                   "closedSize": "0",  
                   "execFee": "0.039712",  
                   "execId": "99a18f80-d3b5-4c6f-a1f1-8c5870e3f3bc",  
                   "parentExecId": "82c82077-0caa-5304-894d-58a50a342bd7",  
                   "execPrice": "124.1",  
                   "execQty": "2",  
                   "execType": "FutureSpread",  
                   "execValue": "248.2",  
                   "feeRate": "0.00016",  
                   "markPrice": "119",  
                   "leavesQty": "0",  
                   "orderId": "",  
                   "orderLinkId": "",  
                   "orderPrice": "124.1",  
                   "orderQty": "2",  
                   "orderType": "Limit",  
                   "side": "Buy",  
                   "execTime": "1744104992224",  
                   "isLeverage": "0",  
                   "isMaker": false,  
                   "seq": 28731107101,  
                   "createType": "CreateByFutureSpread",  
                   "execPnl": "0"  
              }  
         ]  
    }

---

# 個人成交

訂閱價差交易發生的成交

**Topic:** `spread.execution`  


### 響應參數

參數| 類型| 說明  
---|---|---  
id| string| 消息ID  
topic| string| Topic名  
creationTime| number| 消息數據創建時間 (ms)  
data| array<object>|   
> category| string| 組合或單腿類型, `combination`: 組合, `spot_leg`: 現貨單腿, `future_leg`: 合約單腿  
> symbol| string| 組合或單腿的合約名稱  
> isLeverage| string| 帳戶維度, 如果現貨槓桿打開了, 那麼對於category=spot_leg, 該字段暫時為1, 組合總是"", category=future_leg總是"0"  
> orderId| string| 組合訂單ID, 單腿展示""  
> orderLinkId| string| 組合訂單IDD, 單腿展示""  
> side| string| 組合或單腿訂單方向. `Buy`,`Sell`  
> orderPrice| string| 組合或單腿的訂單價格  
> orderQty| string| 組合或單腿的訂單數量  
> leavesQty| string| 剩餘未成交數量  
> [createType](/docs/zh-TW/v5/enum#createtype)| string| 訂單創建類型  
> orderType| string| 訂單類型. `Market`,`Limit`  
> execFee| string| 手續費, 組合暫時為""  
> execFeeV2| string| 現貨單腿手續費  
> feeCoin| string| 單腿交易手續費幣種  
> parentExecId| string| 單腿的母成交ID, 即對應組合的成交ID, 組合暫時""  
> execId| string| 成交ID  
> execPrice| string| 成交價格  
> execQty| string| 成交數量  
> execPnl| string| 每筆平倉成交的盈虧, 僅合約單腿成交有效  
> [execType](/docs/zh-TW/v5/enum#exectype)| string| 成交類型, 組合總是`Trade`  
> execValue| string| 成交價值, 僅適用於單腿成交  
> execTime| string| 成交時間（ms）  
> isMaker| boolean| 是否是maker成交. `true`: maker, `false`: taker  
> feeRate| string| 手續費率, 僅適用於單腿成交  
> markPrice| string| 成交執行時, 該 symbol 當時的標記價格, markPrice  
> closedSize| string| 平倉數量, 僅適用於單腿成交  
> seq| long| 序列號, 用於關聯成交和倉位的更新  
  
### 訂閱示例
    
    
    {  
        "op": "subscribe",  
        "args": [  
            "spread.execution"  
        ]  
    }  
    

### 推送示例
    
    
    // Combo execution  
    {  
         "topic": "spread.execution",  
         "id": "cvqes8141ilt347i9l20",  
         "creationTime": 1744104992226,  
         "data": [  
              {  
                   "category": "combination",  
                   "symbol": "SOLUSDT_SOL/USDT",  
                   "closedSize": "",  
                   "execFee": "",  
                   "execId": "82c82077-0caa-5304-894d-58a50a342bd7",  
                   "parentExecId": "",  
                   "execPrice": "20.9848",  
                   "execQty": "2",  
                   "execType": "Trade",  
                   "execValue": "",  
                   "feeRate": "",  
                   "markPrice": "",  
                   "leavesQty": "0",  
                   "orderId": "5e010c35-2b44-4f03-8081-8fa31fb73376",  
                   "orderLinkId": "",  
                   "orderPrice": "21",  
                   "orderQty": "2",  
                   "orderType": "Limit",  
                   "side": "Buy",  
                   "execTime": "1744104992220",  
                   "isLeverage": "",  
                   "isMaker": false,  
                   "seq": 241321,  
                   "createType": "CreateByUser",  
                   "execPnl": ""  
              }  
         ]  
    }  
      
    //Future leg execution  
    {  
         "topic": "spread.execution",  
         "id": "1448939_SOLUSDT_28731107101",  
         "creationTime": 1744104992229,  
         "data": [  
              {  
                   "category": "future_leg",  
                   "symbol": "SOLUSDT",  
                   "closedSize": "0",  
                   "execFee": "0.039712",  
                   "execId": "99a18f80-d3b5-4c6f-a1f1-8c5870e3f3bc",  
                   "parentExecId": "82c82077-0caa-5304-894d-58a50a342bd7",  
                   "execPrice": "124.1",  
                   "execQty": "2",  
                   "execType": "FutureSpread",  
                   "execValue": "248.2",  
                   "feeRate": "0.00016",  
                   "markPrice": "119",  
                   "leavesQty": "0",  
                   "orderId": "",  
                   "orderLinkId": "",  
                   "orderPrice": "124.1",  
                   "orderQty": "2",  
                   "orderType": "Limit",  
                   "side": "Buy",  
                   "execTime": "1744104992224",  
                   "isLeverage": "0",  
                   "isMaker": false,  
                   "seq": 28731107101,  
                   "createType": "CreateByFutureSpread",  
                   "execPnl": "0"  
              }  
         ]  
    }