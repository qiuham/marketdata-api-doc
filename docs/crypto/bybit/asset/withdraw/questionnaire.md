---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/asset/withdraw/questionnaire
api_type: REST
updated_at: 2026-11-13 19:21:53.382725
---

# Questionnaire

The `questionnaire` field is a JSON string used to carry Travel Rule compliance information in both the [Submit Deposit Originator Info](/docs/v5/asset/deposit/submit-info) and [Withdraw](/docs/v5/asset/withdraw) endpoints. It replaces the legacy `beneficiary` \+ `transactionPurpose` combination for new integrations.

info

  * Max length: **16384 bytes**
  * When both `questionnaire` and the legacy `beneficiary`/`transactionPurpose` fields are present, **`questionnaire` takes precedence**
  * Field names use **lowerCamelCase** (e.g. `walletType`, `poiIssuingCountry`)
  * Country codes follow **ISO 3166-1 alpha-3** (e.g. `JPN`, `TUR`, `KAZ`, `IND`)
  * Dates follow **ISO 8601** short format `YYYY-MM-DD`



### Common Fields

The following fields apply to all compliance zones.

Field| Type| Required| Comments  
---|---|---|---  
walletType| integer| **true**|  Wallet type. `0`: custodial/VASP wallet. `1`: non-custodial (personal) wallet  
legalType| string| **true**|  Entity type. `individual`: natural person. `company`: legal entity / institution  
vaspCode| string(64)| Conditional| Counterparty VASP code. **Required** when `walletType=0`. Use `others` if not matched. Retrieve valid codes via the VASP List API  
isSelfWallet| bool| false| Whether the wallet belongs to the user themselves. For non-custodial wallets only  
firstName| string(128)| Conditional| First name. **Required** when `legalType=individual`  
lastName| string(128)| Conditional| Last name. **Required** when `legalType=individual`  
companyName| string(256)| Conditional| Company / institution name. **Required** when `legalType=company`  
  
### Regional Field Differences

#### EU (MiCA / TFR)

Common fields plus:

Field| Type| Required| Comments  
---|---|---|---  
transactionPurpose| string(20,500)| **true**|  Transaction purpose. Minimum 20 characters  
  
#### TUR — Turkey (MASAK)

Common fields plus all four POI document fields:

Field| Type| Required| Comments  
---|---|---|---  
poiType| string(32)| **true**|  Document type. `ID_CARD` / `PASSPORT` / `DRIVERS` / `RESIDENCE_PERMIT` / `OTHER`  
poiNumber| string(64)| **true**|  Document number  
poiIssuingCountry| string(10)| **true**|  Document issuing country, three-letter country code  
poiExpiredDate| string(20)| **true**|  Document expiry date, `YYYY-MM-DD`  
transactionPurpose| string(20,500)| **true**|  Transaction purpose. Minimum 20 characters  
  
#### KAZ — Kazakhstan (AFSA)

Common fields plus all four POI document fields:

Field| Type| Required| Comments  
---|---|---|---  
poiType| string(32)| **true**|  Document type. `ID_CARD` / `PASSPORT` / `DRIVERS` / `RESIDENCE_PERMIT` / `OTHER`  
poiNumber| string(64)| **true**|  Document number  
poiIssuingCountry| string(10)| **true**|  Document issuing country, three-letter country code  
poiExpiredDate| string(20)| **true**|  Document expiry date, `YYYY-MM-DD`  
  
#### BYBIT-IND — India (FIU-IND)

Common fields only. No additional required fields.

#### BYBIT-KOR — Korea (SAFA) — Withdrawal only

Common fields plus:

Field| Type| Required| Comments  
---|---|---|---  
representativeFirstName| string(128)| Conditional| Company representative first name. **Required when`legalType=company`** (Korean SAFA requirement)  
representativeLastName| string(128)| Conditional| Company representative last name. **Required when`legalType=company`** (Korean SAFA requirement)  
  
note

Korean entity **deposit side** does not use this questionnaire — it is handled separately via the local bank / CTP channel.

### Compliance Zone Coverage

Entity Code| Region| Withdrawal| Deposit| Notes  
---|---|---|---|---  
EU| EU| ✅| ✅| MiCA / TFR  
TUR| Turkey| ✅| ✅| MASAK — POI required  
KAZ| Kazakhstan| ✅| ✅| AFSA — POI required  
BYBIT-IND| India| ✅| ✅| FIU-IND  
BYBIT-KOR| Korea| ✅| ❌| SAFA — company representative required for withdrawal; deposit handled via local bank / CTP  
  
