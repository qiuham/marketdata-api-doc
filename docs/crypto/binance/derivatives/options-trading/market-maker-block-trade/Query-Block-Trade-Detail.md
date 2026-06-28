---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/options-trading/market-maker-block-trade/Query-Block-Trade-Detail
api_type: Market Data
updated_at: 2026-01-15T23:41:52.233508
---

# Query Block Trade Details (USER_DATA)

## API Description[​](/docs/derivatives/options-trading/market-maker-block-trade/Query-Block-Trade-Detail#api-description "Direct link to API Description")

Query block trade details; returns block trade details from counterparty's perspective.

## HTTP Request[​](/docs/derivatives/options-trading/market-maker-block-trade/Query-Block-Trade-Detail#http-request "Direct link to HTTP Request")

GET `/eapi/v1/block/order/execute`

## Request Weight[​](/docs/derivatives/options-trading/market-maker-block-trade/Query-Block-Trade-Detail#request-weight "Direct link to Request Weight")

**5**

## Request Parameters[​](/docs/derivatives/options-trading/market-maker-block-trade/Query-Block-Trade-Detail#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory|  Description  
---|---|---|---  
blockOrderMatchingKey| STRING| YES|   
recvWindow| LONG| NO| The value cannot be greater than 60000  
timestamp| LONG| YES|   
  
## Response Example[​](/docs/derivatives/options-trading/market-maker-block-trade/Query-Block-Trade-Detail#response-example "Direct link to Response Example")
    
    
    {  
        "blockTradeSettlementKey": "12b96c28-ba05-8906-c89t-703215cfb2e6",  
        "expireTime": 1730171860460,  
        "liquidity": "MAKER",  
        "status": "RECEIVED",  
        "createTime": 1730170060462,  
        "legs": [  
            {  
                "symbol": "BNB-241101-700-C",  
                "side": "SELL",  
                "quantity": "1.66",  
                "price": "20"  
            }  
        ]  
    }

---

# Query Block Trade Details (USER_DATA)

## API Description[​](/docs/zh-CN/derivatives/options-trading/market-maker-block-trade/Query-Block-Trade-Detail#api-description "API Description的直接链接")

Query block trade details; returns block trade details from counterparty's perspective.

## HTTP Request[​](/docs/zh-CN/derivatives/options-trading/market-maker-block-trade/Query-Block-Trade-Detail#http-request "HTTP Request的直接链接")

GET `/eapi/v1/block/order/execute`

## Request Weight[​](/docs/zh-CN/derivatives/options-trading/market-maker-block-trade/Query-Block-Trade-Detail#request-weight "Request Weight的直接链接")

**5**

## Request Parameters[​](/docs/zh-CN/derivatives/options-trading/market-maker-block-trade/Query-Block-Trade-Detail#request-parameters "Request Parameters的直接链接")

Name| Type| Mandatory|  Description  
---|---|---|---  
blockOrderMatchingKey| STRING| YES|   
recvWindow| LONG| NO| The value cannot be greater than 60000  
timestamp| LONG| YES|   
  
## Response Example[​](/docs/zh-CN/derivatives/options-trading/market-maker-block-trade/Query-Block-Trade-Detail#response-example "Response Example的直接链接")
    
    
    {  
        "blockTradeSettlementKey": "12b96c28-ba05-8906-c89t-703215cfb2e6",  
        "expireTime": 1730171860460,  
        "liquidity": "MAKER",  
        "status": "RECEIVED",  
        "createTime": 1730170060462,  
        "legs": [  
            {  
                "symbol": "BNB-241101-700-C",  
                "side": "SELL",  
                "quantity": "1.66",  
                "price": "20"  
            }  
        ]  
    }