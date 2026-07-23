---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#affiliate-rest-api-get-invitee-list
anchor_id: affiliate-rest-api-get-invitee-list
api_type: REST
updated_at: 2026-07-23 19:23:28.728130
---

# Get invitee list

Paginated invitee list with trading stats and KYC info.  
  
#### Rate Limit: 3 requests per second

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/affiliate/invitee/list`

> Request Example
    
    
    GET /api/v5/affiliate/invitee/list?page=1&kycStatus=verified
    

#### Request Parameters

**Parameter** | **Type** | **Required** | **Description**  
---|---|---|---  
page | String | No | 1-indexed page number. Non-numeric values fall back to `1`. The default is `1`.  
limit | String | No | Items per page. Clamped to `[1, 100]`. The default is `100`.  
periodType | String | No | Stats window.  
`last_7d`  
`last_30d`  
`this_month`  
`last_month`  
`total`  
`today`  
`this_week`  
`custom`: pass `begin` and `end` to define a custom window.  
begin | String | Conditional | Custom stats-window start, Unix timestamp in millisecond format. Required when `periodType=custom`, together with `end`. Inclusive.  
end | String | Conditional | Custom stats-window end, Unix timestamp in millisecond format. Required when `periodType=custom`, together with `begin`. Inclusive.  
keyword | String | No | Search by UID or channel name.  
commissionCategory | String | No | Commission calculation category.  
`SPOT`  
`DERIVATIVE`  
`BSC`  
orderBy | String | No | Sort field.  
`cTime`  
`depAmt`  
`vol`  
`fee`  
`rebate`  
The default is `cTime`.  
orderDir | String | No | Sort direction.  
`asc`  
`desc`  
The default is `desc`.  
kycStatus | String | No | KYC status.  
`unverified`  
`verified` (passed at least KYC2)  
subAffiliateUid | String | No | Filter invitees under a specific sub-affiliate (external UID).  
  
When `periodType=custom`, supply both `begin` and `end`. Supplying only one returns `50014`.  
For all other `periodType` values, server-defined windows are used and any `begin` / `end` passed alongside are ignored. The window between `begin` and `end` must not exceed 90 days. `begin` cannot be earlier than 180 days from now.

> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "totalPage": "5",
        "data": [
            {
                "uid": "835449167911924693",
                "country": "CN",
                "joinTime": "1777448564000",
                "firstTradeTime": "",
                "channelName": "X2UWA2T89",
                "rebateRate": "0.1600",
                "feeTierRank": "0",
                "kycStatus": "verified",
                "kycTime": "1777448563000",
                "depAmt": "0.0000000000",
                "totalVol": "0.0000000000",
                "totalFee": "0.0000000000",
                "totalCommission": "0.0000000000",
                "isCompliant": true
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
totalPage | String | Total number of pages under the current filters and `limit`. Same level as `data` in the response.  
uid | String | External user UID.  
country | String | ISO 3166-1 alpha-2 country code of the invitee's residence, e.g. `KR`, `CN`. Empty string when residence is not set.  
joinTime | String | Relationship established timestamp, Unix timestamp in millisecond format.  
firstTradeTime | String | First trade timestamp, Unix timestamp in millisecond format. `""` if never traded.  
channelName | String | Affiliate channel name used at registration.  
rebateRate | String | Invitee's effective rebate rate from the active rebate calculation rule (in decimal), e.g. `0.1000` represents `10%`.  
feeTierRank | String | Cross-category fee tier ranking integer (`0` = lowest, `13` = highest). Does not distinguish regular vs VIP — for the categorized label use `level` on [Get the invitee's detail](/docs-v5/en/#affiliate-rest-api-get-the-invitee-39-s-detail).  
kycStatus | String | KYC status.  
`unverified`  
`verified`  
kycTime | String | KYC2 verification timestamp, Unix timestamp in millisecond format. `""` if user has not passed KYC2.  
depAmt | String | Total deposit amount, unit in `USDT`.  
totalVol | String | Total trading volume, unit in `USDT`.  
totalFee | String | Total trading fees, unit in `USDT`.  
totalCommission | String | Total commission earned from this invitee, unit in `USDT`.  
isCompliant | Boolean | Whether the invitee is permitted under regional compliance rules.  
`true`: unrestricted  
`false`: restricted due to KYC entity or jurisdiction (e.g. sanctioned region)

---

# 获取直客列表

分页获取直客列表，包含交易统计与 KYC 信息。  
  
#### 限速：3次/s

#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/affiliate/invitee/list`

