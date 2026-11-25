---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/web3-task-verification/apis
api_type: Guide
updated_at: 2026-11-25 18:27:26.940668
---

# Binance Web3 API Specification

## Web3 API description

- Binance's Partners need to follow the API specification in this doc to provide Binance with a set
  of endpoints that Binance will call to check if a user has completed specific tasks (like a
  deposit, swap,etc.).

## General API Information

- All endpoints return a common JSON object with "code", "message" and "data", no matter if it's a
  success or not.
- Here "data" is either a customized JSON object or a simple type (int, string...). It may vary from
  endpoint to endpoint.
  ```json
  {
      "code": "XXXXXX",
      "message": "success",
      "data": {
         "abc": "efg",
         ...
     }
  }
  ```
- General codes in responses: | code | Description | | --- | --- | | 000000 | success | | 000001 |
  too many requests | | 000006 | invalid argument | | 000007 | other error |
- All time and timestamp related fields are in milliseconds.
- HTTP 5XX return codes are used for internal errors. The issue is on the partner's side. Binance
  will **NOT** treat this as a failure operation; the execution status is UNKNOWN.
- For GET endpoints, parameters must be sent as a query string.
- Parameters may be sent in any order.
- Each request and response should be logged in both Binance and partner's sides for further
  investigation.
- Every partner needs to define a url prefix so that Binance can invoke the partner's endpoint using
  prefix + endpoint_url. <span style="word-break:break-all;">E.g.
  https<span></span>://tasks-api.x.build/api/v1/task/completion?walletAddress=xx&task=["deposit"]</span>

* **Front all OpenAPI endpoints with a WAF**
  - Place every public endpoint behind a Web Application Firewall.

  - Enable core protections (SQLi, XSS, RCE) and basic rate/behavior policies.

* **Rate limiting & overload protection**
  - Enforce global and per-key limits (per IP / user / token), plus per-endpoint limits on critical
    paths.

  - When capacity is exceeded, return **HTTP 429 (Too Many Requests)** and include a `Retry-After`
    header.

  - Consider circuit breakers and exponential backoff hints for clients.

## API Specification​

### Task Completion

```
GET /v1/task/completion
```

**Parameters:**

| Name          | Type              | Mandatory | Description                                                                                                                                                                                                                                                                                             |
| ------------- | ----------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| walletAddress | String            | YES       | a user's unified id                                                                                                                                                                                                                                                                                     |
| task          | String json array | YES       | Task ID used to identify the task. Try to use a Task ID that is relevant and descriptive of the task, not a random or arbitrary string. For example, task=["deposit","withdraw"]. If it's not empty, just return corresponding task completion status. Otherwise, return all tasks completion statuses. |

**Response Body:**

| Name    | Type        | Mandatory |
| ------- | ----------- | --------- |
| code    | String      | YES       |
| message | String      | YES       |
| data    | JSON Object | YES       |

**Examples:**

```json
GET {prefix} + /v1/task/completion?walletAddress=0xabcdefg&task=["deposit", "withdrawal"]

Response:
{
 "code": "000000",
 "message": "success",
 "data": {
     "withdrawal": true, // complete
     "deposit": false, // incomplete
 }
}

{
 "code": "000006",
 "message": "invalid argument",
 "data": null
}
```

- **Task verification (`verify` API)**
  - Flow: After a user completes a task and taps **Verify**, Binance backend calls your `verify` API
    to confirm completion.

  - **Latency SLO**: **P99 \< 1s**, **hard timeout ≤ 3s** (set a server-side timeout of 3 seconds).

  - **Observability**: Monitor latency (P50/P95/P99), error ratio, dependency timing; alert on
    timeouts and anomalies, and investigate immediately.

  - **Correctness over speed**: Do not return success/failure optimistically if data is
    inconclusive.

  - **Response shape**:
    - If incomplete, return a clear reason to reduce support load (e.g., a missing sub-step).

Example:

```json
{
  "completed": false,
  "reason": "Subtask 'bridge_tx_confirmed' not met (0/1 confirmations)",
  "evidence": null
}
```

-

Success example:

```json
{
  "completed": true,
  "reason": null,
  "evidence": {
    "tx_hash": "0xabc...123",
    "chain_id": 56,
    "timestamp": 1732178452
  }
}
```

## Web3 API Performance

