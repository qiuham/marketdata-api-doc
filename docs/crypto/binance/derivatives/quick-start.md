---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/quick-start
api_type: REST
updated_at: 2026-05-27 18:55:51.918261
---

# Quick Start

## API Key Setup[​](/docs/derivatives/quick-start#api-key-setup "Direct link to API Key Setup")

  * Some endpoints will require an API Key. Please refer to [this page](https://www.binance.com/en/support/faq/how-to-create-api-keys-on-binance-360002502072) regarding API key creation.
  * Once API key is created, it is recommended to set IP restrictions on the key for security reasons.
  * **Never share your API key/secret key to ANYONE.**

If the API keys were accidentally shared, please delete them immediately and create a new key. 

## API Key Restrictions[​](/docs/derivatives/quick-start#api-key-restrictions "Direct link to API Key Restrictions")

  * After creating the API key, the default restrictions is `Enable Reading`.
  * To **enable withdrawals via the API** , the API key restriction needs to be modified through the Binance UI.



## Enabling Accounts[​](/docs/derivatives/quick-start#enabling-accounts "Direct link to Enabling Accounts")

### Account[​](/docs/derivatives/quick-start#account "Direct link to Account")

A `SPOT` account is provided by default upon creation of a Binance Account.

### Futures Account[​](/docs/derivatives/quick-start#futures-account "Direct link to Futures Account")

To enable a `FUTURES` account for Futures Trading, please refer to the [Futures Trading Guide](https://www.binance.com/en/support/faq/a-beginner-s-guide-to-futures-trading-website-360039304272)

### Futures Testnet[​](/docs/derivatives/quick-start#futures-testnet "Direct link to Futures Testnet")

Users can use the Futures Testnet to practice `FUTURES` trading.

Currently, this is only available via the API.

Please refer to the [Futures Testnet page](https://testnet.binancefuture.com/en/futures/BTCUSDT) for more information and how to set up the Testnet API key.

### Option Account[​](/docs/derivatives/quick-start#option-account "Direct link to Option Account")

To enable a `OPTION` account for Option Trading, please refer to the [Option Trading Guide](https://www.binance.com/en/support/faq/introduction-to-binance-options-374321c9317c473480243365298b8706)

## API Library[​](/docs/derivatives/quick-start#api-library "Direct link to API Library")

### Python connector[​](/docs/derivatives/quick-start#python-connector "Direct link to Python connector")

This is a lightweight library that works as a connector to Binance public API, written in Python.

<https://github.com/binance/binance-connector-python>

### Java connector[​](/docs/derivatives/quick-start#java-connector "Direct link to Java connector")

This is a lightweight library that works as a connector to Binance public API, written for Java users.

<https://github.com/binance/binance-connector-java>

---

# 快速开始

## API Key 权限设置[​](/docs/zh-CN/derivatives/quick-start#api-key-权限设置 "API Key 权限设置的直接链接")

  * 新创建的API的默认权限是 `只读`。
  * 如果需要通过API提款, 需要在UI修改权限, 选中 `允许提现`。
  * 如果需要通过API交易, 需要在UI修改权限, 选中对应交易权限



## 账户[​](/docs/zh-CN/derivatives/quick-start#账户 "账户的直接链接")

### 现货账户[​](/docs/zh-CN/derivatives/quick-start#现货账户 "现货账户的直接链接")

新注册的币安账号都会有一个现货(`SPOT`)账号。

### 期货账户[​](/docs/zh-CN/derivatives/quick-start#期货账户 "期货账户的直接链��接")

为了开设期货(`FUTURES`)账户, 可以参考[币安期权介绍](https://www.binance.com/zh-CN/support/faq/%E6%95%B0%E5%AD%97%E8%B4%A7%E5%B8%81%E8%A1%8D%E7%94%9F%E5%93%81?c=4&navId=4#18-36)

### 期货测试网[​](/docs/zh-CN/derivatives/quick-start#期货测试网 "期货测试网的直接链接")

用户可以使用期货的测试网来体验`FUTURES`交易. 现在只能通过API来交易。

更多信息请参考[期货测试网](https://testnet.binancefuture.com/en/futures/BTCUSDT)。

### 期权账户[​](/docs/zh-CN/derivatives/quick-start#期权账户 "期权账户的直接链接")

为了开设期权(`OPTION`)账户, 可以参考[Binance期权概览](https://www.binance.com/zh-CN/support/faq/%E5%B9%A3%E5%AE%89%E6%9C%9F%E6%AC%8A%E6%A6%82%E8%A6%BD-374321c9317c473480243365298b8706)

## API 代码库[​](/docs/zh-CN/derivatives/quick-start#api-代码库 "API 代码库的直接链接")

### Python connector[​](/docs/zh-CN/derivatives/quick-start#python-connector "Python connector的直接链接")

一个轻量级的Python代码库，提供让用户直接调用API的方法。支持所有合约的接口。

<https://github.com/binance/binance-connector-python>

### Java connector[​](/docs/zh-CN/derivatives/quick-start#java-connector "Java connector的直接链接")

一个轻量级的代码库，提供Java用户直接调用API的方法。支持所有合约的接口。

<https://github.com/binance/binance-connector-java>