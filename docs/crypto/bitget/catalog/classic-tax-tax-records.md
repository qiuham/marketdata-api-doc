---
exchange: bitget
source_url: https://www.bitget.com/docs/catalog/classic-tax-tax-records
api_type: REST
updated_at: 2026-11-18 19:01:25.430784
---

# Classic Tax API

Classic account — futures / margin / P2P / spot transaction records.

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `GET /api/v2/tax/spot-record` — Spot Transaction Records
- `GET /api/v2/tax/future-record` — Futures Transaction Records
- `GET /api/v2/tax/margin-record` — Margin Transaction History
- `GET /api/v2/tax/p2p-record` — P2P Transaction Records

## Spot Transaction Records

`GET /api/v2/tax/spot-record`

Frequency limit: 1 times/1s (User ID)

Spot transaction records

Operation ID: `classicTaxGetSpotAccountRecord`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string |  | Default all coin type |
| startTime | query | string | 是 | Start time, Unix millisecond timestamps |
| endTime | query | string | 是 | End time, Unix millisecond timestamps<br><br>The maximum interval between startTime and endTime is 30 days. |
| limit | query | string |  | Default: 500, maximum: 500 |
| idLessThan | query | string |  | The last recorded ID |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].id | string |  | Record ID |
| data[].coin | string |  | Coin |
| data[].spotTaxType | string |  | tax type spot<br><br>Deposit<br><br>Withdrawal<br><br>User fees<br><br>Fiat withdrawal success - Deduct<br><br>Sell<br><br>Buy<br><br>Transaction fee deduct<br><br>Strategic purchase-user accounts<br><br>Subscribe to trader-user accounts<br><br>System charges fees<br><br>Strategic refund-User account<br><br>Subscription fee refund-user account<br><br>Strategic Income-Traders' accounts<br><br>Crypto Voucher Distribution<br><br>Copy Trade expense<br><br>Judicial recall<br><br>Copy Trade profit<br><br>Refund Copy Trade commission<br><br>Buy Crypto<br><br>Deduction of judicial recall<br><br>Buy with card<br><br>Airdrop Reward-B<br><br>Decrease due to ETF settlement<br><br>Increase due to ETF settlement<br><br>System lock-up<br><br>User lock-up<br><br>Trading fee rebate<br><br>Manage background lock positions<br><br>Automatic deposit<br><br>Automatic withdrawal<br><br>Deposit from strategy account<br><br>Withdraw to strategy account<br><br>Lotto rewards<br><br>User contract trial fund<br><br>User contract simulation fund<br><br>Delegate<br><br>Undelegate<br><br>un_delegate_user_out<br><br>delegate_user_account_in<br><br>delegate_user_account_out<br><br>settle_user_account_receive_in<br><br>delegate_user_account_payable_out<br><br>Rebate rewards<br><br>Consumption<br><br>Gains<br><br>Unlock locked order<br><br>Deduction<br><br>Return<br><br>Release<br><br>Repayment<br><br>Forced liquidation return<br><br>The locked order is returned to the system<br><br>Failed<br><br>Withdrawal frozen<br><br>Mirror fund<br><br>Supplement fund<br><br>Reduce fund<br><br>Settlement out<br><br>Withdrawal unfreeze<br><br>Ordinary Withdrawal<br><br>Fast withdrawal fee<br><br>Airdrop Reward-A<br><br>Subscribe<br><br>Interest<br><br>Penalty<br><br>Redemption<br><br>Activity fund(USDT-Ⓜ)<br><br>Activity fund<br><br>Activity fund(Coin-Ⓜ)<br><br>Increase exchange rate<br><br>Reduce exchange rate<br><br>Transfer in<br><br>Activity issuance<br><br>Transfer out<br><br>Super account<br><br>Exchange spending<br><br>Exchange income<br><br>Sent<br><br>Received<br><br>MegaSwap Transfer in<br><br>MegaSwap Transfer out<br><br>Channel referral rewards<br><br>System account<br><br>Sell Crypto<br><br>Fiat deposit |
| data[].amount | string |  | Quantity |
| data[].fee | string |  | Transaction fee |
| data[].balance | string |  | Total accounts |
| data[].ts | string |  | When this record was generated Timestamp |
| data[].bizOrderId | string |  | Business order number |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1687257612262,
  "data": [
    {
      "id": "1",
      "coin": "AIBB",
      "spotTaxType": "Interest",
      "amount": "6018333.33333333",
      "fee": "0",
      "balance": "468575833.33333306",
      "bizOrderId": "1333333333333333333",
      "ts": "1686128884851"
    }
  ]
}
```

## Futures Transaction Records

`GET /api/v2/tax/future-record`

Frequency limit: 1 times/1s (User ID)

Futures transaction records

Operation ID: `classicTaxGetFutureAccountRecord`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| productType | query | string |  | Product type default `USDT-FUTURES`<br><br>`USDT-FUTURES` USDT-M Futures<br><br>`COIN-FUTURES` Coin-M Futures<br><br>`USDC-FUTURES` USDC-M Futures |
| marginCoin | query | string |  | Default all margin coin |
| startTime | query | string | 是 | Start time (time stamp in milliseconds) |
| endTime | query | string | 是 | The maximum interval between startTime and endTime (time stamp in milliseconds) is 30 days. |
| limit | query | string |  | Default: 500, maximum: 500 |
| idLessThan | query | string |  | The last recorded ID |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].id | string |  | Transaction history ID |
| data[].symbol | string |  | symbol |
| data[].marginCoin | string |  | margin Coin |
| data[].futureTaxType | string |  | Futures transaction type<br><br>TRANSFER_IN Fund transfer<br><br>TRANSFER_OUT Fund transfer<br><br>ORDER_DEALT_FROZEN_OUT Order dealt fund out<br><br>ORDER_DEALT_IN Order dealt fund in<br><br>ORDER_PLF_FEE_OUT handling fee deduction<br><br>EXCHANGE_SOURCE_TOKEN_USER_OUT Redeem<br><br>EXCHANGE_TARGET_TOKEN_USER_IN Redeem<br><br>OPEN_LONG Open long<br><br>OPEN_SHORT Open short<br><br>BUY_DEAL Buy<br><br>SELL_DEAL Sell<br><br>CLOSE_LONG Close long<br><br>CLOSE_SHORT Close short<br><br>FORCE_CLOSE_LONG Forced reduction of long position<br><br>FORCE_CLOSE_SHORT Forced reduction of short position<br><br>BURST_CLOSE_LONG Liquidate long position<br><br>BURST_CLOSE_SHORT Liquidate short position<br><br>OFFSET_REDUCE_CLOSE_LONG Offset close long<br><br>OFFSET_REDUCE_CLOSE_SHORT Offset close short<br><br>FORCE_BUY_SSM Forced buy<br><br>FORCE_SELL_SSM Forced sell<br><br>BURST_BUY_SSM Liquidate buy<br><br>BURST_SELL_SSM Liquidate sell<br><br>RISK_LIQ_USER_IN User money in due to liquidation risk<br><br>RISK_LIQ_USER_OUT User money out due to liquidation risk<br><br>INTEREST_SETTLEMENT_OUT Interest deduction<br><br>CONTRACT_MAIN_SETTLE_FEE_USER_IN Funding fee collection<br><br>CONTRACT_MAIN_SETTLE_FEE_USER_OUT Funding Fee deduction |
| data[].amount | string |  | Quantity |
| data[].fee | string |  | Transaction fee |
| data[].ts | string |  | When this record was generated, millisecond timestamp |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1687257612262,
  "data": [
    {
      "id": "1",
      "symbol": "TRXUSDT",
      "marginCoin": "USDT",
      "futureTaxType": "close_long",
      "amount": "0.10545",
      "fee": "-0.02134863",
      "ts": "1679909309766"
    }
  ]
}
```

