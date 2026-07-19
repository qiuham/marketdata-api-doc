---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#public-data-websocket-liquidation-orders-channel
anchor_id: public-data-websocket-liquidation-orders-channel
api_type: WebSocket
updated_at: 2026-07-19 19:16:33.361769
---

# Liquidation orders channel

Retrieve the recent liquidation orders. This data doesn’t represent the total number of liquidations on OKX.

#### URL Path

/ws/v5/public

> Request Example
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "liquidation-orders",
          "instType": "SWAP"
        }
      ]
    }
    
    
    
    import asyncio
    from okx.websocket.WsPublicAsync import WsPublicAsync
    
    def callbackFunc(message):
        print(message)
    
    async def main():
        ws = WsPublicAsync(url="wss://wspap.okx.com:8443/ws/v5/public")
        await ws.start()
        args = [
            {
              "channel": "liquidation-orders",
              "instType": "SWAP"
            }
        ]
    
        await ws.subscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
        await ws.unsubscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
    asyncio.run(main())
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
id | String | No | Unique identifier of the message   
Provided by client. It will be returned in response message for identifying the corresponding request.   
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
op | String | Yes | Operation  
`subscribe`  
`unsubscribe`  
args | Array of objects | Yes | List of subscribed channels  
> channel | String | Yes | Channel name  
`liquidation-orders`  
> instType | String | Yes | Instrument type  
`SWAP`  
`FUTURES`  
`MARGIN`  
`OPTION`  
  
> Response Example
    
    
    {
        "id": "1512",
        "arg": {
            "channel": "liquidation-orders",
            "instType": "SWAP"
        },
        "data": [
            {
                "details": [
                    {
                        "bkLoss": "0",
                        "bkPx": "0.007831",
                        "ccy": "",
                        "posSide": "short",
                        "side": "buy",
                        "sz": "13",
                        "ts": "1692266434010"
                    }
                ],
                "instFamily": "IOST-USDT",
                "instId": "IOST-USDT-SWAP",
                "instType": "SWAP",
                "uly": "IOST-USDT"
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
id | String | Unique identifier of the message  
arg | Object | Successfully subscribed channel  
> channel | String | Channel name  
> instId | String | Instrument ID  
data | Array of objects | Subscribed data  
> instType | String | Instrument type  
> instId | String | Instrument ID, e.g. `BTC-USD-SWAP`  
> uly | String | Underlying  
Applicable to `FUTURES`/`SWAP`/`OPTION`  
> details | Array of objects | Liquidation details  
>> side | String | Order side  
`buy`  
`sell`  
Applicable to `FUTURES`/`SWAP`  
>> posSide | String | Position mode side  
`long`: Hedge mode long  
`short`: Hedge mode short  
`net`: Net mode  
>> bkPx | String | Liquidation mark price. The price of the transaction with the system's liquidation account, only applicable to `FUTURES`/`SWAP`  
>> sz | String | Quantity of liquidation, only applicable to `MARGIN`/`FUTURES`/`SWAP`.  
For `MARGIN`, the unit is base currency.   
For `FUTURES/SWAP`, the unit is contract.  
>> bkLoss | String | Bankruptcy loss  
>> ccy | String | Liquidation currency, only applicable to `MARGIN`  
>> ts | String | Liquidation time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
Liquidation data comes from different data sources, so the updated data is not necessarily in chronological order.

---

# 平台公共爆仓单频道

获取爆仓单信息。显示的强平数据并不准确代表欧易的总强平量，亦不应被当做总强平量使用。

#### URL Path

/ws/v5/public

> 请求示例
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "liquidation-orders",
          "instType": "SWAP"
        }
      ]
    }
    
    
    
    import asyncio
    from okx.websocket.WsPublicAsync import WsPublicAsync
    
    def callbackFunc(message):
        print(message)
    
    async def main():
        ws = WsPublicAsync(url="wss://wspap.okx.com:8443/ws/v5/public")
        await ws.start()
        args = [
            {
              "channel": "liquidation-orders",
              "instType": "SWAP"
            }
        ]
    
        await ws.subscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
        await ws.unsubscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
    asyncio.run(main())
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
id | String | 否 | 消息的唯一标识。  
用户提供，返回参数中会返回以便于找到相应的请求。  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度必须要在1-32位之间。  
op | String | 是 | 操作  
`subscribe`  
`unsubscribe`  
args | Array of objects | 是 | 请求订阅的频道  
> channel | String | 是 | 频道名  
`liquidation-orders`  
> instType | String | 是 | 产品类型  
`MARGIN`：币币杠杆  
`SWAP`：永续合约  
`FUTURES`：交割合约  
`OPTION`：期权  
  
> 返回结果
    
    
    {
      "id": "1512",
        "arg": {
            "channel": "liquidation-orders",
            "instType": "SWAP"
        },
        "data": [
            {
                "details": [
                    {
                        "bkLoss": "0",
                        "bkPx": "0.007831",
                        "ccy": "",
                        "posSide": "short",
                        "side": "buy",
                        "sz": "13",
                        "ts": "1692266434010"
                    }
                ],
                "instFamily": "IOST-USDT",
                "instId": "IOST-USDT-SWAP",
                "instType": "SWAP",
                "uly": "IOST-USDT"
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
id | String | 消息的唯一标识  
arg | Object | 订阅成功的频道  
> channel | String | 频道名  
> instType | String | 产品类型  
data | Array of objects | 订阅的数据  
> instType | String | 产品类型  
> instId | String | 产品ID，如 `BTC-USD-SWAP`  
> uly | String | 标的指数  
适用于`交割`/`永续`/`期权`  
> details | Array of objects | 详细内容  
>> side | String | 订单方向  
`buy`：买  
`sell`：卖  
仅适用于`交割`/`永续`  
>> posSide | String | 持仓模式方向  
`long`：开平仓模式开多  
`short`：开平仓模式开空  
`net`：买卖模式  
>> bkPx | String | 强平标记价格，与系统爆仓账号委托成交的价格，仅适用于`交割/永续`  
>> sz | String | 强平数量  
适用于`杠杆`/`交割`/`永续`  
对于`杠杆`，单位为交易货币。  
对于`交割/永续`，单位为张。  
>> bkLoss | String | 穿仓亏损数量  
>> ccy | String | 强平币种  
适用于`币币杠杆`  
>> ts | String | 强平发生的时间，Unix时间戳的毫秒数格式，如 `1597026383085` /  
爆仓数据来自不同的数据源，因此推送的数据在时间上不一定是顺序的。