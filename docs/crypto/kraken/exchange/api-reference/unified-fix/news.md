---
api_type: reference
source_type: llms_txt
version: ''
scope: crypto
asset_class: digital_asset
domain: exchanges
provider: kraken
provider_name: Kraken
product: api
product_id: kraken
source_url: 'https://docs.kraken.com/exchange/api-reference/unified-fix/news'
updated_at: 2026-11-13
---

# News

> News via FIX

FIX
session: market-data
35=B

News messages are disseminated for upcoming maintenance or emergency events when a subscription is requested through the Trading Session Status Request (/exchange/api-reference/unified-fix/tssr).

***

**header** *required*

35=`B`

**41 - OrigTime** `UTCTimestamp` *required*

Event emission time

**61 - Urgency** `integer` *required*

**Possible values:**

* `0` : Scheduled maintenance
* `1` : Emergency

**148 - Headline** `string` *required*

`event.title` OR `Emergency: <incident_status>`

**149 - URLLink** `string`

Status page link

**62 - ValidUntilTime** `string`

SExpected end of the maintenance window

**33 - LinesOfText** `integer` *required*

Always 1

**58 - Text** `string` *required*

Full advisory text

**1472 - NewID** `string` *required*

Unique identifier of the news message

**1473 - NewsCategory** `integer` *required*

Always "3 - Technical New"

**1476 - NewsRefID** `string`

When present, points at the NewsID of the previous message for the same logical event. Used for phase transitions and event closure.

**1477 - NewsRefType** `integer`

0 (Replacement) — the newer message supersedes the referenced one

**5203 - KrakenEventPhase** `sring` *required*

**Possible values:**

* announced | reminder\_24h | approaching\_30mimminent\_5m | final\_warning\_30s | cancelled (maintenance);
* investigating | identified | monitoring | resolved (emergency)

**5204 - KrakenAffectedServices** `string` *required*

**Possible values:**

* spot\_fix
* spot\_ws
* spot\_rest,futures\_fix
* futures\_rest
* futures\_ws

**5205 - KrakenExpectedStartUTC** `UTCTime`

Maintenance Only. Window start time.

**5206 - KrakenExpectedEndUTC** `UTCTime`

Maintenance Only. Window stendart time.

**5207 - KrakenCancelBeforeUTC** `UTCTime`

Maintenance Only. Pre-window marker

**5208 - KrakenRecommendedAction** `string`

Maintenance Only. Client Action.
**Possible values:**

* continue
* reduce\_activity
* cancel\_open\_orders
* stop\_new\_orders
* disconnect\_and\_wait

**5209 - KrakenOrderSubmission** `string`

Maintenance Only. Trading advisability
**Possible values:**

* allowed
* discouraged
* blocked

**5210 - KrakenTimeToStartSec** `integer`

Maintenance Only. Seconds to start.

**5211 - KrakenNextStepType** `string`

Emergency Only. Expected next state.
**Possible values:**

* expected\_restart
* expected\_cancel\_only
* expected\_post\_only
* expected\_online

**5212 - KrakenNextStepAtUTC** `UTCTime`

Emergency Only. Next steps.

**5213 - KrakenNextStepAppliesTo** `string`

Emergency Only.

**trailer** *required*

```New message Example theme={null}
8=FIX.4.4|35=B|49=KRAKEN-TRD|56=QAProdFIXtesting|33=1|58=We will be performing scheduled maintenance on August 7 between 08:00-08:05 am UTC. Clients may experience brief connection errors or service interruptions lasting up to 60 seconds. Trading is not affected.|42=20260806-15:34:02.769|61=0|62=20260807-08:05:00.000|148=Scheduled Maintenance - Website|1472=maint-16-r5|1473=3|5203=reminder_24h|5204=spot_trading|5205=20260807-08:00:00.000|5206=20260807-08:05:00.000|5207=20260807-07:55:00.000|5208=continue|5209=allowed|5210=59157|10=206|
```
