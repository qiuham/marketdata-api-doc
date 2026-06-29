---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/ws/connect
api_type: REST
updated_at: 2026-06-29 19:34:16.360370
---

# Connect

**[WebSocket public stream](/docs/v5/websocket/public/orderbook):**

  * **Mainnet:**  
Spot: `wss://stream.bybit.com/v5/public/spot`  
USDT, USDC perpetual & USDT Futures: `wss://stream.bybit.com/v5/public/linear`  
Inverse contract: `wss://stream.bybit.com/v5/public/inverse`  
Spread trading: `wss://stream.bybit.com/v5/public/spread`  
RFQ: `wss://stream-testnet.bybit.com/v5/public/rfq`  
USDT/USDC Options: `wss://stream.bybit.com/v5/public/option`

  * **Testnet:**  
Spot: `wss://stream-testnet.bybit.com/v5/public/spot`  
USDT,USDC perpetual & USDT Futures: `wss://stream-testnet.bybit.com/v5/public/linear`  
Inverse contract: `wss://stream-testnet.bybit.com/v5/public/inverse`  
Spread trading: `wss://stream-testnet.bybit.com/v5/public/spread`  
RFQ: `wss://stream-testnet.bybit.com/v5/public/rfq`  
USDT/USDC Options: `wss://stream-testnet.bybit.com/v5/public/option`




**[WebSocket private stream](/docs/v5/websocket/private/order):**

  * **Mainnet:**  
`wss://stream.bybit.com/v5/private`

  * **Testnet:**  
`wss://stream-testnet.bybit.com/v5/private`




**[WebSocket Order Entry](/docs/v5/websocket/trade/guideline):**

  * **Mainnet:**  
`wss://stream.bybit.com/v5/trade` (Spread trading is not supported)

  * **Testnet:**  
`wss://stream-testnet.bybit.com/v5/trade` (Spread trading is not supported)




**[WebSocket GET System Status](/docs/v5/websocket/system/system-status):**

  * **Mainnet:**  
`wss://stream.bybit.com/v5/public/misc/status`

  * **Testnet:**  
`wss://stream-testnet.bybit.com/v5/public/misc/status`




