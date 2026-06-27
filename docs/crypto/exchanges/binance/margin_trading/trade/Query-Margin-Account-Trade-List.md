---
exchange: binance
source_url: https://developers.binance.com/docs/margin_trading/trade/Query-Margin-Account-Trade-List
api_type: Trading
updated_at: 2026-05-27 18:57:57.240572
---

# Query Prevented Matches(USER_DATA)

## Description[​](/docs/margin_trading/trade/Query-Margin-Prevented-Matches#description "Direct link to Description")

Displays the list of orders that were expired due to STP. (Self-Trade Prevention).

## HTTP Request[​](/docs/margin_trading/trade/Query-Margin-Prevented-Matches#http-request "Direct link to HTTP Request")

GET `/sapi/v1/margin/myPreventedMatches`

## Request Weight[​](/docs/margin_trading/trade/Query-Margin-Prevented-Matches#request-weight "Direct link to Request Weight")

**10(IP)**

## Request Parameters[​](/docs/margin_trading/trade/Query-Margin-Prevented-Matches#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
preventedMatchId| LONG| NO|   
orderId| LONG| NO|   
fromPreventedMatchId| LONG| NO|   
recvWindow| LONG| NO| The value cannot be greater than 60000. Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.  
timestamp| LONG| YES|   
isIsolated| STRING| NO| For isolated margin or not, "TRUE", "FALSE", default "FALSE"  
  
  * Supported parameter combinations: 
    * `symbol` \+ `preventedMatchId`
    * `symbol` \+ `orderId`
    * `symbol` \+ `orderId` \+ `fromPreventedMatchId`
  * If `orderId` is provided, all prevented matches for that order will be returned.
  * If `preventedMatchId` is provided, the specific prevented match will be returned.
  * A single request returns a maximum of 500 records. If there are more than 500 records, use `symbol` \+ `orderId` \+ `fromPreventedMatchId` combination for pagination.



## Data Source[​](/docs/margin_trading/trade/Query-Margin-Prevented-Matches#data-source "Direct link to Data Source")

Database

## Response Example[​](/docs/margin_trading/trade/Query-Margin-Prevented-Matches#response-example "Direct link to Response Example")
    
    
    [  
        {  
            "symbol": "BTCUSDT",  
            "preventedMatchId": 1,  
            "takerOrderId": 5,  
            "makerSymbol": "BTCUSDT",  
            "makerOrderId": 3,  
            "tradeGroupId": 1,  
            "selfTradePreventionMode": "EXPIRE_MAKER",  
            "price": "1.100000",  
            "makerPreventedQuantity": "1.300000",  
            "transactTime": 1669101687094  
        }  
    ]  
    

## Response Parameters[​](/docs/margin_trading/trade/Query-Margin-Prevented-Matches#response-parameters "Direct link to Response Parameters")

Name| Type| Description  
---|---|---  
symbol| STRING| The trading pair symbol  
preventedMatchId| LONG| Unique identifier for the prevented match event  
takerOrderId| LONG| The order ID of the taker order that triggered STP  
makerSymbol| STRING| The symbol of the maker order  
makerOrderId| LONG| The order ID of the maker order involved in STP  
tradeGroupId| LONG| Identifier grouping related prevented matches  
selfTradePreventionMode| STRING| The STP mode applied. Possible values: `EXPIRE_TAKER`, `EXPIRE_MAKER`, `EXPIRE_BOTH`  
price| STRING| The price at which the match would have occurred  
makerPreventedQuantity| STRING| The quantity that was prevented from being filled on the maker side  
transactTime| LONG| Unix timestamp (milliseconds) when the prevention occurred

---

# 查询杠杆账户被阻止的撮合记录 (USER_DATA)

## 接口描述[​](/docs/zh-CN/margin_trading/trade/Query-Margin-Prevented-Matches#接口描述 "接口描述的直接链接")

获取因STP(自我交易预防)而过期的订单列表

## HTTP请求[​](/docs/zh-CN/margin_trading/trade/Query-Margin-Prevented-Matches#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/margin/myPreventedMatches`

## 请求权重[​](/docs/zh-CN/margin_trading/trade/Query-Margin-Prevented-Matches#请求权重 "请求权重的直接链接")

**10(IP)**

## 请求参数[​](/docs/zh-CN/margin_trading/trade/Query-Margin-Prevented-Matches#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES|   
preventedMatchId| LONG| NO| 预防撮合ID  
orderId| LONG| NO|   
fromPreventedMatchId| LONG| NO| 分页查询的起始预防撮合ID  
recvWindow| LONG| NO| 最大值为 60000 毫秒。支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。  
timestamp| LONG| YES|   
isIsolated| STRING| NO| 是否逐仓杠杆，"TRUE", "FALSE", 默认 "FALSE"  
  
  * 支持的参数组合: 
    * `symbol` \+ `preventedMatchId`
    * `symbol` \+ `orderId`
    * `symbol` \+ `orderId` \+ `fromPreventedMatchId`
  * 如果提供 `orderId`，将返回与该订单相关的所有被阻止撮合记录。
  * 如果提供 `preventedMatchId`，将返回指定的被阻止撮合记录。
  * 单次请求最多返回500条记录。如果记录超过500条，需要使用 `symbol` \+ `orderId` \+ `fromPreventedMatchId` 组合进行分页查询。



## 响应示例[​](/docs/zh-CN/margin_trading/trade/Query-Margin-Prevented-Matches#响应示例 "响应示例的直接链接")
    
    
    [  
        {  
            "symbol": "BTCUSDT",  
            "preventedMatchId": 1,  
            "takerOrderId": 5,  
            "makerSymbol": "BTCUSDT",  
            "makerOrderId": 3,  
            "tradeGroupId": 1,  
            "selfTradePreventionMode": "EXPIRE_MAKER",  
            "price": "1.100000",  
            "makerPreventedQuantity": "1.300000",  
            "transactTime": 1669101687094  
        }  
    ]  
    

## 响应参数[​](/docs/zh-CN/margin_trading/trade/Query-Margin-Prevented-Matches#响应参数 "响应参数的直接链接")

名称| 类型| 描述  
---|---|---  
symbol| STRING| 交易对  
preventedMatchId| LONG| 被阻止匹配的ID  
takerOrderId| LONG| 吃单方订单ID  
makerSymbol| STRING| 挂单方交易对  
makerOrderId| LONG| 挂单方订单ID  
tradeGroupId| LONG| 交易组ID  
selfTradePreventionMode| STRING| 自我交易预防模式，可能的值: `EXPIRE_TAKER`, `EXPIRE_MAKER`, `EXPIRE_BOTH`  
price| STRING| 价格  
makerPreventedQuantity| STRING| 挂单方被阻止的数量  
transactTime| LONG| 交易时间