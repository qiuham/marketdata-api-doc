---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/options-trading/market-maker-block-trade/Cancel-Block-Trade-Order
api_type: Market Data
updated_at: 2026-01-15T23:41:52.044055
---

# Cancel Block Trade Order (TRADE)

## API Description[​](/docs/derivatives/options-trading/market-maker-block-trade/Cancel-Block-Trade-Order#api-description "Direct link to API Description")

Cancel a block trade order.

## HTTP Request[​](/docs/derivatives/options-trading/market-maker-block-trade/Cancel-Block-Trade-Order#http-request "Direct link to HTTP Request")

DELETE `eapi/v1/block/order/create`

## Request Weight[​](/docs/derivatives/options-trading/market-maker-block-trade/Cancel-Block-Trade-Order#request-weight "Direct link to Request Weight")

**5**

## Request Parameters[​](/docs/derivatives/options-trading/market-maker-block-trade/Cancel-Block-Trade-Order#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory|  Description  
---|---|---|---  
blockOrderMatchingKey| STRING| YES|   
recvWindow| INT| NO| The value cannot be greater than 60000  
timestamp| INT| YES|   
  
## Response Example[​](/docs/derivatives/options-trading/market-maker-block-trade/Cancel-Block-Trade-Order#response-example "Direct link to Response Example")
    
    
    {}

---

# Cancel Block Trade Order (TRADE)

## API Description[​](/docs/zh-CN/derivatives/options-trading/market-maker-block-trade/Cancel-Block-Trade-Order#api-description "API Description的直接链接")

Cancel a block trade order.

## HTTP Request[​](/docs/zh-CN/derivatives/options-trading/market-maker-block-trade/Cancel-Block-Trade-Order#http-request "HTTP Request的直接链接")

DELETE `eapi/v1/block/order/create`

## Request Weight[​](/docs/zh-CN/derivatives/options-trading/market-maker-block-trade/Cancel-Block-Trade-Order#request-weight "Request Weight的直接链接")

**5**

## Request Parameters[​](/docs/zh-CN/derivatives/options-trading/market-maker-block-trade/Cancel-Block-Trade-Order#request-parameters "Request Parameters的直接链接")

Name| Type| Mandatory|  Description  
---|---|---|---  
blockOrderMatchingKey| STRING| YES|   
recvWindow| INT| NO| The value cannot be greater than 60000  
timestamp| INT| YES|   
  
## Response Example[​](/docs/zh-CN/derivatives/options-trading/market-maker-block-trade/Cancel-Block-Trade-Order#response-example "Response Example的直��接链接")
    
    
    {}