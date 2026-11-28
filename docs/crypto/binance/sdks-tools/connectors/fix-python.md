---
exchange: binance
source_url: https://developers.binance.com/en/docs/sdks-tools/connectors/fix-python
api_type: FIX
updated_at: 2026-11-28 18:27:10.308126
---

# FIX (Python)

The Python FIX connector provides access to Binance Financial Information eXchange (FIX) APIs using
the FIX protocol.

This connector is intended for **advanced and institutional use cases** that require low-latency
order entry, execution, and session-based trading workflows. It exposes Binance Spot FIX message
types and session flows and allows you to place orders, cancel orders, and track order status using
FIX messages.

For source code, issues, and release notes, see the
[binance-fix-connector-python](https://github.com/binance/binance-fix-connector-python) repository
on GitHub.

## Supported environments

- Python 3.9 or newer
- Backend services and trading systems

> This connector is intended for server-side usage only and requires a persistent FIX session.

## Scope and capabilities

The FIX Python connector supports:

- Binance Spot FIX Order Entry
- Order placement and cancellation
- Execution reports and order state updates
- Session-based FIX communication

This connector **does not** replace REST or WebSocket APIs and is designed for specialized trading
workflows.

## Authentication

> ⚠️ **Important**
>
> Binance FIX APIs **only support Ed25519 keys**. Other authentication methods (such as HMAC or RSA)
> are not supported.

Before using the FIX connector, ensure that:

- You have generated an `Ed25519` key pair
- Your API key has FIX permissions enabled
- You are using the correct FIX endpoint for production or testnet

Refer to the following guides:

- [How to generate an Ed25519 key pair (mainnet)](https://www.binance.com/en/support/faq/how-to-generate-an-ed25519-key-pair-to-send-api-requests-on-binance-6b9a63f1e3384cf48a2eedb82767a69a)
- [Binance Spot FIX API documentation](/products/spot/fix-api)

## Installation

Install the connector using `pip`:

```bash
pip install binance-fix-connector
```

> The package is published on PyPI as `binance-fix-connector`. Source code is maintained in the
> GitHub repository linked above.

## Getting started

All FIX messages are created and managed through the `create_order_entry_session` helper, which
establishes a FIX session and exposes utilities to create and send messages.

The example below demonstrates how to establish a FIX Order Entry session and submit a simple limit
order.

```python
import time
from binance_fix_connector.fix_connector import create_order_entry_session
from binance_fix_connector.utils import get_private_key

API_KEY = "<your-api-key>"
PRIVATE_KEY = get_private_key("/path/to/private.key")

FIX_OE_URL = "tcp+tls://fix-oe.testnet.binance.vision:9000"

client = create_order_entry_session(
    api_key=API_KEY,
    private_key=PRIVATE_KEY,
    endpoint=FIX_OE_URL,
)

# Wait for logon
client.retrieve_messages_until(message_type="A")

# Create and send a NewOrderSingle (D)
msg = client.create_fix_message_with_basic_header("D")
msg.append_pair(11, str(time.time_ns()))  # ClOrdID
msg.append_pair(55, "BNBUSDT")            # Symbol
msg.append_pair(54, 1)                    # Side (BUY)
msg.append_pair(38, 1)                    # OrderQty
msg.append_pair(40, 2)                    # OrdType (LIMIT)
msg.append_pair(44, 730)                  # Price
msg.append_pair(59, 1)                    # TimeInForce (GTC)

client.send_message(msg)

# Receive execution reports
responses = client.retrieve_messages_until(message_type="8")
```

Refer to the repository documentation for more examples.

## Typical use cases

- Low-latency order entry and execution
- Institutional or professional trading systems
- FIX-based integrations requiring session control
- Advanced trading infrastructure where REST or WebSocket APIs are not sufficient

## Notes and best practices

- FIX APIs require a persistent TCP/TLS connection
- Always handle session lifecycle events (logon, heartbeat, logout)
- Use testnet endpoints for development and validation
- Consider implementing reconnect/backoff logic and monitoring session health
- This connector is intended for experienced FIX users
- For general-purpose integrations, prefer REST or WebSocket APIs

---

# FIX (Python)

Python FIX 连接器使用 FIX 协议提供对 Binance 金融信息交换（FIX）API 的访问。

本连接器适用于**高级和机构级使用场景**，这些场景需要低延迟的订单报送、成交执行以及基于会话的交易工作流。它提供 Binance 现货 FIX 消息类型和会话流程，支持通过 FIX 消息进行下单、撤单以及跟踪订单状态。

如需查看源代码、问题反馈及版本说明，请访问 GitHub 上的
[binance-fix-connector-python](https://github.com/binance/binance-fix-connector-python) 仓库。

## 支持的环境

- Python 3.9 或更高版本
- 后端服务及交易系统

> 本连接器仅适用于服务端使用，且需要维持持久的 FIX 会话。

## 范围与功能

Python FIX 连接器支持以下功能：

- Binance 现货 FIX 订单报送
- 下单与撤单
- 成交回报及订单状态更新
- 基于会话的 FIX 通信

本连接器**不**替代 REST 或 WebSocket API，专为特定交易工作流设计。

## 身份验证

> ⚠️ **重要提示**
>
> Binance FIX API **仅支持 Ed25519 密钥**。其他身份验证方式（如 HMAC 或 RSA）不受支持。

在使用 FIX 连接器之前，请确保：

- 已生成 `Ed25519` 密钥对
- API 密钥已开启 FIX 权限
- 使用正确的 FIX 端点（正式环境或测试网）

请参阅以下指南：

- [如何生成 Ed25519 密钥对（主网）](https://www.binance.com/en/support/faq/how-to-generate-an-ed25519-key-pair-to-send-api-requests-on-binance-6b9a63f1e3384cf48a2eedb82767a69a)
- [Binance 现货 FIX API 文档](/products/spot/fix-api)

## 安装

使用 `pip` 安装连接器：

```bash
pip install binance-fix-connector
```

> 该包在 PyPI 上以 `binance-fix-connector` 发布，源代码维护于上方链接的 GitHub 仓库中。

## 快速开始

所有 FIX 消息均通过 `create_order_entry_session`
辅助函数创建和管理，该函数用于建立 FIX 会话并提供消息创建与发送的工具方法。

以下示例演示如何建立 FIX 订单报送会话并提交一个简单的限价订单。

```python
import time
from binance_fix_connector.fix_connector import create_order_entry_session
from binance_fix_connector.utils import get_private_key

API_KEY = "<your-api-key>"
PRIVATE_KEY = get_private_key("/path/to/private.key")

FIX_OE_URL = "tcp+tls://fix-oe.testnet.binance.vision:9000"

client = create_order_entry_session(
    api_key=API_KEY,
    private_key=PRIVATE_KEY,
    endpoint=FIX_OE_URL,
)

# 等待登录确认
client.retrieve_messages_until(message_type="A")

# 创建并发送新订单报文（D）
msg = client.create_fix_message_with_basic_header("D")
msg.append_pair(11, str(time.time_ns()))  # ClOrdID 客户订单编号
msg.append_pair(55, "BNBUSDT")            # Symbol 交易对
msg.append_pair(54, 1)                    # Side 方向（买入）
msg.append_pair(38, 1)                    # OrderQty 订单数量
msg.append_pair(40, 2)                    # OrdType 订单类型（限价）
msg.append_pair(44, 730)                  # Price 价格
msg.append_pair(59, 1)                    # TimeInForce 有效方式（GTC）

client.send_message(msg)

# 接收成交回报
responses = client.retrieve_messages_until(message_type="8")
```

更多示例请参阅仓库文档。

## 典型使用场景

- 低延迟订单报送与成交执行
- 机构级或专业交易系统
- 需要会话控制的 FIX 集成
- REST 或 WebSocket API 无法满足需求的高级交易基础设施

## 注意事项与最佳实践

- FIX API 需要持久的 TCP/TLS 连接
- 务必处理好会话生命周期事件（登录、心跳、登出）
- 开发和验证阶段请使用测试网端点
- 建议实现重连/退避逻辑并监控会话健康状态
- 本连接器适用于有 FIX 经验的用户
- 通用集成场景建议优先使用 REST 或 WebSocket API