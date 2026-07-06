---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#spread-trading-comprehensive-api-workflow-trade-state
anchor_id: spread-trading-comprehensive-api-workflow-trade-state
api_type: API
updated_at: 2026-07-06 19:53:49.119100
---

# Trade State

Track the state of a trade by subscribing to the `sprd-trades`WebSocket channel.

  1. After an executed trade undergoes clearing and settlement on OKX, it reaches finality.
  2. For successfully cleared trades, a WebSocket message is sent with the `state`denoted as `filled`.
  3. In the case of an unsuccessful trade clearing, a trade update message is sent with the `state` reflected as `rejected`.
  4. If the trade state is `rejected`, the trade update message will also include the error `code` and a corresponding error message (`msg`) that explains the reason for the rejection.

---

# 用户的交易状态

通过订阅 `sprd-trades`WebSocket 频道，用户可以跟踪他们的交易状态。 1\. 一笔已执行的交易在OKX上进行清算结算后，即为最终交易。 2\. 对于成功清算的交易，用户会收到一条 WebSocket 消息，其中的`state`表示`filled`。 3\. 在交易清算不成功的情况下，用户会收到一条交易更新消息，`state`反映为`rejected`。 4\. 如果交易`state`为`rejected`，交易更新消息还将包含错误代码`code`和解释拒绝原因的相应错误消息 `msg`。