---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/copy-trading/quick-start
api_type: REST
updated_at: 2026-11-13 20:31:05.857948
---

# Quick Start

## API Key Setup

  * Some endpoints will require an API Key. Please refer to [this page](https://www.binance.com/en/support/articles/360002502072) regarding API key creation.
  * Once API key is created, it is recommended to set IP restrictions on the key for security reasons.
  * **Never share your API key/secret key to ANYONE.**



## API Key Restrictions

  * After creating the API key, the default restrictions is `Enable Reading`.
  * To **enable withdrawals via the API** , the API key restriction needs to be modified through the Binance UI.



## Enabling Accounts

### Spot Account

A `SPOT` account is provided by default upon creation of a Binance Account.

### Margin Account

To enable a `MARGIN` account for Margin Trading, please refer to the [Margin Trading Guide](https://www.binance.vision/tutorials/binance-margin-trading-guide)

## API Library

### Python connector

This is a lightweight library that works as a connector to Binance public API, written in Python.

<https://github.com/binance/binance-connector-python>

### Javascript connector

This is a lightweight library that works as a connector to Binance public API, written for JavaScript users.

<https://github.com/binance/binance-connector-js>

### Ruby connector

This is a lightweight library that works as a connector to Binance public API, written for Ruby users.

<https://github.com/binance/binance-connector-ruby>

### DotNET connector

This is a lightweight library that works as a connector to Binance public API, written for C# users.

<https://github.com/binance/binance-connector-dotnet>

### Java connector

This is a lightweight library that works as a connector to Binance public API, written for Java users.

<https://github.com/binance/binance-connector-java>

### Postman Collections

There is now a Postman collection containing the API endpoints for quick and easy use.

This is recommended for new users who want to get a quick-start into using the API.

For more information please refer to this page: [Binance API Postman](https://github.com/binance/binance-api-postman)

### Swagger

A YAML file with OpenAPI specification on the RESTful API is available to be used, as well as a Swagger UI page for the consulting.

<https://github.com/binance/binance-api-swagger>

Was this page helpful?

Last modified on November 12, 2026

[General Info](/en/docs/products/copy-trading/general-info)[Error Codes](/en/docs/products/copy-trading/error-code)

---

# 快速开始

## API Key 权限设置

  * 新创建的API的默认权限是 `只读`。
  * 如果需要通过API提款, 需要在UI修改权限, 选中 `允许提现`。



## 账户

### 现货账户

新注册的币安账号都会有一个现货(`SPOT`)账号。

### 杠杆账户

为了开设杠杆(`MARGIN`)账户, 可以参考[Binance杠杆交易账户设置指南](https://www.binance.vision/zh/tutorials/binance-margin-trading-guide)

## API 代码库

### Connectors

以下有一些轻量级的代码库，使不同语言的用户能够直接调用现货的 Binance 公共 API：

  * Python <https://github.com/binance/binance-connector-python>
  * JavaScript <https://github.com/binance/binance-connector-js>
  * Ruby <https://github.com/binance/binance-connector-ruby>
  * DotNET C# <https://github.com/binance/binance-connector-dotnet>
  * Java <https://github.com/binance/binance-connector-java>
  * Rust <https://github.com/binance/binance-spot-connector-rust>
  * PHP <https://github.com/binance/binance-connector-php>
  * Go <https://github.com/binance/binance-connector-go>



### Postman Collections

Postman 集合现已推出。推荐给寻求快速和轻松地开始使用 API 的新用户。

<https://github.com/binance/binance-api-postman>

### Swagger

以下有提供包含 RESTful API 的 OpenAPI 规范的 YAML 文件，以及可供参考的 Swagger UI 页面。

<https://github.com/binance/binance-api-swagger>

此页面是否有帮助？

Last modified on November 12, 2026

[基本信息](/zh-CN/docs/products/copy-trading/general-info)[错误代码](/zh-CN/docs/products/copy-trading/error-code)