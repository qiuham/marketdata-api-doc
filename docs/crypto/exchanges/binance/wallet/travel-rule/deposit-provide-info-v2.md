---
exchange: binance
source_url: https://developers.binance.com/docs/wallet/travel-rule/deposit-provide-info-v2
api_type: REST
updated_at: 2026-05-27 19:00:03.108842
---

# Deposit Questionnaire Contents (for existing local entities)

## Local Entities[​](/docs/wallet/travel-rule/deposit-questionnaire#local-entities "Direct link to Local Entities")

  * [Japan](/docs/wallet/travel-rule/deposit-questionnaire#japan)
  * [Kazakhstan](/docs/wallet/travel-rule/deposit-questionnaire#kazakhstan)
  * [Bahrain](/docs/wallet/travel-rule/deposit-questionnaire#bahrain)
  * [UAE](/docs/wallet/travel-rule/deposit-questionnaire#united-arab-emirates)
  * [India](/docs/wallet/travel-rule/deposit-questionnaire#india)
  * [EU(Poland,France)](/docs/wallet/travel-rule/deposit-questionnaire#eupolandfrance)
  * [South Africa](/docs/wallet/travel-rule/deposit-questionnaire#south-africa)



## Japan[​](/docs/wallet/travel-rule/deposit-questionnaire#japan "Direct link to Japan")

Name| Type| Mandatory| Description  
---|---|---|---  
depositOriginator| INTEGER| YES| 2:Myself, 1:Not Myself  
bnfType| INTEGER| YES| 0:Individual, 1:Corporate/Entity  
country| STRING| YES *1| Originator country code, ISO 2 digit, lower case. For more information please refer to the `Countries and Regions` section in the `appendix`.  
region| STRING| YES *2| Originator region  
city| STRING| YES *1| Originator’s city/village/town.  
kanjiName| STRING| YES *1|   
kanaName| STRING| YES *1|   
latinName| STRING| YES *1| For more information please refer to the `Name restrictions` section in the `appendix`.  
vaspName| STRING| YES|   
isAttested| BOOLEAN| YES|   
  
>   1. Required when `depositOriginator` is `1`.
>   2. Required when `country` is `cn`(China) or `ua`(Ukraine). > 1\. If `country` is `cn`(China), `region` must be `notNortheasternProvinces` (Jilin, Liaoning and Heilongjiang) or `other`. 2\. If `country` is `ua`(Ukraine), `region` should not be `crimea`, `donetsk` or `luhansk`，should be `other`.
> 


## Kazakhstan[​](/docs/wallet/travel-rule/deposit-questionnaire#kazakhstan "Direct link to Kazakhstan")

Name| Type| Mandatory| Description  
---|---|---|---  
originatorName| STRING| YES| Name of originator.  
country| STRING| YES| Originator country code, ISO 2 digit, lower case. For more information please refer to the `Countries and Regions` section in the `appendix`.  
city| STRING| YES| Originator’s city/village/town.  
txnPurpose| STRING| YES| Value: service, goods, p2p, charity, others  
txnPurposeOthers| STRING| YES *1|   
  
>   1. Required when `txnPurpose` is `others`.
> 


## Bahrain[​](/docs/wallet/travel-rule/deposit-questionnaire#bahrain "Direct link to Bahrain")

Name| Type| Mandatory| Description  
---|---|---|---  
depositOriginator| INTEGER| YES| 1:Myself, 2:Not myself  
orgType| INTEGER| YES *1| 0:Individual, 1:Corporate/Entity  
orgFirstName| STRING| YES *1| Originator's First Name, for more information please refer to the `Name restrictions` section in the `appendix`.  
orgLastName| STRING| YES *1| Originator's Last Name, for more information please refer to the `Name restrictions` section in the `appendix`.  
country| STRING| YES *1| Originator's residence country code, ISO 2 digit, lower case. For more information please refer to the `Countries and Regions` section in the `appendix`.  
city| STRING| YES *1|   
receiveFrom| INTEGER| YES| 1:Private Wallet, 2:Another VASP  
vasp| STRING| YES *2| Vasp identifier of the originator.  
vaspName| STRING| YES *3|   
  
>   1. Required when `depositOriginator` is `2`.
>   2. Required when `receiveFrom` is `2`.
>   3. Required when `vasp` is `others`.
>   4. The `Vasp List` API provides the VASP and identifier information. If the VASP cannot be found, please input `others` within `vasp list` and the name of the exchange within `vaspName` field.
> 


## United Arab Emirates[​](/docs/wallet/travel-rule/deposit-questionnaire#united-arab-emirates "Direct link to United Arab Emirates")

Name| Type| Mandatory| Description  
---|---|---|---  
depositOriginator| INTEGER| YES| 1:Myself, 2:Not myself  
orgType| INTEGER| YES *1| 0:Individual, 1:Corporate/Entity  
orgName| STRING| YES *1| For more information please refer to the `Name restrictions` section in the `appendix`.  
country| STRING| YES *1| Originator's nationality code, ISO 2 digit, lower case. For more information please refer to the `Countries and Regions` section in the `appendix`.  
city| STRING| YES *1|   
receiveFrom| INTEGER| YES| 1:Private Wallet, 2:Another VASP  
vasp| STRING| YES *2| Vasp identifier of the beneficiary  
vaspName| STRING| YES *3|   
  
>   1. Required when `depositOriginator` is `2`.
>   2. Required when `receiveFrom` is `2`.
>   3. Required when `vasp` is `others`.
>   4. The `Vasp List` API provides the VASP and identifier information. If the VASP cannot be found, please input `others` within `vasp list` and the name of the exchange within `vaspName` field.
> 


## India[​](/docs/wallet/travel-rule/deposit-questionnaire#india "Direct link to India")

Name| Type| Mandatory| Description  
---|---|---|---  
depositOriginator| INTEGER| YES| 1:Myself, 2:Not myself  
orgType| INTEGER| YES *1| 0:Individual, 1:Corporate/Entity  
orgName| STRING| YES *1| Originator's Name, for more information please refer to the `Name restrictions` section in the `appendix`.  
pan| STRING| YES *1| Permanent Account Number (PAN) or National ID Number  
country| STRING| YES *1| Originator's nationality code, ISO 2 digit, lower case. For more information please refer to the `Countries and Regions` section in the `appendix`.  
state| STRING| YES *1| Originator's State  
city| STRING| YES *1| Originator’s City/Village/Town  
pinCode| STRING| YES *1|   
address| STRING| YES *1|   
receiveFrom| INTEGER| YES| 1:Private Wallet, 2:Another VASP  
vasp| STRING| YES *2| Vasp identifier of the beneficiary  
vaspName| STRING| YES *3|   
  
>   1. Required when `depositOriginator` is `2`.
>   2. Required when `receiveFrom` is `2`.
>   3. Required when `vasp` is `others`.
>   4. The `Vasp List` API provides the VASP and identifier information. If the VASP cannot be found, please input `others` within `vasp list` and the name of the exchange within `vaspName` field.
> 


## EU(Poland,France)[​](/docs/wallet/travel-rule/deposit-questionnaire#eupolandfrance "Direct link to EU\(Poland,France\)")

Name| Type| Mandatory| Description  
---|---|---|---  
depositOriginator| INTEGER| YES| 1:Myself, 2:Not myself  
orgType| INTEGER| YES *1| 0:Individual, 1:Corporate/Entity  
orgFirstName| STRING| YES *2| Originator's First Name, for more information please refer to the `Name restrictions` section in the `appendix`.  
orgLastName| STRING| YES *2| Originator's Last Name, for more information please refer to the `Name restrictions` section in the `appendix`.  
country| STRING| YES *2| Originator's nationality code, ISO 2 digit, lower case. For more information please refer to the `Countries and Regions` section in the `appendix`.  
corpName| STRING| YES *3| Originator's (corporation) Name  
corpCountry| STRING| YES *3| Originator's (corporation) nationality code, ISO 2 digit, lower case. For more information please refer to the `Countries and Regions` section in the `appendix`.  
receiveFrom| INTEGER| YES| 1:Private Wallet, 2:Another VASP  
vasp| STRING| YES *4| Vasp identifier of the beneficiary  
vaspName| STRING| YES *5| VASP Name  
declaration| BOOLEAN| YES| Declaration confirmation  
  
>   1. Required when `depositOriginator` is `2`.
>   2. Required when `orgType` is `0`.
>   3. Required when `orgType` is `1`.
>   4. Required when `receiveFrom` is `2`.
>   5. The `Vasp List` API provides the VASP and identifier information. If the VASP cannot be found, please input `others` within `vasp list` and the name of the exchange within `vaspName` field.
> 


## South Africa[​](/docs/wallet/travel-rule/deposit-questionnaire#south-africa "Direct link to South Africa")

Name| Type| Mandatory| Description  
---|---|---|---  
depositOriginator| INTEGER| YES| 1:Myself, 2:Not myself  
orgType| INTEGER| YES *1| 0:Individual, 1:Corporate/Entity  
orgName| STRING| YES *2| Originator's Name, for more information please refer to the `Name restrictions` section in the `appendix`.  
country| STRING| YES *2| Originator's nationality code, ISO 2 digit, lower case. For more information please refer to the `Countries and Regions` section in the `appendix`.  
corpName| STRING| YES *3| Originator's (corporation) Name  
corpCountry| STRING| YES *3| Originator's (corporation) nationality code, ISO 2 digit, lower case. For more information please refer to the `Countries and Regions` section in the `appendix`.  
receiveFrom| INTEGER| YES| 1:Private Wallet, 2:Another VASP  
vasp| STRING| YES *4| Vasp identifier of the beneficiary  
vaspName| STRING| YES *5| VASP Name  
declaration| BOOLEAN| YES| Declaration confirmation  
  
>   1. Required when `depositOriginator` is `2`.
>   2. Required when `orgType` is `0`.
>   3. Required when `orgType` is `1`.
>   4. Required when `receiveFrom` is `2`.
>   5. The `Vasp List` API provides the VASP and identifier information. If the VASP cannot be found, please input `others` within `vasp list` and the name of the exchange within `vaspName` field.
>

---

# 充值问卷内容(针对需要旅行规则的本地站)

## 本地站列表[​](/docs/zh-CN/wallet/travel-rule/deposit-questionnaire#本地站列表 "本地站列表的直接链接")

  * [日本](/docs/zh-CN/wallet/travel-rule/deposit-questionnaire#%E6%97%A5%E6%9C%AC)
  * [哈萨克斯坦](/docs/zh-CN/wallet/travel-rule/deposit-questionnaire#%E5%93%88%E8%90%A8%E5%85%8B%E6%96%AF%E5%9D%A6)
  * [巴林](/docs/zh-CN/wallet/travel-rule/deposit-questionnaire#%E5%B7%B4%E6%9E%97)
  * [阿联酋](/docs/zh-CN/wallet/travel-rule/deposit-questionnaire#%E9%98%BF%E8%81%94%E9%85%8B)
  * [印度](/docs/zh-CN/wallet/travel-rule/deposit-questionnaire#%E5%8D%B0%E5%BA%A6)
  * [欧洲(波兰,法国)](/docs/zh-CN/wallet/travel-rule/deposit-questionnaire#%E6%AC%A7%E6%B4%B2%E6%B3%A2%E5%85%B0%E6%B3%95%E5%9B%BD)
  * [南非](/docs/zh-CN/wallet/travel-rule/deposit-questionnaire#%E5%8D%97%E9%9D%9E)



## 日本[​](/docs/zh-CN/wallet/travel-rule/deposit-questionnaire#日本 "日本的直接链接")

名称| 类型| 是否必须| 描述  
---|---|---|---  
depositOriginator| INTEGER| YES| 2:发款人自己, 1:发款人不是自己  
bnfType| INTEGER| YES| 0:个人账号, 1:企业账号  
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


## 哈萨克斯坦[​](/docs/zh-CN/wallet/travel-rule/deposit-questionnaire#哈萨克斯坦 "哈萨克斯坦的直接链接")

名称| 类型| 是否必须| 描述  
---|---|---|---  
originatorName| STRING| YES| 发款人姓名  
country| STRING| YES| 发款人国家二位字母代码(ISO-3166)，必须为小写. 有关此信息，请参阅`附录`中的`国家和地区`部分。  
city| STRING| YES| 发款人所在城市  
txnPurpose| STRING| YES| 合理值: service, goods, p2p, charity, others  
txnPurposeOthers| STRING| YES *1|   
  
>   1. 当 `txnPurpose` 是 `others` 时必填.
> 


## 巴林[​](/docs/zh-CN/wallet/travel-rule/deposit-questionnaire#巴林 "巴林的直接链接")

名称| 类型| 是否必须| 描述  
---|---|---|---  
depositOriginator| INTEGER| YES| 1:发款人是自己, 2:发款人不是自己  
orgType| INTEGER| YES *1| 0:个人账号, 1:企业账号  
orgFirstName| STRING| YES *1| 发款人名, 姓名的相关信息，请参阅`附录`中的`姓名限制`部分。  
orgLastName| STRING| YES *1| 发款人姓, 姓名的相关信息，请参阅`附录`中的`姓名限制`部分。  
country| STRING| YES *1| 发款人居住国二位字母代码(ISO-3166)，必须为小写. 有关此信息，请参阅`附录`中的`国家和地区`部分。  
city| STRING| YES *1|   
receiveFrom| INTEGER| YES| 1:私有钱包, 2:其他交易所  
vasp| STRING| YES *2| 发款人的VASP identifier  
vaspName| STRING| YES *3| VASP名  
  
>   1. 当 `depositOriginator` 是 `2` 时必填。
>   2. 当 `receiveFrom` 是 `2` 时必填。
>   3. 当 `vasp` 是 `others` 时必填。
>   4. `Vasp List` 接口提供 VASP 及其标识符信息。如果`vasp`不在`预先加载VASP列表`中, `vasp`字段请填`others`, `vaspName`字段请填交易所的名字。
> 


## 阿联酋[​](/docs/zh-CN/wallet/travel-rule/deposit-questionnaire#阿联酋 "阿联酋的直接链接")

名称| 类型| 是否必须| 描述  
---|---|---|---  
depositOriginator| INTEGER| YES| 1:发款人是自己, 2:发款人不是自己  
orgType| INTEGER| YES *1| 0:个人账号, 1:企业账号  
orgName| STRING| YES *1| 姓名的相关信息，请参阅`附录`中的`姓名限制`部分。  
country| STRING| YES *1| 发款人国籍二位字母代码(ISO-3166)，必须为小写. 有关此信息，请参阅`附录`中的`国家和地区`部分。  
city| STRING| YES *1|   
receiveFrom| INTEGER| YES| 1:私有钱包, 2:其他交易所  
vasp| STRING| YES *2| 收款人的VASP identifier  
vaspName| STRING| YES *3| VASP名  
  
>   1. 当 `depositOriginator` 是 `2` 时必填。
>   2. 当 `receiveFrom` 是 `2` 时必填。
>   3. 当 `vasp` 是 `others` 时必填。
>   4. `Vasp List` 接口提供 VASP 及其标识符信息。如果`vasp`不在`预先加载VASP列表`中, `vasp`字段请填`others`, `vaspName`字段请填交易所的名字。
> 


## 印度[​](/docs/zh-CN/wallet/travel-rule/deposit-questionnaire#印度 "印度的直接链接")

名称| 类型| 是否必须| 描述  
---|---|---|---  
depositOriginator| INTEGER| YES| 1:发款人是自己, 2:发款人不是自己  
orgType| INTEGER| YES *1| 0:个人账号, 1:企业账号  
orgName| STRING| YES *1| 发款人姓名, 姓名的相关信息，请参阅`附录`中的`姓名限制`部分。  
pan| STRING| YES *1| 永久账号（PAN）或国民身份证号码  
country| STRING| YES *1| 发款人国籍二位字母代码(ISO-3166)，必须为小写. 有关此信息，请参阅`附录`中的`国家和地区`部分。  
state| STRING| YES *1| 发款人所在州  
city| STRING| YES *1| 发款人所在 城市/城镇/村庄  
pinCode| STRING| YES *1|   
address| STRING| YES *1|   
receiveFrom| INTEGER| YES| 1:私有钱包, 2:其他交易所  
vasp| STRING| YES *2| 收款人的VASP identifier  
vaspName| STRING| YES *3| VASP名  
  
>   1. 当 `depositOriginator` 是 `2`时必填.
>   2. 当 `receiveFrom` 是 `2`时必填.
>   3. 当 `vasp` 是 `others` 时必填。
>   4. `Vasp List` 接口提供 VASP 及其标识符信息。如果`vasp`不在`预先加载VASP列表`中, `vasp`字段请填`others`, `vaspName`字段请填交易所的名字。
> 


## 欧洲(波兰,法国)[​](/docs/zh-CN/wallet/travel-rule/deposit-questionnaire#欧洲波兰法国 "欧洲\(波兰,法国\)的直接链接")

名称| 类型| 是否必须| 描述  
---|---|---|---  
depositOriginator| INTEGER| YES| 1:发款人是自己, 2:发款人不是自己  
orgType| INTEGER| YES *1| 0:个人账号, 1:企业账号  
orgFirstName| STRING| YES *2| 发款人名, 姓名的相关信息，请参阅`附录`中的`姓名限制`部分。  
orgLastName| STRING| YES *2| 发款人姓, 姓名的相关信息，请参阅`附录`中的`姓名限制`部分。  
country| STRING| YES *2| 发款人国家, 有关此信息，请参阅`附录`中的`国家和地区`部分。  
corpName| STRING| YES *3| 发款企业姓名  
corpCountry| STRING| YES *3| 发款企业所在国家  
receiveFrom| INTEGER| YES| 1:私有钱包, 2:其他交易所  
vasp| STRING| YES *4| 交易所 identifier  
vaspName| STRING| YES *5| 交易所名称  
declaration| BOOLEAN| YES|   
  
>   1. 当 `depositOriginator` 是 `2` 时必填.
>   2. 当 `orgType` is `0` 时必填.
>   3. 当 `orgType` is `1` 时必填.
>   4. 当 `receiveFrom` is `2` 时必填.
>   5. `Vasp List` 接口提供 VASP 及其标识符信息。如果`vasp`不在`预先加载VASP列表`中, `vasp`字段请填`others`, `vaspName`字段请填交易所的名字。
> 


## 南非[​](/docs/zh-CN/wallet/travel-rule/deposit-questionnaire#南非 "南非的直接链接")

名称| 类型| 是否必须| 描述  
---|---|---|---  
depositOriginator| INTEGER| YES| 1:发款人是自己, 2:发款人不是自己  
orgType| INTEGER| YES *1| 0:个人账号, 1:企业账号  
orgName| STRING| YES *2| 发款人姓名, 姓名的相关信息，请参阅`附录`中的`姓名限制`部分。  
country| STRING| YES *2| 发款人国家, 有关此信息，请参阅`附录`中的`国家和地区`部分。  
corpName| STRING| YES *3| 发款企业姓名  
corpCountry| STRING| YES *3| 发款企业所在国家, 有关此信息，请参阅`附录`中的`国家和地区`部分。  
receiveFrom| INTEGER| YES| 1:私有钱包, 2:其他交易所  
vasp| STRING| YES *4| 交易所 identifier  
vaspName| STRING| YES *5| 交易所名称  
declaration| BOOLEAN| YES|   
  
>   1. 当 `depositOriginator` 是 `2` 时必填.
>   2. 当 `orgType` is `0` 时必填.
>   3. 当 `orgType` is `1` 时必填.
>   4. 当 `receiveFrom` is `2` 时必填.
>   5. `Vasp List` 接口提供 VASP 及其标识符信息。如果`vasp`不在`预先加载VASP列表`中, `vasp`字段请填`others`, `vaspName`字段请填交易所的名字。
>