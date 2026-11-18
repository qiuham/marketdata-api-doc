---
exchange: bitget
source_url: https://www.bitget.com/docs/uta/websocket/sbe/sbe-bbo
api_type: SBE
updated_at: 2026-11-18 08:37:18.312885
---

# SBE BBO Integration Guide

## Overview

| Field            | Description                                                                                                                                                                                                    |
|:-----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Topic            | `books1`                                                                                                                                                                                                       |
| TemplateId       | `1002`                                                                                                                                                                                                         |
| Format           | SBE binary frame (opcode = 2), little-endian                                                                                                                                                                   |
| Depth            | Provides real-time Level 1 best bid/ask prices and corresponding order sizes                                                                                                                                   |
| Units            | Timestamps in microseconds (µs), but only accurate to milliseconds. Append `000` to a millisecond timestamp to get the microsecond format. E.g., millisecond timestamp 1726233600001 corresponds to µs timestamp 1726233600001000 |
| Update Frequency | Real-time                                                                                                                                                                                                      |

---

## Connection

- **WebSocket URL**: `wss://ws.bitget.com/v3/ws/public/sbe`
- **Heartbeat**: Send text frame `"ping"` every 30 seconds, server responds with `"pong"`
- **Message Protocol**: JSON text frames during subscription phase; SBE binary frames during market data push phase, distinguished by WebSocket opCode (opCode=1 for text, opCode=2 for binary)

---

## Subscription Flow

### 1. Send Subscription Request

```json
{
  "op": "subscribe",
  "args": [
    {
      "instType": "usdt-futures",
      "topic": "books1",
      "symbol": "BTCUSDT"
    }
  ]
}
```

**Parameter Description:**

| Parameter | Type   | Description                                                                         |
|:----------|:-------|:------------------------------------------------------------------------------------|
| instType  | string | Product type: `spot` <br/> `usdt-futures`<br/> `usdc-futures`  <br/> `coin-futures` |
| topic     | string | Fixed value: `books1`                                                               |
| symbol    | string | Symbol name, e.g. `BTCUSDT`, `ETHUSDT`                                              |

### 2. Subscription Confirmation

```json
{
  "event": "subscribe",
  "arg": {
    "instType": "usdt-futures",
    "topic": "books1",
    "symbol": "BTCUSDT"
  }
}
```

### 3. Receiving Data

After subscription confirmation, SBE binary frames are pushed in real-time as BBO updates arrive.

The `books1` channel uses **auto-culling**: under high system load, stale events may be discarded instead of queued and delivered with delay. For example, if a new BBO event is generated at time T2 while a prior event at T1 (T1 < T2) is still pending delivery, the T1 event is dropped and only the T2 event is sent. This behavior is applied independently per symbol.

### 4. Unsubscribe

```json
{
  "op": "unsubscribe",
  "args": [
    {
      "instType": "usdt-futures",
      "topic": "books1",
      "symbol": "BTCUSDT"
    }
  ]
}
```

---

## SBE Message Structure

Best bid/ask price and corresponding size for a specified trading pair.

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
| templateId  | uint16 | 2             | Channel unique identifier, fixed value = `1002` |
| schemaId    | uint16 | 2             | Schema ID                                       |
| version     | uint16 | 2             | Schema version                                  |

### Message Field Definitions

| #   | Field         | Type         | Description                                                                                                                                                                                                              |
|:----|:--------------|:-------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| -   | messageHeader | Composite    | Fixed header                                                                                                                                                                                                             |
| 1   | ts            | uint64       | Matching engine timestamp<br/> µs timestamp, but only accurate to milliseconds. Append `000` to a millisecond timestamp to get the microsecond format. E.g., millisecond timestamp 1726233600001 → µs 1726233600001000   |
| 2   | bid1Price     | int64        | Best bid price                                                                                                                                                                                                           |
| 3   | bid1Size      | int64        | Best bid size                                                                                                                                                                                                            |
| 4   | ask1Price     | int64        | Best ask price                                                                                                                                                                                                           |
| 5   | ask1Size      | int64        | Best ask size                                                                                                                                                                                                             |
| 6   | priceExponent | int8         | Price exponent                                                                                                                                                                                                            |
| 7   | sizeExponent  | int8         | Size exponent                                                                                                                                                                                                              |
| 8   | seq           | uint64       | Depth sequence number, used for message ordering and packet loss detection                                                                                                                                                |
| 9   | sts           | uint64       | Stream service push timestamp in microseconds                                                                                                                                                                             |
| 10  | category      | uint8        | Product line: `spot` / `usdt-futures` / `coin-futures` / `usdc-futures`                                                                                                                                                   |
| 100 | padding       | uint8        | Padding bytes                                                                                                                                                                                                              |
| 200 | symbol        | varString[8] | Symbol name, UTF-8 format                                                                                                                                                                                          |

