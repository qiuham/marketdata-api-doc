---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-grid-trading-get-rsi-back-testing-public
anchor_id: order-book-trading-grid-trading-get-rsi-back-testing-public
api_type: API
updated_at: 2026-07-04 19:37:49.463539
---

# GET / RSI back testing (public)

Authentication is not required for this public endpoint.  
  
#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: IP

#### Permission: Read

#### HTTP Request

`GET /api/v5/tradingBot/public/rsi-back-testing`

> Request Example
    
    
    GET /api/v5/tradingBot/public/rsi-back-testing?instId=BTC-USDT&thold=30&timeframe=3m&timePeriod=14
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instId | String | Yes | Instrument ID, e.g. `BTC-USDT`  
Only applicable to `SPOT`  
timeframe | String | Yes | K-line type  
`3m`, `5m`, `15m`, `30m` (`m`: minute)  
`1H`, `4H` (`H`: hour)  
`1D` (`D`: day)  
thold | String | Yes | Threshold  
The value should be an integer between 1 to 100  
timePeriod | String | Yes | Time Period  
`14`  
triggerCond | String | No | Trigger condition  
`cross_up`  
`cross_down`  
`above`  
`below`  
`cross`  
Default is `cross_down`  
duration | String | No | Back testing duration  
`1M` (`M`: month)  
Default is `1M`  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "triggerNum": "164"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
triggerNum | String | Trigger number

---

# GET / RSI回测（公共）

公共接口无须鉴权  
  
#### 限速：20次/2s

#### 限速规则：IP

#### 权限：读取

#### HTTP请求

`GET /api/v5/tradingBot/public/rsi-back-testing`

> 请求示例
    
    
    GET /api/v5/tradingBot/public/rsi-back-testing?instId=BTC-USDT&thold=30&timeframe=3m&timePeriod=14
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instId | String | 是 | 产品ID，如`BTC-USDT`  
适用于`币币`  
timeframe | String | 是 | K线种类  
`3m`, `5m`, `15m`, `30m` (`m`代表分钟)  
`1H`, `4H` (`H`代表小时)  
`1D` (`D`代表天)  
thold | String | 是 | 阈值  
取值[1,100]的整数  
timePeriod | String | 是 | 周期  
`14`  
triggerCond | String | 否 | 触发条件  
`cross_up`：上穿  
`cross_down`：下穿  
`above`：上方  
`below`：下方  
`cross`：交叉  
默认是`cross_down`  
duration | String | 否 | 回测周期  
`1M`：1个月  
默认`1M`  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "triggerNum": "164"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
triggerNum | String | 触发次数