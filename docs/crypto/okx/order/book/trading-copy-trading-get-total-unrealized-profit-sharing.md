---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-copy-trading-get-total-unrealized-profit-sharing
anchor_id: order-book-trading-copy-trading-get-total-unrealized-profit-sharing
api_type: API
updated_at: 2026-07-07 19:42:20.641870
---

# GET / Total unrealized profit sharing

The leading trader gets the total unrealized amount of profit shared.  
  
#### Rate limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP request

`GET /api/v5/copytrading/total-unrealized-profit-sharing`

> Request example
    
    
    GET /api/v5/copytrading/total-unrealized-profit-sharing
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instType | String | No | Instrument type  
`SWAP`, the default value.  
  
> Response example
    
    
    {
        "code": "0",
        "data": [
            {
                "profitSharingTs": "1705852800000",
                "totalUnrealizedProfitSharingAmt": "0.114402985553185"
            }
        ],
        "msg": ""
    }
    

#### Response parameters

**Parameter** | **Type** | **Description**  
---|---|---  
profitSharingTs | String | The settlement time for the total unrealized profit sharing amount. Unix timestamp format in milliseconds, e.g.1597026383085  
totalUnrealizedProfitSharingAmt | String | Total unrealized profit sharing amount

---

# GET / 交易员待分润汇总

交易员获取待分润汇总。  
  
#### 限速：5次/2s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/copytrading/total-unrealized-profit-sharing`

> 请求示例
    
    
    GET /api/v5/copytrading/total-unrealized-profit-sharing
    
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instType | String | 否 | 产品类型  
SWAP：永续合约，默认值  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "profitSharingTs": "1705852800000",
                "totalUnrealizedProfitSharingAmt": "0.114402985553185"
            }
        ],
        "msg": ""
    }
    
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
profitSharingTs | String | 当前周期待分润总额的结算时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
totalUnrealizedProfitSharingAmt | String | 待分润总额