## Margin Transaction History

`GET /api/v2/tax/margin-record`

Frequency limit: 1 times/1s (User ID)

Margin transaction records

Operation ID: `classicTaxGetMarginAccountRecord`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| marginType | query | string |  | Leverage type <br><br>`isolated`: Isolated margin<br><br>`crossed`: Cross margin(default) |
| coin | query | string |  | Default all coin type |
| startTime | query | string | 是 | Start time (time stamp in milliseconds) |
| endTime | query | string | 是 | The maximum interval between startTime and endTime (time stamp in milliseconds) is 30 days. |
| limit | query | string |  | Default: 500, maximum: 500 |
| idLessThan | query | string |  | The last recorded ID |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].id | string |  | Record id |
| data[].coin | string |  | Coin |
| data[].symbol | string |  | Trade pair |
| data[].marginTaxType | string |  | transfer_in: Inbound transfer<br><br>transfer_out: Outbound transfer<br><br>borrow: Borrowings<br><br>repay: Repayment<br><br>liquidation_fee: Liquidation fee<br><br>compensate: Risk fund compensation for collateral shortfall<br><br>deal_in: Margin buy<br><br>deal_out: Margin sell<br><br>interest_repay: Interest repayment<br><br>confiscated: Deducted for collateral shortfall<br><br>exchange_in: Conversion profit<br><br>exchange_out: Conversion profit |
| data[].amount | string |  | Quantity |
| data[].fee | string |  | Transaction fee |
| data[].total | string |  | Total accounts |
| data[].ts | string |  | Record generation time, Unix millisecond timestamps |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1687259242290,
  "data": [
    {
      "id": "1",
      "coin": "USDT",
      "marginTaxType": "transfer_in",
      "amount": "13333",
      "fee": "0",
      "total": "13333",
      "symbol": "BTCUSDT",
      "ts": "1686129284474"
    }
  ]
}
```

## P2P Transaction Records

`GET /api/v2/tax/p2p-record`

Frequency limit: 1 times/1s (User ID)

p2p transaction records

Operation ID: `classicTaxGetP2PAccountRecord`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string |  | Default all coin type |
| startTime | query | string | 是 | Start time (time stamp in milliseconds) |
| endTime | query | string | 是 | The maximum interval between startTime and endTime (time stamp in milliseconds) is 30 days. |
| limit | query | string |  | Default: 500, maximum: 500 |
| idLessThan | query | string |  | The last recorded ID |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].id | string |  | Record id lastEndId |
| data[].coin | string |  | Coin |
| data[].p2pTaxType | string |  | p2p taxation types<br><br>transfer_in Inbound transfer<br><br>transfer_out Outbound transfer<br><br>sell Sell<br><br>buy Buy |
| data[].balance | string |  | Quantity |
| data[].ts | string |  | Record generation time, Unix millisecond timestamp |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1687260620793,
  "data": [
    {
      "id": "152526631",
      "coin": "USDT",
      "p2pTaxType": "transfer-in",
      "balance": "1",
      "ts": "1755846320684"
    }
  ]
}
```


