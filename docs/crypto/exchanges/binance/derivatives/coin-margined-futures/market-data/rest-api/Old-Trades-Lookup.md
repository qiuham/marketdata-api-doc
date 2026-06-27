---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/rest-api/Old-Trades-Lookup
api_type: Market Data
updated_at: 2026-01-15T23:38:29.544107
---

# Old Trades Lookup(MARKET_DATA)

## API Description[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Old-Trades-Lookup#api-description "Direct link to API Description")

Get older market historical trades.

## HTTP Request[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Old-Trades-Lookup#http-request "Direct link to HTTP Request")

GET `/dapi/v1/historicalTrades`

## Request Weight[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Old-Trades-Lookup#request-weight "Direct link to Request Weight")

**20**

## Request Parameters[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Old-Trades-Lookup#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
limit| INT| NO| Default 100; max 500.  
fromId| LONG| NO| TradeId to fetch from. Default gets most recent trades.  
  
>   * Market trades means trades filled in the order book. Only market trades will be returned, which means the insurance fund trades and ADL trades won't be returned.
> 


## Response Example[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Old-Trades-Lookup#response-example "Direct link to Response Example")
    
    
    [  
      {  
        "id": 595103,  
        "price": "9642.2",  
        "qty": "1",  
        "baseQty": "0.01037108",  
        "time": 1499865549590,  
        "isBuyerMaker": true,  
      }  
    ]

---

# 查询历史成交 (MARKET_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/coin-margined-futures/market-data/rest-api/Old-Trades-Lookup#接口描述 "接口描述的直接链接")

查询订单簿历史成交

## HTTP请求[​](/docs/zh-CN/derivatives/coin-margined-futures/market-data/rest-api/Old-Trades-Lookup#http请求 "HTTP请求的直接链接")

GET `/dapi/v1/historicalTrades`

## 请求权重[​](/docs/zh-CN/derivatives/coin-margined-futures/market-data/rest-api/Old-Trades-Lookup#请求权重 "请求权重的直接链接")

**20**

## 请求参数[​](/docs/zh-CN/derivatives/coin-margined-futures/market-data/rest-api/Old-Trades-Lookup#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES| 交易对  
limit| INT| NO| 默认值:100 最大值:500.  
fromId| LONG| NO| 从哪一条成交id开始返回. 缺省返回最近的成交记录  
  
>   * 仅返回订单簿成交，即不会返回保险基金和自动减仓(ADL)成交
> 


## 响应示例[​](/docs/zh-CN/derivatives/coin-margined-futures/market-data/rest-api/Old-Trades-Lookup#响应示例 "响应示例的直接链接")
    
    
    [  
      {  
        "id": 595103,				// 成交ID  
        "price": "9642.2",			// 成交价格  
        "qty": "1",					// 成交量(张数)  
        "baseQty": "0.01037108",	// 成交额(标的物数量)  
        "time": 1499865549590,		// 时间  
        "isBuyerMaker": true		// 买方是否为挂单方  
      }  
    ]