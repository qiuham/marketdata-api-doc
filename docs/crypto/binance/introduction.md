---
exchange: binance
source_url: https://developers.binance.com/en/docs/introduction
api_type: Guide
updated_at: 2026-11-19 18:28:25.313309
---

# Binance Developer Documentation

Welcome to the official Binance API documentation.

This portal is the central reference for developers building applications, services, and trading
systems that integrate with Binance. It covers the main programmatic interfaces available across
Binance products, from market data access and account operations to advanced trading, streaming, and
lower-latency integrations.

Whether you are building a simple script, a production backend, or a professional trading system,
these docs are designed to help you understand the available interfaces, choose the right
integration path, and implement it reliably.

---

## How to use this documentation

This documentation is organized into three main areas:

- **Documentation**  
  Conceptual guides, onboarding content, environment information, and operational guidance.

- **API Reference**  
  Endpoint definitions, request parameters, payload schemas, and API-specific details.

- **SDKs & Tools**  
  Official connectors, Postman collections, developer tools, and implementation resources.

If you are new to Binance APIs, start with the documentation guides first. If you already know which
product or endpoint you need, you can move directly into the relevant API reference.

---

## Choose a starting point

A good starting point depends on what you are trying to do:

- **New to Binance APIs**  
  Start with the documentation guides, supported API types, environments, and authentication
  requirements.

- **Need endpoint details**  
  Go directly to the API Reference for request parameters, payloads, and endpoint-specific behavior.

- **Looking for connectors or testing resources**  
  Visit SDKs & Tools for official connectors, Postman collections, developer tools, and
  implementation resources.

- **Working on product-specific integrations**  
  Navigate to the relevant product family first, such as Spot, Futures, Wallet, or other supported
  areas.

---

## Start here

A common onboarding path is:

1. Review the supported API types and product areas
2. Create an API key if your integration requires authenticated access
3. Understand authentication, signing, and environment support
4. Validate your implementation in a supported non-production environment where available
5. Move to production only after confirming product-specific requirements and limits

---

## What you can build with Binance APIs

Using Binance APIs, you can:

- Access real-time and historical market data
- Place, manage, and cancel orders programmatically
- Monitor account state, balances, and positions
- Consume live updates through WebSocket-based interfaces
- Build trading bots, automation, and internal services
- Integrate Binance data into dashboards, analytics, and reporting systems
- Support lower-latency or institutional workflows with specialized interfaces

The platform supports both lightweight integrations and more advanced, performance-sensitive
systems.

---

## API types

Binance provides multiple API styles to support different integration patterns:

- **REST APIs**  
  Request/response HTTP APIs for market data, trading, account operations, and other product
  workflows.

- **WebSocket APIs**  
  Request/response APIs over persistent connections, useful for interactive and stateful workflows.

- **WebSocket Streams**  
  Push-based real-time streams for market data and user events.

- **FIX APIs**  
  Session-based APIs designed for advanced and institutional trading workflows.

- **SBE (Simple Binary Encoding)**  
  Binary-encoded payload formats intended for performance-sensitive environments.

Each API type has different trade-offs in latency, throughput, operational complexity, and client
design. Product documentation will indicate when a specific interface is recommended.

---

## Authentication and security

Many private endpoints require authentication. Depending on the interface and product, Binance
supports mechanisms such as:

- HMAC-based request signing
- Asymmetric key authentication, including RSA and Ed25519
- Session-based authentication for selected WebSocket and FIX workflows

Authentication requirements are documented in the relevant product sections. During development, use
dedicated testnet or demo environments where supported, protect credentials carefully, and review
signing requirements before going live.

---

## Rate limits and reliability

Binance APIs enforce rate limits and request weights. These limits vary by product and endpoint, and
exceeding them may result in throttling or temporary restrictions.

Production integrations should account for:

- Request weights and endpoint-specific limits
- Retry and backoff strategies
- Connection health and reconnection handling
- Monitoring for API errors and degraded conditions

Always review the relevant product documentation before deploying systems at scale.

---

## Environments

Binance provides different environments depending on the product and interface, including:

- **Production** for live trading and real market data
- **Testnet** for supported testing workflows without real funds
- **Demo environments** for supported products and scenarios where simulated or non-production
  access is available

