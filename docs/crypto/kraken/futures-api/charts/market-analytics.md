---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/futures-api/charts/market-analytics
api_type: Market Data
updated_at: 2026-05-27 19:45:15.755852
---

# Market Analytics

**GET** `https://futures.kraken.com/api/charts/v1/analytics/:symbol/:analytics_type`

Analytics data divided into time buckets

## Request

### Path Parameters

**symbol** `string` *required*

Market symbol

**analytics_type** `Type of analytics` *required*

**Possible values:** [`open-interest`, `aggressor-differential`, `trade-volume`, `trade-count`, `liquidation-volume`, `rolling-volatility`, `long-short-ratio`, `long-short-info`, `cvd`, `top-traders`, `orderbook`, `spreads`, `liquidity`, `slippage`, `future-basis`, `funding`]

### Query Parameters

**since** `int64` *required*

epoch time in seconds

**interval** `Resolution in seconds` *required*

**Possible values:** [`60`, `300`, `900`, `1800`, `3600`, `14400`, `43200`, `86400`, `604800`]

**to** `integer`

epoch time in seconds, default now

## Responses

  * 200
  * 400
  * 404

Available analytics by type and symbol

  * application/json
* Schema

**Schema**

**result** `object` *required*

    ↳ **timestamp** `integer[]` *required*

    ↳ **more** `boolean` *required*

True if there are more candles in time range

    ↳ **data** `object` *required*

oneOf
* MOD1
* Statistic of long and short positions
* Orderbook analytics data
* AnalyticsCvdData
* AnalyticsTopTradersData
* AnalyticsLiquidityPoolData
* AnalyticsFutureBasisData
* AnalyticsFundingData

  * Array [

oneOf
* MOD1
* MOD2
* Ohlc

****number

****string

  * Array [

****number

  * ]

  * ]

**longCount** integer[]

**shortCount** integer[]

**longPercent** string<big-decimal>[]

**shortPercent** string<big-decimal>[]

        ↳ **ratio** `string<big-decimal>[]` *required*

        ↳ **bid** `object` *required*

oneOf
* Orderbook spread data
* Orderbook liquidity data
* Orderbook slippage data
* Combination of all orderbook metrics

            ↳ **best_price** `string,null<big-decimal>[]` *required*

**liquidity_005** string,null<big-decimal>[]required

**liquidity_01** string,null<big-decimal>[]required

**liquidity_025** string,null<big-decimal>[]required

**liquidity_05** string,null<big-decimal>[]required

**liquidity_10** string,null<big-decimal>[]required

**liquidity_100** string,null<big-decimal>[]required

**slippage_1k** string,null<big-decimal>[]required

**slippage_10k** string,null<big-decimal>[]required

**slippage_100k** string,null<big-decimal>[]required

**slippage_1m** string,null<big-decimal>[]required

**slippage1k** string,null<big-decimal>[]required

**slippage10k** string,null<big-decimal>[]required

**slippage100k** string,null<big-decimal>[]required

**slippage1m** string,null<big-decimal>[]required

**bestPrice** string,null<big-decimal>[]required

**liquidity005** string,null<big-decimal>[]required

**liquidity01** string,null<big-decimal>[]required

**liquidity025** string,null<big-decimal>[]required

**liquidity05** string,null<big-decimal>[]required

**liquidity10** string,null<big-decimal>[]required

**liquidity100** string,null<big-decimal>[]required

            ↳ **ask** `object` *required*

oneOf
* Orderbook spread data
* Orderbook liquidity data
* Orderbook slippage data
* Combination of all orderbook metrics

                ↳ **best_price** `string,null<big-decimal>[]` *required*

**liquidity_005** string,null<big-decimal>[]required

**liquidity_01** string,null<big-decimal>[]required

**liquidity_025** string,null<big-decimal>[]required

**liquidity_05** string,null<big-decimal>[]required

**liquidity_10** string,null<big-decimal>[]required

**liquidity_100** string,null<big-decimal>[]required

