---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#affiliate-rest-api-get-co-inviter-link-list
anchor_id: affiliate-rest-api-get-co-inviter-link-list
api_type: REST
updated_at: 2026-05-27 19:37:04.769129
---

# Get co-inviter link list

Co-inviter links where the authenticated user is the co-inviter.  
  
#### Rate Limit: 3 requests per second

#### Rate limit rule: User ID

#### Permission: Read

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

---

# 获取联合邀请人链接列表

获取当前用户作为联合邀请人的链接列表。  
  
#### 限速：3次/s

#### 限速规则：User ID

#### 权限：读取

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