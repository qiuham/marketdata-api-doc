---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/tradfi-integration
api_type: REST
updated_at: 2026-07-14 18:57:33.506138
---

# TradFi Integration

This guide explains how to integrate with Bybit's TradFi (Traditional Finance) products via the existing V5 API, including how to distinguish between MT5-based instruments and Bybit-native equity perpetuals, how to sign required agreements, and how to trade.

## Distinguish MT5 & Equity Perp Listing

Bybit offers two paths for trading traditional assets:

### TradFi (MT5-based)

Access via the Web UI: navigate to **Trade → TradFi**. This section covers forex, commodities, and stock CFDs powered by the MT5 engine.

![TradFi Web UI Entry](/docs/assets/images/tradfi-webui-entry-7210218fa16637429a1638df7dd3b7f3.png)

### Bybit Platform (Native)

Access via the main **Trade** menu. This includes all standard Bybit product types:

  * **Spot** : xStock tokens (e.g., TSLAX, AAPLX, GOOGLX)
  * **Futures** : Stock perpetuals (e.g., TSLAUSDT), metals perpetuals (XAU, XAG), crude oil perpetuals
  * **Options** : Options contracts settled in USDT, including tokenised gold options (XAUTUSDT-Options)



![Bybit Trading Menu](/docs/assets/images/tradfi-bybit-trading-721699a402b85e6cc815ed5d1f68e8e8.png)

## Legal Review

