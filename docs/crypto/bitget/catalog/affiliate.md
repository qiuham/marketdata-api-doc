---
exchange: bitget
source_url: https://www.bitget.com/docs/catalog/affiliate
api_type: REST
updated_at: 2026-11-25 19:02:24.356617
---

# Affiliate

Affiliate customer list, assets, trade volume, deposit, KYC result and commission query APIs.

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `GET /api/v3/affiliate/customer-list` — Get Agent Customer List
- `GET /api/v3/affiliate/customer-asset` — Get Agent Customer Asset
- `GET /api/v3/affiliate/customer-trade-volume` — Get Agent Customer Trade Volume
- `GET /api/v3/affiliate/customer-deposit` — Get Agent Customer Deposit
- `GET /api/v3/affiliate/customer-kyc-result` — Get Agent Customer Kyc Result
- `GET /api/v3/affiliate/customer-commission` — Get Agent Customer Commission
- `GET /api/v3/affiliate/sub-customer-list` — Get Agent Sub Customer List
- `GET /api/v3/affiliate/sub-affiliate-info` — Get Sub Affiliate Info
- `GET /api/v3/affiliate/sub-affiliate-commission` — Get Sub Affiliate Commission

## Get Agent Customer List

`GET /api/v3/affiliate/customer-list`

Rate limit: 10/sec/UID

`startTime` and `endTime` should be both set or both left blank

`startTime` and `endTime` should be within 30days

If `startTime` / `endTime` are not set, all registered clients will be returned with no time restriction.

It supports querying clients registered at any time, with no 90-day restriction.

If you want to confirm whether a specific UID is your referral client you invited, you can verify it by passing the `uid` query parameter, for example: `uid=123456`.

The data is updated in real time

Operation ID: `affiliateGetCustomerList`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| startTime | query | string |  | Start time (ms) |
| endTime | query | string |  | End time (ms) |
| pageNo | query | string |  | Page number |
| pageSize | query | string |  | Page size, 100 default, Max 1000 |
| uid | query | string |  | UID |
| referralCode | query | string |  | Referral code |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].uid | string |  | UID |
| data[].registerTime | string |  | Register time |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695785738672,
  "data": [
    {
      "uid": 1235665663,
      "registerTime": "1679991960110"
    },
    {
      "uid": 1235665663,
      "registerTime": "1679991960110"
    }
  ]
}
```

## Get Agent Customer Asset

`GET /api/v3/affiliate/customer-asset`

Rate limit: 10/sec/UID

Data update frequency: 10 minutes

Operation ID: `affiliateGetCustomerAsset`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| pageNo | query | string |  | Page number |
| pageSize | query | string |  | Page size, 100 default, Max 500 |
| uid | query | string |  | UID |
| showSub | query | string |  | Whether to Display Subordinate User Information of Direct Clients <br><br>`yes`: Yes <br><br>`no`: No |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].uid | string |  | UID |
| data[].balance | string |  | Account Balance |
| data[].uTime | string |  | Account Last update Time |
| data[].remark | string |  | When the user has too many sub-accounts, it prompts that there are too many sub-accounts and the account balance cannot be queried |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 163123213132,
  "data": [
    {
      "balance": "1234",
      "uid": "23423432",
      "uTime": "23423423423",
      "remark": "sub account exceed 5"
    }
  ]
}
```

## Get Agent Customer Trade Volume

`GET /api/v3/affiliate/customer-trade-volume`

Rate limit: 10/sec/UID

This API response includes the trading volume for both spot and futures

startTime and endTime should be both set or both left blank

startTime and endTime should be within 30days

This API endpoint can only query the data in 90 days. If you need older data, please contact BD to export it manually.

It will return yesterday's data (00:00-23:59 UTC+8) by default if there is no startTime/endTime set.

Data update frequency: 1 hour

Operation ID: `affiliateGetCustomerTradeVolume`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| startTime | query | string |  | Start time (ms) |
| endTime | query | string |  | End time (ms) |
| pageNo | query | string |  | Page number |
| pageSize | query | string |  | Page size, 100 default, Max 1000 |
| uid | query | string |  | UID |
| showSub | query | string |  | Whether to show sub-customer information <br><br>`yes`: Show <br><br>`no`: Do not show |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].uid | string |  | UID |
| data[].volumn | string |  | Trade volume |
| data[].spotVolume | string |  | Spot trade volume |
| data[].futuresVolume | string |  | Futures trade volume |
| data[].time | string |  | Timestamp(ms) |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 163123213132,
  "data": [
    {
      "uid": "435435345",
      "volumn": "34234.4",
      "spotVolume": "12000.0",
      "futuresVolume": "22234.4",
      "time": "1679991960110"
    },
    {
      "uid": "435435345",
      "volumn": "34234.4",
      "spotVolume": "12000.0",
      "futuresVolume": "22234.4",
      "time": "1679991960110"
    }
  ]
}
```

## Get Agent Customer Deposit

`GET /api/v3/affiliate/customer-deposit`

Rate limit: 10/sec/UID

The API response includes the user's on-chain deposits and internal transfers

startTime and endTime should be both set or both left blank

startTime and endTime should be within 30days

This API endpoint can only query the data in 90 days. If you need older data, please contact BD to export it manually.

It will return yesterday's data (00:00-23:59 UTC+8) by default if there is no startTime/endTime set.

The data is updated in real time

Operation ID: `affiliateGetCustomerDeposit`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| startTime | query | string |  | Start time (ms) |
| endTime | query | string |  | End time (ms) |
| pageNo | query | string |  | Page number |
| pageSize | query | string |  | Page size, 100 default, Max 1000 |
| uid | query | string |  | UID |
| showSub | query | string |  | Whether to Display Subordinate User Information of Direct Clients <br><br>`yes`: Yes <br><br>`no`: No |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].uid | string |  | UID |
| data[].orderId | string |  | Deposit Order ID |
| data[].depositTime | string |  | Deposit Time (ms) |
| data[].depositCoin | string |  | Deposit Coin |
| data[].depositAmount | string |  | Deposit Amount |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 163123213132,
  "data": [
    {
      "orderId": "3423423",
      "uid": "234342343",
      "depositTime": "11234342343",
      "depositCoin": "USDT",
      "depositAmount": "500"
    }
  ]
}
```

