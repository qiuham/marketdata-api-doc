---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-Margin-Account-OCO
api_type: Trading
updated_at: 2026-01-15T23:45:52.418999
---

# Query Margin Account's OCO (USER_DATA)

## API Description[​](/docs/derivatives/portfolio-margin/trade/Query-Margin-Account-OCO#api-description "Direct link to API Description")

Retrieves a specific OCO based on provided optional parameters

## HTTP Request[​](/docs/derivatives/portfolio-margin/trade/Query-Margin-Account-OCO#http-request "Direct link to HTTP Request")

GET `/papi/v1/margin/orderList`

## Weight[​](/docs/derivatives/portfolio-margin/trade/Query-Margin-Account-OCO#weight "Direct link to Weight")

**5**

## Parameters:[​](/docs/derivatives/portfolio-margin/trade/Query-Margin-Account-OCO#parameters "Direct link to Parameters:")

Name| Type| Mandatory| Description  
---|---|---|---  
orderListId| LONG| NO| Either orderListId or origClientOrderId must be provided  
origClientOrderId| STRING| NO| Either orderListId or origClientOrderId must be provided  
recvWindow| LONG| NO| The value cannot be greater than 60000  
timestamp| LONG| YES|   
  
## Response:[​](/docs/derivatives/portfolio-margin/trade/Query-Margin-Account-OCO#response "Direct link to Response:")
    
    
    {  
      "orderListId": 27,  
      "contingencyType": "OCO",  
      "listStatusType": "EXEC_STARTED",  
      "listOrderStatus": "EXECUTING",  
      "listClientOrderId": "h2USkA5YQpaXHPIrkd96xE",  
      "transactionTime": 1565245656253,  
      "symbol": "LTCBTC",  
      "orders": [  
        {  
          "symbol": "LTCBTC",  
          "orderId": 4,  
          "clientOrderId": "qD1gy3kc3Gx0rihm9Y3xwS"  
        },  
        {  
          "symbol": "LTCBTC",  
          "orderId": 5,  
          "clientOrderId": "ARzZ9I00CPM8i3NhmU9Ega"  
        }  
      ]  
    }

---

# 查询杠杆账户 OCO(USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Margin-Account-OCO#接口描述 "接口描述的直接链接")

根据提供的可选参数检索特定的杠杆账户 OCO 订单。

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Margin-Account-OCO#http请求 "HTTP请求的直接链接")

GET `/papi/v1/margin/orderList`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Margin-Account-OCO#请求权重 "请求权重的直接链接")

**5**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Margin-Account-OCO#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
orderListId| LONG| NO| `orderListId` 或 `listClientOrderId` 必须被提供  
origClientOrderId| STRING| NO| `orderListId` 或 `listClientOrderId` 必须被提供  
recvWindow| LONG| NO| 赋值不能大于 60000  
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Margin-Account-OCO#响应示例 "响应示例的直接链接")
    
    
    {  
      "orderListId": 27,  
      "contingencyType": "OCO",  
      "listStatusType": "EXEC_STARTED",  
      "listOrderStatus": "EXECUTING",  
      "listClientOrderId": "h2USkA5YQpaXHPIrkd96xE",  
      "transactionTime": 1565245656253,  
      "symbol": "LTCBTC",  
      "orders": [  
        {  
          "symbol": "LTCBTC",  
          "orderId": 4,  
          "clientOrderId": "qD1gy3kc3Gx0rihm9Y3xwS"  
        },  
        {  
          "symbol": "LTCBTC",  
          "orderId": 5,  
          "clientOrderId": "ARzZ9I00CPM8i3NhmU9Ega"  
        }  
      ]  
    }