**slippage_1k** string,null<big-decimal>[]required

**slippage_10k** string,null<big-decimal>[]required

**slippage_100k** string,null<big-decimal>[]required

**slippage_1m** string,null<big-decimal>[]required

**slippage1k** string,null<big-decimal>[]required

**slippage10k** string,null<big-decimal>[]required

**slippage100k** string,null<big-decimal>[]required

**slippage1m** string,null<big-decimal>[]required

**bestPrice** string,null<big-decimal>[]required

**liquidity005** string,null<big-decimal>[]required

**liquidity01** string,null<big-decimal>[]required

**liquidity025** string,null<big-decimal>[]required

**liquidity05** string,null<big-decimal>[]required

**liquidity10** string,null<big-decimal>[]required

**liquidity100** string,null<big-decimal>[]required

**buyVolume** string<big-decimal>[]required

**sellVolume** string<big-decimal>[]required

                ↳ **cvd** `string<big-decimal>[]` *required*

**top20Percent** objectrequired

**openInterest** string<big-decimal>[]required

**longCount** integer[]required

**shortCount** integer[]required

**longPercent** string<big-decimal>[]required

**shortPercent** string<big-decimal>[]required

                ↳ **ratio** `string<big-decimal>[]` *required*

**usdValue** string<big-decimal>[]required

                ↳ **basis** `string<big-decimal>[]` *required*

                ↳ **rate** `array[]` *required*

**Possible values:** `>= 4`, `<= 4`

**relativeRate** array[]required

**Possible values:** `>= 4`, `<= 4`

                    ↳ **errors** `object[]` *required*

  * Array [

                        ↳ **severity** `string` *required*

                        ↳ **error_class** `string` *required*

                        ↳ **type** `string` *required*

                        ↳ **msg** `string`

                        ↳ **value** `string`

                        ↳ **field** `string`

  * ]

Query has invalid arguments

  * application/json
* Schema

**Schema**

**result** `object` *required*

    ↳ **timestamp** `integer[]` *required*

    ↳ **more** `boolean` *required*

True if there are more candles in time range

    ↳ **data** `object` *required*

oneOf
* MOD1
* Statistic of long and short positions
* Orderbook analytics data
* AnalyticsCvdData
* AnalyticsTopTradersData
* AnalyticsLiquidityPoolData
* AnalyticsFutureBasisData
* AnalyticsFundingData

  * Array [

oneOf
* MOD1
* MOD2
* Ohlc

****number

****string

  * Array [

****number

  * ]

  * ]

**longCount** integer[]

**shortCount** integer[]

**longPercent** string<big-decimal>[]

**shortPercent** string<big-decimal>[]

        ↳ **ratio** `string<big-decimal>[]` *required*

        ↳ **bid** `object` *required*

oneOf
* Orderbook spread data
* Orderbook liquidity data
* Orderbook slippage data
* Combination of all orderbook metrics

            ↳ **best_price** `string,null<big-decimal>[]` *required*

**liquidity_005** string,null<big-decimal>[]required

**liquidity_01** string,null<big-decimal>[]required

**liquidity_025** string,null<big-decimal>[]required

**liquidity_05** string,null<big-decimal>[]required

**liquidity_10** string,null<big-decimal>[]required

**liquidity_100** string,null<big-decimal>[]required

**slippage_1k** string,null<big-decimal>[]required

**slippage_10k** string,null<big-decimal>[]required

**slippage_100k** string,null<big-decimal>[]required

**slippage_1m** string,null<big-decimal>[]required

**slippage1k** string,null<big-decimal>[]required

**slippage10k** string,null<big-decimal>[]required

**slippage100k** string,null<big-decimal>[]required

**slippage1m** string,null<big-decimal>[]required

**bestPrice** string,null<big-decimal>[]required

**liquidity005** string,null<big-decimal>[]required

**liquidity01** string,null<big-decimal>[]required

**liquidity025** string,null<big-decimal>[]required

**liquidity05** string,null<big-decimal>[]required