## Get Agent Customer Kyc Result

`GET /api/v3/affiliate/customer-kyc-result`

Rate limit: 10/sec/UID

startTime and endTime should be both set or both left blank

It will return yesterday's KYC or KYB data(00:00-23:59UTC+8) by default if there is no startTime/endTimeset.

Data update frequency: 5 minutes

Operation ID: `affiliateGetCustomerKycResult`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| startTime | query | string |  | Start time, maximum range of 90 days |
| endTime | query | string |  | End time, maximum range of 90 days. |
| cursor | query | string |  | Cursor ID<br><br>Used for pagination. Omit it on the first call. For subsequent calls, pass in the last `endId` returned by the previous query. |
| limit | query | string |  | Limit number of data(default 100,max 1000) |
| uid | query | string |  | UID |
| showSub | query | string |  | Whether to Display Subordinate User Information of Direct Clients  <br><br>`yes`: Yes <br><br>`no`: No |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.uid | string |  | UID |
| data.kycResult | string |  | KYC or KYB result<br><br>`passed`<br><br> `not_passed` |
| data.endId | string |  | The last userID on the page |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 163123213132,
  "data": {
    "userList": [
      {
        "uid": "435435345",
        "kycResult": "passed"
      }
    ],
    "endId": "435435345"
  }
}
```

## Get Agent Customer Commission

`GET /api/v3/affiliate/customer-commission`

Rate limit: 10/sec/UID

startTime and endTime should be both set or both left blank

This API endpoint can only query the data in 90 days. If you need older data, please contact BD to export it manually.

It will return yesterday's data (00:00-23:59 UTC+8) by default if there is no startTime/endTime set.

Data update frequency: T+1 (UTC+8)

Operation ID: `affiliateGetCustomerCommission`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| startTime | query | string |  | Start time, maximum range of 30 days |
| endTime | query | string |  | End time, maximum range of 30 days. |
| cursor | query | string |  | Cursor ID<br><br>Used for pagination. Omit it on the first call. For subsequent calls, pass in the last `endId` returned by the previous query. |
| limit | query | string |  | Limit number of data(default 100,max 1000) |
| uid | query | string |  | UID |
| coin | query | string |  | Coin, e.g: BTC |
| symbol | query | string |  | Symbol e.g：<br><br> BGBUSDT_SPBL `spot`<br><br> BTCUSDT_SPBL-MABL `spot margin`<br><br> BTCUSDT_UMCBL `USDT-Futures` <br><br>BTCUSD_DMCBL  `COIN-Futures` <br><br>BTCPERP_CMCBL `USDC-Futures` |
| showSub | query | string |  | Whether to Display Subordinate User Information of Direct Clients  <br><br>`yes`: Yes <br><br>`no`: No |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.commissionList | object[] |  | Commission List |
| data.commissionList[].uid | string |  | Referred User UID |
| data.commissionList[].date | string |  | Commission return date (UTC+8) |
| data.commissionList[].coin | string |  | coin |
| data.commissionList[].symbol | string |  | symbol |
| data.commissionList[].productType | string |  | Product type <br><br> `SPOT` Spot trading <br><br> `MARGIN` Margin trading <br><br> `USDT-FUTURES` USDT futures <br><br> `COIN-FUTURES` Coin-M futures <br><br> `USDC-FUTURES` USDC futures |
| data.commissionList[].dealAmount | string |  | Trading amount(maker+taker) |
| data.commissionList[].fee | string |  | Trading fee(maker+taker)<br><br>The commission and fee amounts are denominated in the coin currency |
| data.commissionList[].feeDeduction | string |  | Trading fee deducted(maker+taker) |
| data.commissionList[].activityBonusDeduct | string |  | Fees offset by experience funds |
| data.commissionList[].spotCouponDeduct | string |  | Fees offset by spot cashback coupons |
| data.commissionList[].futuresCouponDeduct | string |  | Fees offset by contract airdrop coupons |
| data.commissionList[].spotFeeDiscountDeduct | string |  | Fees reduced by spot fee discounts |
| data.commissionList[].negativeMakerFeeDeduct | string |  | Fees offset by negative maker fees |
| data.commissionList[].feePaid | string |  | Fees actually paid(maker+taker) |
| data.commissionList[].rebateAmount | string |  | Commission returned to the direct upline partner (maker+taker)<br><br>Represents the agent rebate returned to the partner |
| data.commissionList[].userTotalRebateAmount | string |  | Commission returned to the referred user by the partner (maker+taker)<br><br>Only applicable when the partner has configured user rebates for the direct client |
| data.commissionList[].dayTotalRebateAmount | string |  | Total commission generated on that day (maker+taker)<br><br>= rebateAmount + userTotalRebateAmount |
| data.commissionList[].totalRebateAmount | string |  | Cumulative commission for the past 90 days rolling from today, including the current day (maker+taker) |
| data.endId | string |  | Last data ID. Used as an index for querying data when making a request |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1694593273026,
  "data": {
    "endId": "6624",
    "commissionList": [
      {
        "uid": "3125195374",
        "date": "1694275200000",
        "coin": "BTC",
        "symbol": "BTCUSDT_SPBL",
        "productType": "SPOT",
        "dealAmount": "222",
        "fee": "0.0000111",
        "feeDeduction": "0.00000333",
        "activityBonusDeduct": "0.00001",
        "spotCouponDeduct": "0.00001",
        "futuresCouponDeduct": "0.00001",
        "spotFeeDiscountDeduct": "0.00001",
        "negativeMakerFeeDeduct": "0.00001",
        "feePaid": "0.00000777",
        "rebateAmount": "0.00000388",
        "userTotalRebateAmount": "0",
        "dayTotalRebateAmount": "0.00000388",
        "totalRebateAmount": "0.00000388"
      }
    ]
  }
}
```

