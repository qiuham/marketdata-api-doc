---
exchange: bitget
source_url: https://www.bitget.com/docs/catalog/reality
api_type: REST
updated_at: 2026-11-18 19:01:32.809802
---

# Reality

Reality (rToken) trading guide, market data, and order placement/cancellation APIs.

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `GET /api/v3/reality/market/company-overview` — Get Company Overview
- `GET /api/v3/reality/market/valuation-indicators` — Get Valuation Indicators
- `GET /api/v3/reality/market/earnings-forecast` — Get Earnings Forecast
- `GET /api/v3/reality/market/suspension-resumption-info` — Get Suspension Resumption Info
- `GET /api/v3/reality/market/dividends` — Get Dividends
- `GET /api/v3/reality/market/share-capital-change` — Get Share Capital Change
- `GET /api/v3/reality/market/inner-trades` — Get Inner Trades
- `GET /api/v3/reality/market/executive-shareholdings` — Get Executive Shareholdings
- `GET /api/v3/reality/market/sharehold-detail` — Get Sharehold Detail
- `GET /api/v3/account/reality-orderbook` — Get Reality OrderBook
- `GET /api/v3/account/reality-orderbook-segmented` — Get Reality OrderBook Segmented
- `GET /api/v3/account/reality-fills` — Get Reality Fills
- `GET /api/v3/reality/market/stock-info` — Get Stock Info
- `GET /api/v3/reality/market/states` — Get Market States
- `GET /api/v3/reality/market/calendar` — Get Market Calendar
- `POST /api/v3/trade/place-reality-order` — Place Reality Order
- `POST /api/v3/trade/cancel-reality-order` — Cancel Reality Order

## Get Company Overview

`GET /api/v3/reality/market/company-overview`

Get company overview information for a specified stock.

- Rate limit: 1/sec/IP

- Permission: None

Operation ID: `realityBasicInfoGetCompanyOverview`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| code | query | string | 是 | Company code<br><br>e.g., `MU` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.peRatio | string |  | P/E ratio |
| data.pbRatio | string |  | P/B ratio |
| data.totalShares | string |  | Total shares outstanding |
| data.marketCap | string |  | Total market cap |
| data.high52Week | string |  | 52-week high price |
| data.low52Week | string |  | 52-week low price |
| data.code | string |  | Company code |
| data.name | string |  | Company name |
| data.ListingDate | string |  | Listing date |
| data.employees | string |  | Number of employees |
| data.companyAddress | string |  | Company address |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "peRatio": "12.5",
    "pbRatio": "3.2",
    "totalShares": "1100000000",
    "marketCap": "120000000000",
    "high52Week": "150.00",
    "low52Week": "60.00",
    "code": "MU",
    "name": "Micron Technology, Inc.",
    "ListingDate": "1984-06-01",
    "employees": "48000",
    "companyAddress": "8000 S. Federal Way, Boise, ID 83716-9632"
  }
}
```

## Get Valuation Indicators

`GET /api/v3/reality/market/valuation-indicators`

Get valuation indicators for a specified stock.

- Rate limit: 1/sec/IP

- Permission: None

Operation ID: `realityBasicInfoGetValuationIndicators`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| code | query | string | 是 | Company code<br><br>e.g., `MU` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.date | string |  | Data date |
| data.pb | string |  | P/B ratio |
| data.pbEd | string |  | P/B ratio (period-end) |
| data.pbPd | string |  | P/B ratio (period-average) |
| data.pbMrq | string |  | P/B ratio (most recent quarter) |
| data.pe | string |  | P/E ratio |
| data.peLyr | string |  | P/E ratio (LYR) |
| data.peTtmEd | string |  | P/E ratio (TTM, period-end) |
| data.peTtmPd | string |  | P/E ratio (TTM, period-average) |
| data.ps | string |  | P/S ratio |
| data.psLyr | string |  | P/S ratio (LYR) |
| data.psTtmEd | string |  | P/S ratio (TTM, period-end) |
| data.psTtmPd | string |  | P/S ratio (TTM, period-average) |
| data.pcf | string |  | P/CF ratio |
| data.pcfNet | string |  | P/CF ratio (net cash flow) |
| data.pcfNetTtmEd | string |  | P/CF ratio (net cash flow, TTM, period-end) |
| data.pcfNetTtmPd | string |  | P/CF ratio (net cash flow, TTM, period-average) |
| data.pcfTtmEd | string |  | P/CF ratio (TTM, period-end) |
| data.pcfTtmPd | string |  | P/CF ratio (TTM, period-average) |
| data.evEbitda | string |  | EV/EBITDA multiple |
| data.equityValue | string |  | Equity value |
| data.grossEv | string |  | Gross enterprise value |
| data.netEv | string |  | Net enterprise value |
| data.tmvUsd | string |  | Total market value (USD) |
| data.cirTmvUsd | string |  | Circulating market value (USD) |
| data.dividendYieldTtm | string |  | Dividend yield (TTM) |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "date": "2026-08-25",
    "pb": "3.2",
    "pbEd": "3.1",
    "pbPd": "3.3",
    "pbMrq": "3.2",
    "pe": "12.5",
    "peLyr": "13.0",
    "peTtmEd": "12.4",
    "peTtmPd": "12.6",
    "ps": "2.1",
    "psLyr": "2.2",
    "psTtmEd": "2.0",
    "psTtmPd": "2.3",
    "pcf": "10.5",
    "pcfNet": "10.6",
    "pcfNetTtmEd": "10.4",
    "pcfNetTtmPd": "10.7",
    "pcfTtmEd": "10.3",
    "pcfTtmPd": "10.8",
    "evEbitda": "8.5",
    "equityValue": "120000000000",
    "grossEv": "130000000000",
    "netEv": "125000000000",
    "tmvUsd": "120000000000",
    "cirTmvUsd": "118000000000",
    "dividendYieldTtm": "0.45"
  }
}
```

## Get Earnings Forecast

`GET /api/v3/reality/market/earnings-forecast`

Get individual earnings forecast data for a specified stock.

- Rate limit: 1/sec/IP

- Permission: None

