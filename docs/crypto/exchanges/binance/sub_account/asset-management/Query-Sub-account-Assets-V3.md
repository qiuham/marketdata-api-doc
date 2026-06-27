---
exchange: binance
source_url: https://developers.binance.com/docs/sub_account/asset-management/Query-Sub-account-Assets-V3
api_type: Account
updated_at: 2026-05-27 19:02:32.309700
---

# Query Sub-account Futures Asset Transfer History (For Master Account) (USER_DATA)

## API Description[​](/docs/sub_account/asset-management/Query-Sub-account-Futures-Asset-Transfer-History#api-description "Direct link to API Description")

Query Sub-account Futures Asset Transfer History

## HTTP Request[​](/docs/sub_account/asset-management/Query-Sub-account-Futures-Asset-Transfer-History#http-request "Direct link to HTTP Request")

GET `/sapi/v1/sub-account/futures/internalTransfer`

## Request Weight(IP)[​](/docs/sub_account/asset-management/Query-Sub-account-Futures-Asset-Transfer-History#request-weightip "Direct link to Request Weight\(IP\)")

**1**

## Request Parameters[​](/docs/sub_account/asset-management/Query-Sub-account-Futures-Asset-Transfer-History#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
email| STRING| YES| [Sub-account email](/docs/sub_account/asset-management/Query-Sub-account-Futures-Asset-Transfer-History#email-address)  
futuresType| LONG| YES| 1:USDT-margined Futures，2: Coin-margined Futures  
startTime| LONG| NO| Cannot be earlier than 1 month ago  
endTime| LONG| NO|   
page| INT| NO| Default value: 1  
limit| INT| NO| Default value: 50, Max value: 500  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/sub_account/asset-management/Query-Sub-account-Futures-Asset-Transfer-History#response-example "Direct link to Response Example")
    
    
    {  
        "success":true,  
        "futuresType": 2,  
        "transfers":[  
            {  
                "from":"aaa@test.com",  
                "to":"bbb@test.com",  
                "asset":"BTC",  
                "qty":"1",  
                "tranId":11897001102,  
                "time":1544433328000  
            },  
            {  
                "from":"bbb@test.com",  
                "to":"ccc@test.com",  
                "asset":"ETH",  
                "qty":"2",  
                "tranId":11631474902,  
                "time":1544433328000  
            }  
        ]  
    }

---

# 查询子账户合约资金划转历史 (适用主账户) (USER_DATA)

## 接口描述[​](/docs/zh-CN/sub_account/asset-management/Query-Sub-account-Futures-Asset-Transfer-History#接口描述 "接口描述的直接链接")

查询子账户合约资金划转历史

## HTTP请求[​](/docs/zh-CN/sub_account/asset-management/Query-Sub-account-Futures-Asset-Transfer-History#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/sub-account/futures/internalTransfer`

## 请求权重(IP)[​](/docs/zh-CN/sub_account/asset-management/Query-Sub-account-Futures-Asset-Transfer-History#请求权重ip "请求权重\(IP\)的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/sub_account/asset-management/Query-Sub-account-Futures-Asset-Transfer-History#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
email| STRING| YES| 子账户邮箱 [备注](/docs/zh-CN/sub_account/asset-management/Query-Sub-account-Futures-Asset-Transfer-History#request-email-address)  
futuresType| LONG| YES| 1:USDT合约，2: 币本位合约  
startTime| LONG| NO| 只能查询近一个月内历史纪录  
endTime| LONG| NO|   
page| INT| NO| 默认值: 1  
limit| INT| NO| 默认值: 50, 最大值：500  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/sub_account/asset-management/Query-Sub-account-Futures-Asset-Transfer-History#响应示例 "响应示例的直接链接")
    
    
    {  
        "success":true,  
        "futuresType": 2,  
        "transfers":[  
            {  
                "from":"aaa@test.com",  
                "to":"bbb@test.com",  
                "asset":"BTC",  
                "qty":"1",  
                "tranId":11897001102,  
                "time":1544433328000  
            },  
            {  
                "from":"bbb@test.com",  
                "to":"ccc@test.com",  
                "asset":"ETH",  
                "qty":"2",  
                "tranId":11631474902,  
                "time":1544433328000  
            }  
        ]  
    }