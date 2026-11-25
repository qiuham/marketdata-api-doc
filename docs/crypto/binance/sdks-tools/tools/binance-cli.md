---
exchange: binance
source_url: https://developers.binance.com/en/docs/sdks-tools/tools/binance-cli
api_type: Guide
updated_at: 2026-11-25 18:26:58.290705
---

# Binance CLI

The Binance CLI is a command-line tool for interacting with Binance APIs directly from your
terminal.

It provides access to a subset of Binance REST APIs and WebSocket streams across multiple markets,
making it useful for quick inspections, scripting, and lightweight operational tasks.

For source code, issues, and updates, see the [binance-cli](https://github.com/binance/binance-cli)
repository on GitHub.

## Status

> ⚠️ **Maintenance status**
>
> The Binance CLI is **not actively maintained**, but it is **updated periodically**. It may not
> include the latest endpoints, products, or features.
>
> For long-term integrations or production systems, we recommend using one of the official SDKs
> (JavaScript, Python, Go, Java, PHP or Rust).

## Supported environments

- Node.js (installed globally)
- Unix-like environments (Linux, macOS)

> This tool is intended for local or server-side usage via a terminal.

## Scope and capabilities

The Binance CLI supports:

- REST API interactions for multiple Binance markets
- WebSocket streams for real-time market data
- Order placement and account queries via CLI commands
- Spot, USDⓈ-M Futures, and COIN-M Futures workflows (subset of APIs)

The CLI is designed for **manual usage, debugging, and scripting**, not as a replacement for
SDK-based integrations.

## Typical use cases

- Quickly querying market data from the terminal
- Inspecting exchange metadata and symbol information
- Placing or canceling orders during testing
- Listening to WebSocket streams for debugging or exploration
- Simple automation via shell scripts

## Installation

Install the CLI globally using `npm`:

```bash
git clone https://github.com/binance/binance-cli.git
cd binance-cli
npm install -g
```

Verify installation:

```bash
binance-cli --help
```

## Usage overview

The CLI exposes a large number of commands covering market data, trading, account information, and
WebSocket streams.

Examples:

```bash
# Show help
binance-cli --help

# Get server time
binance-cli time

# Get order book
binance-cli book BNBUSDT

# Place a limit buy order
binance-cli buy -s BNBUSDT -t LIMIT -q 0.05 -p 350 -f GTC

# Listen to WebSocket streams
binance-cli listen bnbusdt@depth bnbusdt@bookTicker
```

Refer to the repository README and `--help` output for the full list of supported commands.

## Notes and best practices

- This CLI supports REST APIs and WebSocket streams
- API and product coverage is limited and may lag behind current Binance APIs
- Always review commands carefully before placing live orders
- Use testnet endpoints when experimenting
- For production systems or advanced workflows, use an official SDK instead of the CLI

---

# Binance CLI

Binance CLI 是一个命令行工具，可直接从终端与 Binance API 进行交互。

它提供对多个市场部分 Binance REST
API 和 WebSocket 数据流的访问，适用于快速检查、脚本编写及轻量级运维任务。

如需查看源代码、问题反馈及更新说明，请访问 GitHub 上的
[binance-cli](https://github.com/binance/binance-cli) 仓库。

## 状态

> ⚠️ **维护状态**
>
> Binance CLI **未处于积极维护状态**，但会**定期更新**。可能不包含最新的接口、产品或功能。
>
> 对于长期集成或生产系统，我们建议使用官方 SDK（JavaScript、Python、Go、Java、PHP 或 Rust）。

## 支持的环境

- Node.js（全局安装）
- 类 Unix 环境（Linux、macOS）

> 本工具适用于通过终端进行本地或服务端使用。

## 范围与功能

Binance CLI 支持以下功能：

- 多个 Binance 市场的 REST API 交互
- 用于获取实时行情数据的 WebSocket 数据流
- 通过 CLI 命令进行下单和账户查询
- 现货、USDⓈ-M 合约和 COIN-M 合约工作流（部分 API）

CLI 专为**手动操作、调试和脚本编写**而设计，不作为基于 SDK 集成方案的替代品。

## 典型使用场景

- 从终端快速查询行情数据
- 检查交易所元数据和交易对信息
- 在测试期间下单或撤单
- 监听 WebSocket 数据流以进行调试或探索
- 通过 Shell 脚本实现简单自动化

## 安装

使用 `npm` 全局安装 CLI：

```bash
git clone https://github.com/binance/binance-cli.git
cd binance-cli
npm install -g
```

验证安装：

```bash
binance-cli --help
```

## 使用概览

CLI 提供大量命令，涵盖行情数据、交易、账户信息和 WebSocket 数据流。

示例：

```bash
# 显示帮助信息
binance-cli --help

# 获取服务器时间
binance-cli time

# 获取订单簿
binance-cli book BNBUSDT

# 下一个限价买单
binance-cli buy -s BNBUSDT -t LIMIT -q 0.05 -p 350 -f GTC

# 监听 WebSocket 数据流
binance-cli listen bnbusdt@depth bnbusdt@bookTicker
```

完整的支持命令列表请参阅仓库 README 及 `--help` 输出。

## 注意事项与最佳实践

- 本 CLI 支持 REST API 和 WebSocket 数据流
- API 和产品覆盖范围有限，可能落后于当前 Binance API
- 在提交真实订单前，请务必仔细核查命令
- 实验性操作请使用测试网接口
- 对于生产系统或高级工作流，请使用官方 SDK 而非 CLI