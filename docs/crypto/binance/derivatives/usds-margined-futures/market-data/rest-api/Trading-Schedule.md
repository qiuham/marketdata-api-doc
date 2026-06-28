---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Trading-Schedule
api_type: Market Data
updated_at: 2026-01-15T23:47:03.463841
---

# Trading Schedule

## API Description[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Trading-Schedule#api-description "Direct link to API Description")

Trading session schedules for the underlying assets of TradFi Perps are provided for a one-week period starting from the day prior to the query time, covering both the U.S. equity and commodity markets. Equity market session types include "PRE_MARKET", "REGULAR", "AFTER_MARKET", "OVERNIGHT", and "NO_TRADING", while commodity market session types include "REGULAR" and "NO_TRADING".

## HTTP Request[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Trading-Schedule#http-request "Direct link to HTTP Request")

GET `/fapi/v1/tradingSchedule`

## Request Weight[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Trading-Schedule#request-weight "Direct link to Request Weight")

**5**

## Request Parameters[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Trading-Schedule#request-parameters "Direct link to Request Parameters")

NONE

## Response Example[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Trading-Schedule#response-example "Direct link to Response Example")
    
    
    {  
      "updateTime": 1761286643918,  
      "marketSchedules": {  
        "EQUITY": {  
          "sessions": [  
            {  
              "startTime": 1761177600000,  
              "endTime": 1761206400000,  
              "type": "OVERNIGHT"  
            },  
            {  
              "startTime": 1761206400000,  
              "endTime": 1761226200000,  
              "type": "PRE_MARKET"  
            }   
          ]  
        },  
        "COMMODITY": {  
          "sessions": [  
            {  
              "startTime": 1761724800000,  
              "endTime": 1761744600000,  
              "type": "NO_TRADING"  
            },  
            {  
              "startTime": 1761744600000,  
              "endTime": 1761768000000,  
              "type": "REGULAR"  
            }  
          ]  
        }  
      }  
    }

---

# 一周交易时段

## 接口描述[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Trading-Schedule#接口描述 "接口描述的直接链接")

从查询时间的前一日起算、返回为期一周的传统金融合约标的资产的交易时段信息，覆盖美国股票市场和商品市场。美股市场的时段类型包括 "PRE_MARKET"、"REGULAR"、"AFTER_MARKET"、"OVERNIGHT" 和 "NO_TRADING"；商品市场的时段类型包括 "REGULAR" 和 "NO_TRADING"。

## HTTP请求[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Trading-Schedule#http请求 "HTTP请求的直接链接")

GET `/fapi/v1/tradingSchedule`

## 请求权重[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Trading-Schedule#请求权重 "请求权重的直接链接")

**5**

## 请求参数[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Trading-Schedule#请求参数 "请求参数的直接链接")

NONE

## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Trading-Schedule#响应示例 "响应示例的直接链接")
    
    
    {  
      "updateTime": 1761286643918,  
      "marketSchedules": {  
        "EQUITY": {  
          "sessions": [  
            {  
              "startTime": 1761177600000,  
              "endTime": 1761206400000,  
              "type": "OVERNIGHT"  
            },  
            {  
              "startTime": 1761206400000,  
              "endTime": 1761226200000,  
              "type": "PRE_MARKET"  
            }   
          ]  
        },  
        "COMMODITY": {  
          "sessions": [  
            {  
              "startTime": 1761724800000,  
              "endTime": 1761744600000,  
              "type": "NO_TRADING"  
            },  
            {  
              "startTime": 1761744600000,  
              "endTime": 1761768000000,  
              "type": "REGULAR"  
            }  
          ]  
        }  
      }  
    }