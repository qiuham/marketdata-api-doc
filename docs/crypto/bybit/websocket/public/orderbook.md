---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/websocket/public/orderbook
api_type: WebSocket
updated_at: 2026-10-10 18:50:39.278763
---

# Ticker

Subscribe to the ticker stream.

note

  * This topic utilises the snapshot field and delta field. If a response param is not found in the message, then its value has not changed.
  * Spot & Option tickers message are `snapshot` **only**



Push frequency: Derivatives & Options - **100ms** , Spot - **50ms**

**Topic:**  
`tickers.{symbol}`

### Response Parameters

  * Linear/Inverse
  * Option
  * Spot



Parameter| Type| Comments  
---|---|---  
topic| string| Topic name  
type| string| Data type. `snapshot`,`delta`  
cs| integer| Cross sequence  
ts| number| The timestamp (ms) that the system generates the data  
data| array| Object  
> symbol| string| Symbol name   
> [tickDirection](/docs/v5/enum#tickdirection)| string| Tick direction   
> price24hPcnt| string| Percentage change of market price in the last 24 hours   
> lastPrice| string| Last price   
> prevPrice24h| string| Market price 24 hours ago   
> highPrice24h| string| The highest price in the last 24 hours   
> lowPrice24h| string| The lowest price in the last 24 hours   
> prevPrice1h| string| Market price an hour ago   
> markPrice| string| Mark price   
> indexPrice| string| Index price   
> openInterest| string| Open interest size (both sides)   
> openInterestValue| string| Open interest value (both sides)  
> singleOpenInterest| string| Open interest size (single side)  
> singleOpenInterestValue| string| Open interest value (single side)  
> turnover24h| string| Turnover for 24h   
> volume24h| string| Volume for 24h   
> nextFundingTime| string| Next funding timestamp (ms)   
> fundingRate| string| Funding rate   
> bid1Price| string| Best bid price   
> bid1Size| string| Best bid size   
> ask1Price| string| Best ask price   
> ask1Size| string| Best ask size   
> deliveryTime| datetime| Delivery date time (UTC+0), applicable to expired futures only  
> basisRate| string| Basis rate. _Unique field for inverse futures & USDT/USDC futures_  
> deliveryFeeRate| string| Delivery fee rate. _Unique field for inverse futures & USDT/USDC futures_  
> predictedDeliveryPrice| string| Predicated delivery price. _Unique field for inverse futures & USDT/USDC futures_  
> preOpenPrice| string| Estimated pre-market contract open price 

  * The value is meaningless when entering continuous trading phase
  * USDC Futures and Inverse Futures do not have this field

  
> preQty| string| Estimated pre-market contract open qty 

  * The value is meaningless when entering continuous trading phase
  * USDC Futures and Inverse Futures do not have this field

  
> [curPreListingPhase](/docs/v5/enum#curauctionphase)| string| The current pre-market contract phase 

  * USDC Futures and Inverse Futures do not have this field

  
> fundingIntervalHour| string| Funding interval hour

  * This value currently only supports whole hours
  * Only for Perpetual,For Futures,this field will not return

  
> fundingCap| string| Funding rate upper and lower limits

  * Only for Perpetual,For Futures,this field will not return

  
> basisRateYear| string| Annual basis rate

  * Only for Futures,For Perpetual,this field will not return

  
  
Parameter| Type| Comments  
---|---|---  
topic| string| Topic name  
type| string| Data type. `snapshot`  
id| string| message ID  
ts| number| The timestamp (ms) that the system generates the data  
data| array| Object  
> symbol| string| Symbol name   
> bidPrice| string| Best bid price   
> bidSize| string| Best bid size   
> bidIv| string| Best bid iv   
> askPrice| string| Best ask price   
> askSize| string| Best ask size   
> askIv| string| Best ask iv   
> lastPrice| string| Last price   
> highPrice24h| string| The highest price in the last 24 hours   
> lowPrice24h| string| The lowest price in the last 24 hours   
> markPrice| string| Mark price   
> indexPrice| string| Index price   
> markPriceIv| string| Mark price iv   
> underlyingPrice| string| Underlying price   
> openInterest| string| Open interest size   
> turnover24h| string| Turnover for 24h   
> volume24h| string| Volume for 24h   
> totalVolume| string| Total volume   
> totalTurnover| string| Total turnover   
> delta| string| Delta   
> gamma| string| Gamma   
> vega| string| Vega   
> theta| string| Theta   
> predictedDeliveryPrice| string| Predicated delivery price. It has value when 30 min before delivery   
> change24h| string| The change in the last 24 hous   
  
Parameter| Type| Comments  
---|---|---  
topic| string| Topic name  
ts| number| The timestamp (ms) that the system generates the data  
type| string| Data type. `snapshot`  
cs| integer| Cross sequence  
data| array| Object  
> symbol| string| Symbol name   
> lastPrice| string| Last price   
> highPrice24h| string| The highest price in the last 24 hours   
> lowPrice24h| string| The lowest price in the last 24 hours   
> prevPrice24h| string| Percentage change of market price relative to 24h   
> volume24h| string| Volume for 24h   
> turnover24h| string| Turnover for 24h   
> price24hPcnt| string| Percentage change of market price relative to 24h   
> usdIndexPrice| string| USD index price 

  * used to calculate USD value of the assets in Unified account
  * non-collateral margin coin returns ""

  
  
### Subscribe Example

  * Linear
  * Option
  * Spot


    
    
    from pybit.unified_trading import WebSocket  
    from time import sleep  
    ws = WebSocket(  
        testnet=True,  
        channel_type="linear",  
    )  
    def handle_message(message):  
        print(message)  
    ws.ticker_stream(  
        symbol="BTCUSDT",  
        callback=handle_message  
    )  
    while True:  
        sleep(1)  
    
    
    
    from pybit.unified_trading import WebSocket  
    from time import sleep  
    ws = WebSocket(  
        testnet=True,  
        channel_type="option",  
    )  
    def handle_message(message):  
        print(message)  
    ws.ticker_stream(  
        symbol="tickers.BTC-22JAN23-17500-C",  
        callback=handle_message  
    )  
    while True:  
        sleep(1)  
    
    
    
    from pybit.unified_trading import WebSocket  
    from time import sleep  
    ws = WebSocket(  
        testnet=True,  
        channel_type="spot",  
    )  
    def handle_message(message):  
        print(message)  
    ws.ticker_stream(  
        symbol="BTCUSDT",  
        callback=handle_message  
    )  
    while True:  
        sleep(1)  
    

### Response Example

  * Linear
  * Option
  * Spot


    
    
    LinearPerpetual  
    {  
      "topic": "tickers.BTCUSDT",  
      "type": "snapshot",  
      "data": {  
        "symbol": "BTCUSDT",  
        "tickDirection": "MinusTick",  
        "price24hPcnt": "-0.158315",  
        "lastPrice": "66666.60",  
        "prevPrice24h": "79206.20",  
        "highPrice24h": "79266.30",  
        "lowPrice24h": "65076.90",  
        "prevPrice1h": "66666.60",  
        "markPrice": "66666.60",  
        "indexPrice": "115418.19",  
        "openInterest": "492373.72",  
        "openInterestValue": "32824881841.75",  
        "turnover24h": "4936790807.6521",  
        "volume24h": "73191.3870",  
        "fundingIntervalHour": "8",  
        "fundingCap": "0.005",  
        "nextFundingTime": "1760342400000",  
        "fundingRate": "-0.005",  
        "bid1Price": "66666.60",  
        "bid1Size": "23789.165",  
        "ask1Price": "66666.70",  
        "ask1Size": "23775.469",  
        "preOpenPrice": "",  
        "preQty": "",  
        "curPreListingPhase": ""  
      },  
      "cs": 9532239429,  
      "ts": 1760325052630  
    }  
    LinearFutures  
    {  
      "topic": "tickers.BTC-26DEC25",  
      "type": "snapshot",  
      "data": {  
        "symbol": "BTC-26DEC25",  
        "tickDirection": "ZeroMinusTick",  
        "price24hPcnt": "0",  
        "lastPrice": "109401.50",  
        "prevPrice24h": "109401.50",  
        "highPrice24h": "109401.50",  
        "lowPrice24h": "109401.50",  
        "prevPrice1h": "109401.50",  
        "markPrice": "121144.63",  
        "indexPrice": "114132.51",  
        "openInterest": "6.622",  
        "openInterestValue": "802219.74",  
        "turnover24h": "0.0000",  
        "volume24h": "0.0000",  
        "deliveryTime": "2025-12-26T08:00:00Z",  
        "basisRate": "0.06129209",  
        "deliveryFeeRate": "0",  
        "predictedDeliveryPrice": "0.00",  
        "basis": "-4730.84",  
        "basisRateYear": "0.30655351",  
        "nextFundingTime": "",  
        "fundingRate": "",  
        "bid1Price": "111254.50",  
        "bid1Size": "0.176",  
        "ask1Price": "131001.00",  
        "ask1Size": "0.580"  
      },  
      "cs": 31337927919,  
      "ts": 1760409119857  
    }  
    
    
    
    {  
        "id": "tickers.BTC-6JAN23-17500-C-2480334983-1672917511074",  
        "topic": "tickers.BTC-6JAN23-17500-C",  
        "ts": 1672917511074,  
        "data": {  
            "symbol": "BTC-6JAN23-17500-C",  
            "bidPrice": "0",  
            "bidSize": "0",  
            "bidIv": "0",  
            "askPrice": "10",  
            "askSize": "5.1",  
            "askIv": "0.514",  
            "lastPrice": "10",  
            "highPrice24h": "25",  
            "lowPrice24h": "5",  
            "markPrice": "7.86976724",  
            "indexPrice": "16823.73",  
            "markPriceIv": "0.4896",  
            "underlyingPrice": "16815.1",  
            "openInterest": "49.85",  
            "turnover24h": "446802.8473",  
            "volume24h": "26.55",  
            "totalVolume": "86",  
            "totalTurnover": "1437431",  
            "delta": "0.047831",  
            "gamma": "0.00021453",  
            "vega": "0.81351067",  
            "theta": "-19.9115368",  
            "predictedDeliveryPrice": "0",  
            "change24h": "-0.33333334"  
        },  
        "type": "snapshot"  
    }  
    
    
    
    {  
        "topic": "tickers.BTCUSDT",  
        "ts": 1673853746003,  
        "type": "snapshot",  
        "cs": 2588407389,  
        "data": {  
            "symbol": "BTCUSDT",  
            "lastPrice": "21109.77",  
            "highPrice24h": "21426.99",  
            "lowPrice24h": "20575",  
            "prevPrice24h": "20704.93",  
            "volume24h": "6780.866843",  
            "turnover24h": "141946527.22907118",  
            "price24hPcnt": "0.0196",  
            "usdIndexPrice": "21120.2400136"  
        }  
    }

---

# 行情

訂閱行情數據推送.  


警告

  * 注意，該topic推送delta數據和snapshot数据。如果delta數據中缺失一些字段，表明該字段自上次推送以來沒有發生變化。
  * 現貨和期權只推送snapshot類型數據



推送頻率: 期貨和期權 - **100ms** , 現貨 - **50ms**

**Topic:**  
`tickers.{symbol}`

### 響應參數

  * Linear/Inverse
  * Option
  * Spot



參數| 類型| 說明  
---|---|---  
topic| string| Topic名稱  
type| string| 數據類型. `snapshot`,`delta`  
cs| integer| 撮合版本號  
ts| number| 行情服務生成數據的時間戳 (毫秒)  
data| array| Object  
> symbol| string| 合約名稱   
> tickDirection| string| 價格變化方向   
> price24hPcnt| string| 市場價格相對24h前變化的百分比   
> lastPrice| string| 最新市場成交價   
> prevPrice24h| string| 24小時前的整點市價   
> highPrice24h| string| 最近24小時的最高價   
> lowPrice24h| string| 最近24小時的最低價   
> prevPrice1h| string| 1小時前的整點市價   
> markPrice| string| 標記價格   
> indexPrice| string| 指數價格   
> openInterest| string| 未平倉合約的數量（雙邊和）  
> singleOpenInterest| string| 未平倉合約的數量（單邊）  
> openInterestValue| string| 未平倉合約的價值（雙邊和）  
> singleOpenInterestValue| string| 未平倉合約的價值（單邊）  
> turnover24h| string| 最近24小時成交額   
> volume24h| string| 最近24小時成交量   
> nextFundingTime| string| 下次結算資金費用的時間戳 (毫秒)   
> fundingRate| string| 資金費率   
> bid1Price| string| 買1價   
> bid1Size| string| 買1價的數量   
> ask1Price| string| 賣1價   
> ask1Size| string| 賣1價的數量   
> deliveryTime| datetime| 交割日期時間 (UTC+0), 僅適用於交割合約  
> basisRate| string| 基差率. _反向交割和USDT/USDC交割獨有字段_  
> deliveryFeeRate| string| 交割費率. _反向交割和USDT/USDC交割獨有字段_  
> predictedDeliveryPrice| string| 預估交割價格. _反向交割和USDT/USDC交割獨有字段_  
> preOpenPrice| string| 盤前合約預估開盤價格 

  * 在進入連續競價後, 該值無意義
  * USDT/USDC交割合約, 反向交割合約不輸出該字段

  
> preQty| string| 盤前合約預估開盤數量 

  * 進入連續競價後, 該值無意義
  * USDT/USDC交割合約, 反向交割合約不輸出該字段

  
> [curPreListingPhase](/docs/zh-TW/v5/enum#curauctionphase)| string| 當前盤前交易階段 

  * USDT/USDC交割合約, 反向交割合約不輸出該字段

  
> fundingIntervalHour| string| 資金費率間隔（小時）

  * 此數值目前僅支援整數小時
  * 僅適用於永續合約；若為交割合約，不輸出該字段

  
> fundingCap| string| 資金費率上下限

  * 僅適用於永續合約；若為交割合約，不輸出該字段

  
> basisRateYear| string| 年化基準利率

  * 僅適用於交割合約；若為永續合約，不輸出該字段

  
  
參數| 類型| 說明  
---|---|---  
topic| string| Topic名稱  
id| string| 消息id  
type| string| 數據類型. `snapshot`  
ts| number| 行情服務生成數據的時間戳 (毫秒)  
data| array| Object  
> symbol| string| 合約名稱   
> bidPrice| string| 買1價   
> bidSize| string| 買1價的數量   
> bidIv| string| 買1價對應的iv   
> askPrice| string| 賣1價   
> askSize| string| 賣1價的數量   
> askIv| string| 賣1價對應的iv   
> lastPrice| string| 最新市場成交價   
> highPrice24h| string| 最近24小時的最高價   
> lowPrice24h| string| 最近24小時的最低價   
> markPrice| string| 標記價格   
> indexPrice| string| 指數價格   
> markPriceIv| string| 標記價格對應的iv   
> underlyingPrice| string| 底層資產的價格   
> openInterest| string| 未平倉合約的數量   
> turnover24h| string| 最近24小時成交額   
> volume24h| string| 最近24小時成交量   
> totalVolume| string| 總成交量   
> totalTurnover| string| 總成交額   
> delta| string| Delta   
> gamma| string| Gamma   
> vega| string| Vega   
> theta| string| Theta   
> predictedDeliveryPrice| string| 預估交割價. 交割前30分鐘有值   
> change24h| string| 過去24小時的變化   
  
參數| 類型| 說明  
---|---|---  
topic| string| Topic名稱  
type| string| 數據類型. `snapshot`  
cs| integer| 撮合版本號  
ts| number| 行情服務生成數據的時間戳 (毫秒)  
data| array| Object  
> symbol| string| 合約名稱   
> lastPrice| string| 最新市場成交價   
> highPrice24h| string| 最近24小時的最高價  
> lowPrice24h| string| 最近24小時的最低價   
> prevPrice24h| string| 24小時前的整點市價   
> volume24h| string| 最近24小時成交量   
> turnover24h| string| 最近24小時成交額   
> price24hPcnt| string| 市場價格相對24h前變化的百分比   
> usdIndexPrice| string| USD指數價格 

  * 用於計算統一帳戶裡資產折算成USD價值的價格
  * 若幣種不屬於抵押品幣種, 則返回空字符串

  
  
### 訂閱示例

  * Linear
  * Option
  * Spot


    
    
    from pybit.unified_trading import WebSocket  
    from time import sleep  
    ws = WebSocket(  
        testnet=True,  
        channel_type="linear",  
    )  
    def handle_message(message):  
        print(message)  
    ws.ticker_stream(  
        symbol="BTCUSDT",  
        callback=handle_message  
    )  
    while True:  
        sleep(1)  
    
    
    
    from pybit.unified_trading import WebSocket  
    from time import sleep  
    ws = WebSocket(  
        testnet=True,  
        channel_type="option",  
    )  
    def handle_message(message):  
        print(message)  
    ws.ticker_stream(  
        symbol="tickers.BTC-22JAN23-17500-C",  
        callback=handle_message  
    )  
    while True:  
        sleep(1)  
    
    
    
    from pybit.unified_trading import WebSocket  
    from time import sleep  
    ws = WebSocket(  
        testnet=True,  
        channel_type="spot",  
    )  
    def handle_message(message):  
        print(message)  
    ws.ticker_stream(  
        symbol="BTCUSDT",  
        callback=handle_message  
    )  
    while True:  
        sleep(1)  
    

### 響應示例

  * Linear
  * Option
  * Spot


    
    
    LinearPerpetual  
    {  
      "topic": "tickers.BTCUSDT",  
      "type": "snapshot",  
      "data": {  
        "symbol": "BTCUSDT",  
        "tickDirection": "MinusTick",  
        "price24hPcnt": "-0.158315",  
        "lastPrice": "66666.60",  
        "prevPrice24h": "79206.20",  
        "highPrice24h": "79266.30",  
        "lowPrice24h": "65076.90",  
        "prevPrice1h": "66666.60",  
        "markPrice": "66666.60",  
        "indexPrice": "115418.19",  
        "openInterest": "492373.72",  
        "openInterestValue": "32824881841.75",  
        "turnover24h": "4936790807.6521",  
        "volume24h": "73191.3870",  
        "fundingIntervalHour": "8",  
        "fundingCap": "0.005",  
        "nextFundingTime": "1760342400000",  
        "fundingRate": "-0.005",  
        "bid1Price": "66666.60",  
        "bid1Size": "23789.165",  
        "ask1Price": "66666.70",  
        "ask1Size": "23775.469",  
        "preOpenPrice": "",  
        "preQty": "",  
        "curPreListingPhase": ""  
      },  
      "cs": 9532239429,  
      "ts": 1760325052630  
    }  
    LinearFutures  
    {  
      "topic": "tickers.BTC-26DEC25",  
      "type": "snapshot",  
      "data": {  
        "symbol": "BTC-26DEC25",  
        "tickDirection": "ZeroMinusTick",  
        "price24hPcnt": "0",  
        "lastPrice": "109401.50",  
        "prevPrice24h": "109401.50",  
        "highPrice24h": "109401.50",  
        "lowPrice24h": "109401.50",  
        "prevPrice1h": "109401.50",  
        "markPrice": "121144.63",  
        "indexPrice": "114132.51",  
        "openInterest": "6.622",  
        "openInterestValue": "802219.74",  
        "turnover24h": "0.0000",  
        "volume24h": "0.0000",  
        "deliveryTime": "2025-12-26T08:00:00Z",  
        "basisRate": "0.06129209",  
        "deliveryFeeRate": "0",  
        "predictedDeliveryPrice": "0.00",  
        "basis": "-4730.84",  
        "basisRateYear": "0.30655351",  
        "nextFundingTime": "",  
        "fundingRate": "",  
        "bid1Price": "111254.50",  
        "bid1Size": "0.176",  
        "ask1Price": "131001.00",  
        "ask1Size": "0.580"  
      },  
      "cs": 31337927919,  
      "ts": 1760409119857  
    }  
    
    
    
    {  
        "id": "tickers.BTC-6JAN23-17500-C-2480334983-1672917511074",  
        "topic": "tickers.BTC-6JAN23-17500-C",  
        "ts": 1672917511074,  
        "data": {  
            "symbol": "BTC-6JAN23-17500-C",  
            "bidPrice": "0",  
            "bidSize": "0",  
            "bidIv": "0",  
            "askPrice": "10",  
            "askSize": "5.1",  
            "askIv": "0.514",  
            "lastPrice": "10",  
            "highPrice24h": "25",  
            "lowPrice24h": "5",  
            "markPrice": "7.86976724",  
            "indexPrice": "16823.73",  
            "markPriceIv": "0.4896",  
            "underlyingPrice": "16815.1",  
            "openInterest": "49.85",  
            "turnover24h": "446802.8473",  
            "volume24h": "26.55",  
            "totalVolume": "86",  
            "totalTurnover": "1437431",  
            "delta": "0.047831",  
            "gamma": "0.00021453",  
            "vega": "0.81351067",  
            "theta": "-19.9115368",  
            "predictedDeliveryPrice": "0",  
            "change24h": "-0.33333334"  
        },  
        "type": "snapshot"  
    }  
    
    
    
    {  
        "topic": "tickers.BTCUSDT",  
        "ts": 1673853746003,  
        "type": "snapshot",  
        "cs": 2588407389,  
        "data": {  
            "symbol": "BTCUSDT",  
            "lastPrice": "21109.77",  
            "highPrice24h": "21426.99",  
            "lowPrice24h": "20575",  
            "prevPrice24h": "20704.93",  
            "volume24h": "6780.866843",  
            "turnover24h": "141946527.22907118",  
            "price24hPcnt": "0.0196",  
            "usdIndexPrice": "21120.2400136"  
        }  
    }