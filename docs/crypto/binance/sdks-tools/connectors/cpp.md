---
exchange: binance
source_url: https://developers.binance.com/en/docs/sdks-tools/connectors/cpp
api_type: Guide
updated_at: 2026-11-27 18:28:04.872117
---

# C++

The official C++ connector for Binance APIs, designed for backend applications and services written
in modern C++.

The connector is a collection of auto-generated CMake components, one per Binance product (for
example `spot` or `wallet`). Each component provides typed REST API, WebSocket API and WebSocket
Streams clients built on the shared `binance::common` library, which handles request signing, HTTP,
WebSocket connection management, errors and utilities.

For source code, issues, and release notes, see the
[binance-connector-cpp](https://github.com/binance/binance-connector-cpp) repository on GitHub. The
generated API reference is available at
[binance.github.io/binance-connector-cpp](https://binance.github.io/binance-connector-cpp/).

## Supported environments

- C++20 compiler: GCC 12+, Clang 15+, Apple Clang 15+ or MSVC 19.34+ (Visual Studio 2022 17.4)
- CMake 3.24 or newer and Ninja
- [vcpkg](https://github.com/microsoft/vcpkg) with `VCPKG_ROOT` set (installs Boost.Asio,
  Boost.Beast, Boost.JSON, OpenSSL 3 and zlib)

> This connector is intended for server-side usage only.

## Package structure

Every product is a separate CMake component and target (`binance::spot`, `binance::wallet`, ...), so
you build and link only what you need. `binance::common` is pulled in automatically.

When installing with vcpkg, each product is a feature named like the product with hyphens instead of
underscores (for example `copy-trading` builds the `copy_trading` component). Name the connectors
you need, or `all` for every connector: without features, only `binance::common` is built.

## Typical use cases

- Low-latency trading and execution services
- High-throughput market data ingestion
- Backend services managing accounts, balances, and orders
- Applications consuming WebSocket APIs or WebSocket Streams for real-time updates

## Key features

- Support for Binance REST APIs, WebSocket APIs and WebSocket Streams
- Built-in request signing (HMAC, RSA and Ed25519 keys) for authenticated endpoints
- Automatic WebSocket connection management: reconnects with backoff, session renewal, and restored
  subscriptions
- Strongly typed request and response models
- Support for production, testnet and (where available) demo environments
- One runnable example program per endpoint

## Getting started

The repository ships a vcpkg port. Use it as an overlay port after checking out the release you
want:

```bash
vcpkg install "binance-connector-cpp[spot]" --overlay-ports=/path/to/binance-connector-cpp/ports
vcpkg install "binance-connector-cpp[wallet,derivatives-trading-usds-futures]" --overlay-ports=/path/to/binance-connector-cpp/ports
```

Alternatively, build from source and install only the products you need:

```bash
cmake --preset release -DBINANCE_PRODUCTS=spot
cmake --build --preset release
cmake --install build/release --prefix /opt/binance --strip
```

Link it from your CMake project:

```cmake
find_package(binance-connector-cpp CONFIG REQUIRED COMPONENTS spot)
target_link_libraries(app PRIVATE binance::spot)
```

Or build it as part of your project with `FetchContent` (or `add_subdirectory`). Your project then
provides the dependencies, for example by listing `boost-asio`, `boost-beast`, `boost-json`,
`openssl` and `zlib` in its own `vcpkg.json`:

```cmake
include(FetchContent)
set(BINANCE_PRODUCTS "spot" CACHE STRING "" FORCE)
FetchContent_Declare(binance-connector-cpp
    GIT_REPOSITORY https://github.com/binance/binance-connector-cpp.git
    GIT_TAG v1.0.0)
FetchContent_MakeAvailable(binance-connector-cpp)
target_link_libraries(app PRIVATE binance::spot)
```

vcpkg is not required: Boost 1.86+ (Asio, Beast, JSON), OpenSSL 3 and zlib from your system package
manager also work. An installed SDK requires at least the Boost version it was built with, and
should be used with that same version.

Include only the module you use (`rest_api.hpp`, `websocket_api.hpp` or `websocket_streams.hpp`) to
keep compile times down; `<binance/spot/spot.hpp>` includes every client of a connector. Each module
has factories for its environments: `production`, `testnet` and, where available, `demo`.

Send a signed request on the Spot testnet (`order_test` validates the order without placing it):

```cpp
#include <cstdlib>
#include <iostream>
#include <utility>

#include <binance/spot/rest_api.hpp>

using namespace binance;

int main() {
    common::RestApiConfig cfg;
    if (const char* key = std::getenv("API_KEY")) cfg.api_key = key;
    if (const char* secret = std::getenv("API_SECRET")) cfg.api_secret = secret;
    const auto rest = spot::SpotRestApi::testnet(std::move(cfg));

    using namespace spot::rest_api;
    const auto response = rest.order_test({.symbol = "BNBUSDT",
                                           .side = OrderTestSideEnum::Buy,
                                           .type = OrderTestTypeEnum::Limit,
                                           .time_in_force = OrderTestTimeInForceEnum::Gtc,
                                           .quantity = common::Decimal("0.1"),
                                           .price = common::Decimal("100")});
    std::cout << "order accepted, HTTP " << response.status() << "\n";
}
```

The example above uses an API secret. Ed25519/RSA keys are also supported by setting
`cfg.private_key = common::PrivateKey::from_file("key.pem")` instead.

Refer to the examples in the repository (`examples/<connector>/`) for product-specific REST,
WebSocket API and WebSocket Streams usage.

## Notes and best practices

- Store API keys securely using environment variables or a secrets manager
- Prefer WebSocket APIs or Streams for real-time data instead of polling REST endpoints
- Monitor rate limits and endpoint weights when building high-throughput services
- Use testnet environments when developing and validating integrations

---

# C++

Binance API 官方 C++ 连接器，专为使用现代 C++ 编写的后端应用程序和服务而设计。

该连接器是一组自动生成的 CMake 组件，每个 Binance 产品对应一个组件（例如
`spot`、`wallet`）。每个组件都提供强类型的 REST API、WebSocket
API 和 WebSocket 数据流客户端，并构建在共享的 `binance::common`
库之上，由其负责请求签名、HTTP、WebSocket 连接管理、错误处理和通用工具。

如需查看源代码、问题反馈及版本说明，请访问 GitHub 上的
[binance-connector-cpp](https://github.com/binance/binance-connector-cpp)
仓库。生成的 API 参考文档位于
[binance.github.io/binance-connector-cpp](https://binance.github.io/binance-connector-cpp/)。

## 支持的环境

- C++20 编译器：GCC 12+、Clang 15+、Apple Clang 15+ 或 MSVC 19.34+（Visual Studio 2022 17.4）
- CMake 3.24 或更高版本，以及 Ninja
- [vcpkg](https://github.com/microsoft/vcpkg)，并设置
  `VCPKG_ROOT`（用于安装 Boost.Asio、Boost.Beast、Boost.JSON、OpenSSL 3 和 zlib）

> 本连接器仅适用于服务端使用。

## 包结构

每个产品都是独立的 CMake 组件和目标（`binance::spot`、`binance::wallet`
等），因此您只需构建并链接所需的产品。 `binance::common` 会被自动引入。

使用 vcpkg 安装时，每个产品对应一个 feature，名称与产品名相同，但以连字符代替下划线（例如
`copy-trading` 会构建 `copy_trading` 组件）。请指定所需的连接器，或使用 `all`
构建所有连接器；不指定 feature 时，仅构建 `binance::common`。

## 典型使用场景

- 低延迟交易与执行服务
- 高吞吐量行情数据采集
- 管理账户、余额和订单的后端服务
- 通过 WebSocket API 或 WebSocket 数据流获取实时更新的应用程序

## 主要特性

- 支持 Binance REST API、WebSocket API 和 WebSocket 数据流
- 内置针对需要身份验证接口的请求签名（支持 HMAC、RSA 和 Ed25519 密钥）
- WebSocket 连接自动管理：带退避的自动重连、会话续期，并自动恢复订阅
- 强类型的请求与响应模型
- 支持正式环境、测试网环境以及（如适用）演示（demo）环境
- 每个接口均提供可运行的示例程序

## 快速开始

仓库提供了 vcpkg port。请先检出所需版本，然后将其作为 overlay port 使用：

```bash
vcpkg install "binance-connector-cpp[spot]" --overlay-ports=/path/to/binance-connector-cpp/ports
vcpkg install "binance-connector-cpp[wallet,derivatives-trading-usds-futures]" --overlay-ports=/path/to/binance-connector-cpp/ports
```

或者从源码构建，仅安装所需的产品：

```bash
cmake --preset release -DBINANCE_PRODUCTS=spot
cmake --build --preset release
cmake --install build/release --prefix /opt/binance --strip
```

在 CMake 项目中链接：

```cmake
find_package(binance-connector-cpp CONFIG REQUIRED COMPONENTS spot)
target_link_libraries(app PRIVATE binance::spot)
```

也可以通过 `FetchContent`（或
`add_subdirectory`）将其作为项目的一部分构建。此时依赖项由您的项目提供，例如在项目自身的
`vcpkg.json` 中列出 `boost-asio`、`boost-beast`、`boost-json`、`openssl` 和 `zlib`：

```cmake
include(FetchContent)
set(BINANCE_PRODUCTS "spot" CACHE STRING "" FORCE)
FetchContent_Declare(binance-connector-cpp
    GIT_REPOSITORY https://github.com/binance/binance-connector-cpp.git
    GIT_TAG v1.0.0)
FetchContent_MakeAvailable(binance-connector-cpp)
target_link_libraries(app PRIVATE binance::spot)
```

vcpkg 并非必需：也可使用系统包管理器提供的 Boost 1.86+（Asio、Beast、JSON）、OpenSSL
3 和 zlib。已安装的 SDK 要求 Boost 版本不低于其构建时所用版本，并应与该版本搭配使用。

建议仅包含所用模块（`rest_api.hpp`、`websocket_api.hpp` 或 `websocket_streams.hpp`）以缩短编译时间；
`<binance/spot/spot.hpp>`
会包含某个连接器的所有客户端。每个模块都为各环境提供工厂函数：`production`、`testnet`，以及（如适用）`demo`。

在 Spot 测试网上发送签名请求（`order_test` 仅验证订单，不会真正下单）：

```cpp
#include <cstdlib>
#include <iostream>
#include <utility>

#include <binance/spot/rest_api.hpp>

using namespace binance;

int main() {
    common::RestApiConfig cfg;
    if (const char* key = std::getenv("API_KEY")) cfg.api_key = key;
    if (const char* secret = std::getenv("API_SECRET")) cfg.api_secret = secret;
    const auto rest = spot::SpotRestApi::testnet(std::move(cfg));

    using namespace spot::rest_api;
    const auto response = rest.order_test({.symbol = "BNBUSDT",
                                           .side = OrderTestSideEnum::Buy,
                                           .type = OrderTestTypeEnum::Limit,
                                           .time_in_force = OrderTestTimeInForceEnum::Gtc,
                                           .quantity = common::Decimal("0.1"),
                                           .price = common::Decimal("100")});
    std::cout << "order accepted, HTTP " << response.status() << "\n";
}
```

上述示例使用 API Secret。也可以改用 Ed25519/RSA 密钥：设置
`cfg.private_key = common::PrivateKey::from_file("key.pem")`。

如需各产品的 REST、WebSocket API 和 WebSocket 数据流示例，请参阅仓库中的 `examples/<connector>/`
目录。

## 注意事项与最佳实践

- 使用环境变量或密钥管理工具安全存储 API 密钥
- 获取实时数据时，优先使用 WebSocket API 或数据流，而非轮询 REST 接口
- 构建高吞吐量服务时，注意监控频率限制和接口权重
- 开发和验证集成方案时，请使用测试网环境