### Binary Layout Overview

```
┌─────────────┬──────────────┬──────────┐
│ Header (8B) │ Root (56B)   │ Symbol   │
└─────────────┴──────────────┴──────────┘
```

**Total message size**: 8 + 56 + 1 + len(symbol) = approximately 72 bytes

---

## Decoding Example

### Raw Binary (hex)

```javascript
38 00 EA 03 01 00 02 00  <- header: blockLength=56, templateId=1002, schemaId=1, version=2
01 80 C6 A7 86 3E 06 00  <- ts (uint64 LE)
4E 3C 64 00 00 00 00 00  <- bid1Price = 6569038
98 3A 00 00 00 00 00 00  <- bid1Size  = 15000
52 3C 64 00 00 00 00 00  <- ask1Price = 6569042
20 4E 00 00 00 00 00 00  <- ask1Size  = 20000
FE                        <- priceExponent = -2
FC                        <- sizeExponent  = -4
01 00 00 00 00 00 00 00  <- seq (uint64 LE) = 1
00 00 00 00 00 00        <- padding6
07 42 54 43 55 53 44 54  <- symbol: length=7, "BTCUSDT"
```

### Decoded JSON

```javascript
{
  "header": {
    "block_length": 56,
    "template_id": 1002,
    "schema_id": 1,
    "version": 2
  },
  "ts": 1700000000000001,
  "bid1_price": "65690.38",
  "bid1_size": "1.5000",
  "ask1_price": "65690.42",
  "ask1_size": "2.0000",
  "price_exponent": -2,
  "size_exponent": -4,
  "seq": 1,
  "sts": 1700000000001001,
  "category": 1,
  "symbol": "BTCUSDT"
}
```

---

## Python Integration Example

```javascript
"""Bitget books1 (BBO) SBE WebSocket subscription example"""
import asyncio
import json
import struct
from decimal import Decimal
import websockets

WS_URL    = "wss://ws.bitget.com/v3/ws/public/sbe"
INST_TYPE = "usdt-futures"
SYMBOL    = "BTCUSDT"
TOPIC     = "books1"


def decode_bbo(data: bytes) -> dict:
    """Decode BestBidAsk (templateId=1002) SBE frame"""
    block_length, template_id, schema_id, version = struct.unpack_from('<HHHH', data, 0)
    assert template_id == 1002, f"unexpected templateId: {template_id}"

    offset     = 8
    base       = offset
    ts,         = struct.unpack_from('<Q', data, offset); offset += 8
    bid1_price, = struct.unpack_from('<q', data, offset); offset += 8
    bid1_size,  = struct.unpack_from('<q', data, offset); offset += 8
    ask1_price, = struct.unpack_from('<q', data, offset); offset += 8
    ask1_size,  = struct.unpack_from('<q', data, offset); offset += 8
    price_exp,  = struct.unpack_from('<b', data, offset); offset += 1
    size_exp,   = struct.unpack_from('<b', data, offset); offset += 1
    seq,        = struct.unpack_from('<Q', data, offset); offset += 8
    sts,        = struct.unpack_from('<Q', data, offset); offset += 8
    category,   = struct.unpack_from('<B', data, offset); offset += 1

    # Skip padding, based on blockLength
    offset = base + block_length

    # symbol (varString8)
    sym_len, = struct.unpack_from('<B', data, offset); offset += 1
    symbol = data[offset:offset + sym_len].decode('utf-8')

    to_dec = lambda m, e: Decimal(m) * Decimal(10) ** e

    return {
        "ts": ts,
        "bid1_price": str(to_dec(bid1_price, price_exp)),
        "bid1_size":  str(to_dec(bid1_size,  size_exp)),
        "ask1_price": str(to_dec(ask1_price, price_exp)),
        "ask1_size":  str(to_dec(ask1_size,  size_exp)),
        "price_exponent": price_exp,
        "size_exponent":  size_exp,
        "seq": seq,
        "sts": sts,
        "category": category,
        "symbol": symbol,
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
                    msg = decode_bbo(message)
                    ts_ms = msg['ts'] // 1000
                    spread = Decimal(msg['ask1_price']) - Decimal(msg['bid1_price'])
                    print(f"\n[BBO] {msg['symbol']}  ts={ts_ms}ms  seq={msg['seq']}  sts={msg['sts']}  category={msg['category']}")
                    print(f"  bid: price={msg['bid1_price']}  size={msg['bid1_size']}")
                    print(f"  ask: price={msg['ask1_price']}  size={msg['ask1_size']}")
                    print(f"  spread: {spread}")
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

# SBE BBO 接入指南

## 总览

| 字段         | 说明                                                                                                           |
|:-----------|:-------------------------------------------------------------------------------------------------------------|
| Topic      | `books1`                                                                                                     |
| TemplateId | `1002`                                                                                                       |
| Format     | SBE 二进制 frame (opcode = 2), little-endian                                                                    |
| Depth      | 提供即时 Level 1 最优买卖价及对应挂单量                                                                                     |
| Units      | 时间戳为 microseconds (µs) ，但是仅精确到毫秒。毫秒时间加上 000 得到微秒格式时间。比如：毫秒时间 1726233600001 对应的微秒格式时间 (µs) 为 1726233600001000 |
| 更新频率       | 实时                                                                                                               |

---

## 连接

- **WebSocket URL**: `wss://ws.bitget.com/v3/ws/public/sbe`
- **心跳**: 每 30 秒发送文本帧 `"ping"`, 服务端返回 `"pong"`
- **报文机制**: 订阅阶段使用 JSON 文本帧；行情推送阶段使用 SBE 二进制帧，通过 WebSocket opCode 区分（opCode=1 文本,
  opCode=2 二进制）

