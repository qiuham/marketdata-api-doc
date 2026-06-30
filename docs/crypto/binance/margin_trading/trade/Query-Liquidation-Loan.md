---
exchange: binance
source_url: https://developers.binance.com/docs/margin_trading/trade/Query-Liquidation-Loan
api_type: Trading
updated_at: 2026-06-30 19:07:54.573779
---

# Query Margin Account's all OCO (USER_DATA)

## API Description[​](/docs/margin_trading/trade/Query-Margin-Account-All-OCO#api-description "Direct link to API Description")

Retrieves all OCO for a specific margin account based on provided optional parameters

## HTTP Request[​](/docs/margin_trading/trade/Query-Margin-Account-All-OCO#http-request "Direct link to HTTP Request")

GET `/sapi/v1/margin/allOrderList`

## Request Weight[​](/docs/margin_trading/trade/Query-Margin-Account-All-OCO#request-weight "Direct link to Request Weight")

**200(IP)**

## Request Parameters[​](/docs/margin_trading/trade/Query-Margin-Account-All-OCO#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
isIsolated| STRING| NO| for isolated margin or not, "TRUE", "FALSE"，default "FALSE"  
symbol| STRING| NO| mandatory for isolated margin, not supported for cross margin  
fromId| LONG| NO| If supplied, neither `startTime` or `endTime` can be provided  
startTime| LONG| NO|   
endTime| LONG| NO|   
limit| INT| NO| Default Value: 500; Max Value: 1000  
recvWindow| LONG| NO| The value cannot be greater than `60000`  
timestamp| LONG| YES|   
  
## Response Example[​](/docs/margin_trading/trade/Query-Margin-Account-All-OCO#response-example "Direct link to Response Example")
    
    
    [  
      {  
        "orderListId": 29,  
        "contingencyType": "OCO",  
        "listStatusType": "EXEC_STARTED",  
        "listOrderStatus": "EXECUTING",  
        "listClientOrderId": "amEEAXryFzFwYF1FeRpUoZ",  
        "transactionTime": 1565245913483,  
        "symbol": "LTCBTC",  
        "isIsolated": true,       // if isolated margin  
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

## 接口描述[​](/docs/zh-CN/margin_trading/trade/Query-Margin-Account-All-OCO#接口描述 "接口描述的直接链接")

根据提供的可选参数检索特定杠杆账户所有的 OCO 订单。

## HTTP请求[​](/docs/zh-CN/margin_trading/trade/Query-Margin-Account-All-OCO#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/margin/allOrderList`

## 请求权重[​](/docs/zh-CN/margin_trading/trade/Query-Margin-Account-All-OCO#请求权重 "请求权重的直接链接")

**200(IP)**

## 请求参数[​](/docs/zh-CN/margin_trading/trade/Query-Margin-Account-All-OCO#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
isIsolated| STRING| NO| 是否逐仓杠杆，"TRUE", "FALSE", 默认 "FALSE"  
symbol| STRING| NO| 逐仓杠杆必填，全仓杠杆不支持该参数  
fromId| LONG| NO| 提供该项后, `startTime` 和 `endTime` 都不可提供  
startTime| LONG| NO|   
endTime| LONG| NO|   
limit| INT| NO| 默认值: 500; 最大值: 1000  
recvWindow| LONG| NO| 赋值不能超过 `60000`  
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/margin_trading/trade/Query-Margin-Account-All-OCO#响应示例 "响应示例的直接链接")
    
    
    [  
      {  
        "orderListId": 29,  
        "contingencyType": "OCO",  
        "listStatusType": "EXEC_STARTED",  
        "listOrderStatus": "EXECUTING",  
        "listClientOrderId": "amEEAXryFzFwYF1FeRpUoZ",  
        "transactionTime": 1565245913483,  
        "symbol": "LTCBTC",  
        "isIsolated": true,       // 是否是逐仓symbol交易   
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