### Examples

#### EU — Individual + Custodial Wallet
    
    
    {  
      "walletType": 0,  
      "vaspCode": "BINANCEUS_VASP",  
      "legalType": "individual",  
      "firstName": "John",  
      "lastName": "Smith",  
      "transactionPurpose": "Personal investment in long-term holdings"  
    }  
    

#### TUR — Individual + Non-Custodial Wallet
    
    
    {  
      "walletType": 1,  
      "legalType": "individual",  
      "firstName": "Ahmet",  
      "lastName": "Yilmaz",  
      "poiType": "ID_CARD",  
      "poiNumber": "12345678901",  
      "poiIssuingCountry": "TUR",  
      "poiExpiredDate": "2030-06-15",  
      "transactionPurpose": "Long-term holding for retirement savings purpose"  
    }  
    

#### KAZ — Company + Custodial Wallet
    
    
    {  
      "walletType": 0,  
      "vaspCode": "EXAMPLE_VASP",  
      "legalType": "company",  
      "companyName": "Example LLC",  
      "poiType": "OTHER",  
      "poiNumber": "BIN1234567890",  
      "poiIssuingCountry": "KAZ",  
      "poiExpiredDate": "2099-12-31"  
    }  
    

#### BYBIT-IND — Individual + Non-Custodial Wallet
    
    
    {  
      "walletType": 1,  
      "legalType": "individual",  
      "firstName": "Rahul",  
      "lastName": "Sharma"  
    }  
    

#### BYBIT-KOR — Company + Custodial Wallet (Withdrawal only)
    
    
    {  
      "walletType": 0,  
      "vaspCode": "EXAMPLE_VASP",  
      "legalType": "company",  
      "companyName": "Example Co., Ltd.",  
      "representativeFirstName": "Min-jun",  
      "representativeLastName": "Kim"  
    }

---

# 問卷說明

`questionnaire` 字段是一個 JSON 字符串，用於在[提交入金發起人信息](/docs/zh-TW/v5/asset/deposit/submit-info)和[提現](/docs/zh-TW/v5/asset/withdraw)接口中傳遞 Travel Rule 合規信息。對於新接入，推薦使用此字段替代舊版 `beneficiary` \+ `transactionPurpose` 組合。

信息

  * 最大長度：**16384 字節**
  * 當 `questionnaire` 與舊版 `beneficiary`/`transactionPurpose` 字段同時存在時，**以`questionnaire` 為準**
  * 字段名統一使用 **lowerCamelCase** （如 `walletType`、`poiIssuingCountry`）
  * 國家碼遵循 **ISO 3166-1 alpha-3** （如 `JPN`、`TUR`、`KAZ`、`IND`）
  * 日期使用 **ISO 8601** 短格式 `YYYY-MM-DD`



### 公共字段

以下字段適用於所有合規區。

字段| 類型| 是否必需| 說明  
---|---|---|---  
walletType| integer| **必填**|  錢包類型。`0`：托管錢包（CASP/VASP）。`1`：非托管錢包（個人錢包）  
legalType| string| **必填**|  實體類型。`individual`：自然人。`company`：法人/機構  
vaspCode| string(64)| 條件必填| 對手方 VASP 代碼。**當`walletType=0` 時必填**，未匹配的填 `others`，可通過 VASP List API 查詢  
isSelfWallet| bool| 否| 是否為本人自有錢包，僅非托管錢包場景使用  
firstName| string(128)| 條件必填| 自然人名（First Name）。**當`legalType=individual` 時必填**  
lastName| string(128)| 條件必填| 自然人姓（Last Name）。**當`legalType=individual` 時必填**  
companyName| string(256)| 條件必填| 法人/機構名稱。**當`legalType=company` 時必填**  
  
### 各合規區字段差異

#### EU（歐盟，MiCA / TFR）

公共字段 + 以下：

字段| 類型| 是否必需| 說明  
---|---|---|---  
transactionPurpose| string(20,500)| **必填**|  交易目的，最少 20 個字符  
  
#### TUR — 土耳其（MASAK）

公共字段 + 以下四項 POI 證件字段：

