---
exchange: binance
source_url: https://developers.binance.com/docs/sub_account/managed-sub-account/Query-Managed-Sub-Account-Transfer-Log-Investor
api_type: Account
updated_at: 2026-05-27 19:02:57.177303
---

# Query Managed Sub Account Transfer Log (For Investor Master Account) (USER_DATA)

## API Description[​](/docs/sub_account/managed-sub-account/Query-Managed-Sub-Account-Transfer-Log-Investor#api-description "Direct link to API Description")

Investor can use this api to query managed sub account transfer log. This endpoint is available for investor of Managed Sub-Account. A Managed Sub-Account is an account type for investors who value flexibility in asset allocation and account application, while delegating trades to a professional trading team. Please refer to [link](https://www.binance.com/en/support/faq/how-to-get-started-with-managed-sub-account-functions-and-frequently-asked-questions-0594748722704383a7c369046e489459)

## HTTP Request[​](/docs/sub_account/managed-sub-account/Query-Managed-Sub-Account-Transfer-Log-Investor#http-request "Direct link to HTTP Request")

GET `/sapi/v1/managed-subaccount/queryTransLogForInvestor`

## Request Weight(IP)[​](/docs/sub_account/managed-sub-account/Query-Managed-Sub-Account-Transfer-Log-Investor#request-weightip "Direct link to Request Weight\(IP\)")

**1**

## Request Parameters[​](/docs/sub_account/managed-sub-account/Query-Managed-Sub-Account-Transfer-Log-Investor#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
email| STRING| YES| Managed Sub Account Email  
startTime| LONG| YES| Start Time  
endTime| LONG| YES| End Time (The start time and end time interval cannot exceed half a year)  
page| INT| YES| Page  
limit| INT| YES| Limit (Max: 500)  
transfers| STRING| NO| Transfer Direction (FROM/TO)  
transferFunctionAccountType| STRING| NO| Transfer function account type (SPOT/MARGIN/ISOLATED_MARGIN/USDT_FUTURE/COIN_FUTURE)  
  
## Response Example[​](/docs/sub_account/managed-sub-account/Query-Managed-Sub-Account-Transfer-Log-Investor#response-example "Direct link to Response Example")
    
    
    {  
        "managerSubTransferHistoryVos": [  
            {  
                "fromEmail": "test_0_virtual@kq3kno9imanagedsub.com"  
                "fromAccountType": "SPOT"  
                "toEmail": "wdywl0lddakh@test.com"  
                "toAccountType": "SPOT"  
                "asset": "BNB"  
                "amount": "0.01"  
                "scheduledData": 1679416673000  
                "createTime": 1679416673000  
                "status": "SUCCESS"  
                "tranId": 91077779  
            },  
            {  
                "fromEmail": "wdywl0lddakh@test.com"  
                "fromAccountType": "SPOT"  
                "toEmail": "test_0_virtual@kq3kno9imanagedsub.com"  
                "toAccountType": "SPOT"  
                "asset": "BNB"  
                "amount": "1"  
                "scheduledData": 1679416616000  
                "createTime": 1679416616000  
                "status": "SUCCESS"  
                "tranId": 91077676  
            }  
        ],  
        "count": 2  
    }

---

# 查询托管子账户的划转记录 (适用投资人母账户) (USER_DATA)

## 接口描述[​](/docs/zh-CN/sub_account/managed-sub-account/Query-Managed-Sub-Account-Transfer-Log-Investor#接口描述 "接口描述的直接链接")

投资人可以根据此接口查询其托管子账户划转记录。此接口可供托管子账户的投资者使用。托管子账户是为重视资产配置与账户应用灵活性，并同时将交易委托专业交易团队的投资者的子账户类型。 请参阅[链接](https://www.binance.com/zh-CN/support/faq/%E6%89%98%E7%AE%A1%E5%AD%90%E8%B4%A6%E6%88%B7%E5%8A%9F%E8%83%BD%E4%BB%8B%E7%BB%8D-0594748722704383a7c369046e489459)

## HTTP请求[​](/docs/zh-CN/sub_account/managed-sub-account/Query-Managed-Sub-Account-Transfer-Log-Investor#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/managed-subaccount/queryTransLogForInvestor`

## 请求权重(UID)[​](/docs/zh-CN/sub_account/managed-sub-account/Query-Managed-Sub-Account-Transfer-Log-Investor#请求权重uid "请求权重\(UID\)的直接链接")

**60**

## 请求参数[​](/docs/zh-CN/sub_account/managed-sub-account/Query-Managed-Sub-Account-Transfer-Log-Investor#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
email| STRING| YES| 托管子账户邮箱  
startTime| LONG| YES| 开始时间  
endTime| LONG| YES| 结束时间(开始时间结束时间间隔不能超过半年)  
page| INT| YES| 页数  
limit| INT| YES| 每页数量 (最大值: 500)  
transfers| STRING| NO| 划转方向 (FROM/TO)  
transferFunctionAccountType| STRING| NO| 划转账户类型 (SPOT/MARGIN/ISOLATED_MARGIN/USDT_FUTURE/COIN_FUTURE)  
  
## 响应示例[​](/docs/zh-CN/sub_account/managed-sub-account/Query-Managed-Sub-Account-Transfer-Log-Investor#响应示例 "响应示例的直接链接")
    
    
    {  
        "managerSubTransferHistoryVos": [  
            {  
                fromEmail: "test_0_virtual@kq3kno9imanagedsub.com",  
                fromAccountType: "SPOT",  
                toEmail: "wdywl0lddakh@test.com",  
                toAccountType: "SPOT",  
                asset: "BNB",  
                amount: "0.01",  
                scheduledData: 1679416673000,  
                createTime: 1679416673000,  
                status: "SUCCESS",  
                tranId: 91077779  
            },  
            {  
                fromEmail: "wdywl0lddakh@test.com",  
                fromAccountType: "SPOT",  
                toEmail: "test_0_virtual@kq3kno9imanagedsub.com",  
                toAccountType: "SPOT",  
                asset: "BNB",  
                amount: "1",  
                scheduledData: 1679416616000,  
                createTime: 1679416616000,  
                status: "SUCCESS",  
                tranId: 91077676  
            }  
        ],  
        "count": 2  
    }