---

经典账户 — 合约、杠杆、P2P 与现货交易记录。

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `GET /api/v2/tax/future-record` — 合约财务记录
- `GET /api/v2/tax/margin-record` — 杠杆财务记录
- `GET /api/v2/tax/spot-record` — 现货财务记录
- `GET /api/v2/tax/p2p-record` — P2P财务记录

## 合约财务记录

`GET /api/v2/tax/future-record`

限速规则 1次/1s (UID)

合约财务记录

Operation ID: `classicTaxGetFutureAccountRecord`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| productType | query | string |  | 产品类型, 默认`USDT-FUTURES`<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |
| marginCoin | query | string |  | 默认全部保证金币种 |
| startTime | query | string | 是 | 开始时间 (时间戳毫秒) |
| endTime | query | string | 是 | 结束时间 (时间戳毫秒) 与 startTime 最大范围30天 |
| limit | query | string |  | 默认500 最大500 |
| idLessThan | query | string |  | 最后一条记录的ID |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].id | string |  | 财务记录ID |
| data[].symbol | string |  | 交易对 |
| data[].marginCoin | string |  | 保证金币种 |
| data[].futureTaxType | string |  | 合约财务类型<br><br>TRANSFER_IN 资金转入<br><br>TRANSFER_OUT 资金转出<br><br>ORDER_DEALT_FROZEN_OUT 卖出<br><br>ORDER_DEALT_IN 买入<br><br>ORDER_PLF_FEE_OUT 手续费抵扣<br><br>EXCHANGE_SOURCE_TOKEN_USER_OUT 兑出<br><br>EXCHANGE_TARGET_TOKEN_USER_IN 兑入<br><br>OPEN_LONG 开多<br><br>OPEN_SHORT 开空<br><br>BUY_DEAL 买多<br><br>SELL_DEAL 卖空<br><br>CLOSE_LONG 平多<br><br>CLOSE_SHORT 平空<br><br>FORCE_CLOSE_LONG 强制减多<br><br>FORCE_CLOSE_SHORT 强制减空<br><br>BURST_CLOSE_LONG 爆仓平多<br><br>BURST_CLOSE_SHORT 爆仓平空<br><br>OFFSET_REDUCE_CLOSE_LONG 扎差减多<br><br>OFFSET_REDUCE_CLOSE_SHORT 扎差减空<br><br>FORCE_BUY_SSM 强制买入<br><br>FORCE_SELL_SSM 强制卖出<br><br>BURST_BUY_SSM 爆仓买入<br><br>BURST_SELL_SSM 爆仓卖出<br><br>RISK_LIQ_USER_IN 清算还款<br><br>INTEREST_SETTLEMENT_OUT 扣息<br><br>CONTRACT_MAIN_SETTLE_FEE_USER_IN 资金费用收取<br><br>CONTRACT_MAIN_SETTLE_FEE_USER_OUT 资金费用扣除<br><br>RISK_LIQ_USER_OUT 负债清算转出 |
| data[].amount | string |  | 数量 |
| data[].fee | string |  | 手续费 |
| data[].ts | string |  | 该记录产生时间，毫秒时间戳 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1687257612262,
  "data": [
    {
      "id": "1",
      "symbol": "TRXUSDT",
      "marginCoin": "USDT",
      "futureTaxType": "close_long",
      "amount": "0.10545",
      "fee": "-0.02134863",
      "ts": "1679909309766"
    }
  ]
}
```

## 杠杆财务记录

`GET /api/v2/tax/margin-record`

限速规则 1次/1s (UID)

杠杆财务记录

Operation ID: `classicTaxGetMarginAccountRecord`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| marginType | query | string |  | 杠杆类型 <br><br>`isolated`：逐仓<br><br>`crossed`：全仓(默认) |
| coin | query | string |  | 默认全部币种 |
| startTime | query | string | 是 | 开始时间(时间戳毫秒) |
| endTime | query | string | 是 | 结束时间 (时间戳毫秒) 与 startTime 最大范围30天 |
| limit | query | string |  | 默认500 最大500 |
| idLessThan | query | string |  | 最后一条记录的ID |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].id | string |  | 记录id |
| data[].coin | string |  | 币种 |
| data[].symbol | string |  | 交易对 |
| data[].marginTaxType | string |  | transfer_in 账户转入<br><br>transfer_out账户转出<br><br>borrow借款<br><br>repay 还款<br><br>liquidation_fee爆仓清算费<br><br>compensate风险基金穿仓补偿<br><br>deal_in 杠杆 成交入帐 买入<br><br>deal_out杠杆 成交扣除 卖出<br><br>interest_repay归还利息<br><br>confiscated穿仓扣除<br><br>exchange_in兑换收入<br><br>exchange_out兑换支出 |
| data[].amount | string |  | 数量 |
| data[].fee | string |  | 手续费 |
| data[].total | string |  | 账户总额 |
| data[].ts | string |  | 记录产生时间, Unix毫秒时间戳 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1687259242290,
  "data": [
    {
      "id": "1",
      "coin": "USDT",
      "marginTaxType": "transfer_in",
      "amount": "13333",
      "fee": "0",
      "total": "13333",
      "symbol": "BTCUSDT",
      "ts": "1686129284474"
    }
  ]
}
```

