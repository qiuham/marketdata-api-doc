---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mining/change-log
api_type: Changelog
updated_at: 2026-11-25 18:30:03.347645
---

# Change Log

## 2022-05-19

- Update endpoint for Mining:
  - `GET /sapi/v1/mining/pub/algoList` and `GET /sapi/v1/mining/pub/coinList`: Need no parameter.

---

## 2022-01-04

- New endpoint for Mining:
  - `GET /sapi/v1/mining/payment/uid` to get Mining account earning.

---

## 2021-01-10

- New parameter `pageSize` for Mining endpoint `GET /sapi/v1/mining/payment/list`
- New fields in response to Mining endpoint `GET /sapi/v1/mining/payment/list`:
  - "type" for income type
  - "hashTransfer" for resale Hashrate
  - "transferAmount" for transferred Income

- New Mining endpoints:
  - `GET /sapi/v1/mining/payment/other`
  - `GET /sapi/v1/mining/hash-transfer/config/details`
  - `GET /sapi/v1/mining/hash-transfer/config/details/list`
  - `GET /sapi/v1/mining/hash-transfer/profit/details`
  - `POST /sapi/v1/mining/hash-transfer/config`
  - `POST /sapi/v1/mining/hash-transfer/config/cancel`

---

## 2020-05-06

- New endpoints for Mining:
  - `GET /sapi/v1/mining/pub/algoList`
  - `GET /sapi/v1/mining/pub/coinList`
  - `GET /sapi/v1/mining/worker/detail`
  - `GET /sapi/v1/mining/worker/list`
  - `GET /sapi/v1/mining/payment/list`
  - `GET /sapi/v1/mining/statistics/user/status`
  - `GET /sapi/v1/mining/statistics/user/list`

---

# 更新日志

## 2022-05-19

- 更新矿池接口參數:
  - `GET /sapi/v1/mining/pub/algoList` 及 `GET /sapi/v1/mining/pub/coinList`：不需要参数

---

## 2022-01-04

- 新增矿池接口:
  - `GET /sapi/v1/mining/payment/uid` 以获取矿池账户收益列表

---

## 2021-01-10

- 矿池接口 `GET /sapi/v1/mining/payment/list` 新增可选参数 `pageSize`
- 矿池接口 `GET /sapi/v1/mining/payment/list` 新增返回字段：
  - "type" 表示收益类型
  - "hashTransfer" 表示已转让算力
  - "transferAmount" 表示已转让收益

- 新增矿池接口:
  - `GET /sapi/v1/mining/payment/other`
  - `GET /sapi/v1/mining/hash-transfer/config/details`
  - `GET /sapi/v1/mining/hash-transfer/config/details/list`
  - `GET /sapi/v1/mining/hash-transfer/profit/details`
  - `POST /sapi/v1/mining/hash-transfer/config`
  - `POST /sapi/v1/mining/hash-transfer/config/cancel`

---

## 2020-05-06

- 新增矿池接口:
  - `GET /sapi/v1/mining/pub/algoList`
  - `GET /sapi/v1/mining/pub/coinList`
  - `GET /sapi/v1/mining/worker/detail`
  - `GET /sapi/v1/mining/worker/list`
  - `GET /sapi/v1/mining/payment/list`
  - `GET /sapi/v1/mining/statistics/user/status`
  - `GET /sapi/v1/mining/statistics/user/list`