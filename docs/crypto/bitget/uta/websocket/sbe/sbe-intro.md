---
exchange: bitget
source_url: https://www.bitget.com/docs/uta/websocket/sbe/sbe-intro
api_type: SBE
updated_at: 2026-11-26 19:03:36.025983
---

# SBE Introduction

## SBE Basics

### Core Features

- **Binary transport**: Market data is no longer delivered as text; instead, it is sent as a binary byte stream
  compliant with the FIX SBE standard.
- **Schema-driven**: An XML Schema file is provided to define field offsets and lengths.
- **Message mechanism**: After a connection is established, the system uses a differentiated message encapsulation
  mechanism. During the subscription phase, interaction is entirely based on JSON text frames. Once market data
  streaming starts, the data switches to SBE-encoded binary frames. You can separate the processing logic by identifying
  the underlying WebSocket frame opcode (`opCode`).

### Version Updates & Compatibility

- **Regular upgrades**: When new fields are added, the Schema ID remains unchanged and only the Version number is
  increased. Existing logic remains backward compatible.
- **Integration requirement**: Ensure your parser can recognize the Schema ID and Version in the message header, so it
  can handle binary streams of different versions during the transition period.

### Channel Scope

| Channel                 | Fields                                         | Update Frequency |
|:------------------------|:-----------------------------------------------|:-----------------|
| Depth50 (limited depth) | Price, quantity, order side                    | 20ms             |
| BestBidAsk (BBO)        | Best bid/ask price and order size              | Real-time        |
| Trade (public trades)   | Trade price, trade size, trade side, timestamp | Real-time        |

### Common Message Header

All SBE messages must include a fixed 8-byte header to enable parsing and identification of the subsequent data.

| Field       | Type   | Length (Byte) | Description                                                                                                           |
|:------------|:-------|:--------------|:----------------------------------------------------------------------------------------------------------------------|
| blockLength | uint16 | 2             | Root block length                                                                                                     |
| templateId  | uint16 | 2             | Unique channel identifier:<br/>**1001**: Depth50 channel<br/>**1002**: BBO channel<br/>**1003**: Public trade channel |
| schemaId    | uint16 | 2             | Schema ID                                                                                                             |
| version     | uint16 | 2             | Schema version                                                                                                        |


### SBE XML Template

