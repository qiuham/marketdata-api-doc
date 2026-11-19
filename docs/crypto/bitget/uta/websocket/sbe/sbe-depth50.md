---
exchange: bitget
source_url: https://www.bitget.com/docs/uta/websocket/sbe/sbe-depth50
api_type: SBE
updated_at: 2026-11-19 19:07:37.862255
---

# SBE Level 50 Integration Guide

## Overview

| Field            | Description                                                                                                                                                                                                    |
|:-----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Topic            | `books50`                                                                                                                                                                                                      |
| TemplateId       | `1001`                                                                                                                                                                                                         |
| Schema Version   | `5`                                                                                                                                                                                                            |
| Format           | SBE binary frame (opcode = 2), little-endian                                                                                                                                                                   |
| Depth            | Provides 50-level bid/ask order book data. The first frame after subscription is a full snapshot (`depthAction = 0`); subsequent frames are incremental updates (`depthAction = 1`) to be merged into the local order book                                                                                                                     |
| Units            | Timestamps in microseconds (µs), but only accurate to milliseconds. Append `000` to a millisecond timestamp to get the microsecond format. E.g., millisecond timestamp 1726233600001 corresponds to µs timestamp 1726233600001000 |
| Update Frequency | 20ms                                                                                                                                                                                                           |

---

## Connection

- **WebSocket URL**: `wss://ws.bitget.com/v3/ws/public/sbe`
- **Heartbeat**: Send text frame `"ping"` every 30 seconds, server responds with `"pong"`
- **Message Protocol**: JSON text frames during subscription phase; SBE binary frames during market data push phase,
  distinguished by WebSocket opCode (opCode=1 for text, opCode=2 for binary)
- The `seq` field is a monotonically increasing sequence number used to detect out-of-order packets
- The `pseq` field carries the `seq` of the previous frame, used together with `seq` to detect packet loss. It is `0`
  for snapshot frames

---

## Subscription Flow 

### 1. Send Subscription Request

```json
{
  "op": "subscribe",
  "args": [
    {
      "instType": "usdt-futures",
      "topic": "books50",
      "symbol": "BTCUSDT"
    }
  ]
}
```

**Parameter Description:**

| Parameter | Type   | Description                                                                         |
|:----------|:-------|:------------------------------------------------------------------------------------|
| instType  | string | Product type: `spot` <br/> `usdt-futures`<br/> `usdc-futures`  <br/> `coin-futures` |
| topic     | string | Fixed value: `books50`                                                              |
| symbol    | string | Symbol name, e.g. `BTCUSDT`, `ETHUSDT`                                              |

### 2. Subscription Confirmation

```json
{
  "event": "subscribe",
  "arg": {
    "instType": "usdt-futures",
    "topic": "books50",
    "symbol": "BTCUSDT"
  }
}
```

### 3. Receiving Data

After subscription confirmation, an SBE binary frame is pushed every 20ms. The first frame after subscription is a full
snapshot (`depthAction = 0`); all subsequent frames are incremental updates (`depthAction = 1`). The `depthAction` field
distinguishes them explicitly — merge each `update` frame into the local order book built from the preceding `snapshot`.

### 4. Unsubscribe

```json
{
  "op": "unsubscribe",
  "args": [
    {
      "instType": "usdt-futures",
      "topic": "books50",
      "symbol": "BTCUSDT"
    }
  ]
}
```

---

## SBE Message Structure

### Price/Size Calculation Formula

```
actual_value = mantissa × 10^exponent
```

**Example**: mantissa = 123456, exponent = -4, represents 12.3456 (actual_value = mantissa × 10 ^ exponent)

### Common Message Header (8 bytes)

All SBE messages must include a fixed 8-byte header for parsing and identifying subsequent data.

| Field       | Type   | Length (Byte) | Description                                     |
|:------------|:-------|:--------------|:------------------------------------------------|
| blockLength | uint16 | 2             | Root block length                               |
| templateId  | uint16 | 2             | Channel unique identifier, fixed value = `1001` |
| schemaId    | uint16 | 2             | Schema ID                                       |
| version     | uint16 | 2             | Schema version                                  |

### Message Field Definitions

