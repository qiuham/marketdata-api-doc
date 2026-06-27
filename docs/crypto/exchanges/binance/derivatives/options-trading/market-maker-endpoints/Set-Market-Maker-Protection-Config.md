---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/options-trading/market-maker-endpoints/Set-Market-Maker-Protection-Config
api_type: Market Data
updated_at: 2026-01-15T23:42:11.428466
---

# Set Market Maker Protection Config (TRADE)

## API Description[​](/docs/derivatives/options-trading/market-maker-endpoints/Set-Market-Maker-Protection-Config#api-description "Direct link to API Description")

Set config for MMP. Market Maker Protection(MMP) is a set of protection mechanism for option market maker, this mechanism is able to prevent mass trading in short period time. Once market maker's account branches the threshold, the Market Maker Protection will be triggered. When Market Maker Protection triggers, all the current MMP orders will be canceled, new MMP orders will be rejected. Market maker can use this time to reevaluate market and modify order price.

## HTTP Request[​](/docs/derivatives/options-trading/market-maker-endpoints/Set-Market-Maker-Protection-Config#http-request "Direct link to HTTP Request")

POST `/eapi/v1/mmpSet`

## Request Weight[​](/docs/derivatives/options-trading/market-maker-endpoints/Set-Market-Maker-Protection-Config#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/options-trading/market-maker-endpoints/Set-Market-Maker-Protection-Config#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
underlying| STRING| TRUE| underlying, e.g BTCUSDT  
windowTimeInMilliseconds| LONG| TRUE| MMP Interval in milliseconds; Range (0,5000]  
frozenTimeInMilliseconds| LONG| TRUE| MMP frozen time in milliseconds, if set to 0 manual reset is required  
qtyLimit| DECIMAL| TRUE| quantity limit  
deltaLimit| DECIMAL| TRUE| net delta limit  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/derivatives/options-trading/market-maker-endpoints/Set-Market-Maker-Protection-Config#response-example "Direct link to Response Example")
    
    
    {  
        "underlyingId": 2,  
        "underlying": "BTCUSDT",  
        "windowTimeInMilliseconds": 3000,  
        "frozenTimeInMilliseconds": 300000,  
        "qtyLimit": "2",  
        "deltaLimit": "2.3",  
        "lastTriggerTime": 0  
      
    }

---

# 设置MMP规则

## 接口描述[​](/docs/zh-CN/derivatives/options-trading/market-maker-endpoints/Set-Market-Maker-Protection-Config#接口描述 "接口描述的直接链接")

设置MMP参数。 做市商保护(Market Maker Protection) 是一种为期权做市商设计的保护机制，该机制能够防止做市商的订单在短时间大量成交。一旦某个账户在短时间内的总交易额超过了配置的限额，该账户的做市商保护将被触发。当做市商保护被触发时，账户现有的做市商保护订单（被标记为做市商保护的订单）将被撮合自动取消，而该账户新的做市商保护订单将在冻结期被拒绝。用户可以利用这段时间重新评估行情并修改报价。

## HTTP请求[​](/docs/zh-CN/derivatives/options-trading/market-maker-endpoints/Set-Market-Maker-Protection-Config#http请求 "HTTP请求的直接链接")

POST `/eapi/v1/mmpSet`

## 请求权重[​](/docs/zh-CN/derivatives/options-trading/market-maker-endpoints/Set-Market-Maker-Protection-Config#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/options-trading/market-maker-endpoints/Set-Market-Maker-Protection-Config#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
underlying| STRING| YES| 标的资产如BTCUSDT  
windowTimeInMilliseconds| LONG| YES| MMP监控时间窗口（毫秒），在(0,5000]之间  
frozenTimeInMilliseconds| LONG| NO| MMP冻结时间（毫秒），设置为0后代表账号为冻结状态，需要手动重置  
qtyLimit| DECIMAL| NO| 数量限制  
deltaLimit| DECIMAL| NO| 净delta限制  
recvWindow| LONG| NO|   
timestamp| LONG| NO|   
  
## 响应示例[​](/docs/zh-CN/derivatives/options-trading/market-maker-endpoints/Set-Market-Maker-Protection-Config#响应示例 "响应示例的直接链接")
    
    
    {  
        "underlyingId": 2,  
        "underlying": "BTCUSDT",  
        "windowTimeInMilliseconds": 3000,  
        "frozenTimeInMilliseconds": 300000,  
        "qtyLimit": "2",  
        "deltaLimit": "2.3",  
        "lastTriggerTime": 0  
      
    }