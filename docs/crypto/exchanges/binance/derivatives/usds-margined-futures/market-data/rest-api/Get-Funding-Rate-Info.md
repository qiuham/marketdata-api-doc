---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Get-Funding-Rate-Info
api_type: Market Data
updated_at: 2026-01-15T23:46:49.783818
---

# Get Funding Rate Info

## API Description[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Get-Funding-Rate-Info#api-description "Direct link to API Description")

Query funding rate info for symbols that had FundingRateCap/ FundingRateFloor / fundingIntervalHours adjustment

## HTTP Request[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Get-Funding-Rate-Info#http-request "Direct link to HTTP Request")

GET `/fapi/v1/fundingInfo`

## Request Weight[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Get-Funding-Rate-Info#request-weight "Direct link to Request Weight")

**0** share 500/5min/IP rate limit with `GET /fapi/v1/fundingInfo`

## Request Parameters[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Get-Funding-Rate-Info#request-parameters "Direct link to Request Parameters")

## Response Example[​](/docs/derivatives/usds-margined-futures/market-data/rest-api/Get-Funding-Rate-Info#response-example "Direct link to Response Example")
    
    
    [  
        {  
            "symbol": "BLZUSDT",  
            "adjustedFundingRateCap": "0.02500000",  
            "adjustedFundingRateFloor": "-0.02500000",  
            "fundingIntervalHours": 8,  
            "disclaimer": false   // ingore  
        }  
    ]

---

# 查询资金费率信息

## 接口描述[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Get-Funding-Rate-Info#接口描述 "接口描述的直接链接")

查询资金费率信息，接口仅返回FundingRateCap/FundingRateFloor/fundingIntervalHours等被特殊调整过的交易对，没调整过的不返回。

## HTTP请求[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Get-Funding-Rate-Info#http请求 "HTTP请求的直接链接")

GET `/fapi/v1/fundingInfo`

## 请求权重[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Get-Funding-Rate-Info#请求权重 "请求权重的直接链接")

**0** 和`GET /fapi/v1/fundingRate`共享500/5min/IP

## 请求参数[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Get-Funding-Rate-Info#请求参数 "请求参数的�直接链接")

## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/market-data/rest-api/Get-Funding-Rate-Info#响应示例 "响应示例的直接链接")
    
    
    [  
        {  
            "symbol": "BLZUSDT",  
            "adjustedFundingRateCap": "0.02500000",  
            "adjustedFundingRateFloor": "-0.02500000",  
            "fundingIntervalHours": 8,  
            "disclaimer": false  
        }  
    ]