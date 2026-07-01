---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/asset/transfer/transferable-coin
api_type: REST
updated_at: 2026-07-01 19:26:36.921102
---

# Withdraw

Withdraw assets from your Bybit account. You can make an off-chain transfer if the target wallet address is from Bybit. This means that no blockchain fee will be charged.

Note that, although the API rate limit for this endpoint is 5 req/s, there is also a secondary limit: you can only withdraw once every 10 seconds per chain/coin combination.

tip

  * Make sure you have whitelisted your wallet address [here](https://www.bybit.com/user/assets/money-address)
  * Request by the master UID's api key **only**



formula

**feeType=0:**

  * withdrawPercentageFee != 0: _handlingFee = inputAmount / (1 - withdrawPercentageFee) * withdrawPercentageFee + withdrawFee_
  * withdrawPercentageFee = 0: _handlingFee = withdrawFee_



**feeType=1:**

  * withdrawPercentageFee != 0: _handlingFee = withdrawFee + (inputAmount - withdrawFee) * withdrawPercentageFee_
  * withdrawPercentageFee = 0: _handlingFee = withdrawFee_



### HTTP Request

POST`/v5/asset/withdraw/create`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
coin| **true**|  string| Coin, uppercase only  
chain| false| string| Chain 

  * `forceChain`=0 or 1: this field is **required**
  * `forceChain`=2: this field can be null

  
address| **true**|  string| 

  * `forceChain`=0 or 1: fill wallet address, and make sure you add address in the [address book](https://www.bybit.com/user/assets/money-address) first. Please note that the address is case sensitive, so use the exact same address added in address book
  * `forceChain`=2: fill Bybit UID, and it can only be another Bybit **main** account UID. Make sure you add UID in the [address book](https://www.bybit.com/user/assets/money-address) first

  
tag| false| string| Tag 

  * **Required** if tag exists in the wallet address list.
  * **Note** : please do not set a tag/memo in the address book if the chain does not support tag

  
amount| **true**|  string| Withdraw amount  
timestamp| **true**|  integer| Current timestamp (ms). Used for preventing from withdraw replay  
forceChain| false| integer| Whether or not to force an on-chain withdrawal

  * `0`(default): If the address is parsed out to be an internal address, then internal transfer (**Bybit main account only**)
  * `1`: Force the withdrawal to occur on-chain
  * `2`: Use UID to withdraw

  
accountType| **true**|  string| Select the wallet to be withdrawn from 

  * `FUND`: Funding wallet
  * `UTA`: System transfers the funds to Funding wallet to withdraw
  * `EARN`: some coins may not support to be withdrawn via Earn account, please transfer it to Funding wallet then withdraw
  * `FUND,UTA,EARN`: For combo withdrawals, funds will be deducted from the Funding wallet first. If the balance is insufficient, the remaining amount will be deducted from the UTA wallet and Earn account.

  
feeType| false| integer| Handling fee option 

  * `0`(default): input amount is the actual amount received, so you have to calculate handling fee manually
  * `1`: input amount is not the actual amount you received, the system will help to deduct the handling fee automatically

  
requestId| false| string| Customised ID, globally unique, it is used for idempotent verification 

  * A combination of letters (case sensitive) and numbers, which can be pure letters or pure numbers and the length must be between 1 and 32 digits

  
transactionPurpose| false| string| Purpose of the withdrawal transaction, need at least 20 characters, **Required for Bybit Turkey site users**  
questionnaire| false| string| Travel Rule questionnaire info, JSON string, ≤16384 bytes. Supersedes `beneficiary` and `transactionPurpose` when both are present. **New integrations are always recommended to use this field to submit travel rule**. See [Questionnaire](/docs/v5/asset/withdraw/questionnaire) for field structure by compliance zone  
beneficiary| false| Object| Travel rule info. It is **required** for kyc/kyb=KOR (Korean), kyc=IND (India) users, and users who registered in [Bybit Turkey(TR)](https://www.bybit-tr.com/en-TR/), [Bybit Kazakhstan(KZ)](https://www.bybit.kz/kk-KAZ/), Bybit Indonesia (ID)  
---|---|---|---  
  
> beneficiaryTransactionPurpose| false| string| Purpose of the withdrawal transaction, **Required** when KR users withdraw funds to a company via Korean CODE channel  
> beneficiaryRepresentativeFirstName| false| string| First name of the beneficiary company's representative, **Required** when KR users withdraw funds to a company via Korean CODE channel  
> beneficiaryRepresentativeLastName| false| string| Last name of the beneficiary company's representative, **Required** when KR users withdraw funds to a company via Korean CODE channel  
> vaspEntityId| false| string| Receiver exchange entity Id. Please call this [endpoint](/docs/v5/asset/withdraw/vasp-list) to get this ID. 

  * **Required** param for Korean users
  * **Ignored by** TR, KZ users

  
> vaspEntityId | false | string | Receiver exchange entity Id. Please call this [endpoint](/docs/v5/asset/withdraw/vasp-list) to get this ID. 

  * **Required** param for Korean users
  * **Ignored by** TR, KZ users

  
> beneficiaryName | false | string | Receiver exchange user KYC name   
**Rules for Korean users** :

  * Please refer to target exchange kyc name
  * When vaspEntityId="others", this field can be null

**Rules for TR, KZ, kyc=IND users** : it is a **required** param, fill with individual name or company name  
> beneficiaryLegalType | false | string | Beneficiary legal type, `individual`(default), `company`

  * **Required** param for TR, KZ, kyc=IND users 
  * Korean users can ignore

  
> beneficiaryWalletType | false | string | Beneficiary wallet type, `0`: custodial/exchange wallet (default), `1`: non custodial/exchane wallet

  * **Required** param for TR, KZ, kyc=IND users
  * Korean users can ignore

  
> beneficiaryUnhostedWalletType | false | string | Beneficiary unhosted wallet type, `0`: Your own wallet, `1`: others' wallet 

  * **Required** param for TR, KZ, kyc=IND users when "beneficiaryWalletType=1"
  * Korean users can ignore

  
> beneficiaryPoiNumber | false | string | Beneficiary ducument number 

  * **Required** param for TR, KZ users
  * Korean users can ignore

  
> beneficiaryPoiType | false | string | Beneficiary ducument type 

  * **Required** param for TR, KZ users: ID card, Passport, driver license, residence permit, Business ID, etc
  * Korean users can ignore

  
> beneficiaryPoiIssuingCountry | false | string | Beneficiary ducument issuing country 

  * **Required** param for TR, KZ users: refer to [Alpha-3 country code](https://www.iban.com/country-codes)
  * Korean users can ignore

  
> beneficiaryPoiExpiredDate | false | string | Beneficiary ducument expiry date 

  * **Required** param for TR, KZ users: yyyy-mm-dd format, e.g., "1990-02-15"
  * Korean users can ignore

  
> beneficiaryAddressCountry | false | string | Beneficiary country 

  * **Required** param for UAE users only, e.g.,`IDN`

  
> beneficiaryAddressState | false | string | Beneficiary state 

  * **Required** param for UAE users only, e.g., "ABC"

  
> beneficiaryAddressCity | false | string | Beneficiary city 

  * **Required** param for UAE users only, e.g., "Jakarta"

  
> beneficiaryAddressBuilding | false | string | Beneficiary building address 

  * **Required** param for UAE users only

  
> beneficiaryAddressStreet | false | string | Beneficiary street address 

  * **Required** param for UAE users only

  
> beneficiaryAddressPostalCode | false | string | Beneficiary address post code 

  * **Required** param for UAE users only

  
> beneficiaryDateOfBirth | false | string | Beneficiary date of birth 

  * **Required** param for UAE users only

  
> beneficiaryPlaceOfBirth | false | string | Beneficiary birth place 

  * **Required** param for UAE users onl

  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
id| string| Withdrawal ID  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/asset/withdraw/create HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672196570254  
    X-BAPI-RECV-WINDOW: 5000  
    X-BAPI-SIGN: XXXXX  
    Content-Type: application/json  
      
    {  
        "coin": "USDT",  
        "chain": "ETH",  
        "address": "0x99ced129603abc771c0dabe935c326ff6c86645d",  
        "amount": "24",  
        "timestamp": 1672196561407,  
        "forceChain": 0,  
        "accountType": "FUND"  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.withdraw(  
        coin="USDT",  
        chain="ETH",  
        address="0x99ced129603abc771c0dabe935c326ff6c86645d",  
        amount="24",  
        timestamp=1672196561407,  
        forceChain=0,  
        accountType="FUND",  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .submitWithdrawal({  
        coin: 'USDT',  
        chain: 'ETH',  
        address: '0x99ced129603abc771c0dabe935c326ff6c86645d',  
        amount: '24',  
        timestamp: 1672196561407,  
        forceChain: 0,  
        accountType: 'FUND',  
      })  
      .then((response) => {  
        console.log(response);  
      })  
      .catch((error) => {  
        console.error(error);  
      });  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "id": "10195"  
        },  
        "retExtInfo": {},  
        "time": 1672196571239  
    }

---

# 提現

若目標地址是Bybit平台內部地址, 您可以實現內部平台轉帳

提示

  * 確保您已經將提現地址加入到[這裡](https://www.bybit.com/user/assets/money-address)
  * 僅支持**母帳號** 的API key



公式

**feeType=0:**

  * 若百分比手續費 != 0: _手續費 = 輸入金額 / (1 - 百分比手續費) * 百分比手續費 + 固定手續費_
  * 若百分比手續費 = 0: _手續費 = 固定手續費_



**feeType=1:**

  * 若百分比手續費 != 0: _手續費 = 固定手續費 + (輸入金額 - 固定手續費) * 百分比手續費_
  * 若百分比手續費 = 0: _手續費 = 固定手續費_



### HTTP 請求

POST`/v5/asset/withdraw/create`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
coin| **true**|  string| 幣種  
chain| false| string| 

  * 鏈名, 當`forceChain`=0 或者 1: 該字段**必填**
  * 當`forceChain`=2: 該字段可忽略

  
address| **true**|  string| 錢包地址或者Bybit UID 

  * 當`forceChain`=0 或者 1: 請填寫錢包地址, 確保將地址添加到了[網頁地址簿](https://www.bybit.com/user/assets/money-address)中, 注意大小寫，請使用和提幣地址簿中完全一樣的地址
  * 當`forceChain`=2: 僅支持填寫目標Bybit母帳戶UID, 確保將目標UID添加到了[網頁地址簿](https://www.bybit.com/user/assets/money-address)中

  
tag| false| string| 標籤 

  * 若添加地址時有填寫tag，則該字段**必傳**.
  * **注意** : 如果鏈不支持tag/memo，請移除地址簿中的tag/memo，然後調用接口時，也不要傳tag字段

  
amount| **true**|  string| 提現金額  
timestamp| **true**|  integer| 當前時間戳 (毫秒). 用於防止請求重放  
forceChain| false| integer| 是否強制走鏈

  * `0`(默認): 若提現地址解析後發現是平台內部地址，則自動轉為走內部平台轉帳**(僅識別Bybit母帳戶錢包地址)**
  * `1`: 強制走鏈
  * `2`: 使用Bybit UID轉帳

  
accountType| **true**|  string| 設置出金帳戶  
`FUND`: 資金錢包出金  
`SPOT`: 現貨錢包(僅限經典賬戶)  
`UTA`: 系統從Unified錢包劃轉到Funding錢包, 然後提現  
`EARN`: 系統從理財帳戶提幣, 有些幣種可能不支持, 請先劃轉到資金帳戶再發起提幣  
`FUND,UTA,EARN`: 多帳戶組合出金, 優先從資金帳戶扣款, 若資金不足, 再從Unified錢包和理財帳戶扣款  
feeType| false| integer| 手續費選項 

  * `0`(默認): 輸入金額即實際收到的金額, 所以您需要額外考慮手續費
  * `1`: 輸入金額不是實際收到的金額, 系統將會自動計算所需的手續費

  
requestId| false| string| 自定義ID, 全局唯一, 用於冪等校驗

  * 字母(區分大小寫)數字組合, 可以是純字母或者純數字, 長度在1-32字符之間

  
transactionPurpose| false| string| 提幣原因, 需填寫至少20個字符, **Bybit土耳其站點用戶必填**  
questionnaire| false| string| Travel Rule 問卷信息，JSON 字符串，最大 16384 字節。與舊版 `beneficiary`/`transactionPurpose` 同時存在時以本字段為準，**新接入用戶總是推薦使用該字段提交travel rule** 。詳見[問卷說明](/docs/zh-TW/v5/asset/withdraw/questionnaire)  
beneficiary| false| Object| 提現目標方基本信息, kyc/kyb=KOR (韓國), kyc=IND (印度) 用戶, 以及在[Bybit土耳其(TR)](https://www.bybit-tr.com/en-TR/), [Bybit哈薩克斯坦(KZ)](https://www.bybit.kz/kk-KAZ/), Bybit印尼 (ID)的註冊用戶  
---|---|---|---  
  
> beneficiaryTransactionPurpose| false| string| 出金目的, 當走韓國CODE渠道出金到公司戶時**必傳**  
> beneficiaryRepresentativeFirstName| false| string| 受益公司代表人的"名", 當走韓國CODE渠道出金到公司戶時**必傳**  
> beneficiaryRepresentativeLastName| false| string| 受益公司代表人的"姓", 當走韓國CODE渠道出金到公司戶時**必傳**  
> vaspEntityId | **true**|  string | 接收方交易所id. 請調用該[接口](/docs/zh-TW/v5/asset/withdraw/vasp-list)來查詢對應的id  
> beneficiaryName | false | string | 接收方交易所用戶kyc姓名, 比如`John Wilson` 或者 `Wilson John` 

  * 請依據目標交易所kyc姓名
  * 僅當vaspEntityId="others"時, 該字段可不傳

  
> beneficiaryLegalType | false | string | 受益人法律類型, `individual`(默認), `company` 

  * TR和KZ及kyc為印度用戶需要傳入參數
  * 韓國用戶可忽略

  
> beneficiaryWalletType | false | string | 受益人錢包類型, `0`: 托管錢包 (默認), `1`: 非托管錢包 

  * TR和KZ及kyc為印度用戶需要傳入參數
  * 韓國用戶可忽略

  
> beneficiaryUnhostedWalletType | false | string | 受益人未托管錢包類型, `0`: 私有錢包, `1`: 其他類型錢包 

  * TR和KZ及kyc為印度用戶需要傳入參數
  * 韓國用戶可忽略

  
> beneficiaryPoiNumber | false | string | 受益人POI號碼 

  * TR和KZ用戶需要傳入參數
  * 韓國用戶可忽略

  
> beneficiaryPoiType | false | string | 受益人POI簽發類型 

  * TR和KZ用戶需要傳入: ID card, Passport, driver license, residence permit, Business ID...
  * 韓國用戶可忽略

  
> beneficiaryPoiIssuingCountry | false | string | 受益人POI簽發國家 

  * TR和KZ用戶需要傳入: 請參考 [Alpha-3 country code](https://www.iban.com/country-codes)
  * 韓國用戶可忽略

  
> beneficiaryPoiExpiredDate | false | string | 受益人POI到期日 

  * TR和KZ用戶需要傳入: yyyy-mm-dd 格式, e.g., "1990-02-15"
  * 韓國用戶可忽略

  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
id| string| 提現Id  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/asset/withdraw/create HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672196570254  
    X-BAPI-RECV-WINDOW: 5000  
    X-BAPI-SIGN: XXXXX  
    Content-Type: application/json  
      
    {  
        "coin": "USDT",  
        "chain": "ETH",  
        "address": "0x99ced129603abc771c0dabe935c326ff6c86645d",  
        "amount": "24",  
        "timestamp": 1672196561407,  
        "forceChain": 0,  
        "accountType": "FUND"  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.withdraw(  
        coin="USDT",  
        chain="ETH",  
        address="0x99ced129603abc771c0dabe935c326ff6c86645d",  
        amount="24",  
        timestamp=1672196561407,  
        forceChain=0,  
        accountType="FUND",  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .submitWithdrawal({  
        coin: 'USDT',  
        chain: 'ETH',  
        address: '0x99ced129603abc771c0dabe935c326ff6c86645d',  
        amount: '24',  
        timestamp: 1672196561407,  
        forceChain: 0,  
        accountType: 'FUND',  
      })  
      .then((response) => {  
        console.log(response);  
      })  
      .catch((error) => {  
        console.error(error);  
      });  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "id": "10195"  
        },  
        "retExtInfo": {},  
        "time": 1672196571239  
    }