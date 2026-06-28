---
exchange: binance
source_url: https://developers.binance.com/docs/institutional_loan/transfer/Query-Institution-Loan-Forced-Liquidation-Transfer-Records
api_type: REST
updated_at: 2026-06-28 18:56:21.820681
---

# Query Risk Unit Forced Liquidation Transfer Records(USER_DATA)

## API Description[​](/docs/institutional_loan/transfer/Query-Institution-Loan-Forced-Liquidation-Transfer-Records#api-description "Direct link to API Description")

Query the institution loan risk unit transfer records during forced liquidation. During the risk unit liquidation, funds from the collateral account may be transferred to the credit account to repay the principal and interest of institutional loans.This endpoint is accessible only with the credit account API key.

## HTTP Request[​](/docs/institutional_loan/transfer/Query-Institution-Loan-Forced-Liquidation-Transfer-Records#http-request "Direct link to HTTP Request")

GET /sapi/v1/margin/loan-group/force-liquidation-transfer-record

## Request Weight[​](/docs/institutional_loan/transfer/Query-Institution-Loan-Forced-Liquidation-Transfer-Records#request-weight "Direct link to Request Weight")

1(IP)

## Request Parameters[​](/docs/institutional_loan/transfer/Query-Institution-Loan-Forced-Liquidation-Transfer-Records#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
startTime| LONG| NO|   
endTime| LONG| NO|   
current| LONG| NO| The currently querying page. Start from 1. Default:1  
size| LONG| NO| Default:10 Max:100  
recvWindow| LONG| NO| The value cannot be greater than 60000  
timestamp| LONG| YES|   
  
>   * Response in descending order
>   * If neither startTime nor endTime is sent, the recent 7-day data will be returned.
>   * If startTime is not sent, default is endTime - 7days. If endTime is not sent, current time will be returned by default.
>   * startTime set as endTime - 7days by default, endTime set as current time by default.
>   * The length between startTime and endTime cannot exceed 100 days, otherwise an error is reported and no record is returned.
> 


## Response Example[​](/docs/institutional_loan/transfer/Query-Institution-Loan-Forced-Liquidation-Transfer-Records#response-example "Direct link to Response Example")
    
    
    {  
        "total": 2,  
        "rows": [  
            {  
                "liquidationId": 56,  
                "liquidationTransferRecord": [  
                    {  
                        "transferTime": 1765378400855,  
                        "fromUid": 1000277033525,  
                        "fromAccountType": "PORTFOLIO_MARGIN",  
                        "toUid": 1000277033505,  
                        "toAccountType": "PORTFOLIO_MARGIN",  
                        "status": "CONFIRM",  
                        "assets": [  
                            {  
                                "assetName": "USDT",  
                                "amount": "17750.6316"  
                            }  
                        ]  
                    },  
                    {  
                        "transferTime": 1765378830528,  
                        "fromUid": 1000277296026,  
                        "fromAccountType": "SPOT",  
                        "toUid": 1000277033505,  
                        "toAccountType": "PORTFOLIO_MARGIN",  
                        "status": "CONFIRM",  
                        "assets": [  
                            {  
                                "assetName": "BTC",  
                                "amount": "0.5"  
                            }  
                        ]  
                    }  
                ]  
            },  
            {  
                "liquidationId": 55,  
                "liquidationTransferRecord": [  
                    {  
                        "transferTime": 1765374361589,  
                        "fromUid": 1000277033515,  
                        "fromAccountType": "CROSS_MARGIN",  
                        "toUid": 1000277033505,  
                        "toAccountType": "PORTFOLIO_MARGIN",  
                        "status": "CONFIRM",  
                        "assets": [  
                            {  
                                "assetName": "USDT",  
                                "amount": "999.999024"  
                            }  
                        ]  
                    },  
                    {  
                        "transferTime": 1765375342535,  
                        "fromUid": 1000277033518,  
                        "fromAccountType": "PORTFOLIO_MARGIN",  
                        "toUid": 1000277033505,  
                        "toAccountType": "PORTFOLIO_MARGIN",  
                        "status": "CONFIRM",  
                        "assets": [  
                            {  
                                "assetName": "USDT",  
                                "amount": "999.999024"  
                            }  
                        ]  
                    },  
                    {  
                        "transferTime": 1765375640990,  
                        "fromUid": 1000277033525,  
                        "fromAccountType": "PORTFOLIO_MARGIN",  
                        "toUid": 1000277033505,  
                        "toAccountType": "PORTFOLIO_MARGIN",  
                        "status": "CONFIRM",  
                        "assets": [  
                            {  
                                "assetName": "USDT",  
                                "amount": "999.999024"  
                            }  
                        ]  
                    }  
                ]  
            }  
        ]  
    }  
      
    

## Response detail desc:[​](/docs/institutional_loan/transfer/Query-Institution-Loan-Forced-Liquidation-Transfer-Records#response-detail-desc "Direct link to Response detail desc:")

Name| Type| Description  
---|---|---  
liquidationId| Long| Risk unit liquidation unique identifier  
liquidationTransferRecord| Object Array| List of transfer records related to the liquidationId.  
→transferTime| Long| Timestamp of the transfer event.  
→fromUid| String| UID of the account transferring the assets.  
→fromAccountType| String| SPOT or PORTFOLIO MARGIN or CROSS MARGIN ACCOUNT  
→toUid| String| UID of the account receiving the assets.  
→toAccountType| String| SPOT or PORTFOLIO MARGIN or CROSS MARGIN ACCOUNT  
→status| String| Current status of the transfer.  
assets| Object Array|   
  