> Note: priceExponent and sizeExponent are fixed values in the XML Schema. Prices and sizes are represented using
> mantissa and exponent.

| #   | Field         | Type                | Description                                                                                                                                                                                                              |
|:----|:--------------|:--------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| -   | messageHeader | Composite           | Fixed header, contains blockLength, templateId, schemaId, version                                                                                                                                                        |
| 1   | ts            | uint64              | Matching engine timestamp<br/> µs timestamp, but only accurate to milliseconds. Append `000` to a millisecond timestamp to get the microsecond format. E.g., millisecond timestamp 1726233600001 → µs 1726233600001000   |
| 2   | seq           | uint64              | Message sequence number, used to detect packet loss or out-of-order delivery                                                                                                                                             |
| 3   | priceExponent | int8                | Price exponent                                                                                                                                                                                                           |
| 4   | sizeExponent  | int8                | Size exponent                                                                                                                                                                                                            |
| 5   | sts           | uint64              | Stream service push timestamp in microseconds                                                                                                                                                                            |
| 6   | category      | uint8               | Product line: `spot` / `usdt-futures` / `coin-futures` / `usdc-futures`
| 7   | pseq          | uint64              | The `seq` of the previous frame, used to detect packet loss or out-of-order delivery of incremental updates. It is `0` for snapshot frames
| 8   | depthAction   | uint8               | Push action: `0` = `Snapshot` (full snapshot), `1` = `Update` (incremental update, only changed levels are included)                                                                                                                                                  |
| 100 | padding       | uint8               | Padding bytes                                                                                                                                                                                                            |
| 200 | asks          | groupSize16Encoding | Fixed 50-entry ask array                                                                                                                                                                                                 |
| 201 | bids          | groupSize16Encoding | Fixed 50-entry bid array                                                                                                                                                                                                 |
| 300 | symbol        | varString[8]        | Symbol name, UTF-8 format                                                                                                                                                                                           |

#### Asks Group

| # | Field | Type  | Description                                            |
|:--|:------|:------|:-------------------------------------------------------|
| 1 | price | int64 | Ask price<br/> Actual price = price × 10^priceExponent |
| 2 | size  | int64 | Ask size<br/> Actual size = size × 10^sizeExponent     |

#### Bids Group

| # | Field | Type  | Description                                            |
|:--|:------|:------|:-------------------------------------------------------|
| 1 | price | int64 | Bid price<br/> Actual price = price × 10^priceExponent |
| 2 | size  | int64 | Bid size<br/> Actual size = size × 10^sizeExponent     |

#### Depth Action Values

The `depthAction` field tells you how to interpret the `asks` / `bids` groups of the current frame.

| Value | Name     | Description                                                                                                                                               |
|:------|:---------|:----------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0     | Snapshot | Full snapshot. The `asks` / `bids` groups contain the complete level set, and `pseq` is `0`                                                                |
| 1     | Update   | Incremental update. Only the levels that changed since the previous frame are included; a level pushed with `size = 0` means that price level was removed |

> For `depthAction = 1` frames, apply the received levels onto the local order book: overwrite the price level with the
> new `size`, or delete it when `size = 0`.

### Binary Layout Overview

```javascript
┌─────────────┬──────────────┬────────────────────────┬────────────────────────┬──────────┐
│ Header (8B) │ Root (40B)   │ Asks: GrpHdr(4B)+N×16B │ Bids: GrpHdr(4B)+N×16B │ Symbol   │
└─────────────┴──────────────┴────────────────────────┴────────────────────────┴──────────┘
```

---

## Decoding Example

### Raw Binary (hex)

The frame below is an incremental update (`depthAction = 1`) carrying the changed ask and bid levels only. A `Snapshot`
frame (`depthAction = 0`) has the same layout, except that `pseq` is `0` and the `asks` / `bids` groups hold the complete
level set.

