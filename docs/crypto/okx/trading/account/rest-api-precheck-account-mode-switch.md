---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#trading-account-rest-api-precheck-account-mode-switch
anchor_id: trading-account-rest-api-precheck-account-mode-switch
api_type: REST
updated_at: 2026-06-28 19:36:23.650308
---

# Precheck account mode switch

Retrieve precheck information for account mode switching.

#### Rate limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/account/set-account-switch-precheck`

> Request example
    
    
    GET /api/v5/account/set-account-switch-precheck?acctLv=3
    
    

#### Request parameters

**Parameter** | **Type** | **Required** | **Description**  
---|---|---|---  
acctLv | String | Yes | Account mode  
`1`: Spot mode  
`2`: Futures mode  
`3`: Multi-currency margin code  
`4`: Portfolio margin mode  
  
> Response example. Futures mode->Portfolio margin mode, need to finish the Q&A on web or mobile first
    
    
    {
        "code": "51070",
        "data": [],
        "msg": "You do not meet the requirements for switching to this account mode. Please upgrade the account mode on the OKX website or App"
    }
    

> Response example. Futures mode->Portfolio margin mode, unmatched information. sCode 1
    
    
    {
        "code": "0",
        "data": [
            {
                "acctLv": "3",
                "curAcctLv": "1",
                "mgnAft": null,
                "mgnBf": null,
                "posList": [],
                "posTierCheck": [],
                "riskOffsetType": "",
                "sCode": "1",
                "unmatchedInfoCheck": [
                    {
                        "posList": [],
                        "totalAsset": "",
                        "type": "repay_borrowings"
                    }
                ]
            }
        ],
        "msg": ""
    }
    

> Response example. Portfolio margin mode->Multi-currency margin code, the user has cross-margin positions but doesn't preset leverage. sCode 3 
    
    
    {
        "code": "0",
        "data": [
            {
                "acctLv": "3",
                "curAcctLv": "4",
                "mgnAft": null,
                "mgnBf": null,
                "posList": [
                    {
                        "lever": "50",
                        "posId": "2005456500916518912"
                    },
                    {
                        "lever": "10",
                        "posId": "2005456108363218944"
                    },
                    {
                        "lever": "100",
                        "posId": "2005456332909477888"
                    },
                    {
                        "lever": "1",
                        "posId": "2005456415990251520"
                    }
                ],
                "posTierCheck": [],
                "riskOffsetType": "",
                "sCode": "3",
                "unmatchedInfoCheck": []
            }
        ],
        "msg": ""
    }
    

> Response example. Portfolio margin mode->Multi-currency margin code, the user finishes the leverage setting to 10, and passes the position tier an margin check. sCode 0. 
    
    
    {
        "code": "0",
        "data": [
            {
                "acctLv": "3",
                "curAcctLv": "4",
                "mgnAft": {
                    "acctAvailEq": "106002.2061970689",
                    "details": [],
                    "mgnRatio": "148.1652396878421"
                },
                "mgnBf": {
                    "acctAvailEq": "77308.89735228613",
                    "details": [],
                    "mgnRatio": "4.460069474634038"
                },
                "posList": [
                    {
                        "lever": "50",
                        "posId": "2005456500916518912"
                    },
                    {
                        "lever": "50",
                        "posId": "2005456108363218944"
                    },
                    {
                        "lever": "50",
                        "posId": "2005456332909477888"
                    },
                    {
                        "lever": "50",
                        "posId": "2005456415990251520"
                    }
                ],
                "posTierCheck": [],
                "riskOffsetType": "",
                "sCode": "0",
                "unmatchedInfoCheck": []
            }
        ],
        "msg": ""
    }
    
    

#### Response parameters

