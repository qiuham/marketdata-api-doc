---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/websocket-api/New-Algo-Order
api_type: WebSocket
updated_at: 2026-01-15T23:47:35.077561
---

# New Algo Order(TRADE)

## API Description[​](/docs/derivatives/usds-margined-futures/trade/websocket-api/New-Algo-Order#api-description "Direct link to API Description")

Send in a new algo order.

## Method[​](/docs/derivatives/usds-margined-futures/trade/websocket-api/New-Algo-Order#method "Direct link to Method")

`algoOrder.place`

## Request[​](/docs/derivatives/usds-margined-futures/trade/websocket-api/New-Algo-Order#request "Direct link to Request")
    
    
    {  
    	"id": "7731f6b5-8d5e-419c-a424-016b0a5fe8d7",  
    	"method": "algoOrder.place",  
    	"params": {  
    		"algoType": "CONDITIONAL",  
    		"apiKey": "autoApiKey7mM4kPWaRuTUypdTEZKG8U8tDjO64xdBJBrmE1nXU2XSwdxGPyXcYx",  
    		"newOrderRespType": "RESULT",  
    		"positionSide": "SHORT",  
    		"price": "160000",  
    		"quantity": "1",  
    		"recvWindow": "99999999",  
    		"side": "SELL",  
    		"symbol": "BTCUSDT",  
    		"timeInForce": "GTC",  
    		"timestamp": 1762506268690,  
    		"triggerprice": 120000,  
    		"type": "TAKE_PROFIT",  
    		"signature": "ec6e529c69fd8193b19484907bc713114eae06259fcab9728dafd5910f9cac5a"  
    	}  
    }  
    

## Request Weight[​](/docs/derivatives/usds-margined-futures/trade/websocket-api/New-Algo-Order#request-weight "Direct link to Request Weight")

**0**

