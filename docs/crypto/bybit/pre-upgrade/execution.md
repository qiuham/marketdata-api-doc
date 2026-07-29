---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/pre-upgrade/execution
api_type: REST
updated_at: 2026-07-29 18:52:29.548607
---

# Rate Limit Rules

## IP Limit

### HTTP IP limit

You are allowed to send **600 requests within a 5-second window per IP** by default. This limit applies to all traffic directed to `api.bybit.com`, `api.bybick.com`, and local site hostnames such as `api.bybit.kz`. If you encounter the error **"403, access too frequent"** , it indicates that your IP has exceeded the allowed request frequency. In this case, you should terminate all HTTP sessions and wait for at least 10 minutes. The ban will be lifted automatically.

We do not recommend running your application at the very edge of these limits in case abnormal network activity results in an unexpected violation.

### Websocket IP limit

  * Do not establish more than 500 connections within a 5-minute window. This limit applies to all connections directed to `stream.bybit.com` as well as local site hostnames such as `stream.bybit.kz`.
  * Do not frequently connect and disconnect the connection
  * Do not establish more than 1,000 connections per IP for market data. The connection limits are counted separately for Spot, Linear, Inverse, and Options markets



## API Rate Limit

caution

If you receive `"retCode": 10006, "retMsg": "Too many visits!"` in the JSON response, you have hit the API rate limit.

The API rate limit is based on the **rolling time window per second and UID**. In other words, it is per second per UID. Every request to the API returns response header shown in the code panel:

  * `X-Bapi-Limit-Status` \- your remaining requests for current endpoint
  * `X-Bapi-Limit` \- your current limit for current endpoint
  * `X-Bapi-Limit-Reset-Timestamp` \- the timestamp indicating when your request limit resets if you have exceeded your rate_limit. Otherwise, this is just the current timestamp (it may not exactly match `timeNow`).



> Http Response Header Example
    
    
    ▶Response Headers  
    Content-Type: application/json; charset=utf-8  
    Content-Length: 141  
    X-Bapi-Limit: 10  
    X-Bapi-Limit-Status: 9  
    X-Bapi-Limit-Reset-Timestamp: 1672738134824  
    

### API Rate Limit Table

#### Trade

Method| Path| UTA2.0 Pro| upgradable  
---|---|---|---  
inverse| linear| option| spot  
POST| /v5/order/create| 10/s| 10/s| 20/s| Y  
/v5/order/amend| 10/s| 10/s| 10/s| Y  
/v5/order/cancel| 10/s| 10/s| 20/s| Y  
/v5/order/cancel-all| 10/s| 1/s| 20/s| Y  
/v5/order/create-batch| 10/s| 10/s| 20/s| Y  
/v5/order/amend-batch| 10/s| 10/s| 20/s| Y  
/v5/order/cancel-batch| 10/s| 10/s| 20/s| Y  
/v5/order/disconnected-cancel-all| 5/s| N  
/v5/order/pre-check| 10/s| 10/s| 20/s| Y  
GET| /v5/order/realtime| 50/s| N  
/v5/order/history| 50/s| N  
/v5/execution/list| 50/s| N  
/v5/order/spot-borrow-check| -| 50/s| N  
POST| /v5/fcombobot/getlimit| 10/s| -| -| N  
/v5/fcombobot/create| 10/s| -| -| N  
/v5/fcombobot/close| 10/s| -| -| N  
/v5/fcombobot/detail| 10/s| -| -| N  
/v5/fgridbot/validate| 10/s| -| -| N  
/v5/fgridbot/create| 10/s| -| -| N  
/v5/fgridbot/close| 10/s| -| -| N  
/v5/fgridbot/detail| 10/s| -| -| N  
/v5/fmartingalebot/getlimit| 10/s| -| -| N  
/v5/fmartingalebot/create| 100/s| -| -| N  
/v5/fmartingalebot/close| 10/s| -| -| N  
/v5/fmartingalebot/detail| 10/s| -| -| N  
/v5/grid/validate-input| -| 100/s| N  
/v5/grid/create-grid| -| 3/s| N  
/v5/grid/close-grid| -| 3/s| N  
/v5/grid/query-grid-detail| -| 10/s| N  
/v5/dca/create-bot| -| 3/s| N  
/v5/dca/close-bot| -| 3/s| N  
/v5/strategy/create| 100/s| -| 100/s| N  
GET| /v5/strategy/list| 200/s| -| 200/s| N  
/v5/strategy/order-list| 200/s| -| 200/s| N  
POST| /v5/strategy/stop| 100/s| -| 100/s| N  
  
#### Position

