---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/wallet/travel-rule/appendix
api_type: REST
updated_at: 2026-11-13 20:30:29.873362
---

# Appendix

## Name restrictions

Strings that match the following regular expression rules are accepted.
    
    
    Code
    
    REGEXP : ^(?=.{1,})(?!.{100,})(?!.*([a-zA-Z])\1{2,})(?!.*[0-9!@#$%^&*()_=.~`<>/:;?€£¥₹₩¢₿+=÷]).*$

  * The string length must be between 1 and 99 characters, inclusive.
  * The string must not contain any digits or a specified set of special characters.
  * The string must not contain any letter repeated consecutively 3 or more times.
  * The string may contain letters (both uppercase and lowercase) and other characters that are not excluded (such as spaces, punctuation marks not listed in the excluded symbols, etc.).



## Country (Regions) ISO code

> You will not be able to use an ISO code that is not listed in the table

Country (Regions)| Code  
---|---  
Afghanistan| af  
Albania| al  
Algeria| dz  
American Samoa| as  
Andorra| ad  
Angola| ao  
Anguilla| ai  
Antigua and Barbuda| ag  
Argentina| ar  
Armenia| am  
Aruba| aw  
Australia| au  
Austria| at  
Azerbaijan| az  
Bahamas (the)| bs  
Bahrain| bh  
Bangladesh| bd  
Barbados| bb  
Belarus| by  
Belgium| be  
Belize| bz  
Benin| bj  
Bermuda| bm  
Bhutan| bt  
Bolivia (Plurinational State of)| bo  
Bonaire, Sint Eustatius and Saba| bq  
Bosnia and Herzegovina| ba  
Botswana| bw  
Bouvet Island| bv  
Brazil| br  
British Indian Ocean Territory (the)| io  
Brunei Darussalam| bn  
Bulgaria| bg  
Burkina Faso| bf  
Burundi| bi  
Cabo Verde| cv  
Cambodia| kh  
Cameroon| cm  
Canada| ca  
Cayman Islands (the)| ky  
Central African Republic (the)| cf  
Chad| td  
Chile| cl  
China| cn  
Christmas Island| cx  
Cocos (Keeling) Islands (the)| cc  
Colombia| co  
Comoros (the)| km  
Congo (the Democratic Republic of the)| cd  
Congo (the)| cg  
Cook Islands (the)| ck  
Costa Rica| cr  
Croatia| hr  
Cuba| cu  
Curaçao| cw  
Cyprus| cy  
Czechia| cz  
Côte d'Ivoire| ci  
Denmark| dk  
Djibouti| dj  
Dominica| dm  
Dominican Republic (the)| do  
Ecuador| ec  
Egypt| eg  
El Salvador| sv  
Equatorial Guinea| gq  
Eritrea| er  
Estonia| ee  
Eswatini| sz  
Ethiopia| et  
Falkland Islands (the) [Malvinas]| fk  
Faroe Islands (the)| fo  
Fiji| fj  
Finland| fi  
France| fr  
French Guiana| gf  
French Polynesia| pf  
Gabon| ga  
Gambia (the)| gm  
Georgia| ge  
Germany| de  
Ghana| gh  
Gibraltar| gi  
Greece| gr  
Greenland| gl  
Grenada| gd  
Guadeloupe| gp  
Guam| gu  
Guatemala| gt  
Guinea| gn  
Guinea-Bissau| gw  
Guernsey| gg  
Guyana| gy  
Haiti| ht  
Heard Island and McDonald Islands| hm  
Holy See (the)| va  
Honduras| hn  
Hungary| hu  
Iceland| is  
India| in  
Indonesia| id  
Iran (Islamic Republic of)| ir  
Iraq| iq  
Ireland| ie  
Israel| il  
Italy| it  
Jamaica| jm  
Japan| jp  
Jersey| je  
Jordan| jo  
Kazakhstan| kz  
Kenya| ke  
Kiribati| ki  
Korea (the Democratic People's Republic of)| kp  
Korea (the Republic of)| kr  
Kosovo| xk  
Kuwait| kw  
Kyrgyzstan| kg  
Lao People's Democratic Republic (the)| la  
Latvia| lv  
Lebanon| lb  
Lesotho| ls  
Liberia| lr  
Libya| ly  
Liechtenstein| li  
Lithuania| lt  
Luxembourg| lu  
Madagascar| mg  
Malawi| mw  
Malaysia| my  
Maldives| mv  
Mali| ml  
Malta| mt  
Marshall Islands (the)| mh  
Martinique| mq  
Mauritania| mr  
Mauritius| mu  
Mayotte| yt  
Mexico| mx  
Micronesia (Federated States of)| fm  
Moldova (the Republic of)| md  
Monaco| mc  
Mongolia| mn  
Montenegro| me  
Montserrat| ms  
Morocco| ma  
Mozambique| mz  
Myanmar| mm  
Namibia| na  
Nauru| nr  
Nepal| np  
Netherlands (the)| nl  
New Caledonia| nc  
New Zealand| nz  
Nicaragua| ni  
Niger (the)| ne  
Nigeria| ng  
Niue| nu  
Northern Cyprus| cy-2  
Norfolk Island| nf  
Northern Mariana Islands (the)| mp  
Norway| no  
Oman| om  
Pakistan| pk  
Palau| pw  
Palestine, State of| ps  
Panama| pa  
Papua New Guinea| pg  
Paraguay| py  
Peru| pe  
Philippines (the)| ph  
Pitcairn| pn  
Poland| pl  
Portugal| pt  
Pridnestrovian Moldavian Republic| pmr  
Puerto Rico| pr  
Qatar| qa  
Republic of North Macedonia| mk  
Romania| ro  
Russian Federation (the)| ru  
Rwanda| rw  
Réunion| re  
Saint Barthélemy| bl  
Saint Helena, Ascension and Tristan da Cunha| sh  
Saint Kitts and Nevis| kn  
Saint Lucia| lc  
Saint Martin (French part)| mf  
Saint Pierre and Miquelon| pm  
Saint Vincent and the Grenadines| vc  
Samoa| ws  
San Marino| sm  
Sao Tome and Principe| st  
Saudi Arabia| sa  
Senegal| sn  
Serbia| rs  
Seychelles| sc  
Sierra Leone| sl  
Singapore| sg  
Sint Maarten (Dutch part)| sx  
Slovakia| sk  
Slovenia| si  
Solomon Islands| sb  
Somalia| so  
Somaliland, Republic of| so-2  
South Africa| za  
South Georgia and the South Sandwich Islands| gs  
South Ossetia| so-3  
South Sudan| ss  
Spain| es  
Sri Lanka| lk  
Sudan (the)| sd  
Suriname| sr  
Svalbard and Jan Mayen| sj  
Sweden| se  
Switzerland| ch  
Syrian Arab Republic| sy  
Tajikistan| tj  
Tanzania, United Republic of| tz  
Thailand| th  
Timor-Leste| tl  
Togo| tg  
Tokelau| tk  
Tonga| to  
Trinidad and Tobago| tt  
Tunisia| tn  
Turkey| tr  
Turkmenistan| tm  
Turks and Caicos Islands (the)| tc  
Tuvalu| tv  
Uganda| ug  
Ukraine| ua  
United Arab Emirates (the)| ae  
United Kingdom of Great Britain and Northern Ireland (the)| gb  
United States Minor Outlying Islands (the)| um  
United States of America (the)| us  
Uruguay| uy  
Uzbekistan| uz  
Vanuatu| vu  
Venezuela (Bolivarian Republic of)| ve  
Viet Nam| vn  
Virgin Islands (British)| vg  
Virgin Islands (U.S.)| vi  
Wallis and Futuna| wf  
Western Sahara| eh  
Yemen| ye  
Zambia| zm  
Zimbabwe| zw  
Åland Islands| ax  
  
## Brazil Regulatory Codes

Code values for the `txnPurpose`, `counterpartyType` and `relationship` fields of the Brazil withdraw and deposit questionnaires. Send the code, not the description.

### Purpose of Transaction (txnPurpose)

The code list depends on the USD-equivalent transaction amount: up to and including USD 50,000, use Annex III; above USD 50,000, use Annex IV.

**Annex III (≤ USD 50,000):**

Code| Description  
---|---  
`12995`| Purchase or sale of goods  
`46002`| Computing and information services  
`46978`| Business services  
`46992`| Other services  
`37994`| Donation / no consideration  
`32999`| International travel  
`72980`| External credit — principal  
`72997`| External credit — interest  
`91992`| Others  
  
**Annex IV ( > USD 50,000):**

Code| Description  
---|---  
`12186`| Virtual assets (crypto is the object of the deal)  
`12108`| Export — advance receipt ≤360d  
`12115`| Export — advance receipt >360d  
`12122`| Export — after shipment ≤360d  
`12139`| Export — after shipment >360d  
`12407`| Import — advance payment ≤180d  
`12414`| Import — advance 181–360d  
`12421`| Import — advance >360d  
`12438`| Import — after delivery ≤180d  
`12445`| Import — after delivery 181–360d  
`12452`| Import — after delivery >360d  
`12029`| Back-to-back operations  
`12823`| Merchanting (no customs transit)  
`22301`| Freight on exports  
`22318`| Freight on imports  
`22325`| Charter with crew  
`22332`| Passenger tickets  
`22349`| Other transport income/expenses  
`27100`| Freight/transport insurance  
`27117`| Insurance/reinsurance — premium  
`27124`| Insurance/reinsurance — claim  
`32999`| International travel  
`37303`| Maintenance of residents (family)  
`37028`| Taxes  
`37310`| Social security contrib./benefits  
`37327`| Pension fund contrib./benefits  
`37334`| Donations and intl. cooperation  
`37217`| Patrimony (estate transfers)  
`37358`| Other unilateral transfers  
`47001`| Postal and courier services  
`47018`| Telecommunications  
`46002`| Computing and information services  
`46019`| Financial services  
`47063`| Research and development  
`46026`| Repairs, maintenance, tech. assistance  
`46033`| Agriculture, mining, waste treatment  
`47111`| Manufacturing services  
`46040`| Management and legal services  
`47173`| Audiovisual services  
`46057`| Engineering & other professional services  
`46105`| Construction  
`46112`| Trademarks/franchises — assignment  
`46129`| Patents/technology — assignment  
`46136`| Marks/patents/tech — right of use  
`47551`| Copyright licence — software  
`47568`| Copyright licence — other  
`47575`| Copyright assignment/use — software  
`47582`| Copyright assignment/use — other  
`47609`| Commissions on commercial transactions  
`46150`| Gaming and betting  
`46167`| Personal, cultural, health, education svcs  
`46198`| Government income and expenses  
`47908`| Salaries and compensation  
`46208`| Rental of real estate and equipment  
`47922`| Athletes' economic/federative rights  
`47939`| Carbon credits / emission rights  
`46215`| Purchase and sale of real estate  
`46222`| Intragroup reimbursements. If selected, `relationship` must be `40`.  
`46239`| Assignment of credits  
`46246`| Indemnities not insurance-related  
`52027`| Dividends — shares and funds  
`52106`| Interest on securities — in Brazil  
`52113`| Interest on securities — external  
`52144`| Premiums/discounts on securities  
`52429`| Interest — trade-related credit  
`52436`| Interest — other loans  
`52443`| Dividends — direct investment  
`52508`| Interest on deposits  
`67005`| Shares (investment abroad)  
`67043`| Investment funds (abroad)  
`67050`| Brazilian Depositary Receipts  
`67108`| Debt securities ≤360d  
`67115`| Debt securities >360d  
`67201`| Derivatives — premiums/adjustments  
`67218`| Derivatives — margins/collateral  
`67438`| Loans and financing ≤360d  
`67445`| Loans and financing >360d  
`67476`| Direct investment abroad — M&A  
`67483`| Direct investment abroad — other  
`67531`| own funds abroad  
`67971`| RERCT (regularisation regime)  
`67919`| International organisations capital  
`72007`| Shares in Brazil (non-resident)  
`72045`| Funds in Brazil (non-resident)  
`72090`| Depositary Receipts (DR)  
`72117`| Securities in Brazil  
`72124`| Securities external ≤360d  
`72131`| Securities external >360d  
`72241`| Derivatives — premiums (foreign cap.)  
`72210`| Derivatives — margins (foreign cap.)  
`72296`| Financial market — other  
`72423`| Loans ≤360d (foreign capital)  
`72430`| Loans >360d (foreign capital)  
`72447`| FDI into Brazil — M&A  
`72454`| FDI into Brazil — other  
`72533`| Deposits in Brazil — non-resident  
  
### Counterparty Type (counterpartyType)

Send the code as a string (e.g. `"03"`, not `3`). The accepted codes depend on the beneficiary type (`bnfType`, withdrawals) or originator type (`orgType`, deposits).

Code| Description| Individual| Corporate/Entity  
---|---|---|---  
`03`| Non-resident — individual| ✓| —  
`05`| Non-resident — non-financial company| ✓| ✓  
`53`| Bank / financial intermediary (incl. exchanges)| —| ✓  
`56`| Investment fund| —| ✓  
`58`| Insurer or reinsurer| —| ✓  
`59`| Pension fund| —| ✓  
`60`| Other financial company| —| ✓  
`71`| Non-profit (NGO)| ✓| ✓  
`78`| Foreign government| ✓| ✓  
`79`| Multilateral organisation| —| ✓  
  
### Relationship (relationship)

Code| Description  
---|---  
`40`| Companies of the same economic group  
`50`| All other cases  
  
Was this page helpful?

Last modified on November 12, 2026

[Error Codes](/en/docs/products/wallet/error-code)[Deposit Questionnaire Contents (for existing local entities)](/en/docs/products/wallet/travel-rule/deposit-questionnaire)

---

# 附录

## 姓名限制

姓名的字符串需要符合下列的正则表达式才会被接受.
    
    
    Code
    
    ^(?=.{1,})(?!.{100,})(?!.*([a-zA-Z])\1{2,})(?!.*[0-9!@#$%^&*()_=.~`<>/:;?€£¥₹₩¢₿+=÷]).*$

  * 字符串长度必须在1到50个字符之间（含1和50）。
  * 字符串中不能包含数字和指定的一系列特殊符号。
  * 字符串中不能有任何字母连续重复3次或以上。
  * 字符串可以包含字母（大小写均可）和其他未被排除的字符（比如空格、标点符号中未列出的符号等）。



## 国家（地区）ISO编码

> 您将无法使用表中未列出的ISO代码

国家（地区）| 编码  
---|---  
Afghanistan| af  
Albania| al  
Algeria| dz  
American Samoa| as  
Andorra| ad  
Angola| ao  
Anguilla| ai  
Antigua and Barbuda| ag  
Argentina| ar  
Armenia| am  
Aruba| aw  
Australia| au  
Austria| at  
Azerbaijan| az  
Bahamas (the)| bs  
Bahrain| bh  
Bangladesh| bd  
Barbados| bb  
Belarus| by  
Belgium| be  
Belize| bz  
Benin| bj  
Bermuda| bm  
Bhutan| bt  
Bolivia (Plurinational State of)| bo  
Bonaire, Sint Eustatius and Saba| bq  
Bosnia and Herzegovina| ba  
Botswana| bw  
Bouvet Island| bv  
Brazil| br  
British Indian Ocean Territory (the)| io  
Brunei Darussalam| bn  
Bulgaria| bg  
Burkina Faso| bf  
Burundi| bi  
Cabo Verde| cv  
Cambodia| kh  
Cameroon| cm  
Canada| ca  
Cayman Islands (the)| ky  
Central African Republic (the)| cf  
Chad| td  
Chile| cl  
China| cn  
Christmas Island| cx  
Cocos (Keeling) Islands (the)| cc  
Colombia| co  
Comoros (the)| km  
Congo (the Democratic Republic of the)| cd  
Congo (the)| cg  
Cook Islands (the)| ck  
Costa Rica| cr  
Croatia| hr  
Cuba| cu  
Curaçao| cw  
Cyprus| cy  
Czechia| cz  
Côte d'Ivoire| ci  
Denmark| dk  
Djibouti| dj  
Dominica| dm  
Dominican Republic (the)| do  
Ecuador| ec  
Egypt| eg  
El Salvador| sv  
Equatorial Guinea| gq  
Eritrea| er  
Estonia| ee  
Eswatini| sz  
Ethiopia| et  
Falkland Islands (the) [Malvinas]| fk  
Faroe Islands (the)| fo  
Fiji| fj  
Finland| fi  
France| fr  
French Guiana| gf  
French Polynesia| pf  
Gabon| ga  
Gambia (the)| gm  
Georgia| ge  
Germany| de  
Ghana| gh  
Gibraltar| gi  
Greece| gr  
Greenland| gl  
Grenada| gd  
Guadeloupe| gp  
Guam| gu  
Guatemala| gt  
Guinea| gn  
Guinea-Bissau| gw  
Guernsey| gg  
Guyana| gy  
Haiti| ht  
Heard Island and McDonald Islands| hm  
Holy See (the)| va  
Honduras| hn  
Hungary| hu  
Iceland| is  
India| in  
Indonesia| id  
Iran (Islamic Republic of)| ir  
Iraq| iq  
Ireland| ie  
Israel| il  
Italy| it  
Jamaica| jm  
Japan| jp  
Jersey| je  
Jordan| jo  
Kazakhstan| kz  
Kenya| ke  
Kiribati| ki  
Korea (the Democratic People's Republic of)| kp  
Korea (the Republic of)| kr  
Kosovo| xk  
Kuwait| kw  
Kyrgyzstan| kg  
Lao People's Democratic Republic (the)| la  
Latvia| lv  
Lebanon| lb  
Lesotho| ls  
Liberia| lr  
Libya| ly  
Liechtenstein| li  
Lithuania| lt  
Luxembourg| lu  
Madagascar| mg  
Malawi| mw  
Malaysia| my  
Maldives| mv  
Mali| ml  
Malta| mt  
Marshall Islands (the)| mh  
Martinique| mq  
Mauritania| mr  
Mauritius| mu  
Mayotte| yt  
Mexico| mx  
Micronesia (Federated States of)| fm  
Moldova (the Republic of)| md  
Monaco| mc  
Mongolia| mn  
Montenegro| me  
Montserrat| ms  
Morocco| ma  
Mozambique| mz  
Myanmar| mm  
Namibia| na  
Nauru| nr  
Nepal| np  
Netherlands (the)| nl  
New Caledonia| nc  
New Zealand| nz  
Nicaragua| ni  
Niger (the)| ne  
Nigeria| ng  
Niue| nu  
Northern Cyprus| cy-2  
Norfolk Island| nf  
Northern Mariana Islands (the)| mp  
Norway| no  
Oman| om  
Pakistan| pk  
Palau| pw  
Palestine, State of| ps  
Panama| pa  
Papua New Guinea| pg  
Paraguay| py  
Peru| pe  
Philippines (the)| ph  
Pitcairn| pn  
Poland| pl  
Portugal| pt  
Pridnestrovian Moldavian Republic| pmr  
Puerto Rico| pr  
Qatar| qa  
Republic of North Macedonia| mk  
Romania| ro  
Russian Federation (the)| ru  
Rwanda| rw  
Réunion| re  
Saint Barthélemy| bl  
Saint Helena, Ascension and Tristan da Cunha| sh  
Saint Kitts and Nevis| kn  
Saint Lucia| lc  
Saint Martin (French part)| mf  
Saint Pierre and Miquelon| pm  
Saint Vincent and the Grenadines| vc  
Samoa| ws  
San Marino| sm  
Sao Tome and Principe| st  
Saudi Arabia| sa  
Senegal| sn  
Serbia| rs  
Seychelles| sc  
Sierra Leone| sl  
Singapore| sg  
Sint Maarten (Dutch part)| sx  
Slovakia| sk  
Slovenia| si  
Solomon Islands| sb  
Somalia| so  
Somaliland, Republic of| so-2  
South Africa| za  
South Georgia and the South Sandwich Islands| gs  
South Ossetia| so-3  
South Sudan| ss  
Spain| es  
Sri Lanka| lk  
Sudan (the)| sd  
Suriname| sr  
Svalbard and Jan Mayen| sj  
Sweden| se  
Switzerland| ch  
Syrian Arab Republic| sy  
Tajikistan| tj  
Tanzania, United Republic of| tz  
Thailand| th  
Timor-Leste| tl  
Togo| tg  
Tokelau| tk  
Tonga| to  
Trinidad and Tobago| tt  
Tunisia| tn  
Turkey| tr  
Turkmenistan| tm  
Turks and Caicos Islands (the)| tc  
Tuvalu| tv  
Uganda| ug  
Ukraine| ua  
United Arab Emirates (the)| ae  
United Kingdom of Great Britain and Northern Ireland (the)| gb  
United States Minor Outlying Islands (the)| um  
United States of America (the)| us  
Uruguay| uy  
Uzbekistan| uz  
Vanuatu| vu  
Venezuela (Bolivarian Republic of)| ve  
Viet Nam| vn  
Virgin Islands (British)| vg  
Virgin Islands (U.S.)| vi  
Wallis and Futuna| wf  
Western Sahara| eh  
Yemen| ye  
Zambia| zm  
Zimbabwe| zw  
Åland Islands| ax  
  
## 巴西监管编码

巴西提币和充值问卷中 `txnPurpose`、`counterpartyType` 和 `relationship` 字段的编码取值。请传入编码，而非描述。

### 交易目的（txnPurpose）

可用编码取决于交易的 USD 等值金额：不超过 USD 50,000（含）使用 Annex III；超过 USD 50,000 使用 Annex IV。

**Annex III（≤ USD 50,000）：**

编码| 描述  
---|---  
`12995`| Purchase or sale of goods  
`46002`| Computing and information services  
`46978`| Business services  
`46992`| Other services  
`37994`| Donation / no consideration  
`32999`| International travel  
`72980`| External credit — principal  
`72997`| External credit — interest  
`91992`| Others  
  
**Annex IV（ > USD 50,000）：**

编码| 描述  
---|---  
`12186`| Virtual assets (crypto is the object of the deal)  
`12108`| Export — advance receipt ≤360d  
`12115`| Export — advance receipt >360d  
`12122`| Export — after shipment ≤360d  
`12139`| Export — after shipment >360d  
`12407`| Import — advance payment ≤180d  
`12414`| Import — advance 181–360d  
`12421`| Import — advance >360d  
`12438`| Import — after delivery ≤180d  
`12445`| Import — after delivery 181–360d  
`12452`| Import — after delivery >360d  
`12029`| Back-to-back operations  
`12823`| Merchanting (no customs transit)  
`22301`| Freight on exports  
`22318`| Freight on imports  
`22325`| Charter with crew  
`22332`| Passenger tickets  
`22349`| Other transport income/expenses  
`27100`| Freight/transport insurance  
`27117`| Insurance/reinsurance — premium  
`27124`| Insurance/reinsurance — claim  
`32999`| International travel  
`37303`| Maintenance of residents (family)  
`37028`| Taxes  
`37310`| Social security contrib./benefits  
`37327`| Pension fund contrib./benefits  
`37334`| Donations and intl. cooperation  
`37217`| Patrimony (estate transfers)  
`37358`| Other unilateral transfers  
`47001`| Postal and courier services  
`47018`| Telecommunications  
`46002`| Computing and information services  
`46019`| Financial services  
`47063`| Research and development  
`46026`| Repairs, maintenance, tech. assistance  
`46033`| Agriculture, mining, waste treatment  
`47111`| Manufacturing services  
`46040`| Management and legal services  
`47173`| Audiovisual services  
`46057`| Engineering & other professional services  
`46105`| Construction  
`46112`| Trademarks/franchises — assignment  
`46129`| Patents/technology — assignment  
`46136`| Marks/patents/tech — right of use  
`47551`| Copyright licence — software  
`47568`| Copyright licence — other  
`47575`| Copyright assignment/use — software  
`47582`| Copyright assignment/use — other  
`47609`| Commissions on commercial transactions  
`46150`| Gaming and betting  
`46167`| Personal, cultural, health, education svcs  
`46198`| Government income and expenses  
`47908`| Salaries and compensation  
`46208`| Rental of real estate and equipment  
`47922`| Athletes' economic/federative rights  
`47939`| Carbon credits / emission rights  
`46215`| Purchase and sale of real estate  
`46222`| Intragroup reimbursements。选择此编码时，`relationship` 必须为 `40`。  
`46239`| Assignment of credits  
`46246`| Indemnities not insurance-related  
`52027`| Dividends — shares and funds  
`52106`| Interest on securities — in Brazil  
`52113`| Interest on securities — external  
`52144`| Premiums/discounts on securities  
`52429`| Interest — trade-related credit  
`52436`| Interest — other loans  
`52443`| Dividends — direct investment  
`52508`| Interest on deposits  
`67005`| Shares (investment abroad)  
`67043`| Investment funds (abroad)  
`67050`| Brazilian Depositary Receipts  
`67108`| Debt securities ≤360d  
`67115`| Debt securities >360d  
`67201`| Derivatives — premiums/adjustments  
`67218`| Derivatives — margins/collateral  
`67438`| Loans and financing ≤360d  
`67445`| Loans and financing >360d  
`67476`| Direct investment abroad — M&A  
`67483`| Direct investment abroad — other  
`67531`| own funds abroad  
`67971`| RERCT (regularisation regime)  
`67919`| International organisations capital  
`72007`| Shares in Brazil (non-resident)  
`72045`| Funds in Brazil (non-resident)  
`72090`| Depositary Receipts (DR)  
`72117`| Securities in Brazil  
`72124`| Securities external ≤360d  
`72131`| Securities external >360d  
`72241`| Derivatives — premiums (foreign cap.)  
`72210`| Derivatives — margins (foreign cap.)  
`72296`| Financial market — other  
`72423`| Loans ≤360d (foreign capital)  
`72430`| Loans >360d (foreign capital)  
`72447`| FDI into Brazil — M&A  
`72454`| FDI into Brazil — other  
`72533`| Deposits in Brazil — non-resident  
  
### 对手方类型（counterpartyType）

编码以字符串传入（如 `"03"`，而非 `3`）。可接受的编码取决于收款人类型（提币为 `bnfType`）或发款人类型（充值为 `orgType`）。

编码| 描述| 个人| 公司/实体  
---|---|---|---  
`03`| Non-resident — individual| ✓| —  
`05`| Non-resident — non-financial company| ✓| ✓  
`53`| Bank / financial intermediary (incl. exchanges)| —| ✓  
`56`| Investment fund| —| ✓  
`58`| Insurer or reinsurer| —| ✓  
`59`| Pension fund| —| ✓  
`60`| Other financial company| —| ✓  
`71`| Non-profit (NGO)| ✓| ✓  
`78`| Foreign government| ✓| ✓  
`79`| Multilateral organisation| —| ✓  
  
### 关系（relationship）

编码| 描述  
---|---  
`40`| Companies of the same economic group  
`50`| All other cases  
  
此页面是否有帮助？

Last modified on November 12, 2026

[错误代码](/zh-CN/docs/products/wallet/error-code)[充值问卷内容(针对需要旅行规则的本地站)](/zh-CN/docs/products/wallet/travel-rule/deposit-questionnaire)