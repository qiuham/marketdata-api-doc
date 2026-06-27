---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#funding-account-rest-api-get-deposit-address
anchor_id: funding-account-rest-api-get-deposit-address
api_type: REST
updated_at: 2026-05-27 19:36:30.803492
---

# Get deposit address

Retrieve the deposit addresses of currencies, including previously-used addresses.  
  
#### Rate Limit: 6 requests per second

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/asset/deposit-address`

> Request Example
    
    
    GET /api/v5/asset/deposit-address?ccy=BTC
    
    
    
    
    import okx.Funding as Funding
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading: 0, Demo trading: 1
    
    fundingAPI = Funding.FundingAPI(apikey, secretkey, passphrase, False, flag)
    
    # Get deposit address
    result = fundingAPI.get_deposit_address(
        ccy="USDT"
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
ccy | String | Yes | Currency, e.g. `BTC`  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "chain": "BTC-Bitcoin",
                "ctAddr": "",
                "ccy": "BTC",
                "to": "6",
                "addr": "39XNxK1Ryqgg3Bsyn6HzoqV4Xji25pNkv6",
                "verifiedName":"John Corner",
                "selected": true
            },
            {
                "chain": "BTC-OKC",
                "ctAddr": "",
                "ccy": "BTC",
                "to": "6",
                "addr": "0x66d0edc2e63b6b992381ee668fbcb01f20ae0428",
                "verifiedName":"John Corner",
                "selected": true
            },
            {
                "chain": "BTC-ERC20",
                "ctAddr": "5807cf",
                "ccy": "BTC",
                "to": "6",
                "addr": "0x66d0edc2e63b6b992381ee668fbcb01f20ae0428",
                "verifiedName":"John Corner",
                "selected": true
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
addr | String | Deposit address  
tag | String | Deposit tag (This will not be returned if the currency does not require a tag for deposit)  
memo | String | Deposit memo (This will not be returned if the currency does not require a memo for deposit)  
pmtId | String | Deposit payment ID (This will not be returned if the currency does not require a payment_id for deposit)  
addrEx | Object | Deposit address attachment (This will not be returned if the currency does not require this)  
e.g. `TONCOIN` attached tag name is `comment`, the return will be `{'comment':'123456'}`  
ccy | String | Currency, e.g. `BTC`  
chain | String | Chain name, e.g. `USDT-ERC20`, `USDT-TRC20`  
to | String | The beneficiary account  
`6`: Funding account `18`: Trading account  
The users under some entity (e.g. Brazil) only support deposit to trading account.  
verifiedName | String | Verified name (for recipient)  
selected | Boolean | Return `true` if the current deposit address is selected by the website page  
ctAddr | String | Last 6 digits of contract address

---

# 获取充值地址信息

获取各个币种的充值地址，包括曾使用过的老地址。  
  
#### 限速：6次/s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/asset/deposit-address`

> 请求示例
    
    
    GET /api/v5/asset/deposit-address?ccy=BTC
    
    
    
    
    import okx.Funding as Funding
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    fundingAPI = Funding.FundingAPI(apikey, secretkey, passphrase, False, flag)
    
    # 获取充值地址信息
    result = fundingAPI.get_deposit_address(
        ccy="USDT"
    )
    print(result)
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
ccy | String | 是 | 币种，如`BTC`  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "chain": "BTC-Bitcoin",
                "ctAddr": "",
                "ccy": "BTC",
                "to": "6",
                "addr": "39XNxK1Ryqgg3Bsyn6HzoqV4Xji25pNkv6",
                "verifiedName":"John Corner",
                "selected": true
            },
            {
                "chain": "BTC-OKC",
                "ctAddr": "",
                "ccy": "BTC",
                "to": "6",
                "addr": "0x66d0edc2e63b6b992381ee668fbcb01f20ae0428",
                "verifiedName":"John Corner",
                "selected": true
            },
            {
                "chain": "BTC-ERC20",
                "ctAddr": "5807cf",
                "ccy": "BTC",
                "to": "6",
                "addr": "0x66d0edc2e63b6b992381ee668fbcb01f20ae0428",
                "verifiedName":"John Corner",
                "selected": true
            }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
addr | String | 充值地址  
tag | String | 部分币种充值需要标签，若不需要则不返回此字段  
memo | String | 部分币种充值需要 memo，若不需要则不返回此字段  
pmtId | String | 部分币种充值需要此字段（payment_id），若不需要则不返回此字段  
addrEx | Object | 充值地址备注，部分币种充值需要，若不需要则不返回此字段  
如币种`TONCOIN`的充值地址备注标签名为`comment`,则该字段返回：{'comment':'123456'}  
ccy | String | 币种，如`BTC`  
chain | String | 币种链信息  
有的币种下有多个链，必须要做区分，如`USDT`下有`USDT-ERC20`，`USDT-TRC20`多个链  
to | String | 转入账户  
`6`：资金账户 `18`：交易账户  
某些主体用户(如巴西)只支持充值到交易账户  
verifiedName | String | (接受方)已验证姓名  
selected | Boolean | 该地址是否为页面选中的地址  
ctAddr | String | 合约地址后6位