---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/rest-api/Recent-Trades-List
api_type: Market Data
updated_at: 2026-01-15T23:38:50.559647
---

# Recent Trades List

## API Description[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Recent-Trades-List#api-description "Direct link to API Description")

Get recent market trades

## HTTP Request[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Recent-Trades-List#http-request "Direct link to HTTP Request")

GET `/dapi/v1/trades`

## Request Weight[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Recent-Trades-List#request-weight "Direct link to Request Weight")

5

## Request Parameters[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Recent-Trades-List#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
limit| INT| NO| Default 500; max 1000.  
  
  * Market trades means trades filled in the order book. Only market trades will be returned, which means the insurance fund trades and ADL trades won't be returned.



## Response Example[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Recent-Trades-List#response-example "Direct link to Response Example")
    
    
    [  
      {  
        "id": 28457,  
        "price": "9635.0",  
        "qty": "1",  
        "baseQty": "0.01037883",  
        "time": 1591250192508,  
        "isBuyerMaker": true,  
      }  
    ]

---

# 近期成交(归集)

## 接口描述[​](/docs/zh-CN/derivatives/coin-margined-futures/market-data/rest-api/Recent-Trades-List#接口描述 "接口描述的直接链接")

获取近期订单簿成交

## HTTP请求[​](/docs/zh-CN/derivatives/coin-margined-futures/market-data/rest-api/Recent-Trades-List#http请求 "HTTP请求的直接链接")

`GET /dapi/v1/trades`

## 请求权重[​](/docs/zh-CN/derivatives/coin-margined-futures/market-data/rest-api/Recent-Trades-List#请求权重 "请求权重的直接链接")

**5**

## 请求参数[​](/docs/zh-CN/derivatives/coin-margined-futures/market-data/rest-api/Recent-Trades-List#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES| 交易对  
limit| INT| NO| 默认 500; 最大 1000.  
  
>   * 仅返回订单簿成交，即不会返回保险基金和自动减仓(ADL)成交
> 


## 响应示例[​](/docs/zh-CN/derivatives/coin-margined-futures/market-data/rest-api/Recent-Trades-List#响应示例 "响应示例的直接链接")
    
    
    [  
      {  
        id: 28457, // 成交ID  
        price: "9635.0", // 成交价格  
        qty: "1", // 成交量(张数)  
        baseQty: "0.01037883", // 成交额(标的数量)  
        time: 1591250192508, // 时间  
        isBuyerMaker: true, // 买方是否为挂单方  
      },  
    ]