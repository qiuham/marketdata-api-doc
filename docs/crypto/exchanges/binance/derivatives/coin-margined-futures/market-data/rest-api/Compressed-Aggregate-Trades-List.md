---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/rest-api/Compressed-Aggregate-Trades-List
api_type: Market Data
updated_at: 2026-01-15T23:38:04.401966
---

# Compressed/Aggregate Trades List

## API Description[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Compressed-Aggregate-Trades-List#api-description "Direct link to API Description")

Get compressed, aggregate trades. Market trades that fill in 100ms with the same price and the same taking side will have the quantity aggregated.

## HTTP Request[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Compressed-Aggregate-Trades-List#http-request "Direct link to HTTP Request")

GET `/dapi/v1/aggTrades`

## Request Weight[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Compressed-Aggregate-Trades-List#request-weight "Direct link to Request Weight")

**20**

## Request Parameters[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Compressed-Aggregate-Trades-List#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
fromId| LONG| NO| ID to get aggregate trades from INCLUSIVE.  
startTime| LONG| NO| Timestamp in ms to get aggregate trades from INCLUSIVE.  
endTime| LONG| NO| Timestamp in ms to get aggregate trades until INCLUSIVE.  
limit| INT| NO| Default 500; max 1000.  
  
>   * support querying futures trade histories that are not older than one year
>   * If both `startTime` and `endTime` are sent, time between `startTime` and `endTime` must be less than 1 hour.
>   * If `fromId`, `startTime`, and `endTime` are not sent, the most recent aggregate trades will be returned.
>   * Only market trades will be aggregated and returned, which means the insurance fund trades and ADL trades won't be aggregated.
>   * Sending both `startTime`/`endTime` and `fromId` might cause response timeout, please send either `fromId` or `startTime`/`endTime`
> 


## Response Example[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Compressed-Aggregate-Trades-List#response-example "Direct link to Response Example")
    
    
    [  
      {  
        "a": 416690,			// Aggregate tradeId  
        "p": "9642.4",  	 	// Price  
        "q": "3",  			 	// Quantity  
        "f": 595259,         	// First tradeId  
        "l": 595259,         	// Last tradeId  
        "T": 1591250548649, 	// Timestamp  
        "m": false,          	// Was the buyer the maker?  
      }  
    ]

---

# 近期成交(归集)

## 接口描述[​](/docs/zh-CN/derivatives/coin-margined-futures/market-data/rest-api/Compressed-Aggregate-Trades-List#接口描述 "接口描述的直接链接")

归集交易与逐笔交易的区别在于，同一价格、同一方向、同一时间(100ms 计算)的订单簿trade 会被聚合为一条

## HTTP请求[​](/docs/zh-CN/derivatives/coin-margined-futures/market-data/rest-api/Compressed-Aggregate-Trades-List#http请求 "HTTP请求的直接链接")

GET `/dapi/v1/aggTrades`

## 请求权重[​](/docs/zh-CN/derivatives/coin-margined-futures/market-data/rest-api/Compressed-Aggregate-Trades-List#请求权重 "请求权重的直接链接")

**20**

## 请求参数[​](/docs/zh-CN/derivatives/coin-margined-futures/market-data/rest-api/Compressed-Aggregate-Trades-List#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES| 交易对  
fromId| LONG| NO| 从包含 fromID 的成交开始返回结果  
startTime| LONG| NO| 从该时刻之后的成交记录开始返回结果  
endTime| LONG| NO| 返回该时刻为止的成交记录  
limit| INT| NO| 默认 500; 最大 1000.  
  
>   * 接口仅支持查询最近1年的交易数据
>   * 如果同时发送`startTime`和`endTime`，间隔必须小于一小时
>   * 如果没有发送任何筛选参数(`fromId`, `startTime`, `endTime`),默认返回最近的成交记录
>   * 保险基金和自动减仓(ADL)成交不属于订单簿成交，故不会被归并聚合
>   * 同时发送`startTime`/`endTime`和`fromId`可能导致请求超时，建议仅发送`fromId`或仅发送`startTime`和`endTime`
> 


## 响应示例[​](/docs/zh-CN/derivatives/coin-margined-futures/market-data/rest-api/Compressed-Aggregate-Trades-List#响应示例 "响应示例的直接链接")
    
    
    [  
      {  
        a: 416690, // 归集成交ID  
        p: "9642.4", // 成交价  
        q: "3", // 成交量  
        f: 595259, // 被归集的首个成交ID  
        l: 595259, // 被归集的末个成交ID  
        T: 1591250548649, // 成交时间  
        m: true, // 是否为主动卖出单  
      }  
    ]