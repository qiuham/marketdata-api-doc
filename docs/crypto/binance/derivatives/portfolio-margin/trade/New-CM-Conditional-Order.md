---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/portfolio-margin/trade/New-CM-Conditional-Order
api_type: Trading
updated_at: 2026-01-15T23:45:33.656104
---

# New CM Conditional Order(TRADE)

## API Description[​](/docs/derivatives/portfolio-margin/trade/New-CM-Conditional-Order#api-description "Direct link to API Description")

New CM Conditional Order

## HTTP Request[​](/docs/derivatives/portfolio-margin/trade/New-CM-Conditional-Order#http-request "Direct link to HTTP Request")

POST `/papi/v1/cm/conditional/order`

## Request Weight[​](/docs/derivatives/portfolio-margin/trade/New-CM-Conditional-Order#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/portfolio-margin/trade/New-CM-Conditional-Order#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
side| ENUM| YES|   
positionSide| ENUM| NO| Default `BOTH` for One-way Mode ; `LONG` or `SHORT` for Hedge Mode. It must be sent in Hedge Mode.  
strategyType| ENUM| YES| "STOP", "STOP_MARKET", "TAKE_PROFIT", "TAKE_PROFIT_MARKET", and "TRAILING_STOP_MARKET"  
timeInForce| ENUM| NO|   
quantity| DECIMAL| NO|   
reduceOnly| STRING| NO| "true" or "false". default "false". Cannot be sent in Hedge Mode  
price| DECIMAL| NO|   
workingType| ENUM| NO| stopPrice triggered by: "MARK_PRICE", "CONTRACT_PRICE". Default "CONTRACT_PRICE"  
priceProtect| STRING| NO| "TRUE" or "FALSE", default "FALSE". Used with `STOP`/`STOP_MARKET` or `TAKE_PROFIT`/`TAKE_PROFIT_MARKET` orders  
newClientStrategyId| STRING| NO| A unique id among open orders. Automatically generated if not sent. Can only be string following the rule: `^[\.A-Z\:/a-z0-9_-]{1,36}$`  
stopPrice| DECIMAL| NO| Used with `STOP/STOP_MARKET` or `TAKE_PROFIT/TAKE_PROFIT_MARKET` orders.  
activationPrice| DECIMAL| NO| Used with `TRAILING_STOP_MARKET` orders, default as the mark price  
callbackRate| DECIMAL| NO| Used with `TRAILING_STOP_MARKET` orders, min 0.1, max 5 where 1 for 1%  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
Additional mandatory parameters based on type:

Type| Additional mandatory parameters  
---|---  
`STOP/TAKE_PROFIT`| `quantity`, `price`, `stopPrice`  
`STOP_MARKET/TAKE_PROFIT_MARKET`| `stopPrice`  
`TRAILING_STOP_MARKET`| `callbackRate`  
  
  * Order with type `STOP/TAKE_PROFIT`, parameter `timeInForce` can be sent ( default `GTC`).

  * Condition orders will be triggered when:

    * `STOP`, `STOP_MARKET`: 
      * BUY: "MARK_PRICE" >= `stopPrice`
      * SELL: "MARK_PRICE" <= `stopPrice`
    * `TAKE_PROFIT`, `TAKE_PROFIT_MARKET`: 
      * BUY: "MARK_PRICE" <= `stopPrice`
      * SELL: "MARK_PRICE" >= `stopPrice`
    * `TRAILING_STOP_MARKET`: 
      * BUY: the lowest mark price after order placed `<= `activationPrice`, and the latest mark price >`= the lowest mark price * (1 + `callbackRate`)
      * SELL: the highest mark price after order placed >= `activationPrice`, and the latest mark price <= the highest mark price * (1 - `callbackRate`)
  * For `TRAILING_STOP_MARKET`, if you got such error code. `{"code": -2021, "msg": "Order would immediately trigger."}` means that the parameters you send do not meet the following requirements:

    * BUY: `activationPrice` should be smaller than latest mark price.
    * SELL: `activationPrice` should be larger than latest mark price.
  * Condition orders will be triggered when:

    * If parameter`priceProtect`is sent as true: 
      * when price reaches the `stopPrice` ，the difference rate between "MARK_PRICE" and "CONTRACT_PRICE" cannot be larger than the "triggerProtect" of the symbol
      * "triggerProtect" of a symbol can be got from `GET /fapi/v1/exchangeInfo`
    * `STOP`, `STOP_MARKET`: 
      * BUY: latest price ("MARK_PRICE" or "CONTRACT_PRICE") >= `stopPrice`
      * SELL: latest price ("MARK_PRICE" or "CONTRACT_PRICE") <= `stopPrice`
    * `TAKE_PROFIT`, `TAKE_PROFIT_MARKET`: 
      * BUY: latest price ("MARK_PRICE" or "CONTRACT_PRICE") <= `stopPrice`
      * SELL: latest price ("MARK_PRICE" or "CONTRACT_PRICE") >= `stopPrice`



