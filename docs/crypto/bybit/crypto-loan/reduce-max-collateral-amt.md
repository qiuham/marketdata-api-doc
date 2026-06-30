---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/crypto-loan/reduce-max-collateral-amt
api_type: REST
updated_at: 2026-06-30 19:25:25.150404
---

# Demo Trading Service

## Introduction

Bybit v5 Open API supports demo trading account, but please note **not** every API is available for demo trading account because demo trading service is mainly for trading experience purpose, so that it does not have a complete function compared with the real trading service.

## Create API Key

  1. You need to log in to your [mainnet](https://www.bybit.com/) account;
  2. Switch to `Demo Trading`, please note it is an independent account for demo trading only, and it has its own user ID;
  3. Hover the mouse on user avatar, then click "API" to generate api key and secret;



## Usage rules

  * Basic trading rules are the same as real trading
  * Orders generated in demo trading keep **7 days**
  * Default rate limit, not upgradable



## Domain

**Mainnet Demo Trading URL:**  
Rest API: `https://api-demo.bybit.com`  
Websocket: `wss://stream-demo.bybit.com` (note that this only supports the private streams; public data is identical to that found on mainnet with `wss://stream.bybit.com`; WS Trade is not supported)

## Tips

  * Please note that demo trading is an isolated module. When you create the key from demo trading, please use above domain to connect.
  * By the way, it is meaningless to use demo trading service in the [testnet](https://testnet.bybit.com) website, so do not create a key from Testnet demo trading.



## Available API List

Cateogory| Title| Endpoint  
---|---|---  
Market| All| all endpoints  
Trade| [Place Order](/docs/v5/order/create-order)| /v5/order/create  
[Amend Order](/docs/v5/order/amend-order)| /v5/order/amend  
[Cancel order](/docs/v5/order/cancel-order)| /v5/order/cancel  
[Get Open Orders](/docs/v5/order/open-order)| /v5/order/realtime  
[Cancel All Orders](/docs/v5/order/cancel-all)| /v5/order/cancel-all  
[Get Order History](/docs/v5/order/order-list)| /v5/order/history  
[Get Trade History](/docs/v5/order/execution)| /v5/execution/list  
[Batch Place Order](/docs/v5/order/batch-place)| /v5/order/create-batch (linear,option)  
[Batch Amend Order](/docs/v5/order/batch-amend)| /v5/order/amend-batch (linear,option)  
[Batch Cancel Order](/docs/v5/order/batch-cancel)| /v5/order/cancel-batch (linear,option)  
Position| [Get Position Info](/docs/v5/position)| /v5/position/list  
[Set Leverage](/docs/v5/position/leverage)| /v5/position/set-leverage  
[Switch Position Mode](/docs/v5/position/position-mode)| /v5/position/switch-mode  
[Set Trading Stop](/docs/v5/position/trading-stop)| /v5/position/trading-stop  
[Set Auto Add Margin](/docs/v5/position/auto-add-margin)| /v5/position/set-auto-add-margin  
[Add Or Reduce Margin](/docs/v5/position/manual-add-margin)| /v5/position/add-margin  
[Get Closed PnL](/docs/v5/position/close-pnl)| /v5/position/closed-pnl  
Account| [Get Wallet Balance](/docs/v5/account/wallet-balance)| /v5/account/wallet-balance  
[Get Borrow History](/docs/v5/account/borrow-history)| /v5/account/borrow-history  
[Set Collateral Coin](/docs/v5/account/set-collateral)| /v5/account/set-collateral-switch  
[Get Collateral Info](/docs/v5/account/collateral-info)| /v5/account/collateral-info  
[Get Coin Greeks](/docs/v5/account/coin-greeks)| /v5/asset/coin-greeks  
[Get Account Info](/docs/v5/account/account-info)| /v5/account/info  
[Get Transaction Log](/docs/v5/account/transaction-log)| /v5/account/transaction-log  
[Set Margin Mode](/docs/v5/account/set-margin-mode)| /v5/account/set-margin-mode  
[Set Spot Hedging](/docs/v5/account/set-spot-hedge)| /v5/account/set-hedging-mode  
Asset| [Get Delivery Record](/docs/v5/asset/delivery)| /v5/asset/delivery-record  
[Get USDC Session Settlement](/docs/v5/asset/settlement)| /v5/asset/settlement-record  
Spot Margin Trade| [Toggle Margin Trade](/docs/v5/spot-margin-uta/switch-mode)| /v5/spot-margin-trade/switch-mode  
[Set Leverage](/docs/v5/spot-margin-uta/set-leverage)| /v5/spot-margin-trade/set-leverage  
[Get Status And Leverage](/docs/v5/spot-margin-uta/status)| /v5/spot-margin-uta/status  
[WS Private](/docs/v5/websocket/private/position)| order,execution,position,wallet,greeks| /v5/private  
  
### Request Demo Trading Funds

> API rate limit: 1 req per minute

#### HTTP Request

POST`/v5/account/demo-apply-money`

#### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
adjustType| false| integer| `0`(default): add demo funds; `1`: reduce demo funds  
utaDemoApplyMoney| false| array|   
> coin| false| string| Applied coin, supports `BTC`, `ETH`, `USDT`, `USDC`  
> amountStr| false| string| Applied amount, the max applied amount in each request 

  * `BTC`: "15"
  * `ETH`: "200"
  * `USDT`: "100000"
  * `USDC`: "100000"

  
  
#### Request Example
    
    
    POST /v5/account/demo-apply-money HTTP/1.1  
    Host: api-demo.bybit.com  
    X-BAPI-SIGN: XXXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1711420489915  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "adjustType": 0,  
        "utaDemoApplyMoney": [  
            {  
                "coin": "USDT",  
                "amountStr": "109"  
            },  
            {  
                "coin": "ETH",  
                "amountStr": "1"  
            }  
        ]  
    }  
    

### Create Demo Account

> API rate limit: 5 req per second  
>  Permission: AccountTransfer, SubMemberTransfer or SubMemberTransferList

info

  * Use product main account or sub account key to call the interface, the domain needs to be "api.bybit.com"
  * If demo account is existing, this POST request will return the existing UID directly
  * If using main account key to call, then the generated demo account is under the main account
  * If using sub account key to call, then the generated demo account is under the sub account



#### HTTP Request

POST`/v5/user/create-demo-member`

#### Request Parameters

None

#### Response Parameters

Parameter| Type| Comments  
---|---|---  
subMemberId| string| Demo account ID  
  
#### Request Example
    
    
    POST /v5/user/create-demo-member HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1728460942776  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 2  
      
    {}  
    

### [Create Demo Account API Key](/docs/v5/user/create-subuid-apikey)

info

  * Input generated demo account uid
  * Use **production main account key** to call the interface, the domain needs to be **"api.bybit.com"**



### [Update Demo Account API Key](/docs/v5/user/modify-sub-apikey)

info

  * Use **production main account key** to call the interface, the domain needs to be **"api.bybit.com"**



### [Get Demo Account API Key Info](/docs/v5/user/apikey-info)

info

  * Use **accordingly demo account key** to call the interface, the domain needs to be **"api-demo.bybit.com"**



### [Delete Demo Account API Key](/docs/v5/user/rm-sub-apikey)

info

  * Use **production main account key** to call the interface, the domain needs to be **"api.bybit.com"**

---

# 模擬交易

## 概覽

Bybit v5 Open API支持模擬交易帳戶, 但是由於模擬交易的主要目的是為了體驗基礎交易功能, 僅支持有限的功能, 所以部分接口不支持使用。

## 創建API Key

  1. 您需要登入到[Bybit 主網](https://www.bybit.com/)帳戶;
  2. 切換到`模擬交易`, 注意: 模擬交易擁有自己獨立的帳戶ID;
  3. 懸停鼠標在用戶頭像上, 然後點擊"API" 來創建key和secret;



## 使用規則

  * 基礎交易規則和實盤保持一致
  * 模擬盤的訂單僅保留**7天**
  * 默認請求頻率, 無法提頻



## 域名

**主網模擬盤:**  
Rest API: `https://api-demo.bybit.com`  
Websocket : `wss://stream-demo.bybit.com` (請注意模擬交易僅支持私有頻道; 公共頻道請使用 `wss://stream.bybit.com`; WS下單服務不支持)

## 小建議

  * 請注意模擬交易是獨立模塊, 當創建了模擬交易的api key後, 請使用以上域名進行連接
  * 順便說下, 在[測試網](https://testnet.bybit.com)使用模擬交易服務是無意義的, 因為二者都是沙盒環境, 若要使用模擬交易, 請至[主網](https://www.bybit.com)生成模擬交易的api key



## 可用接口列表

目錄| 接口名| 路由  
---|---|---  
公有行情| 所有| 所有接口  
交易| [創建委託單](/docs/zh-TW/v5/order/create-order)| /v5/order/create  
[修改委託單](/docs/zh-TW/v5/order/amend-order)| /v5/order/amend  
[撤銷委託單](/docs/zh-TW/v5/order/cancel-order)| /v5/order/cancel  
[查詢實時委託段](/docs/zh-TW/v5/order/open-order)| /v5/order/realtime  
[撤銷所有訂單](/docs/zh-TW/v5/order/cancel-all)| /v5/order/cancel-all  
[查詢歷史訂單](/docs/zh-TW/v5/order/order-list)| /v5/order/history  
[查詢成交紀錄](/docs/zh-TW/v5/order/execution)| /v5/execution/list  
[批量創建委託單](/docs/zh-TW/v5/order/batch-place)| /v5/order/create-batch (期貨/期權)  
[批量修改委託單](/docs/zh-TW/v5/order/batch-amend)| /v5/order/amend-batch (期貨/期權)  
[批量撤銷委託單](/docs/zh-TW/v5/order/batch-cancel)| /v5/order/cancel-batch (期貨/期權)  
持倉| [查詢持倉](/docs/zh-TW/v5/position)| /v5/position/list  
[設置槓桿](/docs/zh-TW/v5/position/leverage)| /v5/position/set-leverage  
[切換持倉模式](/docs/zh-TW/v5/position/position-mode)| /v5/position/switch-mode  
[設置止盈止損](/docs/zh-TW/v5/position/trading-stop)| /v5/position/trading-stop  
[設置自動追加保證金](/docs/zh-TW/v5/position/auto-add-margin)| /v5/position/set-auto-add-margin  
[手動增加或減少保證金](/docs/zh-TW/v5/position/manual-add-margin)| /v5/position/add-margin  
[查詢平常盈虧](/docs/zh-TW/v5/position/close-pnl)| /v5/position/closed-pnl  
帳戶| [查詢錢包餘額](/docs/zh-TW/v5/account/wallet-balance)| /v5/account/wallet-balance  
[查詢利息紀錄](/docs/zh-TW/v5/account/borrow-history)| /v5/account/borrow-history  
[設置抵押品幣種](/docs/zh-TW/v5/account/set-collateral)| /v5/account/set-collateral-switch  
[查詢抵押品信息](/docs/zh-TW/v5/account/collateral-info)| /v5/account/collateral-info  
[查詢Greeks信息](/docs/zh-TW/v5/account/coin-greeks)| /v5/asset/coin-greeks  
[查詢帳戶配置](/docs/zh-TW/v5/account/account-info)| /v5/account/info  
[查詢交易日誌](/docs/zh-TW/v5/account/transaction-log)| /v5/account/transaction-log  
[設置保證金模式](/docs/zh-TW/v5/account/set-margin-mode)| /v5/account/set-margin-mode  
[設置現貨對衝](/docs/zh-TW/v5/account/set-spot-hedge)| /v5/account/set-hedging-mode  
資產| [查詢交割紀錄](/docs/zh-TW/v5/asset/delivery)| /v5/asset/delivery-record  
[查詢USDC結算紀錄](/docs/zh-TW/v5/asset/settlement)| /v5/asset/settlement-record  
全倉槓桿| [全倉槓桿開關](/docs/zh-TW/v5/spot-margin-uta/switch-mode)| /v5/spot-margin-trade/switch-mode  
[全倉槓桿設置](/docs/zh-TW/v5/spot-margin-uta/set-leverage)| /v5/spot-margin-trade/set-leverage  
[查詢開關狀態和倍數](/docs/zh-TW/v5/spot-margin-uta/status)| /v5/spot-margin-uta/status  
[WS私有推送](/docs/zh-TW/v5/websocket/private/position)| order,execution,position,wallet,greeks| /v5/private  
  
### 獲取模擬資金接口

> API頻率: 每分鐘1次

#### HTTP請求

POST`/v5/account/demo-apply-money`

#### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
adjustType| false| integer| `0`(默認): 增加模擬資金; `1`: 減少模擬資金  
utaDemoApplyMoney| false| array|   
> coin| false| string| 申請的幣種, 支持 `BTC`, `ETH`, `USDT`, `USDC`  
> amountStr| false| string| 申請的金額, 每次請求最多支持申請如下金額 

  * `BTC`: "15"
  * `ETH`: "200"
  * `USDT`: "100000"
  * `USDC`: "100000"

  
  
#### 請求示例
    
    
    POST /v5/account/demo-apply-money HTTP/1.1  
    Host: api-demo.bybit.com  
    X-BAPI-SIGN: XXXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1711420489915  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "adjustType": 0,  
        "utaDemoApplyMoney": [  
            {  
                "coin": "USDT",  
                "amountStr": "109"  
            },  
            {  
                "coin": "ETH",  
                "amountStr": "1"  
            }  
        ]  
    }  
    

### 創建模擬交易帳戶

> API 頻率: 5次/秒  
>  權限: 帳戶劃轉, 母子帳戶劃轉

信息

  * 使用生產環境的母子帳戶調用該接口, 域名需要是"api.bybit.com"
  * 如果模擬帳戶已經存在, 這個POST接口直接返回存在的模擬帳戶UID
  * 如果使用的母帳戶key調接口, 則創建的模擬帳戶存在於該母帳戶下面
  * 如果使用的子帳戶key調接口, 則創建的模擬帳戶存在於該子帳戶下面



#### HTTP 請求

POST`/v5/user/create-demo-member`

#### 請求參數

無

#### 響應參數

參數| 類型| 說明  
---|---|---  
subMemberId| string| 模擬帳戶UID  
  
#### 請求實例
    
    
    POST /v5/user/create-demo-member HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1728460942776  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 2  
      
    {}  
    

### [創建模擬帳戶API Key](/docs/zh-TW/v5/user/create-subuid-apikey)

信息

  * 參數填寫模擬帳戶UID
  * 使用**生產環境母帳戶** 調用接口, 域名需要是**"api.bybit.com"**



### [更新模擬帳戶API Key](/docs/zh-TW/v5/user/modify-sub-apikey)

信息

  * 使用**生產環境母帳戶** 調用接口, 域名需要是**"api.bybit.com"**



### [查詢模擬帳戶API Key信息](/docs/zh-TW/v5/user/apikey-info)

信息

  * 使用**對應的模擬帳戶** 調用接口, 域名需要是**"api-demo.bybit.com"**



### [刪除模擬帳戶API Key](/docs/zh-TW/v5/user/rm-sub-apikey)

信息

  * 使用**生產環境母帳戶** 調用接口, 域名需要是**"api.bybit.com"**