```javascript
28 00 E9 03 01 00 05 00  <- header: blockLength=40, templateId=1001, schemaId=1, version=5
00 40 1E 18 24 0A 06 00  <- ts (uint64 LE) = 1700000000000000
2A 00 00 00 00 00 00 00  <- seq (uint64 LE) = 42
FE                        <- priceExponent (int8) = -2
FC                        <- sizeExponent (int8) = -4
E8 43 1E 18 24 0A 06 00  <- sts (uint64 LE) = 1700000000001000
01                        <- category (uint8) = 1 (usdt-futures)
29 00 00 00 00 00 00 00  <- pseq (uint64 LE) = 41
01                        <- depthAction (uint8) = 1 (Update)
00 00 00 00              <- padding4
10 00 02 00              <- asks group: entryBlockLength=16, numInGroup=2
52 33 64 00 00 00 00 00  <- asks[0].price = 6566738
10 27 00 00 00 00 00 00  <- asks[0].size  = 10000
B6 33 64 00 00 00 00 00  <- asks[1].price = 6566838
20 4E 00 00 00 00 00 00  <- asks[1].size  = 20000
10 00 02 00              <- bids group: entryBlockLength=16, numInGroup=2
26 32 64 00 00 00 00 00  <- bids[0].price = 6566438
30 75 00 00 00 00 00 00  <- bids[0].size  = 30000
C2 31 64 00 00 00 00 00  <- bids[1].price = 6566338
40 9C 00 00 00 00 00 00  <- bids[1].size  = 40000
07 42 54 43 55 53 44 54  <- symbol: length=7, "BTCUSDT"
```

### Decoded JSON

```javascript
{
  "header": {
    "block_length": 40,
    "template_id": 1001,
    "schema_id": 1,
    "version": 5
  },
  "ts": 1700000000000000,
  "seq": 42,
  "price_exponent": -2,
  "size_exponent": -4,
  "sts": 1700000000001000,
  "category": 1,
  "pseq": 41,
  "depth_action": 1,
  "asks": [
    {
      "price": "65667.38",
      "size": "1.0000"
    },
    {
      "price": "65668.38",
      "size": "2.0000"
    }
  ],
  "bids": [
    {
      "price": "65664.38",
      "size": "3.0000"
    },
    {
      "price": "65663.38",
      "size": "4.0000"
    }
  ],
  "symbol": "BTCUSDT"
}
```

---

## Python Integration Example

