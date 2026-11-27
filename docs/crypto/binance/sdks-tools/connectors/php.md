---
exchange: binance
source_url: https://developers.binance.com/en/docs/sdks-tools/connectors/php
api_type: Guide
updated_at: 2026-11-27 18:27:56.113052
---

# PHP

The official PHP connector for Binance APIs, designed for backend applications and services written
in PHP.

The connector provides an idiomatic PHP interface to Binance REST APIs. It includes built-in request
signing, configuration helpers, and typed request and response models to help you build reliable
server-side integrations.

For source code, issues, and release notes, see the
[binance-connector-php](https://github.com/binance/binance-connector-php) repository on GitHub.

## Supported environments

- PHP 8.4 or newer
- Backend PHP applications and services

> This connector is intended for server-side usage only.  
> Browser-based or client-side PHP environments are not supported.

## Package structure

The PHP connector is published as a single Composer package.

Product-specific REST APIs (such as `Spot`, `DerivativesTradingUsdsFutures`, `Wallet`, and others)
are organized into namespaces within the library. This structure keeps APIs clearly separated while
allowing shared configuration, authentication, and transport logic.

## Typical use cases

- Trading and execution services using REST APIs
- Backend services managing accounts, balances, and orders
- Historical market data ingestion
- Automation and reporting workflows

## Key features

- Support for Binance REST APIs
- Built-in request signing for authenticated endpoints
- Typed request and response models
- Support for both production and testnet environments
- Consistent and idiomatic PHP API design

## Getting started

Install the connector using Composer:

```bash
composer require binance/binance-connector-php
```

Create a client and send a request:

```php
<?php

require_once __DIR__ . '/vendor/autoload.php';

use Binance\Client\Spot\Api\SpotRestApi;
use Binance\Client\Spot\SpotRestApiUtil;

$configurationBuilder = SpotRestApiUtil::getConfigurationBuilder();
$configurationBuilder
    ->apiKey(getenv('BINANCE_API_KEY'))
    ->privateKey(getenv('BINANCE_PRIVATE_KEY_FILE_PATH'));

$spotClient = new SpotRestApi($configurationBuilder->build());

$accountInfo = $spotClient->getAccount();
```

The example above uses asymmetric key authentication. HMAC-based authentication using an API secret
is also supported.

Refer to the repository documentation for additional REST API examples.

## Notes and best practices

- Store API keys securely using environment variables or a secrets manager
- Monitor rate limits and endpoint weights when building high-throughput services
- Use testnet environments when developing and validating integrations

---

# PHP

Binance API 官方 PHP 连接器，专为使用 PHP 编写的后端应用程序和服务而设计。

该连接器为 Binance REST
API 提供符合 PHP 惯例的接口。内置请求签名、配置辅助工具以及强类型的请求与响应模型，助您构建可靠的服务端集成方案。

如需查看源代码、问题反馈及版本说明，请访问 GitHub 上的
[binance-connector-php](https://github.com/binance/binance-connector-php) 仓库。

## 支持的环境

- PHP 8.4 或更高版本
- 后端 PHP 应用程序及服务

> 本连接器仅适用于服务端使用。  
> 不支持基于浏览器或客户端的 PHP 环境。

## 包结构

PHP 连接器以单一 Composer 包的形式发布。

各产品的 REST API（如 `Spot`、`DerivativesTradingUsdsFutures`、`Wallet`
等）在库中按命名空间进行组织。这种结构使各 API 保持清晰分离，同时允许共享配置、身份验证和传输逻辑。

## 典型使用场景

- 使用 REST API 的交易与执行服务
- 管理账户、余额和订单的后端服务
- 历史行情数据采集
- 自动化和报表工作流

## 主要特性

- 支持 Binance REST API
- 内置针对需要身份验证接口的请求签名
- 强类型的请求与响应模型
- 同时支持正式环境和测试网环境
- 一致且符合 PHP 惯例的 API 设计

## 快速开始

使用 Composer 安装连接器：

```bash
composer require binance/binance-connector-php
```

创建客户端并发送请求：

```php
<?php

require_once __DIR__ . '/vendor/autoload.php';

use Binance\Client\Spot\Api\SpotRestApi;
use Binance\Client\Spot\SpotRestApiUtil;

$configurationBuilder = SpotRestApiUtil::getConfigurationBuilder();
$configurationBuilder
    ->apiKey(getenv('BINANCE_API_KEY'))
    ->privateKey(getenv('BINANCE_PRIVATE_KEY_FILE_PATH'));

$spotClient = new SpotRestApi($configurationBuilder->build());

$accountInfo = $spotClient->getAccount();
```

上述示例使用非对称密钥进行身份验证。同样支持基于 API Secret 的 HMAC 身份验证方式。

如需更多 REST API 示例，请参阅仓库文档。

## 注意事项与最佳实践

- 使用环境变量或密钥管理工具安全存储 API 密钥
- 构建高吞吐量服务时，注意监控频率限制和接口权重
- 开发和验证集成方案时，请使用测试网环境