- Ensure your API can support >=**50 QPS.**
  - In special cases, Binance will review your campaign and contact you to increase the API QPS
    threshold. (E.g. Marketing plan is possible to attract extra traffic to your campaign, or
    special task design will cause high peak verification queries)
  - API performance is vital. So please conduct a performance test on the API.
  - Before developing the API, review the campaign mechanism. Avoid mechanisms requiring all users
    to verify tasks at the same time. (E.g. a task user can only verify on the last day of a
    campaign)
  - When API encounters performance issues, please return an error (error code:000002) to the
    caller.

## API Maintenance Periods:

- Maintain the API till 3 days after the campaign end time.
  - E.g.: the campaign using your API ends on 1st Jan 2025 00:00(UTC), then the earliest time you
    can sunset the API is 4th Jan 2025 00:00(UTC)
  - Before you sunset the API, please ensure no traffic hits your API. If there is still traffic to
    your API, please contact the Binance team.

## Other Good Practise for API Developing:

- Use 95% of the original criteria to verify user’s task status.
  - E.g. for a task that requires the user to stake more than 10 USDT, the API should return
    completed (True) if the user takes more than 9.5 USDT.
- Avoid API changes before sunsetting the API.
  - Please update stakeholders if the API has to be updated due to logic change or issue fix.
- Monitor the API performances especially the 1st 4 hours after the campaign launch time.

* **Observability & slow-query management**
  - Enable slow-query logs for **DB** and **Redis** (or other caches) and wire up application/APM
    monitoring (latency percentiles, error codes, dependency timings).

  - Use distributed tracing (Trace/Span IDs) end-to-end so you can pinpoint bottlenecks quickly.

  - Define alert thresholds and on-call procedures for timeouts and rising error rates.

* **SQL review & caching strategy**
  - Audit **all** SQL statements:
    - Ensure predicates use appropriate **indexes**; avoid full scans and implicit casts.

    - Review execution plans (`EXPLAIN`) and data distribution regularly.

  - Identify **hot keys** / high-QPS reads; use **Redis** (or similar) with proper TTLs and
    invalidation/backfill.

  - Protect against cache **penetration / breakdown / avalanche** (e.g., negative caching, jittered
    TTLs, bulkhead isolation).

  - Revisit schema/index health periodically; consider archival, read replicas, or sharding where
    needed.

Provide feedback on this document: <https://forms.gle/zpBnQWCqoFMmby698>

---

# Binance Web3 API Specification

## Web3 API description

- Binance's Partners need to follow the API specification in this doc to provide Binance with a set
  of endpoints that Binance will call to check if a user has completed specific tasks (like a
  deposit, swap,etc.).

## General API Information

- All endpoints return a common JSON object with "code", "message" and "data", no matter if it's a
  success or not.
- Here "data" is either a customized JSON object or a simple type (int, string...). It may vary from
  endpoint to endpoint.
  ```json
  {
      "code": "XXXXXX",
      "message": "success",
      "data": {
         "abc": "efg",
         ...
     }
  }
  ```
- General codes in responses: | code | Description | | --- | --- | | 000000 | success | | 000001 |
  too many requests | | 000006 | invalid argument | | 000007 | other error |
- All time and timestamp related fields are in milliseconds.
- HTTP 5XX return codes are used for internal errors. The issue is on the partner's side. Binance
  will **NOT** treat this as a failure operation; the execution status is UNKNOWN.
- For GET endpoints, parameters must be sent as a query string.
- Parameters may be sent in any order.
- Each request and response should be logged in both Binance and partner's sides for further
  investigation.
- Every partner needs to define a url prefix so that Binance can invoke the partner's endpoint using
  prefix + endpoint_url. <span style="word-break:break-all;">E.g.
  https<span></span>://tasks-api.x.build/api/v1/task/completion?walletAddress=xx&task=["deposit"]</span>

* **Front all OpenAPI endpoints with a WAF**
  - Place every public endpoint behind a Web Application Firewall.

  - Enable core protections (SQLi, XSS, RCE) and basic rate/behavior policies.

* **Rate limiting & overload protection**
  - Enforce global and per-key limits (per IP / user / token), plus per-endpoint limits on critical
    paths.

  - When capacity is exceeded, return **HTTP 429 (Too Many Requests)** and include a `Retry-After`
    header.

  - Consider circuit breakers and exponential backoff hints for clients.

## API Specification​

### Task Completion

```
GET /v1/task/completion
```

**Parameters:**