**Parameter** | **Type** | **Description**  
---|---|---  
sCode | String | Check code  
`0`: pass all checks  
`1`: unmatched information  
`3`: leverage setting is not finished  
`4`: position tier or margin check is not passed  
curAcctLv | String | Account mode  
`1`: Spot mode  
`2`: Futures mode  
`3`: Multi-currency margin code  
`4`: Portfolio margin mode  
Applicable to all scenarios  
acctLv | String | Account mode  
`1`: Spot mode  
`2`: Futures mode  
`3`: Multi-currency margin code  
`4`: Portfolio margin mode  
Applicable to all scenarios  
riskOffsetType | String | ~~Risk offset type  
`1`: Spot-derivatives (USDT) risk offset  
`2`: Spot-derivatives (Crypto) risk offset  
`3`: Derivatives only mode  
`4`: Spot-derivatives (USDC) risk offset  
Applicable when acctLv is `4`, return "" for other scenarios  
If the user preset before, it will use the user's specified value; if not, the default value `3` will be applied~~(Deprecated)  
unmatchedInfoCheck | Array of objects | Unmatched information list  
Applicable when sCode is `1`, indicating there is unmatched information; return [] for other scenarios  
>> type | String | Unmatched information type  
`asset_validation`: asset validation  
`pending_orders`: order book pending orders  
`pending_algos`: pending algo orders and trading bots, such as iceberg, recurring buy and twap  
`isolated_margin`: isolated margin (quick margin and manual transfers)  
`isolated_contract`: isolated contract (manual transfers)  
`contract_long_short`: contract positions in hedge mode  
`cross_margin`: cross margin positions  
`cross_option_buyer`: cross options buyer  
`isolated_option`: isolated options (only applicable to spot mode)  
`growth_fund`: positions with trial funds  
`all_positions`: all positions  
`spot_lead_copy_only_simple_single`: copy trader and customize lead trader can only use spot mode or Futures mode  
`stop_spot_custom`: spot customize copy trading  
`stop_futures_custom`: contract customize copy trading  
`lead_portfolio`: lead trader can not switch to portfolio margin mode  
`futures_smart_sync`: you can not switch to spot mode when having smart contract sync  
`vip_fixed_loan`: vip loan  
`repay_borrowings`: borrowings  
`compliance_restriction`: due to compliance restrictions, margin trading services are unavailable  
`compliance_kyc2`: Due to compliance restrictions, margin trading services are unavailable. If you are not a resident of this region, please complete kyc2 identity verification.  
>> totalAsset | String | Total assets  
Only applicable when type is `asset_validation`, return "" for other scenarios  
>> posList | Array of strings | Unmatched position list (posId)  
Applicable when type is related to positions, return [] for other scenarios  
posList | Array of objects | Cross margin contract position list  
Applicable when curAcctLv is `4`, acctLv is `2/3` and user has cross margin contract positions  
Applicable when sCode is `0/3/4`  
> posId | String | Position ID  
> lever | String | Leverage of cross margin contract positions after switch  
posTierCheck | Array of objects | Cross margin contract positions that don't pass the position tier check  
Only applicable when sCode is `4`  
> instFamily | String | Instrument family  
> instType | String | Instrument type  
`SWAP`  
`FUTURES`  
`OPTION`  
> pos | String | Quantity of position  
> lever | String | Leverage  
> maxSz | String | If acctLv is `2/3`, it refers to the maximum position size allowed at the current leverage. If acctLv is `4`, it refers to the maximum position limit for cross-margin positions under the PM mode.  
mgnBf | Object | The margin related information before switching account mode  
Applicable when sCode is `0/4`, return null for other scenarios  
> acctAvailEq | String | Account available equity in USD  
Applicable when curAcctLv is `3/4`, return "" for other scenarios  
> mgnRatio | String | Maintenance Margin ratio in USD  
Applicable when curAcctLv is `3/4`, return "" for other scenarios  
> details | Array of objects | Detailed information  
Only applicable when curAcctLv is `2`, return "" for other scenarios  
>> ccy | String | Currency  
>> availEq | String | Available equity of currency  
>> mgnRatio | String | Maintenance margin ratio of currency  
mgnAft | Object | The margin related information after switching account mode  
Applicable when sCode is `0/4`, return null for other scenarios  
> acctAvailEq | String | Account available equity in USD  
Applicable when acctLv is `3/4`, return "" for other scenarios  
> mgnRatio | String | Maintenance margin ratio in USD  
Applicable when acctLv is `3/4`, return "" for other scenarios  
> details | Array of objects | Detailed information  
Only applicable when acctLv is `2`, return "" for other scenarios  
>> ccy | String | Currency  
>> availEq | String | Available equity of currency  
>> mgnRatio | String | Maintenance margin ratio of currency

