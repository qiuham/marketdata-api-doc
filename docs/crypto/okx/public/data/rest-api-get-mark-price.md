---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#public-data-rest-api-get-mark-price
anchor_id: public-data-rest-api-get-mark-price
api_type: REST
updated_at: 2026-07-05 19:34:56.042789
---

# Get mark price

Retrieve mark price.  
  
We set the mark price based on the SPOT index and at a reasonable basis to prevent individual users from manipulating the market and causing the contract price to fluctuate.

#### Rate Limit: 10 requests per 2 seconds

#### Rate limit rule: IP + Instrument ID

#### HTTP Request

`GET /api/v5/public/mark-price`

> Request Example
    
    
    GET /api/v5/public/mark-price?instType=SWAP
    
    
    
    import okx.PublicData as PublicData
    
    flag = "0"  # Production trading: 0, Demo trading: 1
    
    publicDataAPI = PublicData.PublicAPI(flag=flag)
    
    # Retrieve mark price
    result = publicDataAPI.get_mark_price(
        instType="SWAP",
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instType | String | Yes | Instrument type  
`MARGIN`  
`SWAP`  
`FUTURES`  
`OPTION`  
`EVENTS`  
instFamily | String | No | Instrument family  
Applicable to `FUTURES`/`SWAP`/`OPTION`  
instId | String | No | Instrument ID, e.g. `BTC-USD-SWAP`  
  
> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
        {
            "instType":"SWAP",
            "instId":"BTC-USDT-SWAP",
            "markPx":"200",
            "ts":"1597026383085"
        }
      ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
instType | String | Instrument type  
`MARGIN`  
`SWAP`  
`FUTURES`  
`OPTION`  
`EVENTS`  
instId | String | Instrument ID, e.g. `BTC-USD-200214`  
markPx | String | Mark price  
ts | String | Data return time, Unix timestamp format in milliseconds, e.g. `1597026383085`

---

# 获取标记价格

为了防止个别用户恶意操控市场导致合约价格波动剧烈，我们根据现货指数和合理基差设定标记价格。  
  
#### 限速：10次/2s

#### 限速规则：IP + Instrument ID

#### HTTP请求

`GET /api/v5/public/mark-price`

> 请求示例
    
    
    GET /api/v5/public/mark-price?instType=SWAP
    
    
    
    import okx.PublicData as PublicData
    
    flag = "0"  # 实盘:0 , 模拟盘：1
    
    publicDataAPI = PublicData.PublicAPI(flag=flag)
    
    # 获取标记价格
    result = publicDataAPI.get_mark_price(
        instType="SWAP",
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instType | String | 是 | 产品类型  
`MARGIN`：币币杠杆  
`SWAP`：永续合约  
`FUTURES`：交割合约  
`OPTION`：期权  
`EVENTS`：事件合约  
instFamily | String | 否 | 交易品种  
适用于`交割`/`永续`/`期权`  
instId | String | 否 | 产品ID，如 `BTC-USD-SWAP`  
  
> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
        {
            "instType":"SWAP",
            "instId":"BTC-USDT-SWAP",
            "markPx":"200",
            "ts":"1597026383085"
        }
      ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
instType | String | 产品类型  
`MARGIN`：币币杠杆  
`SWAP`：永续合约  
`FUTURES`：交割合约  
`OPTION`：期权  
`EVENTS`：事件合约  
instId | String | 产品ID，如 `BTC-USD-200214`  
markPx | String | 标记价格  
ts | String | 接口数据返回时间，Unix时间戳的毫秒数格式，如`1597026383085`