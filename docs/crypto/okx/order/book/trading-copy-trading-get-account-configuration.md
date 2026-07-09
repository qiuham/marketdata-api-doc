---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-copy-trading-get-account-configuration
anchor_id: order-book-trading-copy-trading-get-account-configuration
api_type: API
updated_at: 2026-07-09 19:37:31.487156
---

# GET / Account configuration

Retrieve current account configuration related to copy/lead trading.  
  
#### Rate limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP request

`GET /api/v5/copytrading/config`

> Request example
    
    
    GET /api/v5/copytrading/config
    
    

#### Request Parameters

None

> Response example
    
    
    {
        "code": "0",
        "data": [
            {
                "details": [
                    {
                        "copyTraderNum": "1",
                        "instType": "SWAP",
                        "maxCopyTraderNum": "100",
                        "profitSharingRatio": "0",
                        "roleType": "1"
                    },
                    {
                        "copyTraderNum": "",
                        "instType": "SPOT",
                        "maxCopyTraderNum": "",
                        "profitSharingRatio": "",
                        "roleType": "0"
                    }
                ],
                "nickName": "155***9957",
                "portLink": "",
                "uniqueCode": "5506D3681454A304"
            }
        ],
        "msg": ""
    }
    
    

#### Response parameters

**Parameter** | **Type** | **Description**  
---|---|---  
uniqueCode | String | User unique code  
nickName | String | Nickname  
portLink | String | Portrait link  
details | Array of objects | Details  
> instType | String | Instrument type  
`SPOT`  
`SWAP`  
> roleType | String | Role type  
`0`: General user  
`1`: Leading trader  
`2`: Copy trader  
> profitSharingRatio | String | Profit sharing ratio.   
Only applicable to lead trader, or it will be "". 0.1 represents 10%  
> maxCopyTraderNum | String | Maximum number of copy traders  
> copyTraderNum | String | Current number of copy traders

---

# GET / 查看账户配置信息

获取跟单交易和带单交易相关的账户配置信息  
  
#### 限速：5次/2s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/copytrading/config`

> 请求示例
    
    
    GET /api/v5/copytrading/config
    
    

#### 请求参数

无

> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "details": [
                    {
                        "copyTraderNum": "1",
                        "instType": "SWAP",
                        "maxCopyTraderNum": "100",
                        "profitSharingRatio": "0",
                        "roleType": "1"
                    },
                    {
                        "copyTraderNum": "",
                        "instType": "SPOT",
                        "maxCopyTraderNum": "",
                        "profitSharingRatio": "",
                        "roleType": "0"
                    }
                ],
                "nickName": "155***9957",
                "portLink": "",
                "uniqueCode": "5506D3681454A304"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
uniqueCode | String | 交易员唯一标识代码  
nickName | String | 昵称  
portLink | String | 头像的链接地址  
details | Array of objects | 详情  
> instType | String | 产品类型  
`SPOT`: 币币  
`SWAP`: 永续合约  
> roleType | String | 用户角色  
`0`：普通用户  
`1`：带单者  
`2`：跟单者  
> profitSharingRatio | String | 分润比例，仅适用于带单员，0.1 代表 10%，否则为""  
> maxCopyTraderNum | String | 最大跟单人数，仅适用于带单员  
> copyTraderNum | String | 当前跟单人数，仅适用于带单员