Operation ID: `realityBasicInfoGetEarningsForecast`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| code | query | string | 是 | Company code<br><br>e.g., `MU` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.fiscalYear | string |  | Fiscal year |
| data.publicationDeadline | string |  | Publication deadline |
| data.isActual | boolean |  | Whether it is an actual value<br><br>`true` Actual value<br><br>`false` Forecast value |
| data.revenue | string |  | Revenue<br><br>_The unit is million USD_ |
| data.ebit | string |  | Earnings before interest and tax<br><br>_The unit is million USD_ |
| data.netIncomeParent | string |  | Net income attributable to parent company shareholders<br><br>_The unit is million USD_ |
| data.eps | string |  | Earnings per share |
| data.bps | string |  | Book value per share |
| data.cfps | string |  | Cash flow per share |
| data.roe | string |  | Return on equity |
| data.roa | string |  | Return on assets |
| data.currency | string |  | Currency |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "fiscalYear": "2026",
    "publicationDeadline": "2026-09-30",
    "isActual": false,
    "revenue": "35000",
    "ebit": "9000",
    "netIncomeParent": "7500",
    "eps": "8.50",
    "bps": "45.20",
    "cfps": "12.30",
    "roe": "0.18",
    "roa": "0.10",
    "currency": "USD"
  }
}
```

## Get Suspension Resumption Info

`GET /api/v3/reality/market/suspension-resumption-info`

Get suspension and resumption information for a specified stock company.

- Rate limit: 1/sec/IP

- Permission: None

Operation ID: `realityBasicInfoGetSuspensionResumptionInfo`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| code | query | string | 是 | Company code<br><br>e.g., `MU` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.code | string |  | Company code<br><br>e.g., `MU` |
| data.name | string |  | Company name<br><br>_Returned based on locale, e.g. Micron Technology in Chinese, `MU` in English_ |
| data.suspensionDate | string |  | Suspension date |
| data.suspensionTime | string |  | Suspension time |
| data.suspensionReason | string |  | Suspension reason |
| data.suspensionPrice | string |  | Suspension price |
| data.resumptionDate | string |  | Resumption date |
| data.resumptionQuoteTime | string |  | Resumption quote time |
| data.resumptionTradingTime | string |  | Resumption trading time |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "code": "MU",
    "name": "MU",
    "suspensionDate": "2026-08-20",
    "suspensionTime": "09:30:00",
    "suspensionReason": "Pending material announcement",
    "suspensionPrice": "120.50",
    "resumptionDate": "2026-08-21",
    "resumptionQuoteTime": "09:00:00",
    "resumptionTradingTime": "09:30:00"
  }
}
```

## Get Dividends

`GET /api/v3/reality/market/dividends`

Get dividend and split history records for a specified stock.

- Rate limit: 1/sec/IP

- Permission: None

Operation ID: `realityBasicInfoGetDividends`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| code | query | string | 是 | Company code<br><br>e.g., `MU` |
| limit | query | string |  | Limit per page <br><br>Default:`20`. Maximum:`100` |
| cursor | query | string |  | Cursor <br><br>Pagination is implemented by omitting the cursor in the first query and applying the cursor from the previous query for subsequent pages |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | object[] |  | Dividend and split list |
| data.list[].type | string |  | Type<br><br>`cash_dividend` Cash dividend<br><br>`stock_split` Stock split<br><br>`stock_dividend` Stock dividend |
| data.list[].announcementDate | string |  | Announcement date |
| data.list[].recordDate | string |  | Record date |
| data.list[].exrightDate | string |  | Ex-dividend/ex-rights date |
| data.list[].dividendDate | string |  | Dividend payment date |
| data.list[].dividendPerShare | string |  | Cash dividend per share |
| data.list[].stockDividendPerShare | string |  | Stock dividend per share |
| data.list[].splitValidDate | string |  | Split effective date |
| data.list[].splitNumerator | string |  | Split numerator |
| data.list[].splitDenominator | string |  | Split denominator |
| data.cursor | string |  | Cursor |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "list": [
      {
        "type": "cash_dividend",
        "announcementDate": "2026-05-10",
        "recordDate": "2026-06-01",
        "exrightDate": "2026-06-02",
        "dividendDate": "2026-06-15",
        "dividendPerShare": "0.12",
        "stockDividendPerShare": "",
        "splitValidDate": "",
        "splitNumerator": "",
        "splitDenominator": ""
      }
    ],
    "cursor": "1233319323918499840"
  }
}
```

## Get Share Capital Change

`GET /api/v3/reality/market/share-capital-change`

Get share capital change data for a specified stock.

- Rate limit: 1/sec/IP

- Permission: None

Operation ID: `realityBasicInfoGetShareCapitalChange`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| code | query | string | 是 | Company code<br><br>e.g., `MU` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.announcementDate | string |  | Announcement date |
| data.changeDate | string |  | Change date |
| data.totalShares | string |  | Total shares |
| data.commonShares | string |  | Common shares |
| data.preferredShares | string |  | Preferred shares |
| data.otherShares | string |  | Shares of other categories |
| data.specialExplain | string |  | Special explanation of share structure |
| data.changeReason | string |  | Reason for change |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "announcementDate": "2026-08-10",
    "changeDate": "2026-08-01",
    "totalShares": "1100000000",
    "commonShares": "1100000000",
    "preferredShares": "0",
    "otherShares": "0",
    "specialExplain": "",
    "changeReason": "Employee stock incentive plan exercise"
  }
}
```

## Get Inner Trades

`GET /api/v3/reality/market/inner-trades`

Get insider trading information for a specified stock company.

- Rate limit: 1/sec/IP

- Permission: None

Operation ID: `realityBasicInfoGetInnerTrades`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| code | query | string | 是 | Company code<br><br>e.g., `MU` |
| limit | query | string |  | Limit per page <br><br>Default:`20`. Maximum:`100` |
| cursor | query | string |  | Cursor <br><br>Pagination is implemented by omitting the cursor in the first query and applying the cursor from the previous query for subsequent pages |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | object[] |  | Insider trading list |
| data.list[].reporterName | string |  | Reporter name |
| data.list[].issueOrgName | string |  | Issuer organization name |
| data.list[].endDate | string |  | End date |
| data.list[].announcementDate | string |  | Announcement date |
| data.list[].innerType | string |  | Insider type<br><br>e.g. Director, Officer, etc. |
| data.list[].position | string |  | Specific position |
| data.list[].securityTitle | string |  | Security title |
| data.list[].tradeDate | string |  | Trade date |
| data.list[].designatedExerciseDate | string |  | Designated exercise date |
| data.list[].innerTradeType | string |  | Insider trade type<br><br>P: Purchase; S: Sale; A: Award; F: TaxWithholding; M: Exempt; C: Conversion; G: Gift; J: Other |
| data.list[].actionType | string |  | Holding change direction<br><br>`add` Increase<br><br>`decrease` Decrease |
| data.list[].tradeVolume | string |  | Trade volume |
| data.list[].tradePrice | string |  | Trade price |
| data.list[].holdingType | string |  | Holding type<br><br>`direct` Direct holding<br><br>`indirect` Indirect holding |
| data.list[].indirectHoldingStatement | string |  | Indirect holding statement |
| data.list[].postTradeQuantity | string |  | Post-trade holding quantity |
| data.cursor | string |  | Cursor |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "list": [
      {
        "reporterName": "John Smith",
        "issueOrgName": "Micron Technology Inc",
        "endDate": "2026-08-15",
        "announcementDate": "2026-08-16",
        "innerType": "Director",
        "position": "Chief Financial Officer",
        "securityTitle": "Common Stock",
        "tradeDate": "2026-08-14",
        "designatedExerciseDate": "",
        "innerTradeType": "S",
        "actionType": "decrease",
        "tradeVolume": "5000",
        "tradePrice": "120.50",
        "holdingType": "direct",
        "indirectHoldingStatement": "",
        "postTradeQuantity": "45000"
      }
    ],
    "cursor": "1233319323918499840"
  }
}
```

## Get Executive Shareholdings

`GET /api/v3/reality/market/executive-shareholdings`

Get executive shareholding details for a specified stock.

- Rate limit: 1/sec/IP

- Permission: None

Operation ID: `realityBasicInfoGetExecutiveShareholdings`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| code | query | string | 是 | Company code<br><br>e.g., `MU` |
| limit | query | string |  | Limit per page <br><br>Default:`20`. Maximum:`100` |
| cursor | query | string |  | Cursor <br><br>Pagination is implemented by omitting the cursor in the first query and applying the cursor from the previous query for subsequent pages |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | object[] |  | Executive shareholding list |
| data.list[].name | string |  | Name |
| data.list[].holdingNum | string |  | Total shares held |
| data.list[].holdingRatio | string |  | Total shareholding ratio |
| data.list[].voteRatio | string |  | Total voting ratio |
| data.list[].period | string |  | Reporting period |
| data.list[].announcementDate | string |  | Announcement date |
| data.cursor | string |  | Cursor |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "list": [
      {
        "name": "John Smith",
        "holdingNum": "45000",
        "holdingRatio": "0.03",
        "voteRatio": "0.03",
        "period": "2026Q2",
        "announcementDate": "2026-08-16"
      }
    ],
    "cursor": "1233319323918499840"
  }
}
```

