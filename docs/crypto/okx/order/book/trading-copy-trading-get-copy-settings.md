---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-copy-trading-get-copy-settings
anchor_id: order-book-trading-copy-trading-get-copy-settings
api_type: API
updated_at: 2026-07-06 19:53:21.191328
---

# GET / Copy settings

Retrieve the copy settings about certain lead trader.  
  
#### Rate limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP request

`GET /api/v5/copytrading/copy-settings`

> Request example
    
    
    GET /api/v5/copytrading/copy-settings?instType=SWAP&uniqueCode=25CD5A80241D6FE6
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instType | String | No | Instrument type  
`SWAP`  
uniqueCode | String | Yes | Lead trader unique code  
A combination of case-sensitive alphanumerics, all numbers and the length is 16 or 18 characters, e.g. 213E8C92DC61EFAC (16 characters) or 381749205163847291 (18 characters)  
  
> Response example
    
    
    {
        "code": "0",
        "data": [
            {
                "ccy": "USDT",
                "copyAmt": "",
                "copyInstIdType": "copy",
                "copyMgnMode": "isolated",
                "copyMode": "ratio_copy",
                "copyRatio": "1",
                "copyState": "1",
                "copyTotalAmt": "500",
                "instIds": [
                    {
                        "enabled": "1",
                        "instId": "ADA-USDT-SWAP"
                    },
                    {
                        "enabled": "1",
                        "instId": "YFII-USDT-SWAP"
                    }
                ],
                "slRatio": "",
                "slTotalAmt": "",
                "subPosCloseType": "copy_close",
                "tpRatio": "",
                "tag": ""
            }
        ],
        "msg": ""
    }
    

#### Response parameters

**Parameter** | **Type** | **Description**  
---|---|---  
copyMode | String | Copy mode  
`fixed_amount` `ratio_copy`  
copyAmt | String | Copy amount in USDT per order.  
copyRatio | String | Copy ratio per order.  
copyTotalAmt | String | Maximum total amount in USDT.   
The maximum total amount you'll invest at any given time across all orders in this copy trade  
tpRatio | String | Take profit per order. 0.1 represents 10%  
slRatio | String | Stop loss per order. 0.1 represents 10%  
copyInstIdType | String | Copy contract type setted  
`custom`: custom by `instId` which is required；  
`copy`: Keep your contracts consistent with this trader by automatically adding or removing contracts when they do  
instIds | Array of objects | Instrument list. It will return all lead contracts of the lead trader  
> instId | String | Instrument ID  
> enabled | String | Whether copying this `instId`  
`0` `1`  
slTotalAmt | String | Total stop loss in USDT for trader.  
subPosCloseType | String | Action type for open positions  
`market_close`: immediately close at market price  
`copy_close`：close when trader closes  
`manual_close`: close manually  
copyMgnMode | String | Copy margin mode  
`cross`: cross  
`isolated`: isolated  
`copy`: Use the same margin mode as lead trader when opening positions  
ccy | String | Margin currency  
copyState | String | Current copy state   
`0`: non-copy, `1`: copy  
tag | String | Order tag

---

# GET / 获取跟单设置

获取针对某个交易员的跟单设置  
  
#### 限速：5次/2s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/copytrading/copy-settings`

> 请求示例
    
    
    GET /api/v5/copytrading/copy-settings?instType=SWAP&uniqueCode=25CD5A80241D6FE6
    
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instType | String | 否 | 产品类型  
`SWAP`：永续合约，默认值  
uniqueCode | String | 是 | 带单交易员唯一标识码。  
数字加字母组合 长度为16或18位，如：213E8C92DC61EFAC（16位）或381749205163847291（18位）  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "ccy": "USDT",
                "copyAmt": "",
                "copyInstIdType": "copy",
                "copyMgnMode": "isolated",
                "copyMode": "ratio_copy",
                "copyRatio": "1",
                "copyState": "1",
                "copyTotalAmt": "500",
                "instIds": [
                    {
                        "enabled": "1",
                        "instId": "ADA-USDT-SWAP"
                    },
                    {
                        "enabled": "1",
                        "instId": "YFII-USDT-SWAP"
                    }
                ],
                "slRatio": "",
                "slTotalAmt": "",
                "subPosCloseType": "copy_close",
                "tpRatio": "",
                "tag": ""
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
copyMode | String | 跟单模式  
`fixed_amount`: 固定金额跟单  
`ratio_copy`: 比例跟单  
copyAmt | String | 单笔跟随金额，单位为 USDT  
copyRatio | String | 跟单比例  
copyTotalAmt | String | 跟单该交易员投入的最大跟单金额，单位为USDT  
tpRatio | String | 单笔止盈百分比，0.1 代表10%  
slRatio | String | 单笔止损百分比，0.1 代表10%  
copyInstIdType | String | 跟单合约设置的类型  
`custom`: 用户自定义   
`copy`: 跟随交易员，自动同步交易员的合约变更  
instIds | Array of objects | 可跟单的合约列表，会返回交易员所有带单合约  
> instId | String | 产品 ID  
> enabled | String | 是否在跟单  
`0`: 没有在跟单 `1`: 在跟单  
slTotalAmt | String | 跟单止损总金额，单位为 USDT  
subPosCloseType | String | 剩余仓位处理方式  
`market_close`: 立即市价全平  
`copy_close`：跟随交易员平仓  
`manual_close`: 手动处理  
copyMgnMode | String | 跟单时的保证金模式  
`cross`: 全仓；  
`isolated`: 逐仓；  
`copy`: 跟随带单员  
ccy | String | 保证金币种  
copyState | String | 当前跟单状态   
`0`: 没在跟单  
`1`：在跟单  
tag | String | 订单标签