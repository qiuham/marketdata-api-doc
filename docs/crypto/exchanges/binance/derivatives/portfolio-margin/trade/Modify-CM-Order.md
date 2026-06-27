---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Modify-CM-Order
api_type: Trading
updated_at: 2026-01-15T23:45:33.529574
---

# Modify CM Order(TRADE)

## API Description[​](/docs/derivatives/portfolio-margin/trade/Modify-CM-Order#api-description "Direct link to API Description")

Order modify function, currently only LIMIT order modification is supported, modified orders will be reordered in the match queue

## HTTP Request[​](/docs/derivatives/portfolio-margin/trade/Modify-CM-Order#http-request "Direct link to HTTP Request")

PUT `/papi/v1/cm/order`

## Request Weight(Order)[​](/docs/derivatives/portfolio-margin/trade/Modify-CM-Order#request-weightorder "Direct link to Request Weight\(Order\)")

**1**

## Request Parameters[​](/docs/derivatives/portfolio-margin/trade/Modify-CM-Order#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
orderId| LONG| NO|   
origClientOrderId| STRING| NO|   
symbol| STRING| YES|   
side| ENUM| YES| SELL, BUY  
quantity| DECIMAL| YES| Order quantity  
price| DECIMAL| YES|   
priceMatch| ENUM| NO| only avaliable for `LIMIT`/`STOP`/`TAKE_PROFIT` order; can be set to `OPPONENT`/ `OPPONENT_5`/ `OPPONENT_10`/ `OPPONENT_20`: /`QUEUE`/ `QUEUE_5`/ `QUEUE_10`/ `QUEUE_20`; Can't be passed together with `price`  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * Either `orderId` or `origClientOrderId` must be sent, and the `orderId` will prevail if both are sent.
>   * Both `quantity` and `price` must be sent
>   * When the new `quantity` or `price` doesn't satisfy PRICE_FILTER / PERCENT_FILTER / LOT_SIZE, amendment will be rejected and the order will stay as it is.
>   * However the order will be cancelled by the amendment in the following situations: 
>     * when the order is in partially filled status and the new `quantity` <= `executedQty`
>     * When the order is `GTX` and the new price will cause it to be executed immediately
> 


## Response Example[​](/docs/derivatives/portfolio-margin/trade/Modify-CM-Order#response-example "Direct link to Response Example")
    
    
    {  
        "orderId": 20072994037,  
        "symbol": "BTCUSD_PERP",  
        "pair": "BTCUSD",  
        "status": "NEW",  
        "clientOrderId": "LJ9R4QZDihCaS8UAOOLpgW",  
        "price": "30005",  
        "avgPrice": "0.0",  
        "origQty": "1",  
        "executedQty": "0",  
        "cumQty": "0",  
        "cumBase": "0",  
        "timeInForce": "GTC",  
        "type": "LIMIT",  
        "reduceOnly": false,  
        "side": "BUY",  
        "positionSide": "LONG",  
        "origType": "LIMIT",  
        "updateTime": 1629182711600  
    }

---

# 修改CM订单(TRADE)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Modify-CM-Order#接口描述 "接口描述的直接链接")

修改CM订单功能，当前只支持限价（LIMIT）订单修改，修改后会在撮合队列里重新排序

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Modify-CM-Order#http请求 "HTTP请求的直接链接")

PUT `/papi/v1/cm/order`

## 请求权重(Order)[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Modify-CM-Order#请求权重order "请求权重\(Order\)的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Modify-CM-Order#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
orderId| LONG| NO| 系统订单号  
origClientOrderId| STRING| NO| 用户自定义的订单号  
symbol| STRING| YES| 交易对  
side| ENUM| YES| 买卖方向 `SELL`, `BUY`; `side`需要和原订单相同  
quantity| DECIMAL| YES| 下单数量  
price| DECIMAL| YES| 委托价格  
priceMatch| ENUM| NO| `OPPONENT`/ `OPPONENT_5`/ `OPPONENT_10`/ `OPPONENT_20`/`QUEUE`/ `QUEUE_5`/ `QUEUE_10`/ `QUEUE_20`；不能与price同时传  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * `orderId` 与 `origClientOrderId` 必须至少发送一个，同时发送则以 order id为准
>   * `quantity` 与 `price` 必须全部发送
>   * 当新订单的`quantity` 或 `price`不满足PRICE_FILTER / PERCENT_FILTER / LOT_SIZE限制，修改会被拒绝，原订单依旧被保留
>   * 订单会在下列情况下被取消： 
>     * 原订单被部分执行且新订单`quantity` <= `executedQty`
>     * 原订单是`GTX`，新订单的价格会导致订单立刻执行
>   * 同一订单修改次数最多10000次
> 


## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Modify-CM-Order#响应示例 "响应示例的直接链接")
    
    
    {  
        "orderId": 20072994037,  
        "symbol": "BTCUSD_PERP",  
        "pair": "BTCUSD",  
        "status": "NEW",  
        "clientOrderId": "LJ9R4QZDihCaS8UAOOLpgW",  
        "price": "30005",  
        "avgPrice": "0.0",  
        "origQty": "1",  
        "executedQty": "0",  
        "cumQty": "0",  
        "cumBase": "0",  
        "timeInForce": "GTC",  
        "type": "LIMIT",  
        "reduceOnly": false,  
        "side": "BUY",  
        "positionSide": "LONG",  
        "origType": "LIMIT",  
        "updateTime": 1629182711600  
    }