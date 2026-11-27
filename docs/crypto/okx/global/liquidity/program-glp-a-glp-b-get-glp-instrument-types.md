---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#global-liquidity-program-glp-a-glp-b-get-glp-instrument-types
anchor_id: global-liquidity-program-glp-a-glp-b-get-glp-instrument-types
api_type: API
updated_at: 2026-11-27 18:59:29.188799
---

# Get GLP instrument types

Retrieve the GLP-A / GLP-B classification of SPOT and SWAP instruments. Use this endpoint to check which program and pool an instrument is assessed under. Expiry Futures & Nitro Spreads are not classified by pair type; all pairs are assessed together. GLP-C instruments are listed by Get GLP-C eligible instruments. Classifications and volume weights are for reference only; the OKX website and the program brochure prevail.  
  
#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/public/mm-instrument-types`

> Request Example
    
    
    GET /api/v5/public/mm-instrument-types?instType=SWAP
    
    
    
    import okx.PublicData as PublicData
    
    flag = "0"  # Production trading: 0, Demo trading: 1
    
    publicDataAPI = PublicData.PublicAPI(flag=flag)
    
    # Retrieve the list of GLP-A / GLP-B instrument classifications
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
pairType | String | GLP-A / GLP-B classification.  
`A`: Type A pair. Assessed under GLP-A (unadjusted share)  
`B-Crypto`: Type B crypto pair. Assessed under GLP-B; volume weight 1×  
`B-TradFi`: Type B TradFi pair (Spot and Perpetuals). Assessed under GLP-B; volume weight 2×  
`Type Special`: GLP Special Pair. Assessed under GLP-B; volume weight 4×

---

# 获取 GLP 币对分类类型

获取 SPOT 和 SWAP 产品的 GLP-A / GLP-B 分类，用于查询产品所属的考核计划及考核池。交割合约和 Nitro Spreads 不区分交易对类型，所有交易对一起考核。GLP-C 产品请参见获取 GLP-C 可参与产品。分类及交易量权重仅供参考，以 OKX 官网和计划手册为准。  
  
#### 限速：每2秒5次请求

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/public/mm-instrument-types`

> 请求示例
    
    
    GET /api/v5/public/mm-instrument-types?instType=SWAP
    
    
    
    import okx.PublicData as PublicData
    
    flag = "0"  # 实盘:0 , 模拟盘：1
    
    publicDataAPI = PublicData.PublicAPI(flag=flag)
    
    # 获取 GLP 币对分类类型
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
pairType | String | GLP-A / GLP-B 分类类型。  
`A`：Type A 交易对，按 GLP-A 未加权份额考核  
`B-Crypto`：Type B 加密交易对，按 GLP-B 考核，交易量权重 1×  
`B-TradFi`：Type B 传统金融交易对（现货和永续合约），按 GLP-B 考核，交易量权重 2×  
`Type Special`：GLP 特殊交易对，按 GLP-B 考核，交易量权重 4×