```xml
<?xml version="1.0" encoding="UTF-8"?>
<sbe:messageSchema xmlns:sbe="http://fixprotocol.io/2016/sbe"
                   package="com.upex.stream.sbe"
                   id="1"
                   version="5"
                   semanticVersion="1.0.0"
                   description="UPEX Market Data SBE Schema"
                   byteOrder="littleEndian">

  <types>
    <!-- Message header -->
    <composite name="messageHeader" description="Standard SBE Message Header">
      <type name="blockLength" primitiveType="uint16" description="Root block length"/>
      <type name="templateId" primitiveType="uint16" description="Template ID"/>
      <type name="schemaId" primitiveType="uint16" description="Schema ID"/>
      <type name="version" primitiveType="uint16" description="Schema version"/>
    </composite>

    <!-- Group size encoding -->
    <composite name="groupSize16Encoding" description="Group size encoding">
      <type name="blockLength" primitiveType="uint16"/>
      <type name="numInGroup" primitiveType="uint16"/>
    </composite>

    <composite name="varString8" description="Variable length UTF-8 string.">
      <type name="length" primitiveType="uint8"/>
      <type name="varData" length="0" primitiveType="uint8" characterEncoding="UTF-8"/>
    </composite>

    <!-- Primitive type definitions -->
    <type name="timestampType" primitiveType="uint64" description="Timestamp in microseconds"/>
    <type name="priceType" primitiveType="int64" description="Price mantissa"/>
    <type name="sizeType" primitiveType="int64" description="Size mantissa"/>
    <type name="sequenceType" primitiveType="uint64" description="Sequence number"/>
    <type name="symbolType" primitiveType="char" length="24" description="Trading pair symbol"/>
    <type name="exponentType" primitiveType="int8" description="Price/Size exponent"/>

    <!-- Padding type library: covers all alignment scenarios from 0 to 7 bytes -->
    <type name="padding0" primitiveType="uint8" length="0" description="No padding needed"/>
    <type name="padding1" primitiveType="uint8" length="1" description="1 byte padding for alignment"/>
    <type name="padding2" primitiveType="uint8" length="2" description="2 bytes padding for alignment"/>
    <type name="padding3" primitiveType="uint8" length="3" description="3 bytes padding for alignment"/>
    <type name="padding4" primitiveType="uint8" length="4" description="4 bytes padding for alignment"/>
    <type name="padding5" primitiveType="uint8" length="5" description="5 bytes padding for alignment"/>
    <type name="padding6" primitiveType="uint8" length="6" description="6 bytes padding for alignment"/>
    <type name="padding7" primitiveType="uint8" length="7" description="7 bytes padding for alignment"/>

    <!-- Enum type definitions -->
    <enum name="tradeSide" encodingType="uint8" description="Trade side">
      <validValue name="Buy" description="Buy side">0</validValue>
      <validValue name="Sell" description="Sell side">1</validValue>
    </enum>

    <!-- Business line enum: instType string → uint8 mapping -->
    <enum name="instCategory" encodingType="uint8" description="Instrument category (business line)">
      <validValue name="Spot" description="Spot trading">0</validValue>
      <validValue name="UsdtFutures" description="USDT-margined futures">1</validValue>
      <validValue name="CoinFutures" description="Coin-margined futures">2</validValue>
      <validValue name="UsdcFutures" description="USDC-margined futures">3</validValue>
    </enum>

    <!-- Boolean flag enum -->
    <enum name="BooleanType" encodingType="uint8" description="Boolean flag">
      <validValue name="F" description="False">0</validValue>
      <validValue name="T" description="True">1</validValue>
    </enum>

    <!-- Depth push action enum -->
    <enum name="depthAction" encodingType="uint8" description="Depth push action: full snapshot or incremental update">
      <validValue name="Snapshot" description="Full snapshot of all levels">0</validValue>
      <validValue name="Update" description="Incremental update, only changed levels included">1</validValue>
    </enum>
  </types>

  <!-- 50-level depth message -->
  <sbe:message name="Depth50" id="1001" description="50-level depth snapshot">
    <field name="ts" id="1" type="timestampType"/>
    <field name="seq" id="2" type="sequenceType"/>
    <field name="priceExponent" id="3" type="exponentType"/>
    <field name="sizeExponent" id="4" type="exponentType"/>
    <field name="sts" id="5" type="timestampType" description="Stream service push timestamp in microseconds"/>
    <field name="category" id="6" type="instCategory" description="Instrument category"/>
    <field name="pseq" id="7" type="sequenceType" sinceVersion="5" description="Previous seq for increment continuity check; 0 for snapshot frames"/>
    <field name="depthAction" id="8" type="depthAction" sinceVersion="5" description="Snapshot or incremental update indicator"/>
    <!-- Reserved IDs: 9-100 for future fields -->
    <field name="padding" id="100" type="padding4" description="Padding for 8-byte alignment"/>

    <group name="asks" id="200" dimensionType="groupSize16Encoding">
      <field name="price" id="1" type="priceType"/>
      <field name="size" id="2" type="sizeType"/>
    </group>

    <group name="bids" id="201" dimensionType="groupSize16Encoding">
      <field name="price" id="1" type="priceType"/>
      <field name="size" id="2" type="sizeType"/>
    </group>

    <data name="symbol" id="300" type="varString8"/>
  </sbe:message>

  <!-- BBO message (best bid and ask) -->
  <sbe:message name="BestBidAsk" id="1002" description="Best bid and ask">
    <field name="ts" id="1" type="timestampType"/>
    <field name="bid1Price" id="2" type="priceType"/>
    <field name="bid1Size" id="3" type="sizeType"/>
    <field name="ask1Price" id="4" type="priceType"/>
    <field name="ask1Size" id="5" type="sizeType"/>
    <field name="priceExponent" id="6" type="exponentType"/>
    <field name="sizeExponent" id="7" type="exponentType"/>
    <field name="seq" id="8" type="sequenceType"/>
    <field name="sts" id="9" type="timestampType" description="Stream service push timestamp in microseconds"/>
    <field name="category" id="10" type="instCategory" description="Instrument category"/>
    <!-- Reserved IDs: 11-100 for future fields -->
    <field name="padding" id="100" type="padding5" description="Padding for 8-byte alignment"/>

    <data name="symbol" id="200" type="varString8"/>
  </sbe:message>

  <!-- Trade message -->
  <sbe:message name="Trade" id="1003" description="Public trade">
    <field name="priceExponent" id="1" type="exponentType"/>
    <field name="sizeExponent" id="2" type="exponentType"/>
    <field name="sts" id="3" type="timestampType" description="Stream service push timestamp in microseconds"/>
    <field name="category" id="4" type="instCategory" description="Instrument category"/>
    <!-- Reserved IDs: 5-100 for future fields -->
    <field name="padding" id="100" type="padding5" description="Padding for 8-byte alignment of root block"/>

    <group id="200" name="trades" dimensionType="groupSize16Encoding">
      <field name="ts" id="1" type="timestampType"/>
      <field name="execId" id="2" type="sequenceType"/>
      <field name="price" id="3" type="priceType"/>
      <field name="size" id="4" type="sizeType"/>
      <field name="side" id="5" type="tradeSide"/>
      <field name="isRPI" id="6" type="BooleanType" sinceVersion="4" description="Retail Price Improvement flag"/>
      <!-- Reserved IDs: 7-50 for future fields -->
      <field name="padding" id="50" type="padding6" description="Padding for 8-byte alignment of group entry"/>
    </group>

    <data name="symbol" id="300" type="varString8"/>
  </sbe:message>
</sbe:messageSchema>
```

