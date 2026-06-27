---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/portfolio-margin/trade/UM-Account-Trade-List
api_type: Trading
updated_at: 2026-01-15T23:46:00.817375
---

# UM Account Trade List(USER_DATA)

## API Description[​](/docs/derivatives/portfolio-margin/trade/UM-Account-Trade-List#api-description "Direct link to API Description")

Get trades for a specific account and UM symbol.

## HTTP Request[​](/docs/derivatives/portfolio-margin/trade/UM-Account-Trade-List#http-request "Direct link to HTTP Request")

GET `/papi/v1/um/userTrades`

## Request Weight[​](/docs/derivatives/portfolio-margin/trade/UM-Account-Trade-List#request-weight "Direct link to Request Weight")

**5**

## Request Parameters[​](/docs/derivatives/portfolio-margin/trade/UM-Account-Trade-List#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
startTime| LONG| NO|   
endTime| LONG| NO|   
fromId| LONG| NO| Trade id to fetch from. Default gets most recent trades.  
limit| INT| NO| Default 500; max 1000.  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * If `startTime` and `endTime` are both not sent, then the last '7 days' data will be returned.
>   * The time between `startTime` and `endTime` cannot be longer than 7 days.
>   * The parameter `fromId` cannot be sent with `startTime` or `endTime`.
> 


## Response Example[​](/docs/derivatives/portfolio-margin/trade/UM-Account-Trade-List#response-example "Direct link to Response Example")
    
    
    [  
        {  
            "symbol": "BTCUSDT",  
            "id": 67880589,  
            "orderId": 270093109,  
            "side": "SELL",  
            "price": "28511.00",  
            "qty": "0.010",  
            "realizedPnl": "2.58500000",  
            "quoteQty": "285.11000",  
            "commission": "-0.11404400",  
            "commissionAsset": "USDT",  
            "time": 1680688557875,  
            "buyer": false,  
            "maker": false,  
            "positionSide": "BOTH"  
        }  
    ]

---

# UM账户成交历史 (USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/trade/UM-Account-Trade-List#接口描述 "接口描述的直接链接")

获取UM某交易对的成交历史

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/trade/UM-Account-Trade-List#http请求 "HTTP请求的直接链接")

GET `/papi/v1/um/userTrades`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/trade/UM-Account-Trade-List#请求权重 "请求权重的直接链接")

**5**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/trade/UM-Account-Trade-List#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES| 交易对  
startTime| LONG| NO|   
endTime| LONG| NO|   
fromId| LONG| NO| 返回该fromId及之后的成交，缺省返回最近的成交  
limit| INT| NO| 返回的结果集数量 默认值:50 最大值:1000  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * 如果`startTime`和`endTime`均不填，默认返回最近7天数据
>   * `startTime`和`endTime`的最大间隔为7天
>   * 参数 `fromId` 不能和`startTime` 与 `endTime`一起发送
> 


## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/trade/UM-Account-Trade-List#响应示例 "响应示例的直接链接")
    
    
    [  
        {  
            "symbol": "BTCUSDT",  
            "id": 67880589,  
            "orderId": 270093109,  
            "side": "SELL",  
            "price": "28511.00",  
            "qty": "0.010",  
            "realizedPnl": "2.58500000",  
            "quoteQty": "285.11000",  
            "commission": "-0.11404400",  
            "commissionAsset": "USDT",  
            "time": 1680688557875,  
            "buyer": false,  
            "maker": false,  
            "positionSide": "BOTH"  
        }  
    ]