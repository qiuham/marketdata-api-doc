---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#public-data-rest-api-get-historical-market-data
anchor_id: public-data-rest-api-get-historical-market-data
api_type: REST
updated_at: 2026-07-23 19:22:39.705289
---

# Get historical market data

**Data availability**  
Historical data backfill is currently in progress. Data availability may vary by module, instrument, and time period. The dataset will be continuously expanded to provide more comprehensive historical coverage.  **Legacy data format notice**  
For module 1 (trade history), some old historical files may contain column headers with both Chinese characters along with English column names. All the Chinese characters will be removed once the data backfill is done. Please account for this when parsing the data.  **Data release schedule**  
Most data for modules 1, 2, 3, 11 is typically available on T+2; order book data is typically available on T+3.   
  
Retrieve historical market data for OKX.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/public/market-data-history`

> Request Example
    
    
    GET /api/v5/public/market-data-history?module=1&instType=SWAP&instFamilyList=BTC-USDT&dateAggrType=daily&begin=1756604295000&end=1756777095000
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
module | String | Yes | Data module type  
`1`: Tick-by-tick trade history  
`2`: 1-minute candlestick  
`3`: Funding rate  
`4`: 400-level orderbook  
`5`: 5000-level orderbook (from Nov 1, 2025)  
`6`: 50-level orderbook (will gradually be deprecated, please use module = `4`,`5` instead)  
`11`: Borrowing rate  
instType | String | Yes | Instrument type  
`SPOT`  
`FUTURES`  
`SWAP`  
`OPTION`  
instIdList | String | Conditional | List of instrument IDs, e.g. `BTC-USDT`, or `ANY` for all instruments (`ANY` is only supported for module = `1`, `2`, `3`, `11` & dateAggrType = `daily`)  
Multiple instrument IDs should be separated by commas, e.g. `BTC-USDT,ETH-USDT`  
Maximum length = 10  
Only applicable when instType = `SPOT`  
instFamilyList | String | Conditional | List of instrument families, e.g. `BTC-USDT`, or `ANY` for all instruments (`ANY` is only supported for module = `1`, `2`, `3`, `11` & dateAggrType = `daily`)  
Multiple instrument families should be separated by commas, e.g. `BTC-USDT,ETH-USDT`  
Maximum length = 10 (= 1when module = `6` & instType = `OPTION`)  
Only applicable when instType ≠ `SPOT`  
dateAggrType | String | Yes | Date aggregation type  
`daily` (not supported for module = `3` & instFamilyList ≠ `ANY`)  
`monthly` (not supported for module = `6`)  
begin | String | Yes | Begin timestamp. Unix timestamp format in milliseconds (inclusive)  
Maximum range: 20 days for daily, 20 months for monthly  
end | String | Yes | End timestamp. Unix timestamp format in milliseconds (inclusive)  
When module = `6` & instType = `OPTION`, only returns data for the day specified by `end`  
  
> Response Example
    
    
    {
      "code": "0",
      "data": [{
        "dateAggrType": "daily",
        "details": [{
          "dateRangeEnd": "1756656000000",
          "dateRangeStart": "1756569600000",
          "groupDetails": [{
            "dateTs": "1756656000000",
            "filename": "BTC-USDT-SWAP-trades-2025-09-01.zip",
            "sizeMB": "10.82",
            "url": "https://static.okx.com/cdn/okex/traderecords/trades/daily/20250901/BTC-USDT-SWAP-trades-2025-09-01.zip"
          },
          {
            "dateTs": "1756569600000",
            "filename": "BTC-USDT-SWAP-trades-2025-08-31.zip",
            "sizeMB": "4.82",
            "url": "https://static.okx.com/cdn/okex/traderecords/trades/daily/20250831/BTC-USDT-SWAP-trades-2025-08-31.zip"
          }],
          "groupSizeMB": "15.64",
          "instFamily": "BTC-USDT",
          "instId": "",
          "instType": "SWAP"
        }],
        "totalSizeMB": "15.64",
        "ts": "1756882260390"
      }],
      "msg": ""
    }
    

> Response Example when no data files are available
    
    
    {
        "code": "0",
        "data": [
            {
                "dateAggrType": "monthly",
                "details": [],
                "totalSizeMB": "0",
                "ts": "1756889595507"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
ts | String | Response timestamp, Unix timestamp format in milliseconds  
totalSizeMB | String | Total size of all data files in MB  
dateAggrType | String | Date aggregation type  
`daily`  
`monthly`  
details | Array |   
> instId | String | Instrument ID  
> instFamily | String | Instrument family  
> dateRangeStart | String | Data range start date, Unix timestamp format in milliseconds (inclusive)  
> dateRangeEnd | String | Data range end date, Unix timestamp format in milliseconds (inclusive)  
> groupSizeMB | String | Data group size in MB  
> groupDetails | Array |   
>> filename | String | Data file name, e.g. `BTC-USDT-SWAP-trades-2025-05-15.zip`  
>> dataTs | String | Data date timestamp, Unix timestamp format in milliseconds  
>> sizeMB | String | File size in MB  
>> url | String | Download URL  
**Data query rules**  
• Only the date portion (yyyy-mm-dd) of timestamps is used; time components are ignored  
• Both begin and end timestamps are inclusive  
• Data is returned in reverse chronological order (closer to end first)  
• If the query exceeds record limits, data closest to the end timestamp is returned  
• **Exception:** When module = 6 & instType = OPTION, only data for the day specified by the end is returned  **Timezone specifications for timestamp parsing**  
When converting Unix timestamps to dates, the following timezone conventions are applied to all timestamp fields (begin, end, dateRangeStart, dateRangeEnd, dataTs):  
• **Orderbook data** (modules 4, 5, 6): UTC+0  
• **All other data modules** (modules 1, 2, 3, 11): UTC+8

---

# 获取历史市场数据

**数据覆盖范围**  
历史数据回填正在进行中，不同模块、产品和时间段的数据覆盖范围可能有所差异。数据集将持续扩展，以提供更全面的历史数据覆盖。  **旧数据格式注意**  
对于模块1（交易历史），一些旧的历史文件可能包含同时带有中文字符和英文列名的列标题。数据回填完成后，所有中文字符将被移除。请在解析数据时考虑到这一点。  **数据发布安排**  
模块 1、2、3、11 的数据通常在 T+2 可用；订单簿数据通常在 T+3 可用。   
  
获取OKX历史市场数据。

#### 限速：2次/5s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/public/market-data-history`