```javascript
"""Bitget books50 SBE WebSocket subscription example"""
import asyncio
import json
import struct
from decimal import Decimal
import websockets

WS_URL    = "wss://ws.bitget.com/v3/ws/public/sbe"
INST_TYPE = "usdt-futures"
SYMBOL    = "BTCUSDT"
TOPIC     = "books50"


DEPTH_ACTION = {0: "Snapshot", 1: "Update"}


def decode_depth50(data: bytes) -> dict:
    """Decode Depth50 (templateId=1001) SBE frame"""
    block_length, template_id, schema_id, version = struct.unpack_from('<HHHH', data, 0)
    assert template_id == 1001, f"unexpected templateId: {template_id}"

    offset     = 8
    base       = offset
    ts,        = struct.unpack_from('<Q', data, offset); offset += 8
    seq,       = struct.unpack_from('<Q', data, offset); offset += 8
    price_exp, = struct.unpack_from('<b', data, offset); offset += 1
    size_exp,  = struct.unpack_from('<b', data, offset); offset += 1
    sts,       = struct.unpack_from('<Q', data, offset); offset += 8
    category,  = struct.unpack_from('<B', data, offset); offset += 1

    # sinceVersion=5: pseq + depthAction
    pseq = depth_action = None
    if version >= 5:
        pseq,         = struct.unpack_from('<Q', data, offset); offset += 8
        depth_action, = struct.unpack_from('<B', data, offset); offset += 1

    # Skip padding, based on blockLength
    offset = base + block_length

    def decode_group(off):
        entry_bl, num = struct.unpack_from('<HH', data, off); off += 4
        levels = []
        for _ in range(num):
            start = off
            p, = struct.unpack_from('<q', data, off); off += 8
            s, = struct.unpack_from('<q', data, off); off += 8
            off = start + entry_bl
            levels.append({
                "price": str(Decimal(p) * Decimal(10) ** price_exp),
                "size":  str(Decimal(s) * Decimal(10) ** size_exp),
            })
        return levels, off

    asks, offset = decode_group(offset)
    bids, offset = decode_group(offset)

    sym_len, = struct.unpack_from('<B', data, offset); offset += 1
    symbol = data[offset:offset + sym_len].decode('utf-8')

    return {
        "ts": ts, "seq": seq, "pseq": pseq,
        "price_exponent": price_exp, "size_exponent": size_exp,
        "sts": sts, "category": category,
        "depth_action": depth_action,
        "asks": asks, "bids": bids, "symbol": symbol,
    }


async def main():
    async with websockets.connect(WS_URL) as ws:
        # Subscribe
        await ws.send(json.dumps({
            "op": "subscribe",
            "args": [{"instType": INST_TYPE, "topic": TOPIC, "symbol": SYMBOL}]
        }))
        print(f"[SUB] {INST_TYPE} {TOPIC} {SYMBOL}")

        # Heartbeat
        async def ping_loop():
            while True:
                await asyncio.sleep(20)
                await ws.send("ping")
                print("[PING] sent")

        asyncio.create_task(ping_loop())

        async for message in ws:
            if isinstance(message, bytes):
                try:
                    msg = decode_depth50(message)
                    ts_ms = msg['ts'] // 1000
                    action = DEPTH_ACTION.get(msg['depth_action'], '?')
                    print(f"\n[Depth50] {msg['symbol']}  ts={ts_ms}ms  seq={msg['seq']}  pseq={msg['pseq']}  sts={msg['sts']}  category={msg['category']}")
                    print(f"  price_exp={msg['price_exponent']}  size_exp={msg['size_exponent']}  action={action}")
                    print(f"  asks ({len(msg['asks'])} levels):")
                    for i, lvl in enumerate(msg['asks'][:5]):
                        print(f"    [{i}] price={lvl['price']}  size={lvl['size']}")
                    print(f"  bids ({len(msg['bids'])} levels):")
                    for i, lvl in enumerate(msg['bids'][:5]):
                        print(f"    [{i}] price={lvl['price']}  size={lvl['size']}")
                except Exception as e:
                    print(f"[ERROR] {e}  raw={message.hex()}")
            else:
                if message == "pong":
                    print("[PONG] received")
                else:
                    print(f"[TEXT] {message}")


if __name__ == "__main__":
    asyncio.run(main())

---

# SBE Level 50 接入指南

## 总览

| 字段         | 说明                                                                                                            |
|:-----------|:--------------------------------------------------------------------------------------------------------------|
| Topic      | `books50`                                                                                                     |
| TemplateId | `1001`                                                                                                        |
| Schema 版本  | `5`                                                                                                           |
| Format     | SBE 二进制 frame (opcode = 2), little-endian                                                                     |
| Depth      | 提供 50 档买卖盘深度数据。订阅后首帧为全量快照（`depthAction = 0`），后续帧为增量更新（`depthAction = 1`），需合并到本地订单簿                                                       |
| Units      | 时间戳为 microseconds (µs) ，但是仅精确到毫秒。毫秒时间加上 000 得到微秒格式时间。比如：毫秒时间 1726233600001 对应的微秒格式时间 (µs) 为 1726233600001000  |
| 更新频率       | 20ms                                                                                                          |

---

## 连接

- **WebSocket URL**: `wss://ws.bitget.com/v3/ws/public/sbe`
- **心跳**: 每 30 秒发送文本帧 `"ping"`, 服务端返回 `"pong"`
- **报文机制**: 订阅阶段使用 JSON 文本帧；行情推送阶段使用 SBE 二进制帧，通过 WebSocket opCode 区分（opCode=1 文本,
  opCode=2 二进制）
- 字段 `seq` 为单调递增的序列号，用于检测乱序
- 字段 `pseq` 为前一帧的 `seq`，与 `seq` 配合用于检测丢包；快照帧的 `pseq` 为 `0`

---

## 订阅流程 

### 1. 发送订阅请求

```json
{
  "op": "subscribe",
  "args": [
    {
      "instType": "usdt-futures",
      "topic": "books50",
      "symbol": "BTCUSDT"
    }
  ]
}
```

**参数说明:**

| 参数       | 类型     | 说明                                                                           |
|:---------|:-------|:-----------------------------------------------------------------------------|
| instType | string | 产品类型:  `spot` <br/> `usdt-futures`<br/> `usdc-futures`  <br/> `coin-futures` |
| topic    | string | 固定值: `books50`                                                               |
| symbol   | string | 交易对, 如 `BTCUSDT`, `ETHUSDT`                                                  |

