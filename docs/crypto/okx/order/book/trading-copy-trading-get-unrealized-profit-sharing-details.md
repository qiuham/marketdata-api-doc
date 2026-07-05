---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-copy-trading-get-unrealized-profit-sharing-details
anchor_id: order-book-trading-copy-trading-get-unrealized-profit-sharing-details
api_type: API
updated_at: 2026-07-05 19:34:09.907580
---

# GET / Unrealized profit sharing details

The leading trader gets the profit sharing details that are expected to be shared in the next settlement cycle.  
The unrealized profit sharing details will update once there copy position is closed.  
  
#### Rate limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP request

`GET /api/v5/copytrading/unrealized-profit-sharing-details`

> Request example
    
    
    GET /api/v5/copytrading/unrealized-profit-sharing-details
    
    

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
                "nickName": "Potato",
                "portLink": "",
                "ts": "1669901824779",
                "unrealizedProfitSharingAmt": "0.455472",
                "instType": "SWAP"
            },
            {
                "ccy": "USDT",
                "nickName": "Apple",
                "portLink": "",
                "ts": "1669460210113",
                "unrealizedProfitSharingAmt": "0.033608",
                "instType": "SWAP"
            }
        ],
        "msg": ""
    }
    

#### Response parameters

**Parameter** | **Type** | **Description**  
---|---|---  
ccy | String | The currency of profit sharing. e.g. USDT  
unrealizedProfitSharingAmt | String | Unrealized profit sharing amount.  
nickName | String | Nickname of copy trader.  
instType | String | Instrument type  
portLink | String | Portrait link  
ts | String | Update time.

---

# GET / 交易员待分润明细

交易员获取预计在下一个周期分到的分润金额明细。  
当有跟单仓位平仓时，待分润明细会进行更新。  
  
#### 限速：5次/2s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/copytrading/unrealized-profit-sharing-details`

> 请求示例
    
    
    GET /api/v5/copytrading/unrealized-profit-sharing-details
    
    

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
                "nickName": "Potato",
                "portLink": "",
                "ts": "1669901824779",
                "unrealizedProfitSharingAmt": "0.455472",
                "instType": "SWAP"
            },
            {
                "ccy": "USDT",
                "nickName": "Apple",
                "portLink": "",
                "ts": "1669460210113",
                "unrealizedProfitSharingAmt": "0.033608",
                "instType": "SWAP"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
ccy | String | 分润币种，如：`USDT`  
unrealizedProfitSharingAmt | String | 待分润额  
nickName | String | 跟单人昵称  
instType | String | 产品类型  
SPOT：币币  
SWAP：永续合约  
portLink | String | 跟单员头像的链接地址  
ts | String | 数据更新时间