---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Symbol-Order-Book-Ticker
api_type: Market Data
updated_at: 2026-01-15T23:47:00.292381
---

# Symbol Order Book Ticker

## API Description[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Symbol-Order-Book-Ticker#api-description "Direct link to API Description")

Best price/qty on the order book for a symbol or symbols.

## HTTP Request[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Symbol-Order-Book-Ticker#http-request "Direct link to HTTP Request")

GET `/fapi/v1/ticker/bookTicker`

**Note** :

> Retail Price Improvement(RPI) orders are not visible and excluded in the response message.

## Request Weight[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Symbol-Order-Book-Ticker#request-weight "Direct link to Request Weight")

**2** for a single symbol;  
**5** when the symbol parameter is omitted

## Request Parameters[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Symbol-Order-Book-Ticker#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| NO|   
  
>   * If the symbol is not sent, bookTickers for all symbols will be returned in an array.
>   * The field `X-MBX-USED-WEIGHT-1M` in response header is not accurate from this endpoint, please ignore.
> 


## Response Example[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Symbol-Order-Book-Ticker#response-example "Direct link to Response Example")
    
    
    {  
      "symbol": "BTCUSDT",  
      "bidPrice": "4.00000000",  
      "bidQty": "431.00000000",  
      "askPrice": "4.00000200",  
      "askQty": "9.00000000",  
      "time": 1589437530011   // Transaction time  
    }  
    

> OR
    
    
    [  
    	{  
      		"symbol": "BTCUSDT",  
      		"bidPrice": "4.00000000",  
      		"bidQty": "431.00000000",  
      		"askPrice": "4.00000200",  
      		"askQty": "9.00000000",  
      		"time": 1589437530011  
    	}  
    ]

---

# 当前最优挂单

## 接口描述[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Symbol-Order-Book-Ticker#接口描述 "接口描述的直接链接")

返回当前最优的挂单(最高买单，最低卖单)

## HTTP请求[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Symbol-Order-Book-Ticker#http请求 "HTTP请求的直接链接")

GET `/fapi/v1/ticker/bookTicker`

**注意：** 响应消息不包含RPI订单，其不可见。

## 请求权重[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Symbol-Order-Book-Ticker#请求权重 "请求权重的直接链接")

单交易对**2** ，无交易对**5**

## 请求参数[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Symbol-Order-Book-Ticker#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| NO| 交易对  
  
>   * 不发送交易对参数，则会返回所有交易对信息
>   * 该接口返回头中的`X-MBX-USED-WEIGHT-1M`参数不准确，可以忽略
> 


## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Symbol-Order-Book-Ticker#响应示例 "响应示例的直接链接")
    
    
    {  
      "symbol": "BTCUSDT", // 交易对  
      "bidPrice": "4.00000000", //最优买单价  
      "bidQty": "431.00000000", //挂单量  
      "askPrice": "4.00000200", //最优卖单价  
      "askQty": "9.00000000", //挂单量  
      "time": 1589437530011   // 撮合引擎时间  
    }  
    

> 或(当不发送symbol)
    
    
    [  
    	{  
      		"symbol": "BTCUSDT", // 交易对  
      		"bidPrice": "4.00000000", //最优买单价  
      		"bidQty": "431.00000000", //挂单量  
      		"askPrice": "4.00000200", //最优卖单价  
      		"askQty": "9.00000000", //挂单量  
      		"time": 1589437530011   // 撮合引擎时间  
    	}  
    ]