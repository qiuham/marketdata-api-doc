---
exchange: binance
source_url: https://developers.binance.com/en/docs/sdks-tools/connectors/dotnet
api_type: Guide
updated_at: 2026-11-28 18:27:11.615999
---

# .NET

The official .NET connector for Binance APIs, designed for backend applications and services written
in C# and other .NET languages.

The connector is a collection of NuGet packages, one per Binance product (for example `Binance.Spot`
or `Binance.Wallet`). Each package provides typed REST API, WebSocket API and WebSocket Streams
clients built on the shared `Binance.Common` library, which handles configuration, request signing,
errors, logging and connection management.

For source code, issues, and release notes, see the
[binance-connector-dotnet](https://github.com/binance/binance-connector-dotnet) repository on
GitHub. The generated API reference is available at
[binance.github.io/binance-connector-dotnet](https://binance.github.io/binance-connector-dotnet/).

> **Upgrading from 4.x?** `Binance.Spot` 5.x replaces the previous HttpClient-based connector. See
> the
> [Migration Guide](https://github.com/binance/binance-connector-dotnet/blob/master/MIGRATION.md).

## Supported environments

- .NET 8 or newer (the packages target `net8.0` and `net10.0`)
- Backend .NET applications and services
- Platforms: `win-x64`, `win-x86`, `win-arm64`, `linux-x64`, `linux-arm64`, `linux-arm`,
  `linux-musl-x64`, `linux-musl-arm64`, `osx-x64` and `osx-arm64`

The platform library (`libbinance_c`) ships inside the packages. On an unsupported platform,
creating the first client throws a `BinanceLibraryException`.

> This connector is intended for server-side usage only.

## Package structure

Every product is a separate NuGet package (`Binance.<Product>`), so you install only what you need.
`Binance.Common` is pulled in automatically.

Each package has up to three modules, depending on what the product offers: `RestApi`,
`WebSocketApi` and `WebSocketStreams`. Every module has factories for its environments:
`Production`, `Testnet` and, where available, `Demo`.

Every package is versioned independently and follows [Semantic Versioning](https://semver.org). A
connector gets a new version when its API changes.

The optional `Binance.Common.DependencyInjection` package registers any client with
`Microsoft.Extensions.DependencyInjection`.

## Typical use cases

- Backend services interacting with Binance REST APIs
- Applications consuming WebSocket Streams for real-time data
- Applications using WebSocket APIs for request-response communication
- Trading, account and wallet automation in existing .NET systems

## Key features

- Support for Binance REST APIs, WebSocket APIs and WebSocket Streams
- Request signing with HMAC-SHA256, RSA or Ed25519 keys
- Automatic WebSocket connection management: reconnects with backoff, session renewal and restored
  subscriptions
- Strongly typed request and response models, with exact `decimal` values
- Asynchronous calls with `CancellationToken` support; stream events are exposed as a
  `ChannelReader<T>`
- Proxies, private CAs and certificate pinning
- A single exception hierarchy (`BinanceException`) carrying the Binance error code
- Logging through `Microsoft.Extensions.Logging`
- Trimming and Native AOT support
- One runnable example per endpoint

## Getting started

Install the package for the product you need:

```bash
dotnet add package Binance.Spot
```

Create a client and send a request:

```csharp
using Binance.Common;
using Binance.Spot.RestApi;

using var rest = SpotRestApi.Production(new RestApiConfig
{
    ApiKey = Environment.GetEnvironmentVariable("API_KEY"),
    ApiSecret = Environment.GetEnvironmentVariable("API_SECRET"),
});
var time = await rest.TimeAsync();
Console.WriteLine(time.Data()!.ServerTime);
```

Place a signed order on the Spot testnet (create testnet keys at
[testnet.binance.vision](https://testnet.binance.vision)):

```csharp
using Binance.Common;
using Binance.Spot.RestApi;

using var client = SpotRestApi.Testnet(new RestApiConfig
{
    ApiKey = Environment.GetEnvironmentVariable("API_KEY"),
    ApiSecret = Environment.GetEnvironmentVariable("API_SECRET"),
});

try
{
    var response = await client.NewOrderAsync(new()
    {
        Symbol = "BTCUSDT",
        Side = NewOrderSide.Buy,
        Type = NewOrderType.Market,
        Quantity = 0.001m,
    });
    Console.WriteLine($"Order {response.Data()!.OrderId} placed");
}
catch (BinanceException e)
{
    Console.Error.WriteLine($"{e.Kind} {e.Code}: {e.Message}");
}
```

To sign with a private key instead of an HMAC secret, set
`PrivateKeyFile = "/path/to/ed25519-private-key.pem"` (or `PrivateKeyPem`) in place of `ApiSecret`.

Subscribe to a market data stream (public, no credentials):

```csharp
using Binance.Spot.WebSocketStreams;

var client = SpotWebSocketStreams.Production();
await using var connection = await client.ConnectAsync();
using var trades = connection.AggTrade(new() { Symbol = "btcusdt" });
await foreach (var trade in trades.Events.ReadAllAsync())
    Console.WriteLine($"{trade.S} {trade.P}");
```

### Dependency injection and logging

```csharp
services.AddBinanceRestApi<SpotRestApi>(SpotRestApi.Production, o => o.ApiKey = Environment.GetEnvironmentVariable("API_KEY"));
```

`BinanceLogging.Configure(loggerFactory)` sends the (process-wide) log to `ILogger`.

### Examples

The repository has one runnable example for every endpoint, named after the operation, under
`examples/Binance.<Product>.Examples/`. For instance, run the Spot klines example with:

```bash
dotnet run --project examples/Binance.Spot.Examples -- RestApi/Market/Klines
```

Without an argument, the project lists the available examples. The example projects target
`net10.0`, so running them needs the .NET 10 SDK.

## Notes and best practices

- Store API keys securely using environment variables or a secrets manager
- Prefer WebSocket APIs or Streams for real-time data instead of polling REST endpoints
- Monitor rate limits and endpoint weights; REST responses expose the rate-limit headers
- Use testnet environments when developing and validating integrations
- Dispose clients (`using` / `await using`) to release connections

---

# .NET

Binance API 官方 .NET 连接器，专为使用 C# 及其他 .NET 语言编写的后端应用程序和服务而设计。

该连接器是一组 NuGet 包，每个 Binance 产品对应一个包（例如
`Binance.Spot`、`Binance.Wallet`）。每个包都提供强类型的 REST API、WebSocket
API 和 WebSocket 数据流客户端，并构建在共享的 `Binance.Common`
库之上，由其负责配置、请求签名、错误处理、日志和连接管理。

如需查看源代码、问题反馈及版本说明，请访问 GitHub 上的
[binance-connector-dotnet](https://github.com/binance/binance-connector-dotnet)
仓库。生成的 API 参考文档位于
[binance.github.io/binance-connector-dotnet](https://binance.github.io/binance-connector-dotnet/)。

> **从 4.x 升级？** `Binance.Spot` 5.x 取代了此前基于 HttpClient 的连接器，请参阅
> [迁移指南](https://github.com/binance/binance-connector-dotnet/blob/master/MIGRATION.md)。

## 支持的环境

- .NET 8 或更高版本（软件包目标框架为 `net8.0` 和 `net10.0`）
- 后端 .NET 应用程序及服务
- 平台：`win-x64`、`win-x86`、`win-arm64`、`linux-x64`、`linux-arm64`、`linux-arm`、`linux-musl-x64`、
  `linux-musl-arm64`、`osx-x64` 和 `osx-arm64`

平台库（`libbinance_c`）已包含在软件包中。在不受支持的平台上，创建第一个客户端时会抛出
`BinanceLibraryException`。

> 本连接器仅适用于服务端使用。

## 包结构

每个产品都是独立的 NuGet 包（`Binance.<Product>`），因此您只需安装所需的产品。`Binance.Common`
会被自动引入。

每个包根据产品提供的能力，最多包含三个模块：`RestApi`、`WebSocketApi` 和
`WebSocketStreams`。每个模块都为各环境提供工厂方法： `Production`、`Testnet`，以及（如适用）`Demo`。

每个包独立版本化，遵循[语义化版本](https://semver.org)。仅当某个连接器的 API 发生变化时，才会发布新版本。

可选的 `Binance.Common.DependencyInjection` 包可将任意客户端注册到
`Microsoft.Extensions.DependencyInjection`。

## 典型使用场景

- 与 Binance REST API 交互的后端服务
- 通过 WebSocket 数据流获取实时数据的应用程序
- 使用 WebSocket API 进行请求-响应通信的应用程序
- 现有 .NET 系统中的交易、账户和钱包自动化

## 主要特性

- 支持 Binance REST API、WebSocket API 和 WebSocket 数据流
- 支持 HMAC-SHA256、RSA 或 Ed25519 密钥的请求签名
- WebSocket 连接自动管理：带退避的自动重连、会话续期，并自动恢复订阅
- 强类型的请求与响应模型，数值使用精确的 `decimal`
- 异步调用，支持 `CancellationToken`；数据流事件以 `ChannelReader<T>` 形式提供
- 支持代理、私有 CA 和证书固定
- 统一的异常体系（`BinanceException`），携带 Binance 错误码
- 通过 `Microsoft.Extensions.Logging` 输出日志
- 支持裁剪（trimming）和 Native AOT
- 每个接口均提供可运行的示例

## 快速开始

安装所需产品对应的包：

```bash
dotnet add package Binance.Spot
```

创建客户端并发送请求：

```csharp
using Binance.Common;
using Binance.Spot.RestApi;

using var rest = SpotRestApi.Production(new RestApiConfig
{
    ApiKey = Environment.GetEnvironmentVariable("API_KEY"),
    ApiSecret = Environment.GetEnvironmentVariable("API_SECRET"),
});
var time = await rest.TimeAsync();
Console.WriteLine(time.Data()!.ServerTime);
```

在 Spot 测试网上下达签名订单（可在 [testnet.binance.vision](https://testnet.binance.vision)
创建测试网密钥）：

```csharp
using Binance.Common;
using Binance.Spot.RestApi;

using var client = SpotRestApi.Testnet(new RestApiConfig
{
    ApiKey = Environment.GetEnvironmentVariable("API_KEY"),
    ApiSecret = Environment.GetEnvironmentVariable("API_SECRET"),
});

try
{
    var response = await client.NewOrderAsync(new()
    {
        Symbol = "BTCUSDT",
        Side = NewOrderSide.Buy,
        Type = NewOrderType.Market,
        Quantity = 0.001m,
    });
    Console.WriteLine($"Order {response.Data()!.OrderId} placed");
}
catch (BinanceException e)
{
    Console.Error.WriteLine($"{e.Kind} {e.Code}: {e.Message}");
}
```

如需使用私钥而非 HMAC Secret 签名，请将 `ApiSecret` 替换为
`PrivateKeyFile = "/path/to/ed25519-private-key.pem"`（或 `PrivateKeyPem`）。

订阅行情数据流（公开，无需凭证）：

```csharp
using Binance.Spot.WebSocketStreams;

var client = SpotWebSocketStreams.Production();
await using var connection = await client.ConnectAsync();
using var trades = connection.AggTrade(new() { Symbol = "btcusdt" });
await foreach (var trade in trades.Events.ReadAllAsync())
    Console.WriteLine($"{trade.S} {trade.P}");
```

### 依赖注入与日志

```csharp
services.AddBinanceRestApi<SpotRestApi>(SpotRestApi.Production, o => o.ApiKey = Environment.GetEnvironmentVariable("API_KEY"));
```

`BinanceLogging.Configure(loggerFactory)` 会将（进程级）日志输出到 `ILogger`。

### 示例

仓库在 `examples/Binance.<Product>.Examples/`
下为每个接口提供了一个可运行的示例，并以操作名称命名。例如，运行 Spot K 线示例：

```bash
dotnet run --project examples/Binance.Spot.Examples -- RestApi/Market/Klines
```

不带参数运行时，项目会列出所有可用示例。示例项目的目标框架为 `net10.0`，因此运行示例需要 .NET 10
SDK。

## 注意事项与最佳实践

- 使用环境变量或密钥管理工具安全存储 API 密钥
- 获取实时数据时，优先使用 WebSocket API 或数据流，而非轮询 REST 接口
- 注意监控频率限制和接口权重；REST 响应会提供频率限制相关的响应头
- 开发和验证集成方案时，请使用测试网环境
- 请释放客户端（`using` / `await using`）以回收连接