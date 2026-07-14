---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#public-data-rest-api-get-limit-price
anchor_id: public-data-rest-api-get-limit-price
api_type: REST
updated_at: 2026-07-14 19:20:21.384486
---

# Get limit price

Retrieve the highest buy limit and lowest sell limit of the instrument.  
  
#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/public/price-limit`

> Request Example
    
    
    GET /api/v5/public/price-limit?instId=BTC-USDT-SWAP
    
    
    
    import okx.PublicData as PublicData
    
    flag = "0"  # Production trading: 0, Demo trading: 1
    
    publicDataAPI = PublicData.PublicAPI(flag=flag)
    
    # Retrieve the highest buy limit and lowest sell limit of the instrument
    result = publicDataAPI.get_price_limit(
        instId="BTC-USD-SWAP",
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instId | String | Yes | Instrument ID, e.g. `BTC-USDT-SWAP`  
  
> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
        {
            "instType":"SWAP",
            "instId":"BTC-USDT-SWAP",
            "buyLmt":"17057.9",
            "sellLmt":"16388.9",
            "ts":"1597026383085",
            "enabled": true
        }
      ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
instType | String | Instrument type  
instId | String | Instrument ID, e.g. `BTC-USDT-SWAP`  
buyLmt | String | Highest buy limit   
Return "" when enabled is false  
sellLmt | String | Lowest sell limit   
Return "" when enabled is false  
ts | String | Data return time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
enabled | Boolean | Whether price limit is effective   
`true`: the price limit is effective   
`false`: the price limit is not effective

---

# 获取限价

查询单个交易产品的最高买价和最低卖价  
  
#### 限速：20次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/public/price-limit`

> 请求示例
    
    
    GET /api/v5/public/price-limit?instId=BTC-USDT-SWAP
    
    
    
    import okx.PublicData as PublicData
    
    flag = "0"  # 实盘:0 , 模拟盘：1
    
    publicDataAPI = PublicData.PublicAPI(flag=flag)
    
    # 获取限价
    result = publicDataAPI.get_price_limit(
        instId="BTC-USD-SWAP",
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instId | String | 是 | 产品ID，如 `BTC-USDT-SWAP`  
  
> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
        {
            "instType":"SWAP",
            "instId":"BTC-USDT-SWAP",
            "buyLmt":"17057.9",
            "sellLmt":"16388.9",
            "ts":"1597026383085",
            "enabled": true
        }
      ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
instType | String | 产品类型  
`SPOT`：币币  
`MARGIN`：杠杆  
`SWAP`：永续合约  
`FUTURES`：交割合约  
`OPTION`：期权   
若产品ID支持杠杆交易，则返回`MARGIN`；否则，返回`SPOT`。  
instId | String | 产品ID ，如 `BTC-USDT-SWAP`  
buyLmt | String | 最高买价   
当enabled为false时，返回""  
sellLmt | String | 最低卖价   
当enabled为false时，返回""  
ts | String | 限价数据更新时间 ，Unix时间戳的毫秒数格式，如 `1597026383085`  
enabled | Boolean | 限价是否生效   
`true`：限价生效   
`false`：限价不生效