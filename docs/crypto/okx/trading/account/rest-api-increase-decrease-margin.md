---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#trading-account-rest-api-increase-decrease-margin
anchor_id: trading-account-rest-api-increase-decrease-margin
api_type: REST
updated_at: 2026-07-20 19:35:09.911042
---

# Increase/decrease margin

Increase or decrease the margin of the isolated position. Margin reduction may result in the change of the actual leverage.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/account/position/margin-balance`

> Request Example
    
    
    POST /api/v5/account/position/margin-balance 
    body
    {
        "instId":"BTC-USDT-200626",
        "posSide":"short",
        "type":"add",
        "amt":"1"
    }
    
    
    
    
    import okx.Account as Account
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading:0 , demo trading:1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # Increase margin
    result = accountAPI.adjustment_margin(
        instId="BTC-USDT-SWAP",
        posSide="short",
        type= "add",
        amt="1"
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instId | String | Yes | Instrument ID  
posSide | String | Yes | Position side, the default is `net`  
`long`   
`short`   
`net`  
type | String | Yes | `add`: add margin   
`reduce`: reduce margin  
amt | String | Yes | Amount to be increased or decreased.  
ccy | String | Conditional | Currency   
Applicable to `isolated` `MARGIN` orders  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
                "amt": "0.3",
                "ccy": "BTC",
                "instId": "BTC-USDT",
                "leverage": "",
                "posSide": "net",
                "type": "add"
            }]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
instId | String | Instrument ID  
posSide | String | Position side, `long` `short`  
amt | String | Amount to be increase or decrease  
type | String | `add`: add margin  
`reduce`: reduce margin  
leverage | String | Real leverage after the margin adjustment  
ccy | String | Currency  
Manual transfer mode  
The value of the margin initially assigned to the isolated position must be greater than or equal to 10,000 USDT, and a position will be created on the account.

---

# 调整保证金

增加或者减少逐仓保证金。减少保证金可能会导致实际杠杆倍数发生变化。

#### 限速：20次/2s

#### 限速规则：User ID

#### HTTP请求

`POST /api/v5/account/position/margin-balance`

> 请求示例
    
    
    POST /api/v5/account/position/margin-balance 
    body
    {
        "instId":"BTC-USDT-SWAP",
        "posSide":"short",
        "type":"add",
        "amt":"1"
    }
    
    
    
    
    import okx.Account as Account
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘:1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # 调整保证金
    result = accountAPI.adjustment_margin(
        instId="BTC-USDT-SWAP",
        posSide="short",
        type= "add",
        amt="1"
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instId | String | 是 | 产品ID  
posSide | String | 是 | 持仓方向，默认值是`net`  
`long`：开平仓模式开多  
`short`：开平仓模式开空  
`net`：买卖模式  
type | String | 是 | 增加/减少保证金  
`add`：增加   
`reduce`：减少  
amt | String | 是 | 增加或减少的保证金数量  
ccy | String | 可选 | 增加或减少的保证金的币种，  
适用于`逐仓杠杆`仓位  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "amt": "0.3",
                "ccy": "BTC",
                "instId": "BTC-USDT",
                "leverage": "",
                "posSide": "net",
                "type": "add"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
instId | String | 产品ID  
posSide | String | 持仓方向  
amt | String | 已增加/减少的保证金数量  
type | String | 增加/减少保证金  
leverage | String | 调整保证金后的实际杠杆倍数  
ccy | String | 增加或减少的保证金的币种  
自主划转模式  
初始划入逐仓仓位的保证金价值必须大于等于1万USDT,账户上会产生一个仓位。