---
exchange: binance
source_url: https://developers.binance.com/docs/algo/spot-algo/Time-Weighted-Average-Price-New-Order
api_type: REST
updated_at: 2026-01-15T23:49:14.497162
---

# Time-Weighted Average Price(Twap) New Order(TRADE)

## API Description[​](/docs/algo/spot-algo/Time-Weighted-Average-Price-New-Order#api-description "Direct link to API Description")

Place a new spot TWAP order with Algo service.

## HTTP Request[​](/docs/algo/spot-algo/Time-Weighted-Average-Price-New-Order#http-request "Direct link to HTTP Request")

POST `/sapi/v1/algo/spot/newOrderTwap`

## Request Weight(UID)[​](/docs/algo/spot-algo/Time-Weighted-Average-Price-New-Order#request-weightuid "Direct link to Request Weight\(UID\)")

**3000**

## Request Parameters[​](/docs/algo/spot-algo/Time-Weighted-Average-Price-New-Order#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES| Trading symbol eg. BTCUSDT  
side| ENUM| YES| Trading side ( BUY or SELL )  
quantity| DECIMAL| YES| Quantity of base asset; Maximum notional per order is 200k, 2mm or 10mm, depending on symbol. Please reduce your size if you order is above the maximum notional per order.  
duration| LONG| YES| Duration for TWAP orders in seconds. [300, 86400]  
clientAlgoId| STRING| NO| A unique id among Algo orders (length should be 32 characters)， If it is not sent, we will give default value  
limitPrice| DECIMAL| NO| Limit price of the order; If it is not sent, will place order by market price by default  
timestamp| LONG| YES|   
  
>   * Total Algo open orders max allowed: `20` orders.
> 


## Response Example[​](/docs/algo/spot-algo/Time-Weighted-Average-Price-New-Order#response-example "Direct link to Response Example")
    
    
    {  
        "clientAlgoId": "65ce1630101a480b85915d7e11fd5078",  
        "success": true,  
        "code": 0,  
        "msg": "OK"  
    }

---

# 时间加权平均价格策略(Twap)下单(TRADE)

## 接口描述[​](/docs/zh-CN/algo/spot-algo/Time-Weighted-Average-Price-New-Order#接口描述 "接口描述的直接链接")

通过算法服务进行时间加权平均价格策略（TWAP）下单交易

## HTTP请求[​](/docs/zh-CN/algo/spot-algo/Time-Weighted-Average-Price-New-Order#http请求 "HTTP请求的直接链接")

POST `/sapi/v1/algo/spot/newOrderTwap`

## 请求权重(UID)[​](/docs/zh-CN/algo/spot-algo/Time-Weighted-Average-Price-New-Order#请求权重uid "请求权重\(UID\)的直接链接")

**3000**

## 请求参数[​](/docs/zh-CN/algo/spot-algo/Time-Weighted-Average-Price-New-Order#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES| 交易对 eg. BTCUSDT  
side| ENUM| YES| 买卖方向 ( BUY or SELL )  
quantity| DECIMAL| YES| 下单数量， 以Base资产个数下单; 每单支持最大的金额会是200,000， 2,000,000或者10,000,000 USD等额的，取决于币对。请降低您的下单金额，如果您的下单金额超过了上限。  
duration| LONG| YES| 请以秒为单位发送[300,86400]；少于 5 分钟 => 默认为 5 分钟；大于 24h => 默认为 24h  
clientAlgoId| STRING| NO| 必须传入32位，如果未发送，则自动生成  
limitPrice| DECIMAL| NO| 限价单价格; 若未发送，则以市场价下单  
timestamp| LONG| YES|   
  
>   * 最大所有策略订单挂单数量： 20。
> 


## 响应示例[​](/docs/zh-CN/algo/spot-algo/Time-Weighted-Average-Price-New-Order#响应示例 "响应示例的直接链接")
    
    
    {  
        "clientAlgoId": "65ce1630101a480b85915d7e11fd5078", //用户自定义策略订单ID  
        "success": true,   
        "code": 0,  
        "msg": "OK"  
    }