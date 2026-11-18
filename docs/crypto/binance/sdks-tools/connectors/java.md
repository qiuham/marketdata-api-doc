---
exchange: binance
source_url: https://developers.binance.com/en/docs/sdks-tools/connectors/java
api_type: Guide
updated_at: 2026-11-18 01:51:59.721105
---

# Java

The official Java connector for Binance APIs, designed for backend applications and services running
on the JVM.

The connector provides a modular and idiomatic Java interface to Binance APIs, supporting REST APIs,
WebSocket APIs and WebSocket Streams. It includes built-in request signing, connection management,
and strongly typed request and response models to help you build reliable and maintainable
integrations.

For source code, issues, and release notes, see the
[binance-connector-java](https://github.com/binance/binance-connector-java) repository on GitHub.

## Supported environments

- Java 11 or newer
- Backend Java applications and JVM-based services

> This connector is intended for server-side usage only.

## Package structure

The Java connector is published as a set of product-specific artifacts.

Each Binance product is distributed as an independent dependency (for example `binance-sdk-spot`),
allowing you to include only the APIs you need. This modular structure keeps dependencies minimal
and makes upgrades and integrations easier to manage.

## Typical use cases

- Trading and execution services
- Real-time and historical market data ingestion
- Backend services managing accounts, balances, and orders
- Applications consuming WebSocket APIs or WebSocket Streams for low-latency updates

## Key features

- Support for Binance REST APIs, WebSocket APIs and WebSocket Streams
- Built-in request signing for authenticated endpoints
- WebSocket connection handling with automatic reconnection and session renewal
- Strongly typed request and response models
- Support for both production and testnet environments
- Consistent and idiomatic Java API design

## Getting started

Install the dependency for the product you want to integrate with:

```xml
<dependency>
  <groupId>io.github.binance</groupId>
  <artifactId>binance-spot</artifactId>
  <version><!-- latest version --></version>
</dependency>
```

Create a client and send a request:

```java
import com.binance.connector.client.common.configuration.ClientConfiguration;
import com.binance.connector.client.common.configuration.SignatureConfiguration;
import com.binance.connector.client.spot.rest.api.SpotRestApi;
import com.binance.connector.client.common.ApiResponse;
import com.binance.connector.client.spot.rest.model.GetAccountResponse;

public class Main {
    public static void main(String[] args) throws Exception {
        SignatureConfiguration signatureConfiguration = new SignatureConfiguration();
        signatureConfiguration.setApiKey(System.getenv("BINANCE_API_KEY"));
        signatureConfiguration.setPrivateKey(System.getenv("BINANCE_PRIVATE_KEY"));

        ClientConfiguration clientConfiguration = new ClientConfiguration();
        clientConfiguration.setSignatureConfiguration(signatureConfiguration);
        SpotRestApi spotApi = new SpotRestApi(clientConfiguration);

        ApiResponse<GetAccountResponse> accountInfo = spotApi.getAccount();
    }
}
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

# Java

Binance API 官方 Java 连接器，专为运行在 JVM 上的后端应用程序和服务而设计。

该连接器为 Binance API 提供模块化且符合 Java 惯例的接口，支持 REST API、WebSocket
API 和 WebSocket 数据流。内置请求签名、连接管理以及强类型的请求与响应模型，助您构建可靠且易于维护的集成方案。

如需查看源代码、问题反馈及版本说明，请访问 GitHub 上的
[binance-connector-java](https://github.com/binance/binance-connector-java) 仓库。

## 支持的环境

- Java 11 或更高版本
- 后端 Java 应用程序及基于 JVM 的服务

> 本连接器仅适用于服务端使用。

## 包结构

Java 连接器以一组针对各产品的独立构件形式发布。

每个 Binance 产品均作为独立依赖项分发（例如
`binance-sdk-spot`），您可以按需引入所需的 API。这种模块化结构将依赖项保持在最低限度，同时使升级和集成管理更加便捷。

## 典型使用场景

- 交易与执行服务
- 实时及历史行情数据采集
- 管理账户、余额和订单的后端服务
- 通过 WebSocket API 或 WebSocket 数据流获取低延迟更新的应用程序

## 主要特性

- 支持 Binance REST API、WebSocket API 和 WebSocket 数据流
- 内置针对需要身份验证接口的请求签名
- WebSocket 连接管理，支持自动重连和会话续期
- 强类型的请求与响应模型
- 同时支持正式环境和测试网环境
- 一致且符合 Java 惯例的 API 设计

## 快速开始

安装您需要集成的产品对应的依赖项：

```xml
<dependency>
  <groupId>io.github.binance</groupId>
  <artifactId>binance-spot</artifactId>
  <version><!-- 最新版本 --></version>
</dependency>
```

创建客户端并发送请求：

```java
import com.binance.connector.client.common.configuration.ClientConfiguration;
import com.binance.connector.client.common.configuration.SignatureConfiguration;
import com.binance.connector.client.spot.rest.api.SpotRestApi;
import com.binance.connector.client.common.ApiResponse;
import com.binance.connector.client.spot.rest.model.GetAccountResponse;

public class Main {
    public static void main(String[] args) throws Exception {
        SignatureConfiguration signatureConfiguration = new SignatureConfiguration();
        signatureConfiguration.setApiKey(System.getenv("BINANCE_API_KEY"));
        signatureConfiguration.setPrivateKey(System.getenv("BINANCE_PRIVATE_KEY"));

        ClientConfiguration clientConfiguration = new ClientConfiguration();
        clientConfiguration.setSignatureConfiguration(signatureConfiguration);
        SpotRestApi spotApi = new SpotRestApi(clientConfiguration);

        ApiResponse<GetAccountResponse> accountInfo = spotApi.getAccount();
    }
}
```

上述示例使用非对称密钥进行身份验证。同样支持基于 API Secret 的 HMAC 身份验证方式。

如需各产品的 REST、WebSocket API 和 WebSocket 数据流示例，请参阅各包的文档。

## 注意事项与最佳实践

- 使用环境变量或密钥管理工具安全存储 API 密钥
- 获取实时数据时，优先使用 WebSocket API 或数据流，而非轮询 REST 接口
- 构建高吞吐量服务时，注意监控频率限制和接口权重
- 开发和验证集成方案时，请使用测试网环境