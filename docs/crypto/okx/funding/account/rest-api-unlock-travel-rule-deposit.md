---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#funding-account-rest-api-unlock-travel-rule-deposit
anchor_id: funding-account-rest-api-unlock-travel-rule-deposit
api_type: REST
updated_at: 2026-11-24 18:58:35.364244
---

# Unlock Travel Rule deposit

Submit originator information to unlock a deposit locked under the Travel Rule. If the deposit has already been unlocked, the request returns success without re-processing.  
  
#### Rate Limit: 3 requests per second

#### Rate limit rule: User ID + IP

#### Permission: Withdraw

#### HTTP Request

`POST /api/v5/asset/travel-rule/unlock`

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
depId | String | Yes | Locked deposit ID  
questionnaire | Object | Yes | Originator information. Required keys depend on the user's entity.  
> personType | String | Yes | Originator type. `1`: self (the depositor is the account holder); `2`: third party.  
> walletType | String | Yes | Source wallet type. `exchange`: exchange wallet; `private`: private wallet.  
> exchId | String | Conditional | Source exchange ID from [Get exchange list (public)](/docs-v5/en/#funding-account-rest-api-get-exchange-list-public). Use `0` if the exchange is not listed. Required when `walletType` = `exchange`.  
> exchName | String | Conditional | Source exchange name, e.g. `Example Exchange`. Required when `exchId` = `0`.  
> origFirstName | String | Conditional | Originator first name. Required for a natural person if `origCompanyName` is not provided.  
> origLastName | String | Conditional | Originator last name. Required for a natural person if `origCompanyName` is not provided.  
> origCompanyName | String | Conditional | Originator company name. Required for a legal entity if `origFirstName` and `origLastName` are not provided.  
> origCountry | String | Conditional | Originator country of residence, or country of registration for a legal entity. ISO 3166-1 alpha-2 code, e.g. `SG`.  
> origGeoAddress | String | Conditional | Full address on one line: street, town/city, state/province, postal code.  
> origDob | String | Conditional | Originator date of birth, or date of incorporation / registration for a legal entity, `YYYY-MM-DD`.  
> origPob | String | Conditional | Originator place of birth, or country of registration for a legal entity. ISO 3166-1 alpha-2 code, e.g. `SG`.  
> origNationality | String | Conditional | Originator nationality. ISO 3166-1 alpha-2 code, e.g. `SG`. Required for a natural person.  
> brazilClassificationCode | String | Conditional | Transfer purpose code. For deposits below USD 50,000, use an Annex I code. For deposits of USD 50,000 or more, use an Annex II code. Optional for OKX Brazil users for now; will become required.  
  
> Request Example
    
    
    POST /api/v5/asset/travel-rule/unlock
    body
    
    
    
    {
      "depId": "1234567890",
      "questionnaire": {
        "personType": "2",
        "walletType": "exchange",
        "exchId": "0",
        "exchName": "Example Exchange",
        "origFirstName": "Alex",
        "origLastName": "Chen",
        "origCountry": "SG",
        "origGeoAddress": "123 Main St, Singapore 018956",
        "origDob": "1990-01-01",
        "origPob": "SG"
      }
    }
    

> Response Example
    
    
    {
      "code": "0",
      "data": [{"result": true}],
      "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
result | Boolean | `true`: unlock accepted — deposit released or was already unlocked.  
Empty `data` array: unlock failed — deposit remains locked.

---

# 解锁国际转账规则充值

提交发起人信息以解锁因国际转账规则而被锁定的充值。如果充值已经解锁，则直接返回成功，不重复处理。  
  
#### 限速：3次/s

#### 限速规则：User ID + IP

#### 权限：提币

#### HTTP 请求

`POST /api/v5/asset/travel-rule/unlock`

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
depId | String | 是 | 被锁定的充值 ID  
questionnaire | Object | 是 | 发起人信息。所需字段取决于用户所属实体。  
> personType | String | 是 | 发起人类型。`1`：本人（存款人即账户持有人）；`2`：第三方。  
> walletType | String | 是 | 来源钱包类型。`exchange`：交易所钱包；`private`：私人钱包。  
> exchId | String | 条件必填 | 来源交易所 ID，可通过[获取交易所列表（公共）](/docs-v5/zh/#funding-account-rest-api-get-exchange-list-public)查询；未列出的交易所使用 `0`。当 `walletType` = `exchange` 时必填。  
> exchName | String | 条件必填 | 来源交易所名称，如 `Example Exchange`。当 `exchId` = `0` 时必填。  
> origFirstName | String | 条件必填 | 发起人名字。自然人未提供 `origCompanyName` 时必填。  
> origLastName | String | 条件必填 | 发起人姓氏。自然人未提供 `origCompanyName` 时必填。  
> origCompanyName | String | 条件必填 | 发起人公司名称。法人实体未提供 `origFirstName` 和 `origLastName` 时必填。  
> origCountry | String | 条件必填 | 发起人居住国家；法人实体填写注册国家。ISO 3166-1 alpha-2 代码，如 `SG`。  
> origGeoAddress | String | 条件必填 | 单行完整地址：街道、城镇/城市、州/省、邮政编码。  
> origDob | String | 条件必填 | 发起人出生日期；法人实体填写注册/成立日期，格式为 `YYYY-MM-DD`。  
> origPob | String | 条件必填 | 发起人出生地；法人实体填写注册国家。ISO 3166-1 alpha-2 代码，如 `SG`。  
> origNationality | String | 条件必填 | 发起人国籍。ISO 3166-1 alpha-2 代码，如 `SG`。自然人必填。  
> brazilClassificationCode | String | 条件必填 | 转账用途代码。充值金额低于 50,000 USD 时使用 Annex I 代码；达到或超过 50,000 USD 时使用 Annex II 代码。OKX Brazil 用户目前可选，后续将改为必填。  
  
> 请求示例
    
    
    POST /api/v5/asset/travel-rule/unlock
    body
    
    
    
    {
      "depId": "1234567890",
      "questionnaire": {
        "personType": "2",
        "walletType": "exchange",
        "exchId": "0",
        "exchName": "Example Exchange",
        "origFirstName": "Alex",
        "origLastName": "Chen",
        "origCountry": "SG",
        "origGeoAddress": "123 Main St, Singapore 018956",
        "origDob": "1990-01-01",
        "origPob": "SG"
      }
    }
    

> 返回示例
    
    
    {
      "code": "0",
      "data": [{"result": true}],
      "msg": ""
    }
    

#### 返回参数

参数 | 类型 | 描述  
---|---|---  
result | Boolean | `true`：接受解锁请求，充值已释放或已提前解锁。  
空 `data` 数组：解锁失败，充值仍处于锁定状态。