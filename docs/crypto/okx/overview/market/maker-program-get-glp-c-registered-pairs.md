---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#overview-market-maker-program-get-glp-c-registered-pairs
anchor_id: overview-market-maker-program-get-glp-c-registered-pairs
api_type: API
updated_at: 2026-11-25 18:59:29.189609
---

# GET / GLP-C registered pairs

Retrieve the list of instruments that the account has registered for GLP-C.  
  
#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/users/glp/c/registered-pairs`

> Request Example
    
    
    GET /api/v5/users/glp/c/registered-pairs?instType=SPOT
    

#### Request Parameters

**Parameter** | **Type** | **Required** | **Description**  
---|---|---|---  
instType | String | No | Instrument type filter  
`SPOT`  
`SWAP`  
Returns all if omitted  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "instId": "DOGE-USDT",
                "instType": "SPOT",
                "registerTime": "1732300800000"
            },
            {
                "instId": "PEPE-USDT-SWAP",
                "instType": "SWAP",
                "registerTime": "1732300800000"
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
instId | String | Instrument ID  
instType | String | Instrument type  
`SPOT`  
`SWAP`  
registerTime | String | Registration time. Unix timestamp in milliseconds

---

# GET / 查询已注册 GLP-C 币对

查询账户已注册 GLP-C 的交易产品列表。  
  
#### 限速：5次/2s

#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/users/glp/c/registered-pairs`

> 请求示例
    
    
    GET /api/v5/users/glp/c/registered-pairs?instType=SPOT
    

#### 请求参数

**参数名** | **类型** | **是否必须** | **描述**  
---|---|---|---  
instType | String | 否 | 产品类型过滤  
`SPOT`  
`SWAP`  
不传返回全部  
  
> 返回示例
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "instId": "DOGE-USDT",
                "instType": "SPOT",
                "registerTime": "1732300800000"
            },
            {
                "instId": "PEPE-USDT-SWAP",
                "instType": "SWAP",
                "registerTime": "1732300800000"
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
instId | String | 产品ID  
instType | String | 产品类型  
`SPOT`  
`SWAP`  
registerTime | String | 注册时间。Unix 毫秒时间戳