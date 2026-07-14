---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#trading-account-rest-api-get-mmp-config
anchor_id: trading-account-rest-api-get-mmp-config
api_type: REST
updated_at: 2026-07-14 19:18:51.052881
---

# GET MMP Config

This endpoint is used to get MMP configure information  
  
  
Only applicable to Option in Portfolio Margin mode, and MMP privilege is required.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/account/mmp-config`

> Request Example
    
    
    GET /api/v5/account/mmp-config?instFamily=BTC-USD
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instFamily | String | No | Instrument Family  
  
> Response Example
    
    
    {
      "code": "0",
      "data": [
        {
          "frozenInterval": "2000",
          "instFamily": "ETH-USD",
          "mmpFrozen": true,
          "mmpFrozenUntil": "1000",
          "qtyLimit": "10",
          "timeInterval": "5000"
        }
      ],
      "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
instFamily | String | Instrument Family  
mmpFrozen | Boolean | Whether MMP is currently triggered. `true` or `false`  
mmpFrozenUntil | String | If frozenInterval is configured and mmpFrozen = True, it is the time interval (in ms) when MMP is no longer triggered, otherwise "".  
timeInterval | String | Time window (ms). MMP interval where monitoring is done  
frozenInterval | String | Frozen period (ms). If it is "0", the trade will remain frozen until manually reset and `mmpFrozenUntil` will be "".  
qtyLimit | String | Trade qty limit in number of contracts

---

# 查看 MMP 配置

可以使用该接口获取 MMP 的配置信息。  
仅适用于组合保证金账户模式下的期权订单，且有 MMP 权限。  
  
#### 限速：5次/2s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/account/mmp-config`

> 请求示例
    
    
    GET /api/v5/account/mmp-config?instFamily=BTC-USD
    
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instFamily | String | 否 | 交易品种  
  
> 返回结果
    
    
    {
      "code": "0",
      "data": [
        {
          "frozenInterval": "2000",
          "instFamily": "ETH-USD",
          "mmpFrozen": true,
          "mmpFrozenUntil": "1000",
          "qtyLimit": "10",
          "timeInterval": "5000"
        }
      ],
      "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
instFamily | String | 交易品种  
mmpFrozen | Boolean | 是否 MMP 被触发. `true` 或者 `false`  
mmpFrozenUntil | String | 如果配置了frozenInterval且mmpFrozen = true，则为不再触发MMP时的时间窗口（单位为ms），否则为“”  
timeInterval | String | 时间窗口 (毫秒)  
frozenInterval | String | 冻结时间长度 (毫秒)。   
如果为"0"，代表一直冻结，直到调用 "重置 MMP 状态" 接口解冻，且`mmpFrozenUntil`为 ""。  
qtyLimit | String | 成交张数的上限