> 请求示例
    
    
    GET /api/v5/affiliate/invitee/list?page=1&kycStatus=verified
    

#### 请求参数

**参数名** | **类型** | **是否必须** | **描述**  
---|---|---|---  
page | String | 否 | 1 起始的页码，非数字回退为 `1`。默认为 `1`。  
limit | String | 否 | 每页数量，限定在 `[1, 100]`。默认为 `100`。  
periodType | String | 否 | 统计窗口。  
`last_7d`  
`last_30d`  
`this_month`  
`last_month`  
`total`  
`today`  
`this_week`  
`custom`：自定义窗口，需配合 `begin` 与 `end` 使用。  
begin | String | 条件必填 | 自定义统计窗口起始时间，Unix时间戳的毫秒数格式。当 `periodType=custom` 时必填，需与 `end` 同时传入。包含端点。  
end | String | 条件必填 | 自定义统计窗口结束时间，Unix时间戳的毫秒数格式。当 `periodType=custom` 时必填，需与 `begin` 同时传入。包含端点。  
keyword | String | 否 | 按直客 UID 或渠道名搜索。  
commissionCategory | String | 否 | 返佣计算类别。  
`SPOT`  
`DERIVATIVE`  
`BSC`  
orderBy | String | 否 | 排序字段。  
`cTime`  
`depAmt`  
`vol`  
`fee`  
`rebate`  
默认为 `cTime`  
orderDir | String | 否 | 排序方向。  
`asc`  
`desc`  
默认为 `desc`  
kycStatus | String | 否 | KYC 状态。  
`unverified`：未通过  
`verified`：至少通过 KYC2  
subAffiliateUid | String | 否 | 按指定二级节点（外部 UID）筛选其直客。  
  
当 `periodType=custom` 时，需同时传 `begin` 和 `end`，仅传一个会返回 `50014`。  
其他 `periodType` 值使用服务端预设窗口，与之同时传入的 `begin` / `end` 将被忽略。`begin` 与 `end` 区间不得超过 90 天，`begin` 不得早于当前时间 180 天前。

> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "totalPage": "5",
        "data": [
            {
                "uid": "835449167911924693",
                "country": "CN",
                "joinTime": "1777448564000",
                "firstTradeTime": "",
                "channelName": "X2UWA2T89",
                "rebateRate": "0.1600",
                "feeTierRank": "0",
                "kycStatus": "verified",
                "kycTime": "1777448563000",
                "depAmt": "0.0000000000",
                "totalVol": "0.0000000000",
                "totalFee": "0.0000000000",
                "totalCommission": "0.0000000000",
                "isCompliant": true
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
totalPage | String | 当前过滤条件与 `limit` 下的总页数，与 `data` 在响应中同级。  
uid | String | 直客的外部 UID。  
country | String | 直客所在地的 ISO 3166-1 alpha-2 国家/地区码，如 `KR`、`CN`。未设置时返回空字符串。  
joinTime | String | 返佣关系建立时间，Unix时间戳的毫秒数格式。  
firstTradeTime | String | 首次交易时间，Unix时间戳的毫秒数格式。如未交易，返回 `""`。  
channelName | String | 注册时使用的节点渠道名。  
rebateRate | String | 直客在当前返佣规则下的实际返佣比例（小数形式），如 `0.1000` 表示 `10%`。  
feeTierRank | String | 跨类别手续费等级排名整数（`0` 最低，`13` 最高）。不区分常规/VIP——分类标签请使用 [获取被邀请人返佣信息](/docs-v5/zh/#affiliate-rest-api-get-the-invitee-39-s-detail) 中的 `level`。  
kycStatus | String | KYC 状态。  
`unverified`  
`verified`  
kycTime | String | KYC2 认证时间，Unix时间戳的毫秒数格式。如未通过 KYC2，返回 `""`。  
depAmt | String | 累计充值金额，单位为 `USDT`。  
totalVol | String | 累计交易量，单位为 `USDT`。  
totalFee | String | 累计交易手续费，单位为 `USDT`。  
totalCommission | String | 来自该直客的累计返佣，单位为 `USDT`。  
isCompliant | Boolean | 该直客是否符合区域合规要求。  
`true`：无限制  
`false`：因 KYC 主体或司法辖区受限（如制裁地区）