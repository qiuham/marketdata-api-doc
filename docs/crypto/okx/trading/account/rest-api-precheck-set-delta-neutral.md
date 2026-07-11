---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#trading-account-rest-api-precheck-set-delta-neutral
anchor_id: trading-account-rest-api-precheck-set-delta-neutral
api_type: REST
updated_at: 2026-07-11 19:12:20.518818
---

# Precheck set delta neutral

#### Rate limit: 1 request per 2 seconds  
  
#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/account/precheck-set-delta-neutral`

> Request example
    
    
    GET /api/v5/account/precheck-set-delta-neutral?stgyType=1
    
    

#### Request parameters

**Parameter** | **Type** | **Required** | **Description**  
---|---|---|---  
stgyType | String | Yes | Strategy type  
`0`: general strategy  
`1`: delta neutral strategy  
  
> Response example
    
    
    {
        "code": "0",
        "data": [
            {
                "unmatchedInfoCheck": [
                    {
                        "posList": [],
                        "ordList": [],
                        "deltaLever": "",
                        "type": "spot_mode"
                    },
                   {
                        "posList": ["123","123","123"],
                        "ordList": [],
                        "deltaLever": "",
                        "type": "isolated_margin"
                    }
                ]
            }
        ],
        "msg": ""
    }
    
    

#### Response parameters

**Parameter** | **Type** | **Description**  
---|---|---  
unmatchedInfoCheck | Array of objects | Unmatched information list  
> type | String | Unmatched information type  
`spot_mode`: DNA is not supported under spot mode  
`futures_mode`: DNA is not supported under futures mode  
`isolated_margin`: Isolated margin position is not supported in DNA  
`isolated_contract`: Isolated contract position is not supported in DNA  
`positions_options`: Options are not supported in DNA  
`isolated_pending_orders`: Isolated pending orders are not supported in DNA  
`pending_orders_options`: Pending options orders are not supported in DNA  
`trading_bot`: Trading bot is not supported in DNA  
`repay_borrowings`: borrowing in the targeted strategy will exceed the main account borrowing limit after the switch. Repay liabilities and try again.  
`loan`: Flexible loan and DNA cannot be used at the same time   
`delta_risk`: delta risk check failed, lower delta and try again  
`collateral_all`: all coins must be set as collateral in DNA  
`risk_unit_type`: The account is part of a delta neutral risk unit and cannot be switched to general mode. Remove it from the risk unit before switching strategies.  
> deltaLever | String | Delta leverage  
Applicable when type is `delta_risk`  
> ordList | Array of strings | Unmatched order list, order ID  
Applicable when type is `isolated_pending_orders`/`pending_orders_options`  
> posList | Array of strings | Unmatched position list, position ID  
Applicable when type is `isolated_margin`/`isolated_contract`/`positions_options`

---

# 设置Delta中性预检查

#### **限速：1次/2s**  
  
#### **限速规则：User ID**

#### **HTTP请求**

`GET /api/v5/account/precheck-set-delta-neutral`

> 请求示例
    
    
    GET /api/v5/account/precheck-set-delta-neutral?stgyType=1
    
    

#### 请求参数

**参数名** | **类型** | **是否必须** | **描述**  
---|---|---|---  
stgyType | String | Yes | 策略类型  
`0`：普通策略模式  
`1`：delta 中性策略模式  
  
> 返回示例
    
    
    {
        "code": "0",
        "data": [
            {
                "unmatchedInfoCheck": [
                    {
                        "posList": [],
                        "ordList": [],
                        "deltaLever": "",
                        "type": "spot_mode"
                    },
                   {
                        "posList": ["123","123","123"],
                        "ordList": [],
                        "deltaLever": "",
                        "type": "isolated_margin"
                    }
                ]
            }
        ],
        "msg": ""
    }
    
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
unmatchedInfoCheck | Array of objects | 包含不匹配信息对象的列表  
> type | String | 不匹配信息类型  
`spot_mode`：delta 中性策略模式不支持现货模式  
`futures_mode`：delta 中性策略模式不支持合约模式  
`isolated_margin`：delta 中性策略模式不支持逐仓杠杆仓位  
`isolated_contract`：delta 中性策略模式不支持逐仓合约仓位  
`positions_options`：delta 中性策略模式不支持期权仓位  
`isolated_pending_orders`：delta 中性策略模式不支持逐仓挂单  
`pending_orders_options`：delta 中性策略模式不支持期权挂单  
`trading_bot`：delta 中性策略模式不支持策略交易  
`repay_borrowings`：在转换后，在目前策略下的负债量超过母账户维度借币限额，请偿还负债后重试  
`loan`：不支持delta 中性策略模式使用活期借币  
`delta_risk`：Delta风险检查失败，降低delta后重试  
`collateral_all`：delta 中性策略模式下，所有币种必要被设置为质押币  
`risk_unit_type`：该账户在Delta中性风险单元内，无法切换至通用模式。请在切换策略前将其从风险单元中移除。  
> deltaLever | String | Delta权益比率  
仅适用于type为`delta_risk`  
> ordList | Array of strings | 不匹配订单列表，返回订单ID  
在type为`isolated_pending_orders`/`pending_orders_options`时适用  
> posList | Array of strings | 不匹配仓位列表，返回仓位ID  
在type为`isolated_margin`/`isolated_contract`/`positions_options`时适用