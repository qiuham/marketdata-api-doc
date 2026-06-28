---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#funding-account-rest-api-get-currencies
anchor_id: funding-account-rest-api-get-currencies
api_type: REST
updated_at: 2026-05-27 19:36:28.291253
---

# Get currencies

Retrieve a list of all currencies available which are related to the current account's KYC entity.

#### Rate Limit: 6 requests per second

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/asset/currencies`

> Request Example
    
    
    GET /api/v5/asset/currencies
    
    
    
    
    import okx.Funding as Funding
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading: 0, Demo trading: 1
    
    fundingAPI = Funding.FundingAPI(apikey, secretkey, passphrase, False, flag)
    
    # Get currencies
    result = fundingAPI.get_currencies()
    print(result)
    

#### Request Parameters

**Parameters** | **Types** | **Required** | **Description**  
---|---|---|---  
ccy | String | No | Single currency or multiple currencies separated with comma, e.g. `BTC` or `BTC,ETH`.  
  
> Response Example
    
    
    {
      "code": "0",
      "msg": "",
      "data": [
        {
            "burningFeeRate": "",
            "canDep": true,
            "canInternal": true,
            "canWd": true,
            "ccy": "BTC",
            "chain": "BTC-Bitcoin",
            "ctAddr": "",
            "depEstOpenTime": "",
            "depQuotaFixed": "",
            "depQuoteDailyLayer2": "",
            "fee": "0.00005",
            "logoLink": "https://static.coinall.ltd/cdn/oksupport/asset/currency/icon/btc20230419112752.png",
            "mainNet": true,
            "maxFee": "0.00005",
            "maxFeeForCtAddr": "",
            "maxWd": "500",
            "minDep": "0.0005",
            "minDepArrivalConfirm": "1",
            "minFee": "0.00005",
            "minFeeForCtAddr": "",
            "minInternal": "0.0001",
            "minWd": "0.0005",
            "minWdUnlockConfirm": "2",
            "name": "Bitcoin",
            "needTag": false,
            "usedDepQuotaFixed": "",
            "usedWdQuota": "0",
            "wdEstOpenTime": "",
            "wdQuota": "10000000",
            "wdTickSz": "8"
        }
      ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
ccy | String | Currency, e.g. `BTC`  
name | String | Name of currency. There is no related name when it is not shown.  
logoLink | String | The logo link of currency  
chain | String | Chain name, e.g. `USDT-ERC20`, `USDT-TRC20`  
ctAddr | String | Contract address  
canDep | Boolean | The availability to deposit from chain   
`false`: not available   
`true`: available  
canWd | Boolean | The availability to withdraw to chain   
`false`: not available   
`true`: available  
canInternal | Boolean | The availability to internal transfer   
`false`: not available   
`true`: available  
depEstOpenTime | String | Estimated opening time for deposit, Unix timestamp format in milliseconds, e.g. `1597026383085`  
if `canDep` is `true`, it returns `""`  
wdEstOpenTime | String | Estimated opening time for withdraw, Unix timestamp format in milliseconds, e.g. `1597026383085`  
if `canWd` is `true`, it returns `""`  
minDep | String | The minimum deposit amount of currency in a single transaction  
minWd | String | The minimum `on-chain withdrawal` amount of currency in a single transaction  
minInternal | String | The minimum `internal transfer` amount of currency in a single transaction  
No maximum `internal transfer` limit in a single transaction, subject to the withdrawal limit in the past 24 hours(`wdQuota`).  
maxWd | String | The maximum amount of currency `on-chain withdrawal` in a single transaction  
wdTickSz | String | The withdrawal precision, indicating the number of digits after the decimal point.  
The withdrawal fee precision kept the same as withdrawal precision.  
The accuracy of internal transfer withdrawal is 8 decimal places.  
wdQuota | String | The withdrawal limit in the past 24 hours (including `on-chain withdrawal` and `internal transfer`), unit in `USD`  
usedWdQuota | String | The amount of currency withdrawal used in the past 24 hours, unit in `USD`  
fee | String | The fixed withdrawal fee  
Apply to `on-chain withdrawal`  
minFee | String | ~~The minimum withdrawal fee for normal address  
Apply to `on-chain withdrawal`~~  
(Deprecated)  
maxFee | String | ~~The maximum withdrawal fee for normal address  
Apply to `on-chain withdrawal`~~  
(Deprecated)  
minFeeForCtAddr | String | ~~The minimum withdrawal fee for contract address  
Apply to `on-chain withdrawal`~~  
(Deprecated)  
maxFeeForCtAddr | String | ~~The maximum withdrawal fee for contract address  
Apply to `on-chain withdrawal`~~  
(Deprecated)  
burningFeeRate | String | Burning fee rate, e.g "0.05" represents "5%".  
Some currencies may charge combustion fees. The burning fee is deducted based on the withdrawal quantity (excluding gas fee) multiplied by the burning fee rate.  
Apply to `on-chain withdrawal`  
mainNet | Boolean | If current chain is main net, then it will return `true`, otherwise it will return `false`  
needTag | Boolean | Whether tag/memo information is required for withdrawal, e.g. `EOS` will return `true`  
minDepArrivalConfirm | String | The minimum number of blockchain confirmations to acknowledge fund deposit. The account is credited after that, but the deposit can not be withdrawn  
minWdUnlockConfirm | String | The minimum number of blockchain confirmations required for withdrawal of a deposit  
depQuotaFixed | String | The fixed deposit limit, unit in `USD`  
Return empty string if there is no deposit limit  
usedDepQuotaFixed | String | The used amount of fixed deposit quota, unit in `USD`  
Return empty string if there is no deposit limit  
depQuoteDailyLayer2 | String | The layer2 network daily deposit limit

---

# 获取币种列表

获取当前用户KYC实体支持的币种列表。

#### 限速：6 次/s

#### 限速规则：User ID

#### 权限：读取

#### HTTP 请求

`GET /api/v5/asset/currencies`

> 请求示例
    
    
    GET /api/v5/asset/currencies
    
    
    
    
    import okx.Funding as Funding
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    fundingAPI = Funding.FundingAPI(apikey, secretkey, passphrase, False, flag)
    
    # 获取币种列表
    result = fundingAPI.get_currencies()
    print(result)
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
ccy | String | 否 | 币种，如 `BTC`  
支持多币种查询，币种之间半角逗号分隔  
  
> 返回结果
    
    
    {
      "code": "0",
      "msg": "",
      "data": [
        {
            "burningFeeRate": "",
            "canDep": true,
            "canInternal": true,
            "canWd": true,
            "ccy": "BTC",
            "chain": "BTC-Bitcoin",
            "ctAddr": "",
            "depEstOpenTime": "",
            "depQuotaFixed": "",
            "depQuoteDailyLayer2": "",
            "fee": "0.00005",
            "logoLink": "https://static.coinall.ltd/cdn/oksupport/asset/currency/icon/btc20230419112752.png",
            "mainNet": true,
            "maxFee": "0.00005",
            "maxFeeForCtAddr": "",
            "maxWd": "500",
            "minDep": "0.0005",
            "minDepArrivalConfirm": "1",
            "minFee": "0.00005",
            "minFeeForCtAddr": "",
            "minInternal": "0.0001",
            "minWd": "0.0005",
            "minWdUnlockConfirm": "2",
            "name": "Bitcoin",
            "needTag": false,
            "usedDepQuotaFixed": "",
            "usedWdQuota": "0",
            "wdEstOpenTime": "",
            "wdQuota": "10000000",
            "wdTickSz": "8"
        }
      ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
ccy | String | 币种名称，如 `BTC`  
name | String | 币种名称，不显示则无对应名称  
logoLink | String | 币种Logo链接  
chain | String | 币种链信息  
有的币种下有多个链，必须要做区分，如`USDT`下有`USDT-ERC20`，`USDT-TRC20`多个链  
ctAddr | String | 合约地址  
canDep | Boolean | 当前是否可充值  
`false`：不可链上充值  
`true`：可以链上充值  
canWd | Boolean | 当前是否可提币  
`false`：不可链上提币  
`true`：可以链上提币  
canInternal | Boolean | 当前是否可内部转账  
`false`：不可内部转账  
`true`：可以内部转账  
depEstOpenTime | String | 充值预期开放时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
如果 `canDep` 为 `true`，则返回 `""`  
wdEstOpenTime | String | 提币预期开放时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
如果 `canWd` 为 `true`，则返回 `""`  
minDep | String | 币种单笔最小充值量  
minWd | String | 币种单笔最小`链上提币`量  
minInternal | String | 币种单笔最小`内部转账`量  
无单笔最大`内部转账`量限制，受24小时内提币额度(`wdQuota`)限制  
maxWd | String | 币种单笔最大`链上提币`量  
wdTickSz | String | 提币精度,表示小数点后的位数。提币手续费精度与提币精度保持一致。  
内部转账提币精度为小数点后8位。  
wdQuota | String | 过去24小时内提币额度（包含`链上提币`和`内部转账`），单位为`USD`  
usedWdQuota | String | 过去24小时内已用提币额度，单位为`USD`  
fee | String | 固定的提币手续费数量  
适用于`链上提币`  
minFee | String | ~~普通地址最小提币手续费数量  
适用于`链上提币`~~  
该字段已废弃  
maxFee | String | ~~普通地址最大提币手续费数量  
适用于`链上提币`~~  
该字段已废弃  
minFeeForCtAddr | String | ~~合约地址最小提币手续费数量  
适用于`链上提币`~~  
该字段已废弃  
maxFeeForCtAddr | String | ~~合约地址最大提币手续费数量  
适用于`链上提币`~~  
该字段已废弃  
burningFeeRate | String | 燃烧费率，如 `0.05` 代表 `5%`。  
部分币种会收取燃烧费用。燃烧费用按照提币数量（不含gas fee） 乘以 燃烧费率，在提币数量基础上扣除。  
适用于`链上提币`  
mainNet | Boolean | 当前链是否为主链  
needTag | Boolean | 当前链提币是否需要标签（tag/memo）信息，如 `EOS`该字段为`true`  
minDepArrivalConfirm | String | 充值到账最小网络确认数。币已到账但不可提。  
minWdUnlockConfirm | String | 提现解锁最小网络确认数  
depQuotaFixed | String | 充币固定限额，单位为`USD`  
没有充币限制则返回""  
usedDepQuotaFixed | String | 已用充币固定额度，单位为`USD`  
没有充币限制则返回""  
depQuoteDailyLayer2 | String | Layer2网络每日充值上限