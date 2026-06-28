---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/coin-margined-futures/market-data/rest-api/Get-Funding-Info
api_type: Market Data
updated_at: 2026-01-15T23:38:10.398855
---

# Get Funding Rate Info

## API Description[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Get-Funding-Info#api-description "Direct link to API Description")

Query funding rate info for symbols that had FundingRateCap/ FundingRateFloor / fundingIntervalHours adjustment

## HTTP Request[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Get-Funding-Info#http-request "Direct link to HTTP Request")

GET `/dapi/v1/fundingInfo`

## Response Example[​](/docs/derivatives/coin-margined-futures/market-data/rest-api/Get-Funding-Info#response-example "Direct link to Response Example")
    
    
    [  
        {  
            "symbol": "BTCUSD_PERP",  
            "adjustedFundingRateCap": "0.02500000",  
            "adjustedFundingRateFloor": "-0.02500000",  
            "fundingIntervalHours": 8,  
            "disclaimer": false   // ignore  
        }  
    ]

---

# 查询资金费率信息

## 接口描述[​](/docs/zh-CN/derivatives/coin-margined-futures/market-data/rest-api/Get-Funding-Info#接口描述 "接口描述的直接链接")

查询资金费率信息，接口仅返回FundingRateCap/FundingRateFloor/fundingIntervalHours被特殊调整过的交易对

## HTTP请求[​](/docs/zh-CN/derivatives/coin-margined-futures/market-data/rest-api/Get-Funding-Info#http请求 "HTTP请求的直接链接")

GET `/dapi/v1/fundingInfo`

## 响应示例[​](/docs/zh-CN/derivatives/coin-margined-futures/market-data/rest-api/Get-Funding-Info#响应示例 "响应示例的直接链接")
    
    
    [  
        {  
            "symbol": "BTCUSD_PERP",  
            "adjustedFundingRateCap": "0.02500000",  
            "adjustedFundingRateFloor": "-0.02500000",  
            "fundingIntervalHours": 8,  
            "disclaimer": false   // ignore  
        }  
    ]