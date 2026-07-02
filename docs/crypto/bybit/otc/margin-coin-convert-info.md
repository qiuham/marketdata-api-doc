---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/otc/margin-coin-convert-info
api_type: REST
updated_at: 2026-07-02 19:20:15.391756
---

# Get Position Info

Query real-time position data, such as position size, cumulative realized PNL, etc.

info

**category="inverse"**

  1. You can query all open positions with `/v5/position/list?category=inverse`;
  2. Cannot query multiple symbols in one request
  3. During periods of extreme market volatility, this interface may experience increased latency or temporary delays in data delivery



### HTTP Request

GET`/v5/position/list`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
[category](/docs/v5/enum#category)| **true**|  string| Product type `linear`, `inverse`, `option`  
symbol| false| string| Symbol name, like `BTCUSDT`, uppercase only

  * If `symbol` passed, it returns data regardless of having position or not.
  * If `symbol`=null and `settleCoin` specified, it returns position size greater than zero.

  
baseCoin| false| string| Base coin, uppercase only. `option` **only**. Return all option positions if not passed  
settleCoin| false| string| Settle coin

  * `linear`: either `symbol` or `settleCoin` is **required**. `symbol` has a higher priority

  
limit| false| integer| Limit for data size per page. [`1`, `200`]. Default: `20`  
cursor| false| string| Cursor. Use the `nextPageCursor` token from the response to retrieve the next page of the result set  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
[category](/docs/v5/enum#category)| string| Product type  
nextPageCursor| string| Refer to the `cursor` request parameter  
list| array| Object  
> [positionIdx](/docs/v5/enum#positionidx)| integer| Position idx, used to identify positions in different position modes

  * `0`: One-Way Mode
  * `1`: Buy side of both side mode
  * `2`: Sell side of both side mode

  
> riskId| integer| Risk tier ID  
 _for portfolio margin mode, this field returns 0, which means risk limit rules are invalid_  
> riskLimitValue| string| Risk limit value, become meaningless when auto risk-limit tier is applied  
 _for portfolio margin mode, this field returns 0, which means risk limit rules are invalid_  
> symbol| string| Symbol name  
> side| string| Position side. `Buy`: long, `Sell`: short  
return an empty string `""` for an empty position  
> size| string| Position size, always positive  
> avgPrice| string| Average entry price 

  * For USDC Perp & Futures, it indicates average entry price, and it will not be changed with 8-hour session settlement

  
> positionValue| string| Position value  
> autoAddMargin| integer| Whether to add margin automatically when using isolated margin mode 

  * `0`: false
  * `1`: true

  
> [positionStatus](/docs/v5/enum#positionstatus)| String| Position status. `Normal`, `Liq`, `Adl`  
> leverage| string| Position leverage  
 _for portfolio margin mode, this field returns "", which means leverage rules are invalid_  
> breakEvenPrice| string| Break even price, Only for `linear`,`inverse`. 
* breakeven_price = (entry_price _qty - realized_pnl) / (qty - abs(qty)_ max(taker fee rate, 0.00055))  
> markPrice| string| Mark price  
> liqPrice| string| Position liquidation price 

  * Isolated margin:   
it is the real price for isolated and cross positions, and keeps `""` when liqPrice <= minPrice or liqPrice >= maxPrice
  * Cross margin:  
it is an **estimated** price for cross positions(because the unified mode controls the risk rate according to the account), and keeps `""` when liqPrice <= minPrice or liqPrice >= maxPrice

 _this field is empty for Portfolio Margin Mode, and no liquidation price will be provided_  
> positionIM| string| Initial margin, the same value as `positionIMByMp`, please note this change [The New Margin Calculation: Adjustments and Implications](https://www.bybit.com/en/help-center/article/Understanding-the-Adjustment-and-Impact-of-the-New-Margin-Calculation)

  * Portfolio margin mode: returns ""

  
> positionIMByMp| string| Initial margin calculated by mark price, the same value as `positionIM`

  * Portfolio margin mode: returns ""

  
> positionMM| string| Maintenance margin, the same value as `positionMMByMp`

  * Portfolio margin mode: returns ""

  
> positionMMByMp| string| Maintenance margin calculated by mark price, the same value as `positionMM`

  * Portfolio margin mode: returns ""

  
> takeProfit| string| Take profit price  
> stopLoss| string| Stop loss price  
> trailingStop| string| Trailing stop (the distance from market price)  
> sessionAvgPrice| string| USDC contract session avg price, it is the same figure as avg entry price shown in the web UI  
> delta| string| Delta  
> gamma| string| Gamma  
> vega| string| Vega  
> theta| string| Theta  
> unrealisedPnl| string| Unrealised PnL  
> curRealisedPnl| string| The realised PnL for the current holding position  
> cumRealisedPnl| string| Cumulative realised pnl 

  * Futures & Perps: it is the all time cumulative realised P&L
  * Option: always "", meaningless

  
> [adlRankIndicator](/docs/v5/enum#adlrankindicator)| integer| Auto-deleverage rank indicator. [What is Auto-Deleveraging?](https://www.bybit.com/en-US/help-center/s/article/What-is-Auto-Deleveraging-ADL)  
> createdTime| string| Timestamp of the first time a position was created on this symbol (ms)  
> updatedTime| string| Position updated timestamp (ms)  
> openTime| integer| Position open timestamp (ms), default: `0`  
> seq| long| Cross sequence, used to associate each fill and each position update

  * Different symbols may have the same seq, please use seq + symbol to check unique
  * Returns `"-1"` if the symbol has never been traded
  * Returns the seq updated by the last transaction when there are settings like leverage, risk limit

  
> isReduceOnly| boolean| Useful when Bybit lower the risk limit 

  * `true`: Only allowed to reduce the position. You can consider a series of measures, e.g., lower the risk limit, decrease leverage or reduce the position, add margin, or cancel orders, after these operations, you can call [confirm new risk limit](/docs/v5/position/confirm-mmr) endpoint to check if your position can be removed the reduceOnly mark
  * `false`: There is no restriction, and it means your position is under the risk when the risk limit is systematically adjusted
  * Only meaningful for isolated margin & cross margin of USDT Perp, USDC Perp, USDC Futures, Inverse Perp and Inverse Futures, meaningless for others

  
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

  
> tpslMode| string| **Deprecated** , always "Full"  
> bustPrice| string| **Deprecated** , always `""`  
> positionBalance| string| **Deprecated** , can refer to `positionIM` or `positionIMByMp` field  
> tradeMode| integer| **Deprecated** , always `0`, check [Get Account Info](/docs/v5/account/account-info) to know the margin mode  
[](/docs/api-explorer/v5/position/position-info)

* * *

### Request Example

  * HTTP
  * Python
  * Java
  * Node.js


    
    
    GET /v5/position/list?category=inverse&symbol=BTCUSD HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672280218882  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_positions(  
        category="inverse",  
        symbol="BTCUSD",  
    ))  
    
    
    
    import com.bybit.api.client.domain.*;  
    import com.bybit.api.client.domain.position.*;  
    import com.bybit.api.client.domain.position.request.*;  
    import com.bybit.api.client.service.BybitApiClientFactory;  
    var client = BybitApiClientFactory.newInstance().newAsyncPositionRestClient();  
    var positionListRequest = PositionDataRequest.builder().category(CategoryType.LINEAR).symbol("BTCUSDT").build();  
    client.getPositionInfo(positionListRequest, System.out::println);  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
        key: 'xxxxxxxxxxxxxxxxxx',  
        secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
        .getPositionInfo({  
            category: 'inverse',  
            symbol: 'BTCUSD',  
        })  
        .then((response) => {  
            console.log(response);  
        })  
        .catch((error) => {  
            console.error(error);  
        });  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "list": [  
                {  
                    "positionIdx": 0,  
                    "riskId": 1,  
                    "riskLimitValue": "150",  
                    "symbol": "BTCUSD",  
                    "side": "Sell",  
                    "size": "300",  
                    "avgPrice": "27464.50441675",  
                    "positionValue": "0.01092319",  
                    "tradeMode": 0,  
                    "positionStatus": "Normal",  
                    "autoAddMargin": 1,  
                    "adlRankIndicator": 2,  
                    "leverage": "10",  
                    "breakEvenPrice":"93556.73034991",  
                    "positionBalance": "0.00139186",  
                    "markPrice": "28224.50",  
                    "liqPrice": "",  
                    "bustPrice": "999999.00",  
                    "positionMM": "0.0000015",  
                    "positionMMByMp": "0.0000015",  
                    "positionIM": "0.00010923",  
                    "positionIMByMp": "0.00010923",  
                    "tpslMode": "Full",  
                    "takeProfit": "0.00",  
                    "stopLoss": "0.00",  
                    "trailingStop": "0.00",  
                    "unrealisedPnl": "-0.00029413",  
                    "curRealisedPnl": "0.00013123",  
                    "cumRealisedPnl": "-0.00096902",  
                    "seq": 5723621632,  
                    "isReduceOnly": false,  
                    "mmrSysUpdateTime": "",  
                    "leverageSysUpdatedTime": "",  
                    "sessionAvgPrice": "",  
                    "createdTime": "1676538056258",  
                    "updatedTime": "1697673600012"  
                }  
            ],  
            "nextPageCursor": "",  
            "category": "inverse"  
        },  
        "retExtInfo": {},  
        "time": 1697684980172  
    }

---

# 查詢持倉 (實時)

該接口可以獲取用戶的持倉信息，比如持倉數量，累計盈虧等

信息

**查詢反向合約倉位**

  1. 通過這種查詢方式 "/v5/position/list?category=inverse", 可以獲得所有持倉數據
  2. 不支持傳入多個symbol來查詢



**在極端市場波動期間, 此介面可能會出現延遲增加或資料傳遞暫時延遲的情況**

### HTTP 請求

GET`/v5/position/list`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
[category](/docs/zh-TW/v5/enum#category)| **true**|  string| 產品類型 `linear`,`inverse`, `option`  
symbol| false| string| 合約名稱

  * 若傳了`symbol`, 則不管是否有倉位都返回該symbol數據
  * 若`symbol`不傳但傳了`settleCoin`, 則僅返回有實際倉位的數據

  
baseCoin| false| string| 交易幣種, 若不傳, 則返回期權下所有持倉  
僅適用於`option`  
settleCoin| false| string| 結算幣種

  * USDT和USDC期貨: `symbol`和`settleCon`**必傳** 其中一個, 若都傳，則`symbol`有更高的優先級

  
limit| false| integer| 每頁數量限制. [`1`, `200`]. 默認: `20`  
cursor| false| string| 游標，用於翻頁  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
[category](/docs/zh-TW/v5/enum#category)| string| 產品類型  
list| array| Object  
> [positionIdx](/docs/zh-TW/v5/enum#positionidx)| integer| 倉位標識符, 用于在不同仓位模式下标识仓位  
> riskId| integer| 风险限额ID, 參見[風險限額](/docs/zh-TW/v5/market/risk-limit)接口   
_若賬戶為組合保證金模式(PM), 該字段返回0, 風險限額規則失效_  
> riskLimitValue| string| 由於自動升降檔機制, 該字段變得**無意義**   
_若賬戶為組合保證金模式(PM)，該字段返回"", 風險限額規則失效_  
> symbol| string| 合約名称  
> side| string| 持倉方向, Buy: 多头; Sell: 空头. 空倉時, 單向或者雙向持倉模式都返回空字符串 `""`  
> size| string| 當前倉位的合约數量, 總是正數  
> avgPrice| string| 當前倉位的平均入場價格 

  * 對於8小時結算的USDC合約倉位, 該字段表示的是平均開倉價格, 不隨著結算而改變

  
> positionValue| string| 仓位的價值  
> autoAddMargin| integer| 是否自動追加保證金, _反向合約不支持設置自動追加保證金_

  * `0`: 否
  * `1`: 是

  
> [positionStatus](/docs/zh-TW/v5/enum#positionstatus)| String| 倉位状态. `Normal`,`Liq`, `Adl`  
> leverage| string| 當前倉位的槓桿，**仅适用于合约**  
 _若賬戶為組合保證金模式(PM), 該字段返回空字符串, 槓桿規則失效_  
> breakEvenPrice| string| 損益平衡價，**仅适用于合约**. 
* breakeven_price = (entry_price _qty - realized_pnl) / (qty - abs(qty)_ max(taker fee rate, 0.00055))  
> markPrice| string| symbol 的最新標記價格  
> liqPrice| string| 倉位強平價格

  * 逐倉保證金:  
是持仓的真實價格, 當強平價 <= minPrice或者 強平價 >= maxPrice, 則為`""`。
  * 全倉保證金:  
請注意, 這是預計強平價格僅供參考。僅當帳戶維持保證金率達到100%時會觸發強平, 當強平價 <= minPrice或者 強平價 >= maxPrice, 則為`""`

_對於組合保證金模式, 此字段為空, 不會提供強平價格_  
> positionIM| string| 倉位起始保證金(用mark price計算), 值和`positionIMByMp`保持相同, 请看这个这则[调整](https://www.bybit.com/zh-TW/help-center/article/Understanding-the-Adjustment-and-Impact-of-the-New-Margin-Calculation)

  * 組合保證金模式(PM)下, 該字段返回為空字符串

  
> positionIMByMp| string| 倉位起始保證金(過渡期字段, 用mark price計算), 值和`positionIM`保持相同 

  * 組合保證金模式(PM)下, 該字段返回為空字符串

  
> positionMM| string| 倉位維持保證金(用mark price計算) 

  * 組合保證金模式(PM)下, 該字段返回為空字符串

  
> positionMMByMp| string| 倉位維持保證金(過渡期字段, 用mark price計算) 

  * 組合保證金模式(PM)下, 該字段返回為空字符串

  
> takeProfit| string| 止盈價格  
> stopLoss| string| 止損價格  
> trailingStop| string| 追蹤止損（與當前價格的距離）  
> sessionAvgPrice| string| USDC合約平均持倉價格, 會隨著8小時結算而變動  
> delta| string| Delta  
> gamma| string| Gamma  
> vega| string| Vega  
> theta| string| Theta  
> unrealisedPnl| string| 未结盈亏  
> curRealisedPnl| string| 當前持倉的已結盈虧  
> cumRealisedPnl| string| 累计已结盈亏 

  * 期貨: 是從第一次開始有持倉加總的已結盈虧
  * 期權: 總是"", 無意義

  
> [adlRankIndicator](/docs/zh-TW/v5/enum#adlrankindicator)| integer| 自動減倉燈. [什麼是自動減倉機制?](https://www.bybit.com/zh-TW/help-center/s/article/What-is-Auto-Deleveraging-ADL)  
> createdTime| string| 倉位創建時間  
> updatedTime| string| 倉位數據更新時間  
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

  
> tpslMode| string| 該字段**廢棄** , 無意義, 總是返回"Full". 期權總是返回""  
> tradeMode| integer| 該字段**廢棄** , 總是 `0`, 請通過接口[查詢賬戶配置](/docs/zh-TW/v5/account/account-info)查詢帳戶保證金模式  
> positionBalance| string| 該字段**廢棄** , 請使用`positionIM`或者`positionIMByMp`  
> bustPrice| string| 該字段**廢棄** , 將始終返回空值  
nextPageCursor| string| 游標，用於翻頁  
[](/docs/zh-TW/api-explorer/v5/position/position-info)

* * *

### 請求示例

  * HTTP
  * Python
  * Java
  * Node.js


    
    
    GET /v5/position/list?category=linear&symbol=XRPUSDT HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672280218882  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_positions(  
        category="linear",  
        symbol="XRPUSDT",  
    ))  
    
    
    
    import com.bybit.api.client.domain.*;  
    import com.bybit.api.client.domain.position.*;  
    import com.bybit.api.client.domain.position.request.*;  
    import com.bybit.api.client.service.BybitApiClientFactory;  
    var client = BybitApiClientFactory.newInstance().newAsyncPositionRestClient();  
    var positionListRequest = PositionDataRequest.builder().category(CategoryType.LINEAR).symbol("BTCUSDT").build();  
    client.getPositionInfo(positionListRequest, System.out::println);  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
        key: 'xxxxxxxxxxxxxxxxxx',  
        secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
        .getPositionInfo({  
            category: 'inverse',  
            symbol: 'BTCUSD',  
        })  
        .then((response) => {  
            console.log(response);  
        })  
        .catch((error) => {  
            console.error(error);  
        });  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "list": [  
                {  
                    "positionIdx": 0,  
                    "riskId": 1,  
                    "riskLimitValue": "150",  
                    "symbol": "BTCUSD",  
                    "side": "Sell",  
                    "size": "300",  
                    "avgPrice": "27464.50441675",  
                    "positionValue": "0.01092319",  
                    "tradeMode": 0,  
                    "positionStatus": "Normal",  
                    "autoAddMargin": 1,  
                    "adlRankIndicator": 2,  
                    "leverage": "10",  
                    "breakEvenPrice":"93556.73034991",  
                    "positionBalance": "0.00139186",  
                    "markPrice": "28224.50",  
                    "liqPrice": "",  
                    "bustPrice": "999999.00",  
                    "positionMM": "0.0000015",  
                    "positionMMByMp": "0.0000015",  
                    "positionIM": "0.00010923",  
                    "positionIMByMp": "0.00010923",  
                    "tpslMode": "Full",  
                    "takeProfit": "0.00",  
                    "stopLoss": "0.00",  
                    "trailingStop": "0.00",  
                    "unrealisedPnl": "-0.00029413",  
                    "sessionAvgPrice": "",  
                    "curRealisedPnl": "0.00013123",  
                    "cumRealisedPnl": "-0.00096902",  
                    "seq": 5723621632,  
                    "isReduceOnly": false,  
                    "mmrSysUpdateTime": "",  
                    "leverageSysUpdatedTime": "",  
                    "createdTime": "1676538056258",  
                    "updatedTime": "1697673600012"  
                }  
            ],  
            "nextPageCursor": "",  
            "category": "inverse"  
        },  
        "retExtInfo": {},  
        "time": 1697684980172  
    }