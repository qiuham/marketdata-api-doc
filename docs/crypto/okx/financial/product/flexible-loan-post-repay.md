---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#financial-product-flexible-loan-post-repay
anchor_id: financial-product-flexible-loan-post-repay
api_type: API
updated_at: 2026-08-30 19:11:01.433313
---

# POST / Repay

#### Rate Limit: 2 requests per 2 seconds  
  
#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/finance/flexible-loan/repay`

Repays part or all of an order's outstanding borrow amount. Settlement is asynchronous; a successful response means the request was accepted. Use the Loan info endpoint to confirm the final result.

> Request Example
    
    
    POST /api/v5/finance/flexible-loan/repay
    body
    {
      "ordId": "680234819012345678",
      "ccy": "USDT",
      "amt": "1000",
      "clOrdId": "my-repay-001"
    }
    

#### Request Parameters

**Parameter** | **Type** | **Required** | **Description**  
---|---|---|---  
ordId | String | Yes | Order ID to repay.  
ccy | String | Yes | Repayment currency. It must match the order's borrow currency.  
amt | String | Yes | Repayment amount. Repaying the entire outstanding balance closes the order.  
clOrdId | String | Yes | Client-supplied idempotency key, scoped to the UID and endpoint path. It is retained for 60 seconds; a completed duplicate returns `51016`, and an in-flight duplicate returns `51784`.  
  
> Response Example
    
    
    {
      "code": "0",
      "data": [{"ordId": "680234819012345678", "ccy": "USDT", "amt": "1000", "clOrdId": "my-repay-001"}],
      "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
ordId | String | Order ID.  
ccy | String | Repaid currency.  
amt | String | Requested repayment amount, echoed from the request.  
clOrdId | String | Client-supplied ID echoed from the request.

---

# POST / 还款

#### 限速：2次/2秒  
  
#### 限速规则：User ID

#### HTTP 请求

`POST /api/v5/finance/flexible-loan/repay`

对订单的未偿借款进行部分或全额还款。结算为异步执行；成功响应仅表示请求已受理。请通过借款信息接口确认最终结果。

> 请求示例
    
    
    POST /api/v5/finance/flexible-loan/repay
    body
    {
      "ordId": "680234819012345678",
      "ccy": "USDT",
      "amt": "1000",
      "clOrdId": "my-repay-001"
    }
    

#### 请求参数

**参数名** | **类型** | **是否必须** | **描述**  
---|---|---|---  
ordId | String | 是 | 待还款的订单 ID。  
ccy | String | 是 | 还款币种，必须与订单借入币种一致。  
amt | String | 是 | 还款数量。偿还全部未偿余额将关闭订单。  
clOrdId | String | 是 | UID 与接口路径维度的客户端幂等键。记录保留 60 秒；已完成的重复请求返回 `51016`，执行中的重复请求返回 `51784`。  
  
> 返回示例
    
    
    {
      "code": "0",
      "data": [{"ordId": "680234819012345678", "ccy": "USDT", "amt": "1000", "clOrdId": "my-repay-001"}],
      "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
ordId | String | 订单 ID。  
ccy | String | 已还款币种。  
amt | String | 从请求中回显的还款数量。  
clOrdId | String | 从请求中回显的客户端订单 ID。