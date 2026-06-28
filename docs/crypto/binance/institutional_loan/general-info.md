---
exchange: binance
source_url: https://developers.binance.com/docs/institutional_loan/general-info
api_type: REST
updated_at: 2026-05-27 19:01:30.594796
---

# Get Risk Unit Force Liquidation Record(USER_DATA)

#### API Description[​](/docs/institutional_loan/trade#api-description "Direct link to API Description")

Get Institution Loan Risk Unit Force Liquidation Record. This endpoint is accessible only with the credit account API key.

#### HTTP Request[​](/docs/institutional_loan/trade#http-request "Direct link to HTTP Request")

GET /sapi/v1/margin/loan-group/force-liquidation

#### Request Weight[​](/docs/institutional_loan/trade#request-weight "Direct link to Request Weight")

1(IP)

#### Request Parameters[​](/docs/institutional_loan/trade#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
groupId| LONG| NO| Risk unit unique identifier  
startTime| LONG| NO|   
  
endTime| LONG| NO|   
  
current| LONG| NO| The currently querying page. Start from 1. Default:1  
size| LONG| NO| Default:10 Max:100  
recvWindow| LONG| NO| The value cannot be greater than 60000  
timestamp| LONG| YES|   
  
  
  * Credit account may query currently activated and closed risk unit based on the parameter groupId. If groupId is empty, only currently activated risk units will be returned.
  * Responses are returned in descending order.
  * If startTime and endTime are not provided, data from the last 7 days will be returned by default.
  * If startTime is omitted, it defaults to endTime minus 7 days.
  * If endTime is omitted, it defaults to the current time.
  * The time span between startTime and endTime must not exceed 100 days; otherwise, an error will be returned with no records.



#### Response Example[​](/docs/institutional_loan/trade#response-example "Direct link to Response Example")
    
    
    {  
      "total": 2,  
      "rows": [  
        {  
          "groupId": 6,  
          "startLtv": 1,  
          "endLtv": 0,  
          "liquidationStartTime": 1748381716906,  
          "liquidationEndTime": 1748525848742,  
          "totalNetEquity": 16671.5507973,  
          "totalMaintenanceMargin": 0,  
          "totalLiability": 16667.926,  
          "liquidationSnapshot": {  
            "snapshots": [  
              {  
                "subEmail": "1000255973134@test.com",  
                "memberType": "CREDIT",  
                "walletType": "PORTFOLIO_MARGIN",  
                "netEquity": "12671.05079731",  
                "maintainMargin": "0E-8"  
              },  
              {  
                "subEmail": "1000255973134@test.com",  
                "memberType": "CREDIT",  
                "walletType": "SPOT",  
                "netEquity": "0E-8",  
                "maintainMargin": "0E-8"  
              },  
              {  
                "subEmail": "1000255973138@test.com",  
                "memberType": "COLLATERAL",  
                "walletType": "PORTFOLIO_MARGIN",  
                "netEquity": "1000.25333000",  
                "maintainMargin": "0E-8"  
              },  
              {  
                "subEmail": "1000255973137@test.com",  
                "memberType": "COLLATERAL",  
                "walletType": "PORTFOLIO_MARGIN",  
                "netEquity": "1000.24667000",  
                "maintainMargin": "0E-8"  
              },  
              {  
                "subEmail": "1000255973135@test.com",  
                "memberType": "COLLATERAL",  
                "walletType": "CROSS_MARGIN",  
                "netEquity": "1000.00000000",  
                "maintainMargin": "0E-8"  
              },  
              {  
                "subEmail": "1000255973136@test.com",  
                "memberType": "COLLATERAL",  
                "walletType": "CROSS_MARGIN",  
                "netEquity": "1000.00000000",  
                "maintainMargin": "0E-8"  
              }  
            ],  
            "liabilities":   
              {"assetName": "USDT",  
                "principal": "11667.92600000",  
                "interest": "5000.00000000"  
              }  
          }  
        }  
      ]  
    }  
    

## Response detail description:[​](/docs/institutional_loan/trade#response-detail-description "Direct link to Response detail description:")