### 2. 订阅确认

```json
{
  "event": "subscribe",
  "arg": {
    "instType": "usdt-futures",
    "topic": "books50",
    "symbol": "BTCUSDT"
  }
}
```

### 3. 接收数据

订阅确认后, 每 20ms 推送一次 SBE 二进制帧。订阅后首帧为全量快照（`depthAction = 0`），后续帧均为增量更新（`depthAction = 1`）。报文中的 `depthAction` 字段可明确区分两者——将每个 `update` 帧合并到由前一 `snapshot` 帧构建的本地订单簿之上。

### 4. 取消订阅

```json
{
  "op": "unsubscribe",
  "args": [
    {
      "instType": "usdt-futures",
      "topic": "books50",
      "symbol": "BTCUSDT"
    }
  ]
}
```

---

## SBE 消息结构

### 价格/数量计算公式

```
实际值 = mantissa × 10^exponent
```

**示例**: 尾数为 123456，指数为 -4，表示 12.3456（实际值 = 尾数 × 10 ^ 指数）

### 公共消息头 (8 bytes)

所有 SBE 消息必须包含固定 8 字节的头部，以便解析识别后续数据。

| 字段名         | 类型 (Type) | 长度 (Byte) | 说明                  |
|:------------|:----------|:----------|:--------------------|
| blockLength | uint16    | 2         | Root 块长度            |
| templateId  | uint16    | 2         | 频道唯一标识，固定值 = `1001` |
| schemaId    | uint16    | 2         | Schema ID           |
| version     | uint16    | 2         | Schema 版本           |

### 消息字段定义

> p.s priceExponent 和 sizeExponent 在 XML Schema 中为固定值。价格和数量将会使用尾数和指数来表示。

| 序号  | 字段名 (Field)   | 类型 (Type)           | 说明                                                                                                          |
|:----|:--------------|:--------------------|:------------------------------------------------------------------------------------------------------------|
| -   | messageHeader | Composite           | 固定头部，包含 blockLength, templateId, schemaId, version                                                          |
| 1   | ts            | uint64              | 撮合引擎时间戳<br/> µs 微秒时间戳，但是仅精确到毫秒。毫秒时间加上 000 得到微秒格式时间。比如：毫秒时间 1726233600001 对应的微秒格式时间 (µs) 为 1726233600001000  |
| 2   | seq           | uint64              | 消息序列号，用于检测丢包或乱序                                                                                             |
| 3   | priceExponent | int8                | 价格指数                                                                                                        |
| 4   | sizeExponent  | int8                | 数量指数                                                                                                        |
| 5   | sts           | uint64              | 流服务推送时间戳，微秒（µs）                                                                                           |
| 6   | category      | uint8               | 业务线：`spot` 现货 / `usdt-futures` U本位合约 / `coin-futures` 币本位合约 / `usdc-futures` USDC合约                       |
| 7   | pseq          | uint64              | 前一帧的 `seq`，用于检测增量推送的丢包或乱序；快照帧的 `pseq` 为 `0`                                                                |
| 8   | depthAction   | uint8               | 推送动作：`0` = `Snapshot`（全量快照），`1` = `Update`（增量更新，仅含发生变化的档位）                                              |
| 100 | padding       | uint8               | 填充字节                                                                                                        |
| 200 | asks          | groupSize16Encoding | 固定 50 组卖单数组                                                                                                 |
| 201 | bids          | groupSize16Encoding | 固定 50 组买单数组                                                                                                 |
| 300 | symbol        | varString[8]        | 交易对名称，UTF-8 格式                                                                                              |

#### Asks Group

| 序号 | 字段名 (Field) | 类型 (Type) | 说明                                               |
|:---|:------------|:----------|:-------------------------------------------------|
| 1  | price       | int64     | 卖一价<br/> 实际价格 = 有效价格 price × 10^指数 priceExponent |
| 2  | size        | int64     | 卖一量<br/> 实际数量 = 有效数量 size × 10^指数 sizeExponent   |

#### Bids Group

