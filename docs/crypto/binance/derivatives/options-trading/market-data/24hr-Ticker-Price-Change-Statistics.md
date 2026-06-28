---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/options-trading/market-data/24hr-Ticker-Price-Change-Statistics
api_type: Market Data
updated_at: 2026-01-15T23:41:03.029712
---

# 24hr Ticker Price Change Statistics

## API Description[​](/docs/derivatives/options-trading/market-data/24hr-Ticker-Price-Change-Statistics#api-description "Direct link to API Description")

24 hour rolling window price change statistics.

## HTTP Request[​](/docs/derivatives/options-trading/market-data/24hr-Ticker-Price-Change-Statistics#http-request "Direct link to HTTP Request")

GET `/eapi/v1/ticker`

## Request Weight[​](/docs/derivatives/options-trading/market-data/24hr-Ticker-Price-Change-Statistics#request-weight "Direct link to Request Weight")

**5**

## Request Parameters[​](/docs/derivatives/options-trading/market-data/24hr-Ticker-Price-Change-Statistics#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| NO| Option trading pair, e.g BTC-200730-9000-C  
  
## Response Example[​](/docs/derivatives/options-trading/market-data/24hr-Ticker-Price-Change-Statistics#response-example "Direct link to Response Example")
    
    
    [  
      {  
        "symbol": "BTC-200730-9000-C",  
        "priceChange": "-16.2038",        //24-hour price change  
        "priceChangePercent": "-0.0162",  //24-hour percent price change  
        "lastPrice": "1000",              //Last trade price  
        "lastQty": "1000",                //Last trade amount  
        "open": "1016.2038",              //24-hour open price  
        "high": "1016.2038",              //24-hour high  
        "low": "0",                       //24-hour low  
        "volume": "5",                    //Trading volume(contracts)  
        "amount": "1",                    //Trade amount(in quote asset)  
        "bidPrice":"999.34",              //The best buy price  
        "askPrice":"1000.23",             //The best sell price  
        "openTime": 1592317127349,        //Time the first trade occurred within the last 24 hours  
        "closeTime": 1592380593516,       //Time the last trade occurred within the last 24 hours       
        "firstTradeId": 1,                //First trade ID  
        "tradeCount": 5,                  //Number of trades  
        "strikePrice": "9000",            //Strike price  
        "exercisePrice": "3000.3356"      //return estimated settlement price one hour before exercise, return index price at other times  
      }  
    ]

---

# 24hr价格变动情况

## 接口描述[​](/docs/zh-CN/derivatives/options-trading/market-data/24hr-Ticker-Price-Change-Statistics#接口描述 "接口描述的直接链接")

24小时期权价格变动

## HTTP请求[​](/docs/zh-CN/derivatives/options-trading/market-data/24hr-Ticker-Price-Change-Statistics#http请求 "HTTP请求的直接链接")

GET `/eapi/v1/ticker`

## 请求权重[​](/docs/zh-CN/derivatives/options-trading/market-data/24hr-Ticker-Price-Change-Statistics#请求权重 "请求权重的直接链接")

**5**

## 请求参数[​](/docs/zh-CN/derivatives/options-trading/market-data/24hr-Ticker-Price-Change-Statistics#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| NO| 交易对  
  
>   * 不发送交易对参数，则会返回所有交易对信息
> 


## 响应示例[​](/docs/zh-CN/derivatives/options-trading/market-data/24hr-Ticker-Price-Change-Statistics#响应示例 "响应示例的直接链接")
    
    
    [  
      {  
        "symbol": "BTC-200730-9000-C",  
        "priceChange": "-16.2038",        //24小时价格变动  
        "priceChangePercent": "-0.0162",  //24小时价格变动百分比  
        "lastPrice": "1000",              //最近一次成交价  
        "lastQty": "1000",                //最近一次成交额  
        "open": "1016.2038",              //24小时内第一次成交的价格  
        "high": "1016.2038",              //24小时最高价  
        "low": "0",                       //24小时最低价  
        "volume": "5",                    //成交额  
        "amount": "1",                    //成交量  
        "bidPrice":"999.34",              //最优买价  
        "askPrice":"1000.23",             //最优卖价  
        "openTime": 1592317127349,        //24小时内，第一笔交易的发生时间  
        "closeTime": 1592380593516,       //24小时内，最后一笔交易的发生时间  
        "firstTradeId": 1,                //首笔成交ID  
        "tradeCount": 5,                  //成交笔数  
        "strikePrice": "9000",            //行权价  
        "exercisePrice": "3000.3356"      //行权前半小时返回预估结算价，其他时刻返回指数价格  
      }  
    ]