---
exchange: binance
source_url: https://developers.binance.com/docs/binance-spot-api-docs/web-socket-streams
api_type: REST
updated_at: 2026-06-28 18:50:13.745485
---

# Data sources

* The API system is asynchronous. Some delay in the response is normal and expected.

  * Each method has a data source indicating where the data is coming from, and thus how up-to-date it is.


Data Source| Latency| Description  
---|---|---  
Matching Engine| lowest| The Matching Engine produces the response directly  
Memory| low| Data is fetched from API server's local or external memory cache  
Database| moderate| Data is retrieved from the database  
  
  * Some methods have more than one data source (e.g., Memory => Database).

This means that the API will look for the latest data in that order: first in the cache, then in the database.

---

# 数据源

* API 系统是异步的。响应中一些延迟是正常和预期的。

  * 每种函数都会有一个数据源, 用来指示数据的来源，以及它的最新程度。


数据源| 延迟| 描述  
---|---|---  
撮合引擎| 最低| 表示撮合引擎直接产生响应  
缓存| 低| 表示数据来源于内部或者外部的缓存  
数据库| 中度| 表示数据直接来源于数据库  
  
  * 某些函数有多个数据源（例如，缓存 => 数据库）。

这代表 API 将按该顺序查找最新数据：首先是缓存，然后是数据库。