Environment support is not identical across all products. Some products support testnet, some
support demo environments, and others may have different non-production availability. Before
implementation or rollout, verify which environments are supported for the specific API and product
you intend to use.

---

## Agent Native

Binance APIs are designed to be agent-friendly. Whether you are building autonomous trading bots,
AI-powered assistants, or automated workflows, the following resources are available:

- **llms.txt** — Machine-readable documentation index at [`/llms.txt`](/llms.txt) for LLM-based
  tools and agents
- **Agent REST API** — Structured endpoints optimized for programmatic and agent-driven access
- **MCP Server** — Model Context Protocol server for seamless integration with AI development tools

For more details, see the [Agent Native overview](/agent-native/overview).

---

## SDKs, tools, and samples

To help accelerate development, Binance provides supporting resources such as:

- Official SDKs in supported languages
- Developer tools and utilities
- Postman collections for exploration and testing
- Examples and sample applications for common workflows

These resources can help shorten the path from initial exploration to a working integration.

---

## Official and supported interfaces

Interfaces, endpoints, streams, parameters, and payloads documented in this portal are considered
officially documented for developer use.

Undocumented behaviors or unofficial interfaces should not be relied upon in production systems.
They may change without notice and are outside the scope of supported documentation.

---

## Product-specific updates

API changes, new features, and breaking updates are typically documented within the relevant product
areas. Before deploying or upgrading an integration, review the documentation for the specific
product you depend on.

---

## Getting help

If you need help while integrating:

- Review the relevant documentation and API reference first
- Check available tools, examples, and sample applications
- Join the [Binance Developer Community](https://dev.binance.vision)
- Open issues in the relevant GitHub repositories when appropriate
- Follow the official Telegram
  [Binance API announcements channel](https://t.me/binance_api_announcements) for service and
  API-related updates

---

This documentation evolves as Binance products and APIs change. Check back regularly and review
product-specific documentation before making production changes.

---

# Binance 开发者文档

欢迎使用 Binance 官方 API 文档。

本门户是面向开发者的核心参考文档，适用于构建与 Binance 集成的应用、服务和交易系统。文档覆盖 Binance 各类产品提供的主要程序化接口，从市场数据访问、账户操作，到高级交易、流式传输以及更低延迟的集成方式。

无论你是在编写简单脚本、生产级后端服务，还是专业交易系统，这些文档都旨在帮助你了解可用接口、选择合适的集成路径，并可靠地完成实现。

---

## 如何使用本套文档

本套文档主要分为三个部分：

- **Documentation**  
  概念指南、入门内容、环境说明以及运维相关指导。

- **API Reference**  
  接口定义、请求参数、负载结构以及 API 细节说明。

- **SDKs & Tools**  
  官方 SDK、Postman Collections、开发者工具以及实现相关资源。

如果你是第一次接触 Binance
API，建议先从文档指南开始阅读。如果你已经明确知道所需的产品或接口，也可以直接进入对应的 API
Reference。

---

## 选择你的起点

合适的起点取决于你当前想完成的事情：

- **刚开始接触 Binance API**  
  建议先阅读文档指南、支持的 API 类型、环境说明以及鉴权要求。

- **需要查看接口细节**  
  可直接进入 API Reference，查看请求参数、负载结构以及接口的具体行为。

- **在寻找 SDK、连接器或测试资源**  
  可访问 SDKs & Tools，查看官方 SDK、Postman Collections、开发者工具以及实现资源。

- **正在进行特定产品集成**  
  建议先进入对应的产品线，例如 Spot、Futures、Wallet 或其他支持的产品领域。

---

## 从这里开始

一个常见的接入路径如下：

1. 了解支持的 API 类型和产品范围
2. 如果你的集成需要鉴权访问，先创建 API Key
3. 了解鉴权、签名以及环境支持情况
4. 在支持的非生产环境中完成验证（如可用）
5. 在确认产品级要求和限制后，再迁移到生产环境

---

## 你可以用 Binance API 构建什么

通过 Binance API，你可以：

- 获取实时和历史市场数据
- 以程序化方式下单、管理订单和撤单
- 监控账户状态、余额和持仓
- 通过基于 WebSocket 的接口接收实时更新
- 构建交易机器人、自动化流程和内部服务
- 将 Binance 数据集成到仪表盘、分析和报表系统中
- 通过专用接口支持更低延迟或机构级工作流

该平台既支持轻量级集成，也支持更高级、对性能更敏感的系统。

---

## API 类型

Binance 提供多种 API 形式，以支持不同的集成模式：

- **REST APIs**  
  基于 HTTP 的请求/响应式 API，适用于市场数据、交易、账户操作及其他产品工作流。

- **WebSocket APIs**  
  基于持久连接的请求/响应式 API，适合交互式和有状态的工作流。

- **WebSocket Streams**  
  面向市场数据和用户事件的实时推送流。

- **FIX APIs**  
  面向高级和机构交易工作流的会话式 API。

- **SBE（Simple Binary Encoding）**  
  面向性能敏感场景的二进制编码负载格式。

不同 API 类型在延迟、吞吐、运维复杂度和客户端设计方面各有取舍。具体产品文档会说明何时更适合使用某种接口。

---

## 鉴权与安全

许多私有接口都需要鉴权。根据接口类型和产品不同，Binance 支持的机制包括：

- 基于 HMAC 的请求签名
- 非对称密钥鉴权，包括 RSA 和 Ed25519
- 适用于部分 WebSocket 和 FIX 工作流的会话式鉴权

具体鉴权要求会在对应产品文档中说明。在开发过程中，请尽量使用支持的 Testnet 或 Demo 环境，妥善保护凭证，并在上线前仔细核对签名要求。

---

## 速率限制与可靠性

Binance
API 会实施速率限制和请求权重控制。这些限制会因产品和接口而异，超出限制可能会导致限流或临时限制。

生产环境中的集成应考虑：

- 请求权重和接口级限制
- 重试与退避策略
- 连接健康检查与重连处理
- 对 API 错误和服务降级的监控

在大规模部署系统之前，请务必先查阅对应产品的相关文档。

---

## 环境

Binance 会根据产品和接口提供不同环境，包括：

- **Production**：用于真实交易和真实市场数据
- **Testnet**：用于支持的测试流程，无需真实资金
- **Demo environments**：适用于支持的产品和场景，可提供模拟或非生产访问

不同产品对环境的支持并不完全一致。有些产品支持 Testnet，有些支持 Demo 环境，另一些则可能提供不同形式的非生产环境。在实现或上线前，请确认你所使用的具体 API 和产品支持哪些环境。

---

## Agent 原生

Binance
API 从设计上即对 Agent 友好。无论你在构建自动化交易机器人、AI 驱动的助手，还是自动化工作流，以下资源均可使用：

- **llms.txt** — 面向 LLM 工具和 Agent 的机器可读文档索引，访问 [`/llms.txt`](/llms.txt)
- **Agent REST API** — 针对程序化和 Agent 驱动访问优化的结构化端点
- **MCP Server** — Model Context Protocol 服务器，无缝集成 AI 开发工具

了解更多详情，请查看 [Agent 原生概览](/agent-native/overview)。

---

## SDK、工具与示例

为帮助你更快完成开发，Binance 提供了以下支持资源：

- 支持语言中的官方 SDK
- 开发者工具与实用程序
- 用于探索和测试的 Postman Collections
- 覆盖常见工作流的示例和样例应用

这些资源可以帮助你更快地从初步探索走向实际可运行的集成。

---

## 官方与受支持的接口

本门户中记录的接口、端点、流、参数和负载，均可视为面向开发者正式文档化的内容。

不应在生产系统中依赖未文档化的行为或非官方接口。这些内容可能在不另行通知的情况下发生变化，也不属于受支持文档范围。

---

## 产品级更新

API 变更、新功能和破坏性更新通常会记录在对应产品区域中。在部署或升级集成之前，请先查看你所依赖产品的相关文档。

---

## 获取帮助

如果你在集成过程中需要帮助：

- 先查看相关文档和 API Reference
- 查看可用工具、示例和样例应用
- 加入 [Binance Developer Community](https://dev.binance.vision)
- 在适当情况下到对应 GitHub 仓库提交 issue
- 关注官方 Telegram
  [Binance API announcements channel](https://t.me/binance_api_announcements)，获取服务和 API 相关更新

---

随着 Binance 产品和 API 的持续演进，本文档也会不断更新。请定期回访，并在进行生产变更前查看相关产品文档。