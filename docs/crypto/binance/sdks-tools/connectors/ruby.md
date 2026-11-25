---
exchange: binance
source_url: https://developers.binance.com/en/docs/sdks-tools/connectors/ruby
api_type: Guide
updated_at: 2026-11-25 18:27:11.502821
---

# Ruby

The Ruby connector for Binance APIs provides a client for interacting with a subset of Binance REST
APIs and WebSocket streams from Ruby applications.

This connector is considered **legacy** and is **not actively maintained**. It supports a limited
set of Binance products and endpoints compared to newer SDKs available in other languages.

For source code, issues, and release notes, see the
[binance-connector-ruby](https://github.com/binance/binance-connector-ruby) repository on GitHub.

## Status

> ⚠️ **Maintenance status**
>
> The Ruby connector is currently **not actively maintained**. It supports only a subset of Binance
> products and APIs, and may not include newer endpoints or features.
>
> For full product coverage and ongoing updates, we recommend using one of the actively maintained
> SDKs such as JavaScript, Python, Go, Java, PHP or Rust.

## Supported environments

- Ruby 2.5 or newer
- Backend Ruby applications and scripts

> This connector is intended for server-side usage only.

## Package structure

The Ruby connector is distributed as a single Ruby gem.

It exposes a unified client interface for supported REST APIs and WebSocket streams, following a
simple client-based design. Product coverage is limited and may vary depending on the API.

## Typical use cases

- Simple scripts interacting with Binance REST APIs
- Applications consuming WebSocket streams for market data
- Lightweight automation or reporting tasks
- Prototyping or existing Ruby-based systems

## Key features

- Support for a subset of Binance REST APIs
- Support for Binance WebSocket streams
- Simple client-based API design
- API key and secret authentication
- Easy installation via RubyGems

## Getting started

Install the connector using RubyGems:

```bash
gem install binance-connector-ruby
```

Or add it to your Gemfile:

```ruby
gem 'binance-connector-ruby'
```

Then install dependencies:

```bash
bundle install
```

Create a client and send requests:

```ruby
require 'binance'

client = Binance::Spot.new(
  key: ENV['BINANCE_API_KEY'],
  secret: ENV['BINANCE_API_SECRET']
)

puts client.account
```

Refer to the repository documentation and the examples folder for additional REST and WebSocket
usage examples.

## Notes and best practices

- This connector supports REST APIs and WebSocket streams
- Product and endpoint coverage is limited and may not reflect the latest Binance APIs
- Monitor rate limits carefully, as older clients may not expose detailed weight information
- For production systems or full API coverage, use an actively maintained SDK

---

# Ruby

Binance API 的 Ruby 连接器为 Ruby 应用程序提供了一个客户端，用于与 Binance REST
API 和 WebSocket 数据流的部分功能进行交互。

该连接器被视为**历史遗留版本**，**未处于积极维护状态**。与其他语言的新版 SDK 相比，它仅支持有限的 Binance 产品和接口。

如需查看源代码、问题反馈及版本说明，请访问 GitHub 上的
[binance-connector-ruby](https://github.com/binance/binance-connector-ruby) 仓库。

## 状态

> ⚠️ **维护状态**
>
> Ruby 连接器目前**未处于积极维护状态**。它仅支持部分 Binance 产品和 API，可能不包含较新的接口或功能。
>
> 如需完整的产品支持和持续更新，我们建议使用以下积极维护中的 SDK：JavaScript、Python、Go、Java、PHP 或 Rust。

## 支持的环境

- Ruby 2.5 或更高版本
- 后端 Ruby 应用程序及脚本

> 本连接器仅适用于服务端使用。

## 包结构

Ruby 连接器以单一 Ruby gem 的形式分发。

它遵循简单的客户端设计模式，为所支持的 REST
API 和 WebSocket 数据流提供统一的客户端接口。产品覆盖范围有限，具体情况可能因 API 而异。

## 典型使用场景

- 与 Binance REST API 交互的简单脚本
- 消费 WebSocket 数据流以获取行情数据的应用程序
- 轻量级自动化或报表任务
- 原型开发或现有的基于 Ruby 的系统

## 主要特性

- 支持部分 Binance REST API
- 支持 Binance WebSocket 数据流
- 简单的客户端 API 设计
- API Key 和 Secret 身份验证
- 通过 RubyGems 便捷安装

## 快速开始

使用 RubyGems 安装连接器：

```bash
gem install binance-connector-ruby
```

或将其添加至 Gemfile：

```ruby
gem 'binance-connector-ruby'
```

然后安装依赖：

```bash
bundle install
```

创建客户端并发送请求：

```ruby
require 'binance'

client = Binance::Spot.new(
  key: ENV['BINANCE_API_KEY'],
  secret: ENV['BINANCE_API_SECRET']
)

puts client.account
```

如需更多 REST 和 WebSocket 的使用示例，请参阅仓库文档及 examples 文件夹。

## 注意事项与最佳实践

- 本连接器支持 REST API 和 WebSocket 数据流
- 产品和接口覆盖范围有限，可能未反映最新的 Binance API
- 请注意监控频率限制，旧版客户端可能不会提供详细的权重信息
- 如需用于生产环境或完整的 API 覆盖，请使用积极维护中的 SDK