## Response Example[​](/docs/derivatives/portfolio-margin/trade/New-CM-Conditional-Order#response-example "Direct link to Response Example")
    
    
    {  
        "newClientStrategyId": "testOrder",  
        "strategyId":123445,  
        "strategyStatus":"NEW",  
        "strategyType": "TRAILING_STOP_MARKET",   
        "origQty": "10",  
        "price": "0",  
        "reduceOnly": false,  
        "side": "BUY",  
        "positionSide": "SHORT",  
        "stopPrice": "9300",        // please ignore when order type is TRAILING_STOP_MARKET  
        "symbol": "BTCUSD_200925",  
        "pair": "BTCUSD",  
        "timeInForce": "GTC",  
        "activatePrice": "9020",    // activation price, only return with TRAILING_STOP_MARKET order  
        "priceRate": "0.3",         // callback rate, only return with TRAILING_STOP_MARKET order  
        "bookTime": 1566818724710,  // order place time  
        "updateTime": 1566818724722  
        "workingType":"CONTRACT_PRICE",  
        "priceProtect": false     
    }

---

# CM条件单下单(TRADE)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/trade/New-CM-Conditional-Order#接口描述 "接口描述的直接链接")

CM条件单下单

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/trade/New-CM-Conditional-Order#http请求 "HTTP请求的直接链接")

POST `/papi/v1/cm/conditional/order`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/trade/New-CM-Conditional-Order#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/trade/New-CM-Conditional-Order#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES| 交易对  
side| ENUM| YES| 方向  
positionSide| ENUM| NO| 持仓方向，单向持仓模式下非必填，默认且仅可填`BOTH`;在双向持仓模式下必填,且仅可选择 `LONG` 或 `SHORT`  
strategyType| ENUM| YES| 条件单类型"STOP", "STOP_MARKET", "TAKE_PROFIT", "TAKE_PROFIT_MARKET"或"TRAILING_STOP_MARKET"  
timeInForce| ENUM| NO|   
quantity| DECIMAL| NO|   
reduceOnly| STRING| NO| `true`或`false`; 非双开模式下默认false；双开模式下不接受此参数  
price| DECIMAL| NO|   
workingType| ENUM| NO| stopPrice 触发类型: `MARK_PRICE`, `CONTRACT_PRICE`. 默认 `CONTRACT_PRICE`  
priceProtect| STRING| NO| 条件单触发保护："TRUE" or "FALSE", 默认 "FALSE". `STOP`/`STOP_MARKET` or `TAKE_PROFIT`/`TAKE_PROFIT_MARKET` 需要此参数  
newClientStrategyId| STRING| NO| 用户自定义的订单号，不可以重复出现在挂单中。如空缺系统会自动赋值。必须满足正则规则: `^[\.A-Z\:/a-z0-9_-]{1,32}$`  
stopPrice| DECIMAL| NO| Used with `STOP/STOP_MARKET` or `TAKE_PROFIT/TAKE_PROFIT_MARKET` orders.  
activationPrice| DECIMAL| NO| `TRAILING_STOP_MARKET` 单使用，默认标记价格  
callbackRate| DECIMAL| NO| `TRAILING_STOP_MARKET` 单使用, 最小0.1, 最大5，1代表1%  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
根据 order `type` 的不同，某些参数强制要求，具体如下:

