---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/websocket-api/Symbol-Order-Book-Ticker
api_type: WebSocket
updated_at: 2026-01-15T23:47:06.083200
---

# Symbol Order Book Ticker

## API Description[​](/docs/derivatives/usds-margined-futures/market-data/websocket-api/Symbol-Order-Book-Ticker#api-description "Direct link to API Description")

Best price/qty on the order book for a symbol or symbols.

## Method[​](/docs/derivatives/usds-margined-futures/market-data/websocket-api/Symbol-Order-Book-Ticker#method "Direct link to Method")

`ticker.book`

**Note** :

> Retail Price Improvement(RPI) orders are not visible and excluded in the response message.

## Request[​](/docs/derivatives/usds-margined-futures/market-data/websocket-api/Symbol-Order-Book-Ticker#request "Direct link to Request")
    
    
    {  
        "id": "9d32157c-a556-4d27-9866-66760a174b57",  
        "method": "ticker.book",  
        "params": {  
            "symbol": "BTCUSDT"  
        }  
    }  
    

## Request Weight[​](/docs/derivatives/usds-margined-futures/market-data/websocket-api/Symbol-Order-Book-Ticker#request-weight "Direct link to Request Weight")

**2** for a single symbol;  
**5** when the symbol parameter is omitted

## Request Parameters[​](/docs/derivatives/usds-margined-futures/market-data/websocket-api/Symbol-Order-Book-Ticker#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| NO|   
  
>   * If the symbol is not sent, bookTickers for all symbols will be returned in an array.
>   * The field `X-MBX-USED-WEIGHT-1M` in response header is not accurate from this endpoint, please ignore.
> 


## Response Example[​](/docs/derivatives/usds-margined-futures/market-data/websocket-api/Symbol-Order-Book-Ticker#response-example "Direct link to Response Example")
    
    
    {  
      "id": "9d32157c-a556-4d27-9866-66760a174b57",  
      "status": 200,  
      "result": {  
        "lastUpdateId": 1027024,  
        "symbol": "BTCUSDT",  
        "bidPrice": "4.00000000",  
        "bidQty": "431.00000000",  
        "askPrice": "4.00000200",  
        "askQty": "9.00000000",  
        "time": 1589437530011   // Transaction time  
      },  
      "rateLimits": [  
        {  
          "rateLimitType": "REQUEST_WEIGHT",  
          "interval": "MINUTE",  
          "intervalNum": 1,  
          "limit": 2400,  
          "count": 2  
        }  
      ]  
    }  
    

> OR
    
    
    {  
      "id": "9d32157c-a556-4d27-9866-66760a174b57",  
      "status": 200,  
      "result": [  
        {  
          "lastUpdateId": 1027024,  
          "symbol": "BTCUSDT",  
          "bidPrice": "4.00000000",  
          "bidQty": "431.00000000",  
          "askPrice": "4.00000200",  
          "askQty": "9.00000000",  
          "time": 1589437530011  
        }  
      ],  
      "rateLimits": [  
        {  
          "rateLimitType": "REQUEST_WEIGHT",  
          "interval": "MINUTE",  
          "intervalNum": 1,  
          "limit": 2400,  
          "count": 2  
        }  
      ]  
    }

---

# 当前最优挂单

## 接口描述[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/websocket-api/Symbol-Order-Book-Ticker#接口描述 "接口描述的直接链接")

返回当前最优的挂单(最高买单，最低卖单)

## 方式[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/websocket-api/Symbol-Order-Book-Ticker#方式 "方式的直接链接")

`ticker.book`

**注意：** 响应消息不包含RPI订单，其不可见。

## 请求[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/websocket-api/Symbol-Order-Book-Ticker#请求 "请求的直接链接")
    
    
    {  
        "id": "9d32157c-a556-4d27-9866-66760a174b57",  
        "method": "ticker.book",  
        "params": {  
            "symbol": "BTCUSDT"  
        }  
    }  
    

## 请求权重[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/websocket-api/Symbol-Order-Book-Ticker#请求权重 "请求权重的直接链接")

单交易对**2** ，无交易对**5**

## 请求参数[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/websocket-api/Symbol-Order-Book-Ticker#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| NO| 交易对  
  
>   * 不发送交易对参数，则会返回所有交易对信息
>   * 该接口返回头中的`X-MBX-USED-WEIGHT-1M`参数不准确，可以忽略
> 


## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/websocket-api/Symbol-Order-Book-Ticker#响应示例 "响应示例的直接链接")
    
    
    {  
      "id": "9d32157c-a556-4d27-9866-66760a174b57",  
      "status": 200,  
      "result": {  
        "lastUpdateId": 1027024,  
        "symbol": "BTCUSDT", // 交易对  
        "bidPrice": "4.00000000", //最优买单价  
        "bidQty": "431.00000000", //挂单量  
        "askPrice": "4.00000200", //最优卖单价  
        "askQty": "9.00000000", //挂单量  
        "time": 1589437530011   // 撮合引擎时间  
      },  
      "rateLimits": [  
        {  
          "rateLimitType": "REQUEST_WEIGHT",  
          "interval": "MINUTE",  
          "intervalNum": 1,  
          "limit": 2400,  
          "count": 2  
        }  
      ]  
    }  
    

> 或(当不发送symbol)
    
    
    {  
      "id": "9d32157c-a556-4d27-9866-66760a174b57",  
      "status": 200,  
      "result": [  
    	{  
          "lastUpdateId": 1027024,  
          "symbol": "BTCUSDT", // 交易对  
          "bidPrice": "4.00000000", //最优买单价  
          "bidQty": "431.00000000", //挂单量  
          "askPrice": "4.00000200", //最优卖单价  
          "askQty": "9.00000000", //挂单量  
          "time": 1589437530011   // 撮合引擎时间  
        }  
     ]  
      "rateLimits": [  
        {  
          "rateLimitType": "REQUEST_WEIGHT",  
          "interval": "MINUTE",  
          "intervalNum": 1,  
          "limit": 2400,  
          "count": 2  
        }  
      ]  
    }