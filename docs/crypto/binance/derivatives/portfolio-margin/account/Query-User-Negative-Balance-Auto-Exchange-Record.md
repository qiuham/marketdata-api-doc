---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/portfolio-margin/account/Query-User-Negative-Balance-Auto-Exchange-Record
api_type: Account
updated_at: 2026-01-15T23:45:11.033645
---

# Query User Negative Balance Auto Exchange Record (USER_DATA)

## API Description[​](/docs/derivatives/portfolio-margin/account/Query-User-Negative-Balance-Auto-Exchange-Record#api-description "Direct link to API Description")

Query user negative balance auto exchange record

## HTTP Request[​](/docs/derivatives/portfolio-margin/account/Query-User-Negative-Balance-Auto-Exchange-Record#http-request "Direct link to HTTP Request")

GET `/papi/v1/portfolio/negative-balance-exchange-record`

## Request Weight[​](/docs/derivatives/portfolio-margin/account/Query-User-Negative-Balance-Auto-Exchange-Record#request-weight "Direct link to Request Weight")

**100**

## Request Parameters[​](/docs/derivatives/portfolio-margin/account/Query-User-Negative-Balance-Auto-Exchange-Record#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
startTime| LONG| YES|   
endTime| LONG| YES|   
recvWindow| LONG| NO| The value cannot be greater than 60000  
timestamp| LONG| YES|   
  
**Note**

>   * Response in descending order
>   * The max interval between `startTime` and `endTime` is 3 months.
> 


## Response Example[​](/docs/derivatives/portfolio-margin/account/Query-User-Negative-Balance-Auto-Exchange-Record#response-example "Direct link to Response Example")
    
    
    {  
      "total": 2,  
      "rows": [  
        {  
          "startTime": 1736263046841,  
          "endTime": 1736263248179,  
          "details": [  
            {  
              "asset": "ETH",  
              "negativeBalance": 18,  //negative balance amount  
              "negativeMaxThreshold": 5  //the max negative balance threshold  
            }  
          ]  
        },  
        {  
          "startTime": 1736184913252,  
          "endTime": 1736184965474,  
          "details": [  
            {  
              "asset": "BNB",  
              "negativeBalance": 1.10264488,  
              "negativeMaxThreshold": 0  
            }  
          ]  
        }  
      ]  
    }

---

# 查询用户负余额自动兑换记录 (USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/account/Query-User-Negative-Balance-Auto-Exchange-Record#接口描述 "接口描述的直接链接")

查询用户负余额自动兑换记录

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/account/Query-User-Negative-Balance-Auto-Exchange-Record#http请求 "HTTP请求的直接链接")

GET `/papi/v1/portfolio/negative-balance-exchange-record`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/account/Query-User-Negative-Balance-Auto-Exchange-Record#请求权重 "请求权重的直接链接")

**100**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/account/Query-User-Negative-Balance-Auto-Exchange-Record#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
startTime| LONG| YES|   
endTime| LONG| YES|   
recvWindow| LONG| NO| 赋值不能超过 60000  
timestamp| LONG| YES|   
  
>   * 响应返回为降序排列。
>   * 查询时间范围最大不得超过3个月。
> 


## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/account/Query-User-Negative-Balance-Auto-Exchange-Record#响应示例 "响应示例的直接链接")
    
    
    {  
      "total": 2,  
      "rows": [  
        {  
          "startTime": 1736263046841,  
          "endTime": 1736263248179,  
          "details": [  
            {  
              "asset": "ETH",  
              "negativeBalance": 18,  //当前负余额值  
              "negativeMaxThreshold": 5  //该资产触发自动兑换的阈值  
            }  
          ]  
        },  
        {  
          "startTime": 1736184913252,  
          "endTime": 1736184965474,  
          "details": [  
            {  
              "asset": "BNB",  
              "negativeBalance": 1.10264488,  
              "negativeMaxThreshold": 0  
            }  
          ]  
        }  
      ]  
    }