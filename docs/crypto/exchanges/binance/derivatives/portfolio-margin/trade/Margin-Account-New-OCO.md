---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Margin-Account-New-OCO
api_type: Trading
updated_at: 2026-01-15T23:45:29.182664
---

# Margin Account New OCO(TRADE)

## API Description[​](/docs/derivatives/portfolio-margin/trade/Margin-Account-New-OCO#api-description "Direct link to API Description")

Send in a new OCO for a margin account

## HTTP Request[​](/docs/derivatives/portfolio-margin/trade/Margin-Account-New-OCO#http-request "Direct link to HTTP Request")

POST `/papi/v1/margin/order/oco`

## Request Weight(Order)[​](/docs/derivatives/portfolio-margin/trade/Margin-Account-New-OCO#request-weightorder "Direct link to Request Weight\(Order\)")

**1**

## Request Parameters[​](/docs/derivatives/portfolio-margin/trade/Margin-Account-New-OCO#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
listClientOrderId| STRING| NO| A unique Id for the entire orderList  
side| ENUM| YES|   
quantity| DECIMAL| YES|   
limitClientOrderId| STRING| NO| A unique Id for the limit order  
price| DECIMAL| YES|   
limitIcebergQty| DECIMAL| NO|   
stopClientOrderId| STRING| NO| A unique Id for the stop loss/stop loss limit leg  
stopPrice| DECIMAL| YES|   
stopLimitPrice| DECIMAL| NO| If provided, stopLimitTimeInForce is required.  
stopIcebergQty| DECIMAL| NO|   
stopLimitTimeInForce| ENUM| NO| Valid values are `GTC/FOK/IOC`  
newOrderRespType| ENUM| NO| Set the response JSON.  
sideEffectType| ENUM| NO| NO_SIDE_EFFECT, MARGIN_BUY, AUTO_REPAY; default NO_SIDE_EFFECT.  
recvWindow| LONG| NO| The value cannot be greater than `60000`  
timestamp| LONG| YES|   
  
Other Info:

>   * Price Restrictions: 
>     * `SELL`: Limit Price > Last Price > Stop Price
>     * `BUY`: Limit Price < Last Price < Stop Price
>   * Quantity Restrictions: 
>     * Both legs must have the same quantity
>     * `ICEBERG` quantities however do not have to be the same.
>   * Order Rate Limit 
>     * `OCO` counts as 2 orders against the order rate limit.
> 


## Response Example[​](/docs/derivatives/portfolio-margin/trade/Margin-Account-New-OCO#response-example "Direct link to Response Example")
    
    
    {  
      "orderListId": 0,  
      "contingencyType": "OCO",  
      "listStatusType": "EXEC_STARTED",  
      "listOrderStatus": "EXECUTING",  
      "listClientOrderId": "JYVpp3F0f5CAG15DhtrqLp",  
      "transactionTime": 1563417480525,  
      "symbol": "LTCBTC",  
      "marginBuyBorrowAmount": "5",       // will not return if no margin trade happens  
      "marginBuyBorrowAsset": "BTC",    // will not return if no margin trade happens  
      "orders": [  
        {  
          "symbol": "LTCBTC",  
          "orderId": 2,  
          "clientOrderId": "Kk7sqHb9J6mJWTMDVW7Vos"  
        },  
        {  
          "symbol": "LTCBTC",  
          "orderId": 3,  
          "clientOrderId": "xTXKaGYd4bluPVp78IVRvl"  
        }  
      ],  
      "orderReports": [  
        {  
          "symbol": "LTCBTC",  
          "orderId": 2,  
          "orderListId": 0,  
          "clientOrderId": "Kk7sqHb9J6mJWTMDVW7Vos",  
          "transactTime": 1563417480525,  
          "price": "0.000000",  
          "origQty": "0.624363",  
          "executedQty": "0.000000",  
          "cummulativeQuoteQty": "0.000000",  
          "status": "NEW",  
          "timeInForce": "GTC",  
          "type": "STOP_LOSS",  
          "side": "BUY",  
          "stopPrice": "0.960664"  
        },  
        {  
          "symbol": "LTCBTC",  
          "orderId": 3,  
          "orderListId": 0,  
          "clientOrderId": "xTXKaGYd4bluPVp78IVRvl",  
          "transactTime": 1563417480525,  
          "price": "0.036435",  
          "origQty": "0.624363",  
          "executedQty": "0.000000",  
          "cummulativeQuoteQty": "0.000000",  
          "status": "NEW",  
          "timeInForce": "GTC",  
          "type": "LIMIT_MAKER",  
          "side": "BUY"  
        }  
      ]  
    }

