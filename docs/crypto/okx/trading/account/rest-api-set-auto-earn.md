---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#trading-account-rest-api-set-auto-earn
anchor_id: trading-account-rest-api-set-auto-earn
api_type: REST
updated_at: 2026-07-02 19:43:02.082066
---

# Set auto earn

Turn on/off auto earn.  
  
#### Rate limit: 2 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/account/set-auto-earn`

> Request example
    
    
    // turn on auto lend
    {
       "earnType": "0",
       "ccy":"BTC",
       "action":"turn_on"
    }
    
    

#### Request parameters

**Parameter** | **Type** | **Required** | **Description**  
---|---|---|---  
earnType | String | No | Auto earn type  
`0`: auto earn (auto lend, auto staking)   
`1`: auto earn (USDG earn)  
The default value is `0`  
ccy | String | Yes | Currency  
action | String | Yes | Auto earn operation action  
`turn_on`: turn on auto earn  
`turn_off`: turn off auto earn  
~~`amend`: amend minimum lending APR, applicable only to earnType `0`~~ (Deprecated)  
apr | String | Optional | ~~Minimum lending APR. Users must pass in this field when earnType is`0` and action is `turn_on/amend`.  
0.01 means 1%, available range 0.01-3.65, increment 0.01~~ (Deprecated)  
  
> Response example
    
    
    {
       "code":"0",
       "msg":"",
       "data":[
          {
             "earnType": "0",
             "ccy":"BTC",
             "action":"turn_on",
             "apr":"0.01"
          }
       ]
    }
    
    

#### Response parameters

**Parameter** | **Type** | **Description**  
---|---|---  
earnType | String | Auto earn type  
`0`: auto earn (auto lend, auto staking)   
`1`: auto earn (USDG earn)  
ccy | String | Currency  
action | String | Auto earn operation action  
`turn_on`  
`turn_off`  
~~`amend`~~ (Deprecated)  
apr | String | ~~Minimum lending APR~~ (Deprecated)

---

# 设置自动赚币

开启/关闭自动赚币  
  
#### 限速：2次/2s

#### 限速规则：User ID

#### HTTP请求

`POST /api/v5/account/set-auto-earn`

> 请求示例
    
    
    // 开启自动赚币
    {
       "earnType": "0",
       "ccy":"BTC",
       "action":"turn_on"
    }
    
    

#### 请求参数

**参数名** | **类型** | **是否必须** | **描述**  
---|---|---|---  
earnType | String | 否 | 自动赚币类型  
`0`: 自动赚币 (自动出借、自动质押)   
`1`: 自动赚币（USDG 赚币）  
默认值为 `0`  
ccy | String | 是 | 币种  
action | String | 是 | 自动赚币操作类型  
`turn_on`: 开启自动赚币  
`turn_off`: 关闭自动赚币  
~~`amend`: 修改最低年化收益率，仅适用于 earnType `0`~~（已弃用）  
apr | String | 可选 | ~~最低年化收益率~~ （已弃用）  
  
> 返回结果
    
    
    {
       "code":"0",
       "msg":"",
       "data":[
          {
             "earnType": "0",
             "ccy":"BTC",
             "action":"turn_on",
             "apr":"0.01"
          }
       ]
    }
    
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
earnType | String | 自动赚币类型  
`0`: 自动赚币 (自动出借、自动质押)   
`1`: 自动赚币（USDG 赚币）  
ccy | String | 币种  
action | Boolean | 自动赚币操作类型  
`turn_on`  
`turn_off`  
~~`amend`~~ （已弃用）  
apr | String | ~~最低年化收益率~~ （已弃用）