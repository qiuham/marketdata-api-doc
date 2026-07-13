---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#block-trading-rest-api-get-mmp-config
anchor_id: block-trading-rest-api-get-mmp-config
api_type: REST
updated_at: 2026-07-13 19:28:21.703266
---

# Get MMP Config

This endpoint is used to get MMP configure information and only applicable to block trading market makers  

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/rfq/mmp-config`

> Request Example
    
    
    GET /api/v5/rfq/mmp-config
    
    

#### Request Parameters

none

> Response Example
    
    
    {
      "code": "0",
      "data": [
        {
          "frozenInterval": "2000",
          "mmpFrozen": true,
          "mmpFrozenUntil": "1000",
          "countLimit": "10",
          "timeInterval": "5000"
        }
      ],
      "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
timeInterval | String | Time window (ms). MMP interval where monitoring is done  
"0" means MMP is diabled  
frozenInterval | String | Frozen period (ms). If it is "0", the trade will remain frozen until manually reset and `mmpFrozenUntil` will be "".  
countLimit | String | Limit in number of execution attempts  
mmpFrozen | Boolean | Whether MMP is currently triggered. `true` or `false`  
mmpFrozenUntil | String | If frozenInterval is not "0" and mmpFrozen = True, it is the time interval (in ms) when MMP is no longer triggered, otherwise ""

---

# 查看 MMP 配置

该接口用于获取 MMP 的配置信息，仅适用于大宗交易中的maker。

#### 限速：5次/2s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/rfq/mmp-config`

> 请求示例
    
    
    GET /api/v5/rfq/mmp-config
    
    

#### 请求参数

none

> 返回结果
    
    
    {
      "code": "0",
      "data": [
        {
          "frozenInterval": "2000",
          "mmpFrozen": true,
          "mmpFrozenUntil": "1000",
          "countLimit": "10",
          "timeInterval": "5000"
        }
      ],
      "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
timeInterval | String | 时间窗口 (毫秒)。  
"0" 代表不使用 MMP。  
frozenInterval | String | 冻结时间长度 (毫秒)。   
如果为"0"，代表一直冻结，直到调用 "重置 MMP 状态" 接口解冻，且`mmpFrozenUntil`为 ""。  
countLimit | String | 尝试执行次数限制  
mmpFrozen | Boolean | MMP 是否被触发。 `true` 或者 `false`  
mmpFrozenUntil | String | 如果配置了 frozenInterval 且 mmpFrozen = `true`，则为不再触发MMP时的时间窗口（单位为ms），否则为""。