## Get Agent Sub Customer List

`GET /api/v3/affiliate/sub-customer-list`

Rate limit: 10/sec/UID

`startTime` and `endTime` should be both set or both left blank

`startTime` and `endTime` should be within 30days

If `startTime` / `endTime` are not set, all registered clients will be returned with no time restriction.

It supports querying clients registered at any time, with no 90-day restriction.

Operation ID: `affiliateGetSubCustomerList`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| startTime | query | string |  | Start time (ms) |
| endTime | query | string |  | End time (ms) |
| cursor | query | string |  | Cursor ID<br><br>Used for pagination. Omit it on the first call. For subsequent calls, pass in the last `minId` returned by the previous query. |
| limit | query | string |  | Items per page |
| uid | query | string |  | UID |
| showSub | query | string |  | Whether to Display Subordinate User Information of Direct Clients  <br><br>`yes`: Yes <br><br>`no`: No |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.uid | string |  | UID |
| data.registerTime | string |  | Register time |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695785738672,
  "data": {
    "list": [
      {
        "uid": 1235665663,
        "registerTime": "1679991960110"
      },
      {
        "uid": 1235665663,
        "registerTime": "1679991960110"
      }
    ],
    "minId": "123456"
  }
}
```

## Get Sub Affiliate Info

`GET /api/v3/affiliate/sub-affiliate-info`

Rate limit: 10/sec/UID

Query sub-affiliate information.

Operation ID: `affiliateGetSubAffiliateInfo`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| uid | query | string |  | User ID<br><br>Pass a sub-affiliate's UID to query the info for that specific sub-affiliate |
| startTime | query | string |  | Query start time<br><br>Unix millisecond timestamp |
| endTime | query | string |  | Query end time<br><br>Unix millisecond timestamp<br><br>The interval between startTime and endTime cannot exceed 30 days |
| idLessThan | query | string |  | Cursor ID<br><br>Used for pagination; retrieves data prior to this ID |
| limit | query | string |  | Number of results to return<br><br>Default `100`, maximum `100` |
| includeDownLine | query | string |  | Whether to include downline users<br><br>`yes` Yes<br><br>`no` No<br><br>Default `yes` if not provided |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | object[] |  | Sub-affiliate list |
| data.list[].uid | string |  | User ID |
| data.list[].uplineName | string |  | Upline name |
| data.list[].rebateRateList | object[] |  | Rebate rate list |
| data.list[].rebateRateList[].rebateType | string |  | Rebate type<br><br>`futures` Futures regular rebate<br><br>`futures_api` Futures API rebate<br><br>`futures_trader` Futures trading expert rebate<br><br>`futures_trader_api` Futures trading expert API rebate<br><br>`spot` Spot regular rebate<br><br>`spot_api` Spot API rebate<br><br>`spot_trader` Spot trading expert rebate<br><br>`spot_trader_api` Spot trading expert API rebate<br><br>`onchain` Onchain regular rebate<br><br>`onchain_api` Onchain API rebate<br><br>`onchain_trader` Onchain trading expert rebate<br><br>`onchain_trader_api` Onchain trading expert API rebate<br><br>`cfd` CFD regular rebate<br><br>`cfd_api` CFD API rebate<br><br>`cfd_trader` CFD trading expert rebate<br><br>`cfd_trader_api` CFD trading expert API rebate<br><br>`stock` Stock regular rebate<br><br>`stock_api` Stock API rebate<br><br>`stock_trader` Stock trading expert rebate<br><br>`stock_trader_api` Stock trading expert API rebate |
| data.list[].rebateRateList[].rebateRate | string |  | Rebate rate<br><br>Percentage value, e.g., `5` represents 5% |
| data.list[].verificationStatus | string |  | Verification status<br><br>`verified` Verified<br><br>`not_verified` Not verified<br><br>Includes both KYC and KYB results; a user who passes either KYC or KYB is considered verified |
| data.list[].directReferrals | string |  | Number of direct referrals |
| data.list[].subAffiliates | string |  | Number of sub-affiliates |
| data.list[].subAffiliateDirectReferrals | string |  | Number of direct referrals under sub-affiliates |
| data.list[].volume | string |  | Trading volume<br><br>Unit: USDT |
| data.list[].deposit | string |  | Deposit amount<br><br>Unit: USDT |
| data.list[].transactionFee | string |  | Transaction fee<br><br>Unit: USDT |
| data.list[].rebate | string |  | Rebate amount<br><br>Unit: USDT<br><br>Rebate paid back to the channel by the sub-affiliate |
| data.endId | string |  | Pagination end ID<br><br>Used as the query cursor for the next request |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1758512000000.0,
  "data": {
    "list": [
      {
        "uid": "123456789",
        "uplineName": "agentUser001",
        "rebateRateList": [
          {
            "rebateType": "futures",
            "rebateRate": "5"
          },
          {
            "rebateType": "spot",
            "rebateRate": "5"
          }
        ],
        "verificationStatus": "verified",
        "directReferrals": "10",
        "subAffiliates": "2",
        "subAffiliateDirectReferrals": "20",
        "volume": "100000",
        "deposit": "5000",
        "transactionFee": "300",
        "rebate": "150"
      }
    ],
    "endId": "123456789"
  }
}
```

