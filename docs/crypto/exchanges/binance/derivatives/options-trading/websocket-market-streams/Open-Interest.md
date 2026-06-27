---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/options-trading/websocket-market-streams/Open-Interest
api_type: WebSocket
updated_at: 2026-01-15T23:43:52.944081
---

# Open Interest

## Stream Description[​](/docs/derivatives/options-trading/websocket-market-streams/Open-Interest#stream-description "Direct link to Stream Description")

Option open interest for specific underlying asset on specific expiration date. E.g.[ethusdt@openInterest@221125](wss://fstream.binance.com/market/stream?streams=ethusdt@openInterest@221125)

## URL PATH[​](/docs/derivatives/options-trading/websocket-market-streams/Open-Interest#url-path "Direct link to URL PATH")

`/market`

## Stream Name[​](/docs/derivatives/options-trading/websocket-market-streams/Open-Interest#stream-name "Direct link to Stream Name")

`underlying@optionOpenInterest@<expirationDate>`

## Update Speed[​](/docs/derivatives/options-trading/websocket-market-streams/Open-Interest#update-speed "Direct link to Update Speed")

**60s**

## Response Example[​](/docs/derivatives/options-trading/websocket-market-streams/Open-Interest#response-example "Direct link to Response Example")
    
    
    [  
        {  
          "e":"openInterest",         // Event type  
          "E":1668759300045,          // Event time  
          "s":"ETH-221125-2700-C",    // option symbol  
          "o":"1580.87",              // Open interest in contracts  
          "h":"1912992.178168204"     // Open interest in USDT  
        }  
    ]

---

# Open Interest

## Stream Description[​](/docs/zh-CN/derivatives/options-trading/websocket-market-streams/Open-Interest#stream-description "Stream Description的直接链接")

Option open interest for specific underlying asset on specific expiration date. E.g.[ethusdt@openInterest@221125](wss://fstream.binance.com/market/stream?streams=ethusdt@openInterest@221125)

## URL PATH[​](/docs/zh-CN/derivatives/options-trading/websocket-market-streams/Open-Interest#url-path "URL PATH的直接链接")

`/market`

## Stream Name[​](/docs/zh-CN/derivatives/options-trading/websocket-market-streams/Open-Interest#stream-name "Stream Name的直接链接")

`underlying@optionOpenInterest@<expirationDate>`

## Update Speed[​](/docs/zh-CN/derivatives/options-trading/websocket-market-streams/Open-Interest#update-speed "Update Speed的直接链接")

**60s**

## Response Example[​](/docs/zh-CN/derivatives/options-trading/websocket-market-streams/Open-Interest#response-example "Response Example的直接链接")
    
    
    [  
        {  
          "e":"openInterest",         // Event type  
          "E":1668759300045,          // Event time  
          "s":"ETH-221125-2700-C",    // option symbol  
          "o":"1580.87",              // Open interest in contracts  
          "h":"1912992.178168204"     // Open interest in USDT  
        }  
    ]