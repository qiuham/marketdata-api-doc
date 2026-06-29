---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-copy-trading-post-amend-profit-sharing-ratio
anchor_id: order-book-trading-copy-trading-post-amend-profit-sharing-ratio
api_type: API
updated_at: 2026-06-29 19:56:31.587899
---

# POST / Amend profit sharing ratio

It is used to amend profit sharing ratio.   
  
#### Rate limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP request

`POST /api/v5/copytrading/amend-profit-sharing-ratio`

> Request example
    
    
    POST /api/v5/copytrading/amend-profit-sharing-ratio
    body
    {
        "instType": "SWAP",
        "profitSharingRatio": "0.1"
    }
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instType | String | No | Instrument type  
`SWAP`  
profitSharingRatio | String | Yes | Profit sharing ratio.   
0.1 represents 10%  
  
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

# POST / 修改分润比例

修改分润比例  
  
#### 限速：5次/2s

#### 限速规则：User ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/copytrading/amend-profit-sharing-ratio`

> 请求示例
    
    
    POST /api/v5/copytrading/amend-profit-sharing-ratio
    body
    {
        "instType": "SWAP",
        "profitSharingRatio": "0.1"
    }
    
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instType | String | 否 | 产品类型  
`SWAP`：永续合约，默认值  
profitSharingRatio | String | 是 | 分润比例。0.1 代表10%  
  
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