Method| Path| UTA2.0 Pro| upgradable  
---|---|---|---  
inverse| linear| option| spot  
GET| /v5/position/list| 50/s| -| N  
/v5/position/closed-pnl| 50/s| -| -| N  
/v5/position/get-closed-positions| -| -| 50/s| -| N  
/v5/position/move-history| 10/s| N  
POST| /v5/position/set-leverage| 10/s| -| -| N  
/v5/position/switch-mode| -| 10/s| -| -| N  
/v5/position/trading-stop| 10/s| -| N  
/v5/position/set-auto-add-margin| -| 10/s| -| -| N  
/v5/position/add-margin| 10/s| -| -| N  
/v5/position/confirm-pending-mmr| 10/s| -| -| N  
/v5/position/move-positions| 10/s| N  
  
#### Account

Method| Path| | Limit| upgradable  
---|---|---|---|---  
GET| /v5/account/wallet-balance| accountType=UNIFIED| 50/s| N  
/v5/account/withdrawal| | 50/s| N  
/v5/account/borrow-history| | 50/s| N  
/v5/account/borrow| | 1/s| N  
/v5/account/repay| | 1/s| N  
/v5/account/no-convert-repay| | 1/s| N  
/v5/account/collateral-info| | 50/s| N  
/v5/asset/coin-greeks| | 50/s| N  
/v5/account/transaction-log| accountType=UNIFIED| 25/s| N  
/v5/account/fee-rate| | 5/s| N  
/v5/account/info| | 50/s| N  
/v5/account/instruments-info| | 10/s| N  
/v5/account/mmp-state| | -| N  
/v5/account/option-asset-info| | -| N  
/v5/account/pay-info| | 50/s| N  
/v5/account/query-dcp-info| | 5/s| N  
/v5/account/smp-group| | 5/s| N  
/v5/account/trade-info-for-analysis| | 50/s| N  
/v5/account/user-setting-config| | 50/s| N  
POST| /v5/account/mmp-modify| | 5/s| N  
/v5/account/mmp-reset| | 5/s| N  
/v5/account/quick-repayment| | 1/s| N  
/v5/account/set-collateral-switch| | -| N  
/v5/account/set-collateral-switch-batch| | 5/s| N  
/v5/account/set-delta-mode| | -| N  
/v5/account/set-hedging-mode| | -| N  
/v5/account/set-limit-px-action| | 10/s| N  
/v5/account/set-margin-mode| | 5/s| N  
/v5/account/upgrade-to-uta| | 1/s| N  
  
#### Asset

Method| Path| Limit| upgradable  
---|---|---|---  
GET| /v5/asset/transfer/query-asset-info| 60 req/min| N  
/v5/asset/transfer/query-transfer-coin-list| 60 req/min| N  
/v5/asset/transfer/query-inter-transfer-list| 60 req/min| N  
/v5/asset/transfer/query-sub-member-list| 60 req/min| N  
/v5/asset/transfer/query-universal-transfer-list| 5 req/s| N  
/v5/asset/transfer/query-account-coins-balance| 5 req/s| N  
/v5/asset/transfer/query-account-coin-balance| 450 req/s| N  
/v5/asset/asset-overview| 50 req/s| N  
/v5/asset/withdraw/withdrawable-amount| 300 req/s| N  
/v5/asset/deposit/query-record| 100 req/min| N  
/v5/asset/deposit/query-sub-member-record| 300 req/min| N  
/v5/asset/deposit/query-address| 300 req/min| N  
/v5/asset/deposit/query-sub-member-address| 300 req/min| N  
/v5/asset/withdraw/query-record| 300 req/min| N  
/v5/asset/coin/query-info| 5 req/s| N  
/v5/asset/exchange/order-record| 600 req/min| N  
/v5/asset/exchange/query-coin-list| 30 req/s| N  
/v5/asset/covert/small-balance-history| 5 req/s| N  
/v5/asset/covert/small-balance-list| 10 req/s| N  
/v5/asset/delivery-record| 50 req/s| N  
/v5/asset/deposit/query-internal-record| 300 req/s| N  
/v5/fiat/balance-query| 1000 req/s| N  
/v5/fiat/query-coin-list| 1000 req/s| N  
/v5/fiat/trade-query| 1000 req/s| N  
/v5/fiat/query-trade-history| 1000 req/s| N  
/v5/asset/fundinghistory| 30 req/s| N  
/v5/asset/portfolio-margin| 50 req/s| N  
/v5/asset/settlement-record| 50 req/s| N  
/v5/asset/total-members-assets| 50 req/s| N  
/v5/asset/withdraw/vasp/list| 1 req/s| N  
/v5/asset/withdraw/query-address| 300 req/s| N  
POST| /v5/asset/transfer/inter-transfer| 60 req/min| N  
/v5/asset/transfer/save-transfer-sub-member| 20 req/s| N  
/v5/asset/transfer/universal-transfer| 5 req/s| N  
/v5/asset/withdraw/create| 5 req/s| N  
/v5/asset/withdraw/cancel| 60 req/min| N  
/v5/asset/exchange/quote-apply| 20 req/s| N  
/v5/asset/exchange/convert-execute| 20 req/s| N  
/v5/asset/covert/small-balance-execute| 5 req/s| N  
/v5/asset/covert/get-quote| 5 req/s| N  
/v5/asset/deposit/deposit-to-account| 300 req/s| N  
/v5/fiat/trade-execute| 100 req/s| N  
/v5/fiat/quote-apply| 1000 req/s| N  
GET| /v5/asset/exchange/convert-result-query| 50 req/s| N  
/v5/asset/exchange/query-convert-history| 50 req/s| N  
/v5/fiat/reference-price| 1000 req/s| N  
  
