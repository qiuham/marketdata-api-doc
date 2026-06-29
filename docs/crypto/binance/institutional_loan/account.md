---
exchange: binance
source_url: https://developers.binance.com/docs/institutional_loan/account
api_type: Account
updated_at: 2026-06-29 19:13:27.655213
---

# Query Closed Risk Unit Record (USER_DATA)

## API Description[​](/docs/institutional_loan/account/Query-Closed-Group-Record#api-description "Direct link to API Description")

Query closed risk unit record. This endpoint is accessible only with the credit account API key.

## HTTP Request[​](/docs/institutional_loan/account/Query-Closed-Group-Record#http-request "Direct link to HTTP Request")

GET /sapi/v1/margin/loan-groups/closed

## Request Weight[​](/docs/institutional_loan/account/Query-Closed-Group-Record#request-weight "Direct link to Request Weight")

1(IP)

## Request Parameters[​](/docs/institutional_loan/account/Query-Closed-Group-Record#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
current| LONG| NO| The currently querying page. Start from 1. Default:1  
size| LONG| NO| Default:10 Max:100  
  
## Response Example[​](/docs/institutional_loan/account/Query-Closed-Group-Record#response-example "Direct link to Response Example")
    
    
    {  
      "total": 2,  
      "rows": [  
        {  
          "groupId": 72,  
          "parentEmail": "wdywgceiwbfq@test.com",  
          "creditEmail": "wdywaxmzlnah@test.com",  
          "enabled": false,  
          "createTime": 1753410654608,  
          "closeTime": 1753422899052  
        },  
        {  
          "groupId": 73,  
          "parentEmail": "wdywgceiwbfq@test.com",  
          "creditEmail": "wdyw7x4gfybn@test.com",  
          "enabled": false,  
          "createTime": 1753422987379,  
          "closeTime": 1753423516629  
        }  
      ]  
    }  
    

## Response detail description[​](/docs/institutional_loan/account/Query-Closed-Group-Record#response-detail-description "Direct link to Response detail description")

Parameter| Type| Description  
---|---|---  
total| LONG| Risk unit number which get as query result  
rows| OBJECT ARRAY|   
→ groupId| LONG| Risk unit unique identifier  
→ parentEmail| STRING| Parent account email  
→ creditEmail| STRING| Credit account email  
→ enabled| STRING| The status of the group. TRUE for enabled; FALSE for disabled.  
→ createTime| LONG| The group create timestamp (milliseconds)  
→ closeTime| LONG| The group close timestamp (milliseconds)

---

# 查询关闭的风险单元记录(USER_DATA)

## 接口描述[​](/docs/zh-CN/institutional_loan/account/Query-Closed-Group-Record#接口描述 "接口描述的直接链接")

查询已关闭的风险单元记录。 仅支持放贷账户调用该接口。

## HTTP请求[​](/docs/zh-CN/institutional_loan/account/Query-Closed-Group-Record#http请求 "HTTP请求的直接链接")

GET /sapi/v1/margin/loan-groups/closed

## 请求权重[​](/docs/zh-CN/institutional_loan/account/Query-Closed-Group-Record#请求权重 "请求权重的直接链接")

1(IP)

## 请求参数[​](/docs/zh-CN/institutional_loan/account/Query-Closed-Group-Record#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
current| LONG| NO| 当前查询页。 开始值 1。 默认:1  
size| LONG| NO| 默认:10 最大:100  
  
## 响应示例[​](/docs/zh-CN/institutional_loan/account/Query-Closed-Group-Record#响应示例 "响应示例的直接链接")
    
    
    {  
      "total": 2,  
      "rows": [  
        {  
          "groupId": 72,  
          "parentEmail": "wdywgceiwbfq@test.com",  
          "creditEmail": "wdywaxmzlnah@test.com",  
          "enabled": false,  
          "createTime": 1753410654608,  
          "closeTime": 1753422899052  
        },  
        {  
          "groupId": 73,  
          "parentEmail": "wdywgceiwbfq@test.com",  
          "creditEmail": "wdyw7x4gfybn@test.com",  
          "enabled": false,  
          "createTime": 1753422987379,  
          "closeTime": 1753423516629  
        }  
      ]  
    }  
    

## 响应信息详解：[​](/docs/zh-CN/institutional_loan/account/Query-Closed-Group-Record#响应信息详解 "响应信息详解：的直接链接")

参数| 类型| 描述  
---|---|---  
total| LONG| 查询记录总数量  
rows| OBJECT ARRAY|   
→ groupId| LONG| 唯一风险单位标识符  
→ parentEmail| STRING|   
→ creditEmail| STRING|   
→ enabled| STRING| 状态。TRUE表示活跃状态；FALSE表示关闭状态。  
→ createTime| LONG| 风险单位创建时间（毫秒）  
→ closeTime| LONG|