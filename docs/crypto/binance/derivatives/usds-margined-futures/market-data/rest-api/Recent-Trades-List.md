---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Recent-Trades-List
api_type: Market Data
updated_at: 2026-01-15T23:47:00.225197
---

# Recent Trades List

## API Description[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Recent-Trades-List#api-description "Direct link to API Description")

Get recent market trades

## HTTP Request[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Recent-Trades-List#http-request "Direct link to HTTP Request")

GET `/fapi/v1/trades`

## Request Weight[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Recent-Trades-List#request-weight "Direct link to Request Weight")

**5**

## Request Parameters[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Recent-Trades-List#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
limit| INT| NO| Default 500; max 1000.  
  
>   * Market trades means trades filled in the order book. Only market trades will be returned, which means the insurance fund trades and ADL trades won't be returned.
> 


## Response Example[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Recent-Trades-List#response-example "Direct link to Response Example")
    
    
    [  
      {  
        "id": 28457,  
        "price": "4.00000100",  
        "qty": "12.00000000",  
        "quoteQty": "48.00",  
        "time": 1499865549590,  
        "isBuyerMaker": true,  
        "isRPITrade": true,  
      }  
    ]

---

# 近期成交

## 接口描述[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Recent-Trades-List#接口描述 "接口描述的直接链接")

获取近期订单簿成交

## HTTP请求[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Recent-Trades-List#http请求 "HTTP请求的直接链接")

GET `/fapi/v1/trades`

**注意：** 响应消息不包含RPI订单，其不可见。

## 请求权重[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Recent-Trades-List#请求权重 "请求权重的直接链接")

**5**

## 请求参数[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Recent-Trades-List#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES| 交易对  
limit| INT| NO| 默认:500，最大1000  
  
>   * 仅返回订单簿成交，即不会返回保险基金和自动减仓(ADL)成交
> 


## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Recent-Trades-List#响应示例 "响应示例的直接链接")
    
    
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