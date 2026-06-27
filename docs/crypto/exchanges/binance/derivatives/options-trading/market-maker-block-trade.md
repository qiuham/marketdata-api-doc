---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/options-trading/market-maker-block-trade
api_type: Market Data
updated_at: 2026-01-15T23:41:27.297402
---

# New Block Trade Order (TRADE)

## API Description[​](/docs/derivatives/options-trading/market-maker-block-trade#api-description "Direct link to API Description")

Send in a new block trade order.

## HTTP Request[​](/docs/derivatives/options-trading/market-maker-block-trade#http-request "Direct link to HTTP Request")

POST `eapi/v1/block/order/create`

## Request Weight[​](/docs/derivatives/options-trading/market-maker-block-trade#request-weight "Direct link to Request Weight")

**5**

## Request Parameters[​](/docs/derivatives/options-trading/market-maker-block-trade#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
liquidity| STRING| YES| Taker or Maker  
legs| LIST| YES| Max 1 (only single leg supported), list of legs parameters in JSON; example: eapi/v1/block/order/create?orders=[{"symbol":"BTC-210115-35000-C", "price":"100","quantity":"0.0002","side":"BUY","type":"LIMIT"}]  
recvWindow| INT| NO| The value cannot be greater than 60000  
timestamp| INT| YES|   
  
## Response Example[​](/docs/derivatives/options-trading/market-maker-block-trade#response-example "Direct link to Response Example")
    
    
    {  
        "blockTradeSettlementKey": "3668822b8-1baa-6a2f-adb8-d3de6289b361",  
        "expireTime": 1730171888109,  
        "liquidity": "TAKER",  
        "status": "RECEIVED",  
        "legs": [  
            {  
                "symbol": "BNB-241101-700-C",  
                "side": "BUY",  
                "quantity": "1.2",  
                "price": "2.8"  
            }  
        ]  
    }

---

# New Block Trade Order (TRADE)

## API Description[​](/docs/zh-CN/derivatives/options-trading/market-maker-block-trade#api-description "API Description的直接链接")

Send in a new block trade order.

## HTTP Request[​](/docs/zh-CN/derivatives/options-trading/market-maker-block-trade#http-request "HTTP Request的直接链接")

POST `eapi/v1/block/order/create`

## Request Weight[​](/docs/zh-CN/derivatives/options-trading/market-maker-block-trade#request-weight "Request Weight的直接链接")

**5**

## Request Parameters[​](/docs/zh-CN/derivatives/options-trading/market-maker-block-trade#request-parameters "Request Parameters的直接链接")

Name| Type| Mandatory| Description  
---|---|---|---  
liquidity| STRING| YES| Taker or Maker  
legs| LIST| YES| Max 1 (only single leg supported), list of legs parameters in JSON; example: eapi/v1/block/order/create?orders=[{"symbol":"BTC-210115-35000-C", "price":"100","quantity":"0.0002","side":"BUY","type":"LIMIT"}]  
recvWindow| INT| NO| The value cannot be greater than 60000  
timestamp| INT| YES|   
  
## Response Example[​](/docs/zh-CN/derivatives/options-trading/market-maker-block-trade#response-example "Response Example的直接链接")
    
    
    {  
        "blockTradeSettlementKey": "3668822b8-1baa-6a2f-adb8-d3de6289b361",  
        "expireTime": 1730171888109,  
        "liquidity": "TAKER",  
        "status": "RECEIVED",  
        "legs": [  
            {  
                "symbol": "BNB-241101-700-C",  
                "side": "BUY",  
                "quantity": "1.2",  
                "price": "2.8"  
            }  
        ]  
    }