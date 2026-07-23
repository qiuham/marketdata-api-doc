---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#affiliate-rest-api
anchor_id: affiliate-rest-api
api_type: REST
updated_at: 2026-07-23 19:23:27.795232
---

# REST API

### Get performance summary  
  
Aggregated affiliate performance metrics for a specified time period.

#### Rate Limit: 3 requests per second

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/affiliate/performance/summary`

> Request Example
    
    
    GET /api/v5/affiliate/performance/summary?periodType=total
    

#### Request Parameters

**Parameter** | **Type** | **Required** | **Description**  
---|---|---|---  
periodType | String | No | Stats window for all summary fields except `uTime`.  
`last_7d`  
`last_30d`  
`this_month`  
`last_month`  
`total`  
`today`  
`this_week`  
`custom`: pass `begin` and `end` to define a custom window.  
The default is `total`.  
begin | String | Conditional | Custom stats-window start, Unix timestamp in millisecond format. Required when `periodType=custom`, together with `end`. Inclusive.  
end | String | Conditional | Custom stats-window end, Unix timestamp in millisecond format. Required when `periodType=custom`, together with `begin`. Inclusive.  
  
When `periodType=custom`, supply both `begin` and `end`. Supplying only one returns `50014`.  
For all other `periodType` values, server-defined windows are used and any `begin` / `end` passed alongside are ignored.  
`periodType` / `begin` / `end` filter the statistics window for all summary fields (`inviteeCnt`, `depAmt`, `details.*`). `uTime` always reflects the latest data snapshot regardless of the window.

> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "uTime": "1777541513000",
                "inviteeCnt": "102",
                "depAmt": "1756.287846940199989393",
                "details": [
                    {
                        "commissionCategory": "SPOT",
                        "firstTraderCnt": "17",
                        "traderCnt": "17",
                        "vol": "21548.6417826825604",
                        "commission": "3.322319946747010328"
                    },
                    {
                        "commissionCategory": "DERIVATIVE",
                        "firstTraderCnt": "9",
                        "traderCnt": "9",
                        "vol": "94531.94802",
                        "commission": "3.25142568535855"
                    },
                    {
                        "commissionCategory": "BSC",
                        "firstTraderCnt": "0",
                        "traderCnt": "0",
                        "vol": "0",
                        "commission": "0"
                    }
                ]
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
uTime | String | Last data update timestamp, Unix timestamp in millisecond format.  
inviteeCnt | String | Total number of invitees.  
depAmt | String | Total deposit amount, unit in `USDT`.  
details | Array of objects | One entry per instrument bucket.  
> commissionCategory | String | Commission calculation category.  
`SPOT`  
`DERIVATIVE`  
`BSC`  
> firstTraderCnt | String | Count of invitees whose lifetime-first trade occurred within the selected window, scoped to this `commissionCategory`. Each invitee can contribute at most once in their lifetime.  
> traderCnt | String | Number of invitees who traded in this `commissionCategory` bucket within the selected window. Period-scoped.  
> vol | String | Trading volume in this `commissionCategory` bucket within the selected window, unit in `USDT`. Period-scoped — distinct from `totalVol` on `/invitee/list` and `/sub-affiliate/list` which is lifetime cumulative.  
> commission | String | Commission earned in this `commissionCategory` bucket within the selected window, unit in `USDT`. Period-scoped — distinct from `totalCommission` on other endpoints which is lifetime cumulative.  
  
### Get the invitee's detail

#### Rate Limit: 3 requests per second

#### Rate limit rule: User ID

#### HTTP request

`GET /api/v5/affiliate/invitee/detail`

> Request sample
    
    
    GET /api/v5/affiliate/invitee/detail?uid=11111111
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
uid | String | Yes | UID of the invitee. Only applicable to the UID of invitee master account.   
The data returned covers invitee master account and invitee sub-accounts.  
  
> Returned results
    
    
    {
        "msg": "",
        "code": "0",
        "data": [
            {
                "accFee": "0",
                "affiliateCode": "HIIIIII",
                "depAmt": "0",
                "wdAmt": "0",
                "firstTradeTime": "",
                "inviteeLevel": "2",
                "inviteeRebateRate": "0.39",
                "joinTime": "1712546713000",
                "kycTime": "",
                "level": "Lv1",
                "region": "Vietnam",
                "totalCommission": "0",
                "volMonth": "0",
                "totalVol": "0"
            }
        ]
    }
    

#### Response parameters

**Parameter name** | **Type** | **Description**  
---|---|---  
inviteeLevel | String | Invitee's relative level to the affiliate  
If the user is a invitee, the level will be `2`.  
joinTime | String | Timestamp that the rebate relationship is established, Unix timestamp in millisecond format, e.g. `1597026383085`  
inviteeRebateRate | String | Self rebate rate of the invitee (in decimal), e.g. `0.01` represents `1%`  
totalCommission | String | Total commission earned from the invitee, unit in `USDT`  
firstTradeTime | String | Timestamp that the first trade is completed after the latest rebate relationship is established with the parent affiliate  
Unix timestamp in millisecond format, e.g. 1597026383085  
If user has not traded, "" will be returned  
level | String | Invitee trading fee level, e.g. Lv1  
depAmt | String | Accumulated amount of deposit in USDT  
If user has not deposited, 0 will be returned  
wdAmt | String | Accumulated amount of withdrawal in USDT  
If user has not withdrawn, 0 will be returned  
volMonth | String | Accumulated Trading volume in the current month in USDT  
If user has not traded, 0 will be returned  
totalVol | String | Lifetime accumulated trading volume in USDT  
If user has not traded, 0 will be returned  
accFee | String | Accumulated Amount of trading fee in USDT  
If there is no any fee, 0 will be returned  
kycTime | String | KYC2 verification time. Unix timestamp in millisecond format and the precision is in day  
If user has not passed KYC2, "" will be returned  
region | String | User country or region. e.g. "United Kingdom"  
affiliateCode | String | Affiliate invite code that the invitee registered/recalled via  
  
### Get invitee list

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
  
### Get link list

Paginated affiliate invite links with commission rates and stats.

#### Rate Limit: 3 requests per second

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/affiliate/link/list`

