---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/coin-margined-futures/trade/websocket-api/Modify-Order
api_type: WebSocket
updated_at: 2026-01-15T23:39:57.135988
---

# Modify Order (TRADE)

## API Description[​](/docs/derivatives/coin-margined-futures/trade/websocket-api/Modify-Order#api-description "Direct link to API Description")

Order modify function, currently only LIMIT order modification is supported, modified orders will be reordered in the match queue

## Method[​](/docs/derivatives/coin-margined-futures/trade/websocket-api/Modify-Order#method "Direct link to Method")

`order.modify`

## Request[​](/docs/derivatives/coin-margined-futures/trade/websocket-api/Modify-Order#request "Direct link to Request")
    
    
    {  
      "id": "88601d02-bd0d-430d-8733-2708a569ebda",  
      "method": "order.modify",  
      "params": {  
        "apiKey": "",  
        "orderId": 333245211,  
        "price": "51000",  
        "quantity": 1,  
        "side": "BUY",  
        "symbol": "BTCUSD_PERP",  
        "timestamp": 1728415697189,  
        "signature": "0f04368b2d22aafd0ggc8809ea34297eff602272917b5f01267db4efbc1c9422"  
       }  
    }  
    

## Request Weight[​](/docs/derivatives/coin-margined-futures/trade/websocket-api/Modify-Order#request-weight "Direct link to Request Weight")

1 on 10s order rate limit(X-MBX-ORDER-COUNT-10S); 1 on 1min order rate limit(X-MBX-ORDER-COUNT-1M); 1 on IP rate limit(x-mbx-used-weight-1m)

## Request Parameters[​](/docs/derivatives/coin-margined-futures/trade/websocket-api/Modify-Order#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
orderId| LONG| NO|   
origClientOrderId| STRING| NO|   
symbol| STRING| YES|   
side| ENUM| YES| `SELL`, `BUY`  
quantity| DECIMAL| YES| Order quantity, cannot be sent with `closePosition=true`  
price| DECIMAL| YES|   
priceMatch| ENUM| NO| only avaliable for `LIMIT`/`STOP`/`TAKE_PROFIT` order; can be set to `OPPONENT`/ `OPPONENT_5`/ `OPPONENT_10`/ `OPPONENT_20`: /`QUEUE`/ `QUEUE_5`/ `QUEUE_10`/ `QUEUE_20`; Can't be passed together with `price`  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * Either `orderId` or `origClientOrderId` must be sent, and the `orderId` will prevail if both are sent.
>   * Both `quantity` and `price` must be sent, which is different from dapi modify order endpoint.
>   * When the new `quantity` or `price` doesn't satisfy PRICE_FILTER / PERCENT_FILTER / LOT_SIZE, amendment will be rejected and the order will stay as it is.
>   * However the order will be cancelled by the amendment in the following situations: 
>     * when the order is in partially filled status and the new `quantity` <= `executedQty`
>     * When the order is `GTX` and the new price will cause it to be executed immediately
>   * One order can only be modfied for less than 10000 times
> 


## Response Example[​](/docs/derivatives/coin-margined-futures/trade/websocket-api/Modify-Order#response-example "Direct link to Response Example")
    
    
    {  
      "id": "88601d02-bd0d-430d-8733-2708a569ebda",  
      "status": 200,  
      "result": {  
          "orderId": 333245211,  
          "symbol": "BTCUSD_PERP",  
          "pair": "BTCUSD",  
          "status": "NEW",  
          "clientOrderId": "5SztZiGFAxgAqw4J9EN9fA",  
          "price": "51000",  
          "avgPrice": "0.00",  
          "origQty": "1",  
          "executedQty": "0",  
          "cumQty": "0",  
          "cumBase": "0",  
          "timeInForce": "GTC",  
          "type": "LIMIT",  
          "reduceOnly": false,  
          "closePosition": false,  
          "side": "BUY",  
          "positionSide": "BOTH",  
          "stopPrice": "0",  
          "workingType": "CONTRACT_PRICE",  
          "priceProtect": false,  
          "origType": "LIMIT",  
          "updateTime": 1728415765493  
      },  
      "rateLimits": [  
          {  
              "rateLimitType": "REQUEST_WEIGHT",  
              "interval": "MINUTE",  
              "intervalNum": 1,  
              "limit": 2400,  
              "count": 6  
          },  
          {  
              "rateLimitType": "ORDERS",  
              "interval": "MINUTE",  
              "intervalNum": 1,  
              "limit": 1200,  
              "count": 1  
          }  
      ]  
    }