## Get Sharehold Detail

`GET /api/v3/reality/market/sharehold-detail`

Get major shareholder shareholding details for a specified stock.

- Rate limit: 1/sec/IP

- Permission: None

Operation ID: `realityBasicInfoGetShareholdDetail`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| code | query | string | 是 | Company code<br><br>e.g., `MU` |
| limit | query | string |  | Limit per page <br><br>Default:`20`. Maximum:`100` |
| cursor | query | string |  | Cursor <br><br>Pagination is implemented by omitting the cursor in the first query and applying the cursor from the previous query for subsequent pages |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | object[] |  | Major shareholder shareholding list |
| data.list[].name | string |  | Name |
| data.list[].holdingNum | string |  | Total shares held |
| data.list[].holdingRatio | string |  | Total shareholding ratio |
| data.cursor | string |  | Cursor |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "list": [
      {
        "name": "The Vanguard Group, Inc.",
        "holdingNum": "120000000",
        "holdingRatio": "0.109"
      }
    ],
    "cursor": "1233319323918499840"
  }
}
```

## Get Reality OrderBook

`GET /api/v3/account/reality-orderbook`

Rate limit: 10/sec/UID

Permission: UTA trade (read)

Query the order book depth snapshot for a specified Reality (US stock) trading pair (up to 40 levels). The depth data returned is raw (unaggregated).

This is the merged (onshore + offshore) depth. See also **Get Reality OrderBook Segmented**, which breaks down onshore and offshore quantities separately.

Access requirements: This endpoint requires API Key authentication. You must contact your Business Development (BD) representative in advance to apply for whitelist access.

Operation ID: `realityMarketDataGetOrderBook`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Trading pair<br><br>e.g., `RAAPLUSDT` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.symbol | string |  | Trading pair |
| data.a | string[][] |  | Sell asks. Sorted by price in ascending order |
| data.b | string[][] |  | Buy bids. Sorted by price in descending order |
| data.ts | string |  | Data snapshot timestamp<br><br>A Unix timestamp in milliseconds |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "symbol": "RAAPLUSDT",
    "a": [
      [
        "227.55",
        "80"
      ],
      [
        "227.60",
        "300"
      ]
    ],
    "b": [
      [
        "227.50",
        "100"
      ],
      [
        "227.45",
        "250"
      ]
    ],
    "ts": "1740000000000"
  }
}
```

## Get Reality OrderBook Segmented

`GET /api/v3/account/reality-orderbook-segmented`

Rate limit: 10/sec/UID

Permission: UTA trade (read)

Query the segmented order book depth snapshot for a specified Reality (US stock) trading pair (up to 50 levels). Each price level reports onshore (internal) and offshore (external) quantities separately.

Access requirements: This endpoint requires API Key authentication. You must contact your Business Development (BD) representative in advance to apply for whitelist access.

Operation ID: `realityMarketDataGetOrderBookSegmented`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Trading pair<br><br>e.g., `RAAPLUSDT` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.symbol | string |  | Trading pair |
| data.a | string[][] |  | Sell asks. Sorted by price in ascending order |
| data.b | string[][] |  | Buy bids. Sorted by price in descending order |
| data.ts | string |  | Data snapshot timestamp<br><br>A Unix timestamp in milliseconds |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "symbol": "RAAPLUSDT",
    "a": [
      [
        "227.55",
        "60",
        "20"
      ],
      [
        "227.60",
        "200",
        "100"
      ]
    ],
    "b": [
      [
        "227.50",
        "80",
        "20"
      ],
      [
        "227.45",
        "250",
        "0"
      ]
    ],
    "ts": "1740000000000"
  }
}
```

## Get Reality Fills

`GET /api/v3/account/reality-fills`

Rate limit: 10/sec/UID

Permission: UTA trade (read)

Query recent platform fill records for a specified Reality (US stock) trading pair. This endpoint only returns fills from the last 3 months.

Access requirements: This endpoint requires API Key authentication. You must contact your Business Development (BD) representative in advance to apply for whitelist access.

Operation ID: `realityMarketDataGetFills`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Trading pair<br><br>e.g., `RAAPLUSDT`. Only Reality trading pairs are supported |
| limit | query | string |  | Limit per page<br><br>Default: `100`. Maximum: `100` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].execId | string |  | Fill ID |
| data[].price | string |  | Fill price |
| data[].size | string |  | Fill quantity<br><br>Unit: base coin |
| data[].side | string |  | Trade side<br><br>`buy` Buy<br><br>`sell` Sell |
| data[].execVenue | string |  | Execution venue<br><br>`internal_market` Internal fill: matched in the internal order book<br><br>`lit_market` Lit market fill: routed to an external broker and executed on the public market<br><br>Note: `execVenue` is where the fill actually took place, which differs from the `venue` order parameter (routing strategy) |
| data[].ts | string |  | Fill time<br><br>A Unix timestamp in milliseconds |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": [
    {
      "execId": "1234567890",
      "price": "227.50",
      "size": "10",
      "side": "buy",
      "execVenue": "internal_market",
      "ts": "1740000000000"
    }
  ]
}
```

## Get Stock Info

`GET /api/v3/reality/market/stock-info`

Get stock information for a specified Reality (US stock) trading pair.

- Rate limit: 1/sec/IP

- Permission: None

