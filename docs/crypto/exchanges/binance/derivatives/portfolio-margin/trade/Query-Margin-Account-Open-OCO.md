---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-Margin-Account-Open-OCO
api_type: Trading
updated_at: 2026-01-15T23:45:52.488724
---

# Query Margin Account's Open OCO (USER_DATA)

## API Description[​](/docs/derivatives/portfolio-margin/trade/Query-Margin-Account-Open-OCO#api-description "Direct link to API Description")

Query Margin Account's Open OCO

## HTTP Request[​](/docs/derivatives/portfolio-margin/trade/Query-Margin-Account-Open-OCO#http-request "Direct link to HTTP Request")

GET `/papi/v1/margin/openOrderList`

## Weight[​](/docs/derivatives/portfolio-margin/trade/Query-Margin-Account-Open-OCO#weight "Direct link to Weight")

**5**

## Parameters:[​](/docs/derivatives/portfolio-margin/trade/Query-Margin-Account-Open-OCO#parameters "Direct link to Parameters:")

Name| Type| Mandatory| Description  
---|---|---|---  
recvWindow| LONG| NO| The value cannot be greater than 60000  
timestamp| LONG| YES|   
  
## Response:[​](/docs/derivatives/portfolio-margin/trade/Query-Margin-Account-Open-OCO#response "Direct link to Response:")
    
    
    [  
      {  
        "orderListId": 31,  
        "contingencyType": "OCO",  
        "listStatusType": "EXEC_STARTED",  
        "listOrderStatus": "EXECUTING",  
        "listClientOrderId": "wuB13fmulKj3YjdqWEcsnp",  
        "transactionTime": 1565246080644,  
        "symbol": "LTCBTC",  
        "orders": [  
          {  
            "symbol": "LTCBTC",  
            "orderId": 4,  
            "clientOrderId": "r3EH2N76dHfLoSZWIUw1bT"  
          },  
          {  
            "symbol": "LTCBTC",  
            "orderId": 5,  
            "clientOrderId": "Cv1SnyPD3qhqpbjpYEHbd2"  
          }  
        ]  
      }  
    ]

---

# 查询杠杆账户 OCO 挂单 (USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Margin-Account-Open-OCO#接口描述 "接口描述的直接链接")

查询杠杆账户 OCO 挂单

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Margin-Account-Open-OCO#http请求 "HTTP请求的直接链接")

GET `/papi/v1/margin/openOrderList`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Margin-Account-Open-OCO#请求权重 "请求权重的直接链接")

**5**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Margin-Account-Open-OCO#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
recvWindow| LONG| NO| 赋值不能大于 60000  
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Margin-Account-Open-OCO#响应示例 "响应示例的直接链接")
    
    
    [  
      {  
        "orderListId": 31,  
        "contingencyType": "OCO",  
        "listStatusType": "EXEC_STARTED",  
        "listOrderStatus": "EXECUTING",  
        "listClientOrderId": "wuB13fmulKj3YjdqWEcsnp",  
        "transactionTime": 1565246080644,  
        "symbol": "LTCBTC",  
        "orders": [  
          {  
            "symbol": "LTCBTC",  
            "orderId": 4,  
            "clientOrderId": "r3EH2N76dHfLoSZWIUw1bT"  
          },  
          {  
            "symbol": "LTCBTC",  
            "orderId": 5,  
            "clientOrderId": "Cv1SnyPD3qhqpbjpYEHbd2"  
          }  
        ]  
      }  
    ]