---

# 预检查账户模式切换

获取账户模式切换预检查相关信息

#### 限速：5次/2s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/account/set-account-switch-precheck`

> 请求示例
    
    
    GET /api/v5/account/set-account-switch-precheck?acctLv=3
    
    

#### 请求参数

**参数名** | **类型** | **是否必须** | **描述**  
---|---|---|---  
acctLv | String | 是 | 账户模式  
`1`: 现货模式  
`2`: 合约模式  
`3`: 跨币种保证金模式  
`4`: 组合保证金模式  
  
> 返回结果: 合约模式->跨币种，需要现在网页或移动端完成答题
    
    
    {
        "code": "51070",
        "data": [],
        "msg": "您当前尚未达到升级至该账户模式的要求，请先在官方网站或APP完成账户模式的升级。"
    }
    

> 返回结果: 合约模式->跨币种，有不兼容信息。sCode 1
    
    
    {
        "code": "0",
        "data": [
            {
                "acctLv": "3",
                "curAcctLv": "1",
                "mgnAft": null,
                "mgnBf": null,
                "posList": [],
                "posTierCheck": [],
                "riskOffsetType": "",
                "sCode": "1",
                "unmatchedInfoCheck": [
                    {
                        "posList": [],
                        "totalAsset": "",
                        "type": "repay_borrowings"
                    }
                ]
            }
        ],
        "msg": ""
    }
    

> 返回结果: 组合保证金->跨币种，未进行杠杆设置，展示用户全部合约全仓仓位。sCode 3
    
    
    {
        "code": "0",
        "data": [
            {
                "acctLv": "3",
                "curAcctLv": "4",
                "mgnAft": null,
                "mgnBf": null,
                "posList": [
                    {
                        "lever": "50",
                        "posId": "2005456500916518912"
                    },
                    {
                        "lever": "10",
                        "posId": "2005456108363218944"
                    },
                    {
                        "lever": "100",
                        "posId": "2005456332909477888"
                    },
                    {
                        "lever": "1",
                        "posId": "2005456415990251520"
                    }
                ],
                "posTierCheck": [],
                "riskOffsetType": "",
                "sCode": "3",
                "unmatchedInfoCheck": []
            }
        ],
        "msg": ""
    }
    