> 请求示例
    
    
    GET /api/v5/public/market-data-history?module=1&instType=SWAP&instFamilyList=BTC-USDT&dateAggrType=daily&begin=1756604295000&end=1756777095000
    

#### 请求参数

参数名称 | 类型 | 是否必须 | 描述  
---|---|---|---  
module | String | 是 | 数据模块类型  
`1`: 逐笔成交历史  
`2`: 1分钟K线  
`3`: 资金费率  
`4`: 400档位深度   
`5`: 5000档位深度（自2025年11月1日起支持）  
`6`: 50档位深度 (将逐步弃用，请使用 module = `4`,`5` 代替)  
`11`: 借币利率  
instType | String | 是 | 产品类型  
`SPOT`  
`FUTURES`  
`SWAP`  
`OPTION`  
instIdList | String | 可选 | 产品ID列表，例如 `BTC-USDT` 或 `ANY` 表示所有产品（`ANY` 仅支持 module = `1`, `2`, `3`, `11` & dateAggrType = `daily`）  
多个产品请用英文逗号分隔，如 `BTC-USDT,ETH-USDT`  
最大长度 = 10   
仅适用于instType = `SPOT`  
instFamilyList | String | 可选 | 交易品种列表，例如 `BTC-USDT` 或 `ANY` 表示所有产品（`ANY` 仅支持 module = `1`, `2`, `3`, `11` & dateAggrType = `daily`）  
多个品种请用英文逗号分隔，如 `BTC-USDT,ETH-USDT`  
最大长度 = 10 (当module = `6` & instType = `OPTION`时为1)   
仅适用于instType ≠ `SPOT`  
dateAggrType | String | 是 | 日期聚合类型  
`daily` (不支持 module = `3` & instFamilyList ≠ `ANY`)  
`monthly` （不支持module = `6`）  
begin | String | 是 | 开始时间戳，Unix时间戳格式为毫秒数（包含该时间）  
日度最大范围：20天，月度最大范围：20个月  
end | String | 是 | 结束时间戳，Unix时间戳格式为毫秒数（包含该时间）  
当module = `6` & instType = `OPTION`时，仅返回`end`指定日期的数据  
  
