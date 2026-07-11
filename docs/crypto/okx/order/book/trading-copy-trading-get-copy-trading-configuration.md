---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-copy-trading-get-copy-trading-configuration
anchor_id: order-book-trading-copy-trading-get-copy-trading-configuration
api_type: API
updated_at: 2026-07-11 19:13:09.417021
---

# GET / Copy trading configuration

Public endpoint. Retrieve copy trading parameter configuration information of copy settings  
  
#### Rate limit: 5 requests per 2 seconds

#### Rate limit rule: IP

#### Permission: Read

#### HTTP request

`GET /api/v5/copytrading/public-config`

> Request example
    
    
    GET /api/v5/copytrading/public-config?instType=SWAP
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instType | String | No | Instrument type  
`SWAP`, the default value  
  
> Response example
    
    
    {
        "code": "0",
        "data": [
            {
                "maxCopyAmt": "1000",
                "maxCopyRatio": "100",
                "maxCopyTotalAmt": "30000",
                "maxSlRatio": "0.75",
                "maxTpRatio": "1.5",
                "minCopyAmt": "20",
                "minCopyRatio": "0.01"
            }
        ],
        "msg": ""
    }
    

#### Response parameters

**Parameter** | **Type** | **Description**  
---|---|---  
maxCopyAmt | String | Maximum copy amount per order in USDT when you are using copy mode `fixed_amount`  
minCopyAmt | String | Minimum copy amount per order in USDT when you are using copy mode `fixed_amount`  
maxCopyTotalAmt | String | Maximum copy total amount under the certain lead trader, the minimum is the same with `minCopyAmt`  
minCopyRatio | String | Minimum ratio per order when you are using copy mode `ratio_copy`  
maxCopyRatio | String | Maximum ratio per order when you are using copy mode `ratio_copy`  
maxTpRatio | String | Maximum ratio of taking profit per order, the minimum is 0  
maxSlRatio | String | Maximum ratio of stopping loss per order, the minimum is 0

---

# GET / 获取跟单配置信息

公共接口，获取跟单设置时的参数配置信息  
  
#### 限速：5次/2s

#### 限速规则：IP

#### 权限：读取

#### HTTP请求

`GET /api/v5/copytrading/public-config`

> 请求示例
    
    
    GET /api/v5/copytrading/public-config?instType=SWAP
    
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instType | String | 否 | 产品类型  
`SWAP`：永续合约，默认值  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "maxCopyAmt": "1000",
                "maxCopyRatio": "100",
                "maxCopyTotalAmt": "30000",
                "maxSlRatio": "0.75",
                "maxTpRatio": "1.5",
                "minCopyAmt": "20",
                "minCopyRatio": "0.01"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
maxCopyAmt | String | 固定金额跟单时，单笔最大跟随金额  
minCopyAmt | String | 固定金额跟单时，单笔最小跟随金额  
maxCopyTotalAmt | String | 最大跟单金额（针对单个带单员），最小跟单金额同`minCopyAmt`  
minCopyRatio | String | 比例跟单的单笔最小比率  
maxCopyRatio | String | 比例跟单的单笔最大比率  
maxTpRatio | String | 单笔最大止盈比率，最小为 0  
maxSlRatio | String | 单笔最大止损比率，最小为 0