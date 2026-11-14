---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/finance/pwm/investment-plan/redeem
api_type: REST
updated_at: 2026-11-13 19:23:35.300291
---

# Redeem

### HTTP Request

POST`/v5/earn/pwm/investment-plan/redeem`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
planId| **true**|  string| Investment plan ID  
category| **true**|  string| Product type  
productId| **true**|  string| Product ID. Pass `fundId` for fund products  
shares| Conditional| string| Number of shares to redeem. Required for fund products  
amount| Conditional| string| Redemption amount. Required for non-fund products  
orderLinkId| **true**|  string| User-defined order ID, max 36 characters, used for idempotency  
positionId| Conditional| string| Position ID to redeem. Required for FundPool and On-chain Earn products  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
orderId| string| Redemption order ID  
planId| string| Investment plan ID  
category| string| Product type  
productId| string| Product ID  
shares| string| Number of shares redeemed (returned for fund products)  
amount| string| Redemption amount (returned for non-fund products)  
estimatedAmount| string| Estimated redemption amount based on current share value. Actual amount is subject to settlement  
coin| string| Redemption coin  
status| string| Redemption status: `Success` (non-fund products redeem instantly) / `Pending` (equity funds require approval)  
orderLinkId| string| User-defined order ID  
  
* * *

### Request Example
    
    
    POST /v5/earn/pwm/investment-plan/redeem HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1741651200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "planId": "10001",  
        "category": "equityFund",  
        "productId": "2001",  
        "shares": "3000",  
        "orderLinkId": "xxx"  
    }  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "result": {  
            "orderId": "ORD20241115003",  
            "planId": "10001",  
            "category": "equityFund",  
            "productId": "2001",  
            "shares": "3000",  
            "estimatedAmount": "3087.00",  
            "coin": "USDT",  
            "status": "Pending",  
            "orderLinkId": "xxx"  
        }  
    }

---

# 贖回

### HTTP 請求

POST`/v5/earn/pwm/investment-plan/redeem`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
planId| **true**|  string| 投資計劃ID  
category| **true**|  string| 產品類型  
productId| **true**|  string| 產品ID（基金產品傳 `fundId`）  
shares| 條件必填| string| 贖回份額數量（基金產品時必填）  
amount| 條件必填| string| 贖回金額（非基金產品時必填）  
orderLinkId| **true**|  string| 用戶自定義訂單ID，最長36字符，用於防重  
positionId| 條件必填| string| 贖回的倉位ID（FundPool 及 On-chain Earn 產品必填）  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
orderId| string| 贖回訂單ID  
planId| string| 投資計劃ID  
category| string| 產品類型  
productId| string| 產品ID  
shares| string| 贖回份額數量（基金產品返回）  
amount| string| 贖回金額（非基金產品返回）  
estimatedAmount| string| 預估贖回到賬金額（按當前份額價值計算，實際以結算時為準）  
coin| string| 贖回幣種  
status| string| 贖回狀態：`Success`（非基金產品即時贖回）/ `Pending`（淨值型基金需審批）  
orderLinkId| string| 用戶自定義訂單ID  
  
* * *

### 請求示例
    
    
    POST /v5/earn/pwm/investment-plan/redeem HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1741651200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "planId": "10001",  
        "category": "equityFund",  
        "productId": "2001",  
        "shares": "3000",  
        "orderLinkId": "xxx"  
    }  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "result": {  
            "orderId": "ORD20241115003",  
            "planId": "10001",  
            "category": "equityFund",  
            "productId": "2001",  
            "shares": "3000",  
            "estimatedAmount": "3087.00",  
            "coin": "USDT",  
            "status": "Pending",  
            "orderLinkId": "xxx"  
        }  
    }