类型| 强制要求的参数  
---|---  
`STOP/TAKE_PROFIT`| `quantity`, `price`, `stopPrice`  
`STOP_MARKET/TAKE_PROFIT_MARKET`| `stopPrice`  
`TRAILING_STOP_MARKET`| `callbackRate`  
  
  * 条件单为`STOP/TAKE_PROFIT`时, 参数`timeInForce`可以使用(默认`GTC`)

  * 条件单的触发必须:

    * `STOP`, `STOP_MARKET` 止损单: 
      * 买入: 最新合约价格/标记价格高于等于触发价`stopPrice`
      * 卖出: 最新合约价格/标记价格低于等于触发价`stopPrice`
    * `TAKE_PROFIT`, `TAKE_PROFIT_MARKET` 止盈单: 
      * 买入: 最新合约价格/标记价格低于等于触发价`stopPrice`
      * 卖出: 最新合约价格/标记价格高于等于触发价`stopPrice`
    * `TRAILING_STOP_MARKET` 跟踪止损单: 
      * 买入: 当合约价格/标记价格区间最低价格低于激活价格`activationPrice`,且最新合约价格/标记价高于等于最低价设定回调幅度。
      * 卖出: 当合约价格/标记价格区间最高价格高于激活价格`activationPrice`,且最新合约价格/标记价低于等于最高价设定回调幅度。
  * `TRAILING_STOP_MARKET` 跟踪止损单如果遇到报错 `{"code": -2021, "msg": "Order would immediately trigger."}`  
表示订单不满足以下条件:

    * 买入: 指定的`activationPrice` 必须小于 latest mark price
    * 卖出: 指定的`activationPrice` 必须大于 latest mark price
  * 条件单的触发必须:

    * 如果订单参数`priceProtect`为true:

      * 达到触发价时，`MARK_PRICE`(标记价格)与`CONTRACT_PRICE`(合约最新价)之间的价差不能超过改symbol触发保护阈值
      * 触发保护阈值请参考接口`GET /fapi/v1/exchangeInfo` 返回内容相应symbol中"triggerProtect"字段
    * `STOP`, `STOP_MARKET` 止损单:

      * 买入: 最新合约价格/标记价格高于等于触发价`stopPrice`
      * 卖出: 最新合约价格/标记价格低于等于触发价`stopPrice`
    * `TAKE_PROFIT`, `TAKE_PROFIT_MARKET` 止盈单:

      * 买入: 最新合约价格/标记价格低于等于触发价`stopPrice`
      * 卖出: 最新合约价格/标记价格高于等于触发价`stopPrice`



## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/trade/New-CM-Conditional-Order#响应示例 "响应示例的直接链接")
    
    
    {  
        "newClientStrategyId": "testOrder",  
        "strategyId":123445,  
        "strategyStatus":"NEW",  
        "strategyType": "TRAILING_STOP_MARKET",   
        "origQty": "10",  
        "price": "0",  
        "reduceOnly": false,  
        "side": "BUY",  
        "positionSide": "SHORT",  
        "stopPrice": "9300",          
        "symbol": "BTCUSD_200925",  
        "pair": "BTCUSD",  
        "timeInForce": "GTC",  
        "activatePrice": "9020",     
        "priceRate": "0.3",           
        "bookTime": 1566818724710, //条件单下单时间    
        "updateTime": 1566818724722,  
        "workingType":"CONTRACT_PRICE",  
        "priceProtect": false     
    }