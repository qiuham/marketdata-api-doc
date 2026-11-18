---
exchange: binance
source_url: https://developers.binance.com/en/docs/sdks-tools/sample-apps/sbe-rust
api_type: SBE
updated_at: 2026-11-18 01:51:09.039681
---

# SBE Sample App (Rust)

The Rust SBE Sample Application is a reference implementation that demonstrates how to **decode
Binance API responses encoded using Simple Binary Encoding (SBE)** in a Rust environment.

It reads an SBE-encoded payload from **STDIN** and outputs a **human-readable YAML representation**
to **STDOUT**, making it useful for inspecting, debugging, and validating SBE responses returned by
Binance APIs.

For source code, updates, and examples, see the
[binance-sbe-rust-sample-app](https://github.com/binance/binance-sbe-rust-sample-app) repository on
GitHub.

## Supported environments

- Rust (toolchain defined in `rust-toolchain.toml`)
- Linux
- macOS

> This is a sample application intended for local execution and inspection.  
> It is not a production-ready SDK.

## What this sample demonstrates

This application focuses on **decoding SBE-encoded API responses**, not on sending or managing
requests.

It demonstrates how to:

- Decode SBE responses in Rust
- Convert binary SBE payloads into human-readable YAML
- Pipe SBE responses from REST or WebSocket APIs into a Rust decoder
- Reuse generated SBE decoder modules in Rust projects

## Typical use cases

- Inspecting and validating SBE responses
- Debugging integrations that use SBE
- Learning how Binance SBE schemas are decoded in Rust
- Building internal tooling around SBE-based APIs
- Verifying authentication and request signing workflows with SBE output

## Getting started

Clone the repository:

```bash
git clone https://github.com/binance/binance-sbe-rust-sample-app.git
cd binance-sbe-rust-sample-app
```

Build the sample application:

```bash
cargo build
```

The resulting binary is located at:

```text
./target/debug/sbe-sample-app
```

## Using the sample app

The application reads SBE-encoded data from STDIN and prints decoded YAML to STDOUT.

### Example: decoding an SBE REST response

```bash
curl -H "Accept: application/sbe" -H "X-MBX-SBE: 3:1" \
  "<api-endpoint>" \
  | ./target/debug/sbe-sample-app
```

### Example: decoding an SBE WebSocket response

You can pipe WebSocket responses into the app using a helper script or tool that forwards raw
WebSocket messages:

```bash
echo '<websocket-request-json>' \
  | ./tools/websocket_send.py '<websocket-endpoint>' \
  | ./target/debug/sbe-sample-app
```

To run `websocket_send.py`, your Python environment must include the websocket-client package.

## Authentication

When requesting SBE responses from authenticated endpoints, standard Binance authentication methods
apply.

Examples in the repository demonstrate usage with:

- `HMAC`-based authentication
- `RSA`-based authentication
- `Ed25519`-based authentication

The sample application itself does not perform signing—it only decodes SBE responses.

## SBE decoders

The repository includes Rust decoder modules generated from Binance SBE schemas using
[Simple Binary Encoding (SBE)](https://github.com/aeron-io/simple-binary-encoding).

These decoders can be reused directly in your own Rust projects. If needed, the decoders can be
regenerated from the latest schema files by following the instructions in the repository.

## Notes and best practices

- This project is intended as a reference and debugging tool
- Always validate decoded fields against the official API documentation
- Prefer SBE only when binary efficiency or latency is required
- For general-purpose integrations, REST or WebSocket APIs may be simpler to use
- Use testnet environments when experimenting with authenticated endpoints

---

# SBE 示例应用（Rust）

Rust SBE 示例应用是一个参考实现，演示如何在 Rust 环境中**解码使用简单二进制编码（SBE）格式的 Binance
API 响应**。

它从 **STDIN** 读取 SBE 编码的数据载荷，并将**人类可读的 YAML 表示**输出至
**STDOUT**，可用于检查、调试和验证 Binance API 返回的 SBE 响应。

如需查看源代码、更新说明及示例，请访问 GitHub 上的
[binance-sbe-rust-sample-app](https://github.com/binance/binance-sbe-rust-sample-app) 仓库。

## 支持的环境

- Rust（工具链版本定义于 `rust-toolchain.toml`）
- Linux
- macOS

> 本示例应用仅供本地运行和检查使用。  
> 它不是一个生产就绪的 SDK。

## 示例演示内容

本应用专注于**解码 SBE 编码的 API 响应**，而非发送或管理请求本身。

它演示了如何：

- 在 Rust 中解码 SBE 响应
- 将二进制 SBE 载荷转换为人类可读的 YAML
- 将 REST 或 WebSocket API 的 SBE 响应通过管道传入 Rust 解码器
- 在 Rust 项目中复用已生成的 SBE 解码器模块

## 典型使用场景

- 检查和验证 SBE 响应
- 调试使用 SBE 的集成方案
- 学习如何在 Rust 中解码 Binance SBE 模式
- 围绕基于 SBE 的 API 构建内部工具
- 验证 SBE 输出的身份验证和请求签名工作流

## 快速开始

克隆仓库：

```bash
git clone https://github.com/binance/binance-sbe-rust-sample-app.git
cd binance-sbe-rust-sample-app
```

构建示例应用：

```bash
cargo build
```

生成的二进制文件位于：

```text
./target/debug/sbe-sample-app
```

## 使用示例应用

该应用从 STDIN 读取 SBE 编码数据，并将解码后的 YAML 输出至 STDOUT。

### 示例：解码 SBE REST 响应

```bash
curl -H "Accept: application/sbe" -H "X-MBX-SBE: 3:1" \
  "<api-endpoint>" \
  | ./target/debug/sbe-sample-app
```

### 示例：解码 SBE WebSocket 响应

您可以通过辅助脚本或工具将 WebSocket 原始消息转发后，通过管道传入应用进行解码：

```bash
echo '<websocket-request-json>' \
  | ./tools/websocket_send.py '<websocket-endpoint>' \
  | ./target/debug/sbe-sample-app
```

运行 `websocket_send.py` 需要 Python 环境中安装 websocket-client 包。

## 身份验证

向需要身份验证的接口请求 SBE 响应时，适用标准的 Binance 身份验证方式。

仓库中的示例演示了以下身份验证方式的用法：

- 基于 `HMAC` 的身份验证
- 基于 `RSA` 的身份验证
- 基于 `Ed25519` 的身份验证

示例应用本身不执行请求签名——它仅负责解码 SBE 响应。

## SBE 解码器

仓库包含使用 [Simple Binary Encoding (SBE)](https://github.com/aeron-io/simple-binary-encoding)
从 Binance SBE 模式文件生成的 Rust 解码器模块。

这些解码器可直接在您自己的 Rust 项目中复用。如有需要，可按照仓库中的说明从最新模式文件重新生成解码器。

## 注意事项与最佳实践

- 本项目旨在作为参考实现和调试工具使用
- 请始终对照官方 API 文档验证解码后的字段
- 仅在需要二进制传输效率或低延迟时才考虑使用 SBE
- 对于通用集成场景，REST 或 WebSocket API 可能更易于使用
- 在测试已认证接口时，请使用测试网环境