## 现货财务记录

`GET /api/v2/tax/spot-record`

限速规则 1次/1s (UID)

现货财务记录

Operation ID: `classicTaxGetSpotAccountRecord`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string |  | 币种默认全部 |
| startTime | query | string | 是 | 开始时间，Unix毫秒时间戳 |
| endTime | query | string | 是 | 结束时间，Unix毫秒时间戳<br><br>startTime与endTime的间隔最大为30天 |
| limit | query | string |  | 默认500 最大500 |
| idLessThan | query | string |  | 最后一条记录的ID |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].id | string |  | 记录ID |
| data[].coin | string |  | 币种 |
| data[].spotTaxType | string |  | 现货财务类型<br><br>Deposit<br><br>Withdrawal<br><br>User fees<br><br>Fiat withdrawal success - Deduct<br><br>Sell<br><br>Buy<br><br>Transaction fee deduct<br><br>Strategic purchase-user accounts<br><br>Subscribe to trader-user accounts<br><br>System charges fees<br><br>Strategic refund-User account<br><br>Subscription fee refund-user account<br><br>Strategic Income-Traders' accounts<br><br>Crypto Voucher Distribution<br><br>Copy Trade expense<br><br>Judicial recall<br><br>Copy Trade profit<br><br>Refund Copy Trade commission<br><br>Buy Crypto<br><br>Deduction of judicial recall<br><br>Buy with card<br><br>Airdrop Reward-B<br><br>Decrease due to ETF settlement<br><br>Increase due to ETF settlement<br><br>System lock-up<br><br>User lock-up<br><br>Trading fee rebate<br><br>Manage background lock positions<br><br>Automatic deposit<br><br>Automatic withdrawal<br><br>Deposit from strategy account<br><br>Withdraw to strategy account<br><br>Lotto rewards<br><br>User contract trial fund<br><br>User contract simulation fund<br><br>Delegate<br><br>Undelegate<br><br>un_delegate_user_out<br><br>delegate_user_account_in<br><br>delegate_user_account_out<br><br>settle_user_account_receive_in<br><br>delegate_user_account_payable_out<br><br>Rebate rewards<br><br>Consumption<br><br>Gains<br><br>Unlock locked order<br><br>Deduction<br><br>Return<br><br>Release<br><br>Repayment<br><br>Forced liquidation return<br><br>The locked order is returned to the system<br><br>Failed<br><br>Withdrawal frozen<br><br>Mirror fund<br><br>Supplement fund<br><br>Reduce fund<br><br>Settlement out<br><br>Withdrawal unfreeze<br><br>Ordinary Withdrawal<br><br>Fast withdrawal fee<br><br>Airdrop Reward-A<br><br>Subscribe<br><br>Interest<br><br>Penalty<br><br>Redemption<br><br>Activity fund(USDT-Ⓜ)<br><br>Activity fund<br><br>Activity fund(Coin-Ⓜ)<br><br>Increase exchange rate<br><br>Reduce exchange rate<br><br>Transfer in<br><br>Activity issuance<br><br>Transfer out<br><br>Super account<br><br>Exchange spending<br><br>Exchange income<br><br>Sent<br><br>Received<br><br>MegaSwap Transfer in<br><br>MegaSwap Transfer out<br><br>Channel referral rewards<br><br>System account<br><br>Sell Crypto<br><br>Fiat deposit |
| data[].amount | string |  | 数量 |
| data[].fee | string |  | 手续费 |
| data[].balance | string |  | 账户总额 |
| data[].ts | string |  | 该记录产生时间 时间戳 |
| data[].bizOrderId | string |  | 业务订单编号 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1687257612262,
  "data": [
    {
      "id": "1",
      "coin": "AIBB",
      "spotTaxType": "Interest",
      "amount": "6018333.33333333",
      "fee": "0",
      "balance": "468575833.33333306",
      "bizOrderId": "1333333333333333333",
      "ts": "1686128884851"
    }
  ]
}
```

## P2P财务记录

`GET /api/v2/tax/p2p-record`

限速规则 1次/1s (UID)

p2p财务记录

Operation ID: `classicTaxGetP2PAccountRecord`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| coin | query | string |  | 币种默认全部币种 |
| startTime | query | string | 是 | 开始时间 (时间戳毫秒) |
| endTime | query | string | 是 | 结束时间 (时间戳毫秒) 与 startTime 最大范围30天 |
| limit | query | string |  | 默认500 最大500 |
| idLessThan | query | string |  | 最后一条记录的ID |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].id | string |  | 记录id lastEndId |
| data[].coin | string |  | 币种 |
| data[].p2pTaxType | string |  | p2p税务类型<br><br>transfer_in 账户转入<br><br>transfer_out 账户转出<br><br>sell卖出<br><br>buy买入 |
| data[].balance | string |  | 数量 |
| data[].ts | string |  | 记录产生时间, Unix毫秒时间戳 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1687260620793,
  "data": [
    {
      "id": "152526631",
      "coin": "USDT",
      "p2pTaxType": "transfer-in",
      "balance": "1",
      "ts": "1755846320684"
    }
  ]
}
```