#### User

Method| Path| Limit| upgradable  
---|---|---|---  
POST| /v5/user/create-sub-member| 1 req/s| N  
/v5/user/create-sub-api| 1 req/s| N  
/v5/user/frozen-sub-member| 5 req/s| N  
/v5/user/update-api| 5 req/s| N  
/v5/user/update-sub-api| 5 req/s| N  
/v5/user/delete-api| 5 req/s| N  
/v5/user/delete-sub-api| 5 req/s| N  
GET| /v5/user/query-sub-members| 10 req/s| N  
/v5/user/query-api| 10 req/s| N  
/v5/user/aff-customer-info| 10 req/s| N  
POST| /v5/user/agreement| 20 req/s| N  
GET| /v5/user/submembers| 5 req/s| N  
/v5/user/escrow_sub_members| 5 req/s| N  
/v5/user/sub-apikeys| 10 req/s| N  
/v5/user/get-member-type| 10 req/s| N  
POST| /v5/user/del-submember| 5 req/s| N  
GET| /v5/user/invitation/referrals| 10 req/s| N  
  
#### Spot Margin Trade

Method| Path| Limit| Upgradable  
---|---|---|---  
POST| [Toggle Margin Trade](/docs/v5/spot-margin-uta/switch-mode)| 5 req/s| N  
POST| [Set Leverage](/docs/v5/spot-margin-uta/set-leverage)| 5 req/s| N  
GET| [Get Status And Leverage](/docs/v5/spot-margin-uta/status)| 50 req/s| N  
GET| [Get Max Borrowable Amount](/docs/v5/spot-margin-uta/max-borrowable)| 50 req/s| N  
GET| [Get Coin State](/docs/v5/spot-margin-uta/coinstate)| 50 req/s| N  
GET| [Get Available Amount to Repay](/docs/v5/spot-margin-uta/repayment-available-amount)| 50 req/s| N  
POST| [Set Auto Repay Mode](/docs/v5/spot-margin-uta/set-auto-repay-mode)| 5 req/s| N  
GET| [Get Auto Repay Mode](/docs/v5/spot-margin-uta/get-auto-repay-mode)| 50 req/s| N  
GET| [Get Fixed-Rate Borrow Order Quote](/docs/v5/spot-margin-uta/fixedborrow-order-quote)| 5 req/s| N  
POST| [Fixed-Rate Borrow](/docs/v5/spot-margin-uta/fixedborrow)| 1 req/s| N  
POST| [Renew Fixed-Rate Borrow](/docs/v5/spot-margin-uta/fixedborrow-renew)| 1 req/s| N  
GET| [Get Fixed-Rate Borrow Order Info](/docs/v5/spot-margin-uta/fixedborrow-order-info)| 5 req/s| N  
GET| [Get Fixed-Rate Borrow Contract Info](/docs/v5/spot-margin-uta/fixedborrow-contract-info)| 5 req/s| N  
GET| [Get Liability Info](/docs/v5/spot-margin-uta/liability)| 5 req/s| N  
  
#### Spread Trading

