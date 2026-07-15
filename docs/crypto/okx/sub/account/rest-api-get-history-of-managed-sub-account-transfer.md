---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#sub-account-rest-api-get-history-of-managed-sub-account-transfer
anchor_id: sub-account-rest-api-get-history-of-managed-sub-account-transfer
api_type: REST
updated_at: 2026-07-15 19:20:33.388509
---

# Get history of managed sub-account transfer

Only applicable to the trading team's master account to getting transfer records of managed sub accounts entrusted to oneself.  
  
#### Rate limit：6 requests per second

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP request

`GET /api/v5/asset/subaccount/managed-subaccount-bills`

> Request sample
    
    
    GET /api/v5/asset/subaccount/managed-subaccount-bills
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
ccy | String | No | Currency, e.g `BTC`  
type | String | No | Transfer type  
`0`: Transfers from master account to sub-account  
`1`: Transfers from sub-account to master account  
subAcct | String | No | Sub-account name  
subUid | String | No | Sub-account UID  
after | String | No | Query the data prior to the requested bill ID creation time (exclude), Unix timestamp in millisecond format, e.g. `1597026383085`  
before | String | No | Query the data after the requested bill ID creation time (exclude), Unix timestamp in millisecond format, e.g. `1597026383085`  
limit | String | No | Number of results per request. The maximum is 100. The default is 100.  
  
> Returned results
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
            "billId": "12344",
            "type": "1",
            "ccy": "BTC",
            "amt": "2",
            "subAcct": "test-1",
            "subUid": "xxxxxx",
            "ts": "1597026383085"
        }]
    }
    

#### Response parameters

**Parameter name** | **Type** | **Description**  
---|---|---  
billId | String | Bill ID  
ccy | String | Transfer currency  
amt | String | Transfer amount  
type | String | Bill type  
subAcct | String | Sub-account name  
subUid | String | Sub-account UID  
ts | String | Bill ID creation time, Unix timestamp in millisecond format, e.g. `1597026383085`

---

# 查询托管子账户转账记录

仅适用于交易团队母账户查看托管给自己的托管子账户转账记录  
  
#### 限速：6次/s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/asset/subaccount/managed-subaccount-bills`

> 请求示例
    
    
    GET /api/v5/asset/subaccount/managed-subaccount-bills
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
ccy | String | 否 | 币种，如 `BTC`  
type | String | 否 | 划转类型  
`0`：母账户转子账户  
`1`：子账户转母账户  
subAcct | String | 否 | 子账户名称  
subUid | String | 否 | 子账户UID  
after | String | 否 | 查询在billId创建时间之前(不包含)的内容，值为时间戳，Unix时间戳的毫秒数格式，如 `1597026383085`  
before | String | 否 | 查询在billId创建时间之后(不包含)的内容，值为时间戳，Unix时间戳的毫秒数格式，如 `1597026383085`  
limit | String | 否 | 分页返回的结果集数量，最大为100，默认返回100条  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
            "billId": "12344",
            "type": "1",
            "ccy": "BTC",
            "amt": "2",
            "subAcct": "test-1",
            "subUid": "xxxxxx",
            "ts": "1597026383085"
        }]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
billId | String | 账单ID  
ccy | String | 划转币种  
amt | String | 划转金额  
type | String | 账单类型  
subAcct | String | 子账户名称  
subUid | String | 子账户UID  
ts | String | 账单ID创建时间，Unix时间戳的毫秒数格式，如 `1597026383085`