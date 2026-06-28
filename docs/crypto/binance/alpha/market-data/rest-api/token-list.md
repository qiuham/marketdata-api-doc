---
exchange: binance
source_url: https://developers.binance.com/docs/alpha/market-data/rest-api/token-list
api_type: Market Data
updated_at: 2026-01-15T23:50:43.921408
---

# Token List

## Endpoint: /bapi/defi/v1/public/wallet-direct/buw/wallet/cex/alpha/all/token/list[​](/docs/alpha/market-data/rest-api/token-list#endpoint-bapidefiv1publicwallet-directbuwwalletcexalphaalltokenlist "Direct link to Endpoint: /bapi/defi/v1/public/wallet-direct/buw/wallet/cex/alpha/all/token/list")

## Full URL[​](/docs/alpha/market-data/rest-api/token-list#full-url "Direct link to Full URL")

<https://www.binance.com/bapi/defi/v1/public/wallet-direct/buw/wallet/cex/alpha/all/token/list>

## Description[​](/docs/alpha/market-data/rest-api/token-list#description "Direct link to Description")

Retrieves a list of all available ALPHA tokens, including their IDs and symbols. Use this to find the token ID for constructing symbols in other endpoints.

## Parameters[​](/docs/alpha/market-data/rest-api/token-list#parameters "Direct link to Parameters")

None

## Response Structure[​](/docs/alpha/market-data/rest-api/token-list#response-structure "Direct link to Response Structure")

  * `code`: String (e.g., 000000 for success)
  * `message`: String (e.g., "success")
  * `data`: Array of objects, each representing a token with fields like: 
    * `alphaId`: Integer (alpha ID, e.g., ALPHA_175)
    * `symbol`: String (token symbol, e.g., "USDT")
    * `name`: String (full name, e.g., "USDT")
    * `chainId`: String (chain id)
    * `contractAddress`: String (contract address)
    * Other fields: May include decimals, network info, etc.



## Example Usage[​](/docs/alpha/market-data/rest-api/token-list#example-usage "Direct link to Example Usage")

Call this first to map symbol names to ALPHA token IDs.

---

# Token列表

## 接口：/bapi/defi/v1/public/wallet-direct/buw/wallet/cex/alpha/all/token/list[​](/docs/zh-CN/alpha/market-data/rest-api/token-list#接口bapidefiv1publicwallet-directbuwwalletcexalphaalltokenlist "接口：/bapi/defi/v1/public/wallet-direct/buw/wallet/cex/alpha/all/token/list的直接链接")

## 完整URL[​](/docs/zh-CN/alpha/market-data/rest-api/token-list#完整url "完整URL的直接链接")

<https://www.binance.com/bapi/defi/v1/public/wallet-direct/buw/wallet/cex/alpha/all/token/list>

## 描述[​](/docs/zh-CN/alpha/market-data/rest-api/token-list#描述 "描述的直接链接")

获取所有可用ALPHA代币的列表，包括它们的ID和符号。用于在其它接口构造symbol参数时查找代币ID。

## 参数[​](/docs/zh-CN/alpha/market-data/rest-api/token-list#参数 "参数的直接链接")

无

## 响应结构[​](/docs/zh-CN/alpha/market-data/rest-api/token-list#响应结构 "响应结构的直接链接")

  * `code`：字符串（例如，000000表示成功）
  * `message`：字符串（例如，“success”）
  * `data`：对象数组，每个对象代表一个代币，包含字段： 
    * `alphaId`：整数（ALPHA代币ID，例如ALPHA_175）
    * `symbol`：字符串（代币符号，例如“USDT”）
    * `name`：字符串（代币全名，例如“USDT”）
    * `chainId`: 字符串 (链ID)
    * `contractAddress`: 字符串 (合约地址)
    * 其他字段：可能包括小数位、网络信息等。



## 使用示例[​](/docs/zh-CN/alpha/market-data/rest-api/token-list#使用示例 "使用示例的直接链接")

先调用此接口以映射代币符号到ALPHA代币ID。