---
exchange: binance
source_url: https://developers.binance.com/en/docs/sdks-tools/connectors/dotnet
api_type: Guide
updated_at: 2026-11-23 18:27:40.654949
---

# .NET

The .NET connector for Binance APIs provides a client for interacting with a subset of Binance REST
APIs, WebSocket APIs, and WebSocket streams from .NET applications.

This connector is considered **legacy** and is **not actively maintained**. It supports a limited
set of Binance products and endpoints compared to newer SDKs available in other languages.

For source code, issues, and release notes, see the
[binance-connector-dotnet](https://github.com/binance/binance-connector-dotnet) repository on
GitHub.

## Status

> ⚠️ **Maintenance status**
>
> The .NET connector is currently **not actively maintained**. It supports only a subset of Binance
> products and APIs, and may not include newer endpoints or features.
>
> For full product coverage and ongoing updates, we recommend using one of the actively maintained
> SDKs such as JavaScript, Python, Go, Java, PHP or Rust.

## Supported environments

- .NET 6.0 or newer
- Backend .NET applications and services

> This connector is intended for server-side usage only.

## Package structure

The .NET connector is distributed as one or more `NuGet` packages.

It exposes client interfaces for supported REST APIs, WebSocket streams, and WebSocket APIs. Product
coverage is limited and may vary depending on the API.

## Typical use cases

- Backend services interacting with Binance REST APIs
- Applications consuming WebSocket streams for real-time data
- Applications using WebSocket APIs for request–response communication
- Existing .NET systems requiring Binance integrations

## Key features

- Support for a subset of Binance products and endpoints
- HMAC and RSA-based request signing
- Integration with the .NET logging ecosystem

## Getting started

Install the connector using NuGet:

```bash
dotnet add package Binance.Spot
```

Create a client and send a request:

```csharp
using System;
using System.Threading.Tasks;
using Binance.Spot;

class Program
{
    static async Task Main(string[] args)
    {
        var market = new Market();
        var serverTime = await market.CheckServerTime();
        Console.WriteLine(serverTime);
    }
}
```

Refer to the repository documentation and the examples folder for additional REST, WebSocket API,
and WebSocket Stream usage examples.

## Notes and best practices

- This connector supports REST APIs, WebSocket APIs, and WebSocket streams
- Product and endpoint coverage is limited and may not reflect the latest Binance APIs
- Monitor rate limits carefully, as older clients may not expose detailed weight information
- For production systems or full API coverage, use an actively maintained SDK

---

# .NET

Binance API 的 .NET 连接器为 .NET 应用程序提供了一个客户端，用于与 Binance REST API、WebSocket
API 和 WebSocket 数据流的部分功能进行交互。

该连接器被视为**历史遗留版本**，**未处于积极维护状态**。与其他语言的新版 SDK 相比，它仅支持有限的 Binance 产品和接口。

如需查看源代码、问题反馈及版本说明，请访问 GitHub 上的
[binance-connector-dotnet](https://github.com/binance/binance-connector-dotnet) 仓库。

## 状态

> ⚠️ **维护状态**
>
> .NET 连接器目前**未处于积极维护状态**。它仅支持部分 Binance 产品和 API，可能不包含较新的接口或功能。
>
> 如需完整的产品支持和持续更新，我们建议使用以下积极维护中的 SDK：JavaScript、Python、Go、Java、PHP 或 Rust。

## 支持的环境

- .NET 6.0 或更高版本
- 后端 .NET 应用程序及服务

> 本连接器仅适用于服务端使用。

## 包结构

.NET 连接器以一个或多个 `NuGet` 包的形式分发。

它为所支持的 REST API、WebSocket 数据流和 WebSocket
API 提供客户端接口。产品覆盖范围有限，具体情况可能因 API 而异。

## 典型使用场景

- 与 Binance REST API 交互的后端服务
- 消费 WebSocket 数据流以获取实时数据的应用程序
- 使用 WebSocket API 进行请求-响应通信的应用程序
- 需要集成 Binance 功能的现有 .NET 系统

## 主要特性

- 支持部分 Binance 产品和接口
- 基于 HMAC 和 RSA 的请求签名
- 与 .NET 日志生态系统集成

## 快速开始

使用 NuGet 安装连接器：

```bash
dotnet add package Binance.Spot
```

创建客户端并发送请求：

```csharp
using System;
using System.Threading.Tasks;
using Binance.Spot;

class Program
{
    static async Task Main(string[] args)
    {
        var market = new Market();
        var serverTime = await market.CheckServerTime();
        Console.WriteLine(serverTime);
    }
}
```

如需更多 REST、WebSocket API 和 WebSocket 数据流的使用示例，请参阅仓库文档及 examples 文件夹。

## 注意事项与最佳实践

- 本连接器支持 REST API、WebSocket API 和 WebSocket 数据流
- 产品和接口覆盖范围有限，可能未反映最新的 Binance API
- 请注意监控频率限制，旧版客户端可能不会提供详细的权重信息
- 如需用于生产环境或完整的 API 覆盖，请使用积极维护中的 SDK