**liquidity10** string,null<big-decimal>[]required

**liquidity100** string,null<big-decimal>[]required

            ↳ **ask** `object` *required*

oneOf
* Orderbook spread data
* Orderbook liquidity data
* Orderbook slippage data
* Combination of all orderbook metrics

                ↳ **best_price** `string,null<big-decimal>[]` *required*

**liquidity_005** string,null<big-decimal>[]required

**liquidity_01** string,null<big-decimal>[]required

**liquidity_025** string,null<big-decimal>[]required

**liquidity_05** string,null<big-decimal>[]required

**liquidity_10** string,null<big-decimal>[]required

**liquidity_100** string,null<big-decimal>[]required

**slippage_1k** string,null<big-decimal>[]required

**slippage_10k** string,null<big-decimal>[]required

**slippage_100k** string,null<big-decimal>[]required

**slippage_1m** string,null<big-decimal>[]required

**slippage1k** string,null<big-decimal>[]required

**slippage10k** string,null<big-decimal>[]required

**slippage100k** string,null<big-decimal>[]required

**slippage1m** string,null<big-decimal>[]required

**bestPrice** string,null<big-decimal>[]required

**liquidity005** string,null<big-decimal>[]required

**liquidity01** string,null<big-decimal>[]required

**liquidity025** string,null<big-decimal>[]required

**liquidity05** string,null<big-decimal>[]required

**liquidity10** string,null<big-decimal>[]required

**liquidity100** string,null<big-decimal>[]required

**buyVolume** string<big-decimal>[]required

**sellVolume** string<big-decimal>[]required

                ↳ **cvd** `string<big-decimal>[]` *required*

**top20Percent** objectrequired

**openInterest** string<big-decimal>[]required

**longCount** integer[]required

**shortCount** integer[]required

**longPercent** string<big-decimal>[]required

**shortPercent** string<big-decimal>[]required

                ↳ **ratio** `string<big-decimal>[]` *required*

**usdValue** string<big-decimal>[]required

                ↳ **basis** `string<big-decimal>[]` *required*

                ↳ **rate** `array[]` *required*

**Possible values:** `>= 4`, `<= 4`

**relativeRate** array[]required

**Possible values:** `>= 4`, `<= 4`

                    ↳ **errors** `object[]` *required*

  * Array [

                        ↳ **severity** `string` *required*

                        ↳ **error_class** `string` *required*

                        ↳ **type** `string` *required*

                        ↳ **msg** `string`

                        ↳ **value** `string`

                        ↳ **field** `string`

  * ]

Symbol or analytics type could not be found

  * application/json
* Schema

**Schema**

**result** `object` *required*

    ↳ **timestamp** `integer[]` *required*

    ↳ **more** `boolean` *required*

True if there are more candles in time range

    ↳ **data** `object` *required*

oneOf
* MOD1
* Statistic of long and short positions
* Orderbook analytics data
* AnalyticsCvdData
* AnalyticsTopTradersData
* AnalyticsLiquidityPoolData
* AnalyticsFutureBasisData
* AnalyticsFundingData

  * Array [

oneOf
* MOD1
* MOD2
* Ohlc

****number

****string

  * Array [

****number

  * ]

  * ]

**longCount** integer[]

**shortCount** integer[]

**longPercent** string<big-decimal>[]

**shortPercent** string<big-decimal>[]

        ↳ **ratio** `string<big-decimal>[]` *required*

        ↳ **bid** `object` *required*

oneOf
* Orderbook spread data
* Orderbook liquidity data
* Orderbook slippage data
* Combination of all orderbook metrics

            ↳ **best_price** `string,null<big-decimal>[]` *required*

**liquidity_005** string,null<big-decimal>[]required

**liquidity_01** string,null<big-decimal>[]required

**liquidity_025** string,null<big-decimal>[]required

**liquidity_05** string,null<big-decimal>[]required

**liquidity_10** string,null<big-decimal>[]required

**liquidity_100** string,null<big-decimal>[]required

