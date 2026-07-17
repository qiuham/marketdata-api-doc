---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#public-data-rest-api-unit-convert
anchor_id: public-data-rest-api-unit-convert
api_type: REST
updated_at: 2026-07-17 19:17:31.800444
---

# Unit convert

Convert the crypto value to the number of contracts, or vice versa

#### Rate Limit: 10 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/public/convert-contract-coin`

> Request Example
    
    
    GET /api/v5/public/convert-contract-coin?instId=BTC-USD-SWAP&px=35000&sz=0.888
    
    
    
    import okx.PublicData as PublicData
    
    flag = "0"  # Production trading: 0, Demo trading: 1
    
    publicDataAPI = PublicData.PublicAPI(flag=flag)
    
    
    # Convert the crypto value to the number of contracts, or vice versa
    result = publicDataAPI.get_convert_contract_coin(
        instId="BTC-USD-SWAP",
        px="35000",
        sz="0.888"
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
type | String | No | Convert type  
`1`: Convert currency to contract  
`2`: Convert contract to currency  
The default is `1`  
instId | String | Yes | Instrument ID  
only applicable to `FUTURES`/`SWAP`/`OPTION`  
sz | String | Yes | Quantity to buy or sell  
It is quantity of currency while converting currency to contract;   
It is quantity of contract while converting contract to currency.  
px | String | Conditional | Order price  
For crypto-margined contracts, it is necessary while converting.  
For USDT-margined contracts, it is necessary while converting between usdt and contract.  
It is optional while converting between coin and contract.   
For OPTION, it is optional.  
unit | String | No | The unit of currency  
`coin`  
`usds`: USDT/USDC  
The default is `coin`, only applicable to USDⓈ-margined contracts from `FUTURES`/`SWAP`  
opType | String | No | Order type  
`open`: round down sz when opening positions   
`close`: round sz to the nearest when closing positions   
The default is `close`   
Applicable to `FUTURES` `SWAP`  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "instId": "BTC-USD-SWAP",
                "px": "35000",
                "sz": "311",
                "type": "1",
                "unit": "coin"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
type | String | Convert type   
`1`: Convert currency to contract  
`2`: Convert contract to currency  
instId | String | Instrument ID  
px | String | Order price  
sz | String | Quantity to buy or sell  
It is quantity of contract while converting currency to contract  
It is quantity of currency while contract to currency.  
unit | String | The unit of currency  
`coin`  
`usds`: USDT/USDC

---

# 张币转换

由币转换为张，或者张转换为币。

#### 限速：10次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/public/convert-contract-coin`

> 请求示例
    
    
    GET /api/v5/public/convert-contract-coin?instId=BTC-USD-SWAP&px=35000&sz=0.888
    
    
    
    import okx.PublicData as PublicData
    
    flag = "0"  # 实盘:0 , 模拟盘：1
    
    publicDataAPI = PublicData.PublicAPI(flag=flag)
    
    
    # 张币转换
    result = publicDataAPI.get_convert_contract_coin(
        instId="BTC-USD-SWAP",
        px="35000",
        sz="0.888"
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
type | String | 否 | 转换类型  
`1`：币转张   
`2`：张转币  
默认为`1`  
instId | String | 是 | 产品ID，仅适用于`交割`/`永续`/`期权`  
sz | String | 是 | 数量，币转张时，为币的数量，张转币时，为张的数量。  
px | String | 可选 | 委托价格  
币本位合约的张币转换时必填  
U本位合约，usdt 与张的转换时，必填；coin 与张的转换时，可不填  
期权的张币转换时，可不填。  
unit | String | 否 | 币的单位  
`coin`：币  
`usds`：usdt/usdc  
默认为 `coin`，仅适用于`交割`/`永续`的U本位合约  
opType | String | 否 | 将要下单的类型  
`open`：开仓时将sz舍位  
`close`：平仓时将sz四舍五入  
默认值为`close`  
适用于`交割`/`永续`  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "instId": "BTC-USD-SWAP",
                "px": "35000",
                "sz": "311",
                "type": "1",
                "unit": "coin"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
type | String | 转换类型   
`1`：币转张   
`2`：张转币  
instId | String | 产品ID  
px | String | 委托价格  
sz | String | 数量  
张转币时，为币的数量；币转张时，为张的数量。  
unit | String | 币的单位  
`coin`：币  
`usds`：usdt/usdc