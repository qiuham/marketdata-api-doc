---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/options-trading/market-data/Kline-Candlestick-Data
api_type: Market Data
updated_at: 2026-01-15T23:41:03.231641
---

# Kline/Candlestick Data

## API Description[​](/docs/derivatives/options-trading/market-data/Kline-Candlestick-Data#api-description "Direct link to API Description")

Kline/candlestick bars for an option symbol. Klines are uniquely identified by their open time.

## HTTP Request[​](/docs/derivatives/options-trading/market-data/Kline-Candlestick-Data#http-request "Direct link to HTTP Request")

GET `/eapi/v1/klines`

## Request Weight[​](/docs/derivatives/options-trading/market-data/Kline-Candlestick-Data#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/options-trading/market-data/Kline-Candlestick-Data#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES| Option trading pair, e.g BTC-200730-9000-C  
interval| STRING| YES| Time interval  
startTime| LONG| NO| Start Time 1592317127349  
endTime| LONG| NO| End Time  
limit| INT| NO| Number of records Default:500 Max:1500  
  
>   * If startTime and endTime are not sent, the most recent klines are returned.
> 


## Response Example[​](/docs/derivatives/options-trading/market-data/Kline-Candlestick-Data#response-example "Direct link to Response Example")
    
    
    [  
        [  
            1762779600000,  // Open time  
            "1300.000",     // Open  
            "1300.000",     // High  
            "1300.000",     // Low  
            "1300.000",     // Close  
            "0.1000",       // Volume  
            1762780499999,  // Close time  
            "130.0000000",  // Quote asset volume  
            1,              // Number of trades  
            "0.1000",       // Taker buy base asset volume  
            "130.0000000",  // Taker buy quote asset volume  
            "0"             // Ignore.  
        ],  
    ]

---

# K线数据

## 接口描述[​](/docs/zh-CN/derivatives/options-trading/market-data/Kline-Candlestick-Data#接口描述 "接口描述的直接链接")

K线数据，每根K线的开盘时间可视为唯一ID

## HTTP请求[​](/docs/zh-CN/derivatives/options-trading/market-data/Kline-Candlestick-Data#http请求 "HTTP请求的直接链接")

GET `/eapi/v1/klines`

## 请求权重[​](/docs/zh-CN/derivatives/options-trading/market-data/Kline-Candlestick-Data#请求��权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/options-trading/market-data/Kline-Candlestick-Data#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES| 交易对  
interval| ENUM| YES| 时间间隔  
startTime| LONG| NO| 起始时间  
endTime| LONG| NO| 结束时间  
limit| INT| NO| 默认值:500 最大值:1500.  
  
>   * 缺省返回最近的数据
> 


## 响应示例[​](/docs/zh-CN/derivatives/options-trading/market-data/Kline-Candlestick-Data#响应示例 "响应示例的直接链接")
    
    
    [  
        [  
            1762779600000,  // 开盘时间  
            "1300.000",     // 开盘价  
            "1300.000",     // 最高价  
            "1300.000",     // 最低价  
            "1300.000",     // 收盘价(当前K线未结束的即为最新价)  
            "0.1000",       // 成交量  
            1762780499999,  // 收盘时间  
            "130.0000000",  // 成交额  
            1,              // 成交笔数  
            "0.1000",       // 主动买入成交量  
            "130.0000000",  // 主动买入成交额  
            "0"             // 请忽略该参数  
        ],  
    ]