Method| Path| Limit| Upgradable  
---|---|---|---  
POST| [Create Order](/docs/v5/spread/trade/create-order)| 20 req/s| N  
POST| [Amend Order](/docs/v5/spread/trade/amend-order)| 20 req/s| N  
POST| [Cancel Order](/docs/v5/spread/trade/cancel-order)| 20 req/s| N  
POST| [Cancel All Orders](/docs/v5/spread/trade/cancel-all)| 5 req/s| N  
GET| [Get Open Orders](/docs/v5/spread/trade/open-order)| 50 req/s| N  
GET| [Get Order History](/docs/v5/spread/trade/order-history)| 50 req/s| N  
GET| [Get Trade History](/docs/v5/spread/trade/trade-history)| 50 req/s| N  
GET| [Get Max Qty](/docs/v5/spread/trade/max-qty)| 50 req/s| N  
  
#### RFQ

Method| Path| Limit| Upgradable  
---|---|---|---  
POST| [Cancel All Quotes](/docs/v5/rfq/trade/cancel-all-quotes)| 50 req/s| N  
POST| [Cancel Quote](/docs/v5/rfq/trade/cancel-quote)| 50 req/s| N  
POST| [Accept non-LP Quote](/docs/v5/rfq/trade/accept-other-quote)| 50 req/s| N  
POST| [Cancel All RFQs](/docs/v5/rfq/trade/cancel-all-rfq)| 50 req/s| N  
POST| [Create Quote](/docs/v5/rfq/trade/create-quote)| 50 req/s| N  
POST| [Create RFQ](/docs/v5/rfq/trade/create-rfq)| 50 req/s| N  
POST| [Execute Quote](/docs/v5/rfq/trade/execute-quote)| 50 req/s| N  
POST| [Cancel RFQ](/docs/v5/rfq/trade/cancel-rfq)| 50 req/s| N  
GET| [Get Public Trades](/docs/v5/rfq/trade/public-trades)| 50 req/s| N  
GET| [Get Quotes](/docs/v5/rfq/trade/quote-list)| 50 req/s| N  
GET| [Get Quotes (real-time)](/docs/v5/rfq/trade/quote-realtime)| 50 req/s| N  
GET| [Get RFQ Configuration](/docs/v5/rfq/trade/rfq-config)| 50 req/s| N  
GET| [Get RFQs](/docs/v5/rfq/trade/rfq-list)| 50 req/s| N  
GET| [Get RFQs (real-time)](/docs/v5/rfq/trade/rfq-realtime)| 50 req/s| N  
GET| [Get Trade History](/docs/v5/rfq/trade/trade-list)| 50 req/s| N  
  
#### Institutional Loan

Method| Path| Limit| Upgradable  
---|---|---|---  
GET| [Get Product Info](/docs/v5/otc/margin-product-info)| 100 req/s| N  
GET| [Get Margin Coin Info](/docs/v5/otc/margin-coin-convert-info)| 100 req/s| N  
GET| [Get Loan Orders](/docs/v5/otc/loan-info)| 20 req/s| N  
GET| [Get Repayment Orders](/docs/v5/otc/repay-info)| 20 req/s| N  
GET| [Get LTV](/docs/v5/otc/ltv-convert)| 20 req/s| N  
POST| [Bind Or Unbind UID](/docs/v5/otc/bind-uid)| 1 req/s| N  
POST| [Repay](/docs/v5/otc/repay)| 1 req/s| N  
  
## Instructions for batch endpoints

tip

The batch order endpoint, which includes operations for creating, amending, and canceling, has its own rate limit and does not share it with single requests, _e.g., let's say the rate limit of single create order endpoint is 100/s, and batch create order endpoint is 100/s, so in this case, I can place 200 linear orders in one second if I use both endpoints to place orders_

### When category = linear spot or inverse

  * API for batch create/amend/cancel order, the frequency of the API will be consistent with the current configuration, but the counting consumption will be consumed according to the actual number of orders. (Number of consumption = number of requests * number of orders included in a single request), and the configuration of business lines is independent of each other.

  * The batch APIs allows 1-10 orders/request. For example, if a batch order request is made once and contains 5 orders, then the request limit will consume 5.

  * If part of the last batch of orders requested within 1s exceeds the limit, the part that exceeds the limit will fail, and the part that does not exceed the limit will succeed. For example, in the 1 second, the remaining limit is 5, but a batch request containing 8 orders is placed at this time, then the first 5 orders will be successfully placed, and the 6-8th orders will report an error exceeding the limit, and these orders will fail.

---

# 基礎頻率限制

## IP限頻

### HTTP IP限頻

默認情況下, 每個IP允許在每5秒的時間窗口內發送最多600次請求。這個速率限制將統計所有打到`api.bybit.com`, `api.bybick.com`, 以及本地站`api.bybit.kz`等域名的請求數量。 如果您遇到了**“403, access too frequent”** 這樣的報錯, 它表示您的IP已經超過了限定的頻率, 這種情況下, 您應當斷開所有來自這個IP的活著的HTTP會話, 然後休息至少10分鐘。IP將會自動解除限制。

