---
exchange: binance
source_url: https://developers.binance.com/docs/institutional_loan/account/Query-Closed-Group-Record
api_type: Account
updated_at: 2026-05-27 19:01:10.450883
---

# Query Active Risk Units(USER_DATA)

## API Description[​](/docs/institutional_loan/account/Query-Institution-Loan-Group_Activated#api-description "Direct link to API Description")

Retrieves the list of active institutional loan risk units. This endpoint is accessible only with the parent account API key.

## HTTP Request[​](/docs/institutional_loan/account/Query-Institution-Loan-Group_Activated#http-request "Direct link to HTTP Request")

GET /sapi/v1/margin/loan-groups/activated

## Request Weight[​](/docs/institutional_loan/account/Query-Institution-Loan-Group_Activated#request-weight "Direct link to Request Weight")

10(IP)

## Request Parameters[​](/docs/institutional_loan/account/Query-Institution-Loan-Group_Activated#request-parameters "Direct link to Request Parameters")

None

## Response Example[​](/docs/institutional_loan/account/Query-Institution-Loan-Group_Activated#response-example "Direct link to Response Example")
    
    
    [  
      {  
       "groupId": 10001,  
       "members": [  
          {  
               "email": "1001@test.com",  
               "type": "CREDIT",  
               "enableMargin": true,  
               "enableSpot": true  
          },  
          {  
               "email": "1002@test.com",  
               "type": "COLLATERAL",  
               "enableMargin": true,  
               "enableSpot": true  
          }  
      ],  
       "createTime": 1747637956083  
      },  
    {  
      "groupId": 10002,  
       "members": [  
          {  
               "email": "1003@test.com",  
               "type": "CREDIT",  
               "enableMargin": true,  
               "enableSpot": true  
          },  
          {  
               "email": "1004@test.com",  
               "type": "COLLATERAL",  
               "enableMargin": true,  
               "enableSpot": true  
          }  
      ],  
       "createTime": 1747637956083  
      }  
    ]  
    

## Response detail description[​](/docs/institutional_loan/account/Query-Institution-Loan-Group_Activated#response-detail-description "Direct link to Response detail description")

Parameter| Type| Description  
---|---|---  
groupId| LONG| Risk unit unique identifier  
members| OBJECT ARRAY|   
→ email| STRING| Account registered email  
→ type| STRING| Credit sub account or Collateral sub account  
→ enableMargin| STRING| TRUE: include margin account as collateral.   
FALSE: exclude margin account as collateral  
→ enableSpot| STRING| TRUE: include spot account as collateral  
FALSE: exclude spot account as collateral  
createTime| LONG| Last update timestamp (milliseconds)

---

# 查询有效风险单位 (USER_DATA)

## 接口描述[​](/docs/zh-CN/institutional_loan/account/Query-Institution-Loan-Group_Activated#接口描述 "接口描述的直接链接")

查询生效状态的机构贷风险单位列表。仅支持母账户查询该接口。

## HTTP 请求[​](/docs/zh-CN/institutional_loan/account/Query-Institution-Loan-Group_Activated#http-请求 "HTTP 请求的直接链接")

GET /sapi/v1/margin/loan-groups/activated

## 请求权重[​](/docs/zh-CN/institutional_loan/account/Query-Institution-Loan-Group_Activated#请求权重 "请求权重的直接链接")

10(IP)

## 请求参数[​](/docs/zh-CN/institutional_loan/account/Query-Institution-Loan-Group_Activated#请求参数 "请求参数的直接链接")

无

## 响应示例[​](/docs/zh-CN/institutional_loan/account/Query-Institution-Loan-Group_Activated#响应示例 "响应示例的直接链接")
    
    
    [  
      {  
       "groupId": 10001,  
       "members": [  
          {  
               "email": "1001@test.com",  
               "type": "CREDIT",  
               "enableMargin": true,  
               "enableSpot": true  
          },  
          {  
               "email": "1002@test.com",  
               "type": "COLLATERAL",  
               "enableMargin": true,  
               "enableSpot": true  
          }  
      ],  
       "createTime": 1747637956083  
      },  
    {  
      "groupId": 10002,  
       "members": [  
          {  
               "email": "1003@test.com",  
               "type": "CREDIT",  
               "enableMargin": true,  
               "enableSpot": true  
          },  
          {  
               "email": "1004@test.com",  
               "type": "COLLATERAL",  
               "enableMargin": true,  
               "enableSpot": true  
          }  
      ],  
       "createTime": 1747637956083  
      }  
    ]  
    

## 响应信息详解：[​](/docs/zh-CN/institutional_loan/account/Query-Institution-Loan-Group_Activated#响应信息详解 "响应信息详解：的直接链接")

参数| 类型| 描述  
---|---|---  
groupId| LONG| 唯一风险单位标识符  
members| OBJECT ARRAY|   
→ email| STRING| 账户注册邮箱  
→ type| STRING| 放贷子账户或抵押子账户  
→ enableMargin| STRING| TRUE: 杠杆账户包括在抵押账户内  
FALSE: 杠杆账户不包括在抵押账户内  
→ enableSpot| STRING| TRUE: 现货账户包括在抵押账户内  
FALSE: 现货账户不包括在抵押账户内  
  
createTime| LONG| 最后更新时间戳（毫秒）