---

# SBE 基本信息

**核心功能**

- 二进制传输：行情数据不再以文本形式发送，而是采用符合 FIX SBE 标准的二进制字节流
- Schema 驱动：提供 XML Schema 文件，定义字段偏移量和长度
- 报文机制：在建立连接后，系统采用差异化的报文封装机制。订阅阶段的交互完全基于 JSON 文本帧进行；一旦进入行情推送阶段，数据将切换至
  SBE 编码的二进制帧。您可通过识别底层 WebSocket 帧的操作码opCode来分流处理逻辑

---

**版本更新与兼容性说明**

- 常规升级：增加新字段时，Schema ID 保持一致，仅提升 Version 号，现有逻辑保持向下兼容
- 接入要求：需确保解析器能够识别消息头中的 Schema ID 和 Version，以便在过渡期内同时处理不同版本的二进制流

---
**频道范围**

| 频道名称            | 字段                 | 更新频率 |
|:----------------|:-------------------|:-----|
| 有限档深度 Depth50   | 价格、数量、订单方向         | 20ms |
| 最优推送 BestBidAsk | 最优买/卖价及挂单量         | 实时   |
| 平台成交 Trade      | 成交价格、成交数量、成交方向、时间戳 | 实时   |

---
**公共消息头**

所有 SBE 消息必须包含固定 8 字节的头部，以便解析识别后续数据

| 字段名         | 类型(Type) | 长度(Byte) | 说明                                                                     |
|:------------|:---------|:---------|:-----------------------------------------------------------------------|
| blockLength | uint16   | 2        | Root 块长度                                                               |
| templateId  | uint16   | 2        | 频道唯一标识：<br/>**1001**：50档深度频道<br/>**1002**：BBO 频道<br/>**1003**：公共成交流水频道 |
| schemaId    | uint16   | 2        | Schema ID                                                              |
| version     | uint16   | 2        | Schema 版本                                                              |