我們不建議您在這些限制的邊緣運行您的應用程序，以防異常的網絡活動導致意外違規。

### Websocket IP 限頻

  * 不要在5分鐘內構建超過500個連接, 這個限頻適用於所有發往`stream.bybit.com` 以及本地站域名, 比如 `stream.bybit.kz`的連接請求;
  * 不要嘗試頻繁地構建連接與斷開連接;
  * 訂閱行情數據時, 每個IP不要構建超過1,000個連接, 現貨、U本位期貨、幣本位期貨以及期權分開計算。



## 賬戶頻率限製

警告

如果您收到這樣的響應`"retCode": 10006, "retMsg": "Too many visits!"`, 則表示您觸發了帳戶頻率限制, 請等到頻率限制重置以後, 再繼續發送請求。

Bybit基於**每秒鍾** 的滾動時間窗口來做頻率限製，並且是按**賬戶** （uid）來做劃分限製，每次請求API響應頭(response header)中都會包含如下字段：

  * `X-Bapi-Limit-Status` \- 該接口當前時間窗口剩余可用請求數
  * `X-Bapi-Limit` \- 該接口當前頻率限製上限
  * `X-Bapi-Limit-Reset-Timestamp` \- 如果您已超過該接口當前窗口頻率限製，該字段表示下個可用時間窗口的時間戳（毫秒），即什麽時候可以恢復訪問；如果您未超過該接口當前窗口頻率限製，該字段表示返回的是當前服務器時間（毫秒).



> Http 響應頭示例
    
    
    ▶Response Headers  
    Content-Type: application/json; charset=utf-8  
    Content-Length: 141  
    X-Bapi-Limit: 10  
    X-Bapi-Limit-Status: 9  
    X-Bapi-Limit-Reset-Timestamp: 1672738134824  
    

### 接口頻率限制表

#### 交易

請求方式| 路徑| 統一帳戶| 是否可提頻  
---|---|---|---  
inverse| linear| option| spot  
POST| /v5/order/create| 10/s| 10/s| 20/s| Y  
/v5/order/amend| 10/s| 10/s| 10/s| Y  
/v5/order/cancel| 10/s| 10/s| 20/s| Y  
/v5/order/cancel-all| 10/s| 1/s| 20/s| Y  
/v5/order/create-batch| 10/s| 10/s| 20/s| Y  
/v5/order/amend-batch| 10/s| 10/s| 20/s| Y  
/v5/order/cancel-batch| 10/s| 10/s| 20/s| Y  
/v5/order/disconnected-cancel-all| 5/s| N  
/v5/order/pre-check| 10/s| 10/s| 20/s| Y  
GET| /v5/order/realtime| 50/s| N  
/v5/order/history| 50/s| N  
/v5/execution/list| 50/s| N  
/v5/order/spot-borrow-check| -| 50/s| N  
POST| /v5/fcombobot/getlimit| 10/s| -| -| N  
/v5/fcombobot/create| 10/s| -| -| N  
/v5/fcombobot/close| 10/s| -| -| N  
/v5/fcombobot/detail| 10/s| -| -| N  
/v5/fgridbot/validate| 10/s| -| -| N  
/v5/fgridbot/create| 10/s| -| -| N  
/v5/fgridbot/close| 10/s| -| -| N  
/v5/fgridbot/detail| 10/s| -| -| N  
/v5/fmartingalebot/getlimit| 10/s| -| -| N  
/v5/fmartingalebot/create| 100/s| -| -| N  
/v5/fmartingalebot/close| 10/s| -| -| N  
/v5/fmartingalebot/detail| 10/s| -| -| N  
/v5/grid/validate-input| -| 100/s| N  
/v5/grid/create-grid| -| 3/s| N  
/v5/grid/close-grid| -| 3/s| N  
/v5/grid/query-grid-detail| -| 10/s| N  
/v5/dca/create-bot| -| 3/s| N  
/v5/dca/close-bot| -| 3/s| N  
/v5/strategy/create| 100/s| -| 100/s| N  
GET| /v5/strategy/list| 200/s| -| 200/s| N  
/v5/strategy/order-list| 200/s| -| 200/s| N  
POST| /v5/strategy/stop| 100/s| -| 100/s| N  
  
#### 持倉

