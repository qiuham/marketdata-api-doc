---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/margin-trading/best-practice
api_type: REST
updated_at: 2026-11-13 20:28:33.125542
---

# Best Practice

### Activating & Enabling Margin Trading via AP

#### Enable Margin on Your Account

Before using the API, please ensure margin trading is enabled on your Binance account. For first time users, you will be required to complete the margin quiz and agree to the margin terms, once completed you will need to transfer supported tokens into the cross margin or isolated margin wallet to activate it. For existing users, you will just need to transfer supported tokens into the cross margin or isolated margin wallet to activate the margin wallet. When creating your API key, check the setting to “Enable Spot & Margin Trading, and Enable Margin Loan, Repay & Transfer”, otherwise margin API calls will be rejected. For your security, please also consider IP whitelisting on your API key.

Please refer to the article [“How to Create API Keys on Binance?”](https://www.binance.com/en/support/faq/detail/360002502072) for more details.

If you are looking for a low-latency connectivity similar to spot trading, VIP 4 and above users are automatically eligible,for further information please refer to [Margin Special Key Api Portal](/en/docs/catalog/core-trading-margin-trading/api/rest-api/trade#create-special-key)

#### Tips to Avoid Common Mistakes:

  * Account activation: Double-check that your margin account is enabled. Otherwise, your API calls will return the following error {"code":-3003, "msg":"Margin account does not exist."}
  * Error handling: If you get an error like {"code":-2015, "msg":"Invalid API-key, IP, or permissions for action."}, it usually means either your API key lacks permission. To resolve this, please enable the API key settings via the website.



### Funding the Margin Account

Before trading on margin, you need to fund your margin account by transferring assets into it as collateral. Binance keeps Spot (exchange wallet) and Margin wallets separate. For cross margin, you have to transfer assets to the cross margin account; for isolated margin, you have to transfer to the specific isolated account for the trading pair.

#### Cross Margin Transfer

Users can invoke the following REST API to transfer assets to the cross margin account:

[POST /sapi/v1/asset/transfer](/en/docs/catalog/core-trading-wallet/api/rest-api/asset#user-universal-transfer)

This endpoint uses a parameter type to indicate direction:

  * MAIN_MARGIN: Spot account transfer to Margin (cross) account
  * UMFUTURE_MARGIN: USDⓈ-M Futures account transfer to Margin (cross) account
  * CMFUTURE_MARGIN: COIN-M Futures account transfer to Margin (cross) account
  * FUNDING_MARGIN: Funding account transfer to Margin (cross) account
  * OPTION_MARGIN: Options account transfer to Margin (cross) account



Other required parameters are asset (e.g. "USDT", "BTC"), amount (the quantity to transfer as a string) and timestamp. Please ensure you have that asset available for use in the source account.

  * Request Parameter:

Name| Type| Mandatory| Description  
---|---|---|---  
type| ENUM| YES|   
asset| STRING| YES|   
amount| DECIMAL| YES|   
fromSymbol| STRING| NO|   
toSymbol| STRING| NO|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
#### Isolated Margin Transfer

For isolated account, the type of direction is as follows:

  * MARGIN_ISOLATEDMARGIN: Margin(cross) account transfer to Isolated margin account
  * ISOLATEDMARGIN_ISOLATEDMARGIN: Isolated margin account transfer to Isolated margin account



When direction types are ISOLATEDMARGIN_MARGIN and ISOLATEDMARGIN_ISOLATEDMARGIN, you should specify the source and destination explicitly. Additional parameters, fromSymbol, is required.

On the other hand, when direction types are MARGIN_ISOLATEDMARGIN and ISOLATEDMARGIN_ISOLATEDMARGIN, toSymbol is required.

You will receive a successful response once the transfer is completed successfully.

{ "tranId": 1234567890 }

This tranId can be used to query transfer status if needed (though usually, a successful response means the transfer is complete).

With funds now in your margin account, you have collateral to borrow against. Next, we’ll borrow funds to perform a leverage trade.

#### Tips to Avoid Common Mistakes:

  * Insufficient collateral margin level: Sometimes, your collateral margin level may be too low to allow a transfer out of your account. You will get an error response {"code":-3020,"msg":"Transfer out amount exceeds max amount."}. To resolve it, you can reduce your outstanding debt or add more assets to meet the required margin level for the transfer.



### Borrowing Funds

One key feature of margin trading is the ability to borrow funds to increase your position size. On Binance, you can borrow different assets as long as you have sufficient collateral in your margin account for your chosen leverage. Borrowing is subject to interest (accrued hourly), and each asset has a maximum borrowable amount based on your collateral value and a chosen leverage.

In Binance, we use the same endpoint to execute borrow and repay

[POST /sapi/v1/margin/borrow-repay](/en/docs/catalog/core-trading-margin-trading/api/rest-api/borrow-repay#margin-account-borrow-repay)

#### Borrow

You must specify the asset you want to borrow and the amount. For isolated margin, you will include an extra parameter to indicate the isolated account. Binance uses a boolean isolated flag and a symbol parameter.

  * Request Parameter:

Name| Type| Mandatory| Description  
---|---|---|---  
asset| STRING| YES|   
isIsolated| STRING| YES| TRUE for Isolated Margin, FALSE for Cross Margin, Default FALSE  
symbol| STRING| YES| Only for Isolated margin  
amount| STRING| YES|   
type| STRING| YES| BORROW or REPAY  
recvWindow| LONG| NO| The value cannot be greater than 60000  
timestamp| LONG| YES|   
  
On success, you’ll get a JSON with a transaction ID for the loan. For example:

{ "tranId": 1234567891 }

This tranId is the identifier of the borrowing transaction (you can use it to query the loan status or history later).

After a successful borrow, the borrowed funds will be credited to the corresponding margin account (increasing your “borrowed” balance for that asset). You are now free to use those funds to trade. Keep in mind interest immediately starts accruing on the loan until it’s repaid.

#### Tips to Avoid Common Mistakes:

  * Maximum borrowable: If you get an error {"code": -3006, "msg": "Your borrow amount has exceed maximum borrow amount."}, it means the amount you want to borrow exceeds your limit. Binance enforces an initial margin requirement – borrowing too much will cause you to be below the initial margin requirement and hence the additional borrowings will be rejected. You can check your max borrowable amount via [GET /sapi/v1/margin/maxBorrowable](/en/docs/catalog/core-trading-margin-trading/api/rest-api/borrow-repay#query-max-borrow) for a given asset (and optionally symbol for isolated). This can be useful to see how much you could borrow against your available collateral.
  * Interest: Each borrowed asset accrues interest, which you can query via [GET /sapi/v1/margin/interestHistory](/en/docs/catalog/core-trading-margin-trading/api/rest-api/borrow-repay#get-interest-history). Interest is usually deducted from your margin account (adding to the “interest” field for that asset). Ensure you account for interest when repaying (please note that repayment covers interest first, then principal).
  * Asset availability: Not all assets may be borrowable at all times. Binance may have limits or temporarily suspend borrowing for certain assets if liquidity is low. If you get an error that an asset is not borrowable, you may need to check [GET /sapi/v1/margin/allAssets](/en/docs/catalog/core-trading-margin-trading/api/rest-api/market-data#get-all-margin-assets) or try later.
  * Insufficient available assets: If you get an error {"code": -3045, "msg": The system does not have enough asset now."} This can occur to both manual Margin borrow requests and auto-borrow Margin orders that require actual borrowing. This can be due to:
    * The Margin system's assets available for borrowing are less than the requested borrowing amount.
    * The system's inventory is critically low, leading to the rejection of all borrowing requests, irrespective of the amount.



We recommend monitoring the system status and adjusting your borrowing strategies accordingly.

  * Cross margin collateral haircuts: If you are trading in Cross Margin/Cross Margin Pro mode, collateral haircuts are factored into the collateral margin level calculation. Meaning assets have tiered collateral ratios that discount their value for margin calculations. For example, higher asset holdings may be valued at lower collateral percentages across tiers, reducing total collateral value accordingly. Please note that this does not affect Isolated Margin mode and the collateral margin level uses collateral asset value, not normal asset value:
    * For Cross Margin Classic, Collateral margin level will be used to calculate maximum borrowing and transfer-out amount, but will NOT be used to trigger Margin Call and Liquidation, where margin level will still be used.
    * For Cross Margin Pro, Collateral margin level will be used to calculate the maximum borrowing and transfer-out amounts, and will be used to trigger Margin Call and Liquidation as well.



You can find out more in [How to Calculate the Margin Level on Cross Margin Pro?](https://www.binance.com/en/support/faq/detail/12a78d8aa813470f96be283b45f75410)

  * Portfolio margin collateral haircuts: The USD value of all assets in the Cross Margin, USDⓈ-M Futures, and COIN-M Futures Wallets will be calculated based on the specified collateral rate (Not the same collateral ratio as Cross Margin Classic/Cross Margin Pro). You can find out the collateral ratio in [Tiered Collateral Ratio for PM Pro](https://www.binance.com/en/futures/trading-rules/perpetual/portfolio-margin/tiered-collateral-ratio)



Upon successfully borrowing, the token will be transferred to your margin wallet.Next, we will use the borrowed tokens to place a margin trade (buy or sell).

### Placing a Margin Trade

With your collateral (including funds you may have borrowed), you can create orders (limit, market, etc.) on your margin account. Binance provides a dedicated endpoint for margin orders:

[POST /sapi/v1/margin/order](/en/docs/catalog/core-trading-margin-trading/api/rest-api/trade#margin-account-new-order)

  * Request Parameter:

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
isIsolated| STRING| NO| for isolated margin or not, "TRUE", "FALSE"，default "FALSE"  
side| ENUM| YES| BUY SELL  
type| ENUM| YES|   
quantity| DECIMAL| NO|   
quoteOrderQty| DECIMAL| NO|   
price| DECIMAL| NO|   
stopPrice| DECIMAL| NO| Used with STOP_LOSS, STOP_LOSS_LIMIT, TAKE_PROFIT, and TAKE_PROFIT_LIMIT orders.  
newClientOrderId| STRING| NO| A unique id among open orders. Automatically generated if not sent.  
icebergQty| DECIMAL| NO| Used with LIMIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT to create an iceberg order.  
newOrderRespType| ENUM| NO| Set the response JSON. ACK, RESULT, or FULL; MARKET and LIMIT order types default to FULL, all other orders default to ACK.  
sideEffectType| ENUM| NO| NO_SIDE_EFFECT, MARGIN_BUY, AUTO_REPAY,AUTO_BORROW_REPAY; default NO_SIDE_EFFECT. More info in[FAQ](https://www.binance.com/en/support/faq/detail/f9fc51cda1984bf08b95e0d96c4570bc)  
timeInForce| ENUM| NO| GTC,IOC,FOK  
selfTradePreventionMode| ENUM| NO| The allowed enums is dependent on what is configured on the symbol. The possible supported values are EXPIRE_TAKER, EXPIRE_MAKER, EXPIRE_BOTH, NONE  
autoRepayAtCancel| BOOLEAN| NO| Only when MARGIN_BUY or AUTO_BORROW_REPAY order takes effect, true means that the debt generated by the order needs to be repay after the order is cancelled. The default is true  
recvWindow| LONG| NO| The value cannot be greater than 60000  
timestamp| LONG| YES|   
  
#### Auto-Borrow

If you have manually borrowed funds, you can use those in your margin trade. If you have not borrowed manually, Binance’s margin order endpoint can auto-borrow or auto-repay for you, depending on a parameter called sideEffectType.

The sideEffectType parameter lets you automate borrowing or repaying as part of the order placement.

  * NO_SIDE_EFFECT: No automatic borrow or repay. This is the default setting. You should have sufficient balance in your margin account (either from deposits or prior manual borrows) to execute the order. If you do not, the order placement will fail due to insufficient balance. Users essentially self-manage their borrowing and repayment themselves.
  * MARGIN_BUY: Automatic borrowing when needed for a BUY order. If you place a BUY order and do not have enough quote assets to deduct, Binance will automatically borrow the necessary amount of the quote asset up to your leverage limit. For a SELL order, if using MARGIN_BUY mode, it would auto-borrow the asset to sell (though typically one would use MARGIN_BUY for buys; see AUTO_BORROW_REPAY for a comprehensive mode). The borrow occurs only if needed and only when the order is executed (not at order creation). Essentially this equates to “borrow asset + place order” in one step.
  * AUTO_REPAY: Automatic repayment after the order executes. If your order results in you obtaining the asset that you owe (borrowed), the system will immediately use the proceeds to repay the loan. For example, if you had borrowed BTC and you sold some BTC (thus obtaining the quoted assets), setting AUTO_REPAY would use the quote assets you have to repay the BTC loan (converting the quote asset to BTC as needed to repay). As an example: if you borrowed USDT to buy BTC, when you sell BTC (for USDT) with AUTO_REPAY, it will use the USDT you receive to repay the USDT loan. Important: auto-repay will repay as much as possible of that asset’s liability (interest first) and will only work if the trade yields the same asset that was borrowed. This is useful to close out a margin position in one step (“place order + upon fill, repay debt”).
  * AUTO_BORROW_REPAY: Combines both of the above – automatic borrow and automatic repay in one step. This mode will borrow as needed to execute the order, and then after execution, immediately try to repay with whatever assets were obtained. It’s effectively a margin flip: e.g., if you have nothing and submit a BUY with AUTO_BORROW_REPAY, it will borrow the quote asset, buy the base asset, then if that base asset was what you needed to repay (in case of short position) it would repay, etc. In practice, this mode is a bit complex and is not allowed for certain multi-leg orders (like OCO/OTOCO).



For beginners, you may wish to start with NO_SIDE_EFFECT (ensuring you manually borrowed what you need) or use MARGIN_BUY if you want to skip the manual borrow step for a buy. Always verify that these automated steps did what you expected (please check your balances and loans after the order).

#### Tips to Avoid Common Mistakes:

  * Order Rules: Margin orders obey the same trading rules as spot (lot size, price step, minimum notional value, etc.). You can check the exchange information([GET /api/v3/exchangeInfo](/en/docs/products/spot/rest-api)) to find min/max order sizes or the margin symbol information ([GET /sapi/v1/margin/allAssets](/en/docs/catalog/core-trading-margin-trading/api/rest-api/market-data#get-all-margin-assets)) to find the minimum borrow/repay amount. If an order is invalid (e.g., too small), you’ll get an error about lot size or minimum notional.
  * Canceling Orders: If you need to cancel an open margin order, use [DELETE /sapi/v1/margin/order](/en/docs/catalog/core-trading-margin-trading/api/rest-api/trade#margin-account-cancel-order) with similar parameters (symbol, orderId or newclientOrderId, and if isolated, isIsolated=TRUE). There is also an endpoint to cancel all open margin orders on a symbol ([DELETE /sapi/v1/margin/openOrders](/en/docs/catalog/core-trading-margin-trading/api/rest-api/trade#margin-account-cancel-all-open-orders-on-a-symbol)). Canceling a margin order that had an auto-borrow does not automatically repay the borrow (unless you set autoRepayAtCancel=true for One-Triggers-a-One-Cancels-the-Other (OTOCO) orders – a parameter autoRepayAtCancel exists for that purpose.)
  * Limit price restriction: This error {“code”: -3064, “msg”: “Limit price needs to be within (-15%,15%) of current index price for this margin trading pair.”} often occurs when the limit price is not allowed. For certain low liquidity pairs or stablecoin to stablecoin pairs on Margin (e.g. USDT/DAI), there will be a price bracket of [-15%, 15%] (which is subject to changes). Please adjust the limit price accordingly.



At this stage, you have executed margin trades. Now it is important that you monitor your margin account to manage risk, as margin trading carries the risk of liquidation if the market moves against you.

### Monitoring the Margin Account

Properly monitoring your margin account is vital. You need to keep track of your balances, margin level (risk ratio), and any accumulating interest. Binance provides endpoints to fetch account details for both cross and isolated margin accounts.

#### Cross Margin Account Details

The endpoint: [GET /sapi/v1/margin/account](/en/docs/catalog/core-trading-margin-trading/api/rest-api/account#query-cross-margin-account-details) returns an overview of your cross margin account. This includes your current margin level, total asset value, total liability (debt) value, and a breakdown of each asset. Key fields in the response:

{

"assets":[
    
    
    Code
    
    {
    
        "baseAsset":
    
        {
    
          "asset": "BTC",
    
          "borrowEnabled": true,
    
          "borrowed": "0.00000000",
    
          "free": "0.00000000",
    
          "interest": "0.00000000",
    
          "locked": "0.00000000",
    
          "netAsset": "0.00000000",
    
          "netAssetOfBtc": "0.00000000",
    
          "repayEnabled": true,
    
          "totalAsset": "0.00000000"
    
        },
    
        "quoteAsset":
    
        {
    
          "asset": "USDT",
    
          "borrowEnabled": true,
    
          "borrowed": "0.00000000",
    
          "free": "0.00000000",
    
          "interest": "0.00000000",
    
          "locked": "0.00000000",
    
          "netAsset": "0.00000000",
    
          "netAssetOfBtc": "0.00000000",
    
          "repayEnabled": true,
    
          "totalAsset": "0.00000000"
    
        },
    
        "symbol": "BTCUSDT",
    
        "isolatedCreated": true,
    
        "enabled": true, // true-enabled, false-disabled
    
        "marginLevel": "0.00000000",
    
        "marginLevelStatus": "EXCESSIVE", // "EXCESSIVE", "NORMAL", "MARGIN\_CALL", "PRE\_LIQUIDATION", "FORCE\_LIQUIDATION"
    
        "marginRatio": "0.00000000",
    
        "indexPrice": "10000.00000000",
    
        "liquidatePrice": "1000.00000000",
    
        "liquidateRate": "1.00000000",
    
        "tradeEnabled": true
    
      }
    
    ],
    
    "totalAssetOfBtc": "0.00000000",
    
    "totalLiabilityOfBtc": "0.00000000",
    
    "totalNetAssetOfBtc": "0.00000000"

}

#### Isolated Margin Account Details

For isolated accounts, there is a similar endpoint: [GET /sapi/v1/margin/isolated/account](/en/docs/catalog/core-trading-margin-trading/api/rest-api/account#query-isolated-margin-account-info). This response includes details for each isolated margin account you have enabled. Each isolated account will have fields including isolatedMarginLevel, totalAsset, totalLiability, etc., specific to that pair, along with an array of assets (two assets per isolated pair, typically).

{

"assets":[
    
    
    Code
    
    {
    
        "baseAsset":
    
        {
    
          "asset": "BTC",
    
          "borrowEnabled": true,
    
          "borrowed": "0.00000000",
    
          "free": "0.00000000",
    
          "interest": "0.00000000",
    
          "locked": "0.00000000",
    
          "netAsset": "0.00000000",
    
          "netAssetOfBtc": "0.00000000",
    
          "repayEnabled": true,
    
          "totalAsset": "0.00000000"
    
        },
    
        "quoteAsset":
    
        {
    
          "asset": "USDT",
    
          "borrowEnabled": true,
    
          "borrowed": "0.00000000",
    
          "free": "0.00000000",
    
          "interest": "0.00000000",
    
          "locked": "0.00000000",
    
          "netAsset": "0.00000000",
    
          "netAssetOfBtc": "0.00000000",
    
          "repayEnabled": true,
    
          "totalAsset": "0.00000000"
    
        },
    
        "symbol": "BTCUSDT",
    
        "isolatedCreated": true,
    
        "enabled": true, // true-enabled, false-disabled
    
        "marginLevel": "0.00000000",
    
        "marginLevelStatus": "EXCESSIVE", // "EXCESSIVE", "NORMAL", "MARGIN\_CALL", "PRE\_LIQUIDATION", "FORCE\_LIQUIDATION"
    
        "marginRatio": "0.00000000",
    
        "indexPrice": "10000.00000000",
    
        "liquidatePrice": "1000.00000000",
    
        "liquidateRate": "1.00000000",
    
        "tradeEnabled": true
    
      }
    
    ],
    
    "totalAssetOfBtc": "0.00000000",
    
    "totalLiabilityOfBtc": "0.00000000",
    
    "totalNetAssetOfBtc": "0.00000000"

}

#### User Data Stream (Advanced)

Binance provides a WebSocket User Data Stream for margin accounts that can push real-time updates on account balance changes and order updates. If you need real-time monitoring (instead of polling REST endpoints), you can create a listenKey via [POST /sapi/v1/userDataStream](/en/docs/products/margin-trading/trade-data-stream) (for margin) and subscribe to events. The use of data stream is advanced and beyond the scope of this guide, but you may wish to keep it in mind if you want instantaneous alerts on margin calls or fills.

After actively managing your positions, you will eventually want to close them and repay any borrowed funds. Let’s move to repaying the loans.

### Repaying Borrowed Tokens

Once you’ve finished using the borrowed tokens (for example, after closing a leveraged trade), you can repay your margin loans. Repaying returns the borrowed tokens to Binance and frees up your collateral. You can repay partially or in full.

In Binance, we use the same endpoint to execute borrow and repay

[POST /sapi/v1/margin/borrow-repay](/en/docs/catalog/core-trading-margin-trading/api/rest-api/borrow-repay#margin-account-borrow-repay)

  * Request Parameter:

Name| Type| Mandatory| Description  
---|---|---|---  
asset| STRING| YES|   
isIsolated| STRING| YES| TRUE for Isolated Margin, FALSE for Cross Margin, Default FALSE  
symbol| STRING| YES| Only for Isolated margin  
amount| STRING| YES|   
type| STRING| YES| BORROW or REPAY  
recvWindow| LONG| NO| The value cannot be greater than 60000  
timestamp| LONG| YES|   
  
Upon repayment successfully, you will receive a JSON with a transaction ID for the loan. For example:

{ "tranId": 1234567894 }

This indicates the repay transaction was successful. After repayment, your outstanding loan for that asset should decrease by the amount repaid (and interest for that asset may drop to 0 if fully repaid).

With borrowing and repaying covered, you have essentially completed a margin trade lifecycle: fund account -> borrow -> trade -> (optional: trade back) -> repay. The last piece is keeping track of what happened – your trade and transaction history.

### Reviewing Trading and Account History

Iti’s important to review your margin trades and account activities, both for understanding your performance and for record-keeping. It can also be helpful for debugging your trading bot. Binance’s API provides endpoints to query past orders, trades, and account actions (transfers, loans, repayments, etc.).

#### Trade History

To get a list of trades (fills) executed on your margin account, use [GET /sapi/v1/margin/myTrades.](/en/docs/catalog/core-trading-margin-trading/api/rest-api/trade#query-margin-accounts-trade-list)

  * Request Parameter:

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
isIsolated| STRING| NO| For isolated margin or not, "TRUE", "FALSE"，default "FALSE"  
orderId| LONG| NO|   
startTime| LONG| NO|   
endTime| LONG| NO|   
fromId| LONG| NO| TradeId to fetch from. Default gets most recent trades.  
limit| INT| NO| Default 500; max 1000.  
recvWindow| LONG| NO| The value cannot be greater than 60000  
timestamp| LONG| YES|   
  
For example, after an earlier BNB buy, a call to myTrades for BNBBTC may return something like:

[ { "commission": "0.00006000", "commissionAsset": "BTC", "id": 34, "isBestMatch": true, "isBuyer": false, "isMaker": false, "orderId": 39324, "price": "0.02000000", "qty": "3.00000000", "symbol": "BNBBTC", "isIsolated": false, "time": 1561973357171 } ]

#### Order History

If you need the order details (including orders that might not have any fills, such as canceled orders), you can use:

  * [GET /sapi/v1/margin/allOrders](/en/docs/catalog/core-trading-margin-trading/api/rest-api/trade#query-margin-accounts-all-orders) – to fetch all orders (filled, canceled, etc.) on a symbol.
  * [GET /sapi/v1/margin/openOrders](/en/docs/catalog/core-trading-margin-trading/api/rest-api/trade#query-margin-accounts-open-orders) – for current open orders (similar to spot).
  * [GET /sapi/v1/margin/order](/en/docs/catalog/core-trading-margin-trading/api/rest-api/trade#query-margin-accounts-order) – to query a specific order by ID.



#### Account Activity History

Binance provides endpoints to review other account activities:

  * [GET /sapi/v1/margin/borrow-repay](/en/docs/catalog/core-trading-margin-trading/api/rest-api/borrow-repay#query-borrow-repay-records-in-margin-account) – Query borrow/repay history. You can filter by asset, isolated symbol, etc. This returns records of each loan and repay transaction with amounts, interest, status. For example, it can show when you borrowed 100 USDC, with a tranId and timestamp.
  * [GET /sapi/v1/margin/transfer](/en/docs/catalog/core-trading-margin-trading/api/rest-api/transfer#get-cross-margin-transfer-history) – Query transfer history between spot and margin. You can see deposits and withdrawals from margin accounts, with timestamps and amounts.
  * [GET /sapi/v1/margin/interestHistory](/en/docs/catalog/core-trading-margin-trading/api/rest-api/borrow-repay#get-interest-history) – List of interest charged over time per asset.
  * [GET /sapi/v1/margin/forceLiquidationRec](/en/docs/catalog/core-trading-margin-trading/api/rest-api/trade#get-force-liquidation-record) – Record of any forced liquidations (hopefully none!).



Was this page helpful?

Last modified on November 12, 2026

[Error Codes](/en/docs/products/margin-trading/error-code)[Introduction](/en/docs/products/wallet/Introduction)

---

# 最佳实践

### 通过 API 激活并启用杠杆交易

#### 在账户中启用杠杆交易

在使用 API 之前，请确保您的币安账户已启用杠杆交易。首次使用者需要完成杠杆交易测试并同意杠杆交易条款，完成后需将支持的代币转入「全仓杠杆」或「逐仓杠杆」钱包以激活。已有杠杆交易账户的用户，只需将支持的代币转入相应的钱包即可激活杠杆交易钱包。创建 API 密钥时，请务必勾选「允许现货及杠杆交易」、「允许杠杆质押借币、还款和划转」权限，否则杠杆交易相关的 API 请求会被拒绝。为保障账户安全，也建议您在 API 密钥中进行 IP 白名单设置。

更多详情请参考文章[《如何在币安创建API密钥》](https://www.binance.com/zh-CN/support/faq/detail/360002502072)。

如果您需要类似现货交易的低延迟连接，VIP 4 及以上等级用户将自动享有该权限，更多信息请参考「[新建低延迟交易SpecialKey(TRADE)](/zh-CN/docs/catalog/core-trading-margin-trading/api/rest-api/trade#create-special-key)」。

#### 如何避免常见错误：

  * 账户启用：请确认您的账户已启用杠杆交易，否则 API 调用将返回错误 {"code":-3003, "msg":"Margin account does not exist."}。
  * 错误处理：遇到错误 {"code":-2015, "msg":"Invalid API-key, IP, or permissions for action."}，通常表明您的 API 密钥权限不足，请检查 API 密钥设置。



### 充值杠杆交易账户

开始杠杆交易前，您需要为杠杆交易账户转入资产作为保证金。币安将现货钱包（交易账户）与杠杆交易钱包分开管理。使用全仓杠杆时，需要将资产转入全仓杠杆账户；使用逐仓杠杆时，则需转入该交易对的对应逐仓杠杆账户。

#### 全仓杠杆转账

用户可调用万向划转接口将资产转入全仓杠杆账户： [POST /sapi/v1/asset/transfer](/zh-CN/docs/catalog/core-trading-wallet/api/rest-api/asset#user-universal-transfer)

该接口使用参数 type 指示转账方向：

  * MAIN_MARGIN：从现货账户转入全仓杠杆账户
  * UMFUTURE_MARGIN：从 USDⓈ-M 合约账户转入全仓杠杆账户
  * CMFUTURE_MARGIN：从币本位合约账户转入全仓杠杆账户
  * FUNDING_MARGIN：从资金账户转入全仓杠杆账户
  * OPTION_MARGIN：从期权账户转入全仓杠杆账户



其他必填参数包括 asset（例如 "USDT"、"BTC"）、amount（转账数量，字符串格式）和 timestamp。请确保源账户拥有足够的对应资产可用来转账。

  * **请求参数** :

名称| 类型| 是否必需| 描述  
---|---|---|---  
type| ENUM| YES|   
asset| STRING| YES|   
amount| DECIMAL| YES|   
fromSymbol| STRING| NO|   
toSymbol| STRING| NO|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
#### 逐仓杠杆转账

对于逐仓账户，转账方向的类型如下：

  * MARGIN_ISOLATEDMARGIN：从全仓杠杆账户转入逐仓杠杆账户
  * ISOLATEDMARGIN_ISOLATEDMARGIN：从一个逐仓杠杆账户转入另一个逐仓杠杆账户



当转账方向为 ISOLATEDMARGIN_MARGIN 和 ISOLATEDMARGIN_ISOLATEDMARGIN 时，您需要明确指定转出和转入账户，额外需要参数 fromSymbol。

而当转账方向为 MARGIN_ISOLATEDMARGIN 和 ISOLATEDMARGIN_ISOLATEDMARGIN 时，则需要指定 toSymbol 参数。

转账成功后，系统会返回如下响应：

{ "tranId": 1234567890 }

该 tranId 可用于查询转账状态（通常成功响应即表示转账完成）。

资金成功转入杠杆交易账户后，您即可凭借保证金进行借贷，接下来您可以借入资金以执行杠杆交易。

#### 如何避免常见错误：

  * 抵押保证金不足：有时您的抵押抵押风险率过低，导致转出资金受限。此时会返回错误提示 {"code":-3020,"msg":"Transfer out amount exceeds max amount."}。请减少未偿还的借款或增加更多资产，以达到转账所需的抵押风险率。



### 借入资金

杠杆交易的核心功能之一是允许借入资金，以扩大您的持仓规模。在币安，只要您的杠杆交易账户中有足够保证金，且符合您设定的杠杆倍数，您就可以借入不同的资产。借款会按照小时计息，每种资产的最大可借额度取决于您的抵押价值及选择的杠杆倍数。

币安使用同一接口执行借款和还款操作： [POST /sapi/v1/margin/borrow-repay](/zh-CN/docs/catalog/core-trading-margin-trading/api/rest-api/borrow-repay#margin-account-borrow-repay)

#### 借款

您需要指定要借入的资产和借款数量。对于逐仓杠杆账户，需额外传入参数以指明具体逐仓账户。币安通过一个布尔参数 isolated 和一个 symbol 参数来区分逐仓账户。

  * **请求参数** :

名称| 类型| 是否必需| 描述  
---|---|---|---  
asset| STRING| YES|   
isIsolated| STRING| YES| 是否逐仓杠杆，TRUE, FALSE, 默认 FALSE  
symbol| STRING| YES| 逐仓交易对，配合逐仓使用  
amount| STRING| YES|   
type| STRING| YES| 操作类型：BORROW、REPAY  
recvWindow| LONG| NO| The value cannot be greater than 60000  
timestamp| LONG| YES|   
  
成功后，您将收到一条包含借款交易 ID 的 JSON 响应，例如：

{ "tranId": 1234567891 }

该 tranId 是借款交易的唯一标识，您后续可以通过它查询借款状态或历史。

借款成功后，借入的资金将记入对应的杠杆交易账户（增加该资产的“借入”余额），您即可使用这些资金进行交易。请注意，利息会从借款开始立即计收，直到借款还清为止。

#### 如何避免常见错误：

  * 最大可借额度：如果收到错误 {"code": -3006, "msg": "Your borrow amount has exceed maximum borrow amount."}，表示您申请借款的金额超过了限额。借款过多会令账户保证金低于要求，导致额外借款被拒。您可以通过接口 [GET /sapi/v1/margin/maxBorrowable](/zh-CN/docs/catalog/core-trading-margin-trading/api/rest-api/borrow-repay#query-max-borrow) 查询某资产（逐仓需指定 trading pair）最大可借额度，了解可借金额。
  * 利息：每笔借款都会计提利息，您可通过接口 [GET /sapi/v1/margin/interestHistory](/zh-CN/docs/catalog/core-trading-margin-trading/api/rest-api/borrow-repay#get-interest-history) 查询。利息通常从杠杆交易账户中扣除（计入该资产的“利息”字段）。还款时会先偿还利息，再偿还本金，请务必考虑利息成本。
  * 资产可借状态：并非所有资产随时可借。若流动性不足，币安可能对部分资产限制或暂停借贷。若提示资产不可借，建议查看接口 [GET /sapi/v1/margin/allAssets](/zh-CN/docs/catalog/core-trading-margin-trading/api/rest-api/market-data#get-all-margin-assets) 或稍后再试。
  * 资产不足：如果收到 {"code": -3045, "msg": "The system does not have enough asset now."} 错误，说明手动借款或自动借款的请求因系统可用资产不足被拒，原因包括：
    * 系统库存中可借资产低于请求借款金额。
    * 系统库存极低，不论借款额度大小，均拒绝借款。



建议密切关注系统状态，适时调整借款策略。

  * 全仓杠杆抵押品估值折扣：在全仓杠杆或全仓杠杆专业模式下，抵押资产在保证金计算时会按『抵押率」折算，资产分层折算后可能会降低总抵押价值。

请注意，逐仓杠杆不适用该规则，逐仓杠杆抵押风险率基于资产原值。

    * 全仓杠杆经典版以抵押风险率计算最大借款及最大转出额度，但保证金追缴和强制平仓仍以风险率为准。
    * 全仓杠杆专业模式的抵押风险率既用于计算最大借款和转出额度，也用于触发保证金追缴与强制平仓。



更多内容请参考[《如何计算全仓杠杆专业模式下的保证金水平》](https://www.binance.com/zh-CN/support/faq/detail/12a78d8aa813470f96be283b45f75410)。

  * 统一帐户抵押品估值折扣：在全仓杠杆、USDⓈ-M 合约及币本位合约钱包中所有资产的美元价值，均按统一帐户所规定的抵押率计算（不同于全仓杠杆经典版/全仓杠杆专业模式的抵押率）。抵押率可参考[《统一帐户专业版阶梯抵押率》](https://www.binance.com/zh-CN/futures/trading-rules/perpetual/portfolio-margin/tiered-collateral-ratio)。



成功借款后，借入的代币将转入您的杠杆交易钱包。接下来，我们将使用借入资金进行杠杆交易（买入或卖出）。

### 下单杠杆交易

凭借您杠杆交易账户內的资金（包括借入资金），您可以创建各种订单（限价单、市价单等）。币安提供专用杠杆交易订单接口： [POST /sapi/v1/margin/order](/zh-CN/docs/catalog/core-trading-margin-trading/api/rest-api/trade#margin-account-new-order)

  * **请求参数** :

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES|   
isIsolated| STRING| NO| 是否逐仓杠杆，"TRUE", "FALSE", 默认 "FALSE"  
side| ENUM| YES| BUY SELL  
type| ENUM| YES| 详见枚举定义：订单类型  
quantity| DECIMAL| NO|   
quoteOrderQty| DECIMAL| NO|   
price| DECIMAL| NO|   
stopPrice| DECIMAL| NO| 与STOP_LOSS, STOP_LOSS_LIMIT, TAKE_PROFIT, 和 TAKE_PROFIT_LIMIT 订单一起使用。  
newClientOrderId| STRING| NO| 客户自定义的唯一订单ID。若未发送自动生成。  
icebergQty| DECIMAL| NO| 与 LIMIT, STOP_LOSS_LIMIT, 和 TAKE_PROFIT_LIMIT 一起使用创建 iceberg 订单。  
newOrderRespType| ENUM| NO| 设置响应: JSON. ACK, RESULT, 或 FULL; MARKET 和 LIMIT 订单类型默认为 FULL, 所有其他订单默认为 ACK。  
sideEffectType| ENUM| NO| NO_SIDE_EFFECT, MARGIN_BUY, AUTO_REPAY,AUTO_BORROW_REPAY;默认为 NO_SIDE_EFFECT. 详见[FAQ](https://www.binance.com/zh-CN/support/faq/detail/f9fc51cda1984bf08b95e0d96c4570bc)  
timeInForce| ENUM| NO| GTC,IOC,FOK  
selfTradePreventionMode| ENUM| NO| 允许的 ENUM 取决于交易对的配置。支持的值有 EXPIRE_TAKER，EXPIRE_MAKER，EXPIRE_BOTH，NONE  
autoRepayAtCancel| BOOLEAN| NO| 只有在自动借款单或者自动借还单生效，true表示的是撤单后需要把订单产生的借款归还，默认为true  
recvWindow| LONG| NO| 赋值不能大于 60000  
timestamp| LONG| YES|   
  
如果您已经手动借入资金，您可以直接使用这些资金进行杠杆交易。如果您没有手动借款，币安的下单接口可以根据一个名为 sideEffectType 的参数自动为您借款或还款。

#### 自动借款

sideEffectType 参数允许您将借款或还款流程自动化，作为下单的一部分：

  * NO_SIDE_EFFECT：不自动借款或还款（默认设置）。您需保证杠杆交易账户余额充足（包括充值或之前手动借款），否则订单会因余额不足失败。
  * MARGIN_BUY：买入订单在报价资产不足时，将自动借款。如果您下买单时，杠杆交易账户报价资产不足，币安会自动借入所需的报价资产，最高不超杠杆限额。虽然该模式一般用于买单，但卖单若使用则会自动借入卖出资产（通常卖单不使用该模式，详见 AUTO_BORROW_REPAY）。借款仅在订单成交时触发，相当于“借入资产 + 下单”一步完成。
  * AUTO_REPAY：订单成交后自动还款。如果成交结果使您获得了借入资产，系统会立即用所得资产偿还贷款。例如，您借入 BTC 后卖出部分 BTC 取得报价资产，设置 AUTO_REPAY 后，会用报价资产转换为 BTC 还清 BTC 贷款。再如，借 USDT 买 BTC，卖 BTC 获得 USDT，设置 AUTO_REPAY 将用 USDT 还贷款。自动还款会优先还利息，且仅对借入资产生效，适合一键平仓。
  * AUTO_BORROW_REPAY：结合上述两种，即自动借款并自动还款模式。一键借入执行订单，成交后用所得资产还款，实质上是“保证金翻转”。例如无资产时，使用此模式买入，先借报价资产买入基础资产，然后若基础资产为需还资产则自动还款。此模式较复杂，某些多腿订单（如 OCO/OTOCO）不可用。



建议初学者先用 NO_SIDE_EFFECT（自行借款），或买单时使用 MARGIN_BUY 跳过手动借款步骤。执行后务必核查余额和借贷状况，确认自动化操作符合预期。

#### 如何避免常见错误：

  * 订单规则：保证金订单与现货订单遵循相同规则（最小交易量、价格步进、最小成交金额等）。请通过接口 [GET /api/v3/exchangeInfo](/zh-CN/docs/zh-CN/products/spot/rest-api) 查看最小/最大订单量，或通过 [GET /sapi/v1/margin/allAssets](/zh-CN/docs/catalog/core-trading-margin-trading/api/rest-api/market-data#get-all-margin-assets) 查询最小借还款金额。订单无效（如太小）将报错。
  * 取消订单：若需取消当前委托的订单，使用 [DELETE /sapi/v1/margin/order](/zh-CN/docs/catalog/core-trading-margin-trading/api/rest-api/trade#margin-account-cancel-order)，参数包括 symbol、orderId 或 newClientOrderId，逐仓单需额外 isIsolated=TRUE。也可调用 [DELETE /sapi/v1/margin/openOrders](/zh-CN/docs/catalog/core-trading-margin-trading/api/rest-api/trade#margin-account-cancel-all-open-orders-on-a-symbol) 一键撤销某交易对所有保证金订单。已自动借款的订单取消不会自动还款（除非为 OTOCO 订单设置 autoRepayAtCancel=true，此参数专为该场景设计）。
  * 限价价格限制：若遇错误 {“code”: -3064, “msg”: “Limit price needs to be within (-15%,15%) of current index price for this margin trading pair.”}，表示限价价格超出允许范围。部分低流动性交易对或稳定币对（如 USDT/DAI），限价价格必须保持在当前指数价格的±15%区间内（该区间可能会调整），请调整限价。



您已成功执行杠杆交易，接下来请持续监控杠杆交易账户状态以管控风险，因为行情不利时存在强制平仓风险。

### 监控杠杆交易账户

合理监控杠杆交易账户至关重要。您需要随时关注余额、抵押风险率（风险比例）及累计利息。币安提供接口查询全仓和逐仓杠杆账户详情。

#### 全仓杠杆账户详情

调用接口：[GET /sapi/v1/margin/account](/zh-CN/docs/catalog/core-trading-margin-trading/api/rest-api/account#query-cross-margin-account-details)，可获得全仓杠杆账户的概览，包括当前抵押风险率、资产总值、负债总值（债务）以及各资产的详细信息。关键返回字段包括：

{

"assets":[

{
    
    
    Code
    
    "baseAsset":
    
    {
    
      "asset": "BTC",
    
      "borrowEnabled": true,
    
      "borrowed": "0.00000000",
    
      "free": "0.00000000",
    
      "interest": "0.00000000",
    
      "locked": "0.00000000",
    
      "netAsset": "0.00000000",
    
      "netAssetOfBtc": "0.00000000",
    
      "repayEnabled": true,
    
      "totalAsset": "0.00000000"
    
    },
    
    "quoteAsset":
    
    {
    
      "asset": "USDT",
    
      "borrowEnabled": true,
    
      "borrowed": "0.00000000",
    
      "free": "0.00000000",
    
      "interest": "0.00000000",
    
      "locked": "0.00000000",
    
      "netAsset": "0.00000000",
    
      "netAssetOfBtc": "0.00000000",
    
      "repayEnabled": true,
    
      "totalAsset": "0.00000000"
    
    },
    
    "symbol": "BTCUSDT",
    
    "isolatedCreated": true,
    
    "enabled": true, // true-enabled, false-disabled
    
    "marginLevel": "0.00000000",
    
    "marginLevelStatus": "EXCESSIVE", // "EXCESSIVE", "NORMAL", "MARGIN\_CALL", "PRE\_LIQUIDATION", "FORCE\_LIQUIDATION"
    
    "marginRatio": "0.00000000",
    
    "indexPrice": "10000.00000000",
    
    "liquidatePrice": "1000.00000000",
    
    "liquidateRate": "1.00000000",
    
    "tradeEnabled": true

}

],

"totalAssetOfBtc": "0.00000000",

"totalLiabilityOfBtc": "0.00000000",

"totalNetAssetOfBtc": "0.00000000"

}

#### 逐仓杠杆账户详情

对于逐仓杠杆账户，有对应的接口： [GET /sapi/v1/margin/isolated/account](/zh-CN/docs/catalog/core-trading-margin-trading/api/rest-api/account#query-isolated-margin-account-info)。

该接口响应会返回您所有已启用的逐仓杠杆账户的详情信息。每个逐仓账户都会包含抵押风险率、总资产价值、总负债（借款）价值、以及该交易对相关的资产数组，通常包含两个资产的信息（即交易对的两个组成资产）。

这些信息帮助您全面了解每个逐仓杠杆账户的风险和资产状况。

{

"assets":[
    
    
    Code
    
    {
    
        "baseAsset":
    
        {
    
          "asset": "BTC",
    
          "borrowEnabled": true,
    
          "borrowed": "0.00000000",
    
          "free": "0.00000000",
    
          "interest": "0.00000000",
    
          "locked": "0.00000000",
    
          "netAsset": "0.00000000",
    
          "netAssetOfBtc": "0.00000000",
    
          "repayEnabled": true,
    
          "totalAsset": "0.00000000"
    
        },
    
        "quoteAsset":
    
        {
    
          "asset": "USDT",
    
          "borrowEnabled": true,
    
          "borrowed": "0.00000000",
    
          "free": "0.00000000",
    
          "interest": "0.00000000",
    
          "locked": "0.00000000",
    
          "netAsset": "0.00000000",
    
          "netAssetOfBtc": "0.00000000",
    
          "repayEnabled": true,
    
          "totalAsset": "0.00000000"
    
        },
    
        "symbol": "BTCUSDT",
    
        "isolatedCreated": true,
    
        "enabled": true, // true-enabled, false-disabled
    
        "marginLevel": "0.00000000",
    
        "marginLevelStatus": "EXCESSIVE", // "EXCESSIVE", "NORMAL", "MARGIN\_CALL", "PRE\_LIQUIDATION", "FORCE\_LIQUIDATION"
    
        "marginRatio": "0.00000000",
    
        "indexPrice": "10000.00000000",
    
        "liquidatePrice": "1000.00000000",
    
        "liquidateRate": "1.00000000",
    
        "tradeEnabled": true
    
      }
    
    ],
    
    "totalAssetOfBtc": "0.00000000",
    
    "totalLiabilityOfBtc": "0.00000000",
    
    "totalNetAssetOfBtc": "0.00000000"

}

#### 用户数据流（进阶）

币安为杠杆交易账户提供了 WebSocket 用户数据流服务，可实时推送账户余额变动和订单更新等信息。如果您需要实时监控（替代定时请求 REST 接口），可以通过调用接口 [POST /sapi/v1/userDataStream](/zh-CN/docs/zh-CN/products/margin-trading/trade-data-stream)（针对杠杆交易账户）创建一个 listenKey，然后订阅相关事件。数据流的使用较为进阶，但如果您需要即时接收保证金追缴通知或订单成交提醒，可考虑使用该功能。

在积极管理持仓后，您最终会需要平仓并偿还所借资金，下面介绍如何还款。

### 偿还借款

使用完借入的代币（例如平仓后），您可以归还保证金借款。还款后，借入的资产将返还给币安，同时释放对应抵押物。还款可以选择部分偿还或全部偿还。

币安采用同一接口执行借款和还款操作： [POST /sapi/v1/margin/borrow-repay](/zh-CN/docs/catalog/core-trading-margin-trading/api/rest-api/borrow-repay#margin-account-borrow-repay)

  * **请求参数** :

名称| 类型| 是否必需| 描述  
---|---|---|---  
asset| STRING| YES|   
isIsolated| STRING| YES| 是否逐仓杠杆，TRUE, FALSE, 默认 FALSE  
symbol| STRING| YES| 逐仓交易对，配合逐仓使用  
amount| STRING| YES|   
type| STRING| YES| 操作类型：BORROW、REPAY  
recvWindow| LONG| NO| The value cannot be greater than 60000  
timestamp| LONG| YES|   
  
还款成功后，您将收到包含借款交易 ID 的 JSON 响应，例如：

{ "tranId": 1234567894 }

这表示还款交易已成功完成。还款后，该资产的未偿贷款余额将减少相应还款金额；如果全部还清，该资产的利息会降至零。

覆盖了借款与还款流程后，您基本完成了杠杆交易的整个生命周期：资金入账 -> 借款 -> 交易 -> （可选：再次交易）-> 还款。最后一步是持续跟踪您当下的交易和交易历史。

### 审查交易和账户历史

审查杠杆交易和账户活动非常重要，有助于了解交易表现和进行账务记录，也便于调试您的交易机器人。币安提供接口查询过去的订单、成交和账户相关操作（转账、借款、还款等）。

#### 成交历史

要获取杠杆交易账户上的成交记录（成交回执），请调用接口： [GET /sapi/v1/margin/myTrades](/zh-CN/docs/catalog/core-trading-margin-trading/api/rest-api/trade#query-margin-accounts-trade-list)

  * **请求参数** :

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES|   
isIsolated| STRING| NO| 无论是否使用逐仓保证金，该参数支持设置为 "TRUE" 或 "FALSE"，默认值为 "FALSE"。  
orderId| LONG| NO|   
startTime| LONG| NO|   
endTime| LONG| NO|   
fromId| LONG| NO| 用于查询指定的起始 TradeId 交易记录，默认情况下接口会返回最新的交易。  
limit| INT| NO| 默认值为 500；最大值为 1000。  
recvWindow| LONG| NO| 此参数的取值不能超过 60000。  
timestamp| LONG| YES|   
  
举例来说，若您之前购买过 BNB，在查询 BNBBTC 交易对的成交记录（调用 myTrades）时，您可能会获得如下示例返回内容：

[ { "commission": "0.00006000", "commissionAsset": "BTC", "id": 34, "isBestMatch": true, "isBuyer": false, "isMaker": false, "orderId": 39324, "price": "0.02000000", "qty": "3.00000000", "symbol": "BNBBTC", "isIsolated": false, "time": 1561973357171 } ]

#### 订单历史

如果您需要查看订单详情（包括未成交的订单，如已取消的订单），可以使用以下接口：

  * [GET /sapi/v1/margin/allOrders](/zh-CN/docs/catalog/core-trading-margin-trading/api/rest-api/trade#query-margin-accounts-all-orders) — 查询某交易对所有订单（已成交、已取消等）。
  * [GET /sapi/v1/margin/openOrders](/zh-CN/docs/catalog/core-trading-margin-trading/api/rest-api/trade#query-margin-accounts-open-orders) — 查询当前开放订单（类似现货交易）。
  * [GET /sapi/v1/margin/order](/zh-CN/docs/catalog/core-trading-margin-trading/api/rest-api/trade#query-margin-accounts-order) — 通过订单 ID 查询指定订单详情。



#### 账户活动历史

币安还提供以下接口用于查看其他账户活动：

  * [GET /sapi/v1/margin/borrow-repay](/zh-CN/docs/catalog/core-trading-margin-trading/api/rest-api/borrow-repay#query-borrow-repay-records-in-margin-account) — 查询借贷和还款历史。支持按资产、逐仓交易对等过滤。返回每笔借款和还款记录，包括金额、利息、状态等，例如显示您某次借入 100 USDC 的交易 ID 和时间戳。
  * [GET /sapi/v1/margin/transfer](/zh-CN/docs/catalog/core-trading-margin-trading/api/rest-api/transfer#get-cross-margin-transfer-history) — 查询现货与全仓杠杆交易账户间的转账历史，包括充值和提现，带时间戳和金额信息。
  * [GET /sapi/v1/margin/interestHistory](/zh-CN/docs/catalog/core-trading-margin-trading/api/rest-api/borrow-repay#get-interest-history) — 按资产列出一段时间内的利息计提记录。
  * [GET /sapi/v1/margin/forceLiquidationRec](/zh-CN/docs/catalog/core-trading-margin-trading/api/rest-api/trade#get-force-liquidation-record) — 强制平仓记录（希望您不需要用到！）。



此页面是否有帮助？

Last modified on November 12, 2026

[错误代码](/zh-CN/docs/products/margin-trading/error-code)[概述](/zh-CN/docs/products/wallet/Introduction)