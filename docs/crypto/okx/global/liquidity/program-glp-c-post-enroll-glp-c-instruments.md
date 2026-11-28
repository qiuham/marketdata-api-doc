---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#global-liquidity-program-glp-c-post-enroll-glp-c-instruments
anchor_id: global-liquidity-program-glp-c-post-enroll-glp-c-instruments
api_type: API
updated_at: 2026-11-28 18:57:22.955200
---

# POST / Enroll GLP-C instruments

Enroll one or more instruments in GLP-C. Enrollment applies to the whole participant and is assessed from the current minute.

#### Rate Limit: 5 requests per second

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/users/glp-c/enroll-instruments`

> Request Example
    
    
    POST /api/v5/users/glp-c/enroll-instruments
    body
    {
        "instsToEnroll": [
            {"instType": "SPOT", "instId": "BTC-USDT"},
            {"instType": "PERP", "instId": "BTC-USDT"}
        ]
    }
    

#### Request Parameters

**Parameter** | **Type** | **Required** | **Description**  
---|---|---|---  
instsToEnroll | Array of objects | Yes | Instruments to enroll  
> instType | String | Yes | Instrument type  
`SPOT`  
`PERP`  
> instId | String | Yes | Instrument ID, e.g. `BTC-USDT`  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": {
            "enrolledInsts": [
                {"instType": "SPOT", "instId": "BTC-USDT"}
            ],
            "failedInsts": [
                {"instType": "PERP", "instId": "BTC-USDT"}
            ]
        }
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
enrolledInsts | Array of objects | Instruments enrolled successfully  
> instType | String | Instrument type  
> instId | String | Instrument ID  
failedInsts | Array of objects | Instruments that failed to enroll, because they are invalid or not eligible for the account  
> instType | String | Instrument type  
> instId | String | Instrument ID  
Enrolling an instrument that is already enrolled returns it in `enrolledInsts`. Withdrawal is not supported in this phase.

---

# POST / 注册 GLP-C 产品

为一个或多个产品注册 GLP-C。注册对整个 participant 生效，并从当前分钟起计入考核。

#### 限速：5次/s

#### 限速规则：User ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/users/glp-c/enroll-instruments`

> 请求示例
    
    
    POST /api/v5/users/glp-c/enroll-instruments
    body
    {
        "instsToEnroll": [
            {"instType": "SPOT", "instId": "BTC-USDT"},
            {"instType": "PERP", "instId": "BTC-USDT"}
        ]
    }
    

#### 请求参数

**参数名** | **类型** | **是否必须** | **描述**  
---|---|---|---  
instsToEnroll | Array of objects | 是 | 要注册的产品  
> instType | String | 是 | 产品类型  
`SPOT`  
`PERP`  
> instId | String | 是 | 产品 ID，如 `BTC-USDT`  
  
> 返回示例
    
    
    {
        "code": "0",
        "msg": "",
        "data": {
            "enrolledInsts": [
                {"instType": "SPOT", "instId": "BTC-USDT"}
            ],
            "failedInsts": [
                {"instType": "PERP", "instId": "BTC-USDT"}
            ]
        }
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
enrolledInsts | Array of objects | 注册成功的产品  
> instType | String | 产品类型  
> instId | String | 产品 ID  
failedInsts | Array of objects | 注册失败的产品，原因为产品无效或当前账户不可参与  
> instType | String | 产品类型  
> instId | String | 产品 ID  
注册已注册的产品时，该产品会在 `enrolledInsts` 中返回。本期不支持退出注册。