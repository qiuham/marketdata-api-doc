---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/w3w-prediction/change-log
api_type: Changelog
updated_at: 2026-11-22 18:27:24.745679
---

# Change Log

## 2026-10-08

- Documentation enhancements (no API behavior changes):
  - `POST /sapi/v1/w3w/wallet/prediction/trade/get-quote`: removed the approximate 1.5 USDT `MARKET`
    minimum and the statement that `LIMIT` orders have no minimum. The minimum order amount is set
    by the server and may change, so no fixed value is documented. It is checked on `BUY` orders by
    amount and on `SELL` orders by share quantity, for both order types. A successful quote does not
    guarantee that an order is accepted or filled. Also documented that a `priceLimit` that is not
    on the price tick is truncated down instead of being rejected.
  - `GET /sapi/v1/w3w/wallet/prediction/market/detail` and
    `GET /sapi/v1/w3w/wallet/prediction/market/list`: documented the values of `status` and
    `markets[].tradingStatus`, that `markets[].tradingStatus` and not `status` decides whether new
    orders may be attempted, the meaning of `decimalPrecision`, and the `outcomes[].winner` field
    that is returned after resolution.
  - `GET /sapi/v1/w3w/wallet/prediction/position/settled-history`: documented that there is no
    separate cancelled, invalid or refunded status and how a split payout of a resolved market is
    represented.

## 2026-09-10

- Documentation enhancements (no API behavior changes):
  - All 28 Prediction Trading endpoints (`market-data`, `account`, `positions`, `trading`,
    `redemption`, `transfers`): corrected `Request Weight(IP)` from `200` to `1` to match measured
    production behavior.
  - `POST /sapi/v1/w3w/wallet/prediction/trade/place-order-bundle`: clarified that `accountType`
    only determines the settlement/reference account, not the funding source — the actual debited
    balance is controlled by `fundingSource`. Also clarified that `orderType` only accepts
    `MARKET`/`LIMIT` and must not be combined with `timeInForce` (e.g. `LIMIT_GTC` is not a valid
    value).
  - `POST /sapi/v1/w3w/wallet/prediction/trade/place-order-bundle`: documented three additional
    cases that return the generic `-3026 Your input param is invalid.`: a well-formed
    `walletAddress` not owned by the calling UID, a malformed (non-address) `walletAddress` (an
    empty string instead returns `-1102` naming the field), and omitting `priceLimit` when
    `orderType=LIMIT`.

## 2026-08-14

- New endpoints:
  - `POST /sapi/v1/w3w/wallet/prediction/otc/blocktrade/create`: create an OTC blocktrade as the
    maker.
  - `POST /sapi/v1/w3w/wallet/prediction/otc/blocktrade/list`: list the maker's own blocktrades.
  - `POST /sapi/v1/w3w/wallet/prediction/otc/blocktrade/detail`: query a blocktrade by `orderId`.
  - `POST /sapi/v1/w3w/wallet/prediction/otc/blocktrade/events`: paginated blocktrade
    lifecycle/settlement events.
  - `POST /sapi/v1/w3w/wallet/prediction/otc/blocktrade/preview`: preview an open blocktrade by
    `secretToken`.
  - `POST /sapi/v1/w3w/wallet/prediction/otc/blocktrade/fulfil`: fulfil a maker blocktrade as the
    taker.
  - `POST /sapi/v1/w3w/wallet/prediction/otc/blocktrade/remove`: cancel open/unsettled blocktrades.
  - `POST /sapi/v1/w3w/wallet/prediction/otc/blocktrade/reserved-balances`: query reserved
    USDT/share balances.
  - `POST /sapi/v1/w3w/wallet/prediction/deposit/apply`: move funds from the bound CeDeFi MPC wallet
    to a CEX account.
  - `POST /sapi/v1/w3w/wallet/prediction/withdraw/apply`: withdraw funds from a CEX account to the
    bound CeDeFi MPC wallet.
  - All of the above are restricted to authorized market makers.

## 2026-06-16

- Documentation enhancements (no API behavior changes):
  - `POST /sapi/v1/w3w/wallet/prediction/trade/batch-cancel`: removed the unused per-item
    `cancelInfoList[i].vendor` field (server auto-fills `predict_fun`). Added Known Issues section
    covering the bracket-encoding incompatibility with mainstream HTTP libraries (Python `requests`,
    Java `URI`, Go `net/url`, Node `url`) — request returns
    `-1022 Signature for this request is not valid` because clients percent-encode `[`/`]` while the
    server signs over raw bytes; included Python / Java / Go workarounds.
  - `POST /sapi/v1/w3w/wallet/prediction/transfer/inbound`: added explicit warning that the endpoint
    requires SAS authorization (returns `-31003` if SAS is not enabled).
  - `POST /sapi/v1/w3w/wallet/prediction/trade/get-quote`: documented the MARKET order minimum
    (`amountIn` ≥ ~1.5 USDT, varies by market depth; `LIMIT` orders are not subject to this
    minimum).
  - `GET /sapi/v1/w3w/wallet/prediction/transfer/status`: corrected the response example — the
    success terminal state is `COMPLETED`, not `SUCCESS`. Added the full set of status values
    (`COMPLETED`, `FAILED`, `PROCESSING`, `PENDING`).

## 2026-05-25

- Initial release of Prediction Trading APIs.

---

# 更新日誌

## 2026-10-08

