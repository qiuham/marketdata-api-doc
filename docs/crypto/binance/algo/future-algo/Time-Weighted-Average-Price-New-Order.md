---
exchange: binance
source_url: https://developers.binance.com/docs/algo/future-algo/Time-Weighted-Average-Price-New-Order
api_type: REST
updated_at: 2026-07-01 19:10:08.787405
---

# Time-Weighted Average Price(Twap) New Order(TRADE)

## API Description[​](/docs/algo/future-algo/Time-Weighted-Average-Price-New-Order#api-description "Direct link to API Description")

Send in a Twap new order. Only support on USDⓈ-M Contracts.

## HTTP Request[​](/docs/algo/future-algo/Time-Weighted-Average-Price-New-Order#http-request "Direct link to HTTP Request")

POST `/sapi/v1/algo/futures/newOrderTwap`

## Request Weight(UID)[​](/docs/algo/future-algo/Time-Weighted-Average-Price-New-Order#request-weightuid "Direct link to Request Weight\(UID\)")

**3000**

## Request Parameters[​](/docs/algo/future-algo/Time-Weighted-Average-Price-New-Order#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES| Trading symbol eg. BTCUSDT  
side| ENUM| YES| Trading side ( BUY or SELL )  
positionSide| ENUM| NO| Default `BOTH` for One-way Mode ; `LONG` or `SHORT` for Hedge Mode. It must be sent in Hedge Mode.  
quantity| DECIMAL| YES| Quantity of base asset; The notional (`quantity` * `mark price(base asset)`) must be more than the equivalent of 1,000 USDT and less than the equivalent of 1,000,000 USDT  
duration| LONG| YES| Duration for TWAP orders in seconds. [300, 86400]  
clientAlgoId| STRING| NO| A unique id among Algo orders (length should be 32 characters), If it is not sent, we will give default value  
reduceOnly| BOOLEAN| NO| "true" or "false". Default "false"; Cannot be sent in Hedge Mode; Cannot be sent when you open a position  
limitPrice| DECIMAL| NO| Limit price of the order; If it is not sent, will place order by market price by default  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
Other Info:

>   * Total Algo open orders max allowed: `30` orders.
>   * Leverage of symbols and position mode will be the same as your futures account settings. You can set up through the trading page or fapi.
>   * Receiving `"success": true` does not mean that your order will be executed. Please use the query order endpoints (`GET sapi/v1/algo/futures/openOrders` or `GET sapi/v1/algo/futures/historicalOrders`) to check the order status. For example: Your futures balance is insufficient, or open position with reduce only or position side is inconsistent with your own setting. In these cases you will receive `"success": true`, but the order status will be `expired` after we check it.
>   * `quantity` * 60 / `duration` should be larger than minQty
>   * `duration` cannot be less than 5 mins or more than 24 hours.
>   * For delivery contracts, TWAP end time should be one hour earlier than the delivery time of the symbol.
>   * You need to enable the corresponding permission for the API key requesting this endpoint: 
>     * `Futures Trading Permission` — for Classic Trading Account mode
>     * `Portfolio Margin Trading Permission` — for Portfolio Margin Account mode
>   * Base URL: <https://api.binance.com>
> 


## Response Example[​](/docs/algo/future-algo/Time-Weighted-Average-Price-New-Order#response-example "Direct link to Response Example")
    
    
    {  
        "clientAlgoId": "65ce1630101a480b85915d7e11fd5078",  
        "success": true,  
        "code": 0,  
        "msg": "OK"  
    }

---

# 时间加权平均价格策略(Twap)下单(TRADE)

## 接口描述[​](/docs/zh-CN/algo/future-algo/Time-Weighted-Average-Price-New-Order#接口描述 "接口描述的直接链接")

发送Twap下单 仅支持U本位合约

## HTTP请求[​](/docs/zh-CN/algo/future-algo/Time-Weighted-Average-Price-New-Order#http请求 "HTTP请求的直接链接")

POST `/sapi/v1/algo/futures/newOrderTwap`

## 请求权重(UID)[​](/docs/zh-CN/algo/future-algo/Time-Weighted-Average-Price-New-Order#请求权重uid "请求权重\(UID\)的直接链接")

**3000**

## 请求参数[​](/docs/zh-CN/algo/future-algo/Time-Weighted-Average-Price-New-Order#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES| 交易对 eg. BTCUSDT  
side| ENUM| YES| 买卖方向 ( BUY or SELL )  
positionSide| ENUM| NO| 持仓方向，单向持仓模式下非必填，默认且仅可填BOTH;在双向持仓模式下必填,且仅可选择 LONG 或 SHORT  
quantity| DECIMAL| YES| 下单数量， 以合约币种（base asset）个数下单; 名义价值 (`quantity` * `标记价格(base asset)`) 需要大于 1,000 USDT，且不超过 1,000,000 USDT  
duration| LONG| YES| 请请以秒为单位发送[300,86400]  
clientAlgoId| STRING| NO| 必须传入32位，如果未发送，则自动生成  
reduceOnly| BOOLEAN| NO| true, false; 非双开模式下默认false；双开模式下不接受此参数； 开仓不接受此参数  
limitPrice| DECIMAL| NO| 限价单价格; 若未发送，则以市场价下单  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * 最大所有策略订单挂单数量： 30。
>   * 杠杆倍数和持仓模式与您的合约账户设置相同，您可以通过合约交易页面设置或者通过fapi设置。
>   * 收到 `"success": true` 不代表您的订单一定会被执行。请通过查询订单接口（`GET sapi/v1/algo/futures/openOrders` 或者 `GET sapi/v1/algo/futures/historicalOrders`）以获取订单状态。 例如: 如果您的合约账户余额不足，或者开仓使用了`reduce only`参数，或者您下单选择的持仓模式与您设置的不符，这些情况您都会收到响应 `"success": true`，但订单状态会显示为 `expired`，代表订单过期。
>   * `quantity` * 60 / `duration` 必须大于minQty。
>   * `duration` 不能小于5分钟，且不能大于24小时。
>   * 对于U本位交割合约, TWAP 的结束时间必须早于交割时间1小时。
>   * 您的 API Key 需要开通相应的权限: 
>     * `允许合约交易` 权限 — 适用于经典交易账户模式
>     * `允许组合保证金交易` 权限 — 适用于组合保证金账户模式
>   * 请使用Base URL: <https://api.binance.com>
> 


## 响应示例[​](/docs/zh-CN/algo/future-algo/Time-Weighted-Average-Price-New-Order#响应示例 "响应示例的直接链接")
    
    
    {  
        "clientAlgoId": "65ce1630101a480b85915d7e11fd5078", //用户自定义策略订单ID  
        "success": true,  
        "code": 0,  
        "msg": "OK"  
    }