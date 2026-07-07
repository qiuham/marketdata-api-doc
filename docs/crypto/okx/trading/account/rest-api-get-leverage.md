---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#trading-account-rest-api-get-leverage
anchor_id: trading-account-rest-api-get-leverage
api_type: REST
updated_at: 2026-07-07 19:41:23.423105
---

# Get leverage

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/account/leverage-info`

> Request Example
    
    
    GET /api/v5/account/leverage-info?instId=BTC-USDT-SWAP&mgnMode=cross
    
    
    
    
    import okx.Account as Account
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading:0 , demo trading:1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # Get leverage
    result = accountAPI.get_leverage(
        instId="BTC-USDT-SWAP",
        mgnMode="cross"
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instId | String | Conditional | Instrument ID  
Single instrument ID or multiple instrument IDs (no more than 20) separated with comma  
ccy | String | Conditional | Currency，used for getting leverage of currency level.  
Applicable to `cross` `MARGIN` of `Spot mode`/`Multi-currency margin`/`Portfolio margin`.  
Supported single currency or multiple currencies (no more than 20) separated with comma.  
mgnMode | String | Yes | Margin mode  
`cross` `isolated`  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
            "ccy":"",
            "instId": "BTC-USDT-SWAP",
            "mgnMode": "cross",
            "posSide": "long",
            "lever": "10"
        },{
            "ccy":"",
            "instId": "BTC-USDT-SWAP",
            "mgnMode": "cross",
            "posSide": "short",
            "lever": "10"
        }]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
instId | String | Instrument ID  
ccy | String | Currency，used for getting leverage of currency level.  
Applicable to `cross` `MARGIN` of `Spot mode`/`Multi-currency margin`/`Portfolio margin`.  
mgnMode | String | Margin mode  
posSide | String | Position side  
`long`   
`short`   
`net`  
In `long/short` mode, the leverage in both directions `long`/`short` will be returned.  
lever | String | Leverage  
Leverage cannot be enquired for the cross positions of Expiry Futures and Perpetual Futures under the portfolio margin account.

---

# 获取杠杆倍数

#### 限速：20次/2s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/account/leverage-info`

> 请求示例
    
    
    GET /api/v5/account/leverage-info?instId=BTC-USDT-SWAP&mgnMode=cross
    
    
    
    
    import okx.Account as Account
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘:1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # 获取杠杆倍数
    result = accountAPI.get_leverage(
        instId="BTC-USDT-SWAP",
        mgnMode="cross"
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instId | String | 可选 | 产品ID  
支持多个instId查询，半角逗号分隔。instId个数不超过20个。  
ccy | String | 可选 | 币种，用于币种维度的杠杆。  
仅适用于`现货模式`/`跨币种保证金模式`/`组合保证金模式`的全仓币币杠杆。  
支持多ccy查询，半角逗号分隔。ccy个数不超过20个。  
mgnMode | String | 是 | 保证金模式  
`isolated`：逐仓  
`cross`：全仓  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
            "ccy":"",
            "instId": "BTC-USDT-SWAP",
            "mgnMode": "cross",
            "posSide": "long",
            "lever": "10"
        },{
            "ccy":"",
            "instId": "BTC-USDT-SWAP",
            "mgnMode": "cross",
            "posSide": "short",
            "lever": "10"
        }]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
instId | String | 产品ID  
ccy | String | 币种，用于币种维度的杠杆。  
仅适用于`现货模式`/`跨币种保证金模式`/`组合保证金模式`的全仓币币杠杆。  
mgnMode | String | 保证金模式  
posSide | String | 持仓方向  
`long`：开平仓模式开多  
`short`：开平仓模式开空  
`net`：买卖模式  
开平仓模式下会返回两个方向的杠杆倍数  
lever | String | 杠杆倍数  
组合保证金账户下交割和永续的全仓不能获取杠杆倍数。