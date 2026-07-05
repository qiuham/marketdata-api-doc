---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#trading-account-rest-api-get-account-and-position-risk
anchor_id: trading-account-rest-api-get-account-and-position-risk
api_type: REST
updated_at: 2026-07-05 19:33:09.335145
---

# Get account and position risk

Get account and position risk  
  
Obtain basic information about accounts and positions on the same time snapshot 

#### Rate Limit: 10 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/account/account-position-risk`

> Request Example
    
    
    GET /api/v5/account/account-position-risk
    
    
    
    
    import okx.Account as Account
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading:0 , demo trading:1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # Get account and position risk
    result = accountAPI.get_account_position_risk()
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instType | String | No | Instrument type  
`MARGIN`  
`SWAP`  
`FUTURES`  
`OPTION`  
  
> Response Example
    
    
    {
        "code":"0",
        "data":[
            {
                "adjEq":"174238.6793649711331679",
                "balData":[
                    {
                        "ccy":"BTC",
                        "disEq":"78846.7803721021362242",
                        "eq":"1.3863533369419636"
                    },
                    {
                        "ccy":"USDT",
                        "disEq":"73417.2495112863300127",
                        "eq":"73323.395564963177146"
                    }
                ],
                "posData":[
                    {
                        "baseBal": "0.4",
                        "ccy": "",
                        "instId": "BTC-USDT",
                        "instType": "MARGIN",
                        "mgnMode": "isolated",
                        "notionalCcy": "0",
                        "notionalUsd": "0",
                        "pos": "0",
                        "posCcy": "",
                        "posId": "310388685292318723",
                        "posSide": "net",
                        "quoteBal": "0"
                    }
                ],
                "ts":"1620282889345"
            }
        ],
        "msg":""
    }
    

#### Response Parameters

**Parameters** | **Types** | **Description**  
---|---|---  
ts | String | Update time of account information, millisecond format of Unix timestamp, e.g. `1597026383085`  
adjEq | String | Adjusted / Effective equity in `USD`  
Applicable to `Multi-currency margin` and `Portfolio margin`  
balData | Array of objects | Detailed asset information in all currencies  
> ccy | String | Currency  
> eq | String | Equity of currency  
> disEq | String | Discount equity of currency in `USD`.  
posData | Array of objects | Detailed position information in all currencies  
> instType | String | Instrument type  
> mgnMode | String | Margin mode  
`cross`   
`isolated`  
> posId | String | Position ID  
> instId | String | Instrument ID, e.g. `BTC-USDT-SWAP`  
> pos | String | Quantity of positions `contract`. In the isolated margin mode, when doing manual transfers, a position with pos of `0` will be generated after the deposit is transferred  
> baseBal | String | ~~Base currency balance, only applicable to`MARGIN`（Quick Margin Mode）~~(Deprecated)  
> quoteBal | String | ~~Quote currency balance, only applicable to`MARGIN`（Quick Margin Mode）~~(Deprecated)  
> posSide | String | Position side  
`long`   
`short`   
`net` (`FUTURES`/`SWAP`/`OPTION`: positive `pos` means long position and negative `pos` means short position. `MARGIN`: `posCcy` being base currency means long position, `posCcy` being quote currency means short position.)  
> posCcy | String | Position currency, only applicable to `MARGIN` positions.  
> ccy | String | Currency used for margin  
> notionalCcy | String | Notional value of positions in `coin`  
> notionalUsd | String | Notional value of positions in `USD`

---

# 查看账户持仓风险

查看账户整体风险。  
  
获取同一时间切片上的账户和持仓的基础信息 

#### 限速：10次/2s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/account/account-position-risk`

> 请求示例
    
    
    GET /api/v5/account/account-position-risk
    
    
    
    
    import okx.Account as Account
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘:1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    # 查看账户特定风险状态
    result = accountAPI.get_account_position_risk()
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instType | String | 否 | 产品类型  
`MARGIN`：币币杠杆  
`SWAP`：永续合约  
`FUTURES`：交割合约  
`OPTION`：期权   
  
  
> 返回结果
    
    
    {
        "code":"0",
        "data":[
            {
                "adjEq":"174238.6793649711331679",
                "balData":[
                    {
                        "ccy":"BTC",
                        "disEq":"78846.7803721021362242",
                        "eq":"1.3863533369419636"
                    },
                    {
                        "ccy":"USDT",
                        "disEq":"73417.2495112863300127",
                        "eq":"73323.395564963177146"
                    }
                ],
                "posData":[
                    {
                        "baseBal": "0.4",
                        "ccy": "",
                        "instId": "BTC-USDT",
                        "instType": "MARGIN",
                        "mgnMode": "isolated",
                        "notionalCcy": "0",
                        "notionalUsd": "0",
                        "pos": "0",
                        "posCcy": "",
                        "posId": "310388685292318723",
                        "posSide": "net",
                        "quoteBal": "0"
                    }
                ],
                "ts":"1620282889345"
            }
        ],
        "msg":""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
ts | String | 获取账户信息数据的时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
adjEq | String | 美金层面有效保证金  
适用于`跨币种保证金模式` 和`组合保证金模式`  
balData | Array of objects | 币种资产信息  
> ccy | String | 币种  
> eq | String | 币种总权益  
> disEq | String | 美金层面币种折算权益  
posData | Array of objects | 持仓详细信息  
> instType | String | 产品类型  
> mgnMode | String | 保证金模式  
`cross`：全仓  
`isolated`：逐仓  
> posId | String | 持仓ID  
> instId | String | 产品ID，如 `BTC-USDT-SWAP`  
> pos | String | 以`张`为单位的持仓数量，逐仓自主划转模式下，转入保证金后会产生pos为`0`的仓位  
> baseBal | String | ~~交易币余额，适用于`币币杠杆`（逐仓一键借币模式）~~（已弃用）  
> quoteBal | String | ~~计价币余额 ，适用于`币币杠杆`（逐仓一键借币模式）~~（已弃用）  
> posSide | String | 持仓方向  
`long`：开平仓模式开多  
`short`：开平仓模式开空  
`net`：买卖模式（`交割`/`永续`/`期权`：`pos`为正代表开多，`pos`为负代表开空。`币币杠杆`：`posCcy`为交易货币时，代表开多；`posCcy`为计价货币时，代表开空。）  
> posCcy | String | 仓位资产币种，仅适用于`币币杠杆`仓位  
> ccy | String | 占用保证金的币种  
> notionalCcy | String | 以`币`为单位的持仓数量  
> notionalUsd | String | 以`美金价值`为单位的持仓数量