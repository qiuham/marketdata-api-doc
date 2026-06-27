---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Account-Trade-List
api_type: Trading
updated_at: 2026-01-15T23:47:06.349066
---

# Account Trade List (USER_DATA)

## API Description[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Account-Trade-List#api-description "Direct link to API Description")

Get trades for a specific account and symbol.

## HTTP Request[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Account-Trade-List#http-request "Direct link to HTTP Request")

GET `/fapi/v1/userTrades`

## Request Weight[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Account-Trade-List#request-weight "Direct link to Request Weight")

**5**

## Request Parameters[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Account-Trade-List#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
orderId| LONG| NO| This can only be used in combination with `symbol`  
startTime| LONG| NO|   
endTime| LONG| NO|   
fromId| LONG| NO| Trade id to fetch from. Default gets most recent trades.  
limit| INT| NO| Default 500; max 1000.  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * If `startTime` and `endTime` are both not sent, then the last 7 days' data will be returned.
>   * The time between `startTime` and `endTime` cannot be longer than 7 days.
>   * The parameter `fromId` cannot be sent with `startTime` or `endTime`.
>   * Only support querying trade in the past 6 months
> 


## Response Example[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Account-Trade-List#response-example "Direct link to Response Example")
    
    
    [  
      {  
      	"buyer": false,  
      	"commission": "-0.07819010",  
      	"commissionAsset": "USDT",  
      	"id": 698759,  
      	"maker": false,  
      	"orderId": 25851813,  
      	"price": "7819.01",  
      	"qty": "0.002",  
      	"quoteQty": "15.63802",  
      	"realizedPnl": "-0.91539999",  
      	"side": "SELL",  
      	"positionSide": "SHORT",  
      	"symbol": "BTCUSDT",  
      	"time": 1569514978020  
      }  
    ]

---

# 账户成交历史 (USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Account-Trade-List#接口描述 "接口描述的直接链接")

获取某交易对的成交历史

## HTTP请求[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Account-Trade-List#http请求 "HTTP请求的直接链接")

GET `/fapi/v1/userTrades`

## 请求权重[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Account-Trade-List#请求权重 "请求权重的直接链接")

**5**

## 请求参数[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Account-Trade-List#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES| 交易对  
orderId| LONG| NO| 必须要和参数`symbol`一起使用  
startTime| LONG| NO| 起始时间  
endTime| LONG| NO| 结束时间  
fromId| LONG| NO| 返回该fromId及之后的成交，缺省返回最近的成交  
limit| INT| NO| 返回的结果集数量 默认值:500 最大值:1000.  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * 如果`startTime` 和 `endTime` 均未发送, 只会返回最近7天的数据。
>   * startTime 和 endTime 的最大间隔为7天
>   * 参数 fromId 不能和startTime 与 endTime一起发送
>   * 本接口仅支持最近6个月历史交易的查询
> 


## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Account-Trade-List#响应示例 "响应示例的直接链接")
    
    
    [  
      {  
      	"buyer": false,	// 是否是买方  
      	"commission": "-0.07819010", // 手续费  
      	"commissionAsset": "USDT", // 手续费计价单位  
      	"id": 698759,	// 交易ID  
      	"maker": false,	// 是否是挂单方  
      	"orderId": 25851813, // 订单编号  
      	"price": "7819.01",	// 成交价  
      	"qty": "0.002",	// 成交量  
      	"quoteQty": "15.63802",	// 成交额  
      	"realizedPnl": "-0.91539999",	// 实现盈亏  
      	"side": "SELL",	// 买卖方向  
      	"positionSide": "SHORT",  // 持仓方向  
      	"symbol": "BTCUSDT", // 交易对  
      	"time": 1569514978020 // 时间  
      }  
    ]