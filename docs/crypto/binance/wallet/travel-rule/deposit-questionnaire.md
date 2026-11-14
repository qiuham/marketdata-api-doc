---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/wallet/travel-rule/deposit-questionnaire
api_type: REST
updated_at: 2026-11-13 20:30:57.677724
---

# Deposit Questionnaire Contents (for existing local entities)

## Local Entities

  * [Japan](/en/docs/products/wallet/travel-rule/deposit-questionnaire#japan)
  * [Kazakhstan](/en/docs/products/wallet/travel-rule/deposit-questionnaire#kazakhstan)
  * [Bahrain](/en/docs/products/wallet/travel-rule/deposit-questionnaire#bahrain)
  * [UAE](/en/docs/products/wallet/travel-rule/deposit-questionnaire#united-arab-emirates)
  * [India](/en/docs/products/wallet/travel-rule/deposit-questionnaire#india)
  * [EU(Poland,France)](/en/docs/products/wallet/travel-rule/deposit-questionnaire#eupolandfrance)
  * [South Africa](/en/docs/products/wallet/travel-rule/deposit-questionnaire#south-africa)
  * [Australia](/en/docs/products/wallet/travel-rule/deposit-questionnaire#australia)
  * [Brazil](/en/docs/products/wallet/travel-rule/deposit-questionnaire#brazil)



## Japan

Name| Type| Mandatory| Description  
---|---|---|---  
depositOriginator| INTEGER| YES| 2 = Myself, 1 = Not Myself  
bnfType| INTEGER| YES| 0 = Individual, 1 = Corporate/Entity  
country| STRING| YES *1| Originator country code, ISO 2 digit, lower case. For more information please refer to the `Countries and Regions` section in the `appendix`.  
region| STRING| YES *2| Originator region  
city| STRING| YES *1| Originator’s city/village/town.  
kanjiName| STRING| YES *1|   
kanaName| STRING| YES *1|   
latinName| STRING| YES *1| For more information please refer to the `Name restrictions` section in the `appendix`.  
vaspName| STRING| YES|   
isAttested| BOOLEAN| YES|   
  
>   1. Required when `depositOriginator` is `1`.
>   2. Required when `country` is `cn`(China) or `ua`(Ukraine).
>      1. If `country` is `cn`(China), `region` must be `notNortheasternProvinces` (Jilin, Liaoning and Heilongjiang) or `other`.
>      2. If `country` is `ua`(Ukraine), `region` should not be `crimea`, `donetsk` or `luhansk`，should be `other`.
> 


## Kazakhstan

Name| Type| Mandatory| Description  
---|---|---|---  
originatorName| STRING| YES| Name of originator.  
country| STRING| YES| Originator country code, ISO 2 digit, lower case. For more information please refer to the `Countries and Regions` section in the `appendix`.  
city| STRING| YES| Originator’s city/village/town.  
txnPurpose| STRING| YES| Value: service, goods, p2p, charity, others  
txnPurposeOthers| STRING| YES *1|   
  
>   1. Required when `txnPurpose` is `others`.
> 


## Bahrain

Name| Type| Mandatory| Description  
---|---|---|---  
depositOriginator| INTEGER| YES| 1 = Myself, 2 = Not myself  
orgType| INTEGER| YES *1| 0 = Individual, 1 = Corporate/Entity  
orgFirstName| STRING| YES *1| Originator's First Name, for more information please refer to the `Name restrictions` section in the `appendix`.  
orgLastName| STRING| YES *1| Originator's Last Name, for more information please refer to the `Name restrictions` section in the `appendix`.  
country| STRING| YES *1| Originator's residence country code, ISO 2 digit, lower case. For more information please refer to the `Countries and Regions` section in the `appendix`.  
city| STRING| YES *1|   
receiveFrom| INTEGER| YES| 1 = Private Wallet, 2 = Another VASP  
vasp| STRING| YES *2| Vasp identifier of the originator.  
vaspName| STRING| YES *3|   
  
>   1. Required when `depositOriginator` is `2`.
>   2. Required when `receiveFrom` is `2`.
>   3. Required when `vasp` is `others`.
>   4. The `Vasp List` API provides the VASP and identifier information. If the VASP cannot be found, please input `others` within `vasp list` and the name of the exchange within `vaspName` field.
> 


## United Arab Emirates

Name| Type| Mandatory| Description  
---|---|---|---  
depositOriginator| INTEGER| YES| 1 = Myself, 2 = Not myself  
orgType| INTEGER| YES *1| 0 = Individual, 1 = Corporate/Entity  
orgName| STRING| YES *1| For more information please refer to the `Name restrictions` section in the `appendix`.  
country| STRING| YES *1| Originator's nationality code, ISO 2 digit, lower case. For more information please refer to the `Countries and Regions` section in the `appendix`.  
city| STRING| YES *1|   
receiveFrom| INTEGER| YES| 1 = Private Wallet, 2 = Another VASP  
vasp| STRING| YES *2| Vasp identifier of the beneficiary  
vaspName| STRING| YES *3|   
  
>   1. Required when `depositOriginator` is `2`.
>   2. Required when `receiveFrom` is `2`.
>   3. Required when `vasp` is `others`.
>   4. The `Vasp List` API provides the VASP and identifier information. If the VASP cannot be found, please input `others` within `vasp list` and the name of the exchange within `vaspName` field.
> 


## India

Name| Type| Mandatory| Description  
---|---|---|---  
depositOriginator| INTEGER| YES| 1 = Myself, 2 = Not myself  
orgType| INTEGER| YES *1| 0 = Individual, 1 = Corporate/Entity  
orgName| STRING| YES *1| Originator's Name, for more information please refer to the `Name restrictions` section in the `appendix`.  
pan| STRING| YES *1| Permanent Account Number (PAN) or National ID Number  
country| STRING| YES *1| Originator's nationality code, ISO 2 digit, lower case. For more information please refer to the `Countries and Regions` section in the `appendix`.  
state| STRING| YES *1| Originator's State  
city| STRING| YES *1| Originator’s City/Village/Town  
pinCode| STRING| YES *1|   
address| STRING| YES *1|   
receiveFrom| INTEGER| YES| 1 = Private Wallet, 2 = Another VASP  
vasp| STRING| YES *2| Vasp identifier of the beneficiary  
vaspName| STRING| YES *3|   
  
>   1. Required when `depositOriginator` is `2`.
>   2. Required when `receiveFrom` is `2`.
>   3. Required when `vasp` is `others`.
>   4. The `Vasp List` API provides the VASP and identifier information. If the VASP cannot be found, please input `others` within `vasp list` and the name of the exchange within `vaspName` field.
> 


## EU(Poland,France)

Name| Type| Mandatory| Description  
---|---|---|---  
depositOriginator| INTEGER| YES| 1 = Myself, 2 = Not myself  
orgType| INTEGER| YES *1| 0 = Individual, 1 = Corporate/Entity  
orgFirstName| STRING| YES *2| Originator's First Name, for more information please refer to the `Name restrictions` section in the `appendix`.  
orgLastName| STRING| YES *2| Originator's Last Name, for more information please refer to the `Name restrictions` section in the `appendix`.  
country| STRING| YES *2| Originator's nationality code, ISO 2 digit, lower case. For more information please refer to the `Countries and Regions` section in the `appendix`.  
corpName| STRING| YES *3| Originator's (corporation) Name  
corpCountry| STRING| YES *3| Originator's (corporation) nationality code, ISO 2 digit, lower case. For more information please refer to the `Countries and Regions` section in the `appendix`.  
receiveFrom| INTEGER| YES| 1 = Private Wallet, 2 = Another VASP  
vasp| STRING| YES *4| Vasp identifier of the beneficiary  
vaspName| STRING| YES *5| VASP Name  
declaration| BOOLEAN| YES| Declaration confirmation  
  
>   1. Required when `depositOriginator` is `2`.
>   2. Required when `orgType` is `0`.
>   3. Required when `orgType` is `1`.
>   4. Required when `receiveFrom` is `2`.
>   5. The `Vasp List` API provides the VASP and identifier information. If the VASP cannot be found, please input `others` within `vasp list` and the name of the exchange within `vaspName` field.
> 


## South Africa

Name| Type| Mandatory| Description  
---|---|---|---  
depositOriginator| INTEGER| YES| 1 = Myself, 2 = Not myself  
orgType| INTEGER| YES *1| 0 = Individual, 1 = Corporate/Entity  
orgName| STRING| YES *2| Originator's Name, for more information please refer to the `Name restrictions` section in the `appendix`.  
country| STRING| YES *2| Originator's nationality code, ISO 2 digit, lower case. For more information please refer to the `Countries and Regions` section in the `appendix`.  
corpName| STRING| YES *3| Originator's (corporation) Name  
corpCountry| STRING| YES *3| Originator's (corporation) nationality code, ISO 2 digit, lower case. For more information please refer to the `Countries and Regions` section in the `appendix`.  
receiveFrom| INTEGER| YES| 1 = Private Wallet, 2 = Another VASP  
vasp| STRING| YES *4| Vasp identifier of the beneficiary  
vaspName| STRING| YES *5| VASP Name  
declaration| BOOLEAN| YES| Declaration confirmation  
  
>   1. Required when `depositOriginator` is `2`.
>   2. Required when `orgType` is `0`.
>   3. Required when `orgType` is `1`.
>   4. Required when `receiveFrom` is `2`.
>   5. The `Vasp List` API provides the VASP and identifier information. If the VASP cannot be found, please input `others` within `vasp list` and the name of the exchange within `vaspName` field.
> 


## Australia

Name| Type| Mandatory| Description  
---|---|---|---  
depositOriginator| INTEGER| YES| 1 = Myself, 2 = Not myself  
orgType| INTEGER| YES *1| 0 = Individual, 1 = Corporate/Entity  
orgFirstName| STRING| YES *2| Originator's First Name. For more information please refer to the `Name restrictions` section in the `appendix`.  
orgLastName| STRING| YES *2| Originator's Last Name. For more information please refer to the `Name restrictions` section in the `appendix`.  
country| STRING| YES *2| Originator's country code, ISO 2 digit, lower case. Obtained from `Country List` API.  
city| STRING| YES *2| Originator's city/town. Obtained from `Region List` API (`regionName` value).  
corpName| STRING| YES *3| Corporation/entity name.  
corpCountry| STRING| YES *3| Corporation country code, ISO 2 digit, lower case. Obtained from `Country List` API.  
corpCity| STRING| YES *3| Corporation city/town. Obtained from `Region List` API (`regionName` value).  
identifierType| STRING| NO| See `Identifier Type Options` below.  
identifier| STRING| YES *6| Identifier value corresponding to `identifierType`.  
receiveFrom| INTEGER| YES| 1 = Private Wallet, 2 = Another VASP  
vasp| STRING| YES *4| VASP identifier of the originator  
vaspName| STRING| YES *5| VASP Name  
declaration| BOOLEAN| YES| Declaration confirmation  
  
>   1. Required when `depositOriginator` is `2`.
>   2. Required when `orgType` is `0`(Individual).
>   3. Required when `orgType` is `1`(Corporate/Entity).
>   4. Required when `receiveFrom` is `2`.
>   5. Required when `vasp` is `others`.
>   6. Required when `identifierType` is provided.
>   7. The `Vasp List` API provides the VASP and identifier information. If the VASP cannot be found, please input `others` within `vasp list` and the name of the exchange within `vaspName` field.
> 


**Identifier Type Options:**

identifierType| Meaning| Applicable When| Validation  
---|---|---|---  
PASSPORT| Passport number| `orgType` = 0 (Individual)| Alphanumeric, 1–50 chars  
NATIONAL_ID| National identity card number| `orgType` = 0 (Individual)| Alphanumeric, 1–50 chars  
ABN| Australian Business Number| `orgType` = 1 (Corporate)| Exactly 11 digits  
ACN| Australian Company Number| `orgType` = 1 (Corporate)| Exactly 9 digits  
OTHER| Other registration number| `orgType` = 1 (Corporate)| Alphanumeric, 1–50 chars  
  
## Brazil

Name| Type| Mandatory| Description  
---|---|---|---  
depositOriginator| INTEGER| YES| 1 = Deposited by myself, 2 = Deposited by someone else  
receiveFrom| INTEGER| YES| 1 = Self-hosted wallet, 2 = VASP / Exchange  
vasp| STRING| YES *6| VASP identifier of the originator. Obtained from `Vasp List` API.  
declaration| BOOLEAN| YES| Declaration confirmation, must be `true`.  
orgType| INTEGER| YES *1| 0 = Individual, 1 = Corporate/Entity  
orgFirstName| STRING| YES *2| Originator's First Name.  
orgLastName| STRING| YES *2| Originator's Last Name.  
country| STRING| YES *2| Originator's country code, ISO 2 digit, lower case. Obtained from `Country List` API.  
corpName| STRING| YES *3| Corporation/entity name.  
corpCountry| STRING| YES *3| Corporation country code, ISO 2 digit, lower case. Obtained from `Country List` API.  
cpf| STRING| YES *4| CPF (Brazilian individual taxpayer number). See `Tax Identifier Rules` below.  
cnpj| STRING| YES *4| CNPJ (Brazilian corporate taxpayer number). See `Tax Identifier Rules` below.  
individualTaxId| STRING| YES *5| Individual taxpayer identification number. See `Tax Identifier Rules` below.  
corporateTaxId| STRING| YES *5| Corporate taxpayer identification number. See `Tax Identifier Rules` below.  
txnPurpose| STRING| YES *7| Purpose of transaction code (e.g. `12995`). For more information please refer to the `Brazil Regulatory Codes` section in the `appendix`.  
counterpartyType| STRING| YES *7| Counterparty type code, sent as a string (e.g. `"03"`). For more information please refer to the `Brazil Regulatory Codes` section in the `appendix`.  
relationship| STRING| YES *8| Relationship code, `40` or `50`. For more information please refer to the `Brazil Regulatory Codes` section in the `appendix`.  
  
>   1. Required when `depositOriginator` is `2`.
>   2. Required when `depositOriginator` is `2` and `orgType` is `0`(Individual).
>   3. Required when `depositOriginator` is `2` and `orgType` is `1`(Corporate/Entity).
>   4. Required when `depositOriginator` is `2` and the originator country (`country` or `corpCountry`) is `br` (domestic): `cpf` for Individual, `cnpj` for Corporate/Entity.
>   5. Required when `depositOriginator` is `2` and the originator country (`country` or `corpCountry`) is not `br` (international): `individualTaxId` for Individual, `corporateTaxId` for Corporate/Entity.
>   6. Required when `receiveFrom` is `2`. Only VASPs returned by the `Vasp List` API are accepted; `others` is not supported.
>   7. Required for international transfers: `depositOriginator` is `2` and the originator country is not `br`.
>   8. Required for international transfers from a Corporate/Entity originator: `depositOriginator` is `2`, the originator country is not `br` and `orgType` is `1`.
> 


**Transaction amount cap:** Cross-border deposits above USD 100,000 equivalent per transaction are blocked with error `-30106` (`Transaction amount exceeds the limit.`). The cap uses the USD-equivalent value at transaction time. Deposits from self-hosted wallets and domestic (BR-to-BR) transfers are exempt. A deposit from your own account at a VASP outside Brazil is international and subject to the cap.

**Tax Identifier Rules:**

Field| Applicable When| Format  
---|---|---  
cpf| `orgType` = 0 (Individual) and `country` = `br`| `###.###.###-##` (11 digits), separators required: `^\d{3}.\d{3}-\d{2}$`. Format check only, no checksum validation.  
cnpj| `orgType` = 1 (Corporate) and `corpCountry` = `br`| `##.###.###/####-##` (14 digits), separators required: `^\d{2}.\d{3}/\d{4}-\d{2}$`. Format check only, no checksum validation.  
individualTaxId| `orgType` = 0 (Individual) and `country` ≠ `br`| 5–50 alphanumeric characters: `^[A-Za-z0-9]{5,50}$`  
corporateTaxId| `orgType` = 1 (Corporate) and `corpCountry` ≠ `br`| 5–50 alphanumeric characters: `^[A-Za-z0-9]{5,50}$`  
  
Was this page helpful?

Last modified on November 12, 2026

[Appendix](/en/docs/products/wallet/travel-rule/appendix)[Withdraw Questionnaire Contents (for existing local entities)](/en/docs/products/wallet/travel-rule/withdraw-questionnaire)

---

# 充值问卷内容(针对需要旅行规则的本地站)

## 本地站列表

  * [日本](/zh-CN/docs/products/wallet/travel-rule/deposit-questionnaire#%E6%97%A5%E6%9C%AC)
  * [哈萨克斯坦](/zh-CN/docs/products/wallet/travel-rule/deposit-questionnaire#%E5%93%88%E8%90%A8%E5%85%8B%E6%96%AF%E5%9D%A6)
  * [巴林](/zh-CN/docs/products/wallet/travel-rule/deposit-questionnaire#%E5%B7%B4%E6%9E%97)
  * [阿联酋](/zh-CN/docs/products/wallet/travel-rule/deposit-questionnaire#%E9%98%BF%E8%81%94%E9%85%8B)
  * [印度](/zh-CN/docs/products/wallet/travel-rule/deposit-questionnaire#%E5%8D%B0%E5%BA%A6)
  * [欧洲(波兰,法国)](/zh-CN/docs/products/wallet/travel-rule/deposit-questionnaire#%E6%AC%A7%E6%B4%B2%E6%B3%A2%E5%85%B0%E6%B3%95%E5%9B%BD)
  * [南非](/zh-CN/docs/products/wallet/travel-rule/deposit-questionnaire#%E5%8D%97%E9%9D%9E)
  * [澳大利亚](/zh-CN/docs/products/wallet/travel-rule/deposit-questionnaire#%E6%BE%B3%E5%A4%A7%E5%88%A9%E4%BA%9A)
  * [巴西](/zh-CN/docs/products/wallet/travel-rule/deposit-questionnaire#%E5%B7%B4%E8%A5%BF)



## 日本

名称| 类型| 是否必须| 描述  
---|---|---|---  
depositOriginator| INTEGER| YES| 2 = 发款人自己, 1 = 发款人不是自己  
bnfType| INTEGER| YES| 0 = 个人账号, 1 = 企业账号  
country| STRING| YES *1| 发款人国家二位字母代码(ISO-3166)，必须为小写. 有关此信息，请参阅`附录`中的`国家和地区`部分。  
region| STRING| YES *2| 发款人所在地区.  
city| STRING| YES *1| 发款人所在城市  
kanjiName| STRING| YES *1|   
kanaName| STRING| YES *1|   
latinName| STRING| YES *1| 姓名的相关信息，请参阅`附录`中的`姓名限制`部分。  
vaspName| STRING| YES|   
isAttested| BOOLEAN| YES|   
  
>   1. 当 `depositOriginator` 是 `1` 时必填。
>   2. 当 `country` 是 `cn`(中国) 或 `ua`(乌克兰) 时。
>      1. 如果 `country` 是 `cn`(中国)，`region` 需要为 `isNortheasternProvinces`(东北三省)，即黑龙江，吉林和辽宁，或者 `other`。
>      2. 如果 `country` 是 `ua`(乌克兰)，`region` 不能为 `crimea`(克里米亚)，`donetsk`(顿涅茨克) 或 `luhansk`(卢甘斯克), 可以为 `other`。
> 


## 哈萨克斯坦

名称| 类型| 是否必须| 描述  
---|---|---|---  
originatorName| STRING| YES| 发款人姓名  
country| STRING| YES| 发款人国家二位字母代码(ISO-3166)，必须为小写. 有关此信息，请参阅`附录`中的`国家和地区`部分。  
city| STRING| YES| 发款人所在城市  
txnPurpose| STRING| YES| 合理值: service, goods, p2p, charity, others  
txnPurposeOthers| STRING| YES *1|   
  
>   1. 当 `txnPurpose` 是 `others` 时必填.
> 


## 巴林

名称| 类型| 是否必须| 描述  
---|---|---|---  
depositOriginator| INTEGER| YES| 1 = 发款人是自己, 2 = 发款人不是自己  
orgType| INTEGER| YES *1| 0 = 个人账号, 1 = 企业账号  
orgFirstName| STRING| YES *1| 发款人名, 姓名的相关信息，请参阅`附录`中的`姓名限制`部分。  
orgLastName| STRING| YES *1| 发款人姓, 姓名的相关信息，请参阅`附录`中的`姓名限制`部分。  
country| STRING| YES *1| 发款人居住国二位字母代码(ISO-3166)，必须为小写. 有关此信息，请参阅`附录`中的`国家和地区`部分。  
city| STRING| YES *1|   
receiveFrom| INTEGER| YES| 1 = 私有钱包, 2 = 其他交易所  
vasp| STRING| YES *2| 发款人的VASP identifier  
vaspName| STRING| YES *3| VASP名  
  
>   1. 当 `depositOriginator` 是 `2` 时必填。
>   2. 当 `receiveFrom` 是 `2` 时必填。
>   3. 当 `vasp` 是 `others` 时必填。
>   4. `Vasp List` 接口提供 VASP 及其标识符信息。如果`vasp`不在`预先加载VASP列表`中, `vasp`字段请填`others`, `vaspName`字段请填交易所的名字。
> 


## 阿联酋

名称| 类型| 是否必须| 描述  
---|---|---|---  
depositOriginator| INTEGER| YES| 1 = 发款人是自己, 2 = 发款人不是自己  
orgType| INTEGER| YES *1| 0 = 个人账号, 1 = 企业账号  
orgName| STRING| YES *1| 姓名的相关信息，请参阅`附录`中的`姓名限制`部分。  
country| STRING| YES *1| 发款人国籍二位字母代码(ISO-3166)，必须为小写. 有关此信息，请参阅`附录`中的`国家和地区`部分。  
city| STRING| YES *1|   
receiveFrom| INTEGER| YES| 1 = 私有钱包, 2 = 其他交易所  
vasp| STRING| YES *2| 收款人的VASP identifier  
vaspName| STRING| YES *3| VASP名  
  
>   1. 当 `depositOriginator` 是 `2` 时必填。
>   2. 当 `receiveFrom` 是 `2` 时必填。
>   3. 当 `vasp` 是 `others` 时必填。
>   4. `Vasp List` 接口提供 VASP 及其标识符信息。如果`vasp`不在`预先加载VASP列表`中, `vasp`字段请填`others`, `vaspName`字段请填交易所的名字。
> 


## 印度

名称| 类型| 是否必须| 描述  
---|---|---|---  
depositOriginator| INTEGER| YES| 1 = 发款人是自己, 2 = 发款人不是自己  
orgType| INTEGER| YES *1| 0 = 个人账号, 1 = 企业账号  
orgName| STRING| YES *1| 发款人姓名, 姓名的相关信息，请参阅`附录`中的`姓名限制`部分。  
pan| STRING| YES *1| 永久账号（PAN）或国民身份证号码  
country| STRING| YES *1| 发款人国籍二位字母代码(ISO-3166)，必须为小写. 有关此信息，请参阅`附录`中的`国家和地区`部分。  
state| STRING| YES *1| 发款人所在州  
city| STRING| YES *1| 发款人所在 城市/城镇/村庄  
pinCode| STRING| YES *1|   
address| STRING| YES *1|   
receiveFrom| INTEGER| YES| 1 = 私有钱包, 2 = 其他交易所  
vasp| STRING| YES *2| 收款人的VASP identifier  
vaspName| STRING| YES *3| VASP名  
  
>   1. 当 `depositOriginator` 是 `2`时必填.
>   2. 当 `receiveFrom` 是 `2`时必填.
>   3. 当 `vasp` 是 `others` 时必填。
>   4. `Vasp List` 接口提供 VASP 及其标识符信息。如果`vasp`不在`预先加载VASP列表`中, `vasp`字段请填`others`, `vaspName`字段请填交易所的名字。
> 


## 欧洲(波兰,法国)

名称| 类型| 是否必须| 描述  
---|---|---|---  
depositOriginator| INTEGER| YES| 1 = 发款人是自己, 2 = 发款人不是自己  
orgType| INTEGER| YES *1| 0 = 个人账号, 1 = 企业账号  
orgFirstName| STRING| YES *2| 发款人名, 姓名的相关信息，请参阅`附录`中的`姓名限制`部分。  
orgLastName| STRING| YES *2| 发款人姓, 姓名的相关信息，请参阅`附录`中的`姓名限制`部分。  
country| STRING| YES *2| 发款人国家, 有关此信息，请参阅`附录`中的`国家和地区`部分。  
corpName| STRING| YES *3| 发款企业姓名  
corpCountry| STRING| YES *3| 发款企业所在国家  
receiveFrom| INTEGER| YES| 1 = 私有钱包, 2 = 其他交易所  
vasp| STRING| YES *4| 交易所 identifier  
vaspName| STRING| YES *5| 交易所名称  
declaration| BOOLEAN| YES|   
  
>   1. 当 `depositOriginator` 是 `2` 时必填.
>   2. 当 `orgType` is `0` 时必填.
>   3. 当 `orgType` is `1` 时必填.
>   4. 当 `receiveFrom` is `2` 时必填.
>   5. `Vasp List` 接口提供 VASP 及其标识符信息。如果`vasp`不在`预先加载VASP列表`中, `vasp`字段请填`others`, `vaspName`字段请填交易所的名字。
> 


## 南非

名称| 类型| 是否必须| 描述  
---|---|---|---  
depositOriginator| INTEGER| YES| 1 = 发款人是自己, 2 = 发款人不是自己  
orgType| INTEGER| YES *1| 0 = 个人账号, 1 = 企业账号  
orgName| STRING| YES *2| 发款人姓名, 姓名的相关信息，请参阅`附录`中的`姓名限制`部分。  
country| STRING| YES *2| 发款人国家, 有关此信息，请参阅`附录`中的`国家和地区`部分。  
corpName| STRING| YES *3| 发款企业姓名  
corpCountry| STRING| YES *3| 发款企业所在国家, 有关此信息，请参阅`附录`中的`国家和地区`部分。  
receiveFrom| INTEGER| YES| 1 = 私有钱包, 2 = 其他交易所  
vasp| STRING| YES *4| 交易所 identifier  
vaspName| STRING| YES *5| 交易所名称  
declaration| BOOLEAN| YES|   
  
>   1. 当 `depositOriginator` 是 `2` 时必填.
>   2. 当 `orgType` is `0` 时必填.
>   3. 当 `orgType` is `1` 时必填.
>   4. 当 `receiveFrom` is `2` 时必填.
>   5. `Vasp List` 接口提供 VASP 及其标识符信息。如果`vasp`不在`预先加载VASP列表`中, `vasp`字段请填`others`, `vaspName`字段请填交易所的名字。
> 


## 澳大利亚

名称| 类型| 是否必须| 描述  
---|---|---|---  
depositOriginator| INTEGER| YES| 1 = 发款人是自己, 2 = 发款人不是自己  
orgType| INTEGER| YES *1| 0 = 个人账号, 1 = 企业账号  
orgFirstName| STRING| YES *2| 发款人名。姓名的相关信息，请参阅`附录`中的`姓名限制`部分。  
orgLastName| STRING| YES *2| 发款人姓。姓名的相关信息，请参阅`附录`中的`姓名限制`部分。  
country| STRING| YES *2| 发款人国家二位字母代码(ISO-3166)，必须为小写。通过`国家列表`接口获取。  
city| STRING| YES *2| 发款人城市/城镇。通过`地区列表`接口获取（使用 `regionName` 值）。  
corpName| STRING| YES *3| 公司/实体名称  
corpCountry| STRING| YES *3| 公司国家二位字母代码(ISO-3166)，必须为小写。通过`国家列表`接口获取。  
corpCity| STRING| YES *3| 公司城市/城镇。通过`地区列表`接口获取（使用 `regionName` 值）。  
identifierType| STRING| NO| 参见下方`证件类型选项`。  
identifier| STRING| YES *6| 对应 `identifierType` 的证件号码。  
receiveFrom| INTEGER| YES| 1 = 私有钱包, 2 = 其他交易所  
vasp| STRING| YES *4| 发款人的VASP identifier  
vaspName| STRING| YES *5| VASP 名称  
declaration| BOOLEAN| YES| 声明确认  
  
>   1. 当 `depositOriginator` 是 `2` 时必填。
>   2. 当 `orgType` 是 `0`（个人）时必填。
>   3. 当 `orgType` 是 `1`（公司/实体）时必填。
>   4. 当 `receiveFrom` 是 `2` 时必填。
>   5. 当 `vasp` 是 `others` 时必填。
>   6. 当 `identifierType` 有值时必填。
>   7. `Vasp List` 接口提供 VASP 及其标识符信息。如果 `vasp` 不在`预先加载VASP列表`中，`vasp`字段请填 `others`，`vaspName` 字段请填交易所的名字。
> 


**证件类型选项（Identifier Type Options）：**

identifierType| 含义| 适用条件| 校验规则  
---|---|---|---  
PASSPORT| 护照号码| `orgType` = 0（个人）| 字母数字，1–50 字符  
NATIONAL_ID| 国民身份证号码| `orgType` = 0（个人）| 字母数字，1–50 字符  
ABN| 澳大利亚商业号码| `orgType` = 1（公司）| 恰好 11 位数字  
ACN| 澳大利亚公司号码| `orgType` = 1（公司）| 恰好 9 位数字  
OTHER| 其他注册号码| `orgType` = 1（公司）| 字母数字，1–50 字符  
  
## 巴西

名称| 类型| 是否必须| 描述  
---|---|---|---  
depositOriginator| INTEGER| YES| 1 = 本人充值, 2 = 他人充值  
receiveFrom| INTEGER| YES| 1 = 自托管钱包, 2 = VASP / 交易所  
vasp| STRING| YES *6| 发款人的 VASP identifier。通过`Vasp List`接口获取。  
declaration| BOOLEAN| YES| 声明确认，必须为 `true`。  
orgType| INTEGER| YES *1| 0 = 个人账号, 1 = 企业账号  
orgFirstName| STRING| YES *2| 发款人名。  
orgLastName| STRING| YES *2| 发款人姓。  
country| STRING| YES *2| 发款人国家二位字母代码(ISO-3166)，必须为小写。通过`国家列表`接口获取。  
corpName| STRING| YES *3| 公司/实体名称  
corpCountry| STRING| YES *3| 公司国家二位字母代码(ISO-3166)，必须为小写。通过`国家列表`接口获取。  
cpf| STRING| YES *4| CPF（巴西个人税号）。参见下方`税务标识规则`。  
cnpj| STRING| YES *4| CNPJ（巴西公司税号）。参见下方`税务标识规则`。  
individualTaxId| STRING| YES *5| 个人税务识别号。参见下方`税务标识规则`。  
corporateTaxId| STRING| YES *5| 公司税务识别号。参见下方`税务标识规则`。  
txnPurpose| STRING| YES *7| 交易目的编码（如 `12995`）。相关信息请参阅`附录`中的`巴西监管编码`部分。  
counterpartyType| STRING| YES *7| 对手方类型编码，以字符串传入（如 `"03"`）。相关信息请参阅`附录`中的`巴西监管编码`部分。  
relationship| STRING| YES *8| 关系编码，`40` 或 `50`。相关信息请参阅`附录`中的`巴西监管编码`部分。  
  
>   1. 当 `depositOriginator` 是 `2` 时必填。
>   2. 当 `depositOriginator` 是 `2` 且 `orgType` 是 `0`（个人）时必填。
>   3. 当 `depositOriginator` 是 `2` 且 `orgType` 是 `1`（公司/实体）时必填。
>   4. 当 `depositOriginator` 是 `2` 且发款人国家（`country` 或 `corpCountry`）是 `br`（境内）时必填：个人填 `cpf`，公司/实体填 `cnpj`。
>   5. 当 `depositOriginator` 是 `2` 且发款人国家（`country` 或 `corpCountry`）不是 `br`（跨境）时必填：个人填 `individualTaxId`，公司/实体填 `corporateTaxId`。
>   6. 当 `receiveFrom` 是 `2` 时必填。仅接受 `Vasp List` 接口返回的 VASP，不支持 `others`。
>   7. 跨境转账时必填：`depositOriginator` 是 `2` 且发款人国家不是 `br`。
>   8. 来自公司/实体发款人的跨境转账时必填：`depositOriginator` 是 `2`、发款人国家不是 `br` 且 `orgType` 是 `1`。
> 


**交易金额上限：** 单笔超过等值 USD 100,000 的跨境充值将被拦截，返回错误 `-30106`（`Transaction amount exceeds the limit.`）。上限按交易时的 USD 等值计算。来自自托管钱包的充值以及境内（BR 对 BR）转账不受限制。来自您本人在巴西境外 VASP 账户的充值属于跨境，受上限约束。

**税务标识规则（Tax Identifier Rules）：**

字段| 适用条件| 格式  
---|---|---  
cpf| `orgType` = 0（个人）且 `country` = `br`| `###.###.###-##`（11 位数字），必须包含分隔符：`^\d{3}.\d{3}-\d{2}$`。仅校验格式，不校验校验位。  
cnpj| `orgType` = 1（公司）且 `corpCountry` = `br`| `##.###.###/####-##`（14 位数字），必须包含分隔符：`^\d{2}.\d{3}/\d{4}-\d{2}$`。仅校验格式，不校验校验位。  
individualTaxId| `orgType` = 0（个人）且 `country` ≠ `br`| 5–50 位字母数字：`^[A-Za-z0-9]{5,50}$`  
corporateTaxId| `orgType` = 1（公司）且 `corpCountry` ≠ `br`| 5–50 位字母数字：`^[A-Za-z0-9]{5,50}$`  
  
此页面是否有帮助？

Last modified on November 12, 2026

[附录](/zh-CN/docs/products/wallet/travel-rule/appendix)[提币问卷内容(针对需要旅行规则的本地站)](/zh-CN/docs/products/wallet/travel-rule/withdraw-questionnaire)