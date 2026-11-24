---
exchange: bitget
source_url: https://www.bitget.com/docs/classic/sdk/golang
api_type: Guide
updated_at: 2026-11-24 19:00:25.505712
---

# Golang

Official Golang SDK for the Bitget API.

**Code path**:`pkg/client/v2`

## Install

```bash
git clone https://github.com/BitgetLimited/v3-bitget-api-sdk.git
cd bitget-golang-sdk-api
```

## Usage

Initialize a client and call an endpoint:

```go
client := new(v1.MixOrderClient).Init()
resp, err := client.PlaceOrder(params)
```

More: [Golang SDK](https://github.com/BitgetLimited/v3-bitget-api-sdk/tree/master/bitget-golang-sdk-api)

---

# Golang

Bitget 官方 Golang SDK。

**代码路径**：`pkg/client/v2`

## 安装

```bash
git clone https://github.com/BitgetLimited/v3-bitget-api-sdk.git
cd bitget-golang-sdk-api
```

## 使用

Initialize a client and call an endpoint:

```go
client := new(v1.MixOrderClient).Init()
resp, err := client.PlaceOrder(params)
```

更多：[Golang SDK](https://github.com/BitgetLimited/v3-bitget-api-sdk/tree/master/bitget-golang-sdk-api)