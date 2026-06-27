---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/options-trading/account/Account-Funding-Flow
api_type: Account
updated_at: 2026-01-15T23:40:56.533909
---

# Account Funding Flow (USER_DATA)

## API Description[​](/docs/derivatives/options-trading/account/Account-Funding-Flow#api-description "Direct link to API Description")

Query account funding flows.

## HTTP Request[​](/docs/derivatives/options-trading/account/Account-Funding-Flow#http-request "Direct link to HTTP Request")

GET `/eapi/v1/bill`

## Request Weight[​](/docs/derivatives/options-trading/account/Account-Funding-Flow#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/options-trading/account/Account-Funding-Flow#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
currency| STRING| YES| Asset type, only support USDT as of now  
recordId| LONG| NO| Return the recordId and subsequent data, the latest data is returned by default, e.g 100000  
startTime| LONG| NO| Start Time, e.g 1593511200000  
endTime| LONG| NO| End Time, e.g 1593512200000  
limit| INT| NO| Number of result sets returned Default:100 Max:1000  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/derivatives/options-trading/account/Account-Funding-Flow#response-example "Direct link to Response Example")
    
    
    [  
      {  
        "id": 1125899906842624000,  
        "asset": "USDT",              // Asset type  
        "amount": "-0.552",           // Amount (positive numbers represent inflow, negative numbers represent outflow)  
        "type": "FEE",                // type (fees)  
        "createDate": 1592449456000,  // Time  
      },  
      {  
        "id": 1125899906842624000,  
        "asset": "USDT",              // Asset type  
        "amount": "100",              // Amount (positive numbers represent inflow, negative numbers represent outflow)  
        "type": "CONTRACT",           // type (buy/sell contracts)  
        "createDate": 1592449456000,  // Time  
      },  
      {  
        "id": 1125899906842624000,  
        "asset": "USDT",              // Asset type  
        "amount": "10000",            // Amount (positive numbers represent inflow, negative numbers represent outflow)  
        "type": "TRANSFER",           // type（Funds transfer）  
        "createDate": 1592448410000,  // Time  
      }  
    ]

---

# 获取账户资金流水(USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/options-trading/account/Account-Funding-Flow#接口描述 "接口描述的直接链接")

获取期权账户资金流水

## HTTP请求[​](/docs/zh-CN/derivatives/options-trading/account/Account-Funding-Flow#http请求 "HTTP请求的直接链接")

GET `/eapi/v1/bill`

## 请求权重[​](/docs/zh-CN/derivatives/options-trading/account/Account-Funding-Flow#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/options-trading/account/Account-Funding-Flow#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
currency| STRING| YES| 资产类型目前仅支持USDT  
recordId| LONG| NO| 返回该`recordId`及之后的成交，缺省返回最近的成交  
startTime| LONG| NO| 起始时间如1593511200000  
endTime| LONG| NO| 结束时间如1593512200000  
limit| INT| NO| 默认100 最大1000  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/derivatives/options-trading/account/Account-Funding-Flow#响应示例 "响应示例的直接链接")
    
    
    [  
      {  
        "id": 1125899906842624000,  
        "asset": "USDT",              // 资产类型  
        "amount": "-0.552",           // 数量 (正数为流入，负数为流出)  
        "type": "FEE",                // 类型 (手续费)  
        "createDate": 1592449456000,  // 时间  
      },  
      {  
        "id": 1125899906842624000,  
        "asset": "USDT",              // 资产类型  
        "amount": "100",              // 数量 (正数为流入，负数为流出)  
        "type": "CONTRACT",           // 类型(买卖合约)  
        "createDate": 1592449456000,  // 时间  
      },  
      {  
        "id": 1125899906842624000,  
        "asset": "USDT",              // 资产类型  
        "amount": "10000",            // 数量 (正数为流入，负数为流出)  
        "type": "TRANSFER",           // 类型（资金划转）  
        "createDate": 1592448410000,  // 时间  
      }  
    ]