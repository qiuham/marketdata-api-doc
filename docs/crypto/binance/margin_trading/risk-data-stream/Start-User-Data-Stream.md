---
exchange: binance
source_url: https://developers.binance.com/docs/margin_trading/risk-data-stream/Start-User-Data-Stream
api_type: REST
updated_at: 2026-05-27 18:57:08.810424
---

# Get Force Liquidation Record (USER_DATA)

## API Description[​](/docs/margin_trading/trade#api-description "Direct link to API Description")

Get Force Liquidation Record

## HTTP Request[​](/docs/margin_trading/trade#http-request "Direct link to HTTP Request")

GET `/sapi/v1/margin/forceLiquidationRec`

## Request Weight[​](/docs/margin_trading/trade#request-weight "Direct link to Request Weight")

**1(IP)**

## Request Parameters[​](/docs/margin_trading/trade#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
startTime| LONG| NO|   
endTime| LONG| NO|   
isolatedSymbol| STRING| NO|   
current| LONG| NO| Currently querying page. Start from 1. Default:1  
size| LONG| NO| Default:10 Max:100  
recvWindow| LONG| NO| The value cannot be greater than `60000`  
timestamp| LONG| YES|   
  
  * Response in descending order



## Response Example[​](/docs/margin_trading/trade#response-example "Direct link to Response Example")
    
    
      {  
          "rows": [  
              {  
                  "avgPrice": "0.00388359",  
                  "executedQty": "31.39000000",  
                  "orderId": 180015097,  
                  "price": "0.00388110",  
                  "qty": "31.39000000",  
                  "side": "SELL",  
                  "symbol": "BNBBTC",  
                  "timeInForce": "GTC",  
                  "isIsolated": true,  
                  "updatedTime": 1558941374745  
              }  
          ],  
          "total": 1  
      }

---

# 获取账户强制平仓记录(USER_DATA)

## 接口描述[​](/docs/zh-CN/margin_trading/trade#接口描述 "接口描述的直接链接")

获取账户强制平仓记录

## HTTP请求[​](/docs/zh-CN/margin_trading/trade#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/margin/forceLiquidationRec`

## 请求权重[​](/docs/zh-CN/margin_trading/trade#请求权重 "请求权重的直接链接")

**1(IP)**

## 请求参数[​](/docs/zh-CN/margin_trading/trade#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
startTime| LONG| NO|   
endTime| LONG| NO|   
isolatedSymbol| STRING| NO|   
current| LONG| NO| 当前查询页。 开始值 1. 默认:1  
size| LONG| NO| 默认:10 最大:100  
recvWindow| LONG| NO| 赋值不能大于 `60000`  
timestamp| LONG| YES|   
  
  * 响应返回为降序排列。



## 响应示例[​](/docs/zh-CN/margin_trading/trade#响应示例 "响应示例的直接链接")
    
    
      {  
          "rows": [  
              {  
                  "avgPrice": "0.00388359",  
                  "executedQty": "31.39000000",  
                  "orderId": 180015097,  
                  "price": "0.00388110",  
                  "qty": "31.39000000",  
                  "side": "SELL",  
                  "symbol": "BNBBTC",  
                  "timeInForce": "GTC",  
                  "isIsolated": true,  
                  "updatedTime": 1558941374745  
              }  
          ],  
          "total": 1  
      }