---
exchange: bitget
source_url: https://www.bitget.com/docs/uta/update-preview
api_type: Guide
updated_at: 2026-11-27 19:02:09.756525
---

# Update Preview

## rToken Limit Order Restriction Trigger Adjusted

**Effective date:** From the start of the statistical cycle on November 19, 2026 (05:00 UTC+8)

- rToken Limit Order Restriction Trigger Adjusted

Changes:
- In the trigger conditions of the rToken limit order trading rule, the threshold for the total number of terminal orders for a single UID on a single trading pair within a statistical cycle will be lowered from more than 2,000 to more than 1,000. The fill rate condition (below 10%) and all other rules remain unchanged. See the [rToken Trading Guide](/docs/uta/reality-trading-guide) for details.

## ANTHROPICUSDT Renamed to ANTUSDT

**Effective date:** November 17, 2026, 17:30 (UTC+8)

Starting from the effective date, the following USDT-M Futures trading pair under both the V2 Classic Account and the V3 Unified Account will be renamed:

| **Before** | **After** |
|:-|:-|
| `ANTHROPICUSDT` | `ANTUSDT` |

**What stays the same:**

The following remain unchanged after the rename. There is no need to cancel orders, close positions or place orders again:
- Existing positions remain valid
- Existing open orders, TP/SL orders and strategy orders remain valid
- Trades, fills, positions and history records are not affected

**What changes:**

1. After the rename, API request parameters will accept both `ANTHROPICUSDT` and `ANTUSDT`, so you can keep using the old name or switch to the new one. However, the `symbol` field in all REST responses and WebSocket pushes will be returned as `ANTUSDT`.

| **Scenario** | **Request `symbol`** | **Response `symbol`** |
|:-|:-|:-|
| Before the rename | `ANTHROPICUSDT` | `ANTHROPICUSDT` |
| After the rename, using the old name | `ANTHROPICUSDT` | `ANTUSDT` |
| After the rename, using the new name | `ANTUSDT` | `ANTUSDT` |

2. Public WebSocket connections subscribed with `ANTHROPICUSDT` will receive a push message notifying you of the rename. Please re-subscribe to this trading pair after receiving the message.

:::warning{title="Note"}
We strongly recommend switching the relevant parameters to `ANTUSDT` as soon as possible after the rename takes effect.
:::

## Candlestick and Public Trades Channels: Snapshot Push Removed

**Effective date:** demo trading on November 4, 2026; live trading expected on November 17, 2026

Interface:
- WebSocket candlestick channel (`kline`)
- WebSocket public trades channel (`publicTrade`)

Changes:
- After a successful subscription, these channels will no longer push snapshot data (`action`=`snapshot`); only real-time incremental data (`action`=`update`) will be pushed.
- To obtain historical candlestick or trade data, please use the corresponding REST API.

## books50 Depth Channel: Incremental Push

**Live date:** December 1, 2026

Interface:
- WebSocket `books50` depth channel (JSON)
- WebSocket SBE Depth50 channel (`books50`, templateId=1001)

Changes:
- The `books50` channel will change from full snapshot on every push to incremental push: the first push after subscription is a full `snapshot`, and all subsequent pushes are incremental `update`s. This applies to both the JSON text-frame channel and the SBE binary channel.
- The `pseq` push parameter will also have a value for the `books50` channel (previously only for the `books` channel), and can be used to determine whether there has been packet loss.
- On the SBE side, the schema version will be raised to `5`, and the `Depth50` message (templateId=1001) will carry two additional fields: `depthAction` (`0` = `snapshot`, `1` = `update`) to distinguish the two frame types explicitly, and `pseq` for packet-loss detection.
- Currently effective in **demo trading**.

---

# 更新预告

## rToken 限价单限制触发条件调整

**生效时间：2026 年 11 月 19 日统计周期开始（05:00 UTC+8）**<br/>

- rToken 限价单限制触发条件调整<br/>
调整内容：rToken 限价单交易规则的限制触发条件中，单个 UID、单个币对在统计周期内的终态订单总数阈值由超过 2,000 笔调整为超过 1,000 笔；成交率低于 10% 的条件及其他规则保持不变。详见 [rToken 交易指南](/zh-CN/docs/uta/reality-trading-guide)<br/>

## ANTHROPICUSDT 更名为 ANTUSDT

**生效时间：2026 年 11 月 17 日 17:30（UTC+8）**<br/>

自生效时间起，V2 经典账户及 V3 统一账户下的 USDT 合约交易对将进行更名：<br/>

| **改名前** | **改名后** |
|:-|:-|
| `ANTHROPICUSDT` | `ANTUSDT` |

**不受影响的事项：**<br/>
以下内容在改名后保持不变，您无需撤单、平仓或重新下单：<br/>
- 存量仓位继续有效<br/>
- 存量挂单、止盈止损及策略单继续有效<br/>
- 交易、成交、持仓及历史记录不受影响<br/>

**需关注的变化：**<br/>
1. 改名后，API 请求入参将同时兼容 `ANTHROPICUSDT` 和 `ANTUSDT`，您可继续使用旧名称发起请求，也可切换为新名称；但所有 REST 响应及 WebSocket 推送中的 `symbol` 将统一返回 `ANTUSDT`。<br/>

| **场景** | **请求 `symbol`** | **返回 `symbol`** |
|:-|:-|:-|
| 改名前 | `ANTHROPICUSDT` | `ANTHROPICUSDT` |
| 改名后使用旧名称 | `ANTHROPICUSDT` | `ANTUSDT` |
| 改名后使用新名称 | `ANTUSDT` | `ANTUSDT` |

2. 使用 `ANTHROPICUSDT` 建立的公共 WebSocket 连接将收到交易对更名的通知推送消息，收到该消息后请重新订阅该交易对。<br/>

:::warning{title="注意"}
强烈建议您在改名生效后尽快将相关参数更换为 `ANTUSDT`。
:::

## K线频道、平台成交频道：移除快照推送

**生效时间：模拟盘 2026 年 11 月 4 日；实盘预计 2026 年 11 月 17 日**<br/>

接口:<br/>
- WebSocket K线频道（`kline`）<br/>
- WebSocket 平台成交频道（`publicTrade`）<br/>

调整内容:<br/>
- 订阅成功后，以上频道不再推送快照数据（`action`=`snapshot`），仅推送实时增量数据（`action`=`update`）<br/>
- 如需获取历史K线或成交数据，请使用对应的 REST 接口<br/>

## books50 深度频道：改为增量推送

**上线时间：2026年12月1日**<br/>

接口:<br/>
- WebSocket `books50` 深度频道（JSON）<br/>
- WebSocket SBE Depth50 频道（`books50`，templateId=1001）<br/>

调整内容:<br/>
- `books50` 频道将由「每次推送全量快照」改为**增量推送**：订阅后首次推送全量 `snapshot`，后续推送增量 `update`。JSON 文本帧频道与 SBE 二进制频道均适用<br/>
- 推送参数 `pseq` 在 `books50` 频道同样有值（此前仅 `books` 频道有值），可用于判断是否丢包<br/>
- SBE 侧 Schema 版本将升至 `5`，`Depth50` 消息（templateId=1001）新增两个字段：`depthAction`（`0` = `snapshot`，`1` = `update`）用于显式区分两类帧，以及 `pseq` 用于丢包检测<br/>
- 目前**模拟盘已生效**<br/>