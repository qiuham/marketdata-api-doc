---
exchange: binance
source_url: https://developers.binance.com/docs/margin_trading/trade/Margin-Account-Cancel-All-Open-Orders
api_type: Trading
updated_at: 2026-05-27 18:57:28.908756
---

# Margin Account Cancel all Open Orders on a Symbol (TRADE)

## API Description[​](/docs/margin_trading/trade/Margin-Account-Cancel-All-Open-Orders#api-description "Direct link to API Description")

Cancels all active orders on a symbol for margin account.  
  
This includes OCO orders.

## HTTP Request[​](/docs/margin_trading/trade/Margin-Account-Cancel-All-Open-Orders#http-request "Direct link to HTTP Request")

DELETE /sapi/v1/margin/openOrders

## Request Weight[​](/docs/margin_trading/trade/Margin-Account-Cancel-All-Open-Orders#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/margin_trading/trade/Margin-Account-Cancel-All-Open-Orders#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
isIsolated| STRING| NO| for isolated margin or not, "TRUE", "FALSE"，default "FALSE"  
recvWindow| LONG| NO| The value cannot be greater than `60000`  
timestamp| LONG| YES|   
  
## Response Example[​](/docs/margin_trading/trade/Margin-Account-Cancel-All-Open-Orders#response-example "Direct link to Response Example")
    
    
    [  
      {  
        "symbol": "BTCUSDT",  
        "isIsolated": true,       // if isolated margin  
        "origClientOrderId": "E6APeyTJvkMvLMYMqu1KQ4",  
        "orderId": 11,  
        "orderListId": -1,  
        "clientOrderId": "pXLV6Hz6mprAcVYpVMTGgx",  
        "price": "0.089853",  
        "origQty": "0.178622",  
        "executedQty": "0.000000",  
        "cummulativeQuoteQty": "0.000000",  
        "status": "CANCELED",  
        "timeInForce": "GTC",  
        "type": "LIMIT",  
        "side": "BUY",  
        "selfTradePreventionMode": "NONE"  
      },  
      {  
        "symbol": "BTCUSDT",  
        "isIsolated": false,       // if isolated margin  
        "origClientOrderId": "A3EF2HCwxgZPFMrfwbgrhv",  
        "orderId": 13,  
        "orderListId": -1,  
        "clientOrderId": "pXLV6Hz6mprAcVYpVMTGgx",  
        "price": "0.090430",  
        "origQty": "0.178622",  
        "executedQty": "0.000000",  
        "cummulativeQuoteQty": "0.000000",  
        "status": "CANCELED",  
        "timeInForce": "GTC",  
        "type": "LIMIT",  
        "side": "BUY",  
        "selfTradePreventionMode": "NONE"  
      },  
      {  
        "orderListId": 1929,  
        "contingencyType": "OCO",  
        "listStatusType": "ALL_DONE",  
        "listOrderStatus": "ALL_DONE",  
        "listClientOrderId": "2inzWQdDvZLHbbAmAozX2N",  
        "transactionTime": 1585230948299,  
        "symbol": "BTCUSDT",  
        "isIsolated": true,       // if isolated margin  
        "orders": [  
          {  
            "symbol": "BTCUSDT",  
            "orderId": 20,  
            "clientOrderId": "CwOOIPHSmYywx6jZX77TdL"  
          },  
          {  
            "symbol": "BTCUSDT",  
            "orderId": 21,  
            "clientOrderId": "461cPg51vQjV3zIMOXNz39"  
          }  
        ],  
        "orderReports": [  
          {  
            "symbol": "BTCUSDT",  
            "origClientOrderId": "CwOOIPHSmYywx6jZX77TdL",  
            "orderId": 20,  
            "orderListId": 1929,  
            "clientOrderId": "pXLV6Hz6mprAcVYpVMTGgx",  
            "price": "0.668611",  
            "origQty": "0.690354",  
            "executedQty": "0.000000",  
            "cummulativeQuoteQty": "0.000000",  
            "status": "CANCELED",  
            "timeInForce": "GTC",  
            "type": "STOP_LOSS_LIMIT",  
            "side": "BUY",  
            "stopPrice": "0.378131",  
            "icebergQty": "0.017083"  
          },  
          {  
            "symbol": "BTCUSDT",  
            "origClientOrderId": "461cPg51vQjV3zIMOXNz39",  
            "orderId": 21,  
            "orderListId": 1929,  
            "clientOrderId": "pXLV6Hz6mprAcVYpVMTGgx",  
            "price": "0.008791",  
            "origQty": "0.690354",  
            "executedQty": "0.000000",  
            "cummulativeQuoteQty": "0.000000",  
            "status": "CANCELED",  
            "timeInForce": "GTC",  
            "type": "LIMIT_MAKER",  
            "side": "BUY",  
            "icebergQty": "0.639962"  
          }  
        ]  
      }  
    ]