Operation ID: `realityMarketDataGetStockInfo`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string |  | Trading pair<br><br>e.g., `RAAPLUSDT`<br><br>If not provided, all trading pairs will be returned |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].symbol | string |  | Trading pair name |
| data[].code | string |  | Stock ticker symbol<br><br>e.g., `AAPL` |
| data[].name | string |  | Company name |
| data[].tradingPeriod | string |  | Tradable sessions<br><br>`pre_market` Pre-market<br><br>`regular` Regular hours<br><br>`after_hours` After-hours<br><br>`overnight` Overnight |
| data[].weekendTradable | string |  | Weekend trading availability<br><br>`yes` Supported<br><br>`no` Not supported |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": [
    {
      "symbol": "RAAPLUSDT",
      "code": "AAPL",
      "name": "Apple Inc.",
      "tradingPeriod": [
        "pre_market",
        "regular",
        "after_hours"
      ],
      "weekendTradable": "yes"
    }
  ]
}
```

## Get Market States

`GET /api/v3/reality/market/states`

Get stock market status information.

:::info US Stock Trading Hours

Pre-market session: ET 04:00 – 09:30

Regular session: ET 09:30 – 16:00

After-hours session: ET 16:00 – 20:00

Overnight session: ET 20:00 – 04:00 (T+1)

:::

- Rate limit: 1/sec/IP

- Permission: None

Operation ID: `realityMarketDataGetMarketStates`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].market | string |  | Market<br><br>Currently only `US` (US equities) is supported |
| data[].daylightType | string |  | Daylight saving type<br><br>`standard` Standard time (winter)<br><br>`dst` Daylight saving time (summer) |
| data[].stateList | object[] |  | List of market session states |
| data[].stateList[].state | string |  | Session state<br><br>`pre_market` Pre-market<br><br>`regular` Regular hours<br><br>`after_hours` After-hours<br><br>`overnight` Overnight |
| data[].stateList[].timeZone | string |  | Time zone<br><br>Currently only `ET` is supported |
| data[].stateList[].startTime | string |  | Session start time<br><br>e.g., `04:00` |
| data[].stateList[].endTime | string |  | Session end time<br><br>e.g., `09:30` |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": [
    {
      "market": "US",
      "daylightType": "dst",
      "stateList": [
        {
          "state": "pre_market",
          "timeZone": "ET",
          "startTime": "04:00",
          "endTime": "09:30"
        },
        {
          "state": "regular",
          "timeZone": "ET",
          "startTime": "09:30",
          "endTime": "16:00"
        }
      ]
    }
  ]
}
```

## Get Market Calendar

`GET /api/v3/reality/market/calendar`

Get the market holiday and closure calendar for US stocks.

- Rate limit: 1/sec/IP

- Permission: None

Operation ID: `realityMarketDataGetMarketCalendar`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.timeZone | string |  | Time zone<br><br>Always returns `EST` |
| data.specificConfig | object[] |  | Special closure list<br><br>Used for non-regular closures such as holidays or special events |
| data.specificConfig[].remark | string |  | Closure remark |
| data.specificConfig[].startTime | string |  | Closure start time<br><br>Format: `YYYY-MM-DD HH:mm` |
| data.specificConfig[].endTime | string |  | Closure end time<br><br>Format: `YYYY-MM-DD HH:mm` |
| data.regularConfig | string[] |  | Regular closure list<br><br>Used for regular weekend closures<br><br>e.g., `SATURDAY`, `SUNDAY` |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1787212600475,
  "data": {
    "timeZone": "EST",
    "specificConfig": [
      {
        "remark": "",
        "startTime": "2026-06-18 20:00",
        "endTime": "2026-06-19 20:00"
      }
    ],
    "regularConfig": [
      "SATURDAY",
      "SUNDAY"
    ]
  }
}
```

## Place Reality Order

`POST /api/v3/trade/place-reality-order`

Rate limit (determined by `venue`):

`internal_market` (on-exchange): follows the Crypto rate limit, 10/sec/UID

Default strategy (`venue` omitted) and `lit_market` (off-exchange): follow the rToken rate limit, 5/sec/UID by default, 30/sec/UID for whitelisted users (users can contact their BD/RM to apply)

Permission: UTA trade (read & write)

Place a limit or market order for Reality stock trading pairs.

> Order modification is not supported for rToken orders. To change the price or quantity of a resting order, cancel it and place a new one. See the [Reality Trading Guide](/docs/uta/reality-trading-guide) for details on order routing (`venue`) and matching mechanics.

Operation ID: `realityTradingPlaceOrder`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| category | query | string |  | Category<br><br>`SPOT` Spot trading<br><br>`MARGIN` Margin trading<br><br>Default: `SPOT` |
| symbol | query | string | 是 | Symbol name<br><br>e.g., `rAAPLUSDT`<br><br>This endpoint only supports Reality stock trading pairs |
| side | query | string | 是 | Order side<br><br>`buy` Buy<br><br>`sell` Sell |
| orderType | query | string | 是 | Order type<br><br>`limit` Limit order<br><br>`market` Market order |
| qty | query | string | 是 | Order quantity<br><br>For market buy orders, the unit is **quote coin**<br><br>For limit and market sell orders, the unit is **base coin** |
| price | query | string |  | Order price<br><br>Required when `orderType=limit` |
| clientOid | query | string |  | Client order ID |
| venue | query | string |  | Order routing strategy<br><br>`internal_market` Orders are matched only within the exchange and are never submitted to the U.S. stock broker, regardless of whether the U.S. market is open or closed<br><br>`lit_market` Orders are submitted to the U.S. stock broker for execution. During U.S. market hours they are not matched within the exchange; while the U.S. market is closed (e.g. weekends) the broker is unavailable, so these orders rest internally within the exchange and the unfilled portion is routed to the broker once the market reopens<br><br>If not provided, the default strategy applies: orders are first matched internally within the exchange at the best price; any unfilled portion is submitted to the broker<br><br>See the [Reality Trading Guide](/docs/uta/reality-trading-guide) for strategy details and open/closed-market behavior differences |
| rTokenTimeInForce | query | string |  | Order execution strategy<br><br>`gtd` Valid for the current session. If placed during US market trading hours (weekdays), the limit order is valid until the end of after-hours trading; if placed on weekends, it is valid until just before the next US market open<br><br>`gtc` Valid for 90 days<br><br>If not provided, defaults to `gtd` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | Order ID |
| data.clientOid | string |  | Client order ID. Returns an empty string if not provided |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695806875837,
  "data": {
    "orderId": "121211212122",
    "clientOid": "myOrder001"
  }
}
```

## Cancel Reality Order

`POST /api/v3/trade/cancel-reality-order`

Rate limit: same as Crypto

Permission: UTA trade (read & write)

Cancel an unfilled or partially filled Reality stock order.

