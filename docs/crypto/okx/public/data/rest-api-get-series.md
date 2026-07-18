---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#public-data-rest-api-get-series
anchor_id: public-data-rest-api-get-series
api_type: REST
updated_at: 2026-07-18 20:04:33.942915
---

# Get series

Retrieve the list of series for OKX prediction markets.

#### Rate Limit: 10 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/public/event-contract/series`

> Request Example
    
    
    GET /api/v5/public/event-contract/series?seriesId=BTC-ABOVE-DAILY
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
seriesId | String | No | Series ID, e.g. `BTC-ABOVE-DAILY`. If not passed, all series will be returned.  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "seriesId": "BTC-ABOVE-DAILY",
                "freq": "daily",
                "title": "BTC price above 15k",
                "category": "Crypto",
                "settlement": {
                    "method": "price_above",
                    "closeEarly": false,
                    "srcName": "okx_index",
                    "underlying": "BTC-USDT"
                }
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
seriesId | String | Series ID, e.g. `BTC-ABOVE-DAILY`  
freq | String | Frequency of the series  
`five_min`  
`fifteen_min`  
`hourly`  
`daily`  
`monthly`  
title | String | Series title  
category | String | Category which this series belongs to, e.g. `Crypto`  
settlement | Object | Settlement information  
> method | String | Settlement method.  
`price_up_down`: Price up/down  
`price_above`: Price above  
`hit`: Hit (price touches strike level, settles immediately)  
`between`: Between (settle price within [floorStrike, capStrike) range)  
> closeEarly | Boolean | Whether the market can be settled earlier than the expiration time.  
`true`  
`false`  
> srcName | String | Settlement source name, e.g. `okx_index`, `cf_benchmark_index`  
> underlying | String | Price underlying in OKX trading symbol format, e.g. `BTC-USDT`. Only applicable to price-related settlement methods.

---

# 获取系列

获取 OKX 预测市场的系列列表。

#### 限速：10次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/public/event-contract/series`

> 请求示例
    
    
    GET /api/v5/public/event-contract/series?seriesId=BTC-ABOVE-DAILY
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
seriesId | String | 否 | 系列 ID，如 `BTC-ABOVE-DAILY`。不传则返回所有系列。  
  
> 返回示例
    
    
    {
        "code": "0",
        "data": [
            {
                "seriesId": "BTC-ABOVE-DAILY",
                "freq": "daily",
                "title": "BTC price above 15k",
                "category": "Crypto",
                "settlement": {
                    "method": "price_above",
                    "closeEarly": false,
                    "srcName": "okx_index",
                    "underlying": "BTC-USDT"
                }
            }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
seriesId | String | 系列 ID，如 `BTC-ABOVE-DAILY`  
freq | String | 系列频率  
`five_min`  
`fifteen_min`  
`hourly`  
`daily`  
`monthly`  
title | String | 系列标题  
category | String | 所属分类，如 `Crypto`  
settlement | Object | 结算信息  
> method | String | 结算方式。  
`price_up_down`：价格涨跌  
`price_above`：价格高于  
`hit`：触及（价格触达行权价格，立即结算）  
`between`：区间（结算价格在 [floorStrike, capStrike) 范围内）  
> closeEarly | Boolean | 是否可以在到期时间前提前结算。  
`true`  
`false`  
> srcName | String | 结算数据来源名称，如 `okx_index`、`cf_benchmark_index`  
> underlying | String | OKX 交易对格式的标的价格，如 `BTC-USDT`。仅适用于价格相关结算方式。