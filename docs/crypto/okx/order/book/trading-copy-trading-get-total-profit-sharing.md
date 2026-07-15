---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-copy-trading-get-total-profit-sharing
anchor_id: order-book-trading-copy-trading-get-total-profit-sharing
api_type: API
updated_at: 2026-07-15 19:19:14.190281
---

# GET / Total profit sharing

The leading trader gets the total amount of profit shared since joining the platform.  
  
#### Rate limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP request

`GET /api/v5/copytrading/total-profit-sharing`

> Request example
    
    
    GET /api/v5/copytrading/total-profit-sharing
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instType | String | No | Instrument type  
`SPOT`  
`SWAP`  
It returns all types by default.  
  
> Response example
    
    
    {
        "code": "0",
        "data": [
            {
                "ccy": "USDT",
                "totalProfitSharingAmt": "0.6584928",
                "instType": "SWAP"
            }
        ],
        "msg": ""
    }
    

#### Response parameters

**Parameter** | **Type** | **Description**  
---|---|---  
ccy | String | The currency of profit sharing.  
totalProfitSharingAmt | String | Total profit sharing amount.  
instType | String | Instrument type

---

# GET / 交易员历史分润汇总

交易员获取自入驻平台以来，累计获得的总分润金额。  
  
#### 限速：5次/2s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/copytrading/total-profit-sharing`

> 请求示例
    
    
    GET /api/v5/copytrading/total-profit-sharing
    
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instType | String | 否 | 产品类型  
SPOT：币币  
SWAP：永续合约  
默认返回所有业务线的信息  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "ccy": "USDT",
                "totalProfitSharingAmt": "0.6584928",
                "instType": "SWAP"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
ccy | String | 分润币种  
totalProfitSharingAmt | String | 历史分润汇总  
instType | String | 产品类型  
SPOT：币币  
SWAP：永续合约