- 文檔優化（不涉及 API 行為變更）：
  - `POST /sapi/v1/w3w/wallet/prediction/trade/get-quote`：移除 `MARKET` 單「約 1.5
    USDT」的最小金額，以及「`LIMIT`
    單不受此限制」的說法。最小下單金額由服務端決定，可能調整，因此不列出固定數值；`BUY`
    單按金額校驗，`SELL`
    單按份額數量校驗，兩種訂單型別均適用。報價成功不保證訂單被接受或成交。另補充：不在價格步長上的
    `priceLimit` 會被向下截斷，而不是被拒絕。
  - `GET /sapi/v1/w3w/wallet/prediction/market/detail` 與
    `GET /sapi/v1/w3w/wallet/prediction/market/list`：補充 `status` 與 `markets[].tradingStatus`
    的取值，說明由 `markets[].tradingStatus`（而不是 `status`）決定是否可以嘗試下單，補充
    `decimalPrecision` 的含義，以及市場裁定後返回的 `outcomes[].winner` 欄位。
  - `GET /sapi/v1/w3w/wallet/prediction/position/settled-history`：補充說明沒有單獨的取消、無效或退款狀態，以及已結算市場的拆分兌付如何表示。

## 2026-09-10

- 文檔優化（不涉及 API 行為變更）：
  - 全部 28 個 Prediction
    Trading 接口（`market-data`、`account`、`positions`、`trading`、`redemption`、`transfers`）：將
    `請求權重（IP）` 從 `200` 修正為 `1`，與生產環境實測結果一致。
  - `POST /sapi/v1/w3w/wallet/prediction/trade/place-order-bundle`：澄清 `accountType`
    僅決定結算/參考賬戶，並非扣款來源——實際扣款餘額由 `fundingSource` 決定。另澄清 `orderType`
    僅接受 `MARKET`/`LIMIT`，不可與 `timeInForce` 合併傳遞（例如 `LIMIT_GTC` 為非法值）。
  - `POST /sapi/v1/w3w/wallet/prediction/trade/place-order-bundle`：補充說明另外三種會返回通用
    `-3026 Your input param is invalid.` 的情況：`walletAddress` 格式合法但不屬於調用方
    `UID`、`walletAddress` 格式非法（傳空字串則會返回會點名該欄位的 `-1102`），以及
    `orderType=LIMIT` 時漏傳 `priceLimit`。

## 2026-08-14

- 新增介面：
  - `POST /sapi/v1/w3w/wallet/prediction/otc/blocktrade/create`：maker 建立一筆 OTC 大宗交易。
  - `POST /sapi/v1/w3w/wallet/prediction/otc/blocktrade/list`：查詢 maker 自己的大宗交易列表。
  - `POST /sapi/v1/w3w/wallet/prediction/otc/blocktrade/detail`：透過 `orderId` 查詢大宗交易。
  - `POST /sapi/v1/w3w/wallet/prediction/otc/blocktrade/events`：分頁查詢大宗交易生命週期/結算事件。
  - `POST /sapi/v1/w3w/wallet/prediction/otc/blocktrade/preview`：透過 `secretToken`
    預覽未結清的大宗交易。
  - `POST /sapi/v1/w3w/wallet/prediction/otc/blocktrade/fulfil`：taker 完成一筆 maker 大宗交易。
  - `POST /sapi/v1/w3w/wallet/prediction/otc/blocktrade/remove`：撤銷未結清/未結算的大宗交易。
  - `POST /sapi/v1/w3w/wallet/prediction/otc/blocktrade/reserved-balances`：查詢 USDT/shares 預留餘額。
  - `POST /sapi/v1/w3w/wallet/prediction/deposit/apply`：將資金從綁定的 CeDeFi
    MPC 錢包移至 CEX 賬戶。
  - `POST /sapi/v1/w3w/wallet/prediction/withdraw/apply`：將資金從 CEX 賬戶提領至綁定的 CeDeFi
    MPC 錢包。
  - 以上介面均僅限已授權的做市商使用。

## 2026-06-16

- 文件增強（不涉及介面行為變更）：
  - `POST /sapi/v1/w3w/wallet/prediction/trade/batch-cancel`：刪除不再使用的
    `cancelInfoList[i].vendor` 欄位（服務端自動填
    `predict_fun`）。新增"已知問題"段，說明主流 HTTP 庫（Python `requests`、Java `URI`、Go
    `net/url`、Node `url`）會自動 percent-encode `[`/`]`，但服務端按原始位元組驗簽，導致
    `-1022 Signature for this request is not valid`；附 Python / Java / Go 的臨時繞過方案。
  - `POST /sapi/v1/w3w/wallet/prediction/transfer/inbound`：顯式說明該介面需要 SAS 授權（未開啟 SAS 時返回
    `-31003`）。
  - `POST /sapi/v1/w3w/wallet/prediction/trade/get-quote`：補充 MARKET 單的最小金額說明（`amountIn`
    ≥ 約 1.5 USDT，隨市場深度浮動；`LIMIT` 單不受此約束）。
  - `GET /sapi/v1/w3w/wallet/prediction/transfer/status`：修正返回示例的終態值為 `COMPLETED`（而非
    `SUCCESS`）。補充完整狀態列舉：`COMPLETED`、`FAILED`、`PROCESSING`、`PENDING`。

## 2026-05-25

- 預測市場交易 API 首次釋出。