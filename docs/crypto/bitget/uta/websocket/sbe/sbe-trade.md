---
exchange: bitget
source_url: https://www.bitget.com/docs/uta/websocket/sbe/sbe-trade
api_type: SBE
updated_at: 2026-11-24 19:01:43.319904
---

# SBE Public Trade Integration Guide

## Overview

| Field            | Description                                                                                                                                                                                                    |
|:-----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Topic            | `publicTrade`                                                                                                                                                                                                  |
| TemplateId       | `1003`                                                                                                                                                                                                         |
| Format           | SBE binary frame (opcode = 2), little-endian                                                                                                                                                                   |
| Units            | Timestamps in microseconds (µs), but only accurate to milliseconds. Append `000` to a millisecond timestamp to get the microsecond format. E.g., millisecond timestamp 1726233600001 corresponds to µs timestamp 1726233600001000 |
| Content          | Public platform trade records (batch push, a single frame may contain multiple trades)                                                                                                                         |
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
      "topic": "publicTrade",
      "symbol": "BTCUSDT"
    }
  ]
}
```

**Parameter Description:**

| Parameter | Type   | Description                                                                          |
|:----------|:-------|:-------------------------------------------------------------------------------------|
| instType  | string | Product type: `spot` <br/> `usdt-futures`  <br/> `usdc-futures` <br/> `coin-futures` |
| topic     | string | Fixed value: `publicTrade`                                                           |
| symbol    | string | Symbol name, e.g. `BTCUSDT`, `ETHUSDT`                                               |

### 2. Subscription Confirmation

```json
{
  "event": "subscribe",
  "arg": {
    "instType": "usdt-futures",
    "topic": "publicTrade",
    "symbol": "BTCUSDT"
  }
}
```

### 3. Receiving Data

After subscription confirmation, SBE binary frames are pushed in real-time whenever a trade occurs. A single frame may contain multiple trades (batch).

### 4. Unsubscribe

```json
{
  "op": "unsubscribe",
  "args": [
    {
      "instType": "usdt-futures",
      "topic": "publicTrade",
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
| templateId  | uint16 | 2             | Channel unique identifier, fixed value = `1003` |
| schemaId    | uint16 | 2             | Schema ID                                       |
| version     | uint16 | 2             | Schema version                                  |

### Message Field Definitions

**Root block**

| id  | Field         | Type      | Description  |
|:----|:--------------|:----------|:-------------|
| -   | messageHeader | Composite | Fixed header |
| 1   | priceExponent | int8      | Price exponent |
| 2   | sizeExponent  | int8      | Size exponent  |
| 100 | padding       | uint8  | Padding bytes  |

**Group: `trades` (id=200)**

| id  | Field  | Type   | Description                                                                                                                                                                                                            |
|:----|:-------|:-------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1   | ts     | uint64 | Matching engine timestamp<br/> µs timestamp, but only accurate to milliseconds. Append `000` to a millisecond timestamp to get the microsecond format. E.g., millisecond timestamp 1726233600001 → µs 1726233600001000 |
| 2   | execId | uint64 | Execution ID                                                                                                                                                                                                           |
| 3   | price  | int64  | Trade price mantissa                                                                                                                                                                                                   |
| 4   | size   | int64  | Trade size mantissa                                                                                                                                                                                                    |
| 5   | side     | uint8  | Trade direction: Buy / Sell                                                                                                                                                                                          |
| 6   | isRPI    | uint8 (BooleanType) | Retail Price Improvement flag: `T` / `F` (since schema version 4)                                                                                                                                      |
| 7   | sts      | uint64 | Stream service push timestamp in microseconds                                                                                                                                                                        |
| 8   | category | uint8  | Product line: `spot` / `usdt-futures` / `coin-futures` / `usdc-futures`                                                                                                                                              |
| 50  | padding  | uint8  | Padding bytes                                                                                                                                                                                                        |

**Data**

| id  | Field  | Type         | Description               |
|:----|:-------|:-------------|:--------------------------|
| 300 | symbol | varString[8] | Symbol name, UTF-8 format |

### Binary Layout Overview

```javascript
┌─────────────┬─────────────┬──────────────────────────────────────────┬──────────┐
│ Header (8B) │ Root (8B)   │ Trades: GrpHdr(4B) + N×40B               │ Symbol   │
└─────────────┴─────────────┴──────────────────────────────────────────┴──────────┘
```

**Single trade message size**: 8 + 8 + 4 + 40 + 1 + len(symbol) = approximately 69 bytes  
**N trade message size**: 8 + 8 + 4 + 40×N + 1 + len(symbol)

---

## Trade Direction (side)

| Value | Name | Description               |
|:------|:-----|:--------------------------|
| 0     | Buy  | Active buy (Taker buyer)  |
| 1     | Sell | Active sell (Taker seller)|

---

## Decoding Example

### Raw Binary (single trade, hex)

```javascript
08 00 EB 03 01 00 04 00  <- header: blockLength=8, templateId=1003, schemaId=1, version=4
FE                       <- priceExponent = -2
FC                       <- sizeExponent  = -4
00 00 00 00 00 00        <- padding6
28 00 01 00              <- trades group: entryBlockLength=40, numInGroup=1
02 80 C6 A7 86 3E 06 00  <- trades[0].ts       (uint64 LE)
0F 27 00 00 00 00 00 00  <- trades[0].execId   = 9999
52 39 64 00 00 00 00 00  <- trades[0].price    = 6566738
88 13 00 00 00 00 00 00  <- trades[0].size     = 5000
00                       <- trades[0].side    = 0 (Buy)
00 00 00 00 00 00 00     <- padding7
07 42 54 43 55 53 44 54  <- symbol: length=7, "BTCUSDT"
```

### Decoded JSON

```javascript
{
  "header": {
    "block_length": 8,
    "template_id": 1003,
    "schema_id": 1,
    "version": 4
  },
  "price_exponent": -2,
  "size_exponent": -4,
  "trades": [
    {
      "ts": 1700000000000002,
      "exec_id": 9999,
      "price": "65667.38",
      "size": "0.5000",
      "side": "Buy",
      "isRPI": "F",
      "sts": 1700000000001002,
      "category": 1
    }
  ],
  "symbol": "BTCUSDT"
}
```

### Batch Trade Decoded JSON (multiple trades)

```javascript
{
  "header": {
    "block_length": 8,
    "template_id": 1003,
    "schema_id": 1,
    "version": 4
  },
  "price_exponent": -2,
  "size_exponent": -4,
  "trades": [
    {
      "ts": 1700000000000002,
      "exec_id": 10001,
      "price": "65665.78",
      "size": "0.5000",
      "side": "Buy",
      "isRPI": "F",
      "sts": 1700000000001002,
      "category": 1
    },
    {
      "ts": 1700000000000003,
      "exec_id": 10002,
      "price": "65666.00",
      "size": "1.2000",
      "side": "Sell",
      "isRPI": "T",
      "sts": 1700000000001003,
      "category": 1
    },
    {
      "ts": 1700000000000004,
      "exec_id": 10003,
      "price": "65664.50",
      "size": "0.3000",
      "side": "Buy",
      "isRPI": "F",
      "sts": 1700000000001004,
      "category": 1
    }
  ],
  "symbol": "BTCUSDT"
}
```

---

## Python Integration Example

```javascript

"""Bitget publicTrade SBE WebSocket subscription example"""
import asyncio
import json
import struct
from decimal import Decimal
import websockets

WS_URL    = "wss://ws.bitget.com/v3/ws/public/sbe"
INST_TYPE = "usdt-futures"
SYMBOL    = "BTCUSDT"
TOPIC     = "publicTrade"

SIDE_MAP = {0: "Buy", 1: "Sell"}
BOOLEAN_MAP = {0: "F", 1: "T"}


def decode_trade(data: bytes) -> dict:
    """Decode Trade (templateId=1003) SBE frame"""
    block_length, template_id, schema_id, version = struct.unpack_from('<HHHH', data, 0)
    assert template_id == 1003, f"unexpected templateId: {template_id}"

    offset    = 8
    base      = offset
    price_exp, = struct.unpack_from('<b', data, offset); offset += 1
    size_exp,  = struct.unpack_from('<b', data, offset); offset += 1

    # Skip padding, based on blockLength
    offset = base + block_length

    # trades group
    entry_bl, num = struct.unpack_from('<HH', data, offset); offset += 4
    has_is_rpi = version >= 4  # sinceVersion=4: entry carries the isRPI field (entryBlockLength stays fixed due to padding, so gate on schema version instead)

    to_dec = lambda m, e: Decimal(m) * Decimal(10) ** e

    trades = []
    for _ in range(num):
        entry_start = offset
        ts,       = struct.unpack_from('<Q', data, offset); offset += 8
        exec_id,  = struct.unpack_from('<Q', data, offset); offset += 8
        price,    = struct.unpack_from('<q', data, offset); offset += 8
        size,     = struct.unpack_from('<q', data, offset); offset += 8
        side_raw,  = struct.unpack_from('<B', data, offset); offset += 1
        if has_is_rpi:
            is_rpi_raw, = struct.unpack_from('<B', data, offset); offset += 1
        sts,       = struct.unpack_from('<Q', data, offset); offset += 8
        category,  = struct.unpack_from('<B', data, offset); offset += 1
        # Skip padding, based on entry_bl
        offset = entry_start + entry_bl
        trade = {
            "ts":       ts,
            "exec_id":  exec_id,
            "price":    str(to_dec(price, price_exp)),
            "size":     str(to_dec(size,  size_exp)),
            "side":     SIDE_MAP.get(side_raw, str(side_raw)),
        }
        if has_is_rpi:
            trade["isRPI"] = BOOLEAN_MAP.get(is_rpi_raw, str(is_rpi_raw))
        trade["sts"] = sts
        trade["category"] = category
        trades.append(trade)

    # symbol (varString8)
    sym_len, = struct.unpack_from('<B', data, offset); offset += 1
    symbol = data[offset:offset + sym_len].decode('utf-8')

    return {
        "price_exponent": price_exp,
        "size_exponent":  size_exp,
        "trades": trades,
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
                    msg = decode_trade(message)
                    print(f"\n[Trade] {msg['symbol']}  ({len(msg['trades'])} trades)")
                    for t in msg['trades']:
                        ts_ms = t['ts'] // 1000
                        print(f"  [{t['side']:4s}] price={t['price']}  size={t['size']}  "
                              f"ts={ts_ms}ms  execId={t['exec_id']}")
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

# SBE Public Trade 接入指南

## 总览

| 字段         | 说明                                                                                                             |
|:-----------|:---------------------------------------------------------------------------------------------------------------|
| Topic      | `publicTrade`                                                                                                  |
| TemplateId | `1003`                                                                                                         |
| Format     | SBE 二进制 frame (opcode = 2), little-endian                                                                      |
| Units      | 时间戳为 microseconds (µs) ，但是仅精确到毫秒。毫秒时间加上 000 得到微秒格式时间。比如：毫秒时间 1726233600001 对应的微秒格式时间 (µs) 为 1726233600001000   |
| 推送内容       | 平台公开成交记录（批量推送，一帧可包含多笔成交）                                                                                       |
| 更新频率       | 实时                                                                                                             |

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
      "topic": "publicTrade",
      "symbol": "BTCUSDT"
    }
  ]
}
```

**参数说明:**

| 参数       | 类型     | 说明                                                                           |
|:---------|:-------|:-----------------------------------------------------------------------------|
| instType | string | 产品类型:  `spot` <br/> `usdt-futures` <br/> `usdc-futures` <br/> `coin-futures` |
| topic    | string | 固定值: `publicTrade`                                                           |
| symbol   | string | 交易对, 如 `BTCUSDT`, `ETHUSDT`                                                  |

### 2. 订阅确认

```json
{
  "event": "subscribe",
  "arg": {
    "instType": "usdt-futures",
    "topic": "publicTrade",
    "symbol": "BTCUSDT"
  }
}
```

### 3. 接收数据

订阅确认后, 每次有成交即实时推送 SBE 二进制帧。单帧可包含多笔成交（batch）。

### 4. 取消订阅

```json
{
  "op": "unsubscribe",
  "args": [
    {
      "instType": "usdt-futures",
      "topic": "publicTrade",
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
| templateId  | uint16    | 2         | 频道唯一标识，固定值 = `1003` |
| schemaId    | uint16    | 2         | Schema ID           |
| version     | uint16    | 2         | Schema 版本           |

### 消息字段定义

**Root block**

| id  | 字段名           | 类型        | 说明                            |
|:----|:--------------|:----------|:------------------------------|
| -   | messageHeader | Composite | 固定头部                          |
| 1   | priceExponent | int8      | 价格指数                          |
| 2   | sizeExponent  | int8      | 数量指数                          |
| 100 | padding       | uint8     | 填充字节           |

**Group: `trades` (id=200)**

| id  | 字段名     | 类型       | 说明                                                                                                      |
|:----|:--------|:---------|:--------------------------------------------------------------------------------------------------------|
| 1   | ts      | uint64   | 撮合引擎时间戳<br/> µs 微秒时间戳，但是仅精确到毫秒。毫秒时间加上 000 得到微秒格式时间。比如：毫秒时间 1726233600001 对应的微秒格式时间 (µs) 为 1726233600001000 |
| 2   | execId  | uint64   | 成交 ID                                                                                                   |
| 3   | price   | int64    | 成交价格尾数                                                                                                  |
| 4   | size    | int64    | 成交数量尾数                                                                                                  |
| 5   | side     | uint8    | 成交方向，Buy 买入 / Sell 卖出                                                                                  |
| 6   | isRPI    | uint8 (BooleanType) | 零售价格改善标记（Retail Price Improvement flag）：`T` / `F`（自 schema version 4 起支持）                    |
| 7   | sts      | uint64   | 流服务推送时间戳，微秒（µs）                                                                                           |
| 8   | category | uint8    | 业务线：`spot` 现货 / `usdt-futures` U本位合约 / `coin-futures` 币本位合约 / `usdc-futures` USDC合约         |
| 50  | padding  | uint8    | 填充字节                                                                                    |

**Data**

| id  | 字段名    | 类型           | 说明             |
|:----|:-------|:-------------|:---------------|
| 300 | symbol | varString[8] | 交易对名称，UTF-8 格式 |

### 二进制布局总览

```
┌─────────────┬─────────────┬──────────────────────────────────────────┬──────────┐
│ Header (8B) │ Root (8B)   │ Trades: GrpHdr(4B) + N×40B               │ Symbol   │
└─────────────┴─────────────┴──────────────────────────────────────────┴──────────┘
```

**单笔成交消息大小**: 8 + 8 + 4 + 40 + 1 + len(symbol) = 约 69 字节
**N 笔成交消息大小**: 8 + 8 + 4 + 40×N + 1 + len(symbol)

---

## 成交方向 (tradeSide)

| 值 | 名称   | 说明             |
|:--|:-----|:---------------|
| 0 | Buy  | 主动买入（Taker 买方） |
| 1 | Sell | 主动卖出（Taker 卖方） |

---

## 解码示例

### 原始二进制 (单笔成交, hex)

```javascript
08 00 EB 03 01 00 04 00  <- header: blockLength=8, templateId=1003, schemaId=1, version=4
FE                       <- priceExponent = -2
FC                       <- sizeExponent  = -4
00 00 00 00 00 00        <- padding6
28 00 01 00              <- trades group: entryBlockLength=40, numInGroup=1
02 80 C6 A7 86 3E 06 00  <- trades[0].ts       (uint64 LE)
0F 27 00 00 00 00 00 00  <- trades[0].execId   = 9999
52 39 64 00 00 00 00 00  <- trades[0].price    = 6566738
88 13 00 00 00 00 00 00  <- trades[0].size     = 5000
00                       <- trades[0].side    = 0 (Buy)
00 00 00 00 00 00 00     <- padding7
07 42 54 43 55 53 44 54  <- symbol: length=7, "BTCUSDT"
```

### 解码后 JSON

```javascript
{
  "header": {
    "block_length": 8,
    "template_id": 1003,
    "schema_id": 1,
    "version": 4
  },
  "price_exponent": -2,
  "size_exponent": -4,
  "trades": [
    {
      "ts": 1700000000000002,
      "exec_id": 9999,
      "price": "65667.38",
      "size": "0.5000",
      "side": "Buy",
      "isRPI": "F",
      "sts": 1700000000001002,
      "category": 1
    }
  ],
  "symbol": "BTCUSDT"
}
```

### 批量成交解码后 JSON (多笔)

```javascript
{
  "header": {
    "block_length": 8,
    "template_id": 1003,
    "schema_id": 1,
    "version": 4
  },
  "price_exponent": -2,
  "size_exponent": -4,
  "trades": [
    {
      "ts": 1700000000000002,
      "exec_id": 10001,
      "price": "65665.78",
      "size": "0.5000",
      "side": "Buy",
      "isRPI": "F",
      "sts": 1700000000001002,
      "category": 1
    },
    {
      "ts": 1700000000000003,
      "exec_id": 10002,
      "price": "65666.00",
      "size": "1.2000",
      "side": "Sell",
      "isRPI": "T",
      "sts": 1700000000001003,
      "category": 1
    },
    {
      "ts": 1700000000000004,
      "exec_id": 10003,
      "price": "65664.50",
      "size": "0.3000",
      "side": "Buy",
      "isRPI": "F",
      "sts": 1700000000001004,
      "category": 1
    }
  ],
  "symbol": "BTCUSDT"
}
```

---

## Python 接入示例

```javascript

"""Bitget publicTrade SBE WebSocket 订阅示例"""
import asyncio
import json
import struct
from decimal import Decimal
import websockets

WS_URL    = "wss://ws.bitget.com/v3/ws/public/sbe"
INST_TYPE = "usdt-futures"
SYMBOL    = "BTCUSDT"
TOPIC     = "publicTrade"

SIDE_MAP = {0: "Buy", 1: "Sell"}
BOOLEAN_MAP = {0: "F", 1: "T"}


def decode_trade(data: bytes) -> dict:
    """解码 Trade (templateId=1003) SBE 帧"""
    block_length, template_id, schema_id, version = struct.unpack_from('<HHHH', data, 0)
    assert template_id == 1003, f"unexpected templateId: {template_id}"

    offset    = 8
    base      = offset
    price_exp, = struct.unpack_from('<b', data, offset); offset += 1
    size_exp,  = struct.unpack_from('<b', data, offset); offset += 1

    # 跳过 padding，以 blockLength 为准
    offset = base + block_length

    # trades group
    entry_bl, num = struct.unpack_from('<HH', data, offset); offset += 4
    has_is_rpi = version >= 4  # sinceVersion=4：entry 携带 isRPI 字段（entryBlockLength 因 padding 补齐后固定不变，无法用它判断，改用 schema version 判断）

    to_dec = lambda m, e: Decimal(m) * Decimal(10) ** e

    trades = []
    for _ in range(num):
        entry_start = offset
        ts,       = struct.unpack_from('<Q', data, offset); offset += 8
        exec_id,  = struct.unpack_from('<Q', data, offset); offset += 8
        price,    = struct.unpack_from('<q', data, offset); offset += 8
        size,     = struct.unpack_from('<q', data, offset); offset += 8
        side_raw,  = struct.unpack_from('<B', data, offset); offset += 1
        if has_is_rpi:
            is_rpi_raw, = struct.unpack_from('<B', data, offset); offset += 1
        sts,       = struct.unpack_from('<Q', data, offset); offset += 8
        category,  = struct.unpack_from('<B', data, offset); offset += 1
        # 跳过 padding，以 entry_bl 为准
        offset = entry_start + entry_bl
        trade = {
            "ts":       ts,
            "exec_id":  exec_id,
            "price":    str(to_dec(price, price_exp)),
            "size":     str(to_dec(size,  size_exp)),
            "side":     SIDE_MAP.get(side_raw, str(side_raw)),
        }
        if has_is_rpi:
            trade["isRPI"] = BOOLEAN_MAP.get(is_rpi_raw, str(is_rpi_raw))
        trade["sts"] = sts
        trade["category"] = category
        trades.append(trade)

    # symbol (varString8)
    sym_len, = struct.unpack_from('<B', data, offset); offset += 1
    symbol = data[offset:offset + sym_len].decode('utf-8')

    return {
        "price_exponent": price_exp,
        "size_exponent":  size_exp,
        "trades": trades,
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
                    msg = decode_trade(message)
                    print(f"\n[Trade] {msg['symbol']}  ({len(msg['trades'])} trades)")
                    for t in msg['trades']:
                        ts_ms = t['ts'] // 1000
                        print(f"  [{t['side']:4s}] price={t['price']}  size={t['size']}  "
                              f"ts={ts_ms}ms  execId={t['exec_id']}")
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