請求方式| 路徑| 統一帳戶| 是否可提頻  
---|---|---|---  
inverse| linear| option| spot  
GET| /v5/position/list| 50/s| -| N  
/v5/position/closed-pnl| 50/s| -| -| N  
/v5/position/get-closed-positions| -| -| 50/s| -| N  
/v5/position/move-history| 10/s| N  
POST| /v5/position/set-leverage| 10/s| -| -| N  
/v5/position/switch-mode| -| 10/s| -| -| N  
/v5/position/trading-stop| 10/s| -| N  
/v5/position/set-auto-add-margin| -| 10/s| -| -| N  
/v5/position/add-margin| 10/s| -| -| N  
/v5/position/confirm-pending-mmr| 10/s| -| -| N  
/v5/position/move-positions| 10/s| N  
  
#### 帳戶

請求方式| 路徑| | 頻率| 是否可提頻  
---|---|---|---|---  
GET| /v5/account/wallet-balance| accountType=UNIFIED| 50/s| N  
/v5/account/withdrawal| | 50/s| N  
/v5/account/borrow-history| | 50/s| N  
/v5/account/borrow| | 1/s| N  
/v5/account/repay| | 1/s| N  
/v5/account/no-convert-repay| | 1/s| N  
/v5/account/collateral-info| | 50/s| N  
/v5/asset/coin-greeks| | 50/s| N  
/v5/account/transaction-log| accountType=UNIFIED| 25/s| N  
/v5/account/fee-rate| | 5/s| N  
/v5/account/info| | 50/s| N  
/v5/account/instruments-info| | 10/s| N  
/v5/account/mmp-state| | -| N  
/v5/account/option-asset-info| | -| N  
/v5/account/pay-info| | 50/s| N  
/v5/account/query-dcp-info| | 5/s| N  
/v5/account/smp-group| | 5/s| N  
/v5/account/trade-info-for-analysis| | 50/s| N  
/v5/account/user-setting-config| | 50/s| N  
POST| /v5/account/mmp-modify| | 5/s| N  
/v5/account/mmp-reset| | 5/s| N  
/v5/account/quick-repayment| | 1/s| N  
/v5/account/set-collateral-switch| | -| N  
/v5/account/set-collateral-switch-batch| | 5/s| N  
/v5/account/set-delta-mode| | -| N  
/v5/account/set-hedging-mode| | -| N  
/v5/account/set-limit-px-action| | 10/s| N  
/v5/account/set-margin-mode| | 5/s| N  
/v5/account/upgrade-to-uta| | 1/s| N  
  
#### 資產

請求方式| 路徑| 頻率| 是否可提頻  
---|---|---|---  
GET| /v5/asset/transfer/query-asset-info| 60 req/min| N  
/v5/asset/transfer/query-transfer-coin-list| 60 req/min| N  
/v5/asset/transfer/query-inter-transfer-list| 60 req/min| N  
/v5/asset/transfer/query-sub-member-list| 60 req/min| N  
/v5/asset/transfer/query-universal-transfer-list| 5 req/s| N  
/v5/asset/transfer/query-account-coins-balance| 5 req/s| N  
/v5/asset/transfer/query-account-coin-balance| 450 req/s| N  
/v5/asset/asset-overview| 50 req/s| N  
/v5/asset/withdraw/withdrawable-amount| 300 req/s| N  
/v5/asset/deposit/query-record| 100 req/min| N  
/v5/asset/deposit/query-sub-member-record| 300 req/min| N  
/v5/asset/deposit/query-address| 300 req/min| N  
/v5/asset/deposit/query-sub-member-address| 300 req/min| N  
/v5/asset/withdraw/query-record| 300 req/min| N  
/v5/asset/coin/query-info| 5 req/s| N  
/v5/asset/exchange/order-record| 600 req/min| N  
/v5/asset/exchange/query-coin-list| 30 req/s| N  
/v5/asset/covert/small-balance-history| 5 req/s| N  
/v5/asset/covert/small-balance-list| 10 req/s| N  
/v5/asset/delivery-record| 50 req/s| N  
/v5/asset/deposit/query-internal-record| 300 req/s| N  
/v5/fiat/balance-query| 1000 req/s| N  
/v5/fiat/query-coin-list| 1000 req/s| N  
/v5/fiat/trade-query| 1000 req/s| N  
/v5/fiat/query-trade-history| 1000 req/s| N  
/v5/asset/fundinghistory| 30 req/s| N  
/v5/asset/portfolio-margin| 50 req/s| N  
/v5/asset/settlement-record| 50 req/s| N  
/v5/asset/total-members-assets| 50 req/s| N  
/v5/asset/withdraw/vasp/list| 1 req/s| N  
/v5/asset/withdraw/query-address| 300 req/s| N  
POST| /v5/asset/transfer/inter-transfer| 60 req/min| N  
/v5/asset/transfer/save-transfer-sub-member| 20 req/s| N  
/v5/asset/transfer/universal-transfer| 5 req/s| N  
/v5/asset/withdraw/create| 5 req/s| N  
/v5/asset/withdraw/cancel| 60 req/min| N  
/v5/asset/exchange/quote-apply| 20 req/s| N  
/v5/asset/exchange/convert-execute| 20 req/s| N  
/v5/asset/covert/small-balance-execute| 5 req/s| N  
/v5/asset/covert/get-quote| 5 req/s| N  
/v5/asset/deposit/deposit-to-account| 300 req/s| N  
/v5/fiat/trade-execute| 100 req/s| N  
/v5/fiat/quote-apply| 1000 req/s| N  
GET| /v5/asset/exchange/convert-result-query| 50 req/s| N  
/v5/asset/exchange/query-convert-history| 50 req/s| N  
/v5/fiat/reference-price| 1000 req/s| N  
  
