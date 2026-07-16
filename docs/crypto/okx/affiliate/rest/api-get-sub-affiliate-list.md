---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#affiliate-rest-api-get-sub-affiliate-list
anchor_id: affiliate-rest-api-get-sub-affiliate-list
api_type: REST
updated_at: 2026-07-16 19:22:01.961952
---

# Get sub-affiliate list

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

# 获取二级节点列表

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