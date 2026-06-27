---
exchange: binance
source_url: https://developers.binance.com/docs/margin_trading/trade/Create-Special-Key-of-Low-Latency-Trading
api_type: Trading
updated_at: 2026-05-27 18:57:18.616490
---

# Delete Special Key(Low-Latency Trading)(TRADE)

## API Description[​](/docs/margin_trading/trade/Delete-Special-Key-of-Low-Latency-Trading#api-description "Direct link to API Description")

This only applies to Special Key for Low Latency Trading.

If apiKey is given, apiName will be ignored. If apiName is given with no apiKey, all apikeys with given apiName will be deleted.

You need to enable Permits “Enable Spot & Margin Trading” option for the API Key which requests this endpoint.

## HTTP Request[​](/docs/margin_trading/trade/Delete-Special-Key-of-Low-Latency-Trading#http-request "Direct link to HTTP Request")

DELETE `/sapi/v1/margin/apiKey`

## Request Weight[​](/docs/margin_trading/trade/Delete-Special-Key-of-Low-Latency-Trading#request-weight "Direct link to Request Weight")

**1(UID)**

## Request Parameters[​](/docs/margin_trading/trade/Delete-Special-Key-of-Low-Latency-Trading#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
apiKey| STRING| NO|   
apiName| STRING| NO|   
symbol| STRING| NO| isolated margin pair  
recvWindow| LONG| NO| The value cannot be greater than `60000`  
timestamp| LONG| YES|   
  
## Response Example[​](/docs/margin_trading/trade/Delete-Special-Key-of-Low-Latency-Trading#response-example "Direct link to Response Example")
    
    
    {  
    }

---

# Delete Special Key(Low-Latency Trading)(TRADE)

## API Description[​](/docs/zh-CN/margin_trading/trade/Delete-Special-Key-of-Low-Latency-Trading#api-description "API Description的直接链接")

This only applies to Special Key for Low Latency Trading.

If apiKey is given, apiName will be ignored. If apiName is given with no apiKey, all apikeys with given apiName will be deleted.

You need to enable Permits “Enable Spot & Margin Trading” option for the API Key which requests this endpoint.

## HTTP Request[​](/docs/zh-CN/margin_trading/trade/Delete-Special-Key-of-Low-Latency-Trading#http-request "HTTP Request的直接链接")

DELETE `/sapi/v1/margin/apiKey`

## Request Weight[​](/docs/zh-CN/margin_trading/trade/Delete-Special-Key-of-Low-Latency-Trading#request-weight "Request Weight的直接链接")

**1(UID)**

## Request Parameters[​](/docs/zh-CN/margin_trading/trade/Delete-Special-Key-of-Low-Latency-Trading#request-parameters "Request Parameters的直接链接")

Name| Type| Mandatory| Description  
---|---|---|---  
apiKey| STRING| NO|   
apiName| STRING| NO|   
symbol| STRING| NO| isolated margin pair  
recvWindow| LONG| NO| The value cannot be greater than `60000`  
timestamp| LONG| YES|   
  
## Response Example[​](/docs/zh-CN/margin_trading/trade/Delete-Special-Key-of-Low-Latency-Trading#response-example "Response Example的直接链接")
    
    
    {  
    }