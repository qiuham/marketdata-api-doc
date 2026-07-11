---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-copy-trading-post-first-copy-settings
anchor_id: order-book-trading-copy-trading-post-first-copy-settings
api_type: API
updated_at: 2026-07-11 19:13:07.855387
---

# POST / First copy settings

The first copy settings for the certain lead trader. You need to first copy settings after stopping copying.  
  
#### Rate limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP request

`POST /api/v5/copytrading/first-copy-settings`

> Request example
    
    
    POST /api/v5/copytrading/first-copy-settings
    body
    {
        "instType": "SWAP",
        "uniqueCode": "25CD5A80241D6FE6",
        "copyMgnMode": "cross",
        "copyInstIdType": "copy",
        "copyMode": "ratio_copy",
        "copyRatio": "1",
        "copyTotalAmt": "500",
        "subPosCloseType": "copy_close"
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instType | String | No | Instrument type  
`SWAP`, the default value  
uniqueCode | String | Yes | Lead trader unique code  
A combination of case-sensitive alphanumerics, all numbers and the length is 16 or 18 characters, e.g. 213E8C92DC61EFAC (16 characters) or 381749205163847291 (18 characters)  
copyMgnMode | String | Yes | Copy margin mode  
`cross`: cross  
`isolated`: isolated  
`copy`: Use the same margin mode as lead trader when opening positions  
copyInstIdType | String | Yes | Copy contract type setted  
`custom`: custom by `instId` which is required；  
`copy`: Keep your contracts consistent with this trader by automatically adding or removing contracts when they do  
instId | String | Conditional | Instrument ID.   
If there are multiple instruments, separate them with commas.  
copyMode | String | No | Copy mode  
`fixed_amount`: set the same fixed amount for each order, and `copyAmt` is required；  
`ratio_copy`: set amount as a multiple of the lead trader’s order value, and `copyRatio` is required   
The default is `fixed_amount`  
copyTotalAmt | String | Yes | Maximum total amount in USDT.   
The maximum total amount you'll invest at any given time across all orders in this copy trade  
You won’t copy new orders if you exceed this amount  
copyAmt | String | Conditional | Copy amount per order in USDT.  
copyRatio | String | Conditional | Copy ratio per order.  
tpRatio | String | No | Take profit per order. 0.1 represents 10%  
slRatio | String | No | Stop loss per order. 0.1 represents 10%  
slTotalAmt | String | No | Total stop loss in USDT for trader.   
If your net loss (total profit - total loss) reaches this amount, you'll stop copying this trader  
subPosCloseType | String | Yes | Action type for open positions  
`market_close`: immediately close at market price  
`copy_close`：close when trader closes  
`manual_close`: close manually  
The default is `copy_close`  
tag | String | No | Order tag  
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 16 characters.  
  
> Response example
    
    
    {
        "code": "0",
        "data": [
            {
                "result": true
            }
        ],
        "msg": ""
    }
    

#### Response parameters

**Parameter** | **Type** | **Description**  
---|---|---  
result | Boolean | The result of setting   
`true`

---

# POST / 首次跟单设置

跟随某一交易员的首次设置，停止跟单后需先进行首次设置；  
  
  
#### 限速：5次/2s

#### 限速规则：User ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/copytrading/first-copy-settings`

> 请求示例
    
    
    POST /api/v5/copytrading/first-copy-settings
    body
    {
        "instType": "SWAP",
        "uniqueCode": "25CD5A80241D6FE6",
        "copyMgnMode": "cross",
        "copyInstIdType": "copy",
        "copyMode": "ratio_copy",
        "copyRatio": "1",
        "copyTotalAmt": "500",
        "subPosCloseType": "copy_close"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instType | String | 否 | 产品类型  
`SWAP`：永续合约，默认值  
uniqueCode | String | 是 | 带单交易员唯一标识码。  
数字加字母组合 长度为16或18位，如：213E8C92DC61EFAC（16位）或381749205163847291（18位）  
copyMgnMode | String | 是 | 跟单时的保证金模式  
`cross`: 全仓；  
`isolated`: 逐仓；  
`copy`: 跟随带单员  
copyInstIdType | String | 是 | 跟单合约设置的类型  
`custom`: 用户自定义，instId 必填；  
`copy`: 跟随交易员，自动同步交易员的合约变更  
instId | String | 可选 | 产品 ID  
可传入多条，以逗号区分  
copyMode | String | 否 | 跟单模式  
`fixed_amount`: 固定金额跟单，`copyAmt`必填；  
`ratio_copy`: 比例跟单，`copyRatio`必填   
默认是`fixed_amount`  
copyTotalAmt | String | 是 | 跟单该交易员投入的最大跟单金额，单位为USDT。  
超过该金额后将不再触发跟单行为  
copyAmt | String | 可选 | 单笔跟随金额，单位为USDT  
copyRatio | String | 可选 | 跟单比例  
tpRatio | String | 否 | 单笔止盈百分比，0.1 代表10%  
slRatio | String | 否 | 单笔止损百分比，0.1 代表10%  
slTotalAmt | String | 否 | 跟单止损总金额，单位为USDT  
净损失达到该金额时，将自动解除跟单关系  
subPosCloseType | String | 是 | 剩余仓位处理方式  
`market_close`: 立即市价全平  
`copy_close`：跟随交易员平仓  
`manual_close`: 手动处理  
默认为 `copy_close`  
tag | String | 否 | 订单标签  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字，且长度在1-16位之间。  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "result": true
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
result | Boolean | 设置结果  
`true`：设置成功