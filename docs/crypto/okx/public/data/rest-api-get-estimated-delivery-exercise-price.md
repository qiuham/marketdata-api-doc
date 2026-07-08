---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#public-data-rest-api-get-estimated-delivery-exercise-price
anchor_id: public-data-rest-api-get-estimated-delivery-exercise-price
api_type: REST
updated_at: 2026-07-08 19:28:43.113718
---

# Get estimated delivery/exercise price

Retrieve the estimated delivery price which will only have a return value one hour before the delivery/exercise.  
  
#### Rate Limit: 10 requests per 2 seconds

#### Rate limit rule: IP + Instrument ID

#### HTTP Request

`GET /api/v5/public/estimated-price`

> Request Example
    
    
    GET /api/v5/public/estimated-price?instId=BTC-USD-200214
    
    
    
    import okx.PublicData as PublicData
    
    flag = "0"  # Production trading: 0, Demo trading: 1
    
    publicDataAPI = PublicData.PublicAPI(flag=flag)
    
    # Retrieve estimated delivery/exercise price
    result = publicDataAPI.get_estimated_price(
        instId = "BTC-USD-200214",
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instId | String | Yes | Instrument ID, e.g. `BTC-USD-200214`   
only applicable to `FUTURES`/`OPTION`/`EVENTS`  
  
> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
        {
            "instType":"FUTURES",
            "instId":"BTC-USDT-201227",
            "settlePx":"200",
            "ts":"1597026383085"
        }
      ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
instType | String | Instrument type  
`FUTURES`  
`OPTION`  
instId | String | Instrument ID, e.g. `BTC-USD-200214`  
settlePx | String | Estimated delivery/exercise price  
ts | String | Data return time, Unix timestamp format in milliseconds, e.g. `1597026383085`

---

# 获取预估交割/行权价格

获取交割合约和期权预估交割/行权价。交割/行权预估价只有交割/行权前一小时才有返回值  
  
#### 限速：10次/2s

#### 限速规则：IP + Instrument ID

#### HTTP请求

`GET /api/v5/public/estimated-price`

> 请求示例
    
    
    GET /api/v5/public/estimated-price?instId=BTC-USD-200214
    
    
    
    import okx.PublicData as PublicData
    
    flag = "0"  # 实盘:0 , 模拟盘：1
    
    publicDataAPI = PublicData.PublicAPI(flag=flag)
    
    # 获取预估交割/行权价格
    result = publicDataAPI.get_estimated_price(
        instId="BTC-USD-200214",
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instId | String | 是 | 产品ID，如 `BTC-USD-200214`  
仅适用于`交割`/`期权`/`事件合约`  
  
> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
        {
            "instType":"FUTURES",
            "instId":"BTC-USDT-201227",
            "settlePx":"200",
            "ts":"1597026383085"
        }
      ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
instType | String | 产品类型  
`FUTURES`：交割合约  
`OPTION`：期权  
instId | String | 产品ID， 如 `BTC-USD-200214`  
settlePx | String | 预估交割/行权价格  
ts | String | 数据返回时间，Unix时间戳的毫秒数格式，如 `1597026383085`