Operation ID: `realityTradingCancelOrder`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| category | query | string |  | Category<br><br>`SPOT` Spot trading<br><br>`MARGIN` Margin trading<br><br>Default: `SPOT` |
| symbol | query | string | 是 | Symbol name<br><br>e.g., `rAAPLUSDT` |
| orderId | query | string |  | Order ID<br><br>Either `orderId` or `clientOid` must be provided. If both are provided, `orderId` takes priority |
| clientOid | query | string |  | Client order ID<br><br>Either `orderId` or `clientOid` must be provided. If both are provided, `orderId` takes priority |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | Order ID |
| data.clientOid | string |  | Client order ID. Returns an empty string if not provided |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695806875837,
  "data": {
    "orderId": "121211212122",
    "clientOid": "myOrder001"
  }
}
```


---

Reality（rToken）交易指南、行情数据以及下单/撤单接口。

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `GET /api/v3/reality/market/company-overview` — 获取公司概况
- `GET /api/v3/reality/market/valuation-indicators` — 获取估值指标
- `GET /api/v3/reality/market/earnings-forecast` — 获取盈利预测
- `GET /api/v3/reality/market/suspension-resumption-info` — 获取停复牌资讯
- `GET /api/v3/reality/market/dividends` — 获取分红与拆分
- `GET /api/v3/reality/market/share-capital-change` — 获取股本变动
- `GET /api/v3/reality/market/inner-trades` — 获取内部人交易
- `GET /api/v3/reality/market/executive-shareholdings` — 获取管理层持股明细
- `GET /api/v3/reality/market/sharehold-detail` — 获取主要股东持股明细
- `GET /api/v3/account/reality-orderbook` — 获取Reality深度数据
- `GET /api/v3/account/reality-orderbook-segmented` — 获取Reality分层订单簿
- `GET /api/v3/account/reality-fills` — 获取Reality平台成交数据
- `GET /api/v3/reality/market/stock-info` — 获取股票信息
- `GET /api/v3/reality/market/states` — 获取市场状态
- `GET /api/v3/reality/market/calendar` — 获取休市日历
- `POST /api/v3/trade/place-reality-order` — 创建Reality股票订单
- `POST /api/v3/trade/cancel-reality-order` — 撤销Reality股票订单

## 获取公司概况

`GET /api/v3/reality/market/company-overview`

获取指定股票的公司概况信息。

- 限频规则: 1次/秒/IP

- 权限: 无

Operation ID: `realityBasicInfoGetCompanyOverview`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| code | query | string | 是 | 公司代码<br><br>如 `MU` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.peRatio | string |  | 市盈率 |
| data.pbRatio | string |  | 市净率 |
| data.totalShares | string |  | 总股本 |
| data.marketCap | string |  | 总市值 |
| data.high52Week | string |  | 52周最高价格 |
| data.low52Week | string |  | 52周最低价格 |
| data.code | string |  | 公司代码 |
| data.name | string |  | 公司名称 |
| data.ListingDate | string |  | 上市日期 |
| data.employees | string |  | 员工人数 |
| data.companyAddress | string |  | 公司地址 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "peRatio": "12.5",
    "pbRatio": "3.2",
    "totalShares": "1100000000",
    "marketCap": "120000000000",
    "high52Week": "150.00",
    "low52Week": "60.00",
    "code": "MU",
    "name": "Micron Technology, Inc.",
    "ListingDate": "1984-06-01",
    "employees": "48000",
    "companyAddress": "8000 S. Federal Way, Boise, ID 83716-9632"
  }
}
```

## 获取估值指标

`GET /api/v3/reality/market/valuation-indicators`

获取指定股票的估值指标数据。

- 限频规则: 1次/秒/IP

- 权限: 无

Operation ID: `realityBasicInfoGetValuationIndicators`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| code | query | string | 是 | 公司代码<br><br>如 `MU` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.date | string |  | 数据日期 |
| data.pb | string |  | 市净率 |
| data.pbEd | string |  | 市净率（期末） |
| data.pbPd | string |  | 市净率（期间均值） |
| data.pbMrq | string |  | 市净率（最新季度） |
| data.pe | string |  | 市盈率 |
| data.peLyr | string |  | 市盈率（LYR） |
| data.peTtmEd | string |  | 市盈率（TTM，期末） |
| data.peTtmPd | string |  | 市盈率（TTM，期间均值） |
| data.ps | string |  | 市销率 |
| data.psLyr | string |  | 市销率（LYR） |
| data.psTtmEd | string |  | 市销率（TTM，期末） |
| data.psTtmPd | string |  | 市销率（TTM，期间均值） |
| data.pcf | string |  | 市现率 |
| data.pcfNet | string |  | 市现率（净现金流） |
| data.pcfNetTtmEd | string |  | 市现率（净现金流，TTM，期末） |
| data.pcfNetTtmPd | string |  | 市现率（净现金流，TTM，期间均值） |
| data.pcfTtmEd | string |  | 市现率（TTM，期末） |
| data.pcfTtmPd | string |  | 市现率（TTM，期间均值） |
| data.evEbitda | string |  | 企业价值倍数 |
| data.equityValue | string |  | 股权价值 |
| data.grossEv | string |  | 企业总价值 |
| data.netEv | string |  | 企业净价值 |
| data.tmvUsd | string |  | 总市值（美元） |
| data.cirTmvUsd | string |  | 流通市值（美元） |
| data.dividendYieldTtm | string |  | 股息率（TTM） |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "date": "2026-08-25",
    "pb": "3.2",
    "pbEd": "3.1",
    "pbPd": "3.3",
    "pbMrq": "3.2",
    "pe": "12.5",
    "peLyr": "13.0",
    "peTtmEd": "12.4",
    "peTtmPd": "12.6",
    "ps": "2.1",
    "psLyr": "2.2",
    "psTtmEd": "2.0",
    "psTtmPd": "2.3",
    "pcf": "10.5",
    "pcfNet": "10.6",
    "pcfNetTtmEd": "10.4",
    "pcfNetTtmPd": "10.7",
    "pcfTtmEd": "10.3",
    "pcfTtmPd": "10.8",
    "evEbitda": "8.5",
    "equityValue": "120000000000",
    "grossEv": "130000000000",
    "netEv": "125000000000",
    "tmvUsd": "120000000000",
    "cirTmvUsd": "118000000000",
    "dividendYieldTtm": "0.45"
  }
}
```

## 获取盈利预测

`GET /api/v3/reality/market/earnings-forecast`

获取指定股票的个股盈利预测数据。

- 限频规则: 1次/秒/IP

- 权限: 无

Operation ID: `realityBasicInfoGetEarningsForecast`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| code | query | string | 是 | 公司代码<br><br>如 `MU` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.fiscalYear | string |  | 年度 |
| data.publicationDeadline | string |  | 公布截止日期 |
| data.isActual | boolean |  | 是否实际值<br><br>`true` 实际值<br><br>`false` 预测值 |
| data.revenue | string |  | 营业收入<br><br>_单位为百万美元_ |
| data.ebit | string |  | 息税前利润<br><br>_单位为百万美元_ |
| data.netIncomeParent | string |  | 归属母公司股东的净利润<br><br>_单位为百万美元_ |
| data.eps | string |  | 每股收益 |
| data.bps | string |  | 每股净资产 |
| data.cfps | string |  | 每股现金流 |
| data.roe | string |  | 净资产收益率 |
| data.roa | string |  | 总资产收益率 |
| data.currency | string |  | 货币 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "fiscalYear": "2026",
    "publicationDeadline": "2026-09-30",
    "isActual": false,
    "revenue": "35000",
    "ebit": "9000",
    "netIncomeParent": "7500",
    "eps": "8.50",
    "bps": "45.20",
    "cfps": "12.30",
    "roe": "0.18",
    "roa": "0.10",
    "currency": "USD"
  }
}
```

