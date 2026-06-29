---
exchange: binance
source_url: https://developers.binance.com/docs/wallet/travel-rule/withdraw-history-v2
api_type: REST
updated_at: 2026-06-29 19:12:36.069831
---

# Withdraw Questionnaire Contents (for existing local entities)

## Local Entities[​](/docs/wallet/travel-rule/withdraw-questionnaire#local-entities "Direct link to Local Entities")

  * [Japan](/docs/wallet/travel-rule/withdraw-questionnaire#japan)
  * [Kazakhstan](/docs/wallet/travel-rule/withdraw-questionnaire#kazakhstan)
  * [New Zealand](/docs/wallet/travel-rule/withdraw-questionnaire#new-zealand)
  * [Bahrain](/docs/wallet/travel-rule/withdraw-questionnaire#bahrain)
  * [UAE(United Arab Emirates)](/docs/wallet/travel-rule/withdraw-questionnaire#uae)
  * [India](/docs/wallet/travel-rule/withdraw-questionnaire#india)
  * [EU(Poland,France)](/docs/wallet/travel-rule/withdraw-questionnaire#eupolandfrance)
  * [South Africa](/docs/wallet/travel-rule/withdraw-questionnaire#south-africa)
  * [Australia](/docs/wallet/travel-rule/withdraw-questionnaire#australia)



> Please refer to `Check Questionnaire Requirements` if you are unsure of which questionnaire content to be used.

## Japan[​](/docs/wallet/travel-rule/withdraw-questionnaire#japan "Direct link to Japan")

Name| Type| Mandatory| Description  
---|---|---|---  
isAddressOwner| INTEGER| YES| 1:Send to myself, 2:Send to another beneficiary.  
bnfType| INTEGER| YES *1| 0:Individual, 1:Corporate/Entity  
kanjiName| STRING| YES *1|   
kanaName| STRING| YES *1|   
latinName| STRING| YES *1| For more information please refer to the `Name restrictions` section in the `appendix`.  
country| STRING| YES| Beneficiary country code, ISO 2 digit, lower case. For more information please refer to the `Countries and Regions` section in the `appendix`.  
city| STRING| YES|   
sendTo| INTEGER| YES| 1:Crypto-asset services provider, 2:Unhosted Wallet  
vasp| STRING| YES *2| Vasp identifier of the beneficiary  
vaspCountry| STRING| YES *2| VASP country code, ISO 2 digit, lower case.  
vaspRegion| STRING| YES *3|   
txnPurpose| INTEGER| YES *4| 1:Purchase of goods within Japan, 2:Inheritance, gift or living expenses, 3:Cross border trade, 4:Investment, 5:Use of services provided by the beneficiary VASP, 6:Loan repayment, 7:Gifts & Donations  
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


## Kazakhstan[​](/docs/wallet/travel-rule/withdraw-questionnaire#kazakhstan "Direct link to Kazakhstan")

Name| Type| Mandatory| Description  
---|---|---|---  
isAddressOwner| BOOLEAN| YES| Whether the address is owned by the user.  
bnfType| INTEGER| YES *1| 0:Individual, 1:Corporate/Entity  
beneficiaryName| STRING| YES *1| For more information please refer to the `Name restrictions` section in the `appendix`.  
beneficiaryCountry| STRING| YES| Beneficiary country code, ISO 2 digit, lower case. For more information please refer to the `Countries and Regions` section in the `appendix`.  
beneficiaryCity| STRING| YES|   
txnPurpose| STRING| YES| Value: service, goods, p2p, charity, others  
txnPurposeOthers| STRING| YES *4|   
sendTo| INTEGER| YES| 2:Exchange, 1:Unhosted Wallet  
vasp| STRING| YES *2| Vasp identifier of the beneficiary  
vaspName| STRING| YES *3| VASP Name  
isAttested| BOOLEAN| YES|   
  
>   1. Required when `isAddressOwner` is `false`.
>   2. Required when `sendTo` is `2`.
>   3. Required when `vasp` is `others`.
>   4. Required when `txnPurpose` is `others`.
>   5. The `Vasp List` API provides the VASP and identifier information. If the VASP cannot be found, please input `others` within `vasp` and the name of the exchange within `vaspName` field.
> 


## New Zealand[​](/docs/wallet/travel-rule/withdraw-questionnaire#new-zealand "Direct link to New Zealand")

Name| Type| Mandatory| Description  
---|---|---|---  
isAddressOwner| INTEGER| YES| 1:Send to myself, 2:Send to another beneficiary  
bnfType| INTEGER| YES *1| 0:Individual, 1:Corporate/Entity  
bnfName| STRING| YES *2| Individual beneficiary name, for more information please refer to the `Name restrictions` section in the `appendix`.  
country| STRING| YES *2| Beneficiary country code, ISO 2 digit, lower case. For more information please refer to the `Countries and Regions` section in the `appendix`.  
bnfCorpName| STRING| YES *3| Beneficiary corporation name.  
bnfCorpCountry| STRING| YES *3| Beneficiary corporation country code, ISO 2 digit, lower case. For more information please refer to the `Countries and Regions` section in the `appendix`.  
sendTo| INTEGER| YES| 1:Private Wallet, 2:Another VASP  
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


## Bahrain[​](/docs/wallet/travel-rule/withdraw-questionnaire#bahrain "Direct link to Bahrain")

Name| Type| Mandatory| Description  
---|---|---|---  
isAddressOwner| INTEGER| YES| 1:Send to myself, 2:Send to another beneficiary  
bnfType| INTEGER| YES *1| 0:Individual, 1:Corporate/Entity  
bnfFirstName| STRING| YES *2| Individual beneficiary first name. For more information please refer to the `Name restrictions` section in the `appendix`.  
bnfLastName| STRING| YES *2| Individual beneficiary last name. For more information please refer to the `Name restrictions` section in the `appendix`.  
bnfName| STRING| YES *3| Beneficiary corporation/entity name.  
country| STRING| YES *1| Beneficiary country code, ISO 2 digit, lower case. For more information please refer to the `Countries and Regions` section in the `appendix`.  
city| STRING| YES *1|   
sendTo| INTEGER| YES| 1:Private Wallet, 2:Another VASP  
vasp| STRING| YES *4| Vasp identifier of the beneficiary  
vaspName| STRING| YES *5| VASP Name  
  
>   1. Required when `isAddressOwner` is `2`.
>   2. Required when `bnfType` is `0`(Individual).
>   3. Required when `bnfType` is `1`(Corporate/Entity).
>   4. Required when `sendTo` is `2`.
>   5. Required when `vasp` is `others`.
>   6. The `Vasp List` API provides the VASP and identifier information. If the VASP cannot be found, please input `others` within `vasp` and the name of the exchange within `vaspName` field.
> 


## UAE[​](/docs/wallet/travel-rule/withdraw-questionnaire#uae "Direct link to UAE")

Name| Type| Mandatory| Description  
---|---|---|---  
isAddressOwner| INTEGER| YES| 1:Send to myself, 2:Send to another beneficiary  
bnfType| INTEGER| YES *1| 0:Individual, 1:Corporate/Entity  
bnfName| STRING| YES *1| For more information please refer to the `Name restrictions` section in the `appendix`.  
country| STRING| YES *1| Beneficiary country code, ISO 2 digit, lower case. For more information please refer to the `Countries and Regions` section in the `appendix`.  
city| STRING| YES *1|   
sendTo| INTEGER| YES| 1:Private Wallet, 2:Another VASP  
vasp| STRING| YES *2| Vasp identifier of the beneficiary  
vaspName| STRING| YES *3| VASP Name  
  
>   1. Required when `isAddressOwner` is `2`.
>   2. Required when `sendTo` is `2`.
>   3. Required when `vasp` is `others`.
>   4. The `Vasp List` API provides the VASP and identifier information. If the VASP cannot be found, please input `others` within `vasp` and the name of the exchange within `vaspName` field.
> 


## India[​](/docs/wallet/travel-rule/withdraw-questionnaire#india "Direct link to India")

Name| Type| Mandatory| Description  
---|---|---|---  
isAddressOwner| INTEGER| YES| 1:Send to myself, 2:Send to another beneficiary  
bnfType| INTEGER| YES *1| 0:Individual, 1:Corporate/Entity  
bnfName| STRING| YES *1| For more information please refer to the `Name restrictions` section in the `appendix`.  
country| STRING| YES *1| Beneficiary country code, ISO 2 digit, lower case. For more information please refer to the `Countries and Regions` section in the `appendix`.  
city| STRING| NO|   
sendTo| INTEGER| YES| 1:Private Wallet, 2:Another VASP  
vasp| STRING| YES *2| VASP identifier of the beneficiary  
vaspName| STRING| YES *3| VASP Name  
  
>   1. Required when `isAddressOwner` is `2`.
>   2. Required when `sendTo` is `2`.
>   3. Required when `vasp` is `others`.
>   4. The `Vasp List` API provides the VASP and identifier information. If the VASP cannot be found, please input `others` within `vasp` and the name of the exchange within `vaspName` field.
> 


## EU(Poland,France)[​](/docs/wallet/travel-rule/withdraw-questionnaire#eupolandfrance "Direct link to EU\(Poland,France\)")

For all the EU countries, please following the same questionnaire.

Name| Type| Mandatory| Description  
---|---|---|---  
isAddressOwner| INTEGER| YES| 1:Send to myself, 2:Send to another beneficiary  
bnfType| INTEGER| YES *1| 0:Individual, 1:Corporate/Entity  
bnfFirstName| STRING| YES *2| Individual beneficiary first name. For more information please refer to the `Name restrictions` section in the `appendix`.  
bnfLastName| STRING| YES *2| Individual beneficiary last name. For more information please refer to the `Name restrictions` section in the `appendix`.  
country| STRING| YES *2| Beneficiary country code, ISO 2 digit, lower case.  
bnfCorpName| STRING| YES *3| Beneficiary corporation name.  
bnfCorpCountry| STRING| YES *3| Beneficiary corporation country code, ISO 2 digit, lower case. For more information please refer to the `Countries and Regions` section in the `appendix`.  
sendTo| INTEGER| YES| 1:Private Wallet, 2:Another VASP  
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


## South Africa[​](/docs/wallet/travel-rule/withdraw-questionnaire#south-africa "Direct link to South Africa")

Name| Type| Mandatory| Description  
---|---|---|---  
isAddressOwner| INTEGER| YES| 1:Send to myself, 2:Send to another beneficiary  
bnfType| INTEGER| YES *1| 0:Individual, 1:Corporate/Entity  
bnfName| STRING| YES *2| Individual beneficiary name. For more information please refer to the `Name restrictions` section in the `appendix`.  
country| STRING| YES *2| Beneficiary country code, ISO 2 digit, lower case.  
bnfCorpName| STRING| YES *3| Beneficiary corporation name.  
bnfCorpCountry| STRING| YES *3| Beneficiary corporation country code, ISO 2 digit, lower case. For more information please refer to the `Countries and Regions` section in the `appendix`.  
sendTo| INTEGER| YES| 1:Private Wallet, 2:Another VASP  
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


## Australia[​](/docs/wallet/travel-rule/withdraw-questionnaire#australia "Direct link to Australia")

Name| Type| Mandatory| Description  
---|---|---|---  
isAddressOwner| INTEGER| YES| 1:Send to myself, 2:Send to another beneficiary  
bnfType| INTEGER| YES *1| 0:Individual, 1:Corporate/Entity  
bnfFirstName| STRING| YES *2| Individual beneficiary first name. For more information please refer to the `Name restrictions` section in the `appendix`.  
bnfLastName| STRING| YES *2| Individual beneficiary last name. For more information please refer to the `Name restrictions` section in the `appendix`.  
country| STRING| YES *2| Beneficiary country code, ISO 2 digit, lower case. Obtained from `Country List` API.  
city| STRING| YES *2| Beneficiary city/town. Obtained from `Region List` API (`regionName` value).  
bnfCorpName| STRING| YES *3| Beneficiary corporation name.  
bnfCorpCountry| STRING| YES *3| Beneficiary corporation country code, ISO 2 digit, lower case. Obtained from `Country List` API.  
bnfCorpCity| STRING| YES *3| Beneficiary corporation city/town. Obtained from `Region List` API (`regionName` value).  
sendTo| INTEGER| YES| 1:Private Wallet, 2:Another VASP  
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

---

# 提币问卷内容(针对需要旅行规则的本地站)

## 本地站列表[​](/docs/zh-CN/wallet/travel-rule/withdraw-questionnaire#本地站列表 "本地站列表的直接链接")

  * [日本](/docs/zh-CN/wallet/travel-rule/withdraw-questionnaire#%E6%97%A5%E6%9C%AC)
  * [哈萨克斯坦](/docs/zh-CN/wallet/travel-rule/withdraw-questionnaire#%E5%93%88%E8%90%A8%E5%85%8B%E6%96%AF%E5%9D%A6)
  * [新西兰](/docs/zh-CN/wallet/travel-rule/withdraw-questionnaire#%E6%96%B0%E8%A5%BF%E5%85%B0)
  * [巴林](/docs/zh-CN/wallet/travel-rule/withdraw-questionnaire#%E5%B7%B4%E6%9E%97)
  * [阿联酋](/docs/zh-CN/wallet/travel-rule/withdraw-questionnaire#%E9%98%BF%E8%81%94%E9%85%8B)
  * [印度](/docs/zh-CN/wallet/travel-rule/withdraw-questionnaire#%E5%8D%B0%E5%BA%A6)
  * [欧洲(波兰,法国)](/docs/zh-CN/wallet/travel-rule/withdraw-questionnaire#%E6%AC%A7%E6%B4%B2%E6%B3%A2%E5%85%B0%E6%B3%95%E5%9B%BD)
  * [南非](/docs/zh-CN/wallet/travel-rule/withdraw-questionnaire#%E5%8D%97%E9%9D%9E)
  * [澳大利亚](/docs/zh-CN/wallet/travel-rule/withdraw-questionnaire#%E6%BE%B3%E5%A4%A7%E5%88%A9%E4%BA%9A)



> 如果您不确定使用的问卷内容，请参阅`检查问卷需求`.

## 日本[​](/docs/zh-CN/wallet/travel-rule/withdraw-questionnaire#日本 "日本的直接链接")

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


## 哈萨克斯坦[​](/docs/zh-CN/wallet/travel-rule/withdraw-questionnaire#哈萨克斯坦 "哈萨克斯坦的直接链接")

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


## 新西兰[​](/docs/zh-CN/wallet/travel-rule/withdraw-questionnaire#新西兰 "新西兰的直接链接")

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


## 巴林[​](/docs/zh-CN/wallet/travel-rule/withdraw-questionnaire#巴林 "巴林的直接链接")

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


## 阿联酋[​](/docs/zh-CN/wallet/travel-rule/withdraw-questionnaire#阿联酋 "阿联酋的直接链接")

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


## 印度[​](/docs/zh-CN/wallet/travel-rule/withdraw-questionnaire#印度 "印度的直接链接")

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


## 欧洲(波兰,法国)[​](/docs/zh-CN/wallet/travel-rule/withdraw-questionnaire#欧洲波兰法国 "欧洲\(波兰,法国\)的直接链接")

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


## 南非[​](/docs/zh-CN/wallet/travel-rule/withdraw-questionnaire#南非 "南非的直接链接")

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


## 澳大利亚[​](/docs/zh-CN/wallet/travel-rule/withdraw-questionnaire#澳大利亚 "澳大利亚的直接链接")

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