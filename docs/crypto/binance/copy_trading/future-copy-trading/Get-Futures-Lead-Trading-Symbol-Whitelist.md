---
exchange: binance
source_url: https://developers.binance.com/docs/copy_trading/future-copy-trading/Get-Futures-Lead-Trading-Symbol-Whitelist
api_type: REST
updated_at: 2026-06-28 18:55:19.500929
---

# Quick Start

## API Key Setup[​](/docs/copy_trading/quick-start#api-key-setup "Direct link to API Key Setup")

  * Some endpoints will require an API Key. Please refer to [this page](https://www.binance.com/en/support/articles/360002502072) regarding API key creation.
  * Once API key is created, it is recommended to set IP restrictions on the key for security reasons.
  * **Never share your API key/secret key to ANYONE.**

If the API keys were accidentally shared, please delete them immediately and create a new key. 

## API Key Restrictions[​](/docs/copy_trading/quick-start#api-key-restrictions "Direct link to API Key Restrictions")

  * After creating the API key, the default restrictions is `Enable Reading`.
  * To **enable withdrawals via the API** , the API key restriction needs to be modified through the Binance UI.



## Enabling Accounts[​](/docs/copy_trading/quick-start#enabling-accounts "Direct link to Enabling Accounts")

### Spot Account[​](/docs/copy_trading/quick-start#spot-account "Direct link to Spot Account")

A `SPOT` account is provided by default upon creation of a Binance Account.

### Margin Account[​](/docs/copy_trading/quick-start#margin-account "Direct link to Margin Account")

To enable a `MARGIN` account for Margin Trading, please refer to the [Margin Trading Guide](https://www.binance.vision/tutorials/binance-margin-trading-guide)

## API Library[​](/docs/copy_trading/quick-start#api-library "Direct link to API Library")

### Python connector[​](/docs/copy_trading/quick-start#python-connector "Direct link to Python connector")

This is a lightweight library that works as a connector to Binance public API, written in Python.

<https://github.com/binance/binance-connector-python>

### Javascript connector[​](/docs/copy_trading/quick-start#javascript-connector "Direct link to Javascript connector")

This is a lightweight library that works as a connector to Binance public API, written for JavaScript users.

<https://github.com/binance/binance-connector-js>

### Ruby connector[​](/docs/copy_trading/quick-start#ruby-connector "Direct link to Ruby connector")

This is a lightweight library that works as a connector to Binance public API, written for Ruby users.

<https://github.com/binance/binance-connector-ruby>

### DotNET connector[​](/docs/copy_trading/quick-start#dotnet-connector "Direct link to DotNET connector")

This is a lightweight library that works as a connector to Binance public API, written for C# users.

<https://github.com/binance/binance-connector-dotnet>

### Java connector[​](/docs/copy_trading/quick-start#java-connector "Direct link to Java connector")

This is a lightweight library that works as a connector to Binance public API, written for Java users.

<https://github.com/binance/binance-connector-java>

### Postman Collections[​](/docs/copy_trading/quick-start#postman-collections "Direct link to Postman Collections")

There is now a Postman collection containing the API endpoints for quick and easy use.

This is recommended for new users who want to get a quick-start into using the API.

For more information please refer to this page: [Binance API Postman](https://github.com/binance/binance-api-postman)

### Swagger[​](/docs/copy_trading/quick-start#swagger "Direct link to Swagger")

A YAML file with OpenAPI specification on the RESTful API is available to be used, as well as a Swagger UI page for the consulting.

<https://github.com/binance/binance-api-swagger>

---

# 快速开始

## API Key 权限设置[​](/docs/zh-CN/copy_trading/quick-start#api-key-权限设置 "API Key 权限设置的直接链接")

  * 新创建的API的默认权限是 `只读`。
  * 如果需要通过API提款, 需要在UI修改权限, 选中 `允许提现`。



## 账户[​](/docs/zh-CN/copy_trading/quick-start#账户 "账户的直接链接")

### 现货账户[​](/docs/zh-CN/copy_trading/quick-start#现货账户 "现货账户的直接链接")

新注册的币安账号都会有一个现货(`SPOT`)账号。

### 杠杆账户[​](/docs/zh-CN/copy_trading/quick-start#杠杆账户 "杠杆账户的直接链接")

为了开设杠杆(`MARGIN`)账户, 可以参考[Binance杠杆交易账户设置指南](https://www.binance.vision/zh/tutorials/binance-margin-trading-guide)

## API 代码库[​](/docs/zh-CN/copy_trading/quick-start#api-代码库 "API 代码库的直接链接")

### Connectors[​](/docs/zh-CN/copy_trading/quick-start#connectors "Connectors的直接链接")

以下有一些轻量级的代码库，使不同语言的用户能够直接调用现货的 Binance 公共 API：

  * Python <https://github.com/binance/binance-connector-python>
  * JavaScript <https://github.com/binance/binance-connector-js>
  * Ruby <https://github.com/binance/binance-connector-ruby>
  * DotNET C# <https://github.com/binance/binance-connector-dotnet>
  * Java <https://github.com/binance/binance-connector-java>
  * Rust <https://github.com/binance/binance-spot-connector-rust>
  * PHP <https://github.com/binance/binance-connector-php>
  * Go <https://github.com/binance/binance-connector-go>



### Postman Collections[​](/docs/zh-CN/copy_trading/quick-start#postman-collections "Postman Collections的直接链接")

Postman 集合现已推出。推荐给寻求快速和轻松地开始使用 API 的新用户。

<https://github.com/binance/binance-api-postman>

### Swagger[​](/docs/zh-CN/copy_trading/quick-start#swagger "Swagger的直接链接")

以下有提供包含 RESTful API 的 OpenAPI 规范的 YAML 文件，以及可供参考的 Swagger UI 页面。

<https://github.com/binance/binance-api-swagger>