## Get Sub Affiliate Commission

`GET /api/v3/affiliate/sub-affiliate-commission`

Rate limit: 10/sec/UID

startTime and endTime should be set simultaneously or not set at all.

The maximum time span supported by startTime and endTime is 7 days.

This API supports retrieving data within the past 90 days.

If startTime and endTime are not set in the request, it will default to returning information for yesterday (00:00-23:

  59 UTC+8).

Operation ID: `affiliateGetSubAffiliateCommission`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| startTime | query | string |  | Start time <br><br> Unix millisecond timestamp |
| endTime | query | string |  | End time <br><br> Unix millisecond timestamp |
| limit | query | string |  | max:100,default: 100 |
| cursor | query | string |  | Cursor ID<br><br>Used for pagination. Omit it on the first call. For subsequent calls, pass in the last `endId` returned by the previous query. |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.commissionList | object[] |  | Customer Commission List |
| data.commissionList[].uid | string |  | Partner UID |
| data.commissionList[].bizType | string |  | Trade type  <br><br> `spot`<br><br> `futures` |
| data.commissionList[].subBizType | string |  | subBizType<br><br> `spot`<br><br> `margin`<br><br> `usdt_futures` <br><br>`coin_futures`<br><br> `usdc_futures` |
| data.commissionList[].symbol | string |  | symbol |
| data.commissionList[].coin | string |  | coin |
| data.commissionList[].fee | string |  | Total fee <br><br> Statistical values within the input time range <br><br> Precision is 8 decimal places |
| data.commissionList[].volume | string |  | Transaction amount<br><br> Statistical value within the input time range <br><br> Precision is 8 decimal places |
| data.commissionList[].activityBonusDeduct | string |  | Fees offset by experience funds |
| data.commissionList[].spotCouponDeduct | string |  | Fees offset by spot cashback coupons |
| data.commissionList[].futuresCouponDeduct | string |  | Fees offset by contract airdrop coupons |
| data.commissionList[].spotFeeDiscountDeduct | string |  | Fees reduced by spot fee discounts |
| data.commissionList[].negativeMakerFeeDeduct | string |  | Fees offset by negative maker fees |
| data.commissionList[].feePaid | string |  | Actual paid fee <br><br> Statistical value within the input time period <br><br> Precision is 8 decimal places |
| data.commissionList[].directCommission | string |  | Direct customer commission<br><br> Direct customers are first-level users directly invited by KOL <br><br> Statistical value within the participation period <br><br> Precision is 8 decimal places |
| data.commissionList[].subCommission | string |  | Subordinate commission<br><br> Direct customer subordinates are second-level, third-level...(not first-level) indirect invitation relationship <br><br> Statistical value within the participation time period <br><br> Precision is 8 decimal places |
| data.commissionList[].partnerCommission | string |  | Partner Commission (= direct customer commission + subordinate commission) <br><br> Statistical value within the entry time period <br><br> Precision is 8 decimal places |
| data.commissionList[].partnerActualCommission | string |  | Partner's actual commission after deducting risk control portion and special scenario deductions <br><br> Statistical value within the entry time period <br><br> Precision is 8 decimal places |
| data.commissionList[].traderType | string |  | Trader type commission <br><br> `user`: ordinary user — ordinary order commission <br><br> `Trader`: trader — trader order commission |
| data.commissionList[].apiType | string |  | API commission type<br><br> `api`: API user `non_api`: non-API user |
| data.commissionList[].status | string |  | status <br><br> `settled`<br><br> `unsettled`<br><br> `notIssued` |
| data.commissionList[].startCalculationTime | string |  | Statistics start time Unix millisecond timestamp |
| data.commissionList[].endCalculationTime | string |  | Statistics end time Unix millisecond timestamp |
| data.endId | string |  | The last data ID. When used as a request, the id is used as an index for the next query |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1694593273026,
  "data": {
    "endId": "6624",
    "commissionList": [
      {
        "uid": "3125195374",
        "bizType": "futures",
        "subBizType": "usdt_futures",
        "symbol": "BTCUSDT",
        "coin": "BTC",
        "fee": "0.0000111",
        "volume": "2.2",
        "activityBonusDeduct": "0.00001",
        "spotCouponDeduct": "0.00001",
        "futuresCouponDeduct": "0.00001",
        "spotFeeDiscountDeduct": "0.00001",
        "negativeMakerFeeDeduct": "0.00001",
        "feePaid": "0.00005",
        "directCommission": "0.00001",
        "subCommission": "0.00001",
        "partnerCommission": "0.000001",
        "partnerActualCommission": "0.00001",
        "traderType": "trader",
        "apiType": "non_api",
        "status": "settled",
        "startCalculationTime": "1728635651441",
        "endCalculationTime": "1728635651441"
      }
    ]
  }
}
```


---

代理商直客列表、资产、交易量、充值、KYC 结果与佣金查询接口。

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `GET /api/v3/affiliate/customer-list` — 获取直客列表
- `GET /api/v3/affiliate/customer-asset` — 获取直客余额
- `GET /api/v3/affiliate/customer-trade-volume` — 获取直客交易量
- `GET /api/v3/affiliate/customer-deposit` — 获取直客充值记录
- `GET /api/v3/affiliate/customer-kyc-result` — 获取直客认证结果
- `GET /api/v3/affiliate/customer-commission` — 获取直客佣金
- `GET /api/v3/affiliate/sub-customer-list` — 获取直客下级信息接口
- `GET /api/v3/affiliate/sub-affiliate-info` — 获取子代理信息
- `GET /api/v3/affiliate/sub-affiliate-commission` — 获取子代理佣金

## 获取直客列表

`GET /api/v3/affiliate/customer-list`

限频规则: 10次/秒/UID

`startTime`和`endTime`应该被同时设置或者同时不设置

`startTime`和`endTime`支持的最大时间跨度为30天

若不传`startTime` / `endTime`，将返回该代理商名下所有时间段注册的直客数据，无时间限制。

支持查询任意时间段注册的直客，已取消 90 天限制。

如果想确认某UID是否是您邀请的直客,可以通过在 query 参数里传入 `uid` 进行验证,例如 `uid=123456`

注册直客数据更新信息是实时的

Operation ID: `affiliateGetCustomerList`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| startTime | query | string |  | 开始时间(毫秒) |
| endTime | query | string |  | 结束时间(毫秒) |
| pageNo | query | string |  | 页码 |
| pageSize | query | string |  | 分页大小,默认100,最大1000 |
| uid | query | string |  | UID |
| referralCode | query | string |  | 邀请code |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].uid | string |  | UID |
| data[].registerTime | string |  | 注册时间 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695785738672,
  "data": [
    {
      "uid": 1235665663,
      "registerTime": "1679991960110"
    },
    {
      "uid": 1235665663,
      "registerTime": "1679991960110"
    }
  ]
}
```