字段| 類型| 是否必需| 說明  
---|---|---|---  
poiType| string(32)| **必填**|  證件類型：`ID_CARD` / `PASSPORT` / `DRIVERS` / `RESIDENCE_PERMIT` / `OTHER`  
poiNumber| string(64)| **必填**|  證件號碼  
poiIssuingCountry| string(10)| **必填**|  簽發國家，三位國家碼  
poiExpiredDate| string(20)| **必填**|  證件有效期，`YYYY-MM-DD`  
transactionPurpose| string(20,500)| **必填**|  交易目的，最少 20 個字符  
  
#### KAZ — 哈薩克斯坦（AFSA）

公共字段 + 以下四項 POI 證件字段：

字段| 類型| 是否必需| 說明  
---|---|---|---  
poiType| string(32)| **必填**|  證件類型：`ID_CARD` / `PASSPORT` / `DRIVERS` / `RESIDENCE_PERMIT` / `OTHER`  
poiNumber| string(64)| **必填**|  證件號碼  
poiIssuingCountry| string(10)| **必填**|  簽發國家，三位國家碼  
poiExpiredDate| string(20)| **必填**|  證件有效期，`YYYY-MM-DD`  
  
#### BYBIT-IND — 印度（FIU-IND）

僅公共字段，無額外必填項。

#### BYBIT-KOR — 韓國（SAFA）— 僅出金

公共字段 + 以下：

字段| 類型| 是否必需| 說明  
---|---|---|---  
representativeFirstName| string(128)| 條件必填| 公司代表人名（First Name）。**當`legalType=company` 時必填**（韓國 SAFA 特殊要求）  
representativeLastName| string(128)| 條件必填| 公司代表人姓（Last Name）。**當`legalType=company` 時必填**（韓國 SAFA 特殊要求）  
  
備註

韓國實體**入金側不採集本問卷** ，由本地銀行 / CTP 鏈路單獨處理。

### 合規區覆蓋矩陣

實體代碼| 地區| 出金| 入金| 備注  
---|---|---|---|---  
EU| 歐盟| ✅| ✅| MiCA / TFR  
TUR| 土耳其| ✅| ✅| MASAK，需 POI 證件  
KAZ| 哈薩克斯坦| ✅| ✅| AFSA，需 POI 證件  
BYBIT-IND| 印度| ✅| ✅| FIU-IND  
BYBIT-KOR| 韓國| ✅| ❌| SAFA，出金需公司代表人；入金走本地銀行/CTP  
  
### 示例

#### EU — 自然人 + 托管錢包
    
    
    {  
      "walletType": 0,  
      "vaspCode": "BINANCEUS_VASP",  
      "legalType": "individual",  
      "firstName": "John",  
      "lastName": "Smith",  
      "transactionPurpose": "Personal investment in long-term holdings"  
    }  
    

#### TUR — 自然人 + 非托管錢包
    
    
    {  
      "walletType": 1,  
      "legalType": "individual",  
      "firstName": "Ahmet",  
      "lastName": "Yilmaz",  
      "poiType": "ID_CARD",  
      "poiNumber": "12345678901",  
      "poiIssuingCountry": "TUR",  
      "poiExpiredDate": "2030-06-15",  
      "transactionPurpose": "Long-term holding for retirement savings purpose"  
    }  
    

#### KAZ — 法人 + 托管錢包
    
    
    {  
      "walletType": 0,  
      "vaspCode": "EXAMPLE_VASP",  
      "legalType": "company",  
      "companyName": "Example LLC",  
      "poiType": "OTHER",  
      "poiNumber": "BIN1234567890",  
      "poiIssuingCountry": "KAZ",  
      "poiExpiredDate": "2099-12-31"  
    }  
    

#### BYBIT-IND — 自然人 + 非托管錢包
    
    
    {  
      "walletType": 1,  
      "legalType": "individual",  
      "firstName": "Rahul",  
      "lastName": "Sharma"  
    }  
    

#### BYBIT-KOR — 法人 + 托管錢包（僅出金）
    
    
    {  
      "walletType": 0,  
      "vaspCode": "EXAMPLE_VASP",  
      "legalType": "company",  
      "companyName": "Example Co., Ltd.",  
      "representativeFirstName": "Min-jun",  
      "representativeLastName": "Kim"  
    }