Parameter| Type| Description  
---|---|---  
total| LONG| Total risk unit number  
rows| OBJECT ARRAY|   
→ groupId| Long| Risk unit unique identifier  
→ startLtv| LONG| The initial LTV for the risk unit  
→ endLtv| LONG| The current LTV for the risk unit  
→ liquidationStartTime| Long| Liquidation start timestamp (milliseconds)  
→ liquidationEndTime| Long| Liquidation end timestamp (milliseconds)  
→ totalNetEquity| String| ∑Equity in all PM sub account + ( ∑Collateral Value - ∑(Liability + Interest) in all Cross Margin account + Free accepted tokens in spot  
→totalMaintenanceMargin| String| Aggregated Maintenance Margin  
→ totalLiability| String| Outstanding Loan Principal + Outstanding Loan Interest  
liquidationSnapshot| OBJECT ARRAY|   
snapshots| OBJECT ARRAY|   
→ subEmail| String| Sub account registered email  
→ memberType| String| memberType can be "CREDIT" or "COLLATERAL"  
→ walletType| String| Account type for sub account . It can be "PORTFOLIO_MARGIN", "SPOT" or "CROSS_MARGIN"  
→ netEquity| String| Net equity in wallet  
→ maintainMargin| String| Maintenance margin required  
liabilities| OBJECT ARRAY|   
→ assetName| String| Asset name  
→ principal| String| Outstanding loan principal amount  
→ interest| String| Outstanding loan interest

---

# 查询风险单元强制平仓记录 (USER_DATA)

#### 接口描述[​](/docs/zh-CN/institutional_loan/trade#接口描述 "接口描述的直接链接")

获取风险单位强制平仓记录。 仅支持放贷账户调用该接口。

#### HTTP请求[​](/docs/zh-CN/institutional_loan/trade#http请求 "HTTP请求的直接链接")

GET /sapi/v1/margin/loan-group/force-liquidation

#### 请求权重[​](/docs/zh-CN/institutional_loan/trade#请求权重 "请求权重的直接链接")

1(IP)

#### 请求参数[​](/docs/zh-CN/institutional_loan/trade#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
groupId| LONG| NO| 唯一风险单位标识符  
startTime| LONG| NO| 开始时间  
endTime| LONG| NO| 结束时间  
current| LONG| NO| 当前查询页。 开始值 1. 默认:1  
size| LONG| NO| 默认:10 最大:100  
recvWindow| LONG| NO|   
  
timestamp| LONG| YES|   
  
  
  * 放贷账户可根据参数groupId查询当前生效状态 风险单位和已经关闭的风险单位，若groupId为空，则返回当前生效状态 的风险单位。
  * 响应返回为降序排列。
  * 若startTime和endTime没传，则默认返回最近7天数据。
  * startTime不传，默认endTime-7天；结束时间不传，默认当前时间。
  * startTime和endTime时间长度不能超过100天，否则报错，无返回记录。



#### 响应示例[​](/docs/zh-CN/institutional_loan/trade#响应示例 "响应示例的直接链接")
    
    
    {  
      "total": 2,  
      "rows": [  
        {  
          "groupId": 6,  
          "startLtv": 1,  
          "endLtv": 0,  
          "liquidationStartTime": 1748381716906,  
          "liquidationEndTime": 1748525848742,  
          "totalNetEquity": 16671.5507973,  
          "totalMaintenanceMargin": 0,  
          "totalLiability": 16667.926,  
          "liquidationSnapshot": {  
            "snapshots": [  
              {  
                "subEmail": "1000255973134@test.com",  
                "memberType": "CREDIT",  
                "walletType": "PORTFOLIO_MARGIN",  
                "netEquity": "12671.05079731",  
                "maintainMargin": "0E-8"  
              },  
              {  
                "subEmail": "1000255973134@test.com",  
                "memberType": "CREDIT",  
                "walletType": "SPOT",  
                "netEquity": "0E-8",  
                "maintainMargin": "0E-8"  
              },  
              {  
                "subEmail": "1000255973138@test.com",  
                "memberType": "COLLATERAL",  
                "walletType": "PORTFOLIO_MARGIN",  
                "netEquity": "1000.25333000",  
                "maintainMargin": "0E-8"  
              },  
              {  
                "subEmail": "1000255973137@test.com",  
                "memberType": "COLLATERAL",  
                "walletType": "PORTFOLIO_MARGIN",  
                "netEquity": "1000.24667000",  
                "maintainMargin": "0E-8"  
              },  
              {  
                "subEmail": "1000255973135@test.com",  
                "memberType": "COLLATERAL",  
                "walletType": "CROSS_MARGIN",  
                "netEquity": "1000.00000000",  
                "maintainMargin": "0E-8"  
              },  
              {  
                "subEmail": "1000255973136@test.com",  
                "memberType": "COLLATERAL",  
                "walletType": "CROSS_MARGIN",  
                "netEquity": "1000.00000000",  
                "maintainMargin": "0E-8"  
              }  
            ],  
            "liabilities":   
              {"assetName": "USDT",  
                "principal": "11667.92600000",  
                "interest": "5000.00000000"  
              }  
          }  
        }  
      ]  
    }  
    

## Response detail description:[​](/docs/zh-CN/institutional_loan/trade#response-detail-description "Response detail description:的直接链接")

Parameter| Type| Description  
---|---|---  
total| LONG| 风险单位数量  
rows| OBJECT ARRAY|   
→ groupId| Long| 唯一风险单位标识符  
→ startLtv| LONG| 初始贷款价值比  
→ endLtv| LONG| 最新贷款价值比  
→ liquidationStartTime| Long| 强平开始时间 (毫秒)  
→ liquidationEndTime| Long| 强平结束时间 (毫秒)  
→ totalNetEquity| String| Σ所有统一账户子账户抵押品权益 + Σ 抵押品价值 - Σ 全仓杠杆账户（负债 + 利息） + 现货可用资产  
→totalMaintenanceMargin| String| 维持保证金总额  
→ totalLiability| String| 未偿还贷款本金 + 未偿还贷款利息  
liquidationSnapshot| OBJECT ARRAY|   
snapshots| OBJECT ARRAY|   
→ subEmail| String| Sub account registered email  
→ memberType| String| 子账号类型，可取值"CREDIT" 或 "COLLATERAL"  
→ walletType| String| 钱包类型，可取值 "PORTFOLIO_MARGIN", "SPOT" 或 "CROSS_MARGIN"  
→ netEquity| String| 账户净资产  
→ maintainMargin| String| 维持保证金  
liabilities| OBJECT ARRAY|   
→ assetName| String| 币种名称  
→ principal| String| 未偿还贷款本金  
→ interest| String| 未偿还利息