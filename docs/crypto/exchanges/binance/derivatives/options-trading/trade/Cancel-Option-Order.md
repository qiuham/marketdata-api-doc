---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/options-trading/trade/Cancel-Option-Order
api_type: Trading
updated_at: 2026-01-15T23:42:29.680838
---

# Cancel Option Order (TRADE)

## API Description[​](/docs/derivatives/options-trading/trade/Cancel-Option-Order#api-description "Direct link to API Description")

Cancel an active order.

## HTTP Request[​](/docs/derivatives/options-trading/trade/Cancel-Option-Order#http-request "Direct link to HTTP Request")

DELETE `/eapi/v1/order`

**Weight:** **1**

## Request Parameters[​](/docs/derivatives/options-trading/trade/Cancel-Option-Order#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES| Option trading pair, e.g BTC-200730-9000-C  
orderId| LONG| NO| Order ID, e.g 4611875134427365377  
clientOrderId| STRING| NO| User-defined order ID, e.g 10000  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * At least one instance of `orderId` and `clientOrderId` must be sent.
> 


## Response Example[​](/docs/derivatives/options-trading/trade/Cancel-Option-Order#response-example "Direct link to Response Example")
    
    
    {  
      "orderId": 4611875134427365377,     // System order number  
      "symbol": "BTC-200730-9000-C",      // Option trading pair  
      "price": "100",                     // Order Price  
      "quantity": "1",                    // Order Quantity  
      "executedQty": "0",                 // Number of executed quantity  
      "side": "BUY",                      // Buy/sell direction  
      "type": "LIMIT",                    // Order type  
      "timeInForce": "GTC",               // Time in force method  
      "reduceOnly": false,                // Order is reduce only Y/N  
      "createDate": 1592465880683,        // Order Time  
      "updateTime": 1566818724722,        // Update time   
      "status": "ACCEPTED",               // Order status  
      "avgPrice": "0",                    // Average price of completed trade  
      "source": "API",  
      "clientOrderId": "",                // Client order ID  
      "priceScale": 4,  
      "quantityScale": 4,  
      "optionSide": "CALL",  
      "quoteAsset": "USDT",  
      "mmp": false  
    }

---

# 撤销订单(TRADE)

## 接口描述[​](/docs/zh-CN/derivatives/options-trading/trade/Cancel-Option-Order#接口描述 "接口描述的直接链接")

撤销订单。

## HTTP请求[​](/docs/zh-CN/derivatives/options-trading/trade/Cancel-Option-Order#http请求 "HTTP请求的直接链接")

DELETE `/eapi/v1/order`

## 请求权重[​](/docs/zh-CN/derivatives/options-trading/trade/Cancel-Option-Order#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/options-trading/trade/Cancel-Option-Order#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES| 交易对  
orderId| LONG| NO| 系统订单号  
clientOrderId| STRING| NO| 用户自定义的订单号  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * `orderId` 与 `origClientOrderId` 必须至少发送一个
> 


## 响应示例[​](/docs/zh-CN/derivatives/options-trading/trade/Cancel-Option-Order#响应示例 "响应示例的直接链接")
    
    
    {  
      "orderId": 4611875134427365377,     // System order number  
      "symbol": "BTC-200730-9000-C",      // Option trading pair  
      "price": "100",                     // Order Price  
      "quantity": "1",                    // Order Quantity  
      "executedQty": "0",                 // Number of executed quantity  
      "side": "BUY",                      // Buy/sell direction  
      "type": "LIMIT",                    // Order type  
      "timeInForce": "GTC",               // Time in force method  
      "reduceOnly": false,                // Order is reduce only Y/N  
      "createDate": 1592465880683,        // Order Time  
      "updateTime": 1566818724722,        // Update time   
      "status": "ACCEPTED",               // Order status  
      "avgPrice": "0",                    // Average price of completed trade  
      "source": "API",  
      "clientOrderId": "",                // Client order ID  
      "priceScale": 4,  
      "quantityScale": 4,  
      "optionSide": "CALL",  
      "quoteAsset": "USDT",  
      "mmp": false  
    }