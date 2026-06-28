---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/websocket-api/Symbol-Price-Ticker
api_type: WebSocket
updated_at: 2026-01-15T23:47:06.149765
---

# Symbol Price Ticker

## API Description[​](/docs/derivatives/usds-margined-futures/market-data/websocket-api/Symbol-Price-Ticker#api-description "Direct link to API Description")

Latest price for a symbol or symbols.

## Method[​](/docs/derivatives/usds-margined-futures/market-data/websocket-api/Symbol-Price-Ticker#method "Direct link to Method")

`ticker.price`

## Request[​](/docs/derivatives/usds-margined-futures/market-data/websocket-api/Symbol-Price-Ticker#request "Direct link to Request")
    
    
    {  
       	"id": "9d32157c-a556-4d27-9866-66760a174b57",  
        "method": "ticker.price",  
        "params": {  
            "symbol": "BTCUSDT"  
        }  
    }  
    

**Weight:**

**1** for a single symbol;  
**2** when the symbol parameter is omitted

## Request Parameters[​](/docs/derivatives/usds-margined-futures/market-data/websocket-api/Symbol-Price-Ticker#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| NO|   
  
>   * If the symbol is not sent, prices for all symbols will be returned in an array.
> 


## Response Example[​](/docs/derivatives/usds-margined-futures/market-data/websocket-api/Symbol-Price-Ticker#response-example "Direct link to Response Example")
    
    
    {  
      "id": "9d32157c-a556-4d27-9866-66760a174b57",  
      "status": 200,  
      "result": {  
    	"symbol": "BTCUSDT",  
    	"price": "6000.01",  
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
        	"symbol": "BTCUSDT",  
          	"price": "6000.01",  
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

# 最新价格

## 接口描述[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/websocket-api/Symbol-Price-Ticker#接口描述 "接口描述的直接链接")

返回最近价格

## 方式[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/websocket-api/Symbol-Price-Ticker#方式 "方式的直接链接")

`ticker.price`

## 请求[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/websocket-api/Symbol-Price-Ticker#请求 "请求的直接链接")
    
    
    {  
       	"id": "9d32157c-a556-4d27-9866-66760a174b57",  
        "method": "ticker.price",  
        "params": {  
            "symbol": "BTCUSDT"  
        }  
    }  
    

## 请求权重[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/websocket-api/Symbol-Price-Ticker#请求权重 "请求权重的直接链接")

单交易对**1** ，无交易对**2**

## 请求参数[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/websocket-api/Symbol-Price-Ticker#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| NO| 交易对  
  
>   * 不发送交易对参数，则会返回所有交易对信息
> 


## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/websocket-api/Symbol-Price-Ticker#响应示例 "响应示例的直接链接")
    
    
    {  
      "id": "9d32157c-a556-4d27-9866-66760a174b57",  
      "status": 200,  
      "result": {  
    	"symbol": "BTCUSDT",  
    	"price": "6000.01",  
    	"time": 1589437530011     
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
    	   "symbol": "BTCUSDT",  
    	   "price": "6000.01",  
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