Before trading traditional asset perpetuals, please review the applicable terms and conditions:

  * [Derivative Contract Terms - TradFi Perps](https://www.bybit.com/en/legal/service-specific-terms/Derivative-Contract-Terms-TradFi-Perps)
  * [Derivative Contract Terms - Oil Perps](https://www.bybit.com/en/legal/service-specific-terms/Derivative-Contract-Terms-Oil-Perps)



## Sign Agreement by Main Account

To trade commodity contracts (metals and crude oil) or stock perpetuals, users must first sign the trading agreement. Stock perpetuals share the same agreement as metals. This can be done in two ways:

### Option 1: Via Web UI

When attempting to trade for the first time, a **Trading Terms** pop-up will appear. Check the checkbox and click **Confirm** to accept.

info

Only the **master account** can sign the agreement via Web UI. Please ensure you are logged in with the master account.

![Trading Terms Agreement Pop-up](/docs/assets/images/tradfi-trading-terms-76a20698cc44a1ce30b4eaa4a1e96e4b.png)

### Option 2: Via API

Use the [Sign Agreement](/docs/v5/user/sign-agreement) endpoint to sign programmatically.

info

  * Only the **master account** can sign the agreement. Subaccounts are not supported for this action.
  * Once the master account has signed, all subaccounts will be eligible to trade.
  * The API key must have at least one of the following permissions: **Account Transfer** , **Subaccount Transfer** , or **Withdrawal**.



#### HTTP Request

POST`/v5/user/agreement`

#### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
category| false| integer| `2`: Metals commodity contracts (XAU & XAG). Stock perps share this agreement  
`3`: Crude oil commodity contract  
 _Either`category` or `categoryV2` is required. This field remains supported, but new enum values will no longer be added here — use `categoryV2` instead._  
categoryV2| false| integer| `1`: Metals commodity contracts (XAU & XAG). Stock perps share this agreement  
`2`: Crude oil commodity contract  
 _Either`category` or `categoryV2` is required. Recommend using this field; new enum values will be added here going forward._  
agree| **true**|  boolean| `true`  
  
#### Response Parameters

None

#### Request Example

  * HTTP
  * Python


    
    
    POST /v5/user/agreement HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: 1772695036541  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 40  
      
    {  
        "agree": true,  
        "categoryV2": 2  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.sign_agreement(  
        category=2,  
        agree=True  
    ))  
    

#### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {},  
        "retExtInfo": {},  
        "time": 1772695037330  
    }  
    

## Index Price Calculation Rule

The index price of a perpetual contract is the **volume-weighted sum** of the top six (6) spot trading pairs across major exchanges. Weights are refreshed hourly based on each pair's 24-hour trading volume.

Key mechanisms:

  * **Price source** : live last-traded price; if liquidity is low or the trade price is abnormal, an orderbook-weighted price is used instead.
  * **Median deviation filter** : if a component deviates from the cross-exchange median by more than 5% (1% for BTC/ETH, 3% for XAU/XAG), it is temporarily excluded and its weight is smoothly redistributed to the remaining components.
  * **Inactivity rule** : a pair with no trades for over 15 minutes is dropped until trading resumes.
  * **Extreme market fallback** : when no reasonable spot price is available, the index is derived from the perpetual's last traded price and orderbook depth (EMA-smoothed).
  * **Special assets** : BBSOL, CMETH, METH, USDE, etc. additionally reference a redemption price with a minimum price floor.



For full formulas and worked examples, refer to the Help Center: [Index Price Calculation](https://www.bybit.com/en/help-center/article/Index-Price-Calculation).

For index component additions, weight adjustments, and other index-related changes, see the [Index Price Announcements](https://www.bybit.com/en/announcement-info/index-price) page.

## Index Price Rollover Mechanism

The index price of perpetual futures is derived from the respective underlying futures contracts. As commodities do not have a traditional spot market, the external reference price is determined based on designated futures contracts.

Before the underlying contract expires, a rollover (contract transition) is performed: the reference price gradually shifts from the front-month contract to the next-month contract over several days, according to a predefined weight schedule.

The weight allocation during the rollover period follows this schedule:

Day| Front-Month Weight| Next-Month Weight  
---|---|---  
Day 1| 80%| 20%  
Day 2| 60%| 40%  
Day 3| 40%| 60%  
Day 4| 20%| 80%  
Day 5| 0%| 100% (Rollover Completed)  
  
For example, a rollover schedule for `CLUSDT` may look like:

Expiry Date (CL/WTIOIL)| Time (UTC+0)| Near-Month Contract Weight (%)| Far-Month Contract Weight (%)  
---|---|---|---  
2026-05-08| 1:00 AM| 80| 20  
2026-05-09| 1:00 AM| 60| 40  
2026-05-12| 1:00 AM| 40| 60  
2026-05-13| 1:00 AM| 20| 80  
2026-05-14| 1:00 AM| 0| 100  
  
For example, `CLUSDT` (Crude Oil) uses this mechanism to transition between its designated underlying futures contracts (e.g., from `WTIK6` to `WTIM6`).

In addition, `CLUSDT` undergoes a monthly **Pyth index rollover** , starting from the **fifth trading day** of each month. This rollover only updates the Pyth index components. 

For example, the following shows the `CLUSDT` index components on **Day 1** of the rollover: ![CLUSDT Index Component](/docs/assets/images/tradfi-index-component-2480f7bd7ee3d68201186a1e51dd61f2.jpg)

info

  1. For the latest rollover schedules and full details, please refer to the Help Center article: [Introduction to TradFi Perpetual Contracts](https://www.bybit.com/en/help-center/article/Introduction-to-TradFi-Perpetual-Contracts?category=4d5d8649cba144c1a8).

  2. The underlying of Pyth is West Texas Intermediate (WTI) crude oil; Pyth price data for the contract can be referenced at [Pyth Data Explorer](https://pythdata.app/explore/Commodities.WTIM6%2FUSD).

  3. On weekends when Pyth markets are closed, Friday's closing price is used as the index price component.

  4. For `CLUSDT`, the anchor price used in index price calculation is Pyth WTI.

  5. When Pyth markets are closed on weekends, the Pyth weight is automatically excluded from the index price calculation. The remaining components' weights are then proportionally rescaled to calculate the index price. This applies to all commodity perpetuals (e.g., crude oil, metals) and stock perpetuals.




To query the current components and their weights contributing to an index price, use the [Get Index Price Components](/docs/v5/market/index-components) endpoint:

GET`/v5/market/index-price-components`

Query parameter: `indexName={symbol}`

The response includes each component's exchange, spot pair, equivalent price, multiplier, and weight used in the index calculation.

## Instruments Info for xStock, Stock & Commodities

Use the [Get Instruments Info](/docs/v5/market/instrument) endpoint together with the `symbolType` filter to retrieve trading rules and metadata for TradFi instruments. See the [symbolType enum](/docs/v5/enum#symboltype) for all supported values.

GET`/v5/market/instruments-info`

Product| `category`| `symbolType`| Example Symbols| Notable Fields  
---|---|---|---|---  
xStock tokens| `spot`| `xstocks`| `TSLAXUSDT`, `AAPLXUSDT`, `NVDAXUSDT`| `xstockMultiplier`  
Stock perpetuals| `linear`| `stock`| `TSLAUSDT`| —  
Commodity perpetuals| `linear`| `commodity`| `XAUUSDT`, `XAGUSDT`, `CLUSDT`| —  
  
Stock and commodity perpetuals return standard linear contract fields (leverage, tick size, funding interval, etc.).

Example request:
    
    
    GET /v5/market/instruments-info?category=linear&symbolType=stock&limit=1000  
    

## Trade via Existing API

After signing the agreement, you can trade TradFi-related instruments (metals perpetuals, crude oil perpetuals, etc.) using the standard [Trade](/docs/v5/order/create-order) endpoints. No separate API is needed — use the same order placement, amendment, and cancellation interfaces:

  * [Place Order](/docs/v5/order/create-order)
  * [Amend Order](/docs/v5/order/amend-order)
  * [Cancel Order](/docs/v5/order/cancel-order)
  * [Get Open & Closed Orders](/docs/v5/order/open-order)
  * [Cancel All Orders](/docs/v5/order/cancel-all)
  * [Get Order History (2 years)](/docs/v5/order/order-list)
  * [Get Trade History (2 years)](/docs/v5/order/execution)
  * [Batch Place Order](/docs/v5/order/batch-place)
  * [Batch Amend Order](/docs/v5/order/batch-amend)
  * [Batch Cancel Order](/docs/v5/order/batch-cancel)
  * [Get Borrow Quota (Spot)](/docs/v5/order/spot-borrow-quota)
  * [Pre Check Order](/docs/v5/order/pre-check-order)



Simply pass the appropriate `category` and `symbol` in your request:

  * **xStock tokens** : `category=spot`, `symbol` e.g., `TSLAXUSDT`, `AAPLXUSDT`
  * **Stock perpetuals** : `category=linear`, `symbol` e.g., `TSLAUSDT`
  * **Metals perpetuals** : `category=linear`, `symbol` e.g., `XAUUSDT`, `XAGUSDT`
  * **Crude oil perpetual** : `category=linear`, `symbol`: `CLUSDT`

---

# TradFi 接入指南

本指南說明如何透過現有的 V5 API 接入 Bybit 的 TradFi（傳統金融）產品，包括如何區分 MT5 相關的交易產品與 Bybit 平台原生的合約、如何簽署所需協議，以及如何進行交易。

## 區分 MT5 與 Equity Perp 上架

Bybit 提供兩條傳統資產交易路徑：

### TradFi（MT5 驅動）

透過 Web UI 進入：導覽至 **Trade → TradFi** 。此區塊涵蓋由 MT5 引擎驅動的外匯、大宗商品及股票 CFD。

![TradFi Web UI 入口](/docs/zh-TW/assets/images/tradfi-webui-entry-7210218fa16637429a1638df7dd3b7f3.png)

### Bybit 平台（原生）

透過主選單 **Trade** 進入，包含所有標準的 Bybit 產品類型：

  * **現貨（Spot）** ：xStock 代幣（如 TSLAX、AAPLX、GOOGLX）
  * **合約（Futures）** ：股票永續合約（如 TSLAUSDT）、貴金屬永續合約（XAU、XAG）、原油永續合約
  * **期權（Options）** ：以 USDT 結算的期權合約，包括代幣化黃金期權（XAUTUSDT-Options）



![Bybit 交易選單](/docs/zh-TW/assets/images/tradfi-bybit-trading-721699a402b85e6cc815ed5d1f68e8e8.png)

## 法律條款審閱

在交易傳統資產永續合約之前，請先閱讀適用的條款與細則：

  * [衍生品合約條款 - TradFi Perps](https://www.bybit.com/en/legal/service-specific-terms/Derivative-Contract-Terms-TradFi-Perps)
  * [衍生品合約條款 - Oil Perps](https://www.bybit.com/en/legal/service-specific-terms/Derivative-Contract-Terms-Oil-Perps)



## 母帳戶簽署協議

交易大宗商品合約（貴金屬與原油）或股票永續合約前，用戶必須先簽署交易協議。股票永續合約與貴金屬共用同一份協議。可透過以下兩種方式完成：

### 方式一：透過 Web UI

首次嘗試交易時，系統會彈出 **Trading Terms** 視窗，勾選核取方塊並點擊 **Confirm** 即可接受。

信息

僅**母帳戶** 可透過 Web UI 簽署協議，請確保使用母帳戶登入。

![交易條款協議彈窗](/docs/zh-TW/assets/images/tradfi-trading-terms-76a20698cc44a1ce30b4eaa4a1e96e4b.png)

### 方式二：透過 API

使用 [簽署協議](/docs/zh-TW/v5/user/sign-agreement) 介面以程式化方式簽署。

信息

  * 請使用**母帳戶** 呼叫介面，子帳戶不支援此操作。
  * 母帳戶簽署後，旗下所有子帳戶即可進行交易。
  * API key 權限需具備其中之一：**帳戶劃轉** 、**母子帳戶劃轉** 、**提幣** 。



#### HTTP 請求

POST`/v5/user/agreement`

#### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
category| false| integer| `2`: 貴金屬（黃金、白銀）合約協議，股票永續合約共用此協議  
`3`: 原油合約協議  
 _`category` 與 `categoryV2` 二選一必傳。該字段仍然可用，但後續新增的枚舉值將不再添加至此字段，請使用 `categoryV2`。_  
categoryV2| false| integer| `1`: 貴金屬（黃金、白銀）合約協議，股票永續合約共用此協議  
`2`: 原油合約協議  
 _`category` 與 `categoryV2` 二選一必傳。建議使用此字段，後續新增的枚舉值將統一添加至此字段。_  
agree| **true**|  boolean| `true`  
  
#### 響應參數

無

#### 請求示例

  * HTTP
  * Python


    
    
    POST /v5/user/agreement HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: 1772695036541  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 40  
      
    {  
        "agree": true,  
        "categoryV2": 2  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.sign_agreement(  
        category=2,  
        agree=True  
    ))  
    

#### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {},  
        "retExtInfo": {},  
        "time": 1772695037330  
    }  
    

## 指數價格計算規則

永續合約的指數價格為主流交易所中**24 小時成交量排名前六（6）** 現貨交易對的**成交量加權總和** ，權重每小時依各交易對的 24 小時成交量重新計算。

主要保護機制：

  * **價格來源** ：採用最新成交價；若流動性不足或成交價異常，則改用訂單簿加權價（Orderbook-Weighted Price）。
  * **中位數偏離過濾** ：若任一成分價偏離跨交易所中位數超過 5%（BTC/ETH 為 1%、黃金/白銀如 XAUUSDT/XAGUSDT 為 3%），該成分將暫時被剔除，其權重以平滑算法逐步重新分配至其他成分。
  * **無交易剔除** ：交易對連續 15 分鐘無成交即剔除,直至恢復成交後重新納入。
  * **極端市況回退** ：在無法取得合理現貨價時，指數將改以永續合約的最新成交價及訂單簿深度（經 EMA 平滑）推導計算。
  * **特殊資產** ：BBSOL、CMETH、METH、USDE 等資產會額外納入贖回價（Redemption Price）並設定最低價格保護。



完整公式與計算範例請參閱幫助中心文章：[指數價格計算](https://www.bybit.com/en/help-center/article/Index-Price-Calculation)。

如需查詢指數成分新增、權重調整及其他指數相關變更，請參閱 [指數價格公告](https://www.bybit.com/en/announcement-info/index-price) 頁面。

## 指數價格展期機制（Index Price Rollover Mechanism）

永續期貨的指數價格源自各自的標的期貨合約。由於大宗商品並無傳統的現貨市場，因此外部參考價格將根據指定的期貨合約來確定。

在標的合約到期前，系統會進行展期換月（contract rollover）：參考價格將依照預定的權重時程，於數日內從前月合約（front-month）逐步過渡至下月合約（next-month）。

展期期間的權重分配依照下表進行：

日期| 前月合約權重（Front-Month）| 下月合約權重（Next-Month）  
---|---|---  
Day 1| 80%| 20%  
Day 2| 60%| 40%  
Day 3| 40%| 60%  
Day 4| 20%| 80%  
Day 5| 0%| 100%（展期完成）  
  
以 `CLUSDT` 為例，換月時間表如下：

到期日（CL/WTIOIL）| 時間（UTC+0）| 近月合約權重（%）| 遠月合約權重（%）  
---|---|---|---  
2026-05-08| 1:00 AM| 80| 20  
2026-05-09| 1:00 AM| 60| 40  
2026-05-12| 1:00 AM| 40| 60  
2026-05-13| 1:00 AM| 20| 80  
2026-05-14| 1:00 AM| 0| 100  
  
以 `CLUSDT`（原油）為例，即依循此機制在其指定的標的期貨合約之間過渡（例如由 `WTIK6` 過渡至 `WTIM6`）。

此外，`CLUSDT` 每月會進行一次 **Pyth 指數成分換月** ，從每月**第五個交易日** 開始。此換月僅更新 Pyth 指數成分。

以下為換月**第 1 日** `CLUSDT` 指數成分示例： ![CLUSDT Index Component](/docs/zh-TW/assets/images/tradfi-index-component-2480f7bd7ee3d68201186a1e51dd61f2.jpg)

信息

  1. 如需取得最新的展期時程與完整說明，請參閱幫助中心文章：[TradFi 永續合約介紹](https://www.bybit.com/en/help-center/article/Introduction-to-TradFi-Perpetual-Contracts?category=4d5d8649cba144c1a8)。

  2. 標的為西德州原油（WTI），合約的 Pyth 行情可參考 [Pyth Data Explorer](https://pythdata.app/explore/Commodities.WTIM6%2FUSD)。

  3. Pyth 遇週末休市時，以週五收盤價作為指數成分計算依據。

  4. 對於 `CLUSDT`，計算指數價格時所使用的錨定價格（Anchor Price）為 Pyth WTI。

  5. 在周末 Pyth 市場收盤時，系統會自動剔除 Pyth 的權重，並按剩餘成分的權重比例重新計算指數價格。此機制適用於所有大宗商品合約（如原油、金屬等）及美股合約。




如需查詢指數的當前成分及各成分的權重，可使用 [查詢指數價格成分](/docs/zh-TW/v5/market/index-components) 介面：

GET`/v5/market/index-price-components`

查詢參數：`indexName={symbol}`

響應包含每個成分的交易所名稱、現貨交易對、等價價格、乘數，以及在指數計算中所占的權重。

## xStock、股票永續合約與大宗商品的可交易產品的規格信息

請使用 [查詢可交易產品的規格信息](/docs/zh-TW/v5/market/instrument) 介面，並搭配 `symbolType` 參數來取得 TradFi 可交易產品的配置規則信息。完整列舉值請參閱 [symbolType 列舉值](/docs/zh-TW/v5/enum#symboltype)。

GET`/v5/market/instruments-info`

產品類型| `category`| `symbolType`| 範例 symbol| 特有欄位  
---|---|---|---|---  
xStock 代幣| `spot`| `xstocks`| `TSLAXUSDT`、`AAPLXUSDT`、`NVDAXUSDT`| `xstockMultiplier`  
股票永續合約| `linear`| `stock`| `TSLAUSDT`| —  
大宗商品永續合約| `linear`| `commodity`| `XAUUSDT`、`XAGUSDT`、`CLUSDT`| —  
  
股票與大宗商品永續合約皆回傳標準的 linear 合約欄位（槓桿、最小價格變動單位、資金費率間隔等）。

請求範例：
    
    
    GET /v5/market/instruments-info?category=linear&symbolType=stock&limit=1000  
    

## 透過現有 API 交易

簽署協議後，您可以使用標準的 [交易](/docs/zh-TW/v5/order/create-order) 介面來交易 TradFi 相關的交易對（貴金屬永續合約、原油永續合約等），無需使用獨立的 API — 使用相同的下單、修改與撤單介面即可：

  * [創建委託單](/docs/zh-TW/v5/order/create-order)
  * [修改委託單](/docs/zh-TW/v5/order/amend-order)
  * [撤銷委託單](/docs/zh-TW/v5/order/cancel-order)
  * [查詢實時委託單](/docs/zh-TW/v5/order/open-order)
  * [撤銷所有委託單](/docs/zh-TW/v5/order/cancel-all)
  * [查詢歷史訂單 (2年)](/docs/zh-TW/v5/order/order-list)
  * [查詢成交紀錄 (2年)](/docs/zh-TW/v5/order/execution)
  * [批量創建委託單](/docs/zh-TW/v5/order/batch-place)
  * [批量修改委託單](/docs/zh-TW/v5/order/batch-amend)
  * [批量撤銷委託單](/docs/zh-TW/v5/order/batch-cancel)
  * [查詢現貨可借額度](/docs/zh-TW/v5/order/spot-borrow-quota)
  * [預檢查訂單](/docs/zh-TW/v5/order/pre-check-order)



僅需在請求中傳入對應的 `category` 與 `symbol`：

  * **xStock 代幣** ：`category=spot`，`symbol` 如 `TSLAXUSDT`、`AAPLXUSDT`
  * **股票永續合約** ：`category=linear`，`symbol` 如 `TSLAUSDT`
  * **貴金屬永續合約** ：`category=linear`，`symbol` 如 `XAUUSDT`、`XAGUSDT`
  * **原油永續合約** ：`category=linear`，`symbol`：`CLUSDT`