## Request Parameters[​](/docs/derivatives/usds-margined-futures/trade/websocket-api/New-Algo-Order#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
algoType| ENUM| YES| Only support `CONDITIONAL`  
symbol| STRING| YES|   
side| ENUM| YES|   
positionSide| ENUM| NO| Default `BOTH` for One-way Mode ; `LONG` or `SHORT` for Hedge Mode. It must be sent in Hedge Mode.  
type| ENUM| YES| For `CONDITIONAL` algoType, `STOP_MARKET`/`TAKE_PROFIT_MARKET`/`STOP`/`TAKE_PROFIT`/`TRAILING_STOP_MARKET` as order type  
timeInForce| ENUM| NO| `IOC` or `GTC` or `FOK`, default `GTC`  
quantity| DECIMAL| NO| Cannot be sent with `closePosition`=`true`(Close-All)  
price| DECIMAL| NO|   
triggerPrice| DECIMAL| NO|   
workingType| ENUM| NO| triggerPrice triggered by: `MARK_PRICE`, `CONTRACT_PRICE`. Default `CONTRACT_PRICE`  
priceMatch| ENUM| NO| only avaliable for `LIMIT`/`STOP`/`TAKE_PROFIT` order; can be set to `OPPONENT`/ `OPPONENT_5`/ `OPPONENT_10`/ `OPPONENT_20`: /`QUEUE`/ `QUEUE_5`/ `QUEUE_10`/ `QUEUE_20`; Can't be passed together with `price`  
closePosition| STRING| NO| true, false；Close-All，used with `STOP_MARKET` or `TAKE_PROFIT_MARKET`.  
priceProtect| STRING| NO| "TRUE" or "FALSE", default "FALSE". Used with `STOP_MARKET` or `TAKE_PROFIT_MARKET` order. when price reaches the triggerPrice ，the difference rate between "MARK_PRICE" and "CONTRACT_PRICE" cannot be larger than the Price Protection Threshold of the symbol.  
reduceOnly| STRING| NO| "true" or "false". default "false". Cannot be sent in Hedge Mode; cannot be sent with `closePosition`=`true`  
activatePrice| DECIMAL| NO| Used with `TRAILING_STOP_MARKET` orders, default as the latest price(supporting different `workingType`)  
callbackRate| DECIMAL| NO| Used with `TRAILING_STOP_MARKET` orders, min 0.1, max 10 where 1 for 1%  
clientAlgoId| STRING| NO| A unique id among open orders. Automatically generated if not sent. Can only be string following the rule: `^[\.A-Z\:/a-z0-9_-]{1,36}$`  
selfTradePreventionMode| ENUM| NO| `EXPIRE_TAKER`:expire taker order when STP triggers/ `EXPIRE_MAKER`:expire taker order when STP triggers/ `EXPIRE_BOTH`:expire both orders when STP triggers; default `NONE`  
goodTillDate| LONG| NO| order cancel time for timeInForce `GTD`, mandatory when `timeInforce` set to `GTD`; order the timestamp only retains second-level precision, ms part will be ignored; The goodTillDate timestamp must be greater than the current time plus 600 seconds and smaller than 253402300799000  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * Condition orders will be triggered when:
> 
>     * If parameter`priceProtect`is sent as true: 
>       * when price reaches the `triggerPrice` ，the difference rate between "MARK_PRICE" and "CONTRACT_PRICE" cannot be larger than the "triggerProtect" of the symbol
>       * "triggerProtect" of a symbol can be got from `GET /fapi/v1/exchangeInfo`
>     * `STOP`, `STOP_MARKET`: 
>       * BUY: latest price ("MARK_PRICE" or "CONTRACT_PRICE") >= `triggerPrice`
>       * SELL: latest price ("MARK_PRICE" or "CONTRACT_PRICE") <= `triggerPrice`
>     * `TAKE_PROFIT`, `TAKE_PROFIT_MARKET`: 
>       * BUY: latest price ("MARK_PRICE" or "CONTRACT_PRICE") <= `triggerPrice`
>       * SELL: latest price ("MARK_PRICE" or "CONTRACT_PRICE") >= `triggerPrice`
>     * `TRAILING_STOP_MARKET`: 
>       * BUY: the lowest price after order placed <= `activatePrice`, and the latest price >= the lowest price * (1 + `callbackRate`)
>       * SELL: the highest price after order placed >= `activatePrice`, and the latest price <= the highest price * (1 - `callbackRate`)
>   * For `TRAILING_STOP_MARKET`, if you got such error code.  
>  `{"code": -2021, "msg": "Order would immediately trigger."}`  
>  means that the parameters you send do not meet the following requirements:
> 
>     * BUY: `activatePrice` should be smaller than latest price.
>     * SELL: `activatePrice` should be larger than latest price.
>   * `STOP_MARKET`, `TAKE_PROFIT_MARKET` with `closePosition`=`true`:
> 
>     * Follow the same rules for condition orders.
>     * If triggered，**close all** current long position( if `SELL`) or current short position( if `BUY`).
>     * Cannot be used with `quantity` paremeter
>     * Cannot be used with `reduceOnly` parameter
>     * In Hedge Mode,cannot be used with `BUY` orders in `LONG` position side. and cannot be used with `SELL` orders in `SHORT` position side
>   * `selfTradePreventionMode` is only effective when `timeInForce` set to `IOC` or `GTC` or `GTD`.
> 
> 


## Response Example[​](/docs/derivatives/usds-margined-futures/trade/websocket-api/New-Algo-Order#response-example "Direct link to Response Example")
    
    
    {  
      "id": "06c9dbd8-ccbf-4ecf-a29c-fe31495ac73f",  
      "status": 200,  
      "result": {  
        "algoId": 3000000000003505,  
        "clientAlgoId": "0Xkl1p621E4EryvufmYre1",  
        "algoType": "CONDITIONAL",  
        "orderType": "TAKE_PROFIT",  
        "symbol": "BTCUSDT",  
        "side": "SELL",  
        "positionSide": "SHORT",  
        "timeInForce": "GTC",  
        "quantity": "1.000",  
        "algoStatus": "NEW",  
        "triggerPrice": "120000.00",  
        "price": "160000.00",  
        "icebergQuantity": null,  
        "selfTradePreventionMode": "EXPIRE_MAKER",  
        "workingType": "CONTRACT_PRICE",  
        "priceMatch": "NONE",  
        "closePosition": false,  
        "priceProtect": false,  
        "reduceOnly": false,  
        "createTime": 1762507264142,  
        "updateTime": 1762507264143,  
        "triggerTime": 0,  
        "goodTillDate": 0  
      },  
      "rateLimits": [  
        {  
          "rateLimitType": "REQUEST_WEIGHT",  
          "interval": "MINUTE",  
          "intervalNum": 1,  
          "limit": 2400,  
          "count": 1  
        }  
      ]  
    }

