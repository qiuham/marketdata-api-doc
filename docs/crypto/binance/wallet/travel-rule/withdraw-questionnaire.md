---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/wallet/travel-rule/withdraw-questionnaire
api_type: REST
updated_at: 2026-11-13 20:30:57.758383
---

# Withdraw Questionnaire Contents (for existing local entities)

## Local Entities

  * [Japan](/en/docs/products/wallet/travel-rule/withdraw-questionnaire#japan)
  * [Kazakhstan](/en/docs/products/wallet/travel-rule/withdraw-questionnaire#kazakhstan)
  * [New Zealand](/en/docs/products/wallet/travel-rule/withdraw-questionnaire#new-zealand)
  * [Bahrain](/en/docs/products/wallet/travel-rule/withdraw-questionnaire#bahrain)
  * [UAE(United Arab Emirates)](/en/docs/products/wallet/travel-rule/withdraw-questionnaire#uae)
  * [India](/en/docs/products/wallet/travel-rule/withdraw-questionnaire#india)
  * [EU(Poland,France)](/en/docs/products/wallet/travel-rule/withdraw-questionnaire#eupolandfrance)
  * [South Africa](/en/docs/products/wallet/travel-rule/withdraw-questionnaire#south-africa)
  * [Australia](/en/docs/products/wallet/travel-rule/withdraw-questionnaire#australia)
  * [Brazil](/en/docs/products/wallet/travel-rule/withdraw-questionnaire#brazil)



> Please refer to `Check Questionnaire Requirements` if you are unsure of which questionnaire content to be used.

## Japan

Name| Type| Mandatory| Description  
---|---|---|---  
isAddressOwner| INTEGER| YES| 1: Send to myself, 2: Send to another beneficiary.  
bnfType| INTEGER| YES *1| 0: Individual, 1: Corporate/Entity  
kanjiName| STRING| YES *1|   
kanaName| STRING| YES *1|   
latinName| STRING| YES *1| For more information please refer to the `Name restrictions` section in the `appendix`.  
country| STRING| YES| Beneficiary country code, ISO 2 digit, lower case. For more information please refer to the `Countries and Regions` section in the `appendix`.  
city| STRING| YES|   
sendTo| INTEGER| YES| 1: Crypto-asset services provider, 2: Unhosted Wallet  
vasp| STRING| YES *2| Vasp identifier of the beneficiary  
vaspCountry| STRING| YES *2| VASP country code, ISO 2 digit, lower case.  
vaspRegion| STRING| YES *3|   
txnPurpose| INTEGER| YES *4| 1: Purchase of goods within Japan, 2: Inheritance, gift or living expenses, 3: Cross border trade, 4: Investment, 5: Use of services provided by the beneficiary VASP, 6: Loan repayment, 7: Gifts & Donations  
isAttested| BOOLEAN| YES|   
  
>   1. Required when `isAddressOwner` is `2`.
>   2. Required when `sendTo` is `1`.
>   3. Required when `vaspCountry` is `cn`(China) or `ua`(Ukraine).
>      1. If `vaspCountry` is `cn`(China), `vaspRegion` must be `notNortheasternProvinces` (Jilin, Liaoning and Heilongjiang) or `other`.
>      2. If `vaspCountry` is `ua`(Ukraine), `vaspRegion` should not be `crimea`, `donetsk` or `luhansk`, should be `other`.
>   4. Required when `txnPurpose` is `others`.
>   5. If `txnPurpose` is `3`, withdrawals will be rejected as transactions for payment for import and/or intermediate trade are prohibited for Binance Japan.
>   6. The `Vasp List` API provides the VASP and identifier information.
> 


## Kazakhstan

Name| Type| Mandatory| Description  
---|---|---|---  
isAddressOwner| BOOLEAN| YES| Whether the address is owned by the user.  
bnfType| INTEGER| YES *1| 0: Individual, 1: Corporate/Entity  
beneficiaryName| STRING| YES *1| For more information please refer to the `Name restrictions` section in the `appendix`.  
beneficiaryCountry| STRING| YES| Beneficiary country code, ISO 2 digit, lower case. For more information please refer to the `Countries and Regions` section in the `appendix`.  
beneficiaryCity| STRING| YES|   
txnPurpose| STRING| YES| Value: service, goods, p2p, charity, others  
txnPurposeOthers| STRING| YES *4|   
sendTo| INTEGER| YES| 2: Exchange, 1: Unhosted Wallet  
vasp| STRING| YES *2| Vasp identifier of the beneficiary  
vaspName| STRING| YES *3| VASP Name  
isAttested| BOOLEAN| YES|   
  
>   1. Required when `isAddressOwner` is `false`.
>   2. Required when `sendTo` is `2`.
>   3. Required when `vasp` is `others`.
>   4. Required when `txnPurpose` is `others`.
>   5. The `Vasp List` API provides the VASP and identifier information. If the VASP cannot be found, please input `others` within `vasp` and the name of the exchange within `vaspName` field.
> 


## New Zealand

Name| Type| Mandatory| Description  
---|---|---|---  
isAddressOwner| INTEGER| YES| 1: Send to myself, 2: Send to another beneficiary  
bnfType| INTEGER| YES *1| 0: Individual, 1: Corporate/Entity  
bnfName| STRING| YES *2| Individual beneficiary name, for more information please refer to the `Name restrictions` section in the `appendix`.  
country| STRING| YES *2| Beneficiary country code, ISO 2 digit, lower case. For more information please refer to the `Countries and Regions` section in the `appendix`.  
bnfCorpName| STRING| YES *3| Beneficiary corporation name.  
bnfCorpCountry| STRING| YES *3| Beneficiary corporation country code, ISO 2 digit, lower case. For more information please refer to the `Countries and Regions` section in the `appendix`.  
sendTo| INTEGER| YES| 1: Private Wallet, 2: Another VASP  
vasp| STRING| YES *4| VASP identifier of the beneficiary  
vaspName| STRING| YES *5| VASP Name  
declaration| BOOLEAN| YES| Declaration confirmation  
  
>   1. Required when `isAddressOwner` is `2`.
>   2. Required when `bnfType` is `0`(Individual).
>   3. Required when `bnfType` is `1`(Corporate/Entity).
>   4. Required when `sendTo` is `2`.
>   5. Required when `vasp` is `others`.
>   6. The `Vasp List` API provides the VASP and identifier information. If the VASP cannot be found, please input `others` within `vasp` and the name of the exchange within `vaspName` field.
> 


## Bahrain

Name| Type| Mandatory| Description  
---|---|---|---  
isAddressOwner| INTEGER| YES| 1: Send to myself, 2: Send to another beneficiary  
bnfType| INTEGER| YES *1| 0: Individual, 1: Corporate/Entity  
bnfFirstName| STRING| YES *2| Individual beneficiary first name. For more information please refer to the `Name restrictions` section in the `appendix`.  
bnfLastName| STRING| YES *2| Individual beneficiary last name. For more information please refer to the `Name restrictions` section in the `appendix`.  
bnfName| STRING| YES *3| Beneficiary corporation/entity name.  
country| STRING| YES *1| Beneficiary country code, ISO 2 digit, lower case. For more information please refer to the `Countries and Regions` section in the `appendix`.  
city| STRING| YES *1|   
sendTo| INTEGER| YES| 1: Private Wallet, 2: Another VASP  
vasp| STRING| YES *4| Vasp identifier of the beneficiary  
vaspName| STRING| YES *5| VASP Name  
  
>   1. Required when `isAddressOwner` is `2`.
>   2. Required when `bnfType` is `0`(Individual).
>   3. Required when `bnfType` is `1`(Corporate/Entity).
>   4. Required when `sendTo` is `2`.
>   5. Required when `vasp` is `others`.
>   6. The `Vasp List` API provides the VASP and identifier information. If the VASP cannot be found, please input `others` within `vasp` and the name of the exchange within `vaspName` field.
> 


## UAE

Name| Type| Mandatory| Description  
---|---|---|---  
isAddressOwner| INTEGER| YES| 1: Send to myself, 2: Send to another beneficiary  
bnfType| INTEGER| YES *1| 0: Individual, 1: Corporate/Entity  
bnfName| STRING| YES *1| For more information please refer to the `Name restrictions` section in the `appendix`.  
country| STRING| YES *1| Beneficiary country code, ISO 2 digit, lower case. For more information please refer to the `Countries and Regions` section in the `appendix`.  
city| STRING| YES *1|   
sendTo| INTEGER| YES| 1: Private Wallet, 2: Another VASP  
vasp| STRING| YES *2| Vasp identifier of the beneficiary  
vaspName| STRING| YES *3| VASP Name  
  
>   1. Required when `isAddressOwner` is `2`.
>   2. Required when `sendTo` is `2`.
>   3. Required when `vasp` is `others`.
>   4. The `Vasp List` API provides the VASP and identifier information. If the VASP cannot be found, please input `others` within `vasp` and the name of the exchange within `vaspName` field.
> 


## India

Name| Type| Mandatory| Description  
---|---|---|---  
isAddressOwner| INTEGER| YES| 1: Send to myself, 2: Send to another beneficiary  
bnfType| INTEGER| YES *1| 0: Individual, 1: Corporate/Entity  
bnfName| STRING| YES *1| For more information please refer to the `Name restrictions` section in the `appendix`.  
country| STRING| YES *1| Beneficiary country code, ISO 2 digit, lower case. For more information please refer to the `Countries and Regions` section in the `appendix`.  
city| STRING| NO|   
sendTo| INTEGER| YES| 1: Private Wallet, 2: Another VASP  
vasp| STRING| YES *2| VASP identifier of the beneficiary  
vaspName| STRING| YES *3| VASP Name  
  
>   1. Required when `isAddressOwner` is `2`.
>   2. Required when `sendTo` is `2`.
>   3. Required when `vasp` is `others`.
>   4. The `Vasp List` API provides the VASP and identifier information. If the VASP cannot be found, please input `others` within `vasp` and the name of the exchange within `vaspName` field.
> 


## EU(Poland,France)

For all the EU countries, please following the same questionnaire.

Name| Type| Mandatory| Description  
---|---|---|---  
isAddressOwner| INTEGER| YES| 1: Send to myself, 2: Send to another beneficiary  
bnfType| INTEGER| YES *1| 0: Individual, 1: Corporate/Entity  
bnfFirstName| STRING| YES *2| Individual beneficiary first name. For more information please refer to the `Name restrictions` section in the `appendix`.  
bnfLastName| STRING| YES *2| Individual beneficiary last name. For more information please refer to the `Name restrictions` section in the `appendix`.  
country| STRING| YES *2| Beneficiary country code, ISO 2 digit, lower case.  
bnfCorpName| STRING| YES *3| Beneficiary corporation name.  
bnfCorpCountry| STRING| YES *3| Beneficiary corporation country code, ISO 2 digit, lower case. For more information please refer to the `Countries and Regions` section in the `appendix`.  
sendTo| INTEGER| YES| 1: Private Wallet, 2: Another VASP  
vasp| STRING| YES *4| VASP identifier of the beneficiary  
vaspName| STRING| YES *5| VASP Name  
declaration| BOOLEAN| YES| Declaration confirmation  
  
>   1. Required when `isAddressOwner` is `2`.
>   2. Required when `bnfType` is `0`.
>   3. Required when `bnfType` is `1`.
>   4. Required when `sendTo` is `2`.
>   5. Required when `vasp` is `others`.
>   6. The `Vasp List` API provides the VASP and identifier information. If the VASP cannot be found, please input `others` within `vasp` and the name of the exchange within `vaspName` field.
> 


## South Africa

Name| Type| Mandatory| Description  
---|---|---|---  
isAddressOwner| INTEGER| YES| 1: Send to myself, 2: Send to another beneficiary  
bnfType| INTEGER| YES *1| 0: Individual, 1: Corporate/Entity  
bnfName| STRING| YES *2| Individual beneficiary name. For more information please refer to the `Name restrictions` section in the `appendix`.  
country| STRING| YES *2| Beneficiary country code, ISO 2 digit, lower case.  
bnfCorpName| STRING| YES *3| Beneficiary corporation name.  
bnfCorpCountry| STRING| YES *3| Beneficiary corporation country code, ISO 2 digit, lower case. For more information please refer to the `Countries and Regions` section in the `appendix`.  
sendTo| INTEGER| YES| 1: Private Wallet, 2: Another VASP  
vasp| STRING| YES *4| VASP identifier of the beneficiary  
vaspName| STRING| YES *5| VASP Name  
declaration| BOOLEAN| YES| Declaration confirmation  
  
>   1. Required when `isAddressOwner` is `2`.
>   2. Required when `bnfType` is `0`(Individual).
>   3. Required when `bnfType` is `1`(Corporate/Entity).
>   4. Required when `sendTo` is `2`.
>   5. Required when `vasp` is `others`.
>   6. The `Vasp List` API provides the VASP and identifier information. If the VASP cannot be found, please input `others` within `vasp` and the name of the exchange within `vaspName` field.
> 


## Australia

Name| Type| Mandatory| Description  
---|---|---|---  
isAddressOwner| INTEGER| YES| 1: Send to myself, 2: Send to another beneficiary  
bnfType| INTEGER| YES *1| 0: Individual, 1: Corporate/Entity  
bnfFirstName| STRING| YES *2| Individual beneficiary first name. For more information please refer to the `Name restrictions` section in the `appendix`.  
bnfLastName| STRING| YES *2| Individual beneficiary last name. For more information please refer to the `Name restrictions` section in the `appendix`.  
country| STRING| YES *2| Beneficiary country code, ISO 2 digit, lower case. Obtained from `Country List` API.  
city| STRING| YES *2| Beneficiary city/town. Obtained from `Region List` API (`regionName` value).  
bnfCorpName| STRING| YES *3| Beneficiary corporation name.  
bnfCorpCountry| STRING| YES *3| Beneficiary corporation country code, ISO 2 digit, lower case. Obtained from `Country List` API.  
bnfCorpCity| STRING| YES *3| Beneficiary corporation city/town. Obtained from `Region List` API (`regionName` value).  
sendTo| INTEGER| YES| 1: Private Wallet, 2: Another VASP  
vasp| STRING| YES *4| VASP identifier of the beneficiary  
vaspName| STRING| YES *5| VASP Name  
declaration| BOOLEAN| YES| Declaration confirmation  
  
>   1. Required when `isAddressOwner` is `2`.
>   2. Required when `bnfType` is `0`(Individual).
>   3. Required when `bnfType` is `1`(Corporate/Entity).
>   4. Required when `sendTo` is `2`.
>   5. Required when `vasp` is `others`.
>   6. The `Vasp List` API provides the VASP and identifier information. If the VASP cannot be found, please input `others` within `vasp` and the name of the exchange within `vaspName` field.
> 


## Brazil

Name| Type| Mandatory| Description  
---|---|---|---  
isAddressOwner| INTEGER| YES| 1: Send to myself, 2: Send to someone else  
sendTo| INTEGER| YES| 1: Self-hosted wallet, 2: VASP / Exchange  
vasp| STRING| YES *6| VASP identifier of the beneficiary. Obtained from `Vasp List` API.  
declaration| BOOLEAN| YES| Declaration confirmation, must be `true`.  
bnfType| INTEGER| YES *1| 0: Individual, 1: Corporate/Entity  
bnfFirstName| STRING| YES *2| Individual beneficiary first name.  
bnfLastName| STRING| YES *2| Individual beneficiary last name.  
country| STRING| YES *2| Beneficiary country code, ISO 2 digit, lower case. Obtained from `Country List` API.  
bnfCorpName| STRING| YES *3| Beneficiary corporation name.  
bnfCorpCountry| STRING| YES *3| Beneficiary corporation country code, ISO 2 digit, lower case. Obtained from `Country List` API.  
cpf| STRING| YES *4| CPF (Brazilian individual taxpayer number). See `Tax Identifier Rules` below.  
cnpj| STRING| YES *4| CNPJ (Brazilian corporate taxpayer number). See `Tax Identifier Rules` below.  
individualTaxId| STRING| YES *5| Individual taxpayer identification number. See `Tax Identifier Rules` below.  
corporateTaxId| STRING| YES *5| Corporate taxpayer identification number. See `Tax Identifier Rules` below.  
txnPurpose| STRING| YES *7| Purpose of transaction code (e.g. `12995`). For more information please refer to the `Brazil Regulatory Codes` section in the `appendix`.  
counterpartyType| STRING| YES *7| Counterparty type code, sent as a string (e.g. `"03"`). For more information please refer to the `Brazil Regulatory Codes` section in the `appendix`.  
relationship| STRING| YES *8| Relationship code, `40` or `50`. For more information please refer to the `Brazil Regulatory Codes` section in the `appendix`.  
  
>   1. Required when `isAddressOwner` is `2`.
>   2. Required when `isAddressOwner` is `2` and `bnfType` is `0`(Individual).
>   3. Required when `isAddressOwner` is `2` and `bnfType` is `1`(Corporate/Entity).
>   4. Required when `isAddressOwner` is `2` and the beneficiary country (`country` or `bnfCorpCountry`) is `br` (domestic): `cpf` for Individual, `cnpj` for Corporate/Entity.
>   5. Required when `isAddressOwner` is `2` and the beneficiary country (`country` or `bnfCorpCountry`) is not `br` (international): `individualTaxId` for Individual, `corporateTaxId` for Corporate/Entity.
>   6. Required when `sendTo` is `2`. Only VASPs returned by the `Vasp List` API are accepted; `others` is not supported.
>   7. Required for international transfers: `isAddressOwner` is `2` and the beneficiary country is not `br`.
>   8. Required for international transfers to a Corporate/Entity beneficiary: `isAddressOwner` is `2`, the beneficiary country is not `br` and `bnfType` is `1`.
> 


**Transaction amount cap:** Cross-border withdrawals above USD 100,000 equivalent per transaction are blocked with error `-30106` (`Transaction amount exceeds the limit.`). The cap uses the USD-equivalent value at transaction time. Withdrawals to self-hosted wallets and domestic (BR-to-BR) transfers are exempt. A withdrawal to your own account at a VASP outside Brazil is international and subject to the cap.

**Tax Identifier Rules:**

Field| Applicable When| Format  
---|---|---  
cpf| `bnfType` = 0 (Individual) and `country` = `br`| `###.###.###-##` (11 digits), separators required: `^\d{3}.\d{3}-\d{2}$`. Format check only, no checksum validation.  
cnpj| `bnfType` = 1 (Corporate) and `bnfCorpCountry` = `br`| `##.###.###/####-##` (14 digits), separators required: `^\d{2}.\d{3}/\d{4}-\d{2}$`. Format check only, no checksum validation.  
individualTaxId| `bnfType` = 0 (Individual) and `country` ≠ `br`| 5–50 alphanumeric characters: `^[A-Za-z0-9]{5,50}$`  
corporateTaxId| `bnfType` = 1 (Corporate) and `bnfCorpCountry` ≠ `br`| 5–50 alphanumeric characters: `^[A-Za-z0-9]{5,50}$`  
  
Was this page helpful?

Last modified on November 12, 2026

[Deposit Questionnaire Contents (for existing local entities)](/en/docs/products/wallet/travel-rule/deposit-questionnaire)[Introduction](/en/docs/products/convert/Introduction)

---

# 提币问卷内容(针对需要旅行规则的本地站)

## 本地站列表

  * [日本](/zh-CN/docs/products/wallet/travel-rule/withdraw-questionnaire#%E6%97%A5%E6%9C%AC)
  * [哈萨克斯坦](/zh-CN/docs/products/wallet/travel-rule/withdraw-questionnaire#%E5%93%88%E8%90%A8%E5%85%8B%E6%96%AF%E5%9D%A6)
  * [新西兰](/zh-CN/docs/products/wallet/travel-rule/withdraw-questionnaire#%E6%96%B0%E8%A5%BF%E5%85%B0)
  * [巴林](/zh-CN/docs/products/wallet/travel-rule/withdraw-questionnaire#%E5%B7%B4%E6%9E%97)
  * [阿联酋](/zh-CN/docs/products/wallet/travel-rule/withdraw-questionnaire#%E9%98%BF%E8%81%94%E9%85%8B)
  * [印度](/zh-CN/docs/products/wallet/travel-rule/withdraw-questionnaire#%E5%8D%B0%E5%BA%A6)
  * [欧洲(波兰,法国)](/zh-CN/docs/products/wallet/travel-rule/withdraw-questionnaire#%E6%AC%A7%E6%B4%B2%E6%B3%A2%E5%85%B0%E6%B3%95%E5%9B%BD)
  * [南非](/zh-CN/docs/products/wallet/travel-rule/withdraw-questionnaire#%E5%8D%97%E9%9D%9E)
  * [澳大利亚](/zh-CN/docs/products/wallet/travel-rule/withdraw-questionnaire#%E6%BE%B3%E5%A4%A7%E5%88%A9%E4%BA%9A)
  * [巴西](/zh-CN/docs/products/wallet/travel-rule/withdraw-questionnaire#%E5%B7%B4%E8%A5%BF)



> 如果您不确定使用的问卷内容，请参阅`检查问卷需求`.

## 日本

名称| 类型| 是否必需| 描述  
---|---|---|---  
isAddressOwner| INTEGER| YES| 1: 发给自己，2:发给其他收款人  
bnfType| INTEGER| YES *1| 0:个人账户，1:企业账户  
kanjiName| STRING| YES *1|   
kanaName| STRING| YES *1|   
latinName| STRING| YES *1| 姓名的相关信息，请参阅`附录`中的`姓名限制`部分。  
country| STRING| YES| 收款人国家二位字母代码(ISO-3166)，必须为小写, 有关此信息，请参阅`附录`中的`国家和地区`部分。  
city| STRING| YES|   
sendTo| INTEGER| YES| 1:虚拟货币服务商，2:私有钱包  
vasp| STRING| YES *2| 收款人的Vasp identifier  
vaspCountry| STRING| YES *2| VASP国家二位字母代码(ISO-3166)，必须为小写, 有关此信息，请参阅`附录`中的`国家和地区`部分。  
vaspRegion| STRING| YES *3|   
txnPurpose| INTEGER| YES *4| 1:在日本国内购物，2:遗产、赠予或生活费，3:跨境交易, 4:投资，5:支付第三方VASP的服务费用，6:偿还贷款，7:礼物或捐款  
isAttested| BOOLEAN| YES|   
  
>   1. 当 `isAddressOwner` 是 `2` 时必填。
>   2. 当 `sendTo` 是 `1` 时必填。
>   3. 当 `vaspCountry` 是 `cn`(中国) 或 `ua`(乌克兰) 时。
>      1. 如果 `vaspCountry` 是 `cn`(中国)，`vaspRegion` 必须是 `notNortheasternProvinces`(东北三省) 或者 `other`，即黑龙江，吉林和辽宁。
>      2. 如果 `vaspCountry` 是 `ua`(乌克兰)，`vaspRegion` 不能为 `crimea`(克里米亚)，`donetsk`(顿涅茨克) 或 `luhansk`(卢甘斯克), 可以是 `other`。
>   4. 当 `txnPurpose` 是 `others` 时必填。
>   5. 如果 `txnPurpose` 为 `3`，提款将被拒绝，因为 Binance Japan 禁止用于支付进口和/或中间贸易的交易。
>   6. `Vasp List` 接口提供 VASP 及其标识符信息。
> 


## 哈萨克斯坦

名称| 类型| 是否必需| 描述  
---|---|---|---  
isAddressOwner| BOOLEAN| YES| 收款人是不是自己  
bnfType| INTEGER| YES *1| 0:个人账户, 1:企业账户  
beneficiaryName| STRING| YES *1| 姓名的相关信息，请参阅`附录`中的`姓名限制`部分。  
beneficiaryCountry| STRING| YES| 收款人国家二位字母代码(ISO-3166)，必须为小写, 有关此信息，请参阅`附录`中的`国家和地区`部分。  
beneficiaryCity| STRING| YES|   
txnPurpose| STRING| YES| 合理值: service, goods, p2p, charity, others  
txnPurposeOthers| STRING| YES *5|   
sendTo| INTEGER| YES| 2:交易所, 1:私有钱包  
vasp| STRING| YES *2| 收款人的VASP identifier  
vaspName| STRING| YES *3| VASP名  
isAttested| BOOLEAN| YES|   
  
>   1. 当 `isAddressOwner` 是 `false` 时必填。
>   2. 当 `sendTo` 是 `2` 时必填。
>   3. 当 `vasp` 是 `others` 时必填。
>   4. `Vasp List` 接口提供 VASP 及其标识符信息。如果`vasp`不在`预先加载VASP列表`中, `vasp`字段请填`others`, `vaspName`字段请填交易所的名字。
>   5. 当 `txnPurpose` 是 `others` 时必填.
> 


## 新西兰

名称| 类型| 是否必需| 描述  
---|---|---|---  
isAddressOwner| INTEGER| YES| 1:提现给自己, 2:提现给其他人  
bnfType| INTEGER| YES *1| 0:个人账户, 1:企业账户  
bnfName| STRING| YES *2| 姓名的相关信息，请参阅`附录`中的`姓名限制`部分。  
country| STRING| YES *2| 收款人国家二位字母代码(ISO-3166)，必须为小写, 有关此信息，请参阅`附录`中的`国家和地区`部分。  
bnfCorpName| STRING| YES *3| 收款人企业名称.  
bnfCorpCountry| STRING| YES *3| 收款人企业所在国家, 有关此信息，请参阅`附录`中的`国家和地区`部分。  
sendTo| INTEGER| YES| 1:私有钱包, 2:交易所  
vasp| STRING| YES *4| 收款人的VASP identifier  
vaspName| STRING| YES *5| 交易所名称  
declaration| BOOLEAN| YES|   
  
>   1. 当 `isAddressOwner` 是 `2` 时必填。
>   2. 当 `bnfType` 是 `0` 时必填.
>   3. 当 `bnfType` 是 `1` 时必填.
>   4. 当 `sendTo` 是 `2` 时必填.
>   5. 当 `vasp` 是 `others` 时必填.
>   6. `Vasp List` 接口提供 VASP 及其标识符信息。如果`vasp`不在`预先加载VASP列表`中, `vasp`字段请填`others`, `vaspName`字段请填交易所的名字。
> 


## 巴林

名称| 类型| 是否必需| 描述  
---|---|---|---  
isAddressOwner| INTEGER| YES| 1:提现给自己, 2:提现给其他人  
bnfType| INTEGER| YES *1| 0:个人账户, 1:企业账户  
bnfFirstName| STRING| YES *2| 个人收款人名。姓名的相关信息，请参阅`附录`中的`姓名限制`部分。  
bnfLastName| STRING| YES *2| 个人收款人姓。姓名的相关信息，请参阅`附录`中的`姓名限制`部分。  
bnfName| STRING| YES *3| 收款人企业/实体名称。  
country| STRING| YES *1| 收款人国家二位字母代码(ISO-3166)，必须为小写, 有关此信息，请参阅`附录`中的`国家和地区`部分。  
city| STRING| YES *1|   
sendTo| INTEGER| YES| 1:私有钱包, 2:交易所  
vasp| STRING| YES *4| 收款人的VASP identifier  
vaspName| STRING| YES *5| VASP名  
  
>   1. 当 `isAddressOwner` 是 `2` 时必填。
>   2. 当 `bnfType` 是 `0`(个人账户) 时必填。
>   3. 当 `bnfType` 是 `1`(企业账户) 时必填。
>   4. 当 `sendTo` 是 `2` 时必填。
>   5. 当 `vasp` 是 `others` 时必填。
>   6. `Vasp List` 接口提供 VASP 及其标识符信息。如果`vasp`不在`预先加载VASP列表`中, `vasp`字段请填`others`, `vaspName`字段请填交易所的名字。
> 


## 阿联酋

名称| 类型| 是否必需| 描述  
---|---|---|---  
isAddressOwner| INTEGER| YES| 1:提现给自己, 2:提现给其他人  
bnfType| INTEGER| YES *1| 0:个人账户, 1:企业账户  
bnfName| STRING| YES *1| 姓名的相关信息，请参阅`附录`中的`姓名限制`部分。  
country| STRING| YES *1| 收款人国家二位字母代码(ISO-3166)，必须为小写, 有关此信息，请参阅`附录`中的`国家和地区`部分。  
city| STRING| YES *1|   
sendTo| INTEGER| YES| 1:私有钱包, 2:交易所  
vasp| STRING| YES *2| 收款人的VASP identifier  
vaspName| STRING| YES *3| VASP名  
  
>   1. 当 `isAddressOwner` 是 `2` 时必填。
>   2. 当 `sendTo` 是 `2` 时必填。
>   3. 当 `vasp` 是 `others` 时必填。
>   4. `Vasp List` 接口提供 VASP 及其标识符信息。如果`vasp`不在`预先加载VASP列表`中, `vasp`字段请填`others`, `vaspName`字段请填交易所的名字。
> 


## 印度

名称| 类型| 是否必需| 描述  
---|---|---|---  
isAddressOwner| INTEGER| YES| 1:提现给自己, 2:提现给其他人  
bnfType| INTEGER| YES *1| 0:个人账户, 1:企业账户  
bnfName| STRING| YES *1| 姓名的相关信息，请参阅`附录`中的`姓名限制`部分。  
country| STRING| YES *1| 收款人国家二位字母代码(ISO-3166)，必须为小写, 有关此信息，请参阅`附录`中的`国家和地区`部分。  
city| STRING| NO|   
sendTo| INTEGER| YES| 1:私有钱包, 2:交易所  
vasp| STRING| YES *2| 收款人的VASP identifier  
vaspName| STRING| YES *3| VASP名  
  
>   1. 当 `isAddressOwner` 是 `2` 时必填。
>   2. 当 `sendTo` 是 `2` 时必填。
>   3. 当 `vasp` 是 `others` 时必填。
>   4. `Vasp List` 接口提供 VASP 及其标识符信息。如果`vasp`不在`预先加载VASP列表`中, `vasp`字段请填`others`, `vaspName`字段请填交易所的名字。
> 


## 欧洲(波兰,法国)

名称| 类型| 是否必需| 描述  
---|---|---|---  
isAddressOwner| INTEGER| YES| 1:提现给自己, 2:提现给其他人  
bnfType| INTEGER| YES *1| 0:个人账户, 1:企业账户  
bnfFirstName| STRING| YES *2| 姓名的相关信息，请参阅`附录`中的`姓名限制`部分。  
bnfLastName| STRING| YES *2| 姓名的相关信息，请参阅`附录`中的`姓名限制`部分。  
country| STRING| YES *2| 收款人国家二位字母代码(ISO-3166)，必须为小写, 有关此信息，请参阅`附录`中的`国家和地区`部分。  
bnfCorpName| STRING| YES *3| 收款人企业名称.  
bnfCorpCountry| STRING| YES *3| 收款人企业所在国家, 有关此信息，请参阅`附录`中的`国家和地区`部分。  
sendTo| INTEGER| YES| 1:私有钱包, 2:交易所  
vasp| STRING| YES *4| 收款人的VASP identifier  
vaspName| STRING| YES *5| 交易所名称  
declaration| BOOLEAN| YES|   
  
>   1. 当 `isAddressOwner` 是 `2` 时必填。
>   2. 当 `bnfType` 是 `0` 时必填.
>   3. 当 `bnfType` 是 `1` 时必填.
>   4. 当 `sendTo` 是 `2` 时必填.
>   5. 当 `vasp` 是 `others` 时必填.
>   6. `Vasp List` 接口提供 VASP 及其标识符信息。如果`vasp`不在`预先加载VASP列表`中, `vasp`字段请填`others`, `vaspName`字段请填交易所的名字。
> 


## 南非

名称| 类型| 是否必需| 描述  
---|---|---|---  
isAddressOwner| INTEGER| YES| 1:提现给自己, 2:提现给其他人  
bnfType| INTEGER| YES *1| 0:个人账户, 1:企业账户  
bnfName| STRING| YES *2| 姓名的相关信息，请参阅`附录`中的`姓名限制`部分。  
country| STRING| YES *2| 收款人国家二位字母代码(ISO-3166)，必须为小写, 有关此信息，请参阅`附录`中的`国家和地区`部分。  
bnfCorpName| STRING| YES *3| 收款人企业名称.  
bnfCorpCountry| STRING| YES *3| 收款人企业所在国家, 有关此信息，请参阅`附录`中的`国家和地区`部分。  
sendTo| INTEGER| YES| 1:私有钱包, 2:交易所  
vasp| STRING| YES *4| 收款人的VASP identifier  
vaspName| STRING| YES *5| 交易所名称  
declaration| BOOLEAN| YES|   
  
>   1. 当 `isAddressOwner` 是 `2` 时必填。
>   2. 当 `bnfType` 是 `0` 时必填.
>   3. 当 `bnfType` 是 `1` 时必填.
>   4. 当 `sendTo` 是 `2` 时必填.
>   5. 当 `vasp` 是 `others` 时必填.
>   6. `Vasp List` 接口提供 VASP 及其标识符信息。如果`vasp`不在`预先加载VASP列表`中, `vasp`字段请填`others`, `vaspName`字段请填交易所的名字。
> 


## 澳大利亚

名称| 类型| 是否必需| 描述  
---|---|---|---  
isAddressOwner| INTEGER| YES| 1:发给自己，2:发给其他收款人  
bnfType| INTEGER| YES *1| 0:个人账户，1:企业账户  
bnfFirstName| STRING| YES *2| 个人收款人名。姓名的相关信息，请参阅`附录`中的`姓名限制`部分。  
bnfLastName| STRING| YES *2| 个人收款人姓。姓名的相关信息，请参阅`附录`中的`姓名限制`部分。  
country| STRING| YES *2| 收款人国家二位字母代码(ISO-3166)，必须为小写。通过`国家列表`接口获取。  
city| STRING| YES *2| 收款人城市/城镇。通过`地区列表`接口获取（使用 `regionName` 值）。  
bnfCorpName| STRING| YES *3| 收款人公司名称。  
bnfCorpCountry| STRING| YES *3| 收款人公司国家二位字母代码(ISO-3166)，必须为小写。通过`国家列表`接口获取。  
bnfCorpCity| STRING| YES *3| 收款人公司城市/城镇。通过`地区列表`接口获取（使用 `regionName` 值）。  
sendTo| INTEGER| YES| 1:私有钱包，2:其他 VASP  
vasp| STRING| YES *4| 收款人的 VASP identifier  
vaspName| STRING| YES *5| VASP 名称  
declaration| BOOLEAN| YES| 声明确认  
  
>   1. 当 `isAddressOwner` 是 `2` 时必填。
>   2. 当 `bnfType` 是 `0`（个人）时必填。
>   3. 当 `bnfType` 是 `1`（公司/实体）时必填。
>   4. 当 `sendTo` 是 `2` 时必填。
>   5. 当 `vasp` 是 `others` 时必填。
>   6. `Vasp List` 接口提供 VASP 及其标识符信息。如果 `vasp` 不在`预先加载VASP列表`中，`vasp`字段请填 `others`，`vaspName` 字段请填交易所的名字。
> 


## 巴西

名称| 类型| 是否必需| 描述  
---|---|---|---  
isAddressOwner| INTEGER| YES| 1: 发给自己，2: 发给其他人  
sendTo| INTEGER| YES| 1: 自托管钱包，2: VASP / 交易所  
vasp| STRING| YES *6| 收款人的 VASP identifier。通过`Vasp List`接口获取。  
declaration| BOOLEAN| YES| 声明确认，必须为 `true`。  
bnfType| INTEGER| YES *1| 0: 个人账户，1: 企业账户  
bnfFirstName| STRING| YES *2| 个人收款人名。  
bnfLastName| STRING| YES *2| 个人收款人姓。  
country| STRING| YES *2| 收款人国家二位字母代码(ISO-3166)，必须为小写。通过`国家列表`接口获取。  
bnfCorpName| STRING| YES *3| 收款人公司名称。  
bnfCorpCountry| STRING| YES *3| 收款人公司国家二位字母代码(ISO-3166)，必须为小写。通过`国家列表`接口获取。  
cpf| STRING| YES *4| CPF（巴西个人税号）。参见下方`税务标识规则`。  
cnpj| STRING| YES *4| CNPJ（巴西公司税号）。参见下方`税务标识规则`。  
individualTaxId| STRING| YES *5| 个人税务识别号。参见下方`税务标识规则`。  
corporateTaxId| STRING| YES *5| 公司税务识别号。参见下方`税务标识规则`。  
txnPurpose| STRING| YES *7| 交易目的编码（如 `12995`）。相关信息请参阅`附录`中的`巴西监管编码`部分。  
counterpartyType| STRING| YES *7| 对手方类型编码，以字符串传入（如 `"03"`）。相关信息请参阅`附录`中的`巴西监管编码`部分。  
relationship| STRING| YES *8| 关系编码，`40` 或 `50`。相关信息请参阅`附录`中的`巴西监管编码`部分。  
  
>   1. 当 `isAddressOwner` 是 `2` 时必填。
>   2. 当 `isAddressOwner` 是 `2` 且 `bnfType` 是 `0`（个人）时必填。
>   3. 当 `isAddressOwner` 是 `2` 且 `bnfType` 是 `1`（公司/实体）时必填。
>   4. 当 `isAddressOwner` 是 `2` 且收款人国家（`country` 或 `bnfCorpCountry`）是 `br`（境内）时必填：个人填 `cpf`，公司/实体填 `cnpj`。
>   5. 当 `isAddressOwner` 是 `2` 且收款人国家（`country` 或 `bnfCorpCountry`）不是 `br`（跨境）时必填：个人填 `individualTaxId`，公司/实体填 `corporateTaxId`。
>   6. 当 `sendTo` 是 `2` 时必填。仅接受 `Vasp List` 接口返回的 VASP，不支持 `others`。
>   7. 跨境转账时必填：`isAddressOwner` 是 `2` 且收款人国家不是 `br`。
>   8. 向公司/实体收款人跨境转账时必填：`isAddressOwner` 是 `2`、收款人国家不是 `br` 且 `bnfType` 是 `1`。
> 


**交易金额上限：** 单笔超过等值 USD 100,000 的跨境提币将被拦截，返回错误 `-30106`（`Transaction amount exceeds the limit.`）。上限按交易时的 USD 等值计算。提币至自托管钱包以及境内（BR 对 BR）转账不受限制。提币至您本人在巴西境外 VASP 的账户属于跨境，受上限约束。

**税务标识规则（Tax Identifier Rules）：**

字段| 适用条件| 格式  
---|---|---  
cpf| `bnfType` = 0（个人）且 `country` = `br`| `###.###.###-##`（11 位数字），必须包含分隔符：`^\d{3}.\d{3}-\d{2}$`。仅校验格式，不校验校验位。  
cnpj| `bnfType` = 1（公司）且 `bnfCorpCountry` = `br`| `##.###.###/####-##`（14 位数字），必须包含分隔符：`^\d{2}.\d{3}/\d{4}-\d{2}$`。仅校验格式，不校验校验位。  
individualTaxId| `bnfType` = 0（个人）且 `country` ≠ `br`| 5–50 位字母数字：`^[A-Za-z0-9]{5,50}$`  
corporateTaxId| `bnfType` = 1（公司）且 `bnfCorpCountry` ≠ `br`| 5–50 位字母数字：`^[A-Za-z0-9]{5,50}$`  
  
此页面是否有帮助？

Last modified on November 12, 2026

[充值问卷内容(针对需要旅行规则的本地站)](/zh-CN/docs/products/wallet/travel-rule/deposit-questionnaire)[概述](/zh-CN/docs/products/convert/Introduction)