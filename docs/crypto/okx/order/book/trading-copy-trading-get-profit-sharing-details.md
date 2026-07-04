---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-copy-trading-get-profit-sharing-details
anchor_id: order-book-trading-copy-trading-get-profit-sharing-details
api_type: API
updated_at: 2026-07-04 19:38:09.110001
---

# GET / Profit sharing details

The leading trader gets profits shared details for the last 3 months.  
  
#### Rate limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP request

`GET /api/v5/copytrading/profit-sharing-details`

> Request example
    
    
    GET /api/v5/copytrading/profit-sharing-details?limit=2
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instType | String | No | Instrument type  
`SPOT`  
`SWAP`  
It returns all types by default.  
after | String | No | Pagination of data to return records earlier than the requested `profitSharingId`  
before | String | No | Pagination of data to return records newer than the requested `profitSharingId`  
limit | String | No | Number of results per request. Maximum is 100. Default is 100.  
  
> Response example
    
    
    {
        "code": "0",
        "data": [
            {
                "ccy": "USDT",
                "nickName": "Potato",
                "profitSharingAmt": "0.00536",
                "profitSharingId": "148",
                "portLink": "",
                "ts": "1723392000000",
                "instType": "SWAP"
            },
            {
                "ccy": "USDT",
                "nickName": "Apple",
                "profitSharingAmt": "0.00336",
                "profitSharingId": "20",
                "portLink": "",
                "ts": "1723392000000",
                "instType": "SWAP"
            }
        ],
        "msg": ""
    }
    

#### Response parameters

**Parameter** | **Type** | **Description**  
---|---|---  
ccy | String | The currency of profit sharing.  
profitSharingAmt | String | Profit sharing amount. It would be 0 if there is no any profit sharing.  
nickName | String | Nickname of copy trader.  
profitSharingId | String | Profit sharing ID.  
instType | String | Instrument type  
portLink | String | Portrait link  
ts | String | Profit sharing time.

---

# GET / 交易员历史分润明细

交易员获取最近三个月的分润明细。  
  
#### 限速：5次/2s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/copytrading/profit-sharing-details`

> 请求示例
    
    
    GET /api/v5/copytrading/profit-sharing-details?limit=2
    
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instType | String | 否 | 产品类型  
SPOT：币币  
SWAP：永续合约  
默认返回所有业务线的信息  
after | String | 否 | 请求此id之前（更旧的数据）的分页内容，传的值为对应接口的`profitSharingId`  
before | String | 否 | 请求此id之后（更新的数据）的分页内容，传的值为对应接口的`profitSharingId`  
limit | String | 否 | 分页返回的结果集数量，最大为100，不填默认返回100条  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "ccy": "USDT",
                "nickName": "Potato",
                "profitSharingAmt": "0.00536",
                "profitSharingId": "148",
                "portLink": "",
                "ts": "1723392000000",
                "instType": "SWAP"
            },
            {
                "ccy": "USDT",
                "nickName": "Apple",
                "profitSharingAmt": "0.00336",
                "profitSharingId": "20",
                "portLink": "",
                "ts": "1723392000000",
                "instType": "SWAP"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
ccy | String | 分润币种  
profitSharingAmt | String | 分润额，没有分润时，默认返回0  
nickName | String | 跟单人的昵称  
profitSharingId | String | 分润ID  
instType | String | 产品类型  
SPOT：币币  
SWAP：永续合约  
portLink | String | 跟单员头像的链接地址  
ts | String | 分润时间