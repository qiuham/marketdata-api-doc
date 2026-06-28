---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/portfolio-margin-pro/market-data/Portfolio-Margin-Pro-Tiered-Collateral-Rate
api_type: Market Data
updated_at: 2026-01-15T23:44:25.755114
---

# Portfolio Margin Pro Tiered Collateral Rate(USER_DATA)

## API Description[​](/docs/derivatives/portfolio-margin-pro/market-data/Portfolio-Margin-Pro-Tiered-Collateral-Rate#api-description "Direct link to API Description")

Portfolio Margin PRO Tiered Collateral Rate

## HTTP Request[​](/docs/derivatives/portfolio-margin-pro/market-data/Portfolio-Margin-Pro-Tiered-Collateral-Rate#http-request "Direct link to HTTP Request")

GET `/sapi/v2/portfolio/collateralRate`

## Request Weight(IP)[​](/docs/derivatives/portfolio-margin-pro/market-data/Portfolio-Margin-Pro-Tiered-Collateral-Rate#request-weightip "Direct link to Request Weight\(IP\)")

**50**

## Request Parameters[​](/docs/derivatives/portfolio-margin-pro/market-data/Portfolio-Margin-Pro-Tiered-Collateral-Rate#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/derivatives/portfolio-margin-pro/market-data/Portfolio-Margin-Pro-Tiered-Collateral-Rate#response-example "Direct link to Response Example")
    
    
    [  
        {  
            "asset": "BNB",  
            "collateralInfo": [  
                {  
                "tierFloor": "0.0000",  
                "tierCap": "1000.0000",  
                "collateralRate": "1.0000",  
                "cum":"0.0000"    //account equity quick addition number  
                },  
                {  
                "tierFloor": "1000.0000",  
                "tierCap": "2000.0000",  
                "collateralRate": "0.9000",  
                "cum":"0.0000"  
                }  
            ]  
        },  
        {  
            "asset": "USDT",  
            "collateralInfo": [  
                {  
                    "tierFloor": "0.0000",  
                    "tierCap": "1000.0000",  
                    "collateralRate": "1.0000",  
                    "cum":"0.0000"  
                },  
                {  
                    "tierFloor": "1000.0000",  
                    "tierCap": "2000.0000",  
                    "collateralRate": "0.9999",  
                    "cum":"0.0000"  
                }  
            ]  
        }  
    ]

---

# 统一账户专业版资产阶梯质押率(USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin-pro/market-data/Portfolio-Margin-Pro-Tiered-Collateral-Rate#接口描述 "接口描述的直接链接")

统一账户专业版资产阶梯质押率

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin-pro/market-data/Portfolio-Margin-Pro-Tiered-Collateral-Rate#http请求 "HTTP请求的直接链接")

GET `/sapi/v2/portfolio/collateralRate`

## 请求权重(IP)[​](/docs/zh-CN/derivatives/portfolio-margin-pro/market-data/Portfolio-Margin-Pro-Tiered-Collateral-Rate#请求权重ip "请求权重\(IP\)的直接链接")

**50**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin-pro/market-data/Portfolio-Margin-Pro-Tiered-Collateral-Rate#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin-pro/market-data/Portfolio-Margin-Pro-Tiered-Collateral-Rate#响应示例 "响应示例的直接链接")
    
    
    [  
        {  
            "asset": "BNB",  
            "collateralInfo": [  
                {  
                "tierFloor": "0.0000",  
                "tierCap": "1000.0000",  
                "collateralRate": "1.0000",  
                "cum":"0.0000"   //账户权益计算速算数  
                },  
                {  
                "tierFloor": "1000.0000",  
                "tierCap": "2000.0000",  
                "collateralRate": "0.9000",  
                "cum":"0.0000"  
                }  
            ]  
        },  
        {  
            "asset": "USDT",  
            "collateralInfo": [  
                {  
                    "tierFloor": "0.0000",  
                    "tierCap": "1000.0000",  
                    "collateralRate": "1.0000",  
                    "cum":"0.0000"  
                },  
                {  
                    "tierFloor": "1000.0000",  
                    "tierCap": "2000.0000",  
                    "collateralRate": "0.9999",  
                    "cum":"0.0000"  
                }  
            ]  
        }  
    ]