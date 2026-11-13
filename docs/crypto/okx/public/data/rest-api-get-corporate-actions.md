---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#public-data-rest-api-get-corporate-actions
anchor_id: public-data-rest-api-get-corporate-actions
api_type: REST
updated_at: 2026-11-13 18:44:17.601987
---

# Get corporate actions

Retrieve corporate action events of underlying stocks, including planned execution time, processing status, and the trading status of related OKX instruments.  
  
#### Rate Limit: 1 request per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/public/corporate-actions`

> Request Example
    
    
    GET /api/v5/public/corporate-actions?ticker=AAPL&limit=20
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
ticker | String | No | Underlying stock ticker, e.g. `AAPL`. Mutually exclusive with `instId`.  
instId | String | No | Instrument ID, e.g. `AAPL-USDT-SWAP`. The system resolves the underlying stock of the instrument and returns its CA events, so `instruments` may include other related instruments. Mutually exclusive with `ticker`.  
limit | String | No | Number of results per request. Maximum is `100`. Default is `20`.  
after | String | No | Pagination of data to return records with `caEventId` earlier than the requested value, exclusive of the value.  
before | String | No | Pagination of data to return records with `caEventId` newer than the requested value, exclusive of the value.  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "caEventId": "CA20261112AAPL001",
                "eventVersion": "1",
                "ticker": "AAPL",
                "bbGlobalId": "BBG000B9XRY4",
                "exchange": "XNAS",
                "actionType": "CASH_DIVIDEND",
                "caClass": "PREDICTABLE",
                "dividendSize": "MEDIUM",
                "cashDividend": {
                    "gross": "0.25",
                    "net": "0.2125",
                    "ccy": "USD",
                    "exDate": "1763164800000",
                    "recordDate": "1763251200000",
                    "paymentDate": "1763596800000"
                },
                "ratioFrom": "",
                "ratioTo": "",
                "status": "upcoming",
                "cutoverTime": "1762992000000",
                "instruments": [
                    {
                        "instId": "AAPL-USDT-SWAP",
                        "state": "live"
                    }
                ]
            }
        ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
caEventId | String | Corporate action event ID  
eventVersion | String | Event version number, e.g. `"1"`. Incremented when event details are updated.  
ticker | String | Underlying stock ticker, e.g. `AAPL`  
bbGlobalId | String | Bloomberg Global Identifier  
exchange | String | Exchange MIC code where the stock is listed, e.g. `XNAS`  
actionType | String | Corporate action type.  
`CASH_DIVIDEND`: Cash dividend  
`STOCK_SPLIT`: Stock split  
`REVERSE_STOCK_SPLIT`: Reverse stock split  
`STOCK_DIVIDEND`: Stock dividend  
`SPINOFF`: Spinoff  
caClass | String | Corporate action classification.  
`PREDICTABLE`  
`UNPREDICTABLE`  
dividendSize | String | Dividend size classification. Only applicable when `actionType` is `CASH_DIVIDEND`.  
`PENDING`  
`SMALL`  
`MEDIUM`  
`LARGE`  
cashDividend | Object | Cash dividend details. Only present when `actionType` is `CASH_DIVIDEND`.  
> gross | String | Gross dividend amount per share  
> net | String | Net dividend amount per share  
> ccy | String | Dividend currency, e.g. `USD`  
> exDate | String | Ex-dividend date. Unix timestamp in milliseconds  
> recordDate | String | Record date. Unix timestamp in milliseconds  
> paymentDate | String | Payment date. Unix timestamp in milliseconds  
ratioFrom | String | Source ratio for stock splits. Only applicable when `actionType` involves splits. Empty string `""` otherwise.  
ratioTo | String | Target ratio for stock splits. Only applicable when `actionType` involves splits. Empty string `""` otherwise.  
status | String | Event processing status.  
`upcoming`  
`scheduled`  
`preparing`  
`pre_pause`  
`progressing`  
`completed`  
cutoverTime | String | Planned cutover time. Unix timestamp in milliseconds  
instruments | Array of objects | Affected OKX instruments and their trading states  
> instId | String | Instrument ID, e.g. `AAPL-USDT-SWAP`  
> state | String | Instrument trading state.  
`live`  
`rebase`  
`post_only`  
`suspend`