**slippage_1k** string,null<big-decimal>[]required

**slippage_10k** string,null<big-decimal>[]required

**slippage_100k** string,null<big-decimal>[]required

**slippage_1m** string,null<big-decimal>[]required

**slippage1k** string,null<big-decimal>[]required

**slippage10k** string,null<big-decimal>[]required

**slippage100k** string,null<big-decimal>[]required

**slippage1m** string,null<big-decimal>[]required

**bestPrice** string,null<big-decimal>[]required

**liquidity005** string,null<big-decimal>[]required

**liquidity01** string,null<big-decimal>[]required

**liquidity025** string,null<big-decimal>[]required

**liquidity05** string,null<big-decimal>[]required

**liquidity10** string,null<big-decimal>[]required

**liquidity100** string,null<big-decimal>[]required

            ↳ **ask** `object` *required*

oneOf
* Orderbook spread data
* Orderbook liquidity data
* Orderbook slippage data
* Combination of all orderbook metrics

                ↳ **best_price** `string,null<big-decimal>[]` *required*

**liquidity_005** string,null<big-decimal>[]required

**liquidity_01** string,null<big-decimal>[]required

**liquidity_025** string,null<big-decimal>[]required

**liquidity_05** string,null<big-decimal>[]required

**liquidity_10** string,null<big-decimal>[]required

**liquidity_100** string,null<big-decimal>[]required

**slippage_1k** string,null<big-decimal>[]required

**slippage_10k** string,null<big-decimal>[]required

**slippage_100k** string,null<big-decimal>[]required

**slippage_1m** string,null<big-decimal>[]required

**slippage1k** string,null<big-decimal>[]required

**slippage10k** string,null<big-decimal>[]required

**slippage100k** string,null<big-decimal>[]required

**slippage1m** string,null<big-decimal>[]required

**bestPrice** string,null<big-decimal>[]required

**liquidity005** string,null<big-decimal>[]required

**liquidity01** string,null<big-decimal>[]required

**liquidity025** string,null<big-decimal>[]required

**liquidity05** string,null<big-decimal>[]required

**liquidity10** string,null<big-decimal>[]required

**liquidity100** string,null<big-decimal>[]required

**buyVolume** string<big-decimal>[]required

**sellVolume** string<big-decimal>[]required

                ↳ **cvd** `string<big-decimal>[]` *required*

**top20Percent** objectrequired

**openInterest** string<big-decimal>[]required

**longCount** integer[]required

**shortCount** integer[]required

**longPercent** string<big-decimal>[]required

**shortPercent** string<big-decimal>[]required

                ↳ **ratio** `string<big-decimal>[]` *required*

**usdValue** string<big-decimal>[]required

                ↳ **basis** `string<big-decimal>[]` *required*

                ↳ **rate** `array[]` *required*

**Possible values:** `>= 4`, `<= 4`

**relativeRate** array[]required

**Possible values:** `>= 4`, `<= 4`

                    ↳ **errors** `object[]` *required*

  * Array [

                        ↳ **severity** `string` *required*

                        ↳ **error_class** `string` *required*

                        ↳ **type** `string` *required*

                        ↳ **msg** `string`

                        ↳ **value** `string`

                        ↳ **field** `string`

  * ]
* curl
  * python
  * go
  * nodejs
* CURL

    
    
    curl -L 'https://futures.kraken.com/api/charts/v1/analytics/:symbol/:analytics_type' \  
    -H 'Accept: application/json'  
    

Request Collapse all

Base URL

https://futures.kraken.com/api/charts/v1

Parameters

symbol — pathrequired

analytics_type — pathrequired

\---open-interestaggressor-differentialtrade-volumetrade-countliquidation-volumerolling-volatilitylong-short-ratiolong-short-infocvdtop-tradersorderbookspreadsliquidityslippagefuture-basisfunding

since — queryrequired

interval — queryrequired

\---6030090018003600144004320086400604800

to — query

ResponseClear

Click the `Send API Request` button above and see the response here!