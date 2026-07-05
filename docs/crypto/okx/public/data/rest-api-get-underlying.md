---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#public-data-rest-api-get-underlying
anchor_id: public-data-rest-api-get-underlying
api_type: REST
updated_at: 2026-07-05 19:34:56.981609
---

# Get underlying

#### Rate Limit: 20 requests per 2 seconds  
  
#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/public/underlying`

> Request Example
    
    
    GET /api/v5/public/underlying?instType=FUTURES
    
    
    
    import okx.PublicData as PublicData
    
    flag = "0"  # Production trading: 0, Demo trading: 1
    
    publicDataAPI = PublicData.PublicAPI(flag=flag)
    
    # Get underlying
    result = publicDataAPI.get_underlying(
        instType="FUTURES"
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instType | String | Yes | Instrument type  
`SWAP`  
`FUTURES`  
`OPTION`  
  
> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            [
                "LTC-USDT",
                "BTC-USDT",
                "ETC-USDT"
            ]
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
uly | Array | Underlying

---

# 获取衍生品标的指数

#### 限速：20次/2s  
  
#### 限速规则：IP

#### HTTP请求

`GET /api/v5/public/underlying`

> 请求示例
    
    
    GET /api/v5/public/underlying?instType=FUTURES
    
    
    
    import okx.PublicData as PublicData
    
    flag = "0"  # 实盘:0 , 模拟盘：1
    
    publicDataAPI = PublicData.PublicAPI(flag=flag)
    
    # 获取衍生品标的指数
    result = publicDataAPI.get_underlying(
        instType="FUTURES"
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instType | String | 是 | 产品类型  
`SWAP`：永续合约  
`FUTURES`：交割合约  
`OPTION`：期权  
  
> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            [
                "LTC-USDT",
                "BTC-USDT",
                "ETC-USDT"
            ]
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
uly | Array of strings | 标的指数 如：BTC-USDT