---
exchange: binance
source_url: https://developers.binance.com/en/docs/sdks-tools/connectors/go
api_type: Guide
updated_at: 2026-11-18 01:52:03.561539
---

# Go

The official Go connector for Binance APIs, designed for backend applications and services written
in Go.

The connector provides a modular and idiomatic Go interface to Binance APIs, supporting REST APIs,
WebSocket APIs and WebSocket Streams. It includes built-in request signing, connection management,
and strongly typed request and response structures for building reliable and maintainable
integrations.

For source code, issues, and release notes, see the
[binance-connector-go](https://github.com/binance/binance-connector-go) repository on GitHub.

## Supported environments

- Go 1.24 or newer
- Backend Go applications and services

> This connector is intended for server-side usage only. Browser-based or WebAssembly environments
> are not supported.

## Package structure

The Go connector is published as a single module that exposes clients for different Binance
products.

Product-specific functionality is organized into dedicated packages within the repository, such as
`spot`, `derivativestradingusdsfutures`, `wallet`, and others. This structure keeps APIs clearly
separated while allowing you to share configuration, authentication, and transport logic across
clients.

## Typical use cases

- Trading and execution services
- Real-time and historical market data ingestion
- Backend services managing accounts, balances, and orders
- Applications consuming WebSocket APIs or WebSocket Streams for low-latency updates

## Key features

- Support for Binance REST APIs, WebSocket APIs and WebSocket Streams
- Built-in request signing for authenticated endpoints
- WebSocket connection handling with automatic reconnection and session renewal
- Strongly typed request and response structures
- Support for both production and testnet environments
- Idiomatic Go API design

## Getting started

Install the package for the product you want to integrate with:

```bash
go get github.com/binance/binance-connector-go/clients/spot
```

Create a client and send a request:

```go
package main

import (
 "context"
 "os"

 spotClient "github.com/binance/binance-connector-go/clients/spot"
 "github.com/binance/binance-connector-go/common/common"
)

func main() {
 config := common.NewConfigurationRestAPI(
  common.WithApiKey(os.Getenv("BINANCE_API_KEY")),
  common.WithPrivateKey(os.Getenv("BINANCE_PRIVATE_KEY")),
 )

 client := spotClient.NewBinanceSpotClient(
  spotClient.WithRestAPI(config),
 )

 accountInfo, err := client
    .RestApi
    .AccountAPI
    .GetAccount(context.Background())
    .Execute()
}
```

The example above uses asymmetric key authentication. HMAC-based authentication using an API secret
is also supported.

Refer to the repository documentation for product-specific REST, WebSocket API and WebSocket Streams
examples.

## Notes and best practices

- Store API keys securely using environment variables or a secrets manager
- Prefer WebSocket APIs or Streams for real-time data instead of polling REST endpoints
- Monitor rate limits and endpoint weights when building high-throughput services
- Use testnet environments when developing and validating integrations

---

# Go

Binance API 官方 Go 连接器，专为使用 Go 编写的后端应用程序和服务而设计。

该连接器为 Binance API 提供模块化且符合 Go 惯例的接口，支持 REST API、WebSocket
API 和 WebSocket 数据流。内置请求签名、连接管理以及强类型的请求与响应结构，助您构建可靠且易于维护的集成方案。

如需查看源代码、问题反馈及版本说明，请访问 GitHub 上的
[binance-connector-go](https://github.com/binance/binance-connector-go) 仓库。

## 支持的环境

- Go 1.24 或更高版本
- 后端 Go 应用程序及服务

> 本连接器仅适用于服务端使用。不支持基于浏览器或 WebAssembly 的环境。

## 包结构

Go 连接器以单一模块的形式发布，对外提供不同 Binance 产品的客户端接口。

各产品的功能按专属包进行组织，例如 `spot`、`derivativestradingusdsfutures`、`wallet`
等。这种结构使各 API 保持清晰分离，同时允许您在多个客户端之间共享配置、身份验证和传输逻辑。

## 典型使用场景

- 交易与执行服务
- 实时及历史行情数据采集
- 管理账户、余额和订单的后端服务
- 通过 WebSocket API 或 WebSocket 数据流获取低延迟更新的应用程序

## 主要特性

- 支持 Binance REST API、WebSocket API 和 WebSocket 数据流
- 内置针对需要身份验证接口的请求签名
- WebSocket 连接管理，支持自动重连和会话续期
- 强类型的请求与响应结构
- 同时支持正式环境和测试网环境
- 符合 Go 惯例的 API 设计

## 快速开始

安装您需要集成的产品对应的包：

```bash
go get github.com/binance/binance-connector-go/clients/spot
```

创建客户端并发送请求：

```go
package main

import (
 "context"
 "os"

 spotClient "github.com/binance/binance-connector-go/clients/spot"
 "github.com/binance/binance-connector-go/common/common"
)

func main() {
 config := common.NewConfigurationRestAPI(
  common.WithApiKey(os.Getenv("BINANCE_API_KEY")),
  common.WithPrivateKey(os.Getenv("BINANCE_PRIVATE_KEY")),
 )

 client := spotClient.NewBinanceSpotClient(
  spotClient.WithRestAPI(config),
 )

 accountInfo, err := client
    .RestApi
    .AccountAPI
    .GetAccount(context.Background())
    .Execute()
}
```

上述示例使用非对称密钥进行身份验证。同样支持基于 API Secret 的 HMAC 身份验证方式。

如需各产品的 REST、WebSocket API 和 WebSocket 数据流示例，请参阅仓库文档。

## 注意事项与最佳实践

- 使用环境变量或密钥管理工具安全存储 API 密钥
- 获取实时数据时，优先使用 WebSocket API 或数据流，而非轮询 REST 接口
- 构建高吞吐量服务时，注意监控频率限制和接口权重
- 开发和验证集成方案时，请使用测试网环境