## 获取停复牌资讯

`GET /api/v3/reality/market/suspension-resumption-info`

获取指定股票公司的停复牌信息。

- 限频规则: 1次/秒/IP

- 权限: 无

Operation ID: `realityBasicInfoGetSuspensionResumptionInfo`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| code | query | string | 是 | 公司代码<br><br>如 `MU` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.code | string |  | 公司代码<br><br>如 `MU` |
| data.name | string |  | 公司名称<br><br>_基于语言返回，如中文为美光科技，英文为 `MU`_ |
| data.suspensionDate | string |  | 停牌日期 |
| data.suspensionTime | string |  | 停牌时间 |
| data.suspensionReason | string |  | 停牌原因 |
| data.suspensionPrice | string |  | 停牌价格 |
| data.resumptionDate | string |  | 复牌日期 |
| data.resumptionQuoteTime | string |  | 恢复报价时间 |
| data.resumptionTradingTime | string |  | 恢复交易时间 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "code": "MU",
    "name": "美光科技",
    "suspensionDate": "2026-08-20",
    "suspensionTime": "09:30:00",
    "suspensionReason": "待发布重大公告",
    "suspensionPrice": "120.50",
    "resumptionDate": "2026-08-21",
    "resumptionQuoteTime": "09:00:00",
    "resumptionTradingTime": "09:30:00"
  }
}
```

## 获取分红与拆分

`GET /api/v3/reality/market/dividends`

获取指定股票的分红派息历史记录。

- 限频规则: 1次/秒/IP

- 权限: 无

Operation ID: `realityBasicInfoGetDividends`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| code | query | string | 是 | 公司代码<br><br>如 `MU` |
| limit | query | string |  | 每页数量 <br><br>默认：`20`。最大：`100` |
| cursor | query | string |  | 游标 <br><br>首次查询不传游标，后续分页使用上一次查询返回的游标 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | object[] |  | 分红与拆分列表 |
| data.list[].type | string |  | 类型<br><br>`cash_dividend` 现金分红<br><br>`stock_split` 股票拆分<br><br>`stock_dividend` 股票分红 |
| data.list[].announcementDate | string |  | 公告日 |
| data.list[].recordDate | string |  | 股权登记日 |
| data.list[].exrightDate | string |  | 除权除息日 |
| data.list[].dividendDate | string |  | 派息日 |
| data.list[].dividendPerShare | string |  | 每股现金分红金额 |
| data.list[].stockDividendPerShare | string |  | 每股股票分红 |
| data.list[].splitValidDate | string |  | 拆分生效日期 |
| data.list[].splitNumerator | string |  | 拆分分子 |
| data.list[].splitDenominator | string |  | 拆分分母 |
| data.cursor | string |  | 游标 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "list": [
      {
        "type": "cash_dividend",
        "announcementDate": "2026-05-10",
        "recordDate": "2026-06-01",
        "exrightDate": "2026-06-02",
        "dividendDate": "2026-06-15",
        "dividendPerShare": "0.12",
        "stockDividendPerShare": "",
        "splitValidDate": "",
        "splitNumerator": "",
        "splitDenominator": ""
      }
    ],
    "cursor": "1233319323918499840"
  }
}
```

## 获取股本变动

`GET /api/v3/reality/market/share-capital-change`

获取指定股票的股本变动数据。

- 限频规则: 1次/秒/IP

- 权限: 无

Operation ID: `realityBasicInfoGetShareCapitalChange`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| code | query | string | 是 | 公司代码<br><br>如 `MU` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.announcementDate | string |  | 公告日 |
| data.changeDate | string |  | 变动日 |
| data.totalShares | string |  | 总股本 |
| data.commonShares | string |  | 普通股股数 |
| data.preferredShares | string |  | 优先股股数 |
| data.otherShares | string |  | 其他类别股股数 |
| data.specialExplain | string |  | 股本结构特殊说明 |
| data.changeReason | string |  | 变动原因 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "announcementDate": "2026-08-10",
    "changeDate": "2026-08-01",
    "totalShares": "1100000000",
    "commonShares": "1100000000",
    "preferredShares": "0",
    "otherShares": "0",
    "specialExplain": "",
    "changeReason": "员工股权激励计划行权"
  }
}
```

## 获取内部人交易

`GET /api/v3/reality/market/inner-trades`

获取指定股票公司的内部人交易信息。

- 限频规则: 1次/秒/IP

- 权限: 无

Operation ID: `realityBasicInfoGetInnerTrades`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| code | query | string | 是 | 公司代码<br><br>如 `MU` |
| limit | query | string |  | 每页条目数 <br><br>默认值20，最大值为100 |
| cursor | query | string |  | 游标ID <br><br>首次查询不传游标，后续分页使用上一次查询返回的游标 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | object[] |  | 内部人交易列表 |
| data.list[].reporterName | string |  | 报告人姓名 |
| data.list[].issueOrgName | string |  | 发行机构名称 |
| data.list[].endDate | string |  | 截止日期 |
| data.list[].announcementDate | string |  | 公告日期 |
| data.list[].innerType | string |  | 内部人类型<br><br>如Director，Officer等 |
| data.list[].position | string |  | 具体职位 |
| data.list[].securityTitle | string |  | 证券标题 |
| data.list[].tradeDate | string |  | 交易日 |
| data.list[].designatedExerciseDate | string |  | 指定行权日 |
| data.list[].innerTradeType | string |  | 内部人交易类型<br><br>P：Purchase（购买）；S：Sale（出售）；A：Award（奖励）；F：TaxWithholding（预提税）；M：Exempt（豁免）；C：Conversion（衍生品转换）；G：Gift（礼物赠予）；J：Other（其他） |
| data.list[].actionType | string |  | 持仓变化方向<br><br>`add` 增加<br><br>`decrease` 减少 |
| data.list[].tradeVolume | string |  | 交易数量 |
| data.list[].tradePrice | string |  | 交易价格 |
| data.list[].holdingType | string |  | 持有类型<br><br>`direct` 直接持有<br><br>`indirect` 非直接持有 |
| data.list[].indirectHoldingStatement | string |  | 非直接持有说明 |
| data.list[].postTradeQuantity | string |  | 交易后持股数量 |
| data.cursor | string |  | 游标ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "list": [
      {
        "reporterName": "John Smith",
        "issueOrgName": "美光科技",
        "endDate": "2026-08-15",
        "announcementDate": "2026-08-16",
        "innerType": "Director",
        "position": "首席财务官",
        "securityTitle": "普通股",
        "tradeDate": "2026-08-14",
        "designatedExerciseDate": "",
        "innerTradeType": "S",
        "actionType": "decrease",
        "tradeVolume": "5000",
        "tradePrice": "120.50",
        "holdingType": "direct",
        "indirectHoldingStatement": "",
        "postTradeQuantity": "45000"
      }
    ],
    "cursor": "1233319323918499840"
  }
}
```

