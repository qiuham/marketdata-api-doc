---
exchange: binance
source_url: https://developers.binance.com/en/docs/sdks-tools/connectors/rust
api_type: Guide
updated_at: 2026-11-20 18:28:42.676173
---

# Rust

The official Rust connector for Binance APIs, designed for backend applications and services written
in Rust.

The connector is published as a single crate (`binance-sdk`). You enable the Binance products you
need using Cargo features (for example `spot`). It supports REST APIs, WebSocket APIs and WebSocket
Streams, and provides built-in request signing, connection management, and strongly typed request
and response models.

For source code, issues, and release notes, see the
[binance-connector-rust](https://github.com/binance/binance-connector-rust) repository on GitHub.

## Supported environments

- Rust 1.86 or newer (stable toolchain)
- Backend Rust applications and services

> This connector is intended for server-side usage only.

## Package structure

The Rust connector is published as a single crate with product modules behind feature flags.

Enable the products you want in `Cargo.toml` (for example `spot`,
`derivatives_trading_usds_futures`, `wallet` etc.), then import the corresponding module in your
code. This keeps dependencies minimal and avoids pulling in APIs you don’t use.

## Typical use cases

- Low-latency trading and execution services
- High-throughput market data ingestion
- Backend services managing accounts, balances, and orders
- Applications consuming WebSocket APIs or WebSocket Streams for real-time updates

## Key features

- Support for Binance REST APIs, WebSocket APIs and WebSocket Streams
- Built-in request signing for authenticated endpoints
- WebSocket connection handling with automatic reconnection and session renewal
- Strongly typed request and response models
- Support for both production and testnet environments
- Memory-safe and performant Rust API design

## Getting started

Enable the product feature you want under `binance-sdk`:

```toml
[dependencies]
binance-sdk = { version = "<VERSION>", features = ["spot"] }
```

Create a client and send a request:

```rust
use anyhow::{Context, Result};
use std::env;

use binance_sdk::config::{ConfigurationRestApi, PrivateKey};
use binance_sdk::spot::{SpotRestApi, rest_api::GetAccountParams};

#[tokio::main]
async fn main() -> Result<()> {
    let api_key = env::var("BINANCE_API_KEY").context("BINANCE_API_KEY must be set")?;
    let private_key = env::var("BINANCE_PRIVATE_KEY").context("BINANCE_PRIVATE_KEY must be set")?;
    let configuration = ConfigurationRestApi::builder()
        .api_key(api_key)
        .private_key(PrivateKey::File(private_key))
        .build()?;

    let spot_client = SpotRestApi::production(configuration);

    let params = GetAccountParams::default();
    let account_info = spot_client
        .get_account(params)
        .await
        .context("get_account request failed")?;

    Ok(())
}
```

The example above uses asymmetric key authentication. HMAC-based authentication using an API secret
is also supported.

Refer to the crate documentation for product-specific REST, WebSocket API and WebSocket Streams
examples.

## Notes and best practices

- Store API keys securely using environment variables or a secrets manager
- Prefer WebSocket APIs or Streams for real-time data instead of polling REST endpoints
- Monitor rate limits and endpoint weights when building high-throughput services
- Use testnet environments when developing and validating integrations

---

# Rust

Binance API 官方 Rust 连接器，专为使用 Rust 编写的后端应用程序和服务而设计。

该连接器以单一 crate（`binance-sdk`）的形式发布。您可以通过 Cargo features（例如
`spot`）启用所需的 Binance 产品。它支持 REST API、WebSocket
API 和 WebSocket 数据流，并提供内置的请求签名、连接管理以及强类型的请求与响应模型。

如需查看源代码、问题反馈及版本说明，请访问 GitHub 上的
[binance-connector-rust](https://github.com/binance/binance-connector-rust) 仓库。

## 支持的环境

- Rust 1.86 或更高版本（stable 工具链）
- 后端 Rust 应用程序及服务

> 本连接器仅适用于服务端使用。

## 包结构

Rust 连接器以单一 crate 的形式发布，各产品模块通过 feature flags 按需启用。

在 `Cargo.toml` 中启用所需的产品（例如 `spot`、`derivatives_trading_usds_futures`、`wallet`
等），然后在代码中导入对应模块。这种方式将依赖项保持在最低限度，避免引入不需要的 API。

## 典型使用场景

- 低延迟交易与执行服务
- 高吞吐量行情数据采集
- 管理账户、余额和订单的后端服务
- 通过 WebSocket API 或 WebSocket 数据流获取实时更新的应用程序

## 主要特性

- 支持 Binance REST API、WebSocket API 和 WebSocket 数据流
- 内置针对需要身份验证接口的请求签名
- WebSocket 连接管理，支持自动重连和会话续期
- 强类型的请求与响应模型
- 同时支持正式环境和测试网环境
- 内存安全且高性能的 Rust API 设计

## 快速开始

在 `binance-sdk` 下启用所需的产品 feature：

```toml
[dependencies]
binance-sdk = { version = "<VERSION>", features = ["spot"] }
```

创建客户端并发送请求：

```rust
use anyhow::{Context, Result};
use std::env;

use binance_sdk::config::{ConfigurationRestApi, PrivateKey};
use binance_sdk::spot::{SpotRestApi, rest_api::GetAccountParams};

#[tokio::main]
async fn main() -> Result<()> {
    let api_key = env::var("BINANCE_API_KEY").context("BINANCE_API_KEY must be set")?;
    let private_key = env::var("BINANCE_PRIVATE_KEY").context("BINANCE_PRIVATE_KEY must be set")?;
    let configuration = ConfigurationRestApi::builder()
        .api_key(api_key)
        .private_key(PrivateKey::File(private_key))
        .build()?;

    let spot_client = SpotRestApi::production(configuration);

    let params = GetAccountParams::default();
    let account_info = spot_client
        .get_account(params)
        .await
        .context("get_account request failed")?;

    Ok(())
}
```

上述示例使用非对称密钥进行身份验证。同样支持基于 API Secret 的 HMAC 身份验证方式。

如需各产品的 REST、WebSocket API 和 WebSocket 数据流示例，请参阅 crate 文档。

## 注意事项与最佳实践

- 使用环境变量或密钥管理工具安全存储 API 密钥
- 获取实时数据时，优先使用 WebSocket API 或数据流，而非轮询 REST 接口
- 构建高吞吐量服务时，注意监控频率限制和接口权重
- 开发和验证集成方案时，请使用测试网环境