info

  * If your account is registered from [www.bybit.tr](http://www.bybit.tr), please use `stream.bybit.tr` for mainnet access
  * If your account is registered from [www.bybit.kz](http://www.bybit.kz), please use `stream.bybit.kz` for mainnet access
  * If your account is registered from [www.bybitgeorgia.ge](http://www.bybitgeorgia.ge), please use `stream.bybitgeorgia.ge` for mainnet access



Customise Private Connection Alive Time

For private stream and order entry, you can customise alive duration by adding a param `max_active_time`, the lowest value is `30s` (30 seconds), the highest value is `600s` (10 minutes). You can also pass `1m`, `2m` etc when you try to configure by minute level. e.g., _wss://stream-testnet.bybit.com/v5/private?max_active_time=1m_.

In general, if there is no "ping-pong" and no stream data sent from server end, the connection will be cut off after 10 minutes. When you have a particular need, you can configure connection alive time by `max_active_time`.

Since ticker scans every 30s, so it is not fully exact, i.e., if you configure 45s, and your last update or ping-pong is occurred on `2023-08-15 17:27:23`, your disconnection time maybe happened on `2023-08-15 17:28:15`

## Authentication

info

**Public** topics do not require authentication. The following section applies to **private** topics only.

Apply for authentication when establishing a connection.

Note: if you're using [pybit](https://github.com/bybit-exchange/pybit), [bybit-api](https://www.npmjs.com/package/bybit-api), or another high-level library, you can ignore this code - as authentication is handled for you.
    
    
    {  
        "req_id": "10001", // optional  
        "op": "auth",  
        "args": [  
            "api_key",  
            1662350400000, // expires; is greater than your current timestamp  
            "signature"  
        ]  
    }  
    
    
    
    # based on: https://github.com/bybit-exchange/pybit/blob/master/pybit/_http_manager.py  
      
    import hmac  
    import json  
    import time  
    import websocket  
      
    api_key = ""  
    api_secret = ""  
      
    # Generate expires.  
    expires = int((time.time() + 1) * 1000)  
      
    # Generate signature.  
    signature = str(hmac.new(  
        bytes(api_secret, "utf-8"),  
        bytes(f"GET/realtime{expires}", "utf-8"), digestmod="sha256"  
    ).hexdigest())  
      
    ws = websocket.WebSocketApp(  
        url=url,  
        ...  
    )  
      
    # Authenticate with API.  
    ws.send(  
        json.dumps({  
            "op": "auth",  
            "args": [api_key, expires, signature]  
        })  
    )  
    

> Successful authentication sample response
    
    
    {  
        "success": true,  
        "ret_msg": "",  
        "op": "auth",  
        "conn_id": "cejreaspqfh3sjdnldmg-p"  
    }  
    

note

Example signature algorithms can be found [here](https://github.com/bybit-exchange/api-usage-examples).

caution

Due to network complexity, your may get disconnected at any time. Please follow the instructions below to ensure that you receive WebSocket messages on time:

  1. Keep connection alive by [sending the heartbeat packet](/docs/v5/ws/connect#how-to-send-the-heartbeat-packet)
  2. Reconnect as soon as possible if disconnected



## IP Limits

  * Do not frequently connect and disconnect the connection.
  * Do not build over 500 connections in 5 minutes. This is counted per WebSocket domain.



## Public channel - Args limits

Regardless of Perpetual, Futures, Options or Spot, for one public connection, you cannot have length of "args" array over 21,000 characters.

  * Spot can input up to 10 args for each subscription request sent to one connection
  * Options can input up to 2000 args for a single connection
  * No args limit for Futures and Spread for now



## How to Send the Heartbeat Packet

> How to Send
    
    
    // req_id is a customised ID, which is optional  
    ws.send(JSON.stringify({"req_id": "100001", "op": "ping"}));  
    

> Pong message example of public channels

  * Spot
  * Linear/Inverse
  * Option/Spread


    
    
    {  
        "success": true,  
        "ret_msg": "pong",  
        "conn_id": "0970e817-426e-429a-a679-ff7f55e0b16a",  
        "op": "ping"  
    }  
    
    
    
    {  
        "success": true,  
        "ret_msg": "pong",  
        "conn_id": "465772b1-7630-4fdc-a492-e003e6f0f260",  
        "req_id": "",  
        "op": "ping"  
    }  
    
    
    
    {  
        "args": [  
            "1672916271846"  
        ],  
        "op": "pong"  
    }  
    

> Pong message example of private channels
    
    
    {  
        "req_id": "test",  
        "op": "pong",  
        "args": [  
            "1675418560633"  
        ],  
        "conn_id": "cfcb4ocsvfriu23r3er0-1b"  
    }  
    

caution

To avoid network or program issues, we recommend that you send the `ping` heartbeat packet every **20** seconds to maintain the WebSocket connection.

## How to Subscribe to Topics

### Understanding WebSocket Filters

How to subscribe with a filter
    
    
    // Subscribing level 1 orderbook  
    {  
        "req_id": "test", // optional  
        "op": "subscribe",  
        "args": [  
            "orderbook.1.BTCUSDT"  
        ]  
    }  
    

Subscribing with multiple symbols and topics is supported.
    
    
    {  
        "req_id": "test", // optional  
        "op": "subscribe",  
        "args": [  
            "orderbook.1.BTCUSDT",  
            "publicTrade.BTCUSDT",  
            "orderbook.1.ETHUSDT"  
        ]  
    }  
    

### Understanding WebSocket Filters: Unsubscription

You can dynamically subscribe and unsubscribe from topics without unsubscribing from the WebSocket like so:
    
    
    {  
        "op": "unsubscribe",  
        "args": [  
            "publicTrade.ETHUSD"  
        ],  
        "req_id": "customised_id"  
    }  
    

## Understanding the Subscription Response

> Topic subscription response message example

  * Private
  * Public Spot
  * Linear/Inverse
  * Option/Spread


    
    
    {  
        "success": true,  
        "ret_msg": "",  
        "op": "subscribe",  
        "conn_id": "cejreassvfrsfvb9v1a0-2m"  
    }  
    
    
    
    {  
        "success": true,  
        "ret_msg": "subscribe",  
        "conn_id": "2324d924-aa4d-45b0-a858-7b8be29ab52b",  
        "req_id": "10001",  
        "op": "subscribe"  
    }  
    
    
    
    {  
        "success": true,  
        "ret_msg": "",  
        "conn_id": "3cd84cb1-4d06-4a05-930a-2efe5fc70f0f",  
        "req_id": "",  
        "op": "subscribe"  
    }  
    
    
    
    {  
        "success": true,  
        "conn_id": "aa01fbfffe80af37-00000001-000b37b9-7147f432704fd28c-00e1c172",  
        "data": {  
        "failTopics": [],  
        "successTopics": [  
            "orderbook.100.BTC-6JAN23-18000-C"  
        ]  
    },  
        "type": "COMMAND_RESP"  
    }

---

# 訂閱WebSocket

**[WebSocket公共頻道](/docs/zh-TW/v5/websocket/public/orderbook):**

  * **主網:**  
現貨: `wss://stream.bybit.com/v5/public/spot`  
USDT, USDC永續 & USDC交割: `wss://stream.bybit.com/v5/public/linear`  
反向合約: `wss://stream.bybit.com/v5/public/inverse`  
期權: `wss://stream.bybit.com/v5/public/option`  
RFQ: `wss://stream.bybit.com/v5/public/rfq`  
價差交易: `wss://stream.bybit.com/v5/public/spread`

  * **測試網:**  
現貨: `wss://stream-testnet.bybit.com/v5/public/spot`  
USDT和USDC永續: `wss://stream-testnet.bybit.com/v5/public/linear`  
反向合約: `wss://stream-testnet.bybit.com/v5/public/inverse`  
期權: `wss://stream-testnet.bybit.com/v5/public/option`  
RFQ: `wss://stream-testnet.bybit.com/v5/public/rfq`  
價差交易: `wss://stream-testnet.bybit.com/v5/public/spread`




**[WebSocket私有頻道](/docs/zh-TW/v5/websocket/private/order):**

  * **主網:**  
`wss://stream.bybit.com/v5/private`

  * **測試網:**  
`wss://stream-testnet.bybit.com/v5/private`




**[WebSocket交易](/docs/zh-TW/v5/websocket/trade/guideline):**

  * **主網:**  
`wss://stream.bybit.com/v5/trade` (價差交易不支持)

  * **測試網:**  
`wss://stream-testnet.bybit.com/v5/trade` (價差交易不支持)




**[Websocket取得系統狀態](/docs/zh-TW/v5/websocket/system/system-status):**

  * **主網:**  
`wss://stream.bybit.com/v5/public/misc/status`

  * **測試網:**  
`wss://stream-testnet.bybit.com/v5/public/misc/status`




信息

  * 如果您的帳戶是在 [www.bybit.tr](http://www.bybit.tr) 註冊, 請使用`stream.bybit.tr`進行主網連接
  * 如果您的帳戶是在 [www.bybit.kz](http://www.bybit.kz), 請使用 `stream.bybit.kz` 進行主網連接
  * 如果您的帳戶是在 [www.bybitgeorgia.ge](http://www.bybitgeorgia.ge) 註冊, 請使用 `stream.bybitgeorgia.ge` 進行主網連接



自定義私有連接存活時長

針對私有頻道和交易, 您可以自定義連接存活時長, 通過增加參數`max_active_time`, 最小支持`30s` (30秒), 最大支持`600s` (10分鐘). 如果您需要按分鐘級別配置, 您也可以傳遞`1m`, `2m`等. 例如, _wss://stream-testnet.bybit.com/v5/private?max_active_time=1m_.

一般來說, 當客戶端與服務端沒有上下行數據, 包括心跳和交易數據下發, 那麼該連接會在最後一條交互後維持10分鐘, 由服務端斷開. 當您由特別的需求時, 可以通過該字段`max_active_time`自行控制存活時間.

由於系統每30秒掃描一次, 因此配置的時長可能無法非常精確, 換句話說, 如果您配置了45秒, 然後最後一條數據下發或者心跳發生在`2023-08-15 17:27:23`, 您的私有連接可能在`2023-08-15 17:28:15`發生斷連.

## 鑒權

信息

**公共頻道** 不需要鑒權，以下部分僅適用於**私有頻道** 的訂閱。

構建連接時，創建鑒權請求。

注意: 如果您正在使用[pybit](https://github.com/bybit-exchange/pybit), [bybit-api](https://www.npmjs.com/package/bybit-api)或者其他第三方庫, 您可以忽略此項-因為鑒權已經內建。
    
    
    {  
        "req_id": "10001", // 可選項  
        "op": "auth",  
        "args": [  
            "api_key",  
            1662350400000, //過期時間應當大於當前時間戳  
            "singature"  
        ]  
    }  
    
    
    
    # based on: https://github.com/bybit-exchange/pybit/blob/master/pybit/_http_manager.py  
      
    import hmac  
    import json  
    import time  
    import websocket  
      
    api_key = ""  
    api_secret = ""  
      
    # Generate expires.  
    expires = int((time.time() + 1) * 1000)  
      
    # Generate signature.  
    signature = str(hmac.new(  
        bytes(api_secret, "utf-8"),  
        bytes(f"GET/realtime{expires}", "utf-8"), digestmod="sha256"  
    ).hexdigest())  
      
    ws = websocket.WebSocketApp(  
        url=url,  
        ...  
    )  
      
    # Authenticate with API.  
    ws.send(  
        json.dumps({  
            "op": "auth",  
            "args": [api_key, expires, signature]  
        })  
    )  
    

> 鑒權成功的響應示例
    
    
    {  
        "success": true,  
        "ret_msg": "",  
        "op": "auth",  
        "conn_id": "cejreaspqfh3sjdnldmg-p"  
    }  
    

備註

簽名生成的示例可以參考[這裡](https://github.com/bybit-exchange/api-usage-examples)。

警告

由於網絡的複雜性，您可能隨時遇到斷連。請參考以下建議確保您能即時接收到推送：

  1. 通過發送[心跳](/docs/zh-TW/v5/ws/connect#%E5%A6%82%E4%BD%95%E7%99%BC%E9%80%81%E5%BF%83%E8%B7%B3)來維持連接;
  2. 遇到斷連時，立即重新連接。



## IP限頻

  * 不要嘗試頻繁地構建連接與斷開連接；
  * 不要在5分鐘內構建超過500個連接。



## 公有頻道訂閱參數限制

不管是期貨、現貨、期權, 對於單個連接, args裡的數組元素長度總和不能超過21,000個字符

  * 現貨每次向單一連接僅能發送不超過10個參數的訂閱請求，但單個連接沒有args訂閱限制
  * 期權單個連接，至多訂閱2000個args
  * 期貨和價差交易單個連接沒有args限制



## 如何發送心跳
    
    
    // req_id is a customised id, which is optional  
    ws.send(JSON.stringify({"req_id": "100001", "op": "ping"}));  
    

> 公共頻道接收到pong的響應示例

  * 現貨
  * 期貨
  * 期權


    
    
    {  
        "success": true,  
        "ret_msg": "pong",  
        "conn_id": "0970e817-426e-429a-a679-ff7f55e0b16a",  
        "op": "ping"  
    }  
    
    
    
    {  
        "success": true,  
        "ret_msg": "pong",  
        "conn_id": "465772b1-7630-4fdc-a492-e003e6f0f260",  
        "req_id": "",  
        "op": "ping"  
    }  
    
    
    
    {  
        "args": [  
        "1672916271846"  
        ],  
        "op": "pong"  
    }  
    

> 私有頻道接收到pong的響應示例
    
    
    {  
        "req_id": "test",  
        "op": "pong",  
        "args": [  
            "1675418560633"  
        ],  
        "conn_id": "cfcb4ocsvfriu23r3er0-1b"  
    }  
    

警告

為了維持連接，我們推薦您每**20** 秒發送一次心跳。

## 如何訂閱topic

### 理解Websocket裡的args

通過傳入args來訂閱指定topic
    
    
    // 訂閱1檔的orderbook  
    {  
        "req_id": "test", // 可選  
        "op": "subscribe",  
        "args": [  
            "orderbook.1.BTCUSDT"  
        ]  
    }  
    

通過逗號隔開，可以同時訂閱多個topic或者多個symbol
    
    
    {  
        "req_id": "test", // 可選  
        "op": "subscribe",  
        "args": [  
            "orderbook.1.BTCUSDT",  
            "publicTrade.BTCUSDT",  
            "orderbook.1.ETHUSDT"  
        ]  
    }  
    

### 理解如何取消訂閱

您可以通過發送請求來動態地停止訂閱:
    
    
    {  
        "op": "unsubscribe",  
        "args": [  
            "publicTrade.ETHUSD"  
        ],  
        "req_id": "customised_id"  
    }  
    

## 理解訂閱的響應

> 訂閱成功後的響應示例

  * 私有頻道
  * 公有現貨
  * 公有期貨
  * 公有期權


    
    
    {  
        "success": true,  
        "ret_msg": "",  
        "op": "subscribe",  
        "conn_id": "cejreassvfrsfvb9v1a0-2m"  
    }  
    
    
    
    {  
        "success": true,  
        "ret_msg": "subscribe",  
        "conn_id": "2324d924-aa4d-45b0-a858-7b8be29ab52b",  
        "req_id": "10001",  
        "op": "subscribe"  
    }  
    
    
    
    {  
        "success": true,  
        "ret_msg": "",  
        "conn_id": "3cd84cb1-4d06-4a05-930a-2efe5fc70f0f",  
        "req_id": "",  
        "op": "subscribe"  
    }  
    
    
    
    {  
        "success": true,  
        "conn_id": "aa01fbfffe80af37-00000001-000b37b9-7147f432704fd28c-00e1c172",  
        "data": {  
        "failTopics": [],  
        "successTopics": [  
        "orderbook.100.BTC-6JAN23-18000-C"  
        ]  
    },  
        "type": "COMMAND_RESP"  
    }