#### 用戶

請求方式| 路徑| 頻率| 是否可提頻  
---|---|---|---  
POST| /v5/user/create-sub-member| 1 req/s| N  
/v5/user/create-sub-api| 1 req/s| N  
/v5/user/frozen-sub-member| 5 req/s| N  
/v5/user/update-api| 5 req/s| N  
/v5/user/update-sub-api| 5 req/s| N  
/v5/user/delete-api| 5 req/s| N  
/v5/user/delete-sub-api| 5 req/s| N  
GET| /v5/user/query-sub-members| 10 req/s| N  
/v5/user/query-api| 10 req/s| N  
/v5/user/aff-customer-info| 10 req/s| N  
POST| /v5/user/agreement| 20 req/s| N  
GET| /v5/user/submembers| 5 req/s| N  
/v5/user/escrow_sub_members| 5 req/s| N  
/v5/user/sub-apikeys| 10 req/s| N  
/v5/user/get-member-type| 10 req/s| N  
POST| /v5/user/del-submember| 5 req/s| N  
GET| /v5/user/invitation/referrals| 10 req/s| N  
  
#### 全倉槓桿

請求方式| 路徑| 頻率| 是否可提頻  
---|---|---|---  
POST| [全倉槓桿開關](/docs/zh-TW/v5/spot-margin-uta/switch-mode)| 5 req/s| N  
POST| [全倉槓桿設置](/docs/zh-TW/v5/spot-margin-uta/set-leverage)| 5 req/s| N  
GET| [查詢開關狀態和倍數](/docs/zh-TW/v5/spot-margin-uta/status)| 50 req/s| N  
GET| [查詢最大可借數](/docs/zh-TW/v5/spot-margin-uta/max-borrowable)| 50 req/s| N  
GET| [查詢幣種槓桿](/docs/zh-TW/v5/spot-margin-uta/coinstate)| 50 req/s| N  
GET| [查詢負債幣種可還款金額](/docs/zh-TW/v5/spot-margin-uta/repayment-available-amount)| 50 req/s| N  
POST| [設定現貨自動還款模式](/docs/zh-TW/v5/spot-margin-uta/set-auto-repay-mode)| 5 req/s| N  
GET| [獲取現貨自動還款模式](/docs/zh-TW/v5/spot-margin-uta/get-auto-repay-mode)| 50 req/s| N  
GET| [查詢固定利率借款掛單報價](/docs/zh-TW/v5/spot-margin-uta/fixedborrow-order-quote)| 5 req/s| N  
POST| [固定利率借款](/docs/zh-TW/v5/spot-margin-uta/fixedborrow)| 1 req/s| N  
POST| [固定利率借款續借](/docs/zh-TW/v5/spot-margin-uta/fixedborrow-renew)| 1 req/s| N  
GET| [查詢固定利率借款訂單信息](/docs/zh-TW/v5/spot-margin-uta/fixedborrow-order-info)| 5 req/s| N  
GET| [查詢固定利率借款合約信息](/docs/zh-TW/v5/spot-margin-uta/fixedborrow-contract-info)| 5 req/s| N  
GET| [查詢負債信息](/docs/zh-TW/v5/spot-margin-uta/liability)| 5 req/s| N  
  
#### 價差交易