---

## 订阅流程

### 1. 发送订阅请求

```json
{
  "op": "subscribe",
  "args": [
    {
      "instType": "usdt-futures",
      "topic": "books1",
      "symbol": "BTCUSDT"
    }
  ]
}
```

**参数说明:**

| 参数       | 类型     | 说明                                                                          |
|:---------|:-------|:----------------------------------------------------------------------------|
| instType | string | 产品类型: `spot` <br/> `usdt-futures` <br/> `usdc-futures` <br/> `coin-futures` |
| topic    | string | 固定值: `books1`                                                               |
| symbol   | string | 交易对, 如 `BTCUSDT`, `ETHUSDT`                                                 |

### 2. 订阅确认

```json
{
  "event": "subscribe",
  "arg": {
    "instType": "usdt-futures",
    "topic": "books1",
    "symbol": "BTCUSDT"
  }
}
```

### 3. 接收数据

订阅确认后, BBO 更新时实时推送 SBE 二进制帧。

`books1` 频道使用**自动剔除（auto-culling）**机制：当系统负载较高时，可能会丢弃过时的事件，而不是将所有事件排队并延迟发送。例如，如果在时间 T2 生成了一个新的 BBO 事件，而此时仍有一个未发送的事件排队在时间 T1（且 T1 < T2），则会丢弃时间 T1 的事件，系统只会发送时间 T2 的事件。此操作基于每个交易对分别进行。

### 4. 取消订阅

```json
{
  "op": "unsubscribe",
  "args": [
    {
      "instType": "usdt-futures",
      "topic": "books1",
      "symbol": "BTCUSDT"
    }
  ]
}
```

---

## SBE 消息结构

指定交易对的最优买价/卖价及对应数量。

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
| templateId  | uint16    | 2         | 频道唯一标识，固定值 = `1002` |
| schemaId    | uint16    | 2         | Schema ID           |
| version     | uint16    | 2         | Schema 版本           |

### 消息字段定义

| 序号  | 字段名           | 类型           | 说明                                                                                                          |
|:----|:--------------|:-------------|:------------------------------------------------------------------------------------------------------------|
| -   | messageHeader | Composite    | 固定头部                                                                                                        |
| 1   | ts            | uint64       | 撮合引擎时间戳<br/> µs 微秒时间戳，但是仅精确到毫秒。毫秒时间加上 000 得到微秒格式时间。比如：毫秒时间 1726233600001 对应的微秒格式时间 (µs) 为 1726233600001000  |
| 2   | bid1Price     | int64        | 买一价                                                                                                         |
| 3   | bid1Size      | int64        | 买一量                                                                                                         |
| 4   | ask1Price     | int64        | 卖一价                                                                                                         |
| 5   | ask1Size      | int64        | 卖一量                                                                                                         |
| 6   | priceExponent | int8         | 价格指数                                                                                                        |
| 7   | sizeExponent  | int8         | 数量指数                                                                                                        |
| 8   | seq           | uint64       | 深度序列号，用于消息排序与丢包检测                                                                                           |
| 9   | sts           | uint64       | 流服务推送时间戳，微秒（µs）                                                                                            |
| 10  | category      | uint8        | 业务线：`spot` 现货 / `usdt-futures` U本位合约 / `coin-futures` 币本位合约 / `usdc-futures` USDC合约                       |
| 100 | padding       | uint8        | 填充字节                                                                                                        |
| 200 | symbol        | varString[8] | 交易对名称，UTF-8 格式                                                                                              |

