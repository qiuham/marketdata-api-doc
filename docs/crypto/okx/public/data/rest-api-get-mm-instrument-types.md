---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#public-data-rest-api-get-mm-instrument-types
anchor_id: public-data-rest-api-get-mm-instrument-types
api_type: REST
updated_at: 2026-07-06 19:54:10.731019
---

# Get MM instrument types

Retrieve the list of MM Program instrument type classifications for SPOT and SWAP instruments.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/public/mm-instrument-types`

> Request Example
    
    
    GET /api/v5/public/mm-instrument-types?instType=SWAP
    
    
    
    import okx.PublicData as PublicData
    
    flag = "0"  # Production trading: 0, Demo trading: 1
    
    publicDataAPI = PublicData.PublicAPI(flag=flag)
    
    # Retrieve the list of MM Program instrument type classifications
    result = publicDataAPI.get_mm_instrument_types(
        instType="SWAP"
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instType | String | No | Instrument type.  
`SPOT`  
`SWAP`  
When not specified, returns all types.  
instId | String | No | Instrument ID, e.g. `BTC-USDT`, `BTC-USDT-SWAP`.  
When specified, returns at most one record.  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "instId": "BTC-USDT-SWAP",
                "instType": "SWAP",
                "pairType": "A"
            },
            {
                "instId": "ETH-USDT-SWAP",
                "instType": "SWAP",
                "pairType": "A"
            },
            {
                "instId": "XAU-USDT-SWAP",
                "instType": "SWAP",
                "pairType": "B-TradFi"
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
instId | String | Instrument ID, e.g. `BTC-USDT-SWAP`  
instType | String | Instrument type.  
`SPOT`  
`SWAP`  
pairType | String | MM Program classification type.  
`A`: High liquidity tier  
`B-Crypto`: Medium/low liquidity crypto assets  
`B-TradFi`: Traditional finance instruments (SWAP only)

---

# 获取 MM 币对分类类型

获取当前做市商（MM）计划 SPOT 和 SWAP 产品的币对分类类型列表。

#### 限速：每2秒5次请求

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/public/mm-instrument-types`

> 请求示例
    
    
    GET /api/v5/public/mm-instrument-types?instType=SWAP
    
    
    
    import okx.PublicData as PublicData
    
    flag = "0"  # 实盘:0 , 模拟盘：1
    
    publicDataAPI = PublicData.PublicAPI(flag=flag)
    
    # 获取 MM 币对分类类型
    result = publicDataAPI.get_mm_instrument_types(
        instType="SWAP"
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instType | String | 否 | 产品类型  
`SPOT`  
`SWAP`  
未指定时返回全部类型  
instId | String | 否 | 产品ID，如 `BTC-USDT`、`BTC-USDT-SWAP`  
指定时返回至多一条记录  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "instId": "BTC-USDT-SWAP",
                "instType": "SWAP",
                "pairType": "A"
            },
            {
                "instId": "ETH-USDT-SWAP",
                "instType": "SWAP",
                "pairType": "A"
            },
            {
                "instId": "XAU-USDT-SWAP",
                "instType": "SWAP",
                "pairType": "B-TradFi"
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
instId | String | 产品ID，如 `BTC-USDT-SWAP`  
instType | String | 产品类型  
`SPOT`  
`SWAP`  
pairType | String | MM 计划分类类型  
`A`：高流动性品种  
`B-Crypto`：中低流动性加密资产  
`B-TradFi`：传统金融品种（仅 SWAP）