---

### SBE XML Template

```xml
<?xml version="1.0" encoding="UTF-8"?>
<sbe:messageSchema xmlns:sbe="http://fixprotocol.io/2016/sbe"
                   package="com.upex.stream.sbe"
                   id="1"
                   version="5"
                   semanticVersion="1.0.0"
                   description="UPEX Market Data SBE Schema"
                   byteOrder="littleEndian">

  <types>
    <!-- 消息头 -->
    <composite name="messageHeader" description="Standard SBE Message Header">
      <type name="blockLength" primitiveType="uint16" description="Root block length"/>
      <type name="templateId" primitiveType="uint16" description="Template ID"/>
      <type name="schemaId" primitiveType="uint16" description="Schema ID"/>
      <type name="version" primitiveType="uint16" description="Schema version"/>
    </composite>

    <!-- 分组大小编码 -->
    <composite name="groupSize16Encoding" description="Group size encoding">
      <type name="blockLength" primitiveType="uint16"/>
      <type name="numInGroup" primitiveType="uint16"/>
    </composite>

    <composite name="varString8" description="Variable length UTF-8 string.">
      <type name="length" primitiveType="uint8"/>
      <type name="varData" length="0" primitiveType="uint8" characterEncoding="UTF-8"/>
    </composite>

    <!-- 基础类型定义 -->
    <type name="timestampType" primitiveType="uint64" description="Timestamp in microseconds"/>
    <type name="priceType" primitiveType="int64" description="Price mantissa"/>
    <type name="sizeType" primitiveType="int64" description="Size mantissa"/>
    <type name="sequenceType" primitiveType="uint64" description="Sequence number"/>
    <type name="symbolType" primitiveType="char" length="24" description="Trading pair symbol"/>
    <type name="exponentType" primitiveType="int8" description="Price/Size exponent"/>

    <!-- Padding 类型库：支持 0-7 字节的所有对齐场景 -->
    <type name="padding0" primitiveType="uint8" length="0" description="No padding needed"/>
    <type name="padding1" primitiveType="uint8" length="1" description="1 byte padding for alignment"/>
    <type name="padding2" primitiveType="uint8" length="2" description="2 bytes padding for alignment"/>
    <type name="padding3" primitiveType="uint8" length="3" description="3 bytes padding for alignment"/>
    <type name="padding4" primitiveType="uint8" length="4" description="4 bytes padding for alignment"/>
    <type name="padding5" primitiveType="uint8" length="5" description="5 bytes padding for alignment"/>
    <type name="padding6" primitiveType="uint8" length="6" description="6 bytes padding for alignment"/>
    <type name="padding7" primitiveType="uint8" length="7" description="7 bytes padding for alignment"/>

    <!-- 枚举类型定义 -->
    <enum name="tradeSide" encodingType="uint8" description="Trade side">
      <validValue name="Buy" description="Buy side">0</validValue>
      <validValue name="Sell" description="Sell side">1</validValue>
    </enum>

    <!-- 业务线枚举：instType 字符串 → uint8 映射 -->
    <enum name="instCategory" encodingType="uint8" description="Instrument category (business line)">
      <validValue name="Spot" description="Spot trading">0</validValue>
      <validValue name="UsdtFutures" description="USDT-margined futures">1</validValue>
      <validValue name="CoinFutures" description="Coin-margined futures">2</validValue>
      <validValue name="UsdcFutures" description="USDC-margined futures">3</validValue>
    </enum>

    <!-- 布尔标志枚举 -->
    <enum name="BooleanType" encodingType="uint8" description="Boolean flag">
      <validValue name="F" description="False">0</validValue>
      <validValue name="T" description="True">1</validValue>
    </enum>

    <!-- 深度推送动作枚举 -->
    <enum name="depthAction" encodingType="uint8" description="Depth push action: full snapshot or incremental update">
      <validValue name="Snapshot" description="Full snapshot of all levels">0</validValue>
      <validValue name="Update" description="Incremental update, only changed levels included">1</validValue>
    </enum>
  </types>

  <!-- 50档深度消息 -->
  <sbe:message name="Depth50" id="1001" description="50-level depth snapshot">
    <field name="ts" id="1" type="timestampType"/>
    <field name="seq" id="2" type="sequenceType"/>
    <field name="priceExponent" id="3" type="exponentType"/>
    <field name="sizeExponent" id="4" type="exponentType"/>
    <field name="sts" id="5" type="timestampType" description="Stream service push timestamp in microseconds"/>
    <field name="category" id="6" type="instCategory" description="Instrument category"/>
    <field name="pseq" id="7" type="sequenceType" sinceVersion="5" description="Previous seq for increment continuity check; 0 for snapshot frames"/>
    <field name="depthAction" id="8" type="depthAction" sinceVersion="5" description="Snapshot or incremental update indicator"/>
    <!-- Reserved IDs: 9-100 for future fields -->
    <field name="padding" id="100" type="padding4" description="Padding for 8-byte alignment"/>

    <group name="asks" id="200" dimensionType="groupSize16Encoding">
      <field name="price" id="1" type="priceType"/>
      <field name="size" id="2" type="sizeType"/>
    </group>

    <group name="bids" id="201" dimensionType="groupSize16Encoding">
      <field name="price" id="1" type="priceType"/>
      <field name="size" id="2" type="sizeType"/>
    </group>

    <data name="symbol" id="300" type="varString8"/>
  </sbe:message>

  <!-- BBO消息（最优买卖价） -->
  <sbe:message name="BestBidAsk" id="1002" description="Best bid and ask">
    <field name="ts" id="1" type="timestampType"/>
    <field name="bid1Price" id="2" type="priceType"/>
    <field name="bid1Size" id="3" type="sizeType"/>
    <field name="ask1Price" id="4" type="priceType"/>
    <field name="ask1Size" id="5" type="sizeType"/>
    <field name="priceExponent" id="6" type="exponentType"/>
    <field name="sizeExponent" id="7" type="exponentType"/>
    <field name="seq" id="8" type="sequenceType"/>
    <field name="sts" id="9" type="timestampType" description="Stream service push timestamp in microseconds"/>
    <field name="category" id="10" type="instCategory" description="Instrument category"/>
    <!-- Reserved IDs: 11-100 for future fields -->
    <field name="padding" id="100" type="padding5" description="Padding for 8-byte alignment"/>

    <data name="symbol" id="200" type="varString8"/>
  </sbe:message>

  <!-- 成交消息 -->
  <sbe:message name="Trade" id="1003" description="Public trade">
    <field name="priceExponent" id="1" type="exponentType"/>
    <field name="sizeExponent" id="2" type="exponentType"/>
    <field name="sts" id="3" type="timestampType" description="Stream service push timestamp in microseconds"/>
    <field name="category" id="4" type="instCategory" description="Instrument category"/>
    <!-- Reserved IDs: 5-100 for future fields -->
    <field name="padding" id="100" type="padding5" description="Padding for 8-byte alignment of root block"/>

    <group id="200" name="trades" dimensionType="groupSize16Encoding">
      <field name="ts" id="1" type="timestampType"/>
      <field name="execId" id="2" type="sequenceType"/>
      <field name="price" id="3" type="priceType"/>
      <field name="size" id="4" type="sizeType"/>
      <field name="side" id="5" type="tradeSide"/>
      <field name="isRPI" id="6" type="BooleanType" sinceVersion="4" description="Retail Price Improvement flag"/>
      <!-- Reserved IDs: 7-50 for future fields -->
      <field name="padding" id="50" type="padding6" description="Padding for 8-byte alignment of group entry"/>
    </group>

    <data name="symbol" id="300" type="varString8"/>
  </sbe:message>
</sbe:messageSchema>
```