---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#public-data-rest-api-get-delta-hedge-currencies
anchor_id: public-data-rest-api-get-delta-hedge-currencies
api_type: REST
updated_at: 2026-09-04 19:13:26.502153
---

# Get Delta hedge currencies

Retrieve the currencies that share the same underlying asset and can therefore form a Delta hedge relationship, e.g. `ETH` and `BETH`, or `AAPL` and `XAAPL`.  
  
#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/public/delta-hedge-currencies`

> Request Example
    
    
    GET /api/v5/public/delta-hedge-currencies
    
    GET /api/v5/public/delta-hedge-currencies?ccy=ETH
    
    
    
    import okx.PublicData as PublicData
    
    flag = "0"  # Production trading: 0, Demo trading: 1
    
    publicDataAPI = PublicData.PublicAPI(flag=flag)
    
    # Retrieve Delta hedge currencies
    result = publicDataAPI.get_delta_hedge_currencies(
        ccy="ETH"
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
ccy | String | No | Currency, e.g. `ETH`.  
When specified, only the mapping entry for that currency is returned.  
When not specified, the full mapping is returned.  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "ccy": "ETH",
                "hedgeCcy": ["BETH"]
            },
            {
                "ccy": "XAU",
                "hedgeCcy": ["XAUT"]
            },
            {
                "ccy": "AAPL",
                "hedgeCcy": ["XAAPL"]
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
ccy | String | Currency, e.g. `AAPL`, `ETH`  
hedgeCcy | Array of strings | Currencies that share the same underlying asset as `ccy` and can form a Delta hedge relationship with it, e.g. `["XAAPL"]` when `ccy` is `AAPL`. The relationship is symmetric.

---

# 获取 Delta 对冲币种

获取具有相同标的资产、可构成 Delta 对冲关系的币种，如 `ETH` 与 `BETH`、`AAPL` 与 `XAAPL`。  
  
#### 限速：每2秒20次请求

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/public/delta-hedge-currencies`

> 请求示例
    
    
    GET /api/v5/public/delta-hedge-currencies
    
    GET /api/v5/public/delta-hedge-currencies?ccy=ETH
    
    
    
    import okx.PublicData as PublicData
    
    flag = "0"  # 实盘:0 , 模拟盘：1
    
    publicDataAPI = PublicData.PublicAPI(flag=flag)
    
    # 获取 Delta 对冲币种
    result = publicDataAPI.get_delta_hedge_currencies(
        ccy="ETH"
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
ccy | String | 否 | 币种，如 `ETH`  
指定时仅返回该币种的对应关系  
未指定时返回全部对应关系  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "ccy": "ETH",
                "hedgeCcy": ["BETH"]
            },
            {
                "ccy": "XAU",
                "hedgeCcy": ["XAUT"]
            },
            {
                "ccy": "AAPL",
                "hedgeCcy": ["XAAPL"]
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
ccy | String | 币种，如 `AAPL`、`ETH`  
hedgeCcy | Array of strings | 与 `ccy` 具有相同标的资产、可与其构成 Delta 对冲关系的币种，如 `ccy` 为 `AAPL` 时返回 `["XAAPL"]`。该关系是双向的。