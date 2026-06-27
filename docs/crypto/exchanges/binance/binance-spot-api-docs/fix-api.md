---
exchange: binance
source_url: https://developers.binance.com/docs/binance-spot-api-docs/fix-api
api_type: REST
updated_at: 2026-05-27 18:54:15.436442
---

# Data Sources

* The API system is asynchronous, so some delay in the response is normal and expected.
  * Each endpoint has a data source indicating where the data is being retrieved, and thus which endpoints have the most up-to-date response.



These are the three sources, ordered by least to most potential for delays in data updates.

  * **Matching Engine** \- the data is from the Matching Engine
  * **Memory** \- the data is from a server's local or external memory
  * **Database** \- the data is taken directly from a database



Some endpoints can have more than 1 data source. (e.g. Memory => Database) This means that the endpoint will check the first Data Source, and if it cannot find the value it's looking for it will check the next one.

---

# 数据来源

* 因为API系统是异步的, 所以返回的数据有延时很正常, 也在预期之中。
  * 在每个接口中，都列出了其数据的来源，可以用于理解数据的时效性。



系统一共有3个数据来源，按照更新速度的先后排序。排在前面的数据最新，在后面就有可能存在延迟。

  * **撮合引擎** \- 表示数据来源于撮合引擎
  * **缓存** \- 表示数据来源于内部或者外部的缓存
  * **数据库** \- 表示数据直接来源于数据库



有些接口有不止一个数据源, 比如 `缓存 => 数据库`, 这表示接口会先从第一个数据源检查，如果没有数据，则检查下一个数据源。