---
exchange: binance
source_url: https://developers.binance.com/docs/wallet/capital/fetch-withdraw-address
api_type: REST
updated_at: 2026-06-30 19:09:29.904212
---

# Withdraw History (supporting network) (USER_DATA)

## API Description[​](/docs/wallet/capital/withdraw-history#api-description "Direct link to API Description")

Fetch withdraw history.

## HTTP Request[​](/docs/wallet/capital/withdraw-history#http-request "Direct link to HTTP Request")

GET `/sapi/v1/capital/withdraw/history`

## Request Weight(UID)[​](/docs/wallet/capital/withdraw-history#request-weightuid "Direct link to Request Weight\(UID\)")

**18000** Request limit: 10 requests per second

## Request Parameters[​](/docs/wallet/capital/withdraw-history#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
coin| STRING| NO|   
withdrawOrderId| STRING| NO| client side id for withdrawal, if provided in POST `/sapi/v1/capital/withdraw/apply`, can be used here for query.  
status| INT| NO| 0(0:Email Sent, 2:Awaiting Approval 3:Rejected 4:Processing 6:Completed)  
offset| INT| NO|   
limit| INT| NO| Default: 1000, Max: 1000  
idList| STRING| NO| id list returned in the response of POST `/sapi/v1/capital/withdraw/apply`, separated by `,`  
startTime| LONG| NO| Default: 90 days from current timestamp  
endTime| LONG| NO| Default: present timestamp  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * `network` may not be in the response for old withdraw.
>   * Please notice the default `startTime` and `endTime` to make sure that time interval is within 0-90 days.
>   * If both `startTime` and `endTime`are sent, time between `startTime`and `endTime`must be less than 90 days.
>   * If `withdrawOrderId` is sent, time between `startTime` and `endTime` must be less than 7 days.
>   * If `withdrawOrderId` is sent, `startTime` and `endTime` are not sent, will return last 7 days records by default.
>   * Maximum support `idList` number is 45.
> 


## Response Example[​](/docs/wallet/capital/withdraw-history#response-example "Direct link to Response Example")
    
    
    [  
        {  
            "id": "b6ae22b3aa844210a7041aee7589627c",                                         // Withdrawal id in Binance  
            "amount": "8.91000000",                                                           // withdrawal amount  
            "transactionFee": "0.004",                                                        // transaction fee  
            "coin": "USDT",  
            "status": 6,  
            "address": "0x94df8b352de7f46f64b01d3666bf6e936e44ce60",  
            "txId": "0xb5ef8c13b968a406cc62a93a8bd80f9e9a906ef1b3fcf20a2e48573c17659268",     // withdrawal transaction id  
            "applyTime": "2019-10-12 11:12:02",                                               // UTC time  
            "network": "ETH",  
            "transferType": 0,                                                                // 1 for internal transfer, 0 for external transfer  
            "withdrawOrderId": "WITHDRAWtest123",                                             // will not be returned if there's no withdrawOrderId for this withdraw.  
            "info": "The address is not valid. Please confirm with the recipient",            // reason for withdrawal failure  
            "confirmNo": 3,                                                                   // confirm times for withdraw  
            "walletType": 1,                                                                  // 1: Funding Wallet 0:Spot Wallet  
            "txKey": "",  
            "completeTime": "2023-03-23 16:52:41"                                             // complete UTC time when user's asset is deduct from withdrawing, only if status =  6(success)  
        },  
        {  
            "id": "156ec387f49b41df8724fa744fa82719",  
            "amount": "0.00150000",  
            "transactionFee": "0.004",  
            "coin": "BTC",  
            "status": 6,  
            "address": "1FZdVHtiBqMrWdjPyRPULCUceZPJ2WLCsB",  
            "txId": "60fd9007ebfddc753455f95fafa808c4302c836e4d1eebc5a132c36c1d8ac354",  
            "applyTime": "2019-09-24 12:43:45",  
            "network": "BTC",  
            "transferType": 0,  
            "info": "",  
            "confirmNo": 2,  
            "walletType": 1,  
            "txKey": "",  
            "completeTime": "2023-03-23 16:52:41"  
        }  
    ]

