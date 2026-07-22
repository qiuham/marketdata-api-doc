---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-copy-trading-post-place-lead-stop-order
anchor_id: order-book-trading-copy-trading-post-place-lead-stop-order
api_type: API
updated_at: 2026-07-22 19:19:41.352087
---

# POST / Place lead stop order

Set TP/SL for the current lead position that are not closed.  
  
#### Rate limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/copytrading/algo-order`

> Request example
    
    
    POST /api/v5/copytrading/algo-order
    body
    {
        "subPosId": "518541406042591232",
        "tpTriggerPx": "10000"
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instType | String | No | Instrument type  
`SPOT`  
`SWAP`, the default value  
subPosId | String | Yes | Lead position ID  
tpTriggerPx | String | Conditional | Take-profit trigger price. Take-profit order price will be the market price after triggering. At least one of tpTriggerPx and slTriggerPx must be filled  
The take profit order will be deleted if it is 0  
slTriggerPx | String | Conditional | Stop-loss trigger price. Stop-loss order price will be the market price after triggering. The stop loss order will be deleted if it is 0  
tpOrdPx | String | No | Take-profit order price  
If the price is -1, take-profit will be executed at the market price, the default is `-1`  
Only applicable to `SPOT` lead trader  
slOrdPx | String | No | Stop-loss order price  
If the price is -1, stop-loss will be executed at the market price, the default is `-1`  
Only applicable to `SPOT` lead trader  
tpTriggerPxType | String | No | Take-profit trigger price type   
  
`last`: last price  
`index`: index price  
`mark`: mark price   
Default is `last`  
slTriggerPxType | String | No | Stop-loss trigger price type  
`last`: last price   
`index`: index price   
`mark`: mark price   
Default is last  
tag | String | No | Order tag  
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 16 characters.  
  
> Response example
    
    
    {
        "code": "0",
        "data": [
            {
                "subPosId": "518560559046594560",
                "tag":""
            }
        ],
        "msg": ""
    }
    

#### Response parameters

**Parameter** | **Type** | **Description**  
---|---|---  
subPosId | String | Lead position ID  
tag | String | Order tag

---

# POST / 带单或跟单仓位止盈止损

为当前未平仓的带单仓位设置止盈止损。  
  
#### 限速：20次/2s

#### 限速规则：User ID

#### HTTP请求

`POST /api/v5/copytrading/algo-order`

> 请求示例
    
    
    POST /api/v5/copytrading/algo-order
    body
    {
        "subPosId": "518541406042591232",
        "tpTriggerPx": "10000"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instType | String | 否 | 产品类型  
SPOT：币币  
SWAP：永续合约，默认值  
subPosId | String | 是 | 带单或者跟单仓位ID  
tpTriggerPx | String | 可选 | 止盈触发价，tpTriggerPx 和 slTriggerPx 至少需要填写一个  
如果止盈触发价为0，那代表删除止盈。  
slTriggerPx | String | 可选 | 止损触发价，  
如果止损触发价为0，那代表删除止损  
tpOrdPx | String | 否 | 止盈委托价  
委托价格为-1时，执行市价止盈，默认为市价止盈  
仅适用于现货交易员  
slOrdPx | String | 否 | 止损委托价  
委托价格为-1时，执行市价止损，默认为市价止损  
仅适用于现货交易员  
tpTriggerPxType | String | 否 | 止盈触发价类型  
`last`：最新价格  
`index`：指数价格  
`mark`：标记价格  
默认为last  
slTriggerPxType | String | 否 | 止损触发价类型  
`last`：最新价格  
`index`：指数价格  
`mark`：标记价格  
默认为last  
tag | String | 否 | 订单标签  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字，且长度在1-16位之间。  
subPosType | String | 否 | 数据的类型  
`lead`: 带单，默认值  
`copy`: 跟单  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "subPosId": "518560559046594560",
                "tag":""
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
subPosId | String | 带单或者跟单仓位ID  
tag | String | 订单标签