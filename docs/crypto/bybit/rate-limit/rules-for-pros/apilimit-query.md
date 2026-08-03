---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/rate-limit/rules-for-pros/apilimit-query
api_type: REST
updated_at: 2026-08-03 19:08:34.964528
---

# Introduction

## API Rate Limit Rules for PROs

Upcoming changes for pro account

Starting **August 13, 2025** , Bybit will roll out a new institutional API rate limit framework designed to enhance performance for high-frequency trading clients. The new system introduces a centralized institution-level rate cap with flexible per-UID configurations, enabling greater efficiency and scalability. Please refer to the [announcement](https://announcements.bybit.com/en/article/update-bybit-enhances-api-rate-limits-for-institutional-traders-bltbbbf60de757d074e/) for more information.

### UID-level rate limit

Maximum limit for a single UID.

| Unified Account  
---|---  
Level\Product| **Futures**| **Option**| **Spot**  
Default| 10/s| 10/s| 20/s  
PRO1| 200/s| 200/s| 200/s  
PRO2| 400/s| 400/s| 400/s  
PRO3| 600/s| 600/s| 600/s  
PRO4| 800/s| 800/s| 800/s  
PRO5| 1000/s| 1000/s| 1000/s  
PRO6| 1200/s| 1200/s| 1200/s  
MM1| 600/s| 600/s| 600/s  
MM2| 800/s| 800/s| 800/s  
MM3| 1000/s| 1000/s| 1000/s  
  
### Institutional-level rate limit

Aggregate limit across all main and sub UIDs.

| Unified Account  
---|---  
Level\Product| **Futures**| **Option**| **Spot**  
PRO1| 10000/s| 10000/s| 10000/s  
PRO2| 20000/s| 20000/s| 20000/s  
PRO3| 30000/s| 30000/s| 30000/s  
PRO4| 40000/s| 40000/s| 40000/s  
PRO5| 50000/s| 50000/s| 50000/s  
PRO6| 60000/s| 60000/s| 60000/s  
MM1| 30000/s| 30000/s| 30000/s  
MM2| 40000/s| 40000/s| 40000/s  
MM3| 50000/s| 50000/s| 50000/s  
  
instructions for API rate limit

  * All of the existing subaccounts still have their original API rate limits.
  * The default API rate limit for a new subaccount is not counted in the institutional-level API rate limit. 
  * The default API rate limit for a new sub is: 10/s for futures, 10/s for options, 20/s for spot.
  * If the aggregate institutional-level API rate limit is exceeded, you must reduce one or several account's API rate limit(s) first. After the API rate limit is less than the aggregate institutional API rate limit, you can increase the API rate limit of an account.

---

# 限頻介紹

## PROs接口限頻規則

即將到來的變更

自**2025年8月13日** 起，Bybit 將推出全新機構 API 限頻框架體系，旨在為高頻交易客戶提升性能體驗。新系統將引入中心化機構級速率上限，并可按 UID 靈活配置，有效提升效率與可擴展性。請參閱[公告](https://announcements.bybit.com/zh-TW/article/update-bybit-enhances-api-rate-limits-for-institutional-traders-bltbbbf60de757d074e/)

### UID 層級:

| 統一帳戶  
---|---  
Level\Product| **Futures**| **Option**| **Spot**  
Default| 10/s| 10/s| 20/s  
PRO1| 200/s| 200/s| 200/s  
PRO2| 400/s| 400/s| 400/s  
PRO3| 600/s| 600/s| 600/s  
PRO4| 800/s| 800/s| 800/s  
PRO5| 1000/s| 1000/s| 1000/s  
PRO6| 1200/s| 1200/s| 1200/s  
MM1| 600/s| 600/s| 600/s  
MM2| 800/s| 800/s| 800/s  
MM3| 1000/s| 1000/s| 1000/s  
  
### 主帳戶和子帳戶層級 (（機構 API 限頻配額）):

| 統一帳戶  
---|---  
Level\Product| **Futures**| **Option**| **Spot**  
PRO1| 10000/s| 10000/s| 10000/s  
PRO2| 20000/s| 20000/s| 20000/s  
PRO3| 30000/s| 30000/s| 30000/s  
PRO4| 40000/s| 40000/s| 40000/s  
PRO5| 50000/s| 50000/s| 50000/s  
PRO6| 60000/s| 60000/s| 60000/s  
MM1| 30000/s| 30000/s| 30000/s  
MM2| 40000/s| 40000/s| 40000/s  
MM3| 50000/s| 50000/s| 50000/s  
  
API 限頻說明

  * 所有現有子帳戶仍享有原有的 API 限頻。
  * 新子帳戶的預設 API 限頻不計入機構 API 限頻總配額。
  * 新子帳戶的預設 API 限頻為：期貨 10 次/秒，期權 10 次/秒，現貨 20 次/秒。
  * 如果超出機構 API 限頻總配額，您只能先降低帳戶的 API 限頻。當 API 限頻總配額低於機構 API 限頻總配額後，您才能提高帳戶的 API 限頻。