## 获取直客余额

`GET /api/v3/affiliate/customer-asset`

限频规则: 10次/秒/UID

数据更新频率：10分钟

Operation ID: `affiliateGetCustomerAsset`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| pageNo | query | string |  | 页码 |
| pageSize | query | string |  | 分页大小,默认100,最大500 |
| uid | query | string |  | UID |
| showSub | query | string |  | 是否展示直客的下级用户信息 <br><br>`yes`: 是<br><br>`no`: 否 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].uid | string |  | 用户ID |
| data[].balance | string |  | 账户余额 |
| data[].uTime | string |  | 账户上次余额更新时间 |
| data[].remark | string |  | 当用户的子账户过多时，提示子账户过多，无法查询到账户余额 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 163123213132,
  "data": [
    {
      "balance": "1234",
      "uid": "23423432",
      "uTime": "23423423423",
      "remark": "sub account exceed 5"
    }
  ]
}
```

## 获取直客交易量

`GET /api/v3/affiliate/customer-trade-volume`

限频规则: 10次/秒/UID

该接口返回的统计数据包含现货、合约的交易量

startTime和endTime应该被同时设置或者同时不设置

startTime和endTime支持的最大时间跨度为30天

该接口支持获取90天内数据

如果请求中不设置startTime和endTime将会默认返回昨日(00:00-23:59 UTC+8)的信息

数据更新频率：1小时

Operation ID: `affiliateGetCustomerTradeVolume`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| startTime | query | string |  | 开始时间(毫秒) |
| endTime | query | string |  | 结束时间(毫秒) |
| pageNo | query | string |  | 页码 |
| pageSize | query | string |  | 分页大小,默认100,最大1000 |
| uid | query | string |  | UID |
| showSub | query | string |  | 是否展示直客的下级用户信息 <br><br>`yes`：是 <br><br>`no`：否 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].uid | string |  | UID |
| data[].volumn | string |  | 交易量 |
| data[].spotVolume | string |  | 现货交易量 |
| data[].futuresVolume | string |  | 合约交易量 |
| data[].time | string |  | 时间戳 (ms) |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 163123213132,
  "data": [
    {
      "uid": "435435345",
      "volumn": "34234.4",
      "spotVolume": "12000.0",
      "futuresVolume": "22234.4",
      "time": "1679991960110"
    },
    {
      "uid": "435435345",
      "volumn": "34234.4",
      "spotVolume": "12000.0",
      "futuresVolume": "22234.4",
      "time": "1679991960110"
    }
  ]
}
```

## 获取直客充值记录

`GET /api/v3/affiliate/customer-deposit`

限频规则: 10次/秒/UID

API响应中包含了用户的链上充值和内部转账

startTime和endTime应该被同时设置或者同时不设置

startTime和endTime支持的最大时间跨度为30天

该接口支持获取90天内数据，如需更久数据可以联系BD手动导出

如果请求中不设置startTime和endTime将会默认返回昨日(00:00-23:59 UTC+8)的信息

该接口数据更新信息是实时的

