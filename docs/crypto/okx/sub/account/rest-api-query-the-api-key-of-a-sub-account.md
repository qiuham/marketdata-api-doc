---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#sub-account-rest-api-query-the-api-key-of-a-sub-account
anchor_id: sub-account-rest-api-query-the-api-key-of-a-sub-account
api_type: REST
updated_at: 2026-07-20 19:37:24.500862
---

# Query the API Key of a sub-account

Applies to master accounts only  
  
#### Rate limit：20 request per 2 seconds

#### Rate limit rule: User ID

#### HTTP request

`GET /api/v5/users/subaccount/apikey`

> Request sample
    
    
    GET /api/v5/users/subaccount/apikey?subAcct=panpanBroker2
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
subAcct | String | Yes | Sub-account name  
apiKey | String | No | API public key  
  
> Returned results
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "label": "v5",
                "apiKey": "******",
                "perm": "read_only,trade",
                "ip": "1.1.1.1,2.2.2.2",
                "ts": "1597026383085"
            },
            {
                "label": "v5.1",
                "apiKey": "******",
                "perm": "read_only",
                "ip": "1.1.1.1,2.2.2.2",
                "ts": "1597026383085"
            }
        ]
    }
    

#### Response parameters

**Parameter name** | **Type** | **Description**  
---|---|---  
label | String | API Key note  
apiKey | String | API public key  
perm | String | API Key access   
read_only: Read only; trade: Trade  
ip | String | IP address that linked with API Key  
ts | String | Creation time

---

# 查询子账户的API Key

仅适用于母账户   
  
#### 限速：20次/2秒

#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/users/subaccount/apikey`

> 请求示例
    
    
    GET /api/v5/users/subaccount/apikey?subAcct=panpanBroker2
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
subAcct | String | 是 | 子账户名称  
apiKey | String | 否 | API的公钥  
  
> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "label":"v5",
                "apiKey":"arg13sdfgs",
                "perm":"read_only,trade",
                "ip":"1.1.1.1,2.2.2.2",
                "ts":"1597026383085"
            },
            {
                "label":"v5.1",
                "apiKey":"arg13sdfgs",
                "perm":"read_only",
                "ip":"1.1.1.1,2.2.2.2",
                "ts":"1597026383085"
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
label | String | API Key的备注  
apiKey | String | API Key公钥  
perm | String | API Key权限  
read_only：读取  
trade ：交易  
ip | String | API Key绑定的ip地址  
ts | String | 创建时间