請求方式| 路徑| 頻率| 是否可提頻  
---|---|---|---  
POST| [創建價差委托單](/docs/zh-TW/v5/spread/trade/create-order)| 20 req/s| N  
POST| [修改價差委託單](/docs/zh-TW/v5/spread/trade/amend-order)| 20 req/s| N  
POST| [撤銷價差委託單](/docs/zh-TW/v5/spread/trade/cancel-order)| 20 req/s| N  
POST| [價差-全部撤單](/docs/zh-TW/v5/spread/trade/cancel-all)| 5 req/s| N  
GET| [查詢價差活動單](/docs/zh-TW/v5/spread/trade/open-order)| 50 req/s| N  
GET| [查詢價差訂單歷史](/docs/zh-TW/v5/spread/trade/order-history)| 50 req/s| N  
GET| [查詢價差成交歷史](/docs/zh-TW/v5/spread/trade/trade-history)| 50 req/s| N  
GET| [查詢最大下單數量](/docs/zh-TW/v5/spread/trade/max-qty)| 50 req/s| N  
  
#### RFQ

請求方式| 路徑| 頻率| 是否可提頻  
---|---|---|---  
POST| [取消所有報價單](/docs/zh-TW/v5/rfq/trade/cancel-all-quotes)| 50 req/s| N  
POST| [取消報價單](/docs/zh-TW/v5/rfq/trade/cancel-quote)| 50 req/s| N  
POST| [接受非 LP 報價](/docs/zh-TW/v5/rfq/trade/accept-other-quote)| 50 req/s| N  
POST| [取消所有詢價單](/docs/zh-TW/v5/rfq/trade/cancel-all-rfq)| 50 req/s| N  
POST| [報價](/docs/zh-TW/v5/rfq/trade/create-quote)| 50 req/s| N  
POST| [詢價](/docs/zh-TW/v5/rfq/trade/create-rfq)| 50 req/s| N  
POST| [執行報價](/docs/zh-TW/v5/rfq/trade/execute-quote)| 50 req/s| N  
POST| [取消詢價單](/docs/zh-TW/v5/rfq/trade/cancel-rfq)| 50 req/s| N  
GET| [獲取rfq公共成交數據](/docs/zh-TW/v5/rfq/trade/public-trades)| 50 req/s| N  
GET| [獲取歷史報價](/docs/zh-TW/v5/rfq/trade/quote-list)| 50 req/s| N  
GET| [獲取即時報價](/docs/zh-TW/v5/rfq/trade/quote-realtime)| 50 req/s| N  
GET| [rfq配寘資訊](/docs/zh-TW/v5/rfq/trade/rfq-config)| 50 req/s| N  
GET| [獲取歷史詢價資訊](/docs/zh-TW/v5/rfq/trade/rfq-list)| 50 req/s| N  
GET| [獲取實时的詢價單資訊](/docs/zh-TW/v5/rfq/trade/rfq-realtime)| 50 req/s| N  
GET| [獲取交易資訊](/docs/zh-TW/v5/rfq/trade/trade-list)| 50 req/s| N  
  
#### 機構借貸

請求方式| 路徑| 頻率| 是否可提頻  
---|---|---|---  
GET| [查詢產品信息](/docs/zh-TW/v5/otc/margin-product-info)| 100 req/s| N  
GET| [查詢保證金幣種信息](/docs/zh-TW/v5/otc/margin-coin-convert-info)| 100 req/s| N  
GET| [查詢借貸訂單信息](/docs/zh-TW/v5/otc/loan-info)| 20 req/s| N  
GET| [查詢還款信息](/docs/zh-TW/v5/otc/repay-info)| 20 req/s| N  
GET| [查詢風險率](/docs/zh-TW/v5/otc/ltv-convert)| 20 req/s| N  
POST| [綁定/解綁UID](/docs/zh-TW/v5/otc/bind-uid)| 1 req/s| N  
POST| [還款](/docs/zh-TW/v5/otc/repay)| 1 req/s| N  
  
## 批量接口限頻說明

提示

批次訂單接口（包括創建、修改和取消）的速率限制不會與單一的下改撤請求共享。 _例如，單一下單接口頻率是100/秒, 批量下單接口是100/秒,，那麼當結合兩個接口一起下單時， 就擁有200單每秒的能力_ 。

#### 僅category=linear, inverse或spot時

  * 批量下單的接口，api rate limit：接口的頻次，還是統一沿用當前配置，但是計數消耗會根據實際的訂單數來消耗。（消耗數 = 請求數 * 請求中包含的訂單數），業務線配置相互獨立。

  * 批量接口允許1-10orders/request，例如，批量下單請求一次，包含5個orders，則本次請求limit數量消耗5。

  * 若1s內的最後一次請求的批量訂單，部分超限，則超過的部分會失敗（報錯超過上限），未超過的部分會成功。例如，這1s中，limit還剩5，但是此時下了一個包含8個orders的批量請求， 那麼前5個orders會下單成功，第6-8的orders，會報錯超過上限，下單失敗。