---

# 杠杆账户 OCO 下单 (TRADE)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Margin-Account-New-OCO#接口描述 "接口描述的直接链接")

杠杆账户发送新 OCO 订单

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Margin-Account-New-OCO#http请求 "HTTP请求的直接链接")

POST `/papi/v1/margin/order/oco`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Margin-Account-New-OCO#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Margin-Account-New-OCO#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES|   
listClientOrderId| STRING| NO| 整个 orderList 的唯一 ID  
side| ENUM| YES| 详见枚举定义：订单方向  
quantity| DECIMAL| YES|   
limitClientOrderId| STRING| NO| 限价单的唯一 ID  
price| DECIMAL| YES|   
limitIcebergQty| DECIMAL| NO|   
stopClientOrderId| STRING| NO| 止损/止损限价单的唯一 ID  
stopPrice| DECIMAL| YES|   
stopLimitPrice| DECIMAL| NO| 如果提供，须配合提交`stopLimitTimeInForce`  
stopIcebergQty| DECIMAL| NO|   
stopLimitTimeInForce| ENUM| NO| 有效值 `GTC/FOK/IOC`  
newOrderRespType| ENUM| NO| 详见枚举定义：订单返回类型  
sideEffectType| ENUM| NO| NO_SIDE_EFFECT, MARGIN_BUY, AUTO_REPAY; 默认为 NO_SIDE_EFFECT  
recvWindow| LONG| NO| 不能大于 `60000`  
timestamp| LONG| YES|   
  
Other Info:

>   * 价格限制： 
>     * `SELL`: 限价 > 最新成交价 >触发价
>     * `BUY`: 限价 < 最新成交价 < 触发价
>   * 数量限制： 
>     * 两个 legs 必须具有同样的数量
>     * `ICEBERG` 数量不必相同
>   * 下单 rate： 
>     * 一个`OCO`订单被算成 2 个普通订单
> 


## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Margin-Account-New-OCO#响应示例 "响应示例的直接链接")
    
    
    {  
      "orderListId": 0,  
      "contingencyType": "OCO",  
      "listStatusType": "EXEC_STARTED",  
      "listOrderStatus": "EXECUTING",  
      "listClientOrderId": "JYVpp3F0f5CAG15DhtrqLp",  
      "transactionTime": 1563417480525,  
      "symbol": "LTCBTC",  
      "marginBuyBorrowAmount": "5",       // 下单后没有发生借款则不返回该字段  
      "marginBuyBorrowAsset": "BTC",    // 下单后没有发生借款则不返回该字段  
      "orders": [  
        {  
          "symbol": "LTCBTC",  
          "orderId": 2,  
          "clientOrderId": "Kk7sqHb9J6mJWTMDVW7Vos"  
        },  
        {  
          "symbol": "LTCBTC",  
          "orderId": 3,  
          "clientOrderId": "xTXKaGYd4bluPVp78IVRvl"  
        }  
      ],  
      "orderReports": [  
        {  
          "symbol": "LTCBTC",  
          "orderId": 2,  
          "orderListId": 0,  
          "clientOrderId": "Kk7sqHb9J6mJWTMDVW7Vos",  
          "transactTime": 1563417480525,  
          "price": "0.000000",  
          "origQty": "0.624363",  
          "executedQty": "0.000000",  
          "cummulativeQuoteQty": "0.000000",  
          "status": "NEW",  
          "timeInForce": "GTC",  
          "type": "STOP_LOSS",  
          "side": "BUY",  
          "stopPrice": "0.960664"  
        },  
        {  
          "symbol": "LTCBTC",  
          "orderId": 3,  
          "orderListId": 0,  
          "clientOrderId": "xTXKaGYd4bluPVp78IVRvl",  
          "transactTime": 1563417480525,  
          "price": "0.036435",  
          "origQty": "0.624363",  
          "executedQty": "0.000000",  
          "cummulativeQuoteQty": "0.000000",  
          "status": "NEW",  
          "timeInForce": "GTC",  
          "type": "LIMIT_MAKER",  
          "side": "BUY"  
        }  
      ]  
    }