## 获取管理层持股明细

`GET /api/v3/reality/market/executive-shareholdings`

获取指定股票的管理层持股明细数据。

- 限频规则: 1次/秒/IP

- 权限: 无

Operation ID: `realityBasicInfoGetExecutiveShareholdings`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| code | query | string | 是 | 公司代码<br><br>如 `MU` |
| limit | query | string |  | 每页条目数 <br><br>默认值20，最大值为100 |
| cursor | query | string |  | 游标ID <br><br>首次查询不传游标，后续分页使用上一次查询返回的游标 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | object[] |  | 管理层持股列表 |
| data.list[].name | string |  | 名称 |
| data.list[].holdingNum | string |  | 总持股数 |
| data.list[].holdingRatio | string |  | 总持股比例 |
| data.list[].voteRatio | string |  | 总投票比例 |
| data.list[].period | string |  | 所属报告期 |
| data.list[].announcementDate | string |  | 公告日期 |
| data.cursor | string |  | 游标ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "list": [
      {
        "name": "John Smith",
        "holdingNum": "45000",
        "holdingRatio": "0.03",
        "voteRatio": "0.03",
        "period": "2026Q2",
        "announcementDate": "2026-08-16"
      }
    ],
    "cursor": "1233319323918499840"
  }
}
```

## 获取主要股东持股明细

`GET /api/v3/reality/market/sharehold-detail`

获取指定股票的主要股东持股明细数据。

- 限频规则: 1次/秒/IP

- 权限: 无

Operation ID: `realityBasicInfoGetShareholdDetail`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| code | query | string | 是 | 公司代码<br><br>如 `MU` |
| limit | query | string |  | 每页条目数 <br><br>默认值20，最大值为100 |
| cursor | query | string |  | 游标ID <br><br>首次查询不传游标，后续分页使用上一次查询返回的游标 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | object[] |  | 主要股东持股列表 |
| data.list[].name | string |  | 名称 |
| data.list[].holdingNum | string |  | 总持股数 |
| data.list[].holdingRatio | string |  | 总持股比例 |
| data.cursor | string |  | 游标ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "list": [
      {
        "name": "The Vanguard Group, Inc.",
        "holdingNum": "120000000",
        "holdingRatio": "0.109"
      }
    ],
    "cursor": "1233319323918499840"
  }
}
```

## 获取Reality深度数据

`GET /api/v3/account/reality-orderbook`

限频规则: 10次/秒/UID

需要统一账户交易只读/读写权限

获取指定 Reality 美股交易对的订单簿深度快照（最多 40 档）。返回的深度数据为未合并的原始深度。

该接口为场内+场外的融合深度。另见**获取Reality分层订单簿**，分别返回场内与场外数量。

接入要求：该接口需要 API Key 认证，请提前联系 BD 申请开通白名单权限。

Operation ID: `realityMarketDataGetOrderBook`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 交易对<br><br>如 `RAAPLUSDT` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.symbol | string |  | 交易对 |
| data.a | string[][] |  | 卖盘深度，按价格升序排列 |
| data.b | string[][] |  | 买盘深度，按价格降序排列 |
| data.ts | string |  | 数据快照时间戳<br><br>Unix毫秒时间戳 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "symbol": "RAAPLUSDT",
    "a": [
      [
        "227.55",
        "80"
      ],
      [
        "227.60",
        "300"
      ]
    ],
    "b": [
      [
        "227.50",
        "100"
      ],
      [
        "227.45",
        "250"
      ]
    ],
    "ts": "1740000000000"
  }
}
```

## 获取Reality分层订单簿

`GET /api/v3/account/reality-orderbook-segmented`

限频规则: 10次/秒/UID

需要统一账户交易只读/读写权限

查询指定 Reality（美股）交易对的分层订单簿深度快照（最多50档）。每个价位分别返回场内（内部）与场外（外部）数量。

接入要求：该接口需要 API Key 认证，请提前联系 BD 申请开通白名单权限。

Operation ID: `realityMarketDataGetOrderBookSegmented`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 交易对<br><br>如 `RAAPLUSDT` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.symbol | string |  | 交易对 |
| data.a | string[][] |  | 卖盘深度，按价格升序排列 |
| data.b | string[][] |  | 买盘深度，按价格降序排列 |
| data.ts | string |  | 数据快照时间戳<br><br>Unix毫秒时间戳 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": {
    "symbol": "RAAPLUSDT",
    "a": [
      [
        "227.55",
        "60",
        "20"
      ],
      [
        "227.60",
        "200",
        "100"
      ]
    ],
    "b": [
      [
        "227.50",
        "80",
        "20"
      ],
      [
        "227.45",
        "250",
        "0"
      ]
    ],
    "ts": "1740000000000"
  }
}
```

## 获取Reality平台成交数据

`GET /api/v3/account/reality-fills`

限频规则: 10次/秒/UID

需要统一账户交易只读/读写权限

获取指定 Reality 美股交易对的平台成交历史记录。该接口仅返回近三个月的成交数据。

接入要求：该接口需要 API Key 认证，请提前联系 BD 申请开通白名单权限。

Operation ID: `realityMarketDataGetFills`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 交易对<br><br>如 `RAAPLUSDT`，仅支持传 Reality 交易对 |
| limit | query | string |  | 每页条数<br><br>默认值：`100`，最大值：`100` |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].execId | string |  | 成交ID |
| data[].price | string |  | 成交价格 |
| data[].size | string |  | 成交数量<br><br>单位为base coin |
| data[].side | string |  | 交易方向<br><br>`buy` 买入<br><br>`sell` 卖出 |
| data[].execVenue | string |  | 成交发生地<br><br>`internal_market` 内部成交：在内部订单簿成交<br><br>`lit_market` 公开市场成交：路由到外部券商，在公开市场成交<br><br>注：`execVenue` 为实际成交地，不同于下单参数 `venue`（订单路由策略） |
| data[].ts | string |  | 成交时间<br><br>Unix毫秒时间戳 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": [
    {
      "execId": "1234567890",
      "price": "227.50",
      "size": "10",
      "side": "buy",
      "execVenue": "internal_market",
      "ts": "1740000000000"
    }
  ]
}
```

## 获取股票信息

`GET /api/v3/reality/market/stock-info`

获取Reality美股指定交易对的股票信息。

- 限频规则: 1次/秒/IP

- 权限: 无

Operation ID: `realityMarketDataGetStockInfo`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string |  | 交易对<br><br>股票交易对名称，如 `RAAPLUSDT`<br><br>如不填，则返回所有交易对 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].symbol | string |  | 交易对名称 |
| data[].code | string |  | 股票代码<br><br>如 `AAPL` |
| data[].name | string |  | 公司名称 |
| data[].tradingPeriod | string |  | 可交易时段<br><br>`pre_market` 盘前<br><br>`regular` 盘中<br><br>`after_hours` 盘后<br><br>`overnight` 夜盘 |
| data[].weekendTradable | string |  | 周末可交易<br><br>`yes` 是<br><br>`no` 否 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": [
    {
      "symbol": "RAAPLUSDT",
      "code": "AAPL",
      "name": "Apple Inc.",
      "tradingPeriod": [
        "pre_market",
        "regular",
        "after_hours"
      ],
      "weekendTradable": "yes"
    }
  ]
}
```

