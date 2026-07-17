---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#affiliate-rest-api-get-the-invitee-39-s-detail
anchor_id: affiliate-rest-api-get-the-invitee-39-s-detail
api_type: REST
updated_at: 2026-07-17 19:18:23.056820
---

# Get the invitee's detail

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

---

# 获取被邀请人返佣信息

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