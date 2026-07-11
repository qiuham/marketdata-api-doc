---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#funding-account-rest-api-get-convert-currency-pair
anchor_id: funding-account-rest-api-get-convert-currency-pair
api_type: REST
updated_at: 2026-07-11 19:14:15.790896
---

# Get convert currency pair

#### Rate Limit: 6 requests per second  
  
#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/asset/convert/currency-pair`

> Request Example
    
    
    GET /api/v5/asset/convert/currency-pair?fromCcy=USDT&toCcy=BTC
    
    

#### Response parameters

**Parameters** | **Types** | **Required** | **Description**  
---|---|---|---  
fromCcy | String | Yes | Currency to convert from, e.g. `USDT`  
toCcy | String | Yes | Currency to convert to, e.g. `BTC`  
convertMode | String | No | `0`: standard convert (default)   
`1`: large order convert for VIP  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "baseCcy": "BTC",
                "baseCcyMax": "0.5",
                "baseCcyMin": "0.0001",
                "instId": "BTC-USDT",
                "quoteCcy": "USDT",
                "quoteCcyMax": "10000",
                "quoteCcyMin": "1"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
instId | String | Currency pair, e.g. `BTC-USDT`  
baseCcy | String | Base currency, e.g. `BTC` in `BTC-USDT`  
baseCcyMax | String | Maximum amount of base currency  
baseCcyMin | String | Minimum amount of base currency  
quoteCcy | String | Quote currency, e.g. `USDT` in `BTC-USDT`  
quoteCcyMax | String | Maximum amount of quote currency  
quoteCcyMin | String | Minimum amount of quote currency

---

# 获取闪兑币对信息

#### 限速：6次/s  
  
#### 限速规则：User ID

#### 权限：读取

#### HTTP 请求

`GET /api/v5/asset/convert/currency-pair`

> 请求示例
    
    
    GET /api/v5/asset/convert/currency-pair?fromCcy=USDT&toCcy=BTC
    
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
fromCcy | String | 是 | 消耗币种，如 `USDT`  
toCcy | String | 是 | 获取币种，如 `BTC`  
convertMode | String | 否 | `0`：标准闪兑（默认）  
`1`：VIP大额闪兑  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "baseCcy": "BTC",
                "baseCcyMax": "0.5",
                "baseCcyMin": "0.0001",
                "instId": "BTC-USDT",
                "quoteCcy": "USDT",
                "quoteCcyMax": "10000",
                "quoteCcyMin": "1"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
instId | String | 币对，如 `BTC-USDT`  
baseCcy | String | 交易货币币种，如 `BTC-USDT`中的`BTC`  
baseCcyMax | String | 交易货币支持闪兑的最大值  
baseCcyMin | String | 交易货币支持闪兑的最小值  
quoteCcy | String | 计价货币币种，如 `BTC-USDT`中的`USDT`  
quoteCcyMax | String | 计价货币支持闪兑的最大值  
quoteCcyMin | String | 计价货币支持闪兑的最小值