---

# 条件单下单 (TRADE)

## 接口描述[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/websocket-api/New-Algo-Order#接口描述 "接口描述的直接链接")

条件单下单

## 方式[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/websocket-api/New-Algo-Order#方式 "方式的直接链接")

`algoOrder.place`

## 请求[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/websocket-api/New-Algo-Order#请求 "请求的直接链接")
    
    
    {  
    	"id": "7731f6b5-8d5e-419c-a424-016b0a5fe8d7",  
    	"method": "algoOrder.place",  
    	"params": {  
    		"algoType": "CONDITIONAL",  
    		"apiKey": "autoApiKey7mM4kPWaRuTUypdTEZKG8U8tDjO64xdBJBrmE1nXU2XSwdxGPyXcYx",  
    		"newOrderRespType": "RESULT",  
    		"positionSide": "SHORT",  
    		"price": "160000",  
    		"quantity": "1",  
    		"recvWindow": "99999999",  
    		"side": "SELL",  
    		"symbol": "BTCUSDT",  
    		"timeInForce": "GTC",  
    		"timestamp": 1762506268690,  
    		"triggerprice": 120000,  
    		"type": "TAKE_PROFIT",  
    		"signature": "ec6e529c69fd8193b19484907bc713114eae06259fcab9728dafd5910f9cac5a"  
    	}  
    }  
    

## 请求权重[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/websocket-api/New-Algo-Order#请求权重 "请求权重的直接链接")

**0**

