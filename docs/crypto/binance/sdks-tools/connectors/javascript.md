---
exchange: binance
source_url: https://developers.binance.com/en/docs/sdks-tools/connectors/javascript
api_type: Guide
updated_at: 2026-11-23 18:27:34.972268
---

# JavaScript

The official JavaScript connector for Binance APIs, designed for backend applications running on
Node.js.

The connector is fully modular: each Binance product is published as a separate `npm` package (for
example `@binance/spot`), allowing you to install and use only the APIs you need. It supports REST
APIs, WebSocket APIs and WebSocket Streams and provides built-in request signing, connection
management and TypeScript definitions.

For source code, issues, and release notes, see the
[binance-connector-js](https://github.com/binance/binance-connector-js) repository on GitHub.

## Supported environments

- Node.js v22 or newer (LTS versions recommended)
- JavaScript and TypeScript backend applications

> This connector is intended for server-side usage only.  
> Browser environments are not supported at this time.

## Package structure

Each Binance product is published as an independent `npm` package under the `@binance` scope.

Commonly used packages include:

- `@binance/spot`
- `@binance/derivatives-trading-usds-futures`
- `@binance/derivatives-trading-coin-futures`
- `@binance/wallet`
- _(additional products follow the same structure)_

This modular approach keeps dependencies minimal and makes upgrades and integrations easier to
manage.

## Typical use cases

- Trading and execution services
- Real-time and historical market data ingestion
- Backend services managing accounts, balances, and orders
- Applications consuming WebSocket APIs or WebSocket Streams for low-latency updates

## Key features

- Support for Binance REST APIs, WebSocket APIs and WebSocket Streams
- Built-in request signing for authenticated endpoints
- WebSocket connection handling with automatic reconnection and session renewal
- First-class TypeScript definitions
- Support for both production and testnet environments
- Consistent API design across products

## Getting started

Install the package for the product you want to integrate with:

```bash
npm install @binance/spot
```

Create a client and send a request:

```ts
import { Spot } from "@binance/spot";

const configurationRestAPI = {
  apiKey: process.env.BINANCE_API_KEY,
  privateKey: process.env.BINANCE_PRIVATE_KEY,
};
const spotClient = new Spot({ configurationRestAPI });

const accountInfo = await spotClient.restAPI.getAccount();
```

The example above uses asymmetric key authentication. HMAC-based authentication using an API secret
is also supported.

Refer to each package’s documentation for product-specific REST, WebSocket API and WebSocket Streams
examples.

## Notes and best practices

- Store API keys securely using environment variables or a secrets manager
- Prefer WebSocket APIs or Streams for real-time data instead of polling REST endpoints
- Monitor rate limits and endpoint weights when building high-throughput services
- Use testnet environments when developing and validating integrations

---

# JavaScript

Binance API 官方 JavaScript 连接器，专为运行在 Node.js 上的后端应用程序而设计。

该连接器采用完全模块化设计：每个 Binance 产品均以独立的 `npm` 包形式发布（例如
`@binance/spot`），您可以按需安装和使用所需的 API。它支持 REST API、WebSocket
API 和 WebSocket 数据流，并提供内置的请求签名、连接管理以及 TypeScript 类型定义。

如需查看源代码、问题反馈及版本说明，请访问 GitHub 上的
[binance-connector-js](https://github.com/binance/binance-connector-js) 仓库。

## 支持的环境

- Node.js v22 或更高版本（推荐使用 LTS 版本）
- JavaScript 和 TypeScript 后端应用程序

> 本连接器仅适用于服务端使用。  
> 目前不支持浏览器环境。

## 包结构

每个 Binance 产品均以独立的 `npm` 包形式发布，统一归属于 `@binance` 命名空间。

常用包包括：

- `@binance/spot`
- `@binance/derivatives-trading-usds-futures`
- `@binance/derivatives-trading-coin-futures`
- `@binance/wallet`
- _（其他产品遵循相同的结构）_

这种模块化方式将依赖项保持在最低限度，同时使升级和集成管理更加便捷。

## 典型使用场景

- 交易与执行服务
- 实时及历史行情数据采集
- 管理账户、余额和订单的后端服务
- 通过 WebSocket API 或 WebSocket 数据流获取低延迟更新的应用程序

## 主要特性

- 支持 Binance REST API、WebSocket API 和 WebSocket 数据流
- 内置针对需要身份验证接口的请求签名
- WebSocket 连接管理，支持自动重连和会话续期
- 完整的 TypeScript 类型定义
- 同时支持正式环境和测试网环境
- 跨产品一致的 API 设计

## 快速开始

安装您需要集成的产品对应的包：

```bash
npm install @binance/spot
```

创建客户端并发送请求：

```ts
import { Spot } from "@binance/spot";

const configurationRestAPI = {
  apiKey: process.env.BINANCE_API_KEY,
  privateKey: process.env.BINANCE_PRIVATE_KEY,
};
const spotClient = new Spot({ configurationRestAPI });

const accountInfo = await spotClient.restAPI.getAccount();
```

上述示例使用非对称密钥进行身份验证。同样支持基于 API Secret 的 HMAC 身份验证方式。

如需各产品的 REST、WebSocket API 和 WebSocket 数据流示例，请参阅各包的文档。

## 注意事项与最佳实践

- 使用环境变量或密钥管理工具安全存储 API 密钥
- 获取实时数据时，优先使用 WebSocket API 或数据流，而非轮询 REST 接口
- 构建高吞吐量服务时，注意监控频率限制和接口权重
- 开发和验证集成方案时，请使用测试网环境