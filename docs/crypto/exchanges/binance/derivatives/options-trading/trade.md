---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/options-trading/trade
api_type: Trading
updated_at: 2026-01-15T23:42:29.259270
---

# New Order (TRADE)

## API Description[​](/docs/derivatives/options-trading/trade#api-description "Direct link to API Description")

Send a new order.

## HTTP Request[​](/docs/derivatives/options-trading/trade#http-request "Direct link to HTTP Request")

POST `/eapi/v1/order`

## Request Parameters[​](/docs/derivatives/options-trading/trade#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES| Option trading pair, e.g BTC-200730-9000-C  
side| ENUM| YES| Buy/sell direction: SELL, BUY  
type| ENUM| YES| Order Type: LIMIT(only support limit)  
quantity| DECIMAL| YES| Order Quantity  
price| DECIMAL| NO| Order Price  
timeInForce| ENUM| NO| Time in force method（Default GTC）  
reduceOnly| BOOLEAN| NO| Reduce Only（Default false）  
postOnly| BOOLEAN| NO| Post Only（Default false）  
newOrderRespType| ENUM| NO| "ACK", "RESULT", Default "ACK"  
clientOrderId| STRING| NO| User-defined order ID cannot be repeated in pending orders  
isMmp| BOOLEAN| NO| is market maker protection order, true/false  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
Some parameters are mandatory depending on the order type as follows:

Type| Mandatory parameters  
---|---  
LIMIT| timeInForce, quantity, price  
  
## Response Example[​](/docs/derivatives/options-trading/trade#response-example "Direct link to Response Example")
    
    
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
      "createTime": 1592465880683,        // Order Time  
      "updateTime": 1566818724722,        // Update time  
      "status": "NEW",                    // Order status  
      "avgPrice": "0",                    // Average price of completed trade  
      "source": "API",  
      "clientOrderId": "",                 // Client order ID  
      "priceScale": 2,  
      "quantityScale": 2,  
      "optionSide": "CALL",  
      "quoteAsset": "USDT",  
      "mmp": false  
    }

---

# 下单(TRADE)

## 接口描述[​](/docs/zh-CN/derivatives/options-trading/trade#接口描述 "接口描述的直接链接")

下单

## HTTP请求[​](/docs/zh-CN/derivatives/options-trading/trade#http请求 "HTTP请求的直接链接")

POST `/eapi/v1/order`

## 请求权重[​](/docs/zh-CN/derivatives/options-trading/trade#请求权重 "请求权重的直接链接")

**0**

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES| 交易对  
side| ENUM| YES| 买卖方向 `SELL`, `BUY`  
type| ENUM| YES| 订单类型 `LIMIT`  
quantity| DECIMAL| YES| 下单数量  
price| DECIMAL| NO| 委托价格  
timeInForce| ENUM| NO| 有效时间  
reduceOnly| STRING| NO| 仅减仓`true`, `false`  
postOnly| STRING| NO| 仅做maker`true`, `false`  
newOrderRespType| ENUM| NO| "ACK", "RESULT", 默认 "ACK"  
clientOrderId| STRING| NO| 用户自定义的订单号，不可以重复出现在挂单中。如空缺系统会自动赋值。  
isMmp| BOOLEAN| NO| 是否为MMP订单true/false  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
根据 order `type`的不同，某些参数强制要求，具体如下:

Type| 强制要求的参数  
---|---  
`LIMIT`| `timeInForce`, `quantity`, `price`  
  
## 响应示例[​](/docs/zh-CN/derivatives/options-trading/trade#响应示例 "响应示例的直接链接")
    
    
    {  
      "orderId": 4611875134427365377,     // 订单Id  
      "symbol": "BTC-200730-9000-C",      // 交易对  
      "price": 100,                       // 订单价格  
      "quantity": 1,                      // 订单数量  
      "executedQty": 0,                   // 执行数量  
      "fee": 0,                           // 手续费   
      "side": "BUY",                      // 订单方向  
      "type": "LIMIT",                    // 订单类型  
      "timeInForce": "GTC",               // 有效时间  
      "reduceOnly": false,                // 仅减仓  
      "postOnly": false,                  // 仅做maker  
      "createTime": 1592465880683,        // 订单创建时间  
      "updateTime": 1566818724722,        // 订单更新时间  
      "status": "NEW",                    // 订单状态  
      "avgPrice": "0",                    // 平均价格  
      "source": "API",                    // 订单来源  
      "clientOrderId": ""，               // 用户自定义订单Id  
      "priceScale": 2,                    // 价格精度   
      "quantityScale": 2,                 // 数量精度    
      "optionSide": "CALL",               // 期权类型  
      "quoteAsset": "USDT",               // 报价资产  
      "mmp": false                        // 是否为MMP单  
    }