| 序号 | 字段名 (Field) | 类型 (Type) | 说明                                               |
|:---|:------------|:----------|:-------------------------------------------------|
| 1  | price       | int64     | 买一价<br/> 实际价格 = 有效价格 price × 10^指数 priceExponent |
| 2  | size        | int64     | 买一量<br/> 实际数量 = 有效数量 size × 10^指数 sizeExponent   |

#### depthAction 取值

`depthAction` 字段决定如何解读当前帧的 `asks` / `bids` 分组。

| 取值 | 名称       | 说明                                                                                     |
|:---|:---------|:---------------------------------------------------------------------------------------|
| 0  | Snapshot | 全量快照。`asks` / `bids` 分组为完整档位，且 `pseq` 为 `0`                                               |
| 1  | Update   | 增量更新。仅包含相对上一帧发生变化的档位；若某档位的 `size = 0`，表示该价位已被摘除                                        |

> 对于 `depthAction = 1` 的帧，将收到的档位应用到本地订单簿：以新的 `size` 覆盖该价位，当 `size = 0` 时删除该价位。

### 二进制布局总览

```javascript
┌─────────────┬──────────────┬────────────────────────┬────────────────────────┬──────────┐
│ Header (8B) │ Root (40B)   │ Asks: GrpHdr(4B)+N×16B │ Bids: GrpHdr(4B)+N×16B │ Symbol   │
└─────────────┴──────────────┴────────────────────────┴────────────────────────┴──────────┘
```

---

## 解码示例

### 原始二进制 (hex)

下例为一帧增量更新（`depthAction = 1`），仅携带发生变化的买卖档位。`Snapshot` 帧（`depthAction = 0`）结构相同，区别在于 `pseq` 为 `0`，且 `asks` / `bids` 分组为完整档位。

```javascript
28 00 E9 03 01 00 05 00  <- header: blockLength=40, templateId=1001, schemaId=1, version=5
00 40 1E 18 24 0A 06 00  <- ts (uint64 LE) = 1700000000000000
2A 00 00 00 00 00 00 00  <- seq (uint64 LE) = 42
FE                        <- priceExponent (int8) = -2
FC                        <- sizeExponent (int8) = -4
E8 43 1E 18 24 0A 06 00  <- sts (uint64 LE) = 1700000000001000
01                        <- category (uint8) = 1 (usdt-futures)
29 00 00 00 00 00 00 00  <- pseq (uint64 LE) = 41
01                        <- depthAction (uint8) = 1 (Update)
00 00 00 00              <- padding4
10 00 02 00              <- asks group: entryBlockLength=16, numInGroup=2
52 33 64 00 00 00 00 00  <- asks[0].price = 6566738
10 27 00 00 00 00 00 00  <- asks[0].size  = 10000
B6 33 64 00 00 00 00 00  <- asks[1].price = 6566838
20 4E 00 00 00 00 00 00  <- asks[1].size  = 20000
10 00 02 00              <- bids group: entryBlockLength=16, numInGroup=2
26 32 64 00 00 00 00 00  <- bids[0].price = 6566438
30 75 00 00 00 00 00 00  <- bids[0].size  = 30000
C2 31 64 00 00 00 00 00  <- bids[1].price = 6566338
40 9C 00 00 00 00 00 00  <- bids[1].size  = 40000
07 42 54 43 55 53 44 54  <- symbol: length=7, "BTCUSDT"
```

### 解码后 JSON

```javascript
{
  "header": {
    "block_length": 40,
    "template_id": 1001,
    "schema_id": 1,
    "version": 5
  },
  "ts": 1700000000000000,
  "seq": 42,
  "price_exponent": -2,
  "size_exponent": -4,
  "sts": 1700000000001000,
  "category": 1,
  "pseq": 41,
  "depth_action": 1,
  "asks": [
    {
      "price": "65667.38",
      "size": "1.0000"
    },
    {
      "price": "65668.38",
      "size": "2.0000"
    }
  ],
  "bids": [
    {
      "price": "65664.38",
      "size": "3.0000"
    },
    {
      "price": "65663.38",
      "size": "4.0000"
    }
  ],
  "symbol": "BTCUSDT"
}
```

---

## Python 接入示例

