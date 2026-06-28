---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/options-trading/market-maker-block-trade/Account-Block-Trade-List
api_type: Market Data
updated_at: 2026-01-15T23:41:27.954952
---

# Account Block Trade List (USER_DATA)

## API Description[​](/docs/derivatives/options-trading/market-maker-block-trade/Account-Block-Trade-List#api-description "Direct link to API Description")

Gets block trades for a specific account.

## HTTP Request[​](/docs/derivatives/options-trading/market-maker-block-trade/Account-Block-Trade-List#http-request "Direct link to HTTP Request")

GET `/eapi/v1/block/user-trades`

## Request Weight[​](/docs/derivatives/options-trading/market-maker-block-trade/Account-Block-Trade-List#request-weight "Direct link to Request Weight")

**5**

## Request Parameters[​](/docs/derivatives/options-trading/market-maker-block-trade/Account-Block-Trade-List#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory|  Description  
---|---|---|---  
endTime| LONG| NO|   
startTime| LONG| NO|   
underlying| STRING| NO|   
recvWindow| LONG| NO| The value cannot be greater than 60000  
timestamp| LONG| YES|   
  
## Response Example[​](/docs/derivatives/options-trading/market-maker-block-trade/Account-Block-Trade-List#response-example "Direct link to Response Example")
    
    
    [  
        {  
            "parentOrderId": "4675011431944499201",  
            "crossType": "USER_BLOCK",  
            "legs": [  
                {  
                    "createTime": 1730170445600,  
                    "updateTime": 1730170445600,  
                    "symbol": "BNB-241101-700-C",  
                    "orderId": "4675011431944499203",  
                    "orderPrice": 2.8,  
                    "orderQuantity": 1.2,  
                    "orderStatus": "FILLED",  
                    "executedQty": 1.2,  
                    "executedAmount": 3.36,  
                    "fee": 0.336,  
                    "orderType": "PREV_QUOTED",  
                    "orderSide": "BUY",  
                    "id": "1125899906900937837",  
                    "tradeId": 1,  
                    "tradePrice": 2.8,  
                    "tradeQty": 1.2,  
                    "tradeTime": 1730170445600,  
                    "liquidity": "TAKER",  
                    "commission": 0.336  
                }  
            ],  
            "blockTradeSettlementKey": "7d085e6e-a229-2335-ab9d-6a581febcd25"  
        }  
    ]

---

# Account Block Trade List (USER_DATA)

## API Description[​](/docs/zh-CN/derivatives/options-trading/market-maker-block-trade/Account-Block-Trade-List#api-description "API Description的直接链接")

Gets block trades for a specific account.

## HTTP Request[​](/docs/zh-CN/derivatives/options-trading/market-maker-block-trade/Account-Block-Trade-List#http-request "HTTP Request的直接链接")

GET `/eapi/v1/block/user-trades`

## Request Weight[​](/docs/zh-CN/derivatives/options-trading/market-maker-block-trade/Account-Block-Trade-List#request-weight "Request Weight的直接链接")

**5**

## Request Parameters[​](/docs/zh-CN/derivatives/options-trading/market-maker-block-trade/Account-Block-Trade-List#request-parameters "Request Parameters的直接链接")

Name| Type| Mandatory|  Description  
---|---|---|---  
endTime| LONG| NO|   
startTime| LONG| NO|   
underlying| STRING| NO|   
recvWindow| LONG| NO| The value cannot be greater than 60000  
timestamp| LONG| YES|   
  
## Response Example[​](/docs/zh-CN/derivatives/options-trading/market-maker-block-trade/Account-Block-Trade-List#response-example "Response Example的直接链接")
    
    
    [  
        {  
            "parentOrderId": "4675011431944499201",  
            "crossType": "USER_BLOCK",  
            "legs": [  
                {  
                    "createTime": 1730170445600,  
                    "updateTime": 1730170445600,  
                    "symbol": "BNB-241101-700-C",  
                    "orderId": "4675011431944499203",  
                    "orderPrice": 2.8,  
                    "orderQuantity": 1.2,  
                    "orderStatus": "FILLED",  
                    "executedQty": 1.2,  
                    "executedAmount": 3.36,  
                    "fee": 0.336,  
                    "orderType": "PREV_QUOTED",  
                    "orderSide": "BUY",  
                    "id": "1125899906900937837",  
                    "tradeId": 1,  
                    "tradePrice": 2.8,  
                    "tradeQty": 1.2,  
                    "tradeTime": 1730170445600,  
                    "liquidity": "TAKER",  
                    "commission": 0.336  
                }  
            ],  
            "blockTradeSettlementKey": "7d085e6e-a229-2335-ab9d-6a581febcd25"  
        }  
    ]