Operation ID: `affiliateGetCustomerDeposit`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| startTime | query | string |  | 开始时间(毫秒) |
| endTime | query | string |  | 结束时间(毫秒) |
| pageNo | query | string |  | 页码 |
| pageSize | query | string |  | 分页大小,默认100,最大1000 |
| uid | query | string |  | UID |
| showSub | query | string |  | 是否展示直客的下级用户信息 <br><br>`yes`: 是<br><br>`no`: 否 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].uid | string |  | UID |
| data[].orderId | string |  | 充值订单ID |
| data[].depositTime | string |  | 充值时间 (ms) |
| data[].depositCoin | string |  | 充值币种 |
| data[].depositAmount | string |  | 充值数量 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 163123213132,
  "data": [
    {
      "orderId": "3423423",
      "uid": "234342343",
      "depositTime": "11234342343",
      "depositCoin": "USDT",
      "depositAmount": "500"
    }
  ]
}
```

## 获取直客认证结果

`GET /api/v3/affiliate/customer-kyc-result`

限频规则: 10次/秒/UID

startTime和endTime应该被同时设置或者同时不设置

如果请求中不设置startTime和endTime将会默认返回昨日(00:00-23:59UTC+8)KYC或KYB的用戶信息

数据更新频率：5分钟

Operation ID: `affiliateGetCustomerKycResult`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| startTime | query | string |  | 开始时间(毫秒)  <br><br>开始、结束时间间隔最大90天 |
| endTime | query | string |  | 结束时间(毫秒)   <br><br>开始、结束时间间隔最大90天 |
| cursor | query | string |  | 游标ID<br><br>用于分页。首次调用不传。后续调用传入上次查询返回的最后一个`endId` |
| limit | query | string |  | 查询条数，默认100，最大1000 |
| uid | query | string |  | UID |
| showSub | query | string |  | 是否展示直客的下级用户信息  <br><br>`yes`: 是<br><br>`no`: 否 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.uid | string |  | UID |
| data.kycResult | string |  | 认证结果<br><br>`passed`<br><br> `not_passed` |
| data.endId | string |  | 本页面最后的UID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 163123213132,
  "data": {
    "userList": [
      {
        "uid": "435435345",
        "kycResult": "passed"
      }
    ],
    "endId": "435435345"
  }
}
```

## 获取直客佣金

`GET /api/v3/affiliate/customer-commission`

限频规则: 10次/秒/UID

startTime和endTime应该被同时设置或者同时不设置

该接口支持获取90天内数据，如需更久数据可以联系BD手动导出

如果请求中不设置startTime和endTime将会默认返回昨日(00:00-23:59 UTC+8)的信息

数据更新频率：T+1 (UTC +8)

Operation ID: `affiliateGetCustomerCommission`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| startTime | query | string |  | 开始时间(毫秒) <br><br>开始、结束时间间隔最大30天 |
| endTime | query | string |  | 结束时间(毫秒)  <br><br>开始、结束时间间隔最大30天 |
| cursor | query | string |  | 游标ID<br><br>用于分页。首次调用不传。后续调用传入上次查询返回的最后一个`endId` |
| limit | query | string |  | 查询条数，默认100，最大1000 |
| uid | query | string |  | 用户ID |
| coin | query | string |  | 币种，如BTC |
| symbol | query | string |  | 交易对 举例：<br><br> BGBUSDT_SPBL `spot`<br><br> BTCUSDT_SPBL-MABL `spot margin`<br><br> BTCUSDT_UMCBL `USDT-Futures` <br><br>BTCUSD_DMCBL  `COIN-Futures` <br><br>BTCPERP_CMCBL `USDC-Futures` |
| showSub | query | string |  | 是否展示直客的下级用户信息  <br><br>`yes`: 是<br><br>`no`: 否 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.commissionList | object[] |  | 直客佣金列表 |
| data.commissionList[].uid | string |  | 用户ID |
| data.commissionList[].date | string |  | 返佣日期 |
| data.commissionList[].coin | string |  | 币种 |
| data.commissionList[].symbol | string |  | 交易对 |
| data.commissionList[].productType | string |  | 业务线 <br><br> `SPOT` 现货<br><br>`MARGIN` 杠杆<br><br>`USDT-FUTURES` USDT合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |
| data.commissionList[].dealAmount | string |  | 交易量(maker+taker) |
| data.commissionList[].fee | string |  | 手续费(maker+taker)<br><br>佣金和手续费均以 coin 币种计价 |
| data.commissionList[].feeDeduction | string |  | 手续费抵扣 |
| data.commissionList[].activityBonusDeduct | string |  | 体验金抵扣的金额 |
| data.commissionList[].spotCouponDeduct | string |  | 现货返现券抵扣的金额 |
| data.commissionList[].futuresCouponDeduct | string |  | 合约空投券抵扣的金额 |
| data.commissionList[].spotFeeDiscountDeduct | string |  | 现货手续费折扣减免的金额 |
| data.commissionList[].negativeMakerFeeDeduct | string |  | 负maker手续费抵扣的金额 |
| data.commissionList[].feePaid | string |  | 实际收取手续费(maker+taker) |
| data.commissionList[].rebateAmount | string |  | 返还代理佣金，用户返给直接上级代理商的佣金(maker+taker) |
| data.commissionList[].userTotalRebateAmount | string |  | 返还用户佣金，代理商返给用户的佣金；仅在合伙人为直客设置了用户返佣后才有此数据(maker+taker) |
| data.commissionList[].dayTotalRebateAmount | string |  | 当日总佣金(maker+taker)<br><br>= rebateAmount + userTotalRebateAmount |
| data.commissionList[].totalRebateAmount | string |  | 90天累计佣金(maker+taker)<br><br>统计范围为今天往前推90天，包括当天 |
| data.endId | string |  | 最后一条数据 ID。用于在发出请求时作为查询数据的索引 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1694593273026,
  "data": {
    "endId": "6624",
    "commissionList": [
      {
        "uid": "3125195374",
        "date": "1694275200000",
        "coin": "BTC",
        "symbol": "BTCUSDT_SPBL",
        "productType": "SPOT",
        "dealAmount": "222",
        "fee": "0.0000111",
        "feeDeduction": "0.00000333",
        "activityBonusDeduct": "0.00001",
        "spotCouponDeduct": "0.00001",
        "futuresCouponDeduct": "0.00001",
        "spotFeeDiscountDeduct": "0.00001",
        "negativeMakerFeeDeduct": "0.00001",
        "feePaid": "0.00000777",
        "rebateAmount": "0.00000388",
        "userTotalRebateAmount": "0",
        "dayTotalRebateAmount": "0.00000388",
        "totalRebateAmount": "0.00000388"
      }
    ]
  }
}
```

## 获取直客下级信息接口

`GET /api/v3/affiliate/sub-customer-list`

限频规则: 10次/秒/UID

`startTime`和`endTime`应该被同时设置或者同时不设置

`startTime`和`endTime`支持的最大时间跨度为30天

若不传`startTime` / `endTime`，将返回该代理商名下所有时间段注册的直客数据，无时间限制。

支持查询任意时间段注册的直客，已取消 90 天限制。

Operation ID: `affiliateGetSubCustomerList`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| startTime | query | string |  | 开始时间(毫秒) |
| endTime | query | string |  | 结束时间(毫秒) |
| cursor | query | string |  | 游标ID<br><br>用于分页。首次调用不传。后续调用传入上次查询返回的最后一个`minId` |
| limit | query | string |  | 每页条目数 |
| uid | query | string |  | UID |
| showSub | query | string |  | 是否展示直客的下级用户信息  <br><br>`yes`: 是<br><br>`no`: 否 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.uid | string |  | UID |
| data.registerTime | string |  | 注册时间 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695785738672,
  "data": {
    "list": [
      {
        "uid": 1235665663,
        "registerTime": "1679991960110"
      },
      {
        "uid": 1235665663,
        "registerTime": "1679991960110"
      }
    ],
    "minId": "123456"
  }
}
```