| Name          | Type              | Mandatory | Description                                                                                                                                                                                                                                                                                             |
| ------------- | ----------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| walletAddress | String            | YES       | a user's unified id                                                                                                                                                                                                                                                                                     |
| task          | String json array | YES       | Task ID used to identify the task. Try to use a Task ID that is relevant and descriptive of the task, not a random or arbitrary string. For example, task=["deposit","withdraw"]. If it's not empty, just return corresponding task completion status. Otherwise, return all tasks completion statuses. |

**Response Body:**

| Name    | Type        | Mandatory |
| ------- | ----------- | --------- |
| code    | String      | YES       |
| message | String      | YES       |
| data    | JSON Object | YES       |

**Examples:**

```json
GET {prefix} + /v1/task/completion?walletAddress=0xabcdefg&task=["deposit", "withdrawal"]

Response:
{
 "code": "000000",
 "message": "success",
 "data": {
     "withdrawal": true, // complete
     "deposit": false, // incomplete
 }
}

{
 "code": "000006",
 "message": "invalid argument",
 "data": null
}
```

- **Task verification (`verify` API)**
  - Flow: After a user completes a task and taps **Verify**, Binance backend calls your `verify` API
    to confirm completion.

  - **Latency SLO**: **P99 \< 1s**, **hard timeout ≤ 3s** (set a server-side timeout of 3 seconds).

  - **Observability**: Monitor latency (P50/P95/P99), error ratio, dependency timing; alert on
    timeouts and anomalies, and investigate immediately.

  - **Correctness over speed**: Do not return success/failure optimistically if data is
    inconclusive.

  - **Response shape**:
    - If incomplete, return a clear reason to reduce support load (e.g., a missing sub-step).

Example:

```json
{
  "completed": false,
  "reason": "Subtask 'bridge_tx_confirmed' not met (0/1 confirmations)",
  "evidence": null
}
```

-

Success example:

```json
{
  "completed": true,
  "reason": null,
  "evidence": {
    "tx_hash": "0xabc...123",
    "chain_id": 56,
    "timestamp": 1732178452
  }
}
```

## Web3 API Performance

- Ensure your API can support >=**50 QPS.**
  - In special cases, Binance will review your campaign and contact you to increase the API QPS
    threshold. (E.g. Marketing plan is possible to attract extra traffic to your campaign, or
    special task design will cause high peak verification queries)
  - API performance is vital. So please conduct a performance test on the API.
  - Before developing the API, review the campaign mechanism. Avoid mechanisms requiring all users
    to verify tasks at the same time. (E.g. a task user can only verify on the last day of a
    campaign)
  - When API encounters performance issues, please return an error (error code:000002) to the
    caller.

## API Maintenance Periods:

- Maintain the API till 3 days after the campaign end time.
  - E.g.: the campaign using your API ends on 1st Jan 2025 00:00(UTC), then the earliest time you
    can sunset the API is 4th Jan 2025 00:00(UTC)
  - Before you sunset the API, please ensure no traffic hits your API. If there is still traffic to
    your API, please contact the Binance team.

## Other Good Practise for API Developing:

- Use 95% of the original criteria to verify user’s task status.
  - E.g. for a task that requires the user to stake more than 10 USDT, the API should return
    completed (True) if the user takes more than 9.5 USDT.
- Avoid API changes before sunsetting the API.
  - Please update stakeholders if the API has to be updated due to logic change or issue fix.
- Monitor the API performances especially the 1st 4 hours after the campaign launch time.

* **Observability & slow-query management**
  - Enable slow-query logs for **DB** and **Redis** (or other caches) and wire up application/APM
    monitoring (latency percentiles, error codes, dependency timings).

  - Use distributed tracing (Trace/Span IDs) end-to-end so you can pinpoint bottlenecks quickly.

  - Define alert thresholds and on-call procedures for timeouts and rising error rates.

* **SQL review & caching strategy**
  - Audit **all** SQL statements:
    - Ensure predicates use appropriate **indexes**; avoid full scans and implicit casts.

    - Review execution plans (`EXPLAIN`) and data distribution regularly.

  - Identify **hot keys** / high-QPS reads; use **Redis** (or similar) with proper TTLs and
    invalidation/backfill.

  - Protect against cache **penetration / breakdown / avalanche** (e.g., negative caching, jittered
    TTLs, bulkhead isolation).

  - Revisit schema/index health periodically; consider archival, read replicas, or sharding where
    needed.

Provide feedback on this document: <https://forms.gle/zpBnQWCqoFMmby698>