→assetName| String| Name of the transferred token.  
→amount| String| Amount of the token transferred.

---

# 查询机构贷强制平仓划转记录 (USER_DATA)

## 接口描述[​](/docs/zh-CN/institutional_loan/transfer/Query-Institution-Loan-Forced-Liquidation-Transfer-Records#接口描述 "接口描述的直接链接")

查询机构贷款风险单位在强制平仓期间的资金划转记录。在风险单位强制平仓期间，抵押账户中的资金可能会划转至放贷账户，用于偿还机构贷款的本金和利息。

仅支持放贷账户调用该接口。

## HTTP请求[​](/docs/zh-CN/institutional_loan/transfer/Query-Institution-Loan-Forced-Liquidation-Transfer-Records#http请求 "HTTP请求的直接链接")

GET /sapi/v1/margin/loan-group/force-liquidation-transfer-record

## 请求权重[​](/docs/zh-CN/institutional_loan/transfer/Query-Institution-Loan-Forced-Liquidation-Transfer-Records#请求权重 "请求权重的直接链接")

1(IP)

## 请求参数[​](/docs/zh-CN/institutional_loan/transfer/Query-Institution-Loan-Forced-Liquidation-Transfer-Records#请求参数 "请求参数的直接链接")

Name| Type| 是否必须| 描述  
---|---|---|---  
startTime| LONG| NO| 开始时间  
endTime| LONG| NO| 结束时间  
current| LONG| NO| 当前查询页。 开始值 1. 默认:1  
size| LONG| NO| 默认:10 最大:100  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * 响应返回为降序排列。
>   * 若startTime和endTime没传，则默认返回最近7天数据。
>   * startTime不传，默认endTime-7天；结束时间不传，默认当前时间。
>   * startTime和endTime时间长度不能超过100天，否则报错，无返回记录。
> 


## 响应示例[​](/docs/zh-CN/institutional_loan/transfer/Query-Institution-Loan-Forced-Liquidation-Transfer-Records#响应示例 "响应示例的直接链接")
    
    
    {  
        "total": 2,  
        "rows": [  
            {  
                "liquidationId": 56,  
                "liquidationTransferRecord": [  
                    {  
                        "transferTime": 1765378400855,  
                        "fromUid": 1000277033525,  
                        "fromAccountType": "PORTFOLIO_MARGIN",  
                        "toUid": 1000277033505,  
                        "toAccountType": "PORTFOLIO_MARGIN",  
                        "status": "CONFIRM",  
                        "assets": [  
                            {  
                                "assetName": "USDT",  
                                "amount": "17750.6316"  
                            }  
                        ]  
                    },  
                    {  
                        "transferTime": 1765378830528,  
                        "fromUid": 1000277296026,  
                        "fromAccountType": "SPOT",  
                        "toUid": 1000277033505,  
                        "toAccountType": "PORTFOLIO_MARGIN",  
                        "status": "CONFIRM",  
                        "assets": [  
                            {  
                                "assetName": "BTC",  
                                "amount": "0.5"  
                            }  
                        ]  
                    }  
                ]  
            },  
            {  
                "liquidationId": 55,  
                "liquidationTransferRecord": [  
                    {  
                        "transferTime": 1765374361589,  
                        "fromUid": 1000277033515,  
                        "fromAccountType": "CROSS_MARGIN",  
                        "toUid": 1000277033505,  
                        "toAccountType": "PORTFOLIO_MARGIN",  
                        "status": "CONFIRM",  
                        "assets": [  
                            {  
                                "assetName": "USDT",  
                                "amount": "999.999024"  
                            }  
                        ]  
                    },  
                    {  
                        "transferTime": 1765375342535,  
                        "fromUid": 1000277033518,  
                        "fromAccountType": "PORTFOLIO_MARGIN",  
                        "toUid": 1000277033505,  
                        "toAccountType": "PORTFOLIO_MARGIN",  
                        "status": "CONFIRM",  
                        "assets": [  
                            {  
                                "assetName": "USDT",  
                                "amount": "999.999024"  
                            }  
                        ]  
                    },  
                    {  
                        "transferTime": 1765375640990,  
                        "fromUid": 1000277033525,  
                        "fromAccountType": "PORTFOLIO_MARGIN",  
                        "toUid": 1000277033505,  
                        "toAccountType": "PORTFOLIO_MARGIN",  
                        "status": "CONFIRM",  
                        "assets": [  
                            {  
                                "assetName": "USDT",  
                                "amount": "999.999024"  
                            }  
                        ]  
                    }  
                ]  
            }  
        ]  
    }  
    

## 响应信息详解:[​](/docs/zh-CN/institutional_loan/transfer/Query-Institution-Loan-Forced-Liquidation-Transfer-Records#响应信息详解 "响应信息详解:的直接链接")

名称| 类型| 详情  
---|---|---  
liquidationId| Long| 唯一风险单位强制平仓标识符  
liquidationTransferRecord| Object Array| 与liquidationId相关的划转记录列表  
→transferTime| Long| 划转时间戳  
→fromUid| String| 划出资产的账号UID  
→fromAccountType| String| 现货账户或统一账户或全仓杠杆账户经典模式  
→toUid| String| 接收划转资产的账号UID  
→toAccountType| String| 现货账户或统一账户或全仓杠杆账户经典模式  
→status| String| 划转状态  
assets| Object Array|   
  
→assetName| String| 划转资产名称  
→amount| String| 划转资产金额