> 返回示例
    
    
    {
      "code": "0",
      "data": [{
        "dateAggrType": "daily",
        "details": [{
          "dateRangeEnd": "1756656000000",
          "dateRangeStart": "1756569600000",
          "groupDetails": [{
            "dateTs": "1756656000000",
            "filename": "BTC-USDT-SWAP-trades-2025-09-01.zip",
            "sizeMB": "10.82",
            "url": "https://static.okx.com/cdn/okex/traderecords/trades/daily/20250901/BTC-USDT-SWAP-trades-2025-09-01.zip"
          },
          {
            "dateTs": "1756569600000",
            "filename": "BTC-USDT-SWAP-trades-2025-08-31.zip",
            "sizeMB": "4.82",
            "url": "https://static.okx.com/cdn/okex/traderecords/trades/daily/20250831/BTC-USDT-SWAP-trades-2025-08-31.zip"
          }],
          "groupSizeMB": "15.64",
          "instFamily": "BTC-USDT",
          "instId": "",
          "instType": "SWAP"
        }],
        "totalSizeMB": "15.64",
        "ts": "1756882260390"
      }],
      "msg": ""
    }
    

> 返回示例，当没有数据文件时
    
    
    {
        "code": "0",
        "data": [
            {
                "dateAggrType": "monthly",
                "details": [],
                "totalSizeMB": "0",
                "ts": "1756889595507"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名称** | **类型** | **描述**  
---|---|---  
ts | String | 响应时间戳，Unix时间戳格式为毫秒数  
totalSizeMB | String | 所有数据文件总大小，单位MB  
dateAggrType | String | 日期聚合类型  
`daily`  
`monthly`  
details | Array |   
> instId | String | 产品ID  
> instFamily | String | 交易品种  
> dateRangeStart | String | 数据范围开始日期，Unix时间戳格式为毫秒数（包含该时间）  
> dateRangeEnd | String | 数据范围结束日期，Unix时间戳格式为毫秒数（包含该时间）  
> groupSizeMB | String | 数据组大小，单位MB  
> groupDetails | Array |   
>> filename | String | 数据文件名，例如 `BTC-USDT-SWAP-trades-2025-05-15.zip`  
>> dataTs | String | 数据日期时间戳，Unix时间戳格式为毫秒数  
>> sizeMB | String | 文件大小，单位MB  
>> url | String | 下载链接  
**数据查询规则**  
• 仅使用时间戳的日期部分（yyyy-mm-dd），忽略时间部分  
• begin和end时间戳均为包含该时间  
• 数据按倒序时间顺序返回（越接近end的数据越靠前）  
• 如果查询超出记录限制，返回最接近end时间戳的数据  
• **例外：** 当 module = 6 且 instType = OPTION 时，仅返回 end 指定日期的数据  **时间戳解析的时区规范**  
将Unix时间戳转换为日期时，以下时区约定适用于所有时间戳字段（begin, end, dateRangeStart, dateRangeEnd, dataTs）：  
• **深度数据** （模块4、5、6）：UTC+0  
• **其他数据模块** （模块1、2、3、11）：UTC+8