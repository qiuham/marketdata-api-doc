---
exchange: binance
source_url: https://developers.binance.com/docs/margin_trading/trade/Exit-Special-Key-Mode
api_type: Trading
updated_at: 2026-05-27 18:57:23.505098
---

# Get Small Liability Exchange Coin List (USER_DATA)

## API Description[​](/docs/margin_trading/trade/Get-Small-Liability-Exchange-Coin-List#api-description "Direct link to API Description")

Query the coins which can be small liability exchange

## HTTP Request[​](/docs/margin_trading/trade/Get-Small-Liability-Exchange-Coin-List#http-request "Direct link to HTTP Request")

GET `/sapi/v1/margin/exchange-small-liability`

## Request Weight(IP)[​](/docs/margin_trading/trade/Get-Small-Liability-Exchange-Coin-List#request-weightip "Direct link to Request Weight\(IP\)")

**100**

## Request Parameters[​](/docs/margin_trading/trade/Get-Small-Liability-Exchange-Coin-List#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/margin_trading/trade/Get-Small-Liability-Exchange-Coin-List#response-example "Direct link to Response Example")
    
    
    [  
        {  
          "asset": "ETH",  
          "interest": "0.00083334",  
          "principal": "0.001",  
          "liabilityAsset": "USDT",  
          "liabilityQty": 0.3552  
        }  
    ]

---

# 查询可小额负债转换的资产 (USER_DATA)

## 接口描述[​](/docs/zh-CN/margin_trading/trade/Get-Small-Liability-Exchange-Coin-List#接口描述 "接口描述的直接链接")

查询可小额负债转换的币种

## HTTP请求[​](/docs/zh-CN/margin_trading/trade/Get-Small-Liability-Exchange-Coin-List#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/margin/exchange-small-liability`

## 请求权重(IP)[​](/docs/zh-CN/margin_trading/trade/Get-Small-Liability-Exchange-Coin-List#请求权重ip "请求权重\(IP\)的直接链接")

**100**

## 请求参数[​](/docs/zh-CN/margin_trading/trade/Get-Small-Liability-Exchange-Coin-List#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/margin_trading/trade/Get-Small-Liability-Exchange-Coin-List#响应示例 "响应示例的直接链接")
    
    
    [  
        {  
          "asset": "ETH",  
          "interest": "0.00083334",  
          "principal": "0.001",  
          "liabilityAsset": "USDT",  
          "liabilityQty": 0.3552  
        }  
    ]