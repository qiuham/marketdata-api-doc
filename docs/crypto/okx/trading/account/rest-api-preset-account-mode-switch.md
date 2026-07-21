---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#trading-account-rest-api-preset-account-mode-switch
anchor_id: trading-account-rest-api-preset-account-mode-switch
api_type: REST
updated_at: 2026-07-21 19:25:23.953364
---

# Preset account mode switch

Pre-set the required information for account mode switching. When switching from `Portfolio margin mode` back to `Futures mode` / `Multi-currency margin mode`, and if there are existing cross-margin contract positions, it is mandatory to pre-set leverage.  
  
If the user does not follow the required settings, they will receive an error message during the pre-check or when setting the account mode.

#### Rate limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/account/account-level-switch-preset`

> Request example
    
    
    # 1. Futures mode -> Multi-currency margin mode
    POST /api/v5/account/account-level-switch-preset
    {
        "acctLv": "3"
    }
    
    # 2. Multi-currency margin mode -> Futures mode
    POST /api/v5/account/account-level-switch-preset
    {
        "acctLv": "2"
    }
    
    # 3. Portfolio margin mode -> Futures mode/Multi-currency margin mode, the user have cross-margin contract position and lever is required
    POST /api/v5/account/account-level-switch-preset
    {
        "acctLv": "2",
        "lever": "10"
    }
    
    # 4. Portfolio margin mode -> Futures mode/Multi-currency margin mode, the user doesn't have cross-margin contract position and lever is not required
    POST /api/v5/account/account-level-switch-preset
    {
        "acctLv": "3"
    }
    
    

#### Request parameters

**Parameter** | **Type** | **Required** | **Description**  
---|---|---|---  
acctLv | String | Yes | Account mode  
`2`: Futures mode  
`3`: Multi-currency margin code  
`4`: Portfolio margin mode  
lever | String | Optional | Leverage  
Required when switching from Portfolio margin mode to `Futures mode` or `Multi-currency margin mode`, and the user holds cross-margin positions.  
riskOffsetType | String | Optional | ~~Risk offset type  
`1`: Spot-derivatives (USDT) risk offset  
`2`: Spot-derivatives (Crypto) risk offset  
`3`: Derivatives only mode  
`4`: Spot-derivatives (USDC) risk offset  
Applicable when switching from Futures mode or Multi-currency margin mode to Portfolio margin mode.~~(Deprecated)  
  
> Response example 1. Futures mode -> Multi-currency margin mode
    
    
    {
        "acctLv": "3",
        "curAcctLv": "2",
        "lever": "",
        "riskOffsetType": ""
    }
    

> Response example 2. Multi-currency margin mode -> Futures mode
    
    
    {
        "acctLv": "2",
        "curAcctLv": "3",
        "lever": "",
        "riskOffsetType": ""
    }
    

> Response example 3. Portfolio margin mode -> Futures mode/Multi-currency margin mode
    
    
    {
        "acctLv": "2",
        "curAcctLv": "4",
        "lever": "10",
        "riskOffsetType": ""
    }
    

> Response example 4. Portfolio margin mode -> Futures mode/Multi-currency margin mode
    
    
    {
        "acctLv": "3",
        "curAcctLv": "4",
        "lever": "",
        "riskOffsetType": ""
    }
    

#### Response parameters

**Parameter** | **Type** | **Description**  
---|---|---  
curAcctLv | String | Current account mode  
acctLv | String | Account mode after switch  
lever | String | The leverage user preset for cross-margin positions  
riskOffsetType | String | ~~The risk offset type user preset~~(Deprecated)  
  
lever: When switching from Portfolio margin mode to Futures mode or Multi-currency margin mode, if the user holds cross-margin positions, this parameter must be provided; otherwise, error code 50014 will occur. The maximum allowable value for this parameter is determined by the smallest maximum leverage based on current position sizes under the target mode. For example, if a user in PM mode holds three cross-margin positions, with maximum allowable leverage of 20x, 50x, and 100x respectively, the maximum leverage it can set is 20x.