```javascript
"""Bitget books50 SBE WebSocket 订阅示例"""
import asyncio
import json
import struct
from decimal import Decimal
import websockets

WS_URL    = "wss://ws.bitget.com/v3/ws/public/sbe"
INST_TYPE = "usdt-futures"
SYMBOL    = "BTCUSDT"
TOPIC     = "books50"


DEPTH_ACTION = {0: "Snapshot", 1: "Update"}


def decode_depth50(data: bytes) -> dict:
    """解码 Depth50 (templateId=1001) SBE 帧"""
    block_length, template_id, schema_id, version = struct.unpack_from('<HHHH', data, 0)
    assert template_id == 1001, f"unexpected templateId: {template_id}"

    offset     = 8
    base       = offset
    ts,        = struct.unpack_from('<Q', data, offset); offset += 8
    seq,       = struct.unpack_from('<Q', data, offset); offset += 8
    price_exp, = struct.unpack_from('<b', data, offset); offset += 1
    size_exp,  = struct.unpack_from('<b', data, offset); offset += 1
    sts,       = struct.unpack_from('<Q', data, offset); offset += 8
    category,  = struct.unpack_from('<B', data, offset); offset += 1

    # sinceVersion=5：pseq + depthAction
    pseq = depth_action = None
    if version >= 5:
        pseq,         = struct.unpack_from('<Q', data, offset); offset += 8
        depth_action, = struct.unpack_from('<B', data, offset); offset += 1

    # 跳过 padding，以 blockLength 为准
    offset = base + block_length

    def decode_group(off):
        entry_bl, num = struct.unpack_from('<HH', data, off); off += 4
        levels = []
        for _ in range(num):
            start = off
            p, = struct.unpack_from('<q', data, off); off += 8
            s, = struct.unpack_from('<q', data, off); off += 8
            off = start + entry_bl
            levels.append({
                "price": str(Decimal(p) * Decimal(10) ** price_exp),
                "size":  str(Decimal(s) * Decimal(10) ** size_exp),
            })
        return levels, off

    asks, offset = decode_group(offset)
    bids, offset = decode_group(offset)

    sym_len, = struct.unpack_from('<B', data, offset); offset += 1
    symbol = data[offset:offset + sym_len].decode('utf-8')

    return {
        "ts": ts, "seq": seq, "pseq": pseq,
        "price_exponent": price_exp, "size_exponent": size_exp,
        "sts": sts, "category": category,
        "depth_action": depth_action,
        "asks": asks, "bids": bids, "symbol": symbol,
    }


async def main():
    async with websockets.connect(WS_URL) as ws:
        # 订阅
        await ws.send(json.dumps({
            "op": "subscribe",
            "args": [{"instType": INST_TYPE, "topic": TOPIC, "symbol": SYMBOL}]
        }))
        print(f"[SUB] {INST_TYPE} {TOPIC} {SYMBOL}")

        # 心跳
        async def ping_loop():
            while True:
                await asyncio.sleep(20)
                await ws.send("ping")
                print("[PING] sent")

        asyncio.create_task(ping_loop())

        async for message in ws:
            if isinstance(message, bytes):
                try:
                    msg = decode_depth50(message)
                    ts_ms = msg['ts'] // 1000
                    action = DEPTH_ACTION.get(msg['depth_action'], '?')
                    print(f"\n[Depth50] {msg['symbol']}  ts={ts_ms}ms  seq={msg['seq']}  pseq={msg['pseq']}  sts={msg['sts']}  category={msg['category']}")
                    print(f"  price_exp={msg['price_exponent']}  size_exp={msg['size_exponent']}  action={action}")
                    print(f"  asks ({len(msg['asks'])} levels):")
                    for i, lvl in enumerate(msg['asks'][:5]):
                        print(f"    [{i}] price={lvl['price']}  size={lvl['size']}")
                    print(f"  bids ({len(msg['bids'])} levels):")
                    for i, lvl in enumerate(msg['bids'][:5]):
                        print(f"    [{i}] price={lvl['price']}  size={lvl['size']}")
                except Exception as e:
                    print(f"[ERROR] {e}  raw={message.hex()}")
            else:
                if message == "pong":
                    print("[PONG] received")
                else:
                    print(f"[TEXT] {message}")


if __name__ == "__main__":
    asyncio.run(main())
```