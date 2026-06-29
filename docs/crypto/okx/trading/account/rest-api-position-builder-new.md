---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#trading-account-rest-api-position-builder-new
anchor_id: trading-account-rest-api-position-builder-new
api_type: REST
updated_at: 2026-06-29 19:55:39.114456
---

# Position builder (new)

Calculates portfolio margin information for virtual position/assets or current position of the user.  
You can add up to 200 virtual positions and 200 virtual assets in one request.  
  
#### Rate Limit: 2 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`POST /api/v5/account/position-builder`

> Request Example
    
    
    # Both real and virtual positions and assets are calculated 
    POST /api/v5/account/position-builder
    body
    {
        "inclRealPosAndEq": false,
        "simPos":[
             {
                "pos":"-10",
                "instId":"BTC-USDT-SWAP",
                "avgPx":"100000"
             },
             {
                "pos":"10",
                "instId":"LTC-USDT-SWAP",
                "avgPx":"8000"
             }
        ],
        "simAsset":[
            {
                "ccy": "USDT",
                "amt": "100"
            }
        ],
        "greeksType":"CASH"
    }
    
    
    # Only existing real positions are calculated
    POST /api/v5/account/position-builder
    body
    {
       "inclRealPosAndEq":true
    }
    
    
    # Only virtual positions are calculated
    POST /api/v5/account/position-builder
    body
    {
        "acctLv": "4",
        "inclRealPosAndEq": false,
        "simPos":[
            {
                "pos":"10",
                "instId":"BTC-USDT-SWAP",
                "avgPx":"100000"
            },
            {
                "pos":"10",
                "instId":"LTC-USDT-SWAP",
                "avgPx":"8000"
            }
        ]
    }
    
    # Switch to Multi-currency margin mode
    POST /api/v5/account/position-builder
    body
    {
        "acctLv": "3",
        "lever":"10",
        "simPos":[
            {
                "pos":"10",
                "instId":"BTC-USDT-SWAP",
                "avgPx":"100000",
                "lever":"5"
            },
            {
                "pos":"10",
                "instId":"LTC-USDT-SWAP",
                "avgPx":"8000"
            }
        ]
    }
    
    
    
    import okx.Account as Account
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading:0 , demo trading:1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    result = accountAPI.position_builder(
        inclRealPosAndEq=True,
        simPos=[
            {
                "pos": "10",
                "instId": "BTC-USDT-SWAP"
            },
            {
                "pos": "10",
                "instId": "LTC-USDT-SWAP"
            }
        ]
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
acctLv | String | No | Switch to account mode  
`3`: Multi-currency margin  
`4`: Portfolio margin  
The default is `4`  
inclRealPosAndEq | Boolean | No | Whether import existing positions and assets  
The default is `true`  
lever | String | No | Cross margin leverage in Multi-currency margin mode, the default is `1`.  
If the allowed leverage is exceeded, set according to the maximum leverage.  
Only applicable to `Multi-currency margin`  
simPos | Array of objects | No | List of simulated positions  
> instId | String | Yes | Instrument ID, e.g. `BTC-USDT-SWAP`  
Applicable to `SWAP`/`FUTURES`/`OPTION`  
> pos | String | Yes | Quantity of positions  
> avgPx | String | Yes | Average open price  
> lever | String | No | leverage  
Only applicable to `Multi-currency margin`  
The default is `1`  
If the allowed leverage is exceeded, set according to the maximum leverage.  
simAsset | Array of objects | No | List of simulated assets  
When `inclRealPosAndEq` is `true`, only real assets are considered and virtual assets are ignored  
> ccy | String | Yes | Currency, e.g. `BTC`  
> amt | String | Yes | Currency amount  
greeksType | String | No | Greeks type  
`BS`: Black-Scholes Model Greeks  
`PA`: Crypto Greeks  
`CASH`: Empirical Greeks  
The default is `BS`  
idxVol | String | No | Price volatility percentage, indicating what this price change means towards each of the values. In decimal form, range -0.99 ~ 1, in 0.01 increment.  
Default 0  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "acctLever": "-0.1364949794742562",
                "assets": [
                    {
                        "availEq": "0",
                        "borrowImr": "0",
                        "borrowMmr": "",
                        "ccy": "BTC",
                        "spotInUse": "0"
                    },
                    {
                        "availEq": "0",
                        "borrowImr": "0",
                        "borrowMmr": "",
                        "ccy": "LTC",
                        "spotInUse": "0"
                    },
                    {
                        "availEq": "0",
                        "borrowImr": "0",
                        "borrowMmr": "",
                        "ccy": "USDC",
                        "spotInUse": "0"
                    },
                    {
                        "availEq": "-78589.37",
                        "borrowImr": "7855.32188898",
                        "borrowMmr": "",
                        "ccy": "USDT",
                        "spotInUse": "0"
                    }
                ],
                "borrowMmr": "1571.064377796",
                "derivMmr": "1375.4837063088003",
                "eq": "-78553.21888979999",
                "marginRatio": "-25.95365779811705",
                "positions": [],
                "riskUnitData": [
                    {
                        "delta": "-9704.903689800001",
                        "gamma": "0",
                        "imrBf": "",
                        "imr": "1538.9669514070802",
                        "mmrBf": "",
                        "mmr": "1183.8207318516002",
                        "mr1": "1164.4109244719994",
                        "mr1FinalResult": {
                            "pnl": "-1164.4109244719994",
                            "spotShock": "0.12",
                            "volShock": "up"
                        },
                        "mr1Scenarios": {
                            "volSame": {
                                "0": "0",
                                "0.08": "-776.2739496480004",
                                "-0.08": "776.2739496480004",
                                "0.04": "-388.1369748240002",
                                "0.12": "-1164.4109244719994",
                                "-0.12": "1164.4109244719994",
                                "-0.04": "388.1369748240002"
                            },
                            "volShockDown": {
                                "0": "0",
                                "0.08": "-776.2739496480004",
                                "-0.08": "776.2739496480004",
                                "0.04": "-388.1369748240002",
                                "0.12": "-1164.4109244719994",
                                "-0.12": "1164.4109244719994",
                                "-0.04": "388.1369748240002"
                            },
                            "volShockUp": {
                                "0": "0",
                                "0.08": "-776.2739496480004",
                                "-0.08": "776.2739496480004",
                                "0.04": "-388.1369748240002",
                                "0.12": "-1164.4109244719994",
                                "-0.12": "1164.4109244719994",
                                "-0.04": "388.1369748240002"
                            }
                        },
                        "mr2": "0",
                        "mr3": "0",
                        "mr4": "19.4098073796",
                        "mr5": "0",
                        "mr6": "1164.4109244720003",
                        "mr6FinalResult": {
                            "pnl": "-2328.8218489440005",
                            "spotShock": "0.24"
                        },
                        "mr7": "43.67206660410001",
                        "mr8": "1571.064377796",
                        "mr9": "0",
                        "portfolios": [
                            {
                                "amt": "-10",
                                "avgPx": "100000",
                                "delta": "-9704.903689800001",
                                "floatPnl": "290.6300000000003",
                                "gamma": "0",
                                "instId": "BTC-USDT-SWAP",
                                "instType": "SWAP",
                                "isRealPos": false,
                                "markPxBf": "",
                                "markPx": "97093.7",
                                "notionalUsd": "9703.22",
                                "posSide": "net",
                                "theta": "0",
                                "vega": "0"
                            }
                        ],
                        "riskUnit": "BTC",
                        "theta": "0",
                        "upl": "290.49631020000027",
                        "vega": "0"
                    },
                    {
                        "delta": "1019.5308",
                        "gamma": "0",
                        "imrBf": "",
                        "imr": "249.16186679436",
                        "mmrBf": "",
                        "mmr": "191.6629744572",
                        "mr1": "183.50672805719995",
                        "mr1FinalResult": {
                            "pnl": "-183.50672805719995",
                            "spotShock": "-0.18",
                            "volShock": "up"
                        },
                        "mr1Scenarios": {
                            "volSame": {
                                "0": "0",
                                "-0.06": "-61.168909352399936",
                                "0.06": "61.168909352399936",
                                "-0.18": "-183.50672805719995",
                                "0.18": "183.50672805719995",
                                "0.12": "122.33781870480001",
                                "-0.12": "-122.33781870480001"
                            },
                            "volShockDown": {
                                "0": "0",
                                "-0.06": "-61.168909352399936",
                                "0.06": "61.168909352399936",
                                "-0.18": "-183.50672805719995",
                                "0.18": "183.50672805719995",
                                "0.12": "122.33781870480001",
                                "-0.12": "-122.33781870480001"
                            },
                            "volShockUp": {
                                "0": "0",
                                "-0.06": "-61.168909352399936",
                                "0.06": "61.168909352399936",
                                "-0.18": "-183.50672805719995",
                                "0.18": "183.50672805719995",
                                "0.12": "122.33781870480001",
                                "-0.12": "-122.33781870480001"
                            }
                        },
                        "mr2": "0",
                        "mr3": "0",
                        "mr4": "8.1562464",
                        "mr5": "0",
                        "mr6": "183.5067280572",
                        "mr6FinalResult": {
                            "pnl": "-367.0134561144",
                            "spotShock": "-0.36"
                        },
                        "mr7": "7.1367156",
                        "mr8": "1571.064377796",
                        "mr9": "0",
                        "portfolios": [
                            {
                                "amt": "10",
                                "avgPx": "8000",
                                "delta": "1019.5308",
                                "floatPnl": "-78980",
                                "gamma": "0",
                                "instId": "LTC-USDT-SWAP",
                                "instType": "SWAP",
                                "isRealPos": false,
                                "markPxBf": "",
                                "markPx": "102",
                                "notionalUsd": "1018.9",
                                "posSide": "net",
                                "theta": "0",
                                "vega": "0"
                            }
                        ],
                        "riskUnit": "LTC",
                        "theta": "0",
                        "upl": "-78943.6692",
                        "vega": "0"
                    }
                ],
                "totalImr": "9643.45070718144",
                "totalMmr": "2946.5480841048",
                "ts": "1736936801642",
                "upl": "-78653.1728898"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameters** | **Types** | **Description**  
---|---|---  
eq | String | Adjusted equity (`USD`) for the account  
totalMmr | String | Total MMR (`USD`) for the account  
totalImr | String | Total IMR (`USD`) for the account  
borrowMmr | String | Borrow MMR (`USD`) for the account  
derivMmr | String | Derivatives MMR (`USD`) for the account  
marginRatio | String | Cross maintenance margin ratio for the account  
upl | String | UPL for the account  
acctLever | String | Leverage of the account  
ts | String | Update time for the account, Unix timestamp format in milliseconds, e.g. `1597026383085`  
assets | Array of objects | Asset info  
> ccy | String | Currency, e.g. `BTC`  
> availEq | String | Currency equity  
> spotInUse | String | Spot in use  
> borrowMmr | String | ~~Borrowing MMR (`USD`)~~(Deprecated)  
> borrowImr | String | Borrowing IMR (`USD`)  
riskUnitData | Array of objects | Risk unit info  
> riskUnit | String | Risk unit, e.g. `BTC`  
> mmrBf | String | Risk unit MMR before volatility (`USD`)  
Return "" if users don't pass in idxVol  
> mmr | String | Risk unit MMR (`USD`)  
> imrBf | String | Risk unit IMR before volatility (`USD`)  
Return "" if users don't pass in idxVol  
> imr | String | Risk unit IMR (`USD`)  
> upl | String | Risk unit UPL (`USD`)  
> mr1 | String | Stress testing value of spot and volatility (all derivatives, and spot trading in spot-derivatives risk offset mode)  
> mr2 | String | Stress testing value of time value of money (TVM) (for options)  
> mr3 | String | Stress testing value of volatility span (for options)  
> mr4 | String | Stress testing value of basis (for all derivatives)  
> mr5 | String | Stress testing value of interest rate risk (for options)  
> mr6 | String | Stress testing value of extremely volatile markets (for all derivatives, and spot trading in spot-derivatives risk offset mode)  
> mr7 | String | Stress testing value of position reduction cost (for all derivatives)  
> mr8 | String | Borrowing MMR/IMR  
> mr9 | String | USDT-USDC-USD hedge risk  
> mr1Scenarios | Object | MR1 scenario analysis  
>> volShockDown | Object | When volatility shocks down, the P&L of stress tests under different price volatility ratios, format in {`change`: `value`,...}  
`change`: price volatility ratio (in percentage), e.g. `0.01` representing `1%`  
`value`: P&L under stress tests, measured in `USD`  
e.g. {"-0.15":"-2333.23", ...}  
>> volSame | Object | When volatility keeps the same, the P&L of stress tests under different price volatility ratios, format in {`change`: `value`,...}  
`change`: price volatility ratio (in percentage), e.g. `0.01` representing `1%`  
`value`: P&L under stress tests, measured in `USD`  
e.g. {"-0.15":"-2333.23", ...}  
>> volShockUp | Object | When volatility shocks up, the P&L of stress tests under different price volatility ratios, format in {`change`: `value`,...}  
`change`: price volatility ratio (in percentage), e.g. `0.01` representing `1%`  
`value`: P&L under stress tests, measured in `USD`  
e.g. {"-0.15":"-2333.23", ...}  
> mr1FinalResult | Object | MR1 worst-case scenario  
>> pnl | String | MR1 stress P&L (`USD`)  
>> spotShock | String | MR1 worst-case scenario spot shock (in percentage), e.g. `0.01` representing `1%`  
>> volShock | String | MR1 worst-case scenario volatility shock  
`down`: volatility shock down  
`unchange`: volatility unchanged  
`up`: volatility shock up  
> mr6FinalResult | Object | MR6 scenario analysis  
>> pnl | String | MR6 stress P&L (`USD`)  
>> spotShock | String | MR6 worst-case scenario spot shock (in percentage), e.g. `0.01` representing `1%`  
> delta | String | (Risk unit) The rate of change in the contract’s price with respect to changes in the underlying asset’s price.   
When the price of the underlying changes by x, the option’s price changes by delta multiplied by x.  
> gamma | String | (Risk unit) The rate of change in the delta with respect to changes in the underlying price.   
When the price of the underlying changes by x%, the option’s delta changes by gamma multiplied by x%.  
> theta | String | (Risk unit) The change in contract price each day closer to expiry.  
> vega | String | (Risk unit) The change of the option price when underlying volatility increases by 1%.  
> portfolios | Array of objects | Portfolios info  
Only applicable to `Portfolio margin`  
>> instId | String | Instrument ID, e.g. `BTC-USDT-SWAP`  
>> instType | String | Instrument type  
`SPOT`  
`SWAP`  
`FUTURES`  
`OPTION`  
>> amt | String | When `instType` is `SPOT`, it represents spot in use.  
When `instType` is `SWAP`/`FUTURES`/`OPTION`, it represents position amount.  
>> posSide | String | Position side  
`long`  
`short`  
`net`  
>> avgPx | String | Average open price  
>> markPxBf | String | Mark price before price volatility  
Return "" if users don't pass in idxVol  
>> markPx | String | Mark price  
>> floatPnl | String | Float P&L  
>> notionalUsd | String | Notional in `USD`  
>> delta | String | When `instType` is `SPOT`, it represents asset amount.  
When `instType` is `SWAP`/`FUTURES`/`OPTION`, it represents the rate of change in the contract’s price with respect to changes in the underlying asset’s price (by Instrument ID).  
>> gamma | String | The rate of change in the delta with respect to changes in the underlying price (by Instrument ID).   
When `instType` is `SPOT`, it will return "".  
>> theta | String | The change in contract price each day closer to expiry (by Instrument ID).  
When `instType` is `SPOT`, it will return "".  
>> vega | String | The change of the option price when underlying volatility increases by 1% (by Instrument ID).  
When `instType` is `SPOT`, it will return "".  
>> isRealPos | Boolean | Whether it is a real position  
If `instType` is `SWAP`/`FUTURES`/`OPTION`, it is a valid parameter, else it will return `false`  
positions | Array of objects | Position info  
Only applicable to `Multi-currency margin`  
> instId | String | Instrument ID, e.g. `BTC-USDT-SWAP`  
> instType | String | Instrument type  
`SPOT`  
`SWAP`  
`FUTURES`  
`OPTION`  
> amt | String | When `instType` is `SPOT`, it represents spot in use.  
When `instType` is `SWAP`/`FUTURES`/`OPTION`, it represents position amount.  
> posSide | String | Position side  
`long`  
`short`  
`net`  
> avgPx | String | Average open price  
> markPxBf | String | Mark price before price volatility  
Return "" if users don't pass in idxVol  
> markPx | String | Mark price  
> floatPnl | String | Float P&L  
> imrBf | String | IMR before price volatility  
> imr | String | IMR  
> mgnRatio | String | Maintenance margin ratio  
> lever | String | Leverage  
> notionalUsd | String | Notional in `USD`  
> isRealPos | Boolean | Whether it is a real position  
If `instType` is `SWAP`/`FUTURES`/`OPTION`, it is a valid parameter, else it will return `false`

---

# 仓位创建器

计算用户的模拟头寸或当前头寸的投资组合保证金信息，一次请求最多可添加200个虚拟仓位和200个虚拟虚拟资产  
  
#### 限速：2次/2s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`POST /api/v5/account/position-builder`

> 请求示例
    
    
    # 真实与虚拟的仓位与资产一起计算
    POST /api/v5/account/position-builder
    body
    {
        "inclRealPosAndEq": false,
        "simPos":[
             {
                "pos":"-10",
                "instId":"BTC-USDT-SWAP",
                "avgPx":"100000"
             },
             {
                "pos":"10",
                "instId":"LTC-USDT-SWAP",
                "avgPx":"8000"
             }
        ],
        "simAsset":[
            {
                "ccy": "USDT",
                "amt": "100"
            }
        ],
        "greeksType":"CASH"
    }
    
    
    # 只计算已有真实仓位
    POST /api/v5/account/position-builder
    body
    {
       "inclRealPosAndEq": true
    }
    
    
    # 只计算虚拟仓位
    POST /api/v5/account/position-builder
    body
    {
        "acctLv": "4",
        "inclRealPosAndEq": false,
        "simPos":[
            {
                "pos":"10",
                "instId":"BTC-USDT-SWAP",
                "avgPx":"100000"
            },
            {
                "pos":"10",
                "instId":"LTC-USDT-SWAP",
                "avgPx":"8000"
            }
        ]
    }
    
    # 切换到跨币种
    POST /api/v5/account/position-builder
    body
    {
        "acctLv": "3",
        "lever":"10",
        "simPos":[
            {
                "pos":"10",
                "instId":"BTC-USDT-SWAP",
                "avgPx":"100000",
                "lever":"5"
            },
            {
                "pos":"10",
                "instId":"LTC-USDT-SWAP",
                "avgPx":"8000"
            }
        ]
    }
    
    
    
    import okx.Account as Account
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘: 0, 模拟盘: 1
    
    accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)
    
    result = accountAPI.position_builder(
        inclRealPosAndEq=True,
        simPos=[
            {
                "pos": "10",
                "instId": "BTC-USDT-SWAP",
                "avgPx":"100000"
            },
            {
                "pos": "10",
                "instId": "LTC-USDT-SWAP",
                "avgPx":"100000"
            }
        ]
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
acctLv | String | 否 | 切换至账户模式  
`3`：跨币种保证金模式  
`4`：组合保证金模式  
inclRealPosAndEq | Boolean | 否 | 是否代入已有仓位和资产  
默认为`true`  
lever | String | 否 | 跨币种下整体的全仓合约杠杆数量，默认为`1`。  
如果超过允许的杠杆倍数，按照最大的杠杆设置。  
适用于`跨币种保证金模式`  
simPos | Array of objects | 否 | 模拟仓位列表  
> instId | String | 是 | 交易产品ID，如 `BTC-USDT-SWAP`  
适用于 `SWAP`/`FUTURES`/`OPTION`  
> pos | String | 是 | 持仓量  
> avgPx | String | 是 | 平均开仓价格  
> lever | String | 否 | 杠杆  
仅适用于在跨币种保证金模式下指定交易产品的杠杆。如果用户不传，则选择默认杠杆为`1`。  
simAsset | Array of objects | 否 | 模拟资产  
当`inclRealPosAndEq`为`true`，只考虑真实资产，会忽略虚拟资产  
> ccy | String | 是 | 币种，如 `BTC`  
> amt | String | 是 | 币种数量  
可以为负，代表减少币种资产  
greeksType | String | 否 | 希腊值类型  
`BS`：BS模型  
`PA`：币本位  
`CASH`：美元现金等价  
默认是`BS`  
idxVol | String | 否 | 价格变动百分比。小数形式，范围 -0.99 ~ 1，以 0.01 为增量。  
默认值为 0  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "acctLever": "-0.1364949794742562",
                "assets": [
                    {
                        "availEq": "0",
                        "borrowImr": "0",
                        "borrowMmr": "",
                        "ccy": "BTC",
                        "spotInUse": "0"
                    },
                    {
                        "availEq": "0",
                        "borrowImr": "0",
                        "borrowMmr": "",
                        "ccy": "LTC",
                        "spotInUse": "0"
                    },
                    {
                        "availEq": "0",
                        "borrowImr": "0",
                        "borrowMmr": "",
                        "ccy": "USDC",
                        "spotInUse": "0"
                    },
                    {
                        "availEq": "-78589.37",
                        "borrowImr": "7855.32188898",
                        "borrowMmr": "",
                        "ccy": "USDT",
                        "spotInUse": "0"
                    }
                ],
                "borrowMmr": "1571.064377796",
                "derivMmr": "1375.4837063088003",
                "eq": "-78553.21888979999",
                "marginRatio": "-25.95365779811705",
                "positions": [],
                "riskUnitData": [
                    {
                        "delta": "-9704.903689800001",
                        "gamma": "0",
                        "imrBf": "",
                        "imr": "1538.9669514070802",
                        "mmrBf": "",
                        "mmr": "1183.8207318516002",
                        "mr1": "1164.4109244719994",
                        "mr1FinalResult": {
                            "pnl": "-1164.4109244719994",
                            "spotShock": "0.12",
                            "volShock": "up"
                        },
                        "mr1Scenarios": {
                            "volSame": {
                                "0": "0",
                                "0.08": "-776.2739496480004",
                                "-0.08": "776.2739496480004",
                                "0.04": "-388.1369748240002",
                                "0.12": "-1164.4109244719994",
                                "-0.12": "1164.4109244719994",
                                "-0.04": "388.1369748240002"
                            },
                            "volShockDown": {
                                "0": "0",
                                "0.08": "-776.2739496480004",
                                "-0.08": "776.2739496480004",
                                "0.04": "-388.1369748240002",
                                "0.12": "-1164.4109244719994",
                                "-0.12": "1164.4109244719994",
                                "-0.04": "388.1369748240002"
                            },
                            "volShockUp": {
                                "0": "0",
                                "0.08": "-776.2739496480004",
                                "-0.08": "776.2739496480004",
                                "0.04": "-388.1369748240002",
                                "0.12": "-1164.4109244719994",
                                "-0.12": "1164.4109244719994",
                                "-0.04": "388.1369748240002"
                            }
                        },
                        "mr2": "0",
                        "mr3": "0",
                        "mr4": "19.4098073796",
                        "mr5": "0",
                        "mr6": "1164.4109244720003",
                        "mr6FinalResult": {
                            "pnl": "-2328.8218489440005",
                            "spotShock": "0.24"
                        },
                        "mr7": "43.67206660410001",
                        "mr8": "1571.064377796",
                        "mr9": "0",
                        "portfolios": [
                            {
                                "amt": "-10",
                                "avgPx": "100000",
                                "delta": "-9704.903689800001",
                                "floatPnl": "290.6300000000003",
                                "gamma": "0",
                                "instId": "BTC-USDT-SWAP",
                                "instType": "SWAP",
                                "isRealPos": false,
                                "markPxBf": "",
                                "markPx": "97093.7",
                                "notionalUsd": "9703.22",
                                "posSide": "net",
                                "theta": "0",
                                "vega": "0"
                            }
                        ],
                        "riskUnit": "BTC",
                        "theta": "0",
                        "upl": "290.49631020000027",
                        "vega": "0"
                    },
                    {
                        "delta": "1019.5308",
                        "gamma": "0",
                        "imrBf": "",
                        "imr": "249.16186679436",
                        "mmrBf": "",
                        "mmr": "191.6629744572",
                        "mr1": "183.50672805719995",
                        "mr1FinalResult": {
                            "pnl": "-183.50672805719995",
                            "spotShock": "-0.18",
                            "volShock": "up"
                        },
                        "mr1Scenarios": {
                            "volSame": {
                                "0": "0",
                                "-0.06": "-61.168909352399936",
                                "0.06": "61.168909352399936",
                                "-0.18": "-183.50672805719995",
                                "0.18": "183.50672805719995",
                                "0.12": "122.33781870480001",
                                "-0.12": "-122.33781870480001"
                            },
                            "volShockDown": {
                                "0": "0",
                                "-0.06": "-61.168909352399936",
                                "0.06": "61.168909352399936",
                                "-0.18": "-183.50672805719995",
                                "0.18": "183.50672805719995",
                                "0.12": "122.33781870480001",
                                "-0.12": "-122.33781870480001"
                            },
                            "volShockUp": {
                                "0": "0",
                                "-0.06": "-61.168909352399936",
                                "0.06": "61.168909352399936",
                                "-0.18": "-183.50672805719995",
                                "0.18": "183.50672805719995",
                                "0.12": "122.33781870480001",
                                "-0.12": "-122.33781870480001"
                            }
                        },
                        "mr2": "0",
                        "mr3": "0",
                        "mr4": "8.1562464",
                        "mr5": "0",
                        "mr6": "183.5067280572",
                        "mr6FinalResult": {
                            "pnl": "-367.0134561144",
                            "spotShock": "-0.36"
                        },
                        "mr7": "7.1367156",
                        "mr8": "1571.064377796",
                        "mr9": "0",
                        "portfolios": [
                            {
                                "amt": "10",
                                "avgPx": "8000",
                                "delta": "1019.5308",
                                "floatPnl": "-78980",
                                "gamma": "0",
                                "instId": "LTC-USDT-SWAP",
                                "instType": "SWAP",
                                "isRealPos": false,
                                "markPxBf": "",
                                "markPx": "102",
                                "notionalUsd": "1018.9",
                                "posSide": "net",
                                "theta": "0",
                                "vega": "0"
                            }
                        ],
                        "riskUnit": "LTC",
                        "theta": "0",
                        "upl": "-78943.6692",
                        "vega": "0"
                    }
                ],
                "totalImr": "9643.45070718144",
                "totalMmr": "2946.5480841048",
                "ts": "1736936801642",
                "upl": "-78653.1728898"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
eq | String | 账户有效保证金  
totalMmr | String | 账户维持保证金，单位为`USD`  
totalImr | String | 账户初始保证金占用，单位为`USD`  
borrowMmr | String | 账户借币维持保证金，单位为`USD`  
derivMmr | String | 账户衍生品维持保证金，单位为`USD`  
marginRatio | String | 账户全仓维持保证金率  
upl | String | 账户浮动盈亏  
acctLever | String | 账户全仓杠杆  
ts | String | 账户信息的更新时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
assets | Array of objects | 资产信息  
> ccy | String | 币种，如 `BTC`  
> availEq | String | 币种权益  
> spotInUse | String | 现货对冲占用  
> borrowMmr | String | ~~借币维持保证金，单位为`USD`~~字段已废弃  
> borrowImr | String | 借币初始保证金，单位为`USD`  
riskUnitData | Array of objects | Risk unit 相关信息  
适用于`组合保证金模式`  
> riskUnit | String | 账户内的 risk unit，如 `BTC`  
> mmrBf | String | 价格变动前 Risk unit 维度的维持保证金，单位为`USD`  
若用户没有传入idxVol，则返回 ""  
> mmr | String | Risk unit 维度的维持保证金，单位为`USD`  
> imrBf | String | 价格变动前 Risk unit 维度的初始保证金，单位为`USD`  
若用户没有传入idxVol，则返回 ""  
> imr | String | Risk unit 维度的初始保证金，单位为`USD`  
> upl | String | Risk unit 维度的浮动盈亏，单位为`USD`  
> mr1 | String | 现货和波动率变化风险 (适用于所有衍生品，以及在现货对冲模式下的现货)  
> mr2 | String | 时间价值风险 (仅适用于期权)  
> mr3 | String | 波动率跨期风险 (仅适用于期权)  
> mr4 | String | 基差风险 (适用于所有衍生品)  
> mr5 | String | 利率风险 (仅适用于期权)  
> mr6 | String | 极端市场波动风险 (适用于所有衍生品，以及在现货对冲模式下的现货)  
> mr7 | String | 减仓成本 (适用于所有衍生品)  
> mr8 | String | 借币维持保证金/初始保证金  
> mr9 | String | USDT-USDC-USD 对冲风险  
> mr1Scenarios | Object of objects | MR1 的压力测试场景分析  
>> volShockDown | Object | 波动率向下时，不同价格波动比率下的压力测试盈亏  
值为 {`change`: `value`, ...}   
`change`：价格波动比率（百分比），如 `0.01` 代表 `1%`  
`value`：压力测试下的盈亏，单位为`USD`  
如 {"-0.15":"-2333.23", ...}  
>> volSame | Object | 波动率不变时，不同价格波动比率下的压力测试盈亏  
值为 {`change`: `value`, ...}   
`change`：价格波动比率（百分比），如 `0.01` 代表 `1%`  
`value`：压力测试下的盈亏，单位为`USD`  
如 {"-0.15":"-2333.23", ...}  
>> volShockUp | Object | 波动率向上时，不同价格波动比率下的压力测试盈亏  
值为 {`change`: `value`, ...}   
`change`：价格波动比率（百分比），如 `0.01` 代表 `1%`  
`value`：压力测试下的盈亏，单位为`USD`  
如 {"-0.15":"-2333.23", ...}  
> mr1FinalResult | Object | MR1 最大亏损场景  
>> pnl | String | MR1 最大亏损压测盈亏，单位为 `USD`  
>> spotShock | String | MR1 最大亏损的价格波动（百分比），如 `0.01` 代表 `1%`  
>> volShock | String | MR1 最大亏损波动率趋势  
`down`：波动率向下  
`unchange`：波动率不变  
`up`：波动率向上  
> mr6FinalResult | Object | MR6 最大亏损场景  
>> pnl | String | MR6 最大亏损压测盈亏，单位为 `USD`  
>> spotShock | String | MR6 最大亏损的价格波动（百分比），如 `0.01` 代表 `1%`  
> delta | String | (Risk unit 维度) 合约价格随标的价格变动的比例  
当标的价格变动 x 时，合约价格变动约为此 Delta 数值乘以 x  
> gamma | String | (Risk unit 维度) 标的价格对 Delta 值的影响程度  
当标的价格变动 x% 时，期权 Delta 值的变动约为此 Gamma 数值乘以 x%  
> theta | String | (Risk unit 维度) 距离到期日时间缩短 1 天，该合约价格的变化量  
> vega | String | (Risk unit 维度) 标的波动率增加 1%，该合约价格的变化量  
> portfolios | Array of objects | 资产组合  
>> instId | String | 产品ID，如 `BTC-USDT-SWAP`  
>> instType | String | 产品类型  
`SPOT`：现货  
`SWAP`：永续合约  
`FUTURES`：交割合约  
`OPTION`：期权  
>> amt | String | `instType`为`SPOT`，代表现货对冲占用  
`instType`为`SWAP`/`FUTURES`/`OPTION`，代表仓位数量。  
>> posSide | String | 持仓方向  
`long`：开平仓模式开多  
`short`：开平仓模式开空  
`net`：买卖模式  
>> avgPx | String | 平均开仓价格  
>> markPxBf | String | 价格变动前标记价格  
若用户没有传入idxVol，则返回 ""  
>> markPx | String | 标记价格  
>> floatPnl | String | 浮动盈亏  
>> notionalUsd | String | 美金价值  
>> delta | String | `instType`为`SPOT`，代表资产数量。  
`instType`为`SWAP`/`FUTURES`/`OPTION`，代表(产品层面) 合约价格随标的价格变动的比例。  
>> gamma | String | (产品层面) 标的价格对 Delta 值的影响程度  
`instType`为`SPOT`，返回""  
>> theta | String | (产品层面) 距离到期日时间缩短 1 天，该合约价格的变化量  
`instType`为`SPOT`，返回""  
>> vega | String | (产品层面) 标的波动率增加 1%，该合约价格的变化量  
`instType`为`SPOT`，返回""  
>> isRealPos | Boolean | 是否为真实仓位  
`instType`为`SWAP`/`FUTURES`/`OPTION`，该字段有效，其他都默认返回`false`  
positions | Array of objects | 仓位信息  
适用于`跨币种保证金模式`  
> instId | String | 产品ID，如 `BTC-USDT-SWAP`  
> instType | String | 产品类型  
`SPOT`：现货  
`SWAP`：永续合约  
`FUTURES`：交割合约  
`OPTION`：期权  
> amt | String | `instType`为`SPOT`，代表现货对冲占用  
`instType`为`SWAP`/`FUTURES`/`OPTION`，代表仓位数量。  
> posSide | String | 持仓方向  
`long`：开平仓模式开多  
`short`：开平仓模式开空  
`net`：买卖模式  
> avgPx | String | 平均开仓价格  
> markPxBf | String | 价格变动前标记价格  
若用户没有传入idxVol，则返回 ""  
> markPx | String | 标记价格  
> floatPnl | String | 浮动盈亏  
> imrBf | String | 价格变动前初始保证金  
> imr | String | 初始保证金，仅适用于全仓  
> mgnRatio | String | 维持保证金率  
> lever | String | 杠杆倍数  
> notionalUsd | String | 美金价值  
> isRealPos | Boolean | 是否为真实仓位  
`instType`为`SWAP`/`FUTURES`/`OPTION`，该字段有效，其他都默认返回`false`