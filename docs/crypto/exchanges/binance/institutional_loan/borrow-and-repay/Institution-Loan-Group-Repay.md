---
exchange: binance
source_url: https://developers.binance.com/docs/institutional_loan/borrow-and-repay/Institution-Loan-Group-Repay
api_type: REST
updated_at: 2026-05-27 19:01:20.561677
---

# Query Interest Rebate Balance Records(USER_DATA)

## API Description[​](/docs/institutional_loan/borrow-and-repay/Institution-Loan-Interest-Rebate-Balance-Records#api-description "Direct link to API Description")

Query change records for an institutional loan interest rebate balance. Includes ADD (admin grant), DEDUCT (admin deduction), and INTEREST_OFFSET (system interest deduction) types.

## HTTP Request[​](/docs/institutional_loan/borrow-and-repay/Institution-Loan-Interest-Rebate-Balance-Records#http-request "Direct link to HTTP Request")

GET /sapi/v1/margin/loan-group/interest-rebate-balance/records (HMAC SHA256)

## Request Weight[​](/docs/institutional_loan/borrow-and-repay/Institution-Loan-Interest-Rebate-Balance-Records#request-weight "Direct link to Request Weight")

100(IP)

## Request Parameters[​](/docs/institutional_loan/borrow-and-repay/Institution-Loan-Interest-Rebate-Balance-Records#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
type| INT| NO| Record type filter: 0=ADD, 1=DEDUCT, 2=INTEREST_OFFSET. Returns all if not specified.  
startTime| LONG| NO| Start time in ms  
endTime| LONG| NO| End time in ms  
current| LONG| NO| Page number, default 1  
size| LONG| NO| Page size, default 10, max 100  
  
## Response Example[​](/docs/institutional_loan/borrow-and-repay/Institution-Loan-Interest-Rebate-Balance-Records#response-example "Direct link to Response Example")
    
    
    {  
      "total": 3,  
      "rows": [  
        {  
          "type": "ADD",  
          "rebateAsset": "USDT",  
          "delta": "5000.00000000",  
          "createTime": 1711843200000  
        },  
        {  
          "type": "DEDUCT",  
          "rebateAsset": "USDT",  
          "delta": "-1000.00000000",  
          "createTime": 1712016000000  
        },  
        {  
          "type": "INTEREST_OFFSET",  
          "groupId": 10005,  
          "rebateAsset": "USDT",  
          "delta": "-50.12345678",  
          "liabilityAsset": "BTC",  
          "deductedInterest": "0.00050123",  
          "exchangeRate": "0.00001000",  
          "createTime": 1712102400000  
        }  
      ]  
    }  
    

## Response detail description[​](/docs/institutional_loan/borrow-and-repay/Institution-Loan-Interest-Rebate-Balance-Records#response-detail-description "Direct link to Response detail description")

Parameter| Type| Description  
---|---|---  
total| LONG| Total number of records  
rows| ARRAY| Record list  
-> type| STRING| ADD / DEDUCT / INTEREST_OFFSET  
-> groupId| LONG| Loan group ID (only for INTEREST_OFFSET)  
-> rebateAsset| STRING| Rebate asset (USDT)  
-> delta| STRING| Amount change. Positive for ADD, negative for DEDUCT/INTEREST_OFFSET  
-> liabilityAsset| STRING| Liability asset (only for INTEREST_OFFSET)  
-> deductedInterest| STRING| Deducted interest in liability asset (only for INTEREST_OFFSET)  
-> exchangeRate| STRING| Exchange rate snapshot (only for INTEREST_OFFSET)  
-> createTime| LONG| Record creation time in ms

---

# 查询利息减免额度变动记录 (USER_DATA)

## 接口描述[​](/docs/zh-CN/institutional_loan/borrow-and-repay/Institution-Loan-Interest-Rebate-Balance-Records#接口描述 "接口描述的直接链接")

查询机构贷利息减免额度的加减流水。包括发放(ADD)、扣减(DEDUCT)、利息抵扣(INTEREST_OFFSET)三种类型。

## HTTP 请求[​](/docs/zh-CN/institutional_loan/borrow-and-repay/Institution-Loan-Interest-Rebate-Balance-Records#http-请求 "HTTP 请求的直接链接")

GET /sapi/v1/margin/loan-group/interest-rebate-balance/records (HMAC SHA256)

## 请求权重[​](/docs/zh-CN/institutional_loan/borrow-and-repay/Institution-Loan-Interest-Rebate-Balance-Records#请求权重 "请求权重的直接链接")

100(IP)

## 请求参数[​](/docs/zh-CN/institutional_loan/borrow-and-repay/Institution-Loan-Interest-Rebate-Balance-Records#请求参数 "请求参数的直�接链接")

名称| 类型| 是否必须| 描述  
---|---|---|---  
type| INT| 否| 记录类型筛选: 0=发放, 1=扣减, 2=利息抵扣。不传则返回全部。  
startTime| LONG| 否| 开始时间（毫秒）  
endTime| LONG| 否| 结束时间（毫秒）  
current| LONG| 否| 页码，默认 1  
size| LONG| 否| 每页数量，默认 10，最大 100  
  
## 响应示例[​](/docs/zh-CN/institutional_loan/borrow-and-repay/Institution-Loan-Interest-Rebate-Balance-Records#响应示例 "响应示例的直接链接")
    
    
    {  
      "total": 3,  
      "rows": [  
        {  
          "type": "ADD",  
          "rebateAsset": "USDT",  
          "delta": "5000.00000000",  
          "createTime": 1711843200000  
        },  
        {  
          "type": "DEDUCT",  
          "rebateAsset": "USDT",  
          "delta": "-1000.00000000",  
          "createTime": 1712016000000  
        },  
        {  
          "type": "INTEREST_OFFSET",  
          "groupId": 10005,  
          "rebateAsset": "USDT",  
          "delta": "-50.12345678",  
          "liabilityAsset": "BTC",  
          "deductedInterest": "0.00050123",  
          "exchangeRate": "0.00001000",  
          "createTime": 1712102400000  
        }  
      ]  
    }  
    

## 响应信息详解：[​](/docs/zh-CN/institutional_loan/borrow-and-repay/Institution-Loan-Interest-Rebate-Balance-Records#响应信息详解 "响应信息详解：的直接链接")

参数| 类型| 描述  
---|---|---  
total| LONG| 记录总数  
rows| ARRAY| 记录列表  
-> type| STRING| 发放(ADD) / 扣减(DEDUCT) / 利息抵扣(INTEREST_OFFSET)  
-> groupId| LONG| 贷款组 ID（仅利息抵扣）  
-> rebateAsset| STRING| 额度币种（USDT）  
-> delta| STRING| 变动金额。发放为正，扣减/抵扣为负  
-> liabilityAsset| STRING| 负债币种（仅利息抵扣）  
-> deductedInterest| STRING| 抵扣利息金额，以负债币种计（仅利息抵扣）  
-> exchangeRate| STRING| 汇率快照（仅利息抵扣）  
-> createTime| LONG| 记录创建时间（毫秒）