---

# 修改订单 (TRADE)

## 接口描述[​](/docs/zh-CN/derivatives/coin-margined-futures/trade/websocket-api/Modify-Order#接口描述 "接口描述的直接链接")

修改订单功能，当前只支持限价（LIMIT）订单修改，修改后会在撮合队列里重新排序

## 方式[​](/docs/zh-CN/derivatives/coin-margined-futures/trade/websocket-api/Modify-Order#方式 "方式的直接链接")

`order.modify`

## 请求[​](/docs/zh-CN/derivatives/coin-margined-futures/trade/websocket-api/Modify-Order#请求 "请求的直接链接")
    
    
    {  
      "id": "88601d02-bd0d-430d-8733-2708a569ebda",  
      "method": "order.modify",  
      "params": {  
        "apiKey": "",  
        "orderId": 333245211,  
        "price": "51000",  
        "quantity": 1,  
        "side": "BUY",  
        "symbol": "BTCUSD_PERP",  
        "timestamp": 1728415697189,  
        "signature": "0f04368b2d22aafd0ggc8809ea34297eff602272917b5f01267db4efbc1c9422"  
       }  
    }  
    

## 请求权重[​](/docs/zh-CN/derivatives/coin-margined-futures/trade/websocket-api/Modify-Order#请求权重 "请求权重的直接链接")

10s order rate limit(X-MBX-ORDER-COUNT-10S)为1 1min order rate limit(X-MBX-ORDER-COUNT-1M)为1 IP rate limit(x-mbx-used-weight-1m)为1

## 请求参数[​](/docs/zh-CN/derivatives/coin-margined-futures/trade/websocket-api/Modify-Order#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
orderId| LONG| NO| 系统订单号  
origClientOrderId| STRING| NO| 用户自定义的订单号  
symbol| STRING| YES| 交易对  
side| ENUM| YES| 买卖方向 `SELL`, `BUY`  
quantity| DECIMAL| YES| 下单数量,使用`closePosition`不支持此参数。  
price| DECIMAL| YES| 委托价格  
priceMatch| ENUM| NO| `OPPONENT`/ `OPPONENT_5`/ `OPPONENT_10`/ `OPPONENT_20`/`QUEUE`/ `QUEUE_5`/ `QUEUE_10`/ `QUEUE_20`；不能与price同时传  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * `orderId` 与 `origClientOrderId` 必须至少发送一个，同时发送则以 order id为准
>   * `quantity` 与 `price` 均必须发送，这点和 dapi 修改订单不同
>   * 当新订单的`quantity` 或 `price`不满足PRICE_FILTER / PERCENT_FILTER / LOT_SIZE限制，修改会被拒绝，原订单依旧被保留
>   * 订单会在下列情况下被取消： 
>     * 原订单被部分执行且新订单`quantity` <= `executedQty`
>     * 原订单是`GTX`，新订单的价格会导致订单立刻执行
>   * 同一订单修改次数最多10000次
> 


## 响应示例[​](/docs/zh-CN/derivatives/coin-margined-futures/trade/websocket-api/Modify-Order#响应示例 "响应示例的直接链接")
    
    
    {  
      "id": "88601d02-bd0d-430d-8733-2708a569ebda",  
      "status": 200,  
      "result": {  
          "orderId": 333245211,  
          "symbol": "BTCUSD_PERP",  
          "pair": "BTCUSD",  
          "status": "NEW",  
          "clientOrderId": "5SztZiGFAxgAqw4J9EN9fA",  
          "price": "51000",  
          "avgPrice": "0.00",  
          "origQty": "1",  
          "executedQty": "0",  
          "cumQty": "0",  
          "cumBase": "0",  
          "timeInForce": "GTC",  
          "type": "LIMIT",  
          "reduceOnly": false,  
          "closePosition": false,  
          "side": "BUY",  
          "positionSide": "BOTH",  
          "stopPrice": "0",  
          "workingType": "CONTRACT_PRICE",  
          "priceProtect": false,  
          "origType": "LIMIT",  
          "updateTime": 1728415765493  
      },  
      "rateLimits": [  
          {  
              "rateLimitType": "REQUEST_WEIGHT",  
              "interval": "MINUTE",  
              "intervalNum": 1,  
              "limit": 2400,  
              "count": 6  
          },  
          {  
              "rateLimitType": "ORDERS",  
              "interval": "MINUTE",  
              "intervalNum": 1,  
              "limit": 1200,  
              "count": 1  
          }  
      ]  
    }