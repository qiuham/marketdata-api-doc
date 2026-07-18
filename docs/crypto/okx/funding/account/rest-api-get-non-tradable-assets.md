---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#funding-account-rest-api-get-non-tradable-assets
anchor_id: funding-account-rest-api-get-non-tradable-assets
api_type: REST
updated_at: 2026-07-18 20:04:56.045096
---

# Get non-tradable assets

Retrieve the funding account balances of all the assets and the amount that is available or on hold.  
  
#### Rate Limit: 6 requests per second

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/asset/non-tradable-assets`

> Request Example
    
    
    GET /api/v5/asset/non-tradable-assets
    
    
    
    
    import okx.Funding as Funding
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading: 0, Demo trading: 1
    
    fundingAPI = Funding.FundingAPI(apikey, secretkey, passphrase, False, flag)
    
    result = fundingAPI.get_non_tradable_assets()
    print(result)
    

#### Request Parameters

**Parameters** | **Types** | **Required** | **Description**  
---|---|---|---  
ccy | String | No | Single currency or multiple currencies (no more than 20) separated with comma, e.g. `BTC` or `BTC,ETH`.  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "bal": "989.84719571",
                "burningFeeRate": "",
                "canWd": true,
                "ccy": "CELT",
                "chain": "CELT-OKTC",
                "ctAddr": "f403fb",
                "fee": "2",
                "feeCcy": "USDT",
                "logoLink": "https://static.coinall.ltd/cdn/assets/imgs/221/460DA8A592400393.png",
                "minWd": "0.1",
                "name": "",
                "needTag": false,
                "wdAll": false,
                "wdTickSz": "8"
            },
            {
                "bal": "0.001",
                "burningFeeRate": "",
                "canWd": true,
                "ccy": "MEME",
                "chain": "MEME-ERC20",
                "ctAddr": "09b760",
                "fee": "5",
                "feeCcy": "USDT",
                "logoLink": "https://static.coinall.ltd/cdn/assets/imgs/207/2E664E470103C613.png",
                "minWd": "0.001",
                "name": "MEME Inu",
                "needTag": false,
                "wdAll": false,
                "wdTickSz": "8"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
ccy | String | Currency, e.g. `CELT`  
name | String | Chinese name of currency. There is no related name when it is not shown.  
logoLink | String | Logo link of currency  
bal | String | Withdrawable balance  
canWd | Boolean | Availability to withdraw to chain.   
`false`: not available `true`: available  
chain | String | Chain for withdrawal  
minWd | String | Minimum withdrawal amount of currency in a single transaction  
wdAll | Boolean | Whether all assets in this currency must be withdrawn at one time  
fee | String | Fixed withdrawal fee  
feeCcy | String | Fixed withdrawal fee unit, e.g. `USDT`  
burningFeeRate | String | Burning fee rate, e.g "0.05" represents "5%".  
Some currencies may charge combustion fees. The burning fee is deducted based on the withdrawal quantity (excluding gas fee) multiplied by the burning fee rate.  
ctAddr | String | Last 6 digits of contract address  
wdTickSz | String | Withdrawal precision, indicating the number of digits after the decimal point  
needTag | Boolean | Whether tag/memo information is required for withdrawal

---

# 获取不可交易资产

获取当前用户 KYC 实体支持的不可交易资产列表。  
  
#### 限速：6 次/s

#### 限速规则：User ID

#### HTTP 请求

`GET /api/v5/asset/non-tradable-assets`

> 请求示例
    
    
    GET /api/v5/asset/non-tradable-assets
    
    
    
    
    import okx.Funding as Funding
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘: 0, 模拟盘: 1
    
    fundingAPI = Funding.FundingAPI(apikey, secretkey, passphrase, False, flag)
    
    result = fundingAPI.get_non_tradable_assets()
    print(result)
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
ccy | String | 否 | 币种，如 `BTC`  
支持多币种查询（不超过20个），币种之间半角逗号分隔  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "bal": "989.84719571",
                "burningFeeRate": "",
                "canWd": true,
                "ccy": "CELT",
                "chain": "CELT-OKTC",
                "ctAddr": "f403fb",
                "fee": "2",
                "feeCcy": "USDT",
                "logoLink": "https://static.coinall.ltd/cdn/assets/imgs/221/460DA8A592400393.png",
                "minWd": "0.1",
                "name": "",
                "needTag": false,
                "wdAll": false,
                "wdTickSz": "8"
            },
            {
                "bal": "0.001",
                "burningFeeRate": "",
                "canWd": true,
                "ccy": "MEME",
                "chain": "MEME-ERC20",
                "ctAddr": "09b760",
                "fee": "5",
                "feeCcy": "USDT",
                "logoLink": "https://static.coinall.ltd/cdn/assets/imgs/207/2E664E470103C613.png",
                "minWd": "0.001",
                "name": "MEME Inu",
                "needTag": false,
                "wdAll": false,
                "wdTickSz": "8"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
ccy | String | 币种名称，如 `CELT`  
name | String | 币种中文名称，不显示则无对应名称  
logoLink | String | 币种Logo链接  
bal | String | 可提余额  
canWd | Boolean | 是否可提  
`false`: 不可提 `true`: 可提  
chain | String | 支持提币的链  
minWd | String | 币种单笔最小提币量  
wdAll | Boolean | 该币种资产是否必须一次性全部提取  
fee | String | 提币固定手续费。提币手续费精度为小数点后8位。  
feeCcy | String | 提币固定手续费单位  
burningFeeRate | String | 燃烧费率，如 `0.05` 代表 `5%`。  
部分币种会收取燃烧费用。燃烧费用按照提币数量（不含gas fee） 乘以 燃烧费率，在提币数量基础上扣除。  
ctAddr | String | 合约地址后6位  
wdTickSz | String | 提币精度,表示小数点后的位数  
needTag | Boolean | 提币的链是否需要标签（tag/memo）信息