---

# 获取提币历史(支持多网络)(USER_DATA)

## 接口描述[​](/docs/zh-CN/wallet/capital/withdraw-history#接口描述 "接口描述的直接链接")

获取提币历史 (支持多网络)

## HTTP请求[​](/docs/zh-CN/wallet/capital/withdraw-history#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/capital/withdraw/history`

## 请求权重(UID)[​](/docs/zh-CN/wallet/capital/withdraw-history#请求权重uid "请求权重\(UID\)的直接链接")

**18000** **请求限制:** 每秒10次

## 请求参数[​](/docs/zh-CN/wallet/capital/withdraw-history#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
coin| STRING| NO|   
withdrawOrderId| STRING| NO| 用户自定义提币ID，如果在 POST `/sapi/v1/capital/withdraw/apply` 时设置了该字段，则此时可以用该字段查询订单  
status| INT| NO| 0(0:已发送确认Email, 2:等待确认 3:被拒绝 4:处理中 6 提现完成)  
offset| INT| NO|   
limit| INT| NO| 默认：1000， 最大：1000  
idList| STRING| NO| POST `/sapi/v1/capital/withdraw/apply` 返回的 id 列表，以 `,` 分隔  
startTime| LONG| NO| 默认当前时间90天前的时间戳  
endTime| LONG| NO| 默认当前时间戳  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * 支持多网络提币前的历史记录可能不会返回`network`字段.
>   * 请注意`startTime` 与 `endTime` 的默认时间戳，保证请求时间间隔不得超过90天.
>   * 同时提交`startTime` 与 `endTime`间隔不得超过90天.
>   * 若传了`withdrawOrderId`，则请求的`startTime` 与 `endTime`的时间间隔不得超过7天.
>   * 若传了`withdrawOrderId`，没传`startTime` 与 `endTime`，则默认返回最近7天数据.
>   * 最大支持的`idList`是 45 个
> 


## 响应示例[​](/docs/zh-CN/wallet/capital/withdraw-history#响应示例 "响应示例的直接链接")
    
    
    [  
        {  
            "id": "b6ae22b3aa844210a7041aee7589627c",                                         // 该笔提现在币安的id  
            "amount": "8.91000000",                                                           // 提现转出金额  
            "transactionFee": "0.004",                                                        // 手续费  
            "coin": "USDT",  
            "status": 6,  
            "address": "0x94df8b352de7f46f64b01d3666bf6e936e44ce60",  
            "txId": "0xb5ef8c13b968a406cc62a93a8bd80f9e9a906ef1b3fcf20a2e48573c17659268",     // 提现交易id  
            "applyTime": "2019-10-12 11:12:02",                                               // UTC 时间  
            "network": "ETH",  
            "transferType": 0,                                                                // 1: 站内转账, 0: 站外转账  
            "withdrawOrderId": "WITHDRAWtest123",                                             // 自定义ID, 如果没有则不返回该字段  
            "info": "The address is not valid. Please confirm with the recipient",            // 提币失败原因  
            "confirmNo": 3,                                                                   // 提现确认数  
            "walletType": 1,                                                                  // 1: 资金钱包 0:现货钱包  
            "txKey": "",  
            "completeTime": "2023-03-23 16:52:41"                                             // 提现完成，成功下账时间(UTC)  
        },  
        {  
            "id": "156ec387f49b41df8724fa744fa82719",  
            "amount": "0.00150000",  
            "transactionFee": "0.004",  
            "coin": "BTC",  
            "status": 6,  
            "address": "1FZdVHtiBqMrWdjPyRPULCUceZPJ2WLCsB",  
            "txId": "60fd9007ebfddc753455f95fafa808c4302c836e4d1eebc5a132c36c1d8ac354",  
            "applyTime": "2019-09-24 12:43:45",  
            "network": "BTC",  
            "transferType": 0,  
            "info": "",  
            "confirmNo": 2,  
            "walletType": 1,  
            "txKey": "",  
            "completeTime": "2023-03-23 16:52:41"  
        }  
    ]