---

# 预设置账户模式切换

预设置账户模式切换的必要信息，若由`组合保证金模式`切换到`合约模式`/`跨币种保证金模式`，且存在全仓交割、永续仓位，则必须预设置lever，令所有仓位具有相同杠杆倍数。  
  
若用户未按照规定进行设置，在预检查或设置账户模式时将接收到报错或提示信息。

#### 限速：5次/2s

#### 限速规则：User ID

#### HTTP请求

`POST /api/v5/account/account-level-switch-preset`

> 请求示例
    
    
    # 1. 合约模式 -> 跨币种
    POST /api/v5/account/account-level-switch-preset
    body
    {
        "acctLv": "3"
    }
    
    # 2. 跨币种 -> 合约模式
    POST /api/v5/account/account-level-switch-preset
    body
    {
        "acctLv": "2"
    }
    
    # 3. 组合保证金 -> 合约模式/跨币种，且有全仓合约仓位，则必须传入lever
    POST /api/v5/account/account-level-switch-preset
    body
    {
        "acctLv": "2",
        "lever": "10"
    }
    
    # 4. 组合保证金 -> 合约模式/跨币种，没有全仓合约仓位，则不需传入lever，不进行校验
    POST /api/v5/account/account-level-switch-preset
    body
    {
        "acctLv": "3"
    }
    
    

#### 请求参数

**参数名** | **类型** | **是否必须** | **描述**  
---|---|---|---  
acctLv | String | 是 | 账户模式  
`2`: 合约模式  
`3`: 跨币种保证金模式  
`4`: 组合保证金模式  
lever | String | 可选 | 在`组合保证金模式`向`合约模式/跨币种保证金模式`切换，且用户有全仓仓位时，必须传入  
riskOffsetType | String | 可选 | ~~风险对冲模式  
`1`：现货对冲(USDT)  
`2`：现货对冲(币)  
`3`：衍生品对冲（未开启现货对冲）  
`4`：现货对冲(USDC)  
适用于`合约模式/跨币种保证金模式`向`组合保证金模式`切换~~（已弃用）  
  
> 返回结果 1. 合约模式 -> 跨币种
    
    
    {
        "acctLv": "3",
        "curAcctLv": "2",
        "lever": "",
        "riskOffsetType": ""
    }
    

> 返回结果 2. 跨币种 -> 合约模式
    
    
    {
        "acctLv": "2",
        "curAcctLv": "3",
        "lever": "",
        "riskOffsetType": ""
    }
    

> 返回结果 3. 组合保证金 -> 合约模式/跨币种
    
    
    {
        "acctLv": "2",
        "curAcctLv": "4",
        "lever": "10",
        "riskOffsetType": ""
    }
    

> 返回结果 4. 组合保证金 -> 合约模式/跨币种，没有全仓合约仓位，则不需传入lever，不进行校验
    
    
    {
        "acctLv": "3",
        "curAcctLv": "4",
        "lever": "",
        "riskOffsetType": ""
    }
    
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
curAcctLv | String | 当前账户类型  
acctLv | String | 切换后的账户类型  
lever | String | 用户预设置的全仓合约仓位杠杆倍数  
riskOffsetType | String | ~~用户预设置的风险对冲模式~~ （已弃用）  
  
lever：`保证金模式`向`合约模式`/`跨币种保证金模式`切换，且用户有全仓合约仓位，则必须传入此参数，不传则报错50014。传此参数，允许设置的最大值为各个合约的仓位大小对应合约模式/跨币种账户模式下最大杠杆倍数的最小值。例如，用户在PM模式下，有三个全仓仓位，当前仓位大小对应目标账户模式下最大杠杆倍数分别为20x/50x/100x，那么用户能够设置的最大杠杆倍数为20x。