### 二进制布局总览

```
┌─────────────┬──────────────┬──────────┐
│ Header (8B) │ Root (56B)   │ Symbol   │
└─────────────┴──────────────┴──────────┘
```

**总消息大小**: 8 + 56 + 1 + len(symbol) = 约 72 字节

---

## 解码示例

### 原始二进制 (hex)

```javascript
38 00 EA 03 01 00 02 00  <- header: blockLength=56, templateId=1002, schemaId=1, version=2
01 80 C6 A7 86 3E 06 00  <- ts (uint64 LE)
4E 3C 64 00 00 00 00 00  <- bid1Price = 6569038
98 3A 00 00 00 00 00 00  <- bid1Size  = 15000
52 3C 64 00 00 00 00 00  <- ask1Price = 6569042
20 4E 00 00 00 00 00 00  <- ask1Size  = 20000
FE                        <- priceExponent = -2
FC                        <- sizeExponent  = -4
01 00 00 00 00 00 00 00  <- seq (uint64 LE) = 1
00 00 00 00 00 00        <- padding6
07 42 54 43 55 53 44 54  <- symbol: length=7, "BTCUSDT"
```

### 解码后 JSON

```javascript
{
  "header": {
    "block_length": 56,
    "template_id": 1002,
    "schema_id": 1,
    "version": 2
  },
  "ts": 1700000000000001,
  "bid1_price": "65690.38",
  "bid1_size": "1.5000",
  "ask1_price": "65690.42",
  "ask1_size": "2.0000",
  "price_exponent": -2,
  "size_exponent": -4,
  "seq": 1,
  "sts": 1700000000001001,
  "category": 1,
  "symbol": "BTCUSDT"
}
```

---

## Python 接入示例

```javascript
"""Bitget books1 (BBO) SBE WebSocket 订阅示例"""
import asyncio
import json
import struct
from decimal import Decimal
import websockets

WS_URL    = "wss://ws.bitget.com/v3/ws/public/sbe"
INST_TYPE = "usdt-futures"
SYMBOL    = "BTCUSDT"
TOPIC     = "books1"


def decode_bbo(data: bytes) -> dict:
    """解码 BestBidAsk (templateId=1002) SBE 帧"""
    block_length, template_id, schema_id, version = struct.unpack_from('<HHHH', data, 0)
    assert template_id == 1002, f"unexpected templateId: {template_id}"

    offset     = 8
    base       = offset
    ts,         = struct.unpack_from('<Q', data, offset); offset += 8
    bid1_price, = struct.unpack_from('<q', data, offset); offset += 8
    bid1_size,  = struct.unpack_from('<q', data, offset); offset += 8
    ask1_price, = struct.unpack_from('<q', data, offset); offset += 8
    ask1_size,  = struct.unpack_from('<q', data, offset); offset += 8
    price_exp,  = struct.unpack_from('<b', data, offset); offset += 1
    size_exp,   = struct.unpack_from('<b', data, offset); offset += 1
    seq,        = struct.unpack_from('<Q', data, offset); offset += 8
    sts,        = struct.unpack_from('<Q', data, offset); offset += 8
    category,   = struct.unpack_from('<B', data, offset); offset += 1

    # 跳过 padding，以 blockLength 为准
    offset = base + block_length

    # symbol (varString8)
    sym_len, = struct.unpack_from('<B', data, offset); offset += 1
    symbol = data[offset:offset + sym_len].decode('utf-8')

    to_dec = lambda m, e: Decimal(m) * Decimal(10) ** e

    return {
        "ts": ts,
        "bid1_price": str(to_dec(bid1_price, price_exp)),
        "bid1_size":  str(to_dec(bid1_size,  size_exp)),
        "ask1_price": str(to_dec(ask1_price, price_exp)),
        "ask1_size":  str(to_dec(ask1_size,  size_exp)),
        "price_exponent": price_exp,
        "size_exponent":  size_exp,
        "seq": seq,
        "sts": sts,
        "category": category,
        "symbol": symbol,
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
                    msg = decode_bbo(message)
                    ts_ms = msg['ts'] // 1000
                    spread = Decimal(msg['ask1_price']) - Decimal(msg['bid1_price'])
                    print(f"\n[BBO] {msg['symbol']}  ts={ts_ms}ms  seq={msg['seq']}  sts={msg['sts']}  category={msg['category']}")
                    print(f"  bid: price={msg['bid1_price']}  size={msg['bid1_size']}")
                    print(f"  ask: price={msg['ask1_price']}  size={msg['ask1_size']}")
                    print(f"  spread: {spread}")
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