---

# 杠杆账户撤销单一交易对的所有挂单 (TRADE)

## 接口描述[​](/docs/zh-CN/margin_trading/trade/Margin-Account-Cancel-All-Open-Orders#接口描述 "接口描述的直接链接")

杠杆账户撤销单一交易对下所有挂单, 包括OCO的挂单。

## HTTP请求[​](/docs/zh-CN/margin_trading/trade/Margin-Account-Cancel-All-Open-Orders#http请求 "HTTP请求的直接链接")

DELETE /sapi/v1/margin/openOrders

## 请求权重[​](/docs/zh-CN/margin_trading/trade/Margin-Account-Cancel-All-Open-Orders#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/margin_trading/trade/Margin-Account-Cancel-All-Open-Orders#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES|   
isIsolated| STRING| NO| 是否逐仓杠杆，"TRUE", "FALSE", 默认 "FALSE"  
recvWindow| LONG| NO| 赋值不能大于 `60000`  
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/margin_trading/trade/Margin-Account-Cancel-All-Open-Orders#响应示例 "响应示例的直接链接")
    
    
    [  
      {  
        "symbol": "BTCUSDT",  
        "isIsolated": true,       // 是否是逐仓symbol交易   
        "origClientOrderId": "E6APeyTJvkMvLMYMqu1KQ4",  
        "orderId": 11,  
        "orderListId": -1,  
        "clientOrderId": "pXLV6Hz6mprAcVYpVMTGgx",  
        "price": "0.089853",  
        "origQty": "0.178622",  
        "executedQty": "0.000000",  
        "cummulativeQuoteQty": "0.000000",  
        "status": "CANCELED",  
        "timeInForce": "GTC",  
        "type": "LIMIT",  
        "side": "BUY",  
        "selfTradePreventionMode": "NONE"  
      },  
      {  
        "symbol": "BTCUSDT",  
        "isIsolated": false,       // 是否是逐仓symbol交易   
        "origClientOrderId": "A3EF2HCwxgZPFMrfwbgrhv",  
        "orderId": 13,  
        "orderListId": -1,  
        "clientOrderId": "pXLV6Hz6mprAcVYpVMTGgx",  
        "price": "0.090430",  
        "origQty": "0.178622",  
        "executedQty": "0.000000",  
        "cummulativeQuoteQty": "0.000000",  
        "status": "CANCELED",  
        "timeInForce": "GTC",  
        "type": "LIMIT",  
        "side": "BUY",  
        "selfTradePreventionMode": "NONE"  
      },  
      {  
        "orderListId": 1929,  
        "contingencyType": "OCO",  
        "listStatusType": "ALL_DONE",  
        "listOrderStatus": "ALL_DONE",  
        "listClientOrderId": "2inzWQdDvZLHbbAmAozX2N",  
        "transactionTime": 1585230948299,  
        "symbol": "BTCUSDT",  
        "isIsolated": true,       // 是否是逐仓symbol交易   
        "orders": [  
          {  
            "symbol": "BTCUSDT",  
            "orderId": 20,  
            "clientOrderId": "CwOOIPHSmYywx6jZX77TdL"  
          },  
          {  
            "symbol": "BTCUSDT",  
            "orderId": 21,  
            "clientOrderId": "461cPg51vQjV3zIMOXNz39"  
          }  
        ],  
        "orderReports": [  
          {  
            "symbol": "BTCUSDT",  
            "origClientOrderId": "CwOOIPHSmYywx6jZX77TdL",  
            "orderId": 20,  
            "orderListId": 1929,  
            "clientOrderId": "pXLV6Hz6mprAcVYpVMTGgx",  
            "price": "0.668611",  
            "origQty": "0.690354",  
            "executedQty": "0.000000",  
            "cummulativeQuoteQty": "0.000000",  
            "status": "CANCELED",  
            "timeInForce": "GTC",  
            "type": "STOP_LOSS_LIMIT",  
            "side": "BUY",  
            "stopPrice": "0.378131",  
            "icebergQty": "0.017083"  
          },  
          {  
            "symbol": "BTCUSDT",  
            "origClientOrderId": "461cPg51vQjV3zIMOXNz39",  
            "orderId": 21,  
            "orderListId": 1929,  
            "clientOrderId": "pXLV6Hz6mprAcVYpVMTGgx",  
            "price": "0.008791",  
            "origQty": "0.690354",  
            "executedQty": "0.000000",  
            "cummulativeQuoteQty": "0.000000",  
            "status": "CANCELED",  
            "timeInForce": "GTC",  
            "type": "LIMIT_MAKER",  
            "side": "BUY",  
            "icebergQty": "0.639962"  
          }  
        ]  
      }  
    ]