> 返回结果: 组合保证金->跨币种，已进行杠杆设置，将全部杠杆倍数设置为50，通过梯度档位及保证金校验。sCode 0
    
    
    {
        "code": "0",
        "data": [
            {
                "acctLv": "3",
                "curAcctLv": "4",
                "mgnAft": {
                    "acctAvailEq": "106002.2061970689",
                    "details": [],
                    "mgnRatio": "148.1652396878421"
                },
                "mgnBf": {
                    "acctAvailEq": "77308.89735228613",
                    "details": [],
                    "mgnRatio": "4.460069474634038"
                },
                "posList": [
                    {
                        "lever": "50",
                        "posId": "2005456500916518912"
                    },
                    {
                        "lever": "50",
                        "posId": "2005456108363218944"
                    },
                    {
                        "lever": "50",
                        "posId": "2005456332909477888"
                    },
                    {
                        "lever": "50",
                        "posId": "2005456415990251520"
                    }
                ],
                "posTierCheck": [],
                "riskOffsetType": "",
                "sCode": "0",
                "unmatchedInfoCheck": []
            }
        ],
        "msg": ""
    }
    
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
sCode | String | 校验码  
`0`：通过所有验证  
`1`：有不兼容信息  
`3`：未进行杠杆设置  
`4`：梯度档位或保证金校验未通过  
curAcctLv | String | 当前账户模式  
`1`: 现货模式  
`2`: 合约模式  
`3`: 跨币种保证金模式  
`4`: 组合保证金模式  
所有情况下均返回  
acctLv | String | 新账户模式  
`1`: 现货模式  
`2`: 合约模式  
`3`: 跨币种保证金模式  
`4`: 组合保证金模式  
所有情况下均返回  
riskOffsetType | String | ~~风险对冲模式  
`1`：现货对冲(USDT)  
`2`：现货对冲(币)  
`3`：衍生品对冲  
`4`：现货对冲(USDC)  
acctLv为`4`时返回，其余情况下返回""  
若用户有设置，则为用户的设置值；若没有设置，则为默认值~~（已弃用）  
unmatchedInfoCheck | Array of objects | 包含不匹配信息对象的列表  
仅在sCode为`1`，有不兼容信息时返回，其他情况返回[]  
>> type | String | 不匹配信息类型  
`asset_validation`：资产校验  
`pending_orders`：撮合挂单  
`pending_algos`：策略挂单，冰山、时间加权、定投等  
`isolated_margin`：杠杆逐仓一键借币及自主划转  
`isolated_contract`：合约逐仓自主划转  
`contract_long_short`：合约开平模式  
`cross_margin`：杠杆全仓开仓划转  
`cross_option_buyer`：期权全仓买方  
`isolated_option`：期权逐仓 （仅适用于简单账户）  
`growth_fund`：体验金仓位  
`all_positions`：所有仓位  
`spot_lead_copy_only_simple_single`：带单和自定义跟单员只能使用现货或合约模式  
`stop_spot_custom`：停止现货自定义跟单  
`stop_futures_custom`：停止合约自定义跟单  
`lead_portfolio`：身为带单员，您不能切换到组合保证金账户模式  
`futures_smart_sync`：您存在合约智能跟单，无法切换到现货模式  
`repay_borrowings`：存在借币  
`compliance_restriction`：合规，无法使用保证金交易相关服务  
`compliance_kyc2`：合规，无法使用保证金交易相关服务，如果您不是该地区居民，请进行KYC2身份认证  
>> totalAsset | String | 总资产  
仅在type为`asset_validation`时返回，其他情况都为""  
>> posList | Array of strings | 不匹配仓位列表，返回持仓ID  
在type为仓位相关枚举值时返回，其他情况都为[]  
posList | Array of objects | 合约全仓仓位列表  
适用于curAcctLv为`4`，acctLv为`2/3`，且用户具有全仓合约仓位的情况  
在sCode为`0/3/4`的情况下返回  
> posId | String | 持仓ID  
> lever | String | 切换后的全仓仓位杠杆倍数  
posTierCheck | Array of objects | 未满足梯度档位校验全仓仓位的列表  
仅在sCode为`4`时返回  
> instFamily | String | 交易品种  
> instType | String | 产品类型  
`SWAP`：永续合约  
`FUTURES`：交割合约  
`OPTION`：期权  
> pos | String | 持仓量  
> lever | String | 杠杆倍数  
> maxSz | String | 若acctLv为`2/3`，目标账户模式为合约、跨币种，则为当前杠杆倍数下的最大持仓张数；若acctLv为`4`，目标账户模式为组合保证金，则为PM全仓最大持仓量上限  
mgnBf | Object | 切换账户模式前的保证金相关信息  
在sCode为`0/4`时返回，其他时候为null  
> acctAvailEq | String | 美金层面可用保证金  
在curAcctLv为`3/4`时返回，其他情况返回""  
> mgnRatio | String | 美金层面维持保证金率  
在curAcctLv为`3/4`时返回，其他情况返回""  
> details | Array of objects | 各币种资产详细信息  
仅在curAcctLv为`2`时返回，其他情况返回[]  
>> ccy | String | 币种  
>> availEq | String | 币种维度可用保证金  
>> mgnRatio | String | 币种维度全仓维持保证金率  
mgnAft | Object | 切换账户模式后的保证金相关信息  
在sCode为`0/4`时返回，其他时候为null  
> acctAvailEq | String | 美金层面可用保证金  
在acctLv为`3/4`时返回，其他情况返回""  
> mgnRatio | String | 美金层面维持保证金率  
在acctLv为`3/4`时返回，其他情况返回""  
> details | Array of objects | 各币种资产详细信息  
仅在acctLv为`2`时返回，其他情况返回""  
>> ccy | String | 币种  
>> availEq | String | 币种维度可用保证金  
>> mgnRatio | String | 币种维度全仓维持保证金率