---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-Margin-Account-all-OCO
api_type: Trading
updated_at: 2026-01-15T23:45:52.620578
---

# Query Margin Account's all OCO (USER_DATA)

## API Description[​](/docs/derivatives/portfolio-margin/trade/Query-Margin-Account-all-OCO#api-description "Direct link to API Description")

Query all OCO for a specific margin account based on provided optional parameters

## HTTP Request[​](/docs/derivatives/portfolio-margin/trade/Query-Margin-Account-all-OCO#http-request "Direct link to HTTP Request")

GET `/papi/v1/margin/allOrderList`

## Weight[​](/docs/derivatives/portfolio-margin/trade/Query-Margin-Account-all-OCO#weight "Direct link to Weight")

**100**

## Parameters:[​](/docs/derivatives/portfolio-margin/trade/Query-Margin-Account-all-OCO#parameters "Direct link to Parameters:")

Name| Type| Mandatory| Description  
---|---|---|---  
fromId| LONG| NO| If supplied, neither startTime or endTime can be provided  
startTime| LONG| NO|   
endTime| LONG| NO|   
limit| INT| NO| Default 500; max 500.  
recvWindow| LONG| NO| The value cannot be greater than 60000  
timestamp| LONG| YES|   
  
## Response:[​](/docs/derivatives/portfolio-margin/trade/Query-Margin-Account-all-OCO#response "Direct link to Response:")
    
    
    [  
      {  
        "orderListId": 29,  
        "contingencyType": "OCO",  
        "listStatusType": "EXEC_STARTED",  
        "listOrderStatus": "EXECUTING",  
        "listClientOrderId": "amEEAXryFzFwYF1FeRpUoZ",  
        "transactionTime": 1565245913483,  
        "symbol": "LTCBTC",  
        "orders": [  
          {  
            "symbol": "LTCBTC",  
            "orderId": 4,  
            "clientOrderId": "oD7aesZqjEGlZrbtRpy5zB"  
          },  
          {  
            "symbol": "LTCBTC",  
            "orderId": 5,  
            "clientOrderId": "Jr1h6xirOxgeJOUuYQS7V3"  
          }  
        ]  
      },  
      {  
        "orderListId": 28,  
        "contingencyType": "OCO",  
        "listStatusType": "EXEC_STARTED",  
        "listOrderStatus": "EXECUTING",  
        "listClientOrderId": "hG7hFNxJV6cZy3Ze4AUT4d",  
        "transactionTime": 1565245913407,  
        "symbol": "LTCBTC",  
        "orders": [  
          {  
            "symbol": "LTCBTC",  
            "orderId": 2,  
            "clientOrderId": "j6lFOfbmFMRjTYA7rRJ0LP"  
          },  
          {  
            "symbol": "LTCBTC",  
            "orderId": 3,  
            "clientOrderId": "z0KCjOdditiLS5ekAFtK81"  
          }  
        ]  
      }  
    ]

---

# 查询特定杠杆账户所有 OCO (USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Margin-Account-all-OCO#接口描述 "接口描述的直接链接")

根据提供的可选参数检索特定杠杆账户所有的 OCO 订单。

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Margin-Account-all-OCO#http请求 "HTTP请求的直接链接")

GET `/papi/v1/margin/allOrderList`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Margin-Account-all-OCO#请求权重 "请求权重的直接链接")

**100**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Margin-Account-all-OCO#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
fromId| LONG| NO| 提供该项后, `startTime` 和 `endTime` 都不可提供  
startTime| LONG| NO|   
endTime| LONG| NO|   
limit| INT| NO| 默认 500;最大500.  
recvWindow| LONG| NO| 赋值不能大于 60000  
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Margin-Account-all-OCO#响应示例 "响应示例的直接链接")
    
    
    [  
      {  
        "orderListId": 29,  
        "contingencyType": "OCO",  
        "listStatusType": "EXEC_STARTED",  
        "listOrderStatus": "EXECUTING",  
        "listClientOrderId": "amEEAXryFzFwYF1FeRpUoZ",  
        "transactionTime": 1565245913483,  
        "symbol": "LTCBTC",  
        "orders": [  
          {  
            "symbol": "LTCBTC",  
            "orderId": 4,  
            "clientOrderId": "oD7aesZqjEGlZrbtRpy5zB"  
          },  
          {  
            "symbol": "LTCBTC",  
            "orderId": 5,  
            "clientOrderId": "Jr1h6xirOxgeJOUuYQS7V3"  
          }  
        ]  
      },  
      {  
        "orderListId": 28,  
        "contingencyType": "OCO",  
        "listStatusType": "EXEC_STARTED",  
        "listOrderStatus": "EXECUTING",  
        "listClientOrderId": "hG7hFNxJV6cZy3Ze4AUT4d",  
        "transactionTime": 1565245913407,  
        "symbol": "LTCBTC",  
        "orders": [  
          {  
            "symbol": "LTCBTC",  
            "orderId": 2,  
            "clientOrderId": "j6lFOfbmFMRjTYA7rRJ0LP"  
          },  
          {  
            "symbol": "LTCBTC",  
            "orderId": 3,  
            "clientOrderId": "z0KCjOdditiLS5ekAFtK81"  
          }  
        ]  
      }  
    ]