---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#public-data-rest-api-get-open-interest
anchor_id: public-data-rest-api-get-open-interest
api_type: REST
updated_at: 2026-07-12 19:16:51.600493
---

# Get open interest

Retrieve the total open interest for contracts on OKX.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: IP + Instrument ID

#### HTTP Request

`GET /api/v5/public/open-interest`

> Request Example
    
    
    GET /api/v5/public/open-interest?instType=SWAP
    
    
    
    import okx.PublicData as PublicData
    
    flag = "0"  # Production trading: 0, Demo trading: 1
    
    publicDataAPI = PublicData.PublicAPI(flag=flag)
    
    # Retrieve the total open interest for contracts on OKX
    result = publicDataAPI.get_open_interest(
        instType="SWAP",
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instType | String | Yes | Instrument type  
`SWAP`  
`FUTURES`  
`OPTION`  
`EVENTS`  
instFamily | String | Conditional | Instrument family  
Applicable to `FUTURES`/`SWAP`/`OPTION`  
If instType is `OPTION`, instFamily is required.  
instId | String | No | Instrument ID, e.g. `BTC-USDT-SWAP`  
Applicable to `FUTURES`/`SWAP`/`OPTION`/`EVENTS`  
  
> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
        {
            "instType":"SWAP",
            "instId":"BTC-USDT-SWAP",
            "oi":"5000",
            "oiCcy":"555.55",
            "oiUsd": "50000",
            "ts":"1597026383085"
        }
      ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
instType | String | Instrument type  
instId | String | Instrument ID  
oi | String | Open interest in number of contracts  
oiCcy | String | Open interest in number of coin  
oiUsd | String | Open interest in number of USD  
ts | String | Data return time, Unix timestamp format in milliseconds, e.g. `1597026383085`

---

# 获取持仓总量

查询单个交易产品的市场的持仓总量

#### 限速：20次/2s

#### 限速规则：IP + Instrument ID

#### HTTP请求

`GET /api/v5/public/open-interest`

> 请求示例
    
    
    GET /api/v5/public/open-interest?instType=SWAP
    
    
    
    import okx.PublicData as PublicData
    
    flag = "0"  # 实盘:0 , 模拟盘：1
    
    publicDataAPI = PublicData.PublicAPI(flag=flag)
    
    # 获取持仓总量
    result = publicDataAPI.get_open_interest(
        instType="FUTURES",
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instType | String | 是 | 产品类型  
`SWAP`：永续合约  
`FUTURES`：交割合约  
`OPTION`：期权  
`EVENTS`：事件合约  
instFamily | String | 可选 | 交易品种  
适用于`交割`/`永续`/`期权`  
`期权`下必传  
instId | String | 否 | 产品ID，如 `BTC-USDT-SWAP`   
仅适用于`交割`/`永续`/`期权`/`事件合约`  
  
> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
        {
            "instType":"SWAP",
            "instId":"BTC-USDT-SWAP",
            "oi":"5000",
            "oiCcy":"555.55",
            "oiUsd": "50000",
            "ts":"1597026383085"
        }
      ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
instType | String | 产品类型  
instId | String | 产品ID  
oi | String | 持仓量（按`张`折算）  
oiCcy | String | 持仓量（按`币`折算）  
oiUsd | String | 持仓量（按`USD`折算）  
ts | String | 数据返回时间，Unix时间戳的毫秒数格式 ，如 `1597026383085`