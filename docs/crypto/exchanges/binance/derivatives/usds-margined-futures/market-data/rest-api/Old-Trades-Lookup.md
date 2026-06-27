---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Old-Trades-Lookup
api_type: Market Data
updated_at: 2026-01-15T23:46:56.520693
---

# Old Trades Lookup (MARKET_DATA)

## API Description[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Old-Trades-Lookup#api-description "Direct link to API Description")

Get older market historical trades.

## HTTP Request[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Old-Trades-Lookup#http-request "Direct link to HTTP Request")

GET `/fapi/v1/historicalTrades`

## Request Weight[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Old-Trades-Lookup#request-weight "Direct link to Request Weight")

**20**

## Request Parameters[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Old-Trades-Lookup#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
limit| INT| NO| Default 100; max 500.  
fromId| LONG| NO| TradeId to fetch from. Default gets most recent trades.  
  
>   * Market trades means trades filled in the order book. Only market trades will be returned, which means the insurance fund trades and ADL trades won't be returned.
>   * Only supports data from within the last three months
> 


## Response Example[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Old-Trades-Lookup#response-example "Direct link to Response Example")
    
    
    [  
      {  
        "id": 28457,  
        "price": "4.00000100",  
        "qty": "12.00000000",  
        "quoteQty": "8000.00",  
        "time": 1499865549590,  
        "isBuyerMaker": true,  
        "isRPITrade": true,  
      }  
    ]

---

# 查询历史成交(MARKET_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Old-Trades-Lookup#接口描述 "接口描述的直接链接")

查询订单簿历史成交

## HTTP请求[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Old-Trades-Lookup#http请求 "HTTP请求的直接链接")

GET `/fapi/v1/historicalTrades`

## 请求权重[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Old-Trades-Lookup#请求权重 "请求权重的直接链接")

**20**

## 请求参数[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Old-Trades-Lookup#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES| 交易对  
limit| INT| NO| 默认值:100 最大值:500.  
fromId| LONG| NO| 从哪一条成交id开始返回. 缺省返回最近的成交记录  
  
>   * 仅返回订单簿成交，即不会返回保险基金和自动减仓(ADL)成交
>   * 仅支持返回最近3个月的数据
> 


## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Old-Trades-Lookup#响应示例 "响应示例的直接链接")
    
    
    [  
      {  
        "id": 28457,				// 成交ID  
        "price": "4.00000100",		// 成交价格  
        "qty": "12.00000000",		// 成交量  
        "quoteQty": "48.00",		// 成交额  
        "time": 1499865549590,		// 时间  
        "isBuyerMaker": true		// 买方是否为挂单方  
        "isRPITrade": true		// Maker方是否为RPI挂单  
      }  
    ]