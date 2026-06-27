---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/futures-api/history/account-log
api_type: REST
updated_at: 2026-05-27 19:45:51.434198
---

# Get account log

**GET** `https://futures.kraken.com/api/history/v3/account-log`

Lists account log entries, paged by timestamp or by ID.

To request entries by time range, use the `since` and `before` parameters. To request entries by ID range, use the `from` and `to` parameters. Any combination of `since`, `before`, `from` and `to` can be used to restrict the requested range of entries.

## Request

### Query Parameters

**since** `timestamp-milliseconds`

Unix timestamp in milliseconds.

**before** `timestamp-milliseconds`

Unix timestamp in milliseconds.

**from** `integer`

ID of the first entry (inclusive). IDs start at 1.

**to** `integer`

ID of the last entry (inclusive).

**sort** `string`

**Possible values:** [`asc`, `desc`]

Order of events in response. `asc` = chronological, `desc` = reverse-chronological.

**Default value:**`desc`

**info** `string[]`

**Possible values:** [`futures trade`, `futures liquidation`, `futures assignor`, `futures assignee`, `futures unwind counterparty`, `futures unwind bankrupt`, `covered liquidation`, `funding rate change`, `conversion`, `interest payment`, `transfer`, `cross-exchange transfer`, `kfee applied`, `subaccount transfer`, `settlement`, `admin transfer`, `tax withheld`, `tax refund`]

Types of entry to filter by. Only these types will be returned.

**count** `integer`

Amount of entries to be returned.

**Default value:**`500`

**conversion_details** `boolean`

Include exchange rate and conversion fee for conversions.

**Default value:**`false`

## Responses

  * 200
  * 429

Account log.

  * application/json
* Schema

**Schema**

**accountUid** string<uuid>required

UID of the account

**logs** `object[]` *required*

  * Array [

    ↳ **asset** `string` *required*

Asset related with the entry.

    ↳ **booking_uid** `string<uuid>` *required*

UID of the log entry.

    ↳ **collateral** `string | nullnullable` *required*

Currency of the associated entry.

    ↳ **contract** `string | nullnullable` *required*

    ↳ **date** `string<date-time>` *required*

RFC 3339 formatted date-time

**Example:**`2019-08-24T14:15:22Z`

    ↳ **execution** `string | nullnullable` *required*

UID of the associated execution or transfer.

For orders and trades, this is always a UUID. However, this field is also populated with "cross-exchange transfer" references, which are not always UUIDs.

    ↳ **fee** `number,null<double>nullable` *required*

Fee paid

    ↳ **funding_rate** `number,null<double>nullable` *required*

Absolute funding rate at time of entry.

    ↳ **id** `integer<int64>` *required*

Log entry ID.

**Possible values:** `>= 1`

    ↳ **info** `string` *required*

Short description of the entry.

**Possible values:** [`futures trade`, `futures liquidation`, `futures assignor`, `futures assignee`, `futures unwind counterparty`, `futures unwind bankrupt`, `covered liquidation`, `funding rate change`, `conversion`, `interest payment`, `transfer`, `cross-exchange transfer`, `kfee applied`, `subaccount transfer`, `settlement`, `admin transfer`]

    ↳ **margin_account** `string` *required*

Name of the wallet associated with the entry.

    ↳ **mark_price** `number,null<double>nullable` *required*

Mark price at the time the trade was executed.

    ↳ **new_average_entry_price** `number,null<double>nullable` *required*

Average entry price of the position after this trade.

    ↳ **new_balance** `number<double>` *required*

New balance of wallet or new size of the position after the described in info action.

    ↳ **old_average_entry_price** `number,null<double>nullable` *required*

Average entry price of the position prior to this trade.

    ↳ **old_balance** `number<double>` *required*

Account balance before the described in info action.

    ↳ **realized_funding** `number,null<double>nullable` *required*

Funding realized due to change in position size or end of funding rate period.

    ↳ **realized_pnl** `number,null<double>nullable` *required*

PnL that is realized by reducing the position.

    ↳ **trade_price** `number,null<double>nullable` *required*

Price at which the trade was executed.

    ↳ **conversion_spread_percentage** `number,null<double>nullable` *required*

Percentage conversion spread used in a currency conversion.

    ↳ **liquidation_fee** `number,null<double>nullable` *required*

Liquidation fee associated with a liquidation/assignment entry.

Not applicable for inverse futures.

    ↳ **exchange_rate** `number<double>`

The exchange rate used for the conversion, USD quote.

    ↳ **conversion_fee** `number<double>`

The percentage fee charged for the conversion. E.g. 0.05 = 0.05%.

    ↳ **exchange_rate_from** `string`

The currency code of the base currency in the exchange rate.

  * ]

Rate limited.

**Response Headers**

**rate-limit-reset**

Time remaining (in seconds) until repeat request (i.e., same cost) will be accepted.
* text/plain
* Schema

**Schema**

    ↳ **string** `string`

#### Authorization: APIKey
    
    
    **name:** [APIKey](/api/docs/futures-api/history/history#authentication)**type:** apiKey**description:** General API key with at least **read-only** access**in:** header**x-inlineDescription:** true
    
    
    **name:** [Authent](/api/docs/futures-api/history/history#authentication)**type:** apiKey**description:** Authentication string**in:** header**x-inlineDescription:** true

  * curl
  * python
  * go
  * nodejs
* CURL

    
    
    curl -L 'https://futures.kraken.com/api/history/v3/account-log' \  
    -H 'Accept: application/json' \  
    -H 'APIKey: <APIKey>' \  
    -H 'Authent: <Authent>'  
    

Request Collapse all

Base URL

https://futures.kraken.com/api/history/v3

Auth

general-api-key-read-only

authent

Parameters

since — query

before — query

from — query

to — query

sort — query

\---ascdesc

info — query

futures tradefutures liquidationfutures assignorfutures assigneefutures unwind counterpartyfutures unwind bankruptcovered liquidationfunding rate changeconversioninterest paymenttransfercross-exchange transferkfee appliedsubaccount transfersettlementadmin transfertax withheldtax refund

count — query

conversion_details — query

\---truefalse