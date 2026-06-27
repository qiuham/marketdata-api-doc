---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/portfolio-margin/account/Portfolio-Margin-UM-Trading-Quantitative-Rules-Indicators
api_type: Account
updated_at: 2026-01-15T23:45:06.425420
---

# Portfolio Margin UM Trading Quantitative Rules Indicators(USER_DATA)

## API Description[​](/docs/derivatives/portfolio-margin/account/Portfolio-Margin-UM-Trading-Quantitative-Rules-Indicators#api-description "Direct link to API Description")

Portfolio Margin UM Trading Quantitative Rules Indicators

## HTTP Request[​](/docs/derivatives/portfolio-margin/account/Portfolio-Margin-UM-Trading-Quantitative-Rules-Indicators#http-request "Direct link to HTTP Request")

GET `/papi/v1/um/apiTradingStatus`

## Request Weight[​](/docs/derivatives/portfolio-margin/account/Portfolio-Margin-UM-Trading-Quantitative-Rules-Indicators#request-weight "Direct link to Request Weight")

**1** for a single symbol **10** when the symbol parameter is omitted

## Request Parameters[​](/docs/derivatives/portfolio-margin/account/Portfolio-Margin-UM-Trading-Quantitative-Rules-Indicators#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| NO|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/derivatives/portfolio-margin/account/Portfolio-Margin-UM-Trading-Quantitative-Rules-Indicators#response-example "Direct link to Response Example")
    
    
    {  
        "indicators": { // indicator: quantitative rules indicators, value: user's indicators value, triggerValue: trigger indicator value threshold of quantitative rules.   
            "BTCUSDT": [  
                {  
                    "isLocked": true,  
                    "plannedRecoverTime": 1545741270000,  
                    "indicator": "UFR",  // Unfilled Ratio (UFR)  
                    "value": 0.05,  // Current value  
                    "triggerValue": 0.995  // Trigger value  
                },  
                {  
                    "isLocked": true,  
                    "plannedRecoverTime": 1545741270000,  
                    "indicator": "IFER",  // IOC/FOK Expiration Ratio (IFER)  
                    "value": 0.99,  // Current value  
                    "triggerValue": 0.99  // Trigger value  
                },  
                {  
                    "isLocked": true,  
                    "plannedRecoverTime": 1545741270000,  
                    "indicator": "GCR",  // GTC Cancellation Ratio (GCR)  
                    "value": 0.99,  // Current value  
                    "triggerValue": 0.99  // Trigger value  
                },  
                {  
                    "isLocked": true,  
                    "plannedRecoverTime": 1545741270000,  
                    "indicator": "DR",  // Dust Ratio (DR)  
                    "value": 0.99,  // Current value  
                    "triggerValue": 0.99  // Trigger value  
                }  
            ]  
        },  
        "updateTime": 1545741270000  
    }  
    

Or (account violation triggered)
    
    
    {  
        "indicators":{  
            "ACCOUNT":[  
                {  
                    "indicator":"TMV",  //  Too many violations under multiple symbols trigger account violation  
                    "value":10,  
                    "triggerValue":1,  
                    "plannedRecoverTime":1644919865000,  
                    "isLocked":true  
                }  
            ]  
        },  
        "updateTime":1644913304748  
    }

---

# 统一账户UM合约交易量化规则指标(USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/account/Portfolio-Margin-UM-Trading-Quantitative-Rules-Indicators#接口描述 "接口描述的直接链接")

查询合约交易量化规则指标

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/account/Portfolio-Margin-UM-Trading-Quantitative-Rules-Indicators#http请求 "HTTP请求的直接链接")

GET `/papi/v1/um/apiTradingStatus`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/account/Portfolio-Margin-UM-Trading-Quantitative-Rules-Indicators#请求权重 "请求权重的直接链接")

**1** for a single symbol **10** when the symbol parameter is omitted

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/account/Portfolio-Margin-UM-Trading-Quantitative-Rules-Indicators#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| NO|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/account/Portfolio-Margin-UM-Trading-Quantitative-Rules-Indicators#响应示例 "响应示例的直接链接")
    
    
    {  
        "indicators": { // indicator:风控指标名, value:用户在该市场的风控指标数值, triggerValue:阈值, 对于没有达到记录阈值的则不返回数据。  
            "BTCUSDT": [  
                {  
                    "isLocked": true, //用户该品种交易是否被风控禁用  
                    "plannedRecoverTime": 1545741270000,  
                    "indicator": "UFR",  // Unfilled Ratio (UFR)  
                    "value": 0.05,  // Current value  
                    "triggerValue": 0.995  // Trigger value  
                },  
                {  
                    "isLocked": true,  
                    "plannedRecoverTime": 1545741270000,  
                    "indicator": "IFER",  // IOC/FOK Expiration Ratio (IFER)  
                    "value": 0.99,  // Current value  
                    "triggerValue": 0.99  // Trigger value  
                },  
                {  
                    "isLocked": true,  
                    "plannedRecoverTime": 1545741270000,  
                    "indicator": "GCR",  // GTC Cancellation Ratio (GCR)  
                    "value": 0.99,  // Current value  
                    "triggerValue": 0.99  // Trigger value  
                },  
                {  
                    "isLocked": true,  
                    "plannedRecoverTime": 1545741270000,  
                    "indicator": "DR",  // Dust Ratio (DR)  
                    "value": 0.99,  // Current value  
                    "triggerValue": 0.99  // Trigger value  
                }  
            ]  
        },  
        "updateTime": 1545741270000  
    }  
    

> 或(账户级别违规)
    
    
    {  
        "indicators":{  
            "ACCOUNT":[  
                {  
                    "indicator":"TMV",  //  Too many violations 多交易对触发账号层级违规  
                    "value":10,  
                    "triggerValue":1,  
                    "plannedRecoverTime":1644919865000,  
                    "isLocked":true  
                }  
            ]  
        },  
        "updateTime":1644913304748  
    }