## 获取子代理信息

`GET /api/v3/affiliate/sub-affiliate-info`

限频规则: 10次/秒/UID

查询子代理信息。

Operation ID: `affiliateGetSubAffiliateInfo`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| uid | query | string |  | 用户ID<br><br>可传入子代理uid以查询指定子代理信息 |
| startTime | query | string |  | 查询开始时间<br><br>Unix毫秒时间戳 |
| endTime | query | string |  | 查询结束时间<br><br>Unix毫秒时间戳<br><br>开始、结束时间间隔最大30天 |
| idLessThan | query | string |  | 游标ID<br><br>用于翻页，获取此ID前的数据 |
| limit | query | string |  | 查询条数<br><br>默认100，最大100 |
| includeDownLine | query | string |  | 是否包含下级用户<br><br>`yes` 是<br><br>`no` 否<br><br>如不传，默认值为`yes` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | object[] |  | 子代理列表 |
| data.list[].uid | string |  | 用户ID |
| data.list[].uplineName | string |  | 上级名称 |
| data.list[].rebateRateList | object[] |  | 返佣比例列表 |
| data.list[].rebateRateList[].rebateType | string |  | 返佣类型<br><br>`futures` 合约常规返佣<br><br>`futures_api` 合约API返佣<br><br>`futures_trader` 合约交易专家返佣<br><br>`futures_trader_api` 合约交易专家API返佣<br><br>`spot` 现货常规返佣<br><br>`spot_api` 现货API返佣<br><br>`spot_trader` 现货交易专家返佣<br><br>`spot_trader_api` 现货交易专家API返佣<br><br>`onchain` 链上常规返佣<br><br>`onchain_api` 链上API返佣<br><br>`onchain_trader` 链上交易专家返佣<br><br>`onchain_trader_api` 链上交易专家API返佣<br><br>`cfd` CFD常规返佣<br><br>`cfd_api` CFD API返佣<br><br>`cfd_trader` CFD交易专家返佣<br><br>`cfd_trader_api` CFD交易专家API返佣<br><br>`stock` 股票常规返佣<br><br>`stock_api` 股票API返佣<br><br>`stock_trader` 股票交易专家返佣<br><br>`stock_trader_api` 股票交易专家API返佣 |
| data.list[].rebateRateList[].rebateRate | string |  | 返佣比例<br><br>百分比数值，如`5`代表5% |
| data.list[].verificationStatus | string |  | 认证状态<br><br>`verified` 已认证<br><br>`not_verified` 未认证<br><br>包含KYC及KYB结果。通过KYC或KYB其中一项的用户，该字段为已认证 |
| data.list[].directReferrals | string |  | 直客数量 |
| data.list[].subAffiliates | string |  | 子代理数量 |
| data.list[].subAffiliateDirectReferrals | string |  | 子代理直客数量 |
| data.list[].volume | string |  | 交易额<br><br>单位为USDT |
| data.list[].deposit | string |  | 充值金额<br><br>单位为USDT |
| data.list[].transactionFee | string |  | 手续费<br><br>单位为USDT |
| data.list[].rebate | string |  | 返还佣金<br><br>单位为USDT<br><br>子代理返还给渠道的佣金 |
| data.endId | string |  | 分页结尾ID<br><br>用于在发出请求时作为查询数据的索引 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1758512000000.0,
  "data": {
    "list": [
      {
        "uid": "123456789",
        "uplineName": "agentUser001",
        "rebateRateList": [
          {
            "rebateType": "futures",
            "rebateRate": "5"
          },
          {
            "rebateType": "spot",
            "rebateRate": "5"
          }
        ],
        "verificationStatus": "verified",
        "directReferrals": "10",
        "subAffiliates": "2",
        "subAffiliateDirectReferrals": "20",
        "volume": "100000",
        "deposit": "5000",
        "transactionFee": "300",
        "rebate": "150"
      }
    ],
    "endId": "123456789"
  }
}
```

## 获取子代理佣金

`GET /api/v3/affiliate/sub-affiliate-commission`

限频规则: 10次/秒/UID

startTime和endTime应该被同时设置或者同时不设置

startTime和endTime支持的最大时间跨度为7天

该接口支持获取90天内数据，如需更久数据可以联系BD手动导出

如果请求中不设置startTime和endTime将会默认返回昨日(00:00-23:59 UTC+8)的信息

Operation ID: `affiliateGetSubAffiliateCommission`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| startTime | query | string |  | 开始时间 <br><br> Unix时间戳的毫秒数格式 |
| endTime | query | string |  | 结束时间 <br><br> Unix时间戳的毫秒数格式 |
| limit | query | string |  | 分页限制 最大:100,默认: 100 |
| cursor | query | string |  | 游标ID<br><br>用于分页。首次调用不传。后续调用传入上次查询返回的最后一个`endId` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.commissionList | object[] |  | 客户佣金列表 |
| data.commissionList[].uid | string |  | 合作伙伴用户 ID |
| data.commissionList[].bizType | string |  | 交易类型  <br><br> `spot`<br><br> `futures` |
| data.commissionList[].subBizType | string |  | 子交易类型<br><br> `spot`<br><br> `margin`<br><br> `usdt_futures` <br><br>`coin_futures`<br><br> `usdc_futures` |
| data.commissionList[].symbol | string |  | 交易对 |
| data.commissionList[].coin | string |  | 币种 |
| data.commissionList[].fee | string |  | 总手续费 <br><br> 输入时间范围内的统计值 <br><br> 精度为 8 位小数 |
| data.commissionList[].volume | string |  | 交易金额 <br><br> 输入时间范围内的统计值 <br><br> 精度为 8 位小数 |
| data.commissionList[].activityBonusDeduct | string |  | 体验金抵扣的金额 |
| data.commissionList[].spotCouponDeduct | string |  | 现货返现券抵扣的金额 |
| data.commissionList[].futuresCouponDeduct | string |  | 合约空投券抵扣的金额 |
| data.commissionList[].spotFeeDiscountDeduct | string |  | 现货手续费折扣减免的金额 |
| data.commissionList[].negativeMakerFeeDeduct | string |  | 负maker手续费抵扣的金额 |
| data.commissionList[].feePaid | string |  | 实际支付手续费 <br><br> 输入时间范围内的统计值 <br><br> 精度为 8 位小数 |
| data.commissionList[].directCommission | string |  | 直客佣金<br><br> 直客指 KOL 直接邀请的一级用户 <br><br> 输入时间范围内的统计值 <br><br> 精度为 8 位小数 |
| data.commissionList[].subCommission | string |  | 下级佣金<br><br> 直接客户的下级为二级、三级...（非一级）间接邀请关系 <br><br> 输入时间范围内的统计值 <br><br> 精度为 8 位小数 |
| data.commissionList[].partnerCommission | string |  | 合作伙伴佣金（= 直客佣金 + 下级佣金）<br><br>输入时间范围内的统计值 <br><br> 精度为 8 位小数 |
| data.commissionList[].partnerActualCommission | string |  | 合作伙伴实际佣金，扣除风控部分以及特殊场景扣除后实际到手的佣金 <br><br> 输入时间范围内的统计值 <br><br> 精度为 8 位小数 |
| data.commissionList[].traderType | string |  | 交易者类型佣金 <br><br> `user`: 普通用户 — 普通订单佣金 <br><br> `Trader`: 交易员 — 交易员订单佣金 |
| data.commissionList[].apiType | string |  | API 佣金类型<br><br> `api`: API 用户 `non_api`: 非 API 用户 |
| data.commissionList[].status | string |  | 状态 <br><br> `settled` 已结算 <br><br> `unsettled` 未结算<br><br> `notIssued` 未发放 |
| data.commissionList[].startCalculationTime | string |  | 统计开始时间 Unix 毫秒时间戳 |
| data.commissionList[].endCalculationTime | string |  | 统计结束时间 Unix 毫秒时间戳 |
| data.endId | string |  | 最后一条数据 ID。请求时作为下一次查询的索引 ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1694593273026,
  "data": {
    "endId": "6624",
    "commissionList": [
      {
        "uid": "3125195374",
        "bizType": "futures",
        "subBizType": "usdt_futures",
        "symbol": "BTCUSDT",
        "coin": "BTC",
        "fee": "0.0000111",
        "volume": "2.2",
        "activityBonusDeduct": "0.00001",
        "spotCouponDeduct": "0.00001",
        "futuresCouponDeduct": "0.00001",
        "spotFeeDiscountDeduct": "0.00001",
        "negativeMakerFeeDeduct": "0.00001",
        "feePaid": "0.00005",
        "directCommission": "0.00001",
        "subCommission": "0.00001",
        "partnerCommission": "0.000001",
        "partnerActualCommission": "0.00001",
        "traderType": "trader",
        "apiType": "non_api",
        "status": "settled",
        "startCalculationTime": "1728635651441",
        "endCalculationTime": "1728635651441"
      }
    ]
  }
}
```