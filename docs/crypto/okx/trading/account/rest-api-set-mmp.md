---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#trading-account-rest-api-set-mmp
anchor_id: trading-account-rest-api-set-mmp
api_type: REST
updated_at: 2026-07-10 19:30:24.080910
---

# Set MMP

This endpoint is used to set MMP configure  
  
  
Only applicable to Option in Portfolio Margin mode, and MMP privilege is required.

  
What is MMP?  
Market Maker Protection (MMP) is an automated mechanism for market makers to pull their quotes when their executions exceed a certain threshold(`qtyLimit`) within a certain time frame(`timeInterval`). Once mmp is triggered, any pre-existing mmp pending orders(`mmp` and `mmp_and_post_only` orders) will be automatically canceled, and new orders tagged as MMP will be rejected for a specific duration(`frozenInterval`), or until manual reset by makers.  
  
How to enable MMP?  
Please send an email to institutional@okx.com or contact your business development (BD) manager to apply for MMP. The initial threshold will be upon your request. 

#### Rate Limit: 2 requests per 10 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/account/mmp-config`

> Request Example
    
    
    POST /api/v5/account/mmp-config
    body
    {
        "instFamily":"BTC-USD",
        "timeInterval":"5000",
        "frozenInterval":"2000",
        "qtyLimit": "100"
    }
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instFamily | String | Yes | Instrument family  
timeInterval | String | Yes | Time window (ms). MMP interval where monitoring is done  
"0" means disable MMP  
frozenInterval | String | Yes | Frozen period (ms).   
"0" means the trade will remain frozen until you request "Reset MMP Status" to unfrozen  
qtyLimit | String | Yes | Trade qty limit in number of contracts  
Must be > 0  
  
> Response Example
    
    
    {
      "code": "0",
      "msg": "",
      "data": [
        {
            "frozenInterval":"2000",
            "instFamily":"BTC-USD",
            "qtyLimit": "100",
            "timeInterval":"5000"
        }
      ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
instFamily | String | Instrument family  
timeInterval | String | Time window (ms). MMP interval where monitoring is done  
frozenInterval | String | Frozen period (ms).  
qtyLimit | String | Trade qty limit in number of contracts

---

# 设置 MMP

可以使用该接口进行 MMP 的配置。  
仅适用于组合保证金账户模式下的期权订单，且有 MMP 权限。  
  
  
什么是MMP?  
做市商保护(MMP)机制保护做市商在一定时间内成交过多。当做市商保护触发时，即做市商在一定时间内(`timeInterval`)成交超过某阈值(`qtyLimit`)，系统会自动撤销所有MMP挂单(`mmp`和`mmp_and_post_only`挂单)，拒绝任何新的MMP订单直到某个时间(MMP最近一次触发时间+`frozenInterval`)或做市商主动重置。  
  
如何申请MMP?  
请发邮件至 institutional@okx.com 或者联系您的客户经理进行申请。 

#### 限速：2次/10s

#### 限速规则：User ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/account/mmp-config`

> 请求示例
    
    
    POST /api/v5/account/mmp-config
    body
    {
        "instFamily":"BTC-USD",
        "timeInterval":"5000",
        "frozenInterval":"2000",
        "qtyLimit": "100"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instFamily | String | 是 | 交易品种  
timeInterval | String | 是 | 时间窗口 (毫秒)。  
"0" 代表停用 MMP  
frozenInterval | String | 是 | 冻结时间长度 (毫秒)。   
"0" 代表一直冻结，直到调用 "重置 MMP 状态" 接口解冻  
qtyLimit | String | 是 | 成交数量的上限  
需大于 0  
  
> 返回结果
    
    
    {
      "code": "0",
      "msg": "",
      "data": [
        {
            "frozenInterval":"2000",
            "instFamily":"BTC-USD",
            "qtyLimit": "100",
            "timeInterval":"5000"
        }
      ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
instFamily | String | 交易品种  
timeInterval | String | 时间窗口 (毫秒)  
frozenInterval | String | 冻结时间长度 (毫秒)  
qtyLimit | String | 成交张数的上限