## 请求参数[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/websocket-api/New-Algo-Order#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
algoType| ENUM| YES| 仅支持 `CONDITIONAL`  
symbol| STRING| YES| 交易对  
side| ENUM| YES| 买卖方向 `SELL`, `BUY`  
positionSide| ENUM| NO| 持仓方向，单向持仓模式下非必填，默认且仅可填`BOTH`;在双向持仓模式下必填,且仅可选择 `LONG` 或 `SHORT`  
type| ENUM| YES| 条件订单类型 `STOP`, `TAKE_PROFIT`, `STOP_MARKET`, `TAKE_PROFIT_MARKET`, `TRAILING_STOP_MARKET`  
timeInForce| ENUM| NO| `IOC` or `GTC` or `FOK`, 默认 `GTC`  
quantity| DECIMAL| NO| 下单数量,使用`closePosition`不支持此参数。  
price| DECIMAL| NO| 委托价格  
triggerPrice| DECIMAL| NO| 触发价  
workingType| ENUM| NO| 触发类型: `MARK_PRICE`(标记价格), `CONTRACT_PRICE`(合约最新价). 默认 `CONTRACT_PRICE`  
priceMatch| ENUM| NO| `OPPONENT`/ `OPPONENT_5`/ `OPPONENT_10`/ `OPPONENT_20`/`QUEUE`/ `QUEUE_5`/ `QUEUE_10`/ `QUEUE_20`；不能与price同时传  
closePosition| STRING| NO| `true`, `false`；触发后全部平仓，仅支持`STOP_MARKET`和`TAKE_PROFIT_MARKET`；不与`quantity`合用；自带只平仓效果，不与`reduceOnly` 合用  
priceProtect| STRING| NO| 条件单触发保护："TRUE","FALSE", 默认"FALSE".  
reduceOnly| STRING| NO| `true`, `false`; 非双开模式下默认`false`；双开模式下不接受此参数； 使用`closePosition`不支持此参数。  
activatePrice| DECIMAL| NO| 追踪止损激活价格，仅`TRAILING_STOP_MARKET` 需要此参数, 默认为下单当前市场价格(支持不同`workingType`)  
callbackRate| DECIMAL| NO| 追踪止损回调比例，可取值范围[0.1, 10],其中 1代表1% ,仅`TRAILING_STOP_MARKET` 需要此参数  
clientAlgoId| STRING| NO| 用户自定义的条件订单号，不可以重复出现在挂单中。如空缺系统会自动赋值。必须满足正则规则 `^[\.A-Z\:/a-z0-9_-]{1,36}$`  
newOrderRespType| ENUM| NO| "ACK", "RESULT", 默认 "ACK"  
selfTradePreventionMode| ENUM| NO| `EXPIRE_TAKER`/ `EXPIRE_MAKER`/ `EXPIRE_BOTH`； 默认`NONE`  
goodTillDate| LONG| NO| TIF为GTD时订单的自动取消时间， 当`timeInforce`为`GTD`时必传；传入的时间戳仅保留秒级精度，毫秒级部分会被自动忽略，时间戳需大于当前时间+600s且小于253402300799000  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * 条件单的触发必须:
> 
>     * 如果订单参数`priceProtect`为true: 
>       * 达到触发价时，`MARK_PRICE`(标记价格)与`CONTRACT_PRICE`(合约最新价)之间的价差不能超过改symbol触发保护阈值
>       * 触发保护阈值请参考接口`GET /fapi/v1/exchangeInfo` 返回内容相应symbol中"triggerProtect"字段
>     * `STOP`, `STOP_MARKET` 止损单: 
>       * 买入: 最新合约价格/标记价格高于等于触发价`stopPrice`
>       * 卖出: 最新合约价格/标记价格低于等于触发价`stopPrice`
>     * `TAKE_PROFIT`, `TAKE_PROFIT_MARKET` 止盈单: 
>       * 买入: 最新合约价格/标记价格低于等于触发价`stopPrice`
>       * 卖出: 最新合约价格/标记价格高于等于触发价`stopPrice`
>     * `TRAILING_STOP_MARKET` 跟踪止损单: 
>       * 买入: 当合约价格/标记价格区间最低价格低于激活价格`activatePrice`,且最新合约价格/标记价高于等于最低价设定回调幅度。
>       * 卖出: 当合约价格/标记价格区间最高价格高于激活价格`activatePrice`,且最新合约价格/标记价低于等于最高价设定回调幅度。
>   * `TRAILING_STOP_MARKET` 跟踪止损单如果遇到报错 `{"code": -2021, "msg": "Order would immediately trigger."}`  
>  表示订单不满足以下条件:
> 
>     * 买入: 指定的`activatePrice` 必须小于 latest price
>     * 卖出: 指定的`activatePrice` 必须大于 latest price
>   * `STOP_MARKET`, `TAKE_PROFIT_MARKET` 配合 `closePosition`=`true`:
> 
>     * 条件单触发依照上述条件单触发逻辑
>     * 条件触发后，平掉当时持有所有多头仓位(若为卖单)或当时持有所有空头仓位(若为买单)
>     * 不支持 `quantity` 参数
>     * 自带只平仓属性，不支持`reduceOnly`参数
>     * 双开模式下,`LONG`方向上不支持`BUY`; `SHORT` 方向上不支持`SELL`
>   * `selfTradePreventionMode` 仅在 `timeInForce`为`IOC`或`GTC`或`GTD`时生效.
> 
> 


## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/websocket-api/New-Algo-Order#响应示例 "响应示例的直接链接")
    
    
    {  
      "id": "06c9dbd8-ccbf-4ecf-a29c-fe31495ac73f",  
      "status": 200,  
      "result": {  
        "algoId": 3000000000003505,  
        "clientAlgoId": "0Xkl1p621E4EryvufmYre1",  
        "algoType": "CONDITIONAL",  
        "orderType": "TAKE_PROFIT",  
        "symbol": "BTCUSDT",  
        "side": "SELL",  
        "positionSide": "SHORT",  
        "timeInForce": "GTC",  
        "quantity": "1.000",  
        "algoStatus": "NEW",  
        "triggerPrice": "120000.00",  
        "price": "160000.00",  
        "icebergQuantity": null,  
        "selfTradePreventionMode": "EXPIRE_MAKER",  
        "workingType": "CONTRACT_PRICE",  
        "priceMatch": "NONE",  
        "closePosition": false,  
        "priceProtect": false,  
        "reduceOnly": false,  
        "createTime": 1762507264142,  
        "updateTime": 1762507264143,  
        "triggerTime": 0,  
        "goodTillDate": 0  
      },  
      "rateLimits": [  
        {  
          "rateLimitType": "REQUEST_WEIGHT",  
          "interval": "MINUTE",  
          "intervalNum": 1,  
          "limit": 2400,  
          "count": 1  
        }  
      ]  
    }