## 获取市场状态

`GET /api/v3/reality/market/states`

获取股票市场状态信息。

:::info 美股交易时间表

盘前交易：ET 04:00 - 09:30

持续交易时段：ET 09:30 - 16:00

盘后交易时段：ET 16:00 - 20:00

夜盘交易时段：ET 20:00 - 04:00（T+1）

:::

- 限频规则: 1次/秒/IP

- 权限: 无

Operation ID: `realityMarketDataGetMarketStates`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].market | string |  | 市场<br><br>当前仅支持 `US` 美股 |
| data[].daylightType | string |  | 日照时间类型<br><br>`standard` 冬令时<br><br>`dst` 夏令时 |
| data[].stateList | object[] |  | 状态列表 |
| data[].stateList[].state | string |  | 状态<br><br>`pre_market` 盘前交易<br><br>`regular` 盘中交易<br><br>`after_hours` 盘后交易<br><br>`overnight` 夜盘交易 |
| data[].stateList[].timeZone | string |  | 时区<br><br>当前仅支持 `ET` |
| data[].stateList[].startTime | string |  | 状态开始时间<br><br>如 `04:00` |
| data[].stateList[].endTime | string |  | 状态结束时间<br><br>如 `09:30` |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": [
    {
      "market": "US",
      "daylightType": "dst",
      "stateList": [
        {
          "state": "pre_market",
          "timeZone": "ET",
          "startTime": "04:00",
          "endTime": "09:30"
        },
        {
          "state": "regular",
          "timeZone": "ET",
          "startTime": "09:30",
          "endTime": "16:00"
        }
      ]
    }
  ]
}
```

## 获取休市日历

`GET /api/v3/reality/market/calendar`

获取美股市场的休市日历信息。

- 限频规则: 1次/秒/IP

- 权限: 无

Operation ID: `realityMarketDataGetMarketCalendar`

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.timeZone | string |  | 时区<br><br>固定返回 `EST` |
| data.specificConfig | object[] |  | 特殊休市列表<br><br>用于节日或特殊事件等非常规休市场景 |
| data.specificConfig[].remark | string |  | 休市备注 |
| data.specificConfig[].startTime | string |  | 休市开始时间<br><br>年月日 时分格式 |
| data.specificConfig[].endTime | string |  | 休市结束时间<br><br>年月日 时分格式 |
| data.regularConfig | string[] |  | 常规休市列表<br><br>用于周末假日等常规休市场景<br><br>如 `SATURDAY`、`SUNDAY` |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1787212600475,
  "data": {
    "timeZone": "EST",
    "specificConfig": [
      {
        "remark": "",
        "startTime": "2026-06-18 20:00",
        "endTime": "2026-06-19 20:00"
      }
    ],
    "regularConfig": [
      "SATURDAY",
      "SUNDAY"
    ]
  }
}
```

## 创建Reality股票订单

`POST /api/v3/trade/place-reality-order`

限频规则（按 `venue` 区分）:

`internal_market`（场内）: 按 Crypto 限频规则，10次/秒/UID

默认策略（不传 `venue`）及 `lit_market`（场外）: 按 rToken 限频规则，默认 5次/秒/UID；白名单用户 30次/秒/UID（可联系对接BD/RM申请）

需要统一账户交易权限

对 Reality 股票交易对进行限价或市价下单。

> rToken订单暂不支持修改。如需调整挂单的价格或数量，请先撤单，再重新下单。订单路由（`venue`）与撮合机制详见 [Reality 交易指南](/zh-CN/docs/uta/reality-trading-guide)。

Operation ID: `realityTradingPlaceOrder`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| category | query | string |  | 交易类型<br><br>`SPOT` 现货交易<br><br>`MARGIN` 杠杆交易<br><br>默认值：`SPOT` |
| symbol | query | string | 是 | 交易对名称<br><br>如 `rAAPLUSDT`<br><br>该接口仅支持 Reality 股票交易对 |
| side | query | string | 是 | 方向<br><br>`buy` 买<br><br>`sell` 卖 |
| orderType | query | string | 是 | 订单类型<br><br>`limit` 限价单<br><br>`market` 市价单 |
| qty | query | string | 是 | 下单数量<br><br>市价买单，单位为 **quote coin**<br><br>限价及市价卖单，单位为 **base coin** |
| price | query | string |  | 委托价格<br><br>`orderType=limit` 时必传 |
| clientOid | query | string |  | 自定义订单 ID |
| venue | query | string |  | 订单路由策略<br><br>`internal_market` 订单只在交易所内撮合，不提交美股券商，不受开市/休市切换影响<br><br>`lit_market` 订单提交至美股券商执行；美股开市时段不在交易所内撮合，但美股休市（如周末）时外部券商不可用，此时订单会先在场内挂单等待撮合，待开市后未成交部分再路由至券商<br><br>如不传，为默认策略：优先交易所内部比价撮合，未成交部分提交至券商<br><br>策略细节与开休市行为差异详见 [Reality 交易指南](/zh-CN/docs/uta/reality-trading-guide) |
| rTokenTimeInForce | query | string |  | 订单执行策略<br><br>`gtd` 当前时段有效。若在美股交易时间（周中）挂单，限价单有效期至美股盘后结束；若在周末挂单，有效期至美股下次开盘前<br><br>`gtc` 订单有效期 90 天<br><br>如不传，默认值为`gtd` |

### 响应 200：成功响应

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | 系统订单 ID |
| data.clientOid | string |  | 客户端自定义订单 ID，未传则返回空字符串 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695806875837,
  "data": {
    "orderId": "121211212122",
    "clientOid": "myOrder001"
  }
}
```

## 撤销Reality股票订单

`POST /api/v3/trade/cancel-reality-order`

限频规则: 与 Crypto 一致

需要统一账户交易权限

撤销未成交或部分成交的 Reality 股票订单。

Operation ID: `realityTradingCancelOrder`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| category | query | string |  | 交易类型<br><br>`SPOT` 现货交易<br><br>`MARGIN` 杠杆交易<br><br>默认值：`SPOT` |
| symbol | query | string | 是 | 交易对名称<br><br>如 `rAAPLUSDT` |
| orderId | query | string |  | 系统订单 ID<br><br>`orderId` 与 `clientOid` 至少传其一；同时传入时 `orderId` 优先 |
| clientOid | query | string |  | 自定义订单 ID<br><br>`orderId` 与 `clientOid` 至少传其一；同时传入时 `orderId` 优先 |

### 响应 200：成功响应

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.orderId | string |  | 系统订单 ID |
| data.clientOid | string |  | 客户端自定义订单 ID，未传则返回空字符串 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695806875837,
  "data": {
    "orderId": "121211212122",
    "clientOid": "myOrder001"
  }
}
```