> Request Example
    
    
    GET /api/v5/affiliate/link/list
    

#### Request Parameters

**Parameter** | **Type** | **Required** | **Description**  
---|---|---|---  
page | String | No | 1-indexed page number. Non-numeric values fall back to `1`. The default is `1`.  
limit | String | No | Items per page. Clamped to `[1, 100]`. The default is `100`.  
linkType | String | No | Link kind filter.  
`standard`: regular affiliate invite link  
`co_inviter`: co-inviter shared link  
linkStatus | String | No | Link status.  
`normal`  
`abnormal`  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "totalPage": "1",
        "data": [
            {
                "channelId": "78295211",
                "channelName": "78295211",
                "joinLink": "https://okx.com/join/78295211",
                "linkType": "standard",
                "inviterCommissionRate": "0.2900",
                "coInviterCommissionRate": "",
                "inviteeDiscountRate": "0.0100",
                "inviteeCnt": "1",
                "traderCnt": "1",
                "totalCommission": "2.656307",
                "commission24h": "0.5",
                "cTime": "1773739123000",
                "isDefault": true,
                "linkStatus": "normal"
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
totalPage | String | Total number of pages under the current filters and `limit`. Same level as `data` in the response.  
channelId | String | Unique channel/link ID.  
channelName | String | User-defined link name.  
joinLink | String | Shareable invitation URL.  
linkType | String | Link kind.  
`standard`: regular affiliate invite link  
`co_inviter`: co-inviter shared link  
inviterCommissionRate | String | Parent inviter's commission rate (the link owner's), in decimal.  
coInviterCommissionRate | String | Co-inviter's commission rate (in decimal). Empty string for standard links.  
inviteeDiscountRate | String | Invitee rebate rate template configured on this affiliate link (in decimal), applied to invitees registering via this link.  
inviteeCnt | String | Number of invitees from this link.  
traderCnt | String | Number of invitees who traded.  
totalCommission | String | Cumulative commission, unit in `USDT`.  
commission24h | String | Commission earned in the rolling past 24 hours, unit in `USDT`. Independent of `periodType` / `begin` / `end` filters.  
cTime | String | Link creation timestamp, Unix timestamp in millisecond format.  
isDefault | Boolean | Whether this is the default link.  
linkStatus | String | Link status.  
`normal`  
`abnormal`  
  
### Get co-inviter link list

Co-inviter links where the authenticated user is the co-inviter.

#### Rate Limit: 3 requests per second

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/affiliate/co-inviter/list`

> Request Example
    
    
    GET /api/v5/affiliate/co-inviter/list
    

#### Request Parameters

**Parameter** | **Type** | **Required** | **Description**  
---|---|---|---  
page | String | No | 1-indexed page number. Non-numeric values fall back to `1`. The default is `1`.  
limit | String | No | Items per page. Clamped to `[1, 100]`. The default is `100`.  
linkStatus | String | No | Link status.  
`normal`  
`abnormal`  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "totalPage": "1",
        "data": [
            {
                "channelId": "31075853",
                "channelName": "MXCUS",
                "joinLink": "https://okx.com/join/MXCUS",
                "inviterCommissionRate": "0.0000",
                "coInviterCommissionRate": "0.1400",
                "inviteeDiscountRate": "0.1600",
                "parUserName": "12****23",
                "coUserName": "***",
                "isCompliant": true,
                "isDefault": false,
                "totalCommission": "0.032111",
                "commission24h": "0",
                "inviteeCnt": "1",
                "traderCnt": "1",
                "clickCnt": "1",
                "totalFee": "0",
                "cTime": "1773739123000",
                "channelAssessmentStatus": "valid",
                "inviterChannelStatus": "valid",
                "coInviterChannelStatus": "valid",
                "linkStatus": "normal"
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
totalPage | String | Total number of pages under the current filters and `limit`. Same level as `data` in the response.  
channelId | String | Channel ID.  
channelName | String | Channel name.  
joinLink | String | Shareable invitation URL.  
inviterCommissionRate | String | Parent inviter's commission rate, in decimal.  
coInviterCommissionRate | String | Co-inviter's commission rate, in decimal (the caller's, since the caller is the co-inviter on this endpoint).  
inviteeDiscountRate | String | Invitee rebate rate template configured on this affiliate link (in decimal), applied to invitees registering via this link.  
parUserName | String | Partner affiliate's username string (partially masked, not a UID).  
coUserName | String | Co-inviter's username placeholder, always fully masked as `***` (PII fully hidden, not a UID).  
isCompliant | Boolean | Whether the co-inviter is permitted under regional compliance rules.  
`true`: unrestricted  
`false`: restricted due to KYC entity or jurisdiction  
note | String | Optional channel note set by the affiliate (free-form text, may be empty `""`).  
isDefault | Boolean | Whether this is the default co-inviter link.  
totalCommission | String | Total commission, unit in `USDT`.  
commission24h | String | Commission earned in the rolling past 24 hours, unit in `USDT`. Independent of `periodType` / `begin` / `end` filters.  
inviteeCnt | String | Number of invitees.  
traderCnt | String | Number of invitees who placed at least one trade.  
clickCnt | String | Number of times the affiliate link was clicked (click count).  
totalFee | String | Total service fees, unit in `USDT`.  
cTime | String | Link creation timestamp, Unix timestamp in millisecond format.  
channelAssessmentStatus | String | Channel assessment result (trade + invite metrics).  
`valid`: all assessment metrics met  
`not_reach_trade`: trade metric unmet  
`not_reach_invite`: invite metric unmet  
`not_reach_both`: both unmet  
inviterChannelStatus | String | Parent inviter's channel compliance.  
`valid`: parent inviter is compliant  
`identity_invalid`: parent inviter's identity has been revoked  
`level_downgraded`: parent inviter's level has been reduced to 0  
coInviterChannelStatus | String | Co-inviter's channel compliance (compound: identity × assessment).  
`valid`  
`identity_invalid`  
`not_reach_assessment`  
`identity_invalid_and_not_reach_assessment`  
linkStatus | String | Link status.  
`normal`  
`abnormal`  
  
### Get sub-affiliate list

Paginated sub-affiliates under current user.

#### Rate Limit: 3 requests per second

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/affiliate/sub-affiliate/list`

> Request Example
    
    
    GET /api/v5/affiliate/sub-affiliate/list
    

#### Request Parameters

**Parameter** | **Type** | **Required** | **Description**  
---|---|---|---  
page | String | No | 1-indexed page number. Non-numeric values fall back to `1`. The default is `1`.  
limit | String | No | Items per page. Clamped to `[1, 100]`. The default is `100`.  
keyword | String | No | Search by sub-affiliate UID.  
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
The default sorts by `joinTime` (most recently joined first).  
orderDir | String | No | Sort direction.  
`asc`  
`desc`  
The default is `desc`.  
  
The endpoint reports lifetime data.  
Sort is stable: ties on `orderBy` are broken by `subAffiliateUid` ascending. Safe to paginate large result sets without losing or duplicating rows.

> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "totalPage": "1",
        "data": [
            {
                "subAffiliateUid": "668418489887292061",
                "country": "CN",
                "joinTime": "1773739123000",
                "subAffiliateLevel": "2",
                "commissionRate": "0.3000",
                "isCompliant": true,
                "inviteeCnt": "8",
                "traderCnt": "3",
                "depAmt": "37.281133",
                "totalVol": "3618.561430",
                "totalFee": "1.628353",
                "totalCommission": "0.289847"
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
totalPage | String | Total number of pages under the current filters and `limit`. Same level as `data` in the response.  
subAffiliateUid | String | External UID of the sub-affiliate.  
country | String | ISO 3166-1 alpha-2 country code of the sub-affiliate's residence, e.g. `CN`. Empty string when residence is not set.  
joinTime | String | Timestamp the user was registered as a sub-affiliate, Unix timestamp in millisecond format.  
subAffiliateLevel | String | Depth of this sub-affiliate relative to the caller.  
`2`: direct sub-affiliate (caller's L1 child)  
`3`: indirect sub-affiliate, 1 level below a direct sub-affiliate  
commissionRate | String | Sub-affiliate's commission rate, in decimal.  
isCompliant | Boolean | Whether the sub-affiliate is permitted under regional compliance rules.  
`true`: unrestricted  
`false`: restricted due to KYC entity or jurisdiction (e.g. sanctioned region)  
inviteeCnt | String | Direct invitees of the sub-affiliate.  
traderCnt | String | Sub-affiliate's invitees who traded.  
depAmt | String | Total deposit from invitees, unit in `USDT`.  
totalVol | String | Total trading volume from invitees, unit in `USDT`.  
totalFee | String | Total trading fees from invitees, unit in `USDT`.  
totalCommission | String | Your commission earned from this sub-affiliate's invitees, unit in `USDT`.

---

# REST API

### 获取节点业绩概览   
  
获取指定时间窗口内节点的业绩聚合指标。

#### 限速：3次/s

#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/affiliate/performance/summary`

> 请求示例
    
    
    GET /api/v5/affiliate/performance/summary?periodType=total
    

#### 请求参数

**参数名** | **类型** | **是否必须** | **描述**  
---|---|---|---  
periodType | String | 否 | 统计窗口（仅 `uTime` 不受影响）。  
`last_7d`  
`last_30d`  
`this_month`  
`last_month`  
`total`  
`today`  
`this_week`  
`custom`：自定义窗口，需配合 `begin` 与 `end` 使用。  
默认为 `total`  
begin | String | 条件必填 | 自定义统计窗口起始时间，Unix时间戳的毫秒数格式。当 `periodType=custom` 时必填，需与 `end` 同时传入。包含端点。  
end | String | 条件必填 | 自定义统计窗口结束时间，Unix时间戳的毫秒数格式。当 `periodType=custom` 时必填，需与 `begin` 同时传入。包含端点。  
  
当 `periodType=custom` 时，需同时传 `begin` 和 `end`，仅传一个会返回 `50014`。  
其他 `periodType` 值使用服务端预设窗口，与之同时传入的 `begin` / `end` 将被忽略。  
`periodType` / `begin` / `end` 仅作用于 `inviteeCnt`、`depAmt`、`details.*` 等汇总字段，`uTime` 始终返回最新数据快照时间，与窗口无关。

> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "uTime": "1777541513000",
                "inviteeCnt": "102",
                "depAmt": "1756.287846940199989393",
                "details": [
                    {
                        "commissionCategory": "SPOT",
                        "firstTraderCnt": "17",
                        "traderCnt": "17",
                        "vol": "21548.6417826825604",
                        "commission": "3.322319946747010328"
                    },
                    {
                        "commissionCategory": "DERIVATIVE",
                        "firstTraderCnt": "9",
                        "traderCnt": "9",
                        "vol": "94531.94802",
                        "commission": "3.25142568535855"
                    },
                    {
                        "commissionCategory": "BSC",
                        "firstTraderCnt": "0",
                        "traderCnt": "0",
                        "vol": "0",
                        "commission": "0"
                    }
                ]
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
uTime | String | 数据最近更新时间，Unix时间戳的毫秒数格式。  
inviteeCnt | String | 直客总数。  
depAmt | String | 累计充值金额，单位为 `USDT`。  
details | Array of objects | 按业务类别拆分的明细，每个类别一条。  
> commissionCategory | String | 返佣计算类别。  
`SPOT`：现货  
`DERIVATIVE`：衍生品  
`BSC`：返佣业务  
> firstTraderCnt | String | 在选定窗口内首次交易的直客数（按 `commissionCategory` 维度）。每个直客在生命周期内最多统计一次。  
> traderCnt | String | 选定窗口内在该 `commissionCategory` 下产生交易的直客数。按窗口统计。  
> vol | String | 选定窗口内该 `commissionCategory` 下的交易量，单位为 `USDT`。按窗口统计——区别于 `/invitee/list`、`/sub-affiliate/list` 中的 `totalVol`（生命周期累计）。  
> commission | String | 选定窗口内该 `commissionCategory` 下的返佣，单位为 `USDT`。按窗口统计——区别于其他接口中的 `totalCommission`（生命周期累计）。  
  
### 获取被邀请人返佣信息 

#### 限速：3次/s

#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/affiliate/invitee/detail`

> 请求示例
    
    
    GET /api/v5/affiliate/invitee/detail?uid=11111111
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
uid | String | 是 | 被邀请人UID，仅支持使用被邀请人母账号的 UID  
返回数据中涵盖了被邀请人母账户和子账户。  
  
> 返回结果
    
    
    {
        "msg": "",
        "code": "0",
        "data": [
            {
                "accFee": "0",
                "affiliateCode": "HIIIIII",
                "depAmt": "0",
                "wdAmt": "0",
                "firstTradeTime": "",
                "inviteeLevel": "2",
                "inviteeRebateRate": "0.39",
                "joinTime": "1712546713000",
                "kycTime": "",
                "level": "Lv1",
                "region": "越南",
                "totalCommission": "0",
                "volMonth": "0",
                "totalVol": "0"
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
inviteeLevel | String | 被邀请人的节点层级  
直客返回`2`  
joinTime | String | 返佣关系建立的时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
inviteeRebateRate | String | 返佣比例(小数形式)，如 `0.01`代表`1%`  
totalCommission | String | 总返佣数量，单位为`USDT`  
firstTradeTime | String | 首次交易时间（在最近的返佣关系建立之后）  
Unix时间戳的毫秒数格式，如 1597026383085  
如果用户没有交易, 返回 ""  
level | String | 当前在平台上真实交易量的用户等级，如 Lv1  
depAmt | String | 累计充值金额，单位为 USDT  
如果没有充值, 返回 0  
wdAmt | String | 累计提现金额，单位为 USDT  
如果没有提现, 返回 0  
volMonth | String | 当月累计交易量，单位为 USDT  
如果没有交易, 返回 0  
totalVol | String | 生命周期累计交易量，单位为 USDT  
如果没有交易, 返回 0  
accFee | String | 累计交易手续费，单位为 USDT  
如果没有交易手续费，返回 0  
kycTime | String | KYC2 认证时间. Unix时间戳的毫秒数格式，且精确到天  
如果没有通过 KYC2, 返回 ""  
region | String | 国家或地区，如"英国"  
affiliateCode | String | 节点邀请码  
  
### 获取直客列表 

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
  
### 获取邀请链接列表 

分页获取节点的邀请链接，包括返佣比例与统计数据。

#### 限速：3次/s

#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/affiliate/link/list`

> 请求示例
    
    
    GET /api/v5/affiliate/link/list
    

#### 请求参数

**参数名** | **类型** | **是否必须** | **描述**  
---|---|---|---  
page | String | 否 | 1 起始的页码，非数字回退为 `1`。默认为 `1`。  
limit | String | 否 | 每页数量，限定在 `[1, 100]`。默认为 `100`。  
linkType | String | 否 | 链接类型筛选。  
`standard`：常规节点邀请链接  
`co_inviter`：联合邀请人共享链接  
linkStatus | String | 否 | 链接状态。  
`normal`  
`abnormal`  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "totalPage": "1",
        "data": [
            {
                "channelId": "78295211",
                "channelName": "78295211",
                "joinLink": "https://okx.com/join/78295211",
                "linkType": "standard",
                "inviterCommissionRate": "0.2900",
                "coInviterCommissionRate": "",
                "inviteeDiscountRate": "0.0100",
                "inviteeCnt": "1",
                "traderCnt": "1",
                "totalCommission": "2.656307",
                "commission24h": "0.5",
                "cTime": "1773739123000",
                "isDefault": true,
                "linkStatus": "normal"
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
totalPage | String | 当前过滤条件与 `limit` 下的总页数，与 `data` 在响应中同级。  
channelId | String | 渠道/链接唯一 ID。  
channelName | String | 用户自定义的链接名称。  
joinLink | String | 可分享的邀请 URL。  
linkType | String | 链接类型。  
`standard`：常规节点邀请链接  
`co_inviter`：联合邀请人共享链接  
inviterCommissionRate | String | 父级邀请人（链接所有者）的返佣比例，小数形式。  
coInviterCommissionRate | String | 联合邀请人的返佣比例，小数形式。常规链接为空字符串。  
inviteeDiscountRate | String | 该链接配置的直客返佣比例模板（小数形式），适用于通过该链接注册的直客。  
inviteeCnt | String | 通过该链接邀请的直客数。  
traderCnt | String | 已交易的直客数。  
totalCommission | String | 累计返佣，单位为 `USDT`。  
commission24h | String | 滚动近 24 小时返佣，单位为 `USDT`。不受 `periodType` / `begin` / `end` 过滤影响。  
cTime | String | 链接创建时间，Unix时间戳的毫秒数格式。  
isDefault | Boolean | 是否为默认链接。  
linkStatus | String | 链接状态。  
`normal`  
`abnormal`  
  
### 获取联合邀请人链接列表 

获取当前用户作为联合邀请人的链接列表。

#### 限速：3次/s

#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/affiliate/co-inviter/list`

> 请求示例
    
    
    GET /api/v5/affiliate/co-inviter/list
    

#### 请求参数

**参数名** | **类型** | **是否必须** | **描述**  
---|---|---|---  
page | String | 否 | 1 起始的页码，非数字回退为 `1`。默认为 `1`。  
limit | String | 否 | 每页数量，限定在 `[1, 100]`。默认为 `100`。  
linkStatus | String | 否 | 链接状态。  
`normal`  
`abnormal`  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "totalPage": "1",
        "data": [
            {
                "channelId": "31075853",
                "channelName": "MXCUS",
                "joinLink": "https://okx.com/join/MXCUS",
                "inviterCommissionRate": "0.0000",
                "coInviterCommissionRate": "0.1400",
                "inviteeDiscountRate": "0.1600",
                "parUserName": "12****23",
                "coUserName": "***",
                "isCompliant": true,
                "isDefault": false,
                "totalCommission": "0.032111",
                "commission24h": "0",
                "inviteeCnt": "1",
                "traderCnt": "1",
                "clickCnt": "1",
                "totalFee": "0",
                "cTime": "1773739123000",
                "channelAssessmentStatus": "valid",
                "inviterChannelStatus": "valid",
                "coInviterChannelStatus": "valid",
                "linkStatus": "normal"
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
totalPage | String | 当前过滤条件与 `limit` 下的总页数，与 `data` 在响应中同级。  
channelId | String | 渠道 ID。  
channelName | String | 渠道名。  
joinLink | String | 可分享的邀请 URL。  
inviterCommissionRate | String | 父级邀请人的返佣比例，小数形式。  
coInviterCommissionRate | String | 联合邀请人的返佣比例，小数形式（即调用方，因为该接口下调用方是联合邀请人）。  
inviteeDiscountRate | String | 该链接配置的直客返佣比例模板（小数形式），适用于通过该链接注册的直客。  
parUserName | String | 合作节点的用户名（部分脱敏，非 UID）。  
coUserName | String | 联合邀请人的用户名占位，恒为完全脱敏的 `***`（PII 完全隐藏，非 UID）。  
isCompliant | Boolean | 联合邀请人是否符合区域合规要求。  
`true`：无限制  
`false`：因 KYC 主体或司法辖区受限  
note | String | 节点对该渠道的可选备注（自由文本，可能为 `""`）。  
isDefault | Boolean | 是否为默认联合邀请人链接。  
totalCommission | String | 累计返佣，单位为 `USDT`。  
commission24h | String | 滚动近 24 小时返佣，单位为 `USDT`。不受 `periodType` / `begin` / `end` 过滤影响。  
inviteeCnt | String | 直客数。  
traderCnt | String | 至少完成一次交易的直客数。  
clickCnt | String | 邀请链接被点击次数。  
totalFee | String | 累计服务费，单位为 `USDT`。  
cTime | String | 链接创建时间，Unix时间戳的毫秒数格式。  
channelAssessmentStatus | String | 渠道考核结果（交易+邀请指标）。  
`valid`：所有考核指标达标  
`not_reach_trade`：交易指标未达标  
`not_reach_invite`：邀请指标未达标  
`not_reach_both`：两项均未达标  
inviterChannelStatus | String | 父级邀请人渠道合规状态。  
`valid`：父级邀请人合规  
`identity_invalid`：父级邀请人身份已失效  
`level_downgraded`：父级邀请人等级已降为 0  
coInviterChannelStatus | String | 联合邀请人渠道合规状态（身份 × 考核 复合）。  
`valid`  
`identity_invalid`  
`not_reach_assessment`  
`identity_invalid_and_not_reach_assessment`  
linkStatus | String | 链接状态。  
`normal`  
`abnormal`  
  
### 获取二级节点列表 

分页获取当前用户下的二级节点。

#### 限速：3次/s

#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/affiliate/sub-affiliate/list`

> 请求示例
    
    
    GET /api/v5/affiliate/sub-affiliate/list
    

#### 请求参数

**参数名** | **类型** | **是否必须** | **描述**  
---|---|---|---  
page | String | 否 | 1 起始的页码，非数字回退为 `1`。默认为 `1`。  
limit | String | 否 | 每页数量，限定在 `[1, 100]`。默认为 `100`。  
keyword | String | 否 | 按二级节点 UID 搜索。  
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
默认按 `joinTime` 倒序（最近加入的优先）。  
orderDir | String | 否 | 排序方向。  
`asc`  
`desc`  
默认为 `desc`  
  
该接口返回的是生命周期累计数据。  
排序具有稳定性：当 `orderBy` 出现并列时，按 `subAffiliateUid` 升序作为次序。可安全分页大数据集，不会丢行或重复。

> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "totalPage": "1",
        "data": [
            {
                "subAffiliateUid": "668418489887292061",
                "country": "CN",
                "joinTime": "1773739123000",
                "subAffiliateLevel": "2",
                "commissionRate": "0.3000",
                "isCompliant": true,
                "inviteeCnt": "8",
                "traderCnt": "3",
                "depAmt": "37.281133",
                "totalVol": "3618.561430",
                "totalFee": "1.628353",
                "totalCommission": "0.289847"
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
totalPage | String | 当前过滤条件与 `limit` 下的总页数，与 `data` 在响应中同级。  
subAffiliateUid | String | 二级节点的外部 UID。  
country | String | 二级节点所在地的 ISO 3166-1 alpha-2 国家/地区码，如 `CN`。未设置时返回空字符串。  
joinTime | String | 注册为二级节点的时间，Unix时间戳的毫秒数格式。  
subAffiliateLevel | String | 相对调用方的层级深度。  
`2`：直接二级节点（调用方的 L1 子节点）  
`3`：间接二级节点，位于直接二级节点下一层  
commissionRate | String | 二级节点的返佣比例，小数形式。  
isCompliant | Boolean | 二级节点是否符合区域合规要求。  
`true`：无限制  
`false`：因 KYC 主体或司法辖区受限（如制裁地区）  
inviteeCnt | String | 二级节点的直客数。  
traderCnt | String | 二级节点中已交易的直客数。  
depAmt | String | 直客累计充值金额，单位为 `USDT`。  
totalVol | String | 直客累计交易量，单位为 `USDT`。  
totalFee | String | 直客累计交易手续费，单位为 `USDT`。  
totalCommission | String | 您从该二级节点直客中获得的累计返佣，单位为 `USDT`。