---
exchange: binance
source_url: https://developers.binance.com/docs/sub_account/api-management/Delete-IP-List-For-a-Sub-account-API-Key
api_type: Account
updated_at: 2026-05-27 19:02:08.878987
---

# Delete IP List For a Sub-account API Key (For Master Account) (USER_DATA)

## API Description[​](/docs/sub_account/api-management/Delete-IP-List-For-a-Sub-account-API-Key#api-description "Direct link to API Description")

Delete IP List For a Sub-account API Key

## HTTP Request[​](/docs/sub_account/api-management/Delete-IP-List-For-a-Sub-account-API-Key#http-request "Direct link to HTTP Request")

DELETE `/sapi/v1/sub-account/subAccountApi/ipRestriction/ipList`

## Request Weight(UID)[​](/docs/sub_account/api-management/Delete-IP-List-For-a-Sub-account-API-Key#request-weightuid "Direct link to Request Weight\(UID\)")

**3000**

## Request Parameters[​](/docs/sub_account/api-management/Delete-IP-List-For-a-Sub-account-API-Key#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
email| STRING| YES| [Sub-account email](/docs/sub_account/api-management/Delete-IP-List-For-a-Sub-account-API-Key#email-address)  
subAccountApiKey| STRING| YES|   
ipAddress| STRING| YES| IPs to be deleted. Can be added in batches, separated by commas  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * You need to enable Enable Spot & Margin Trading option for the api key which requests this endpoint
> 


## Response Example[​](/docs/sub_account/api-management/Delete-IP-List-For-a-Sub-account-API-Key#response-example "Direct link to Response Example")
    
    
    {  
      "ipRestrict": "true",  
      "ipList": [  
        "69.210.67.14",  
        "8.34.21.10"  
      ],  
      "updateTime": 1636371437000,  
      "apiKey": "k5V49ldtn4tszj6W3hystegdfvmGbqDzjmkCtpTvC0G74WhK7yd4rfCTo4lShf"  
    }

---

# 删除子账户API Key IP白名单 (适用母账户) (USER_DATA)

## 接口描述[​](/docs/zh-CN/sub_account/api-management/Delete-IP-List-For-a-Sub-account-API-Key#接口描述 "接口描述的直接链接")

删除子账户API Key IP白名单

## HTTP请求[​](/docs/zh-CN/sub_account/api-management/Delete-IP-List-For-a-Sub-account-API-Key#http请求 "HTTP请求的直接链接")

DELETE `/sapi/v1/sub-account/subAccountApi/ipRestriction/ipList`

## 请求权重(UID)[​](/docs/zh-CN/sub_account/api-management/Delete-IP-List-For-a-Sub-account-API-Key#请求权重uid "请求权重\(UID\)的直接链接")

**3000**

## 请求参数[​](/docs/zh-CN/sub_account/api-management/Delete-IP-List-For-a-Sub-account-API-Key#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
email| STRING| YES| [Sub-account email](/docs/zh-CN/sub_account/api-management/Delete-IP-List-For-a-Sub-account-API-Key#email-address)  
subAccountApiKey| STRING| YES|   
ipAddress| STRING| YES| 想删除的 IP。可批量删除，用逗号分隔  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * 调用此端口前需要在api管理页开启允许现货及杠杆交易选项
> 


## 响应示例[​](/docs/zh-CN/sub_account/api-management/Delete-IP-List-For-a-Sub-account-API-Key#响应示例 "响应示例的直接链接")
    
    
    {  
      "ipRestrict": "true",  
      "ipList": [  
        "69.210.67.14",  
        "8.34.21.10"  
      ],  
      "updateTime": 1636371437000,  
      "apiKey": "k5V49ldtn4tszj6W3hystegdfvmGbqDzjmkCtpTvC0G74WhK7yd4rfCTo4lShf"  
    }