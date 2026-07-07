---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#trading-account-rest-api-isolated-margin-trading-settings
anchor_id: trading-account-rest-api-isolated-margin-trading-settings
api_type: REST
updated_at: 2026-07-07 19:41:25.935623
---

# Isolated margin trading settings

You can set the currency margin and futures/perpetual Isolated margin trading mode  
  
#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/account/set-isolated-mode`

> Request Example
    
    
    POST /api/v5/account/set-isolated-mode
    body
    {
        "isoMode":"automatic",
        "type":"MARGIN"
    }
    
    
    
    import okx.Account as Account
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading:0 , demo trading:1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # Isolated margin trading settings
    result = accountAPI.set_isolated_mode(
        isoMode="automatic",
        type="MARGIN"
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
isoMode | String | Yes | Isolated margin trading settings  
`auto_transfers_ccy`: New auto transfers, enabling both base and quote currency as the margin for isolated margin trading. Only applicable to `MARGIN`.  
`automatic`: Auto transfers  
type | String | Yes | Instrument type  
`MARGIN`  
`CONTRACTS`  
When there are positions and pending orders in the current account, the margin transfer mode from position to position cannot be adjusted. 

> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "isoMode": "automatic"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
isoMode | String | Isolated margin trading settings  
`automatic`: Auto transfers  
CONTRACTS  
Auto transfers: Automatically occupy and release the margin when opening and closing positions  MARGIN  
Auto transfers: Automatically borrow and return coins when opening and closing positions

---

# 逐仓交易设置

可以通过该接口设置币币杠杆和交割、永续的逐仓仓位保证金的划转模式  
  
#### 限速：5次/2s

#### 限速规则：User ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/account/set-isolated-mode`

> 请求示例
    
    
    POST /api/v5/account/set-isolated-mode
    body
    {
        "isoMode":"automatic",
        "type":"MARGIN"
    }
    
    
    
    import okx.Account as Account
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘:1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # 逐仓交易设置
    result = accountAPI.set_isolated_mode(
        isoMode="automatic",
        type="MARGIN"
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
isoMode | String | 是 | 逐仓保证金划转模式  
`auto_transfers_ccy`：新版开仓自动划转，支持交易货币及计价货币作为保证金，仅适用于`币币杠杆`  
`automatic`：开仓自动划转  
type | String | 是 | 业务线类型  
`MARGIN`：币币杠杆  
`CONTRACTS`：合约  
当前账户内有持仓和挂单时，不能调整逐仓保证金划转模式。 

> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "isoMode": "automatic"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
isoMode | String | 逐仓保证金划转模式  
`auto_transfers_ccy`：新版开仓自动划转  
`automatic`：开仓自动划转  
衍生品  
开仓划转：在开仓和平仓时自动占用和释放保证金  杠杆  
开仓划转：在开仓和平仓时自动借币和还币