---

# 获取公司行动

查询底层股票的公司行动事件、计划执行时间、处理状态及关联产品的交易状态。  
  
#### 限速：1次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/public/corporate-actions`

> 请求示例
    
    
    GET /api/v5/public/corporate-actions?ticker=AAPL&limit=20
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
ticker | String | 否 | 底层股票代码，如 `AAPL`。与 `instId` 互斥。  
instId | String | 否 | 产品 ID，如 `AAPL-USDT-SWAP`。系统会先解析其对应的底层股票，再返回该股票的 CA 事件，因此 `instruments` 中可能包含其他关联产品。与 `ticker` 互斥。  
limit | String | 否 | 每次请求返回的结果数。最大 `100`，默认 `20`。  
after | String | 否 | 请求此 `caEventId` 之前（更旧）的数据，不包含该值。  
before | String | 否 | 请求此 `caEventId` 之后（更新）的数据，不包含该值。  
  
> 返回示例
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "caEventId": "CA20261112AAPL001",
                "eventVersion": "1",
                "ticker": "AAPL",
                "bbGlobalId": "BBG000B9XRY4",
                "exchange": "XNAS",
                "actionType": "CASH_DIVIDEND",
                "caClass": "PREDICTABLE",
                "dividendSize": "MEDIUM",
                "cashDividend": {
                    "gross": "0.25",
                    "net": "0.2125",
                    "ccy": "USD",
                    "exDate": "1763164800000",
                    "recordDate": "1763251200000",
                    "paymentDate": "1763596800000"
                },
                "ratioFrom": "",
                "ratioTo": "",
                "status": "upcoming",
                "cutoverTime": "1762992000000",
                "instruments": [
                    {
                        "instId": "AAPL-USDT-SWAP",
                        "state": "live"
                    }
                ]
            }
        ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
caEventId | String | 公司行动事件 ID  
eventVersion | String | 事件版本号，如 `"1"`。当事件详情更新时递增。  
ticker | String | 底层股票代码，如 `AAPL`  
bbGlobalId | String | Bloomberg 全球标识符  
exchange | String | 股票上市交易所的 MIC 代码，如 `XNAS`  
actionType | String | 公司行动类型。  
`CASH_DIVIDEND`：现金分红  
`STOCK_SPLIT`：股票拆分  
`REVERSE_STOCK_SPLIT`：反向股票拆分  
`STOCK_DIVIDEND`：股票分红  
`SPINOFF`：分拆上市  
caClass | String | 公司行动分类。  
`PREDICTABLE`：可预测  
`UNPREDICTABLE`：不可预测  
dividendSize | String | 分红规模分类。仅当 `actionType` 为 `CASH_DIVIDEND` 时适用。  
`PENDING`：待定  
`SMALL`：小额  
`MEDIUM`：中等  
`LARGE`：大额  
cashDividend | Object | 现金分红详情。仅当 `actionType` 为 `CASH_DIVIDEND` 时返回。  
> gross | String | 每股总分红金额  
> net | String | 每股净分红金额  
> ccy | String | 分红币种，如 `USD`  
> exDate | String | 除息日。Unix 毫秒时间戳  
> recordDate | String | 登记日。Unix 毫秒时间戳  
> paymentDate | String | 付款日。Unix 毫秒时间戳  
ratioFrom | String | 股票拆分源比例。仅当 `actionType` 涉及拆分时适用。否则返回空字符串 `""`。  
ratioTo | String | 股票拆分目标比例。仅当 `actionType` 涉及拆分时适用。否则返回空字符串 `""`。  
status | String | 事件处理状态。  
`upcoming`：即将发生  
`scheduled`：已计划  
`preparing`：准备中  
`pre_pause`：暂停前  
`progressing`：进行中  
`completed`：已完成  
cutoverTime | String | 计划切换时间。Unix 毫秒时间戳  
instruments | Array of objects | 受影响的 OKX 产品及其交易状态  
> instId | String | 产品 ID，如 `AAPL-USDT-SWAP`  
> state | String | 产品交易状态。  
`live`：交易中  
`rebase`：重新定基  
`post_only`：只可挂单  
`suspend`：暂停交易