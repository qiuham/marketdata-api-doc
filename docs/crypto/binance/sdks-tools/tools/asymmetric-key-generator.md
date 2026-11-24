---
exchange: binance
source_url: https://developers.binance.com/en/docs/sdks-tools/tools/asymmetric-key-generator
api_type: Guide
updated_at: 2026-11-24 18:27:13.038823
---

# Asymmetric Key Generator

The Asymmetric Key Generator is a utility for generating **Ed25519** and **RSA** asymmetric key
pairs (private and public keys) used for authenticating and signing requests to Binance APIs.

It is commonly used when working with **asymmetric authentication**, such as FIX APIs or REST /
WebSocket APIs that support `RSA` or `Ed25519` signatures.

For source code, releases, and updates, see the
[asymmetric-key-generator](https://github.com/binance/asymmetric-key-generator) repository on
GitHub.

## Supported key types

The tool can generate the following key types:

- **Ed25519** (PKCS#8)
- **RSA-2048**
- **RSA-4096**

> ⚠️ **Important**
>
> Some Binance APIs (for example FIX APIs) **require Ed25519 keys**. `RSA` keys are supported only
> by APIs that explicitly allow `RSA` authentication.

## Supported environments

- Desktop environments (macOS, Windows, Linux) via prebuilt apps
- Node.js (for CLI and local builds)

## Installation options

You can use the tool in **three different ways**, depending on your workflow.

### Option 1: Download prebuilt application (recommended)

Prebuilt desktop applications are available on the
[GitHub Releases page](https://github.com/binance/asymmetric-key-generator/releases). After
downloading, verify the package integrity using the provided checksum:

```bash
sha256sum -c AsymmetricKeyGenerator-<version>.CHECKSUM
```

If successful, the output will indicate OK.

### Option 2: Build from source

Clone the repository and build the application locally:

```bash
npm install
npm run start      # run locally
npm run dist       # build distributables into the dist folder
```

### Option 3: Command-line usage

The generator can also be used as a CLI tool.

Install dependencies:

```bash
npm install
```

Generate key pairs:

```bash
npm run generate -- -k <key-type> -p <passphrase> -n <count> -o <output>
```

Examples

Generate a single `RSA-2048` key pair:

```bash
npm run generate -- -k rsa-2048 -o id_rsa.tar.gz
```

Generate two `Ed25519` key pairs with a passphrase:

```bash
npm run generate -- -k ed25519 -p mySecretPassphrase -n 2
```

## UI usage

The desktop application provides a simple graphical interface:

1. Open the application
2. Select the key type (`Ed25519` is recommended in most cases)
3. Click Generate Key Pair
4. Save the private key securely (never share it)
5. Save the public key to upload or distribute as required

## Typical use cases

- Generating `Ed25519` keys for Binance FIX APIs
- Generating `RSA` keys for REST or WebSocket APIs that support asymmetric authentication
- Rotating API credentials securely
- Local development and testing of signed API requests

## Security best practices

- Never share your private key
- Store private keys securely on disk or in a secrets manager
- Use passphrases where supported
- Upload only the public key to Binance
- Rotate keys periodically and revoke unused credentials

---

# 非对称密钥生成器

非对称密钥生成器是一个用于生成 **Ed25519** 和 **RSA**
非对称密钥对（私钥和公钥）的工具，用于对 Binance API 的请求进行身份验证和签名。

该工具常用于**非对称身份验证**场景，例如 FIX API，或支持 `RSA` 和 `Ed25519` 签名的 REST / WebSocket
API。

如需查看源代码、版本发布及更新说明，请访问 GitHub 上的
[asymmetric-key-generator](https://github.com/binance/asymmetric-key-generator) 仓库。

## 支持的密钥类型

该工具可生成以下密钥类型：

- **Ed25519**（PKCS#8）
- **RSA-2048**
- **RSA-4096**

> ⚠️ **重要提示**
>
> 部分 Binance API（例如 FIX API）**要求使用 Ed25519 密钥**。 `RSA` 密钥仅受明确支持 `RSA`
> 身份验证的 API 支持。

## 支持的环境

- 桌面环境（macOS、Windows、Linux），通过预构建应用程序使用
- Node.js（用于命令行及本地构建）

## 安装方式

您可以通过以下**三种方式**使用该工具，请根据您的工作流选择合适的方式。

### 方式一：下载预构建应用程序（推荐）

预构建的桌面应用程序可在
[GitHub Releases 页面](https://github.com/binance/asymmetric-key-generator/releases)下载。下载后，请使用提供的校验和验证包的完整性：

```bash
sha256sum -c AsymmetricKeyGenerator-<version>.CHECKSUM
```

验证成功后，输出结果将显示 OK。

### 方式二：从源码构建

克隆仓库并在本地构建应用程序：

```bash
npm install
npm run start      # 本地运行
npm run dist       # 将构建产物输出至 dist 文件夹
```

### 方式三：命令行使用

该生成器也可作为命令行工具使用。

安装依赖：

```bash
npm install
```

生成密钥对：

```bash
npm run generate -- -k <key-type> -p <passphrase> -n <count> -o <output>
```

示例

生成单个 `RSA-2048` 密钥对：

```bash
npm run generate -- -k rsa-2048 -o id_rsa.tar.gz
```

使用密码短语生成两个 `Ed25519` 密钥对：

```bash
npm run generate -- -k ed25519 -p mySecretPassphrase -n 2
```

## 界面使用说明

桌面应用程序提供简洁的图形界面：

1. 打开应用程序
2. 选择密钥类型（大多数情况下推荐使用 `Ed25519`）
3. 点击 Generate Key Pair（生成密钥对）
4. 安全保存私钥（切勿分享）
5. 保存公钥以备上传或按需分发

## 典型使用场景

- 为 Binance FIX API 生成 `Ed25519` 密钥
- 为支持非对称身份验证的 REST 或 WebSocket API 生成 `RSA` 密钥
- 安全轮换 API 凭证
- 本地开发和测试已签名的 API 请求

## 安全最佳实践

- 切勿分享您的私钥
- 将私钥安全存储在磁盘或密钥管理工具中
- 在支持的情况下使用密码短语
- 仅将公钥上传至 Binance
- 定期轮换密钥并撤销未使用的凭证