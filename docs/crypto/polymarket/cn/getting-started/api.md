---
api_type: reference
source_type: llms_txt
version: ''
scope: crypto
asset_class: prediction_market
domain: exchanges
provider: polymarket
provider_name: Polymarket
product: api
product_id: polymarket
source_url: 'https://docs.polymarket.com/cn/getting-started/api'
updated_at: 2026-11-13
---

# API

> 直接使用 Polymarket REST API 和 WebSocket 流进行构建。

Polymarket API 提供对 Polymarket 平台的编程访问。
每个 API 负责集成流程中的不同部分。

## 集成接口

> [tab] REST APIs
>
> > [card] Gamma API
> >
> > **`https://gamma-api.polymarket.com`**
> >
> > 发现事件和市场，并检索与其交互所需的元数据。
>
> > [card] CLOB API
> >
> > **`https://clob.polymarket.com`**
> >
> > 读取价格和订单簿，然后下单和管理订单。
>
> > [card] [Data API](https://docs.polymarket.com/cn/api-reference/data-api/overview.md)
> >
> > **`https://data-api.polymarket.com`**
> >
> > 通过游标分页与统一的响应结构，分析持仓、活动和市场参与情况。
>
> > [card] Relayer API
> >
> > **`https://relayer-v2.polymarket.com`**
> >
> > 提交钱包交易，无需账户持有 POL 支付 Gas 费。

> [tab] WebSocket API
>
> > [card] [CLOB 市场频道](https://docs.polymarket.com/cn/market-data/realtime-data.md#市场数据流)
> >
> > **`wss://ws-subscriptions-clob.polymarket.com/ws/market`**
> >
> > 关注公开订单簿、价格和市场生命周期更新。
>
> > [card] [CLOB 用户频道](https://docs.polymarket.com/cn/trading/realtime-order-updates.md#用户流)
> >
> > **`wss://ws-subscriptions-clob.polymarket.com/ws/user`**
> >
> > 关注账户中经过身份验证的订单和交易更新。
>
> > [card] [RTDS](https://docs.polymarket.com/cn/market-data/realtime-data.md)
> >
> > **`wss://ws-live-data.polymarket.com`**
> >
> > 流式传输公开参考价格、评论和交易活动。
>
> > [card] [体育 WebSocket](https://docs.polymarket.com/cn/market-data/realtime-data.md#体育数据流)
> >
> > **`wss://sports-api.polymarket.com/ws`**
> >
> > 关注公开的比赛状态和比分。

## 何时使用 API

在以下情况下使用直接集成：

* 官方 SDK 不支持您的运行环境。
* 您需要精确控制请求签名、请求头、重试或传输。
* 您需要 SDK 尚未提供的端点或传输格式。

SDK 为 Polymarket 提供了统一的、强类型的接口，并处理分页、错误处理和钱包设置等常见集成问题。

> [!WARNING]
>
> 手动签署订单或直接调用合约时，必须先识别市场的持仓系统。请使用匹配的交易所、签名域、授权目标和持仓路径。不要只根据
> `positionIds` 推断路径，因为 CTF 市场在被其他工作流引用时也可能包含 Position
> ID。

## 发起公开请求

公开市场数据无需凭据即可获取。例如，从 Gamma API 列出活跃市场：

```bash theme={null}
curl -G "https://gamma-api.polymarket.com/markets" \
  --data-urlencode "closed=false" \
  --data-urlencode "limit=5"
```

响应是市场对象数组。以下示例展示了将每个结果与其资产 ID 对应时需要的字段：

```json Polymarket V2 theme={null}
[
  {
    "outcomes": "[\"Yes\", \"No\"]",
    "positionIds": "[\"<yes_position_id>\", \"<no_position_id>\"]"
  }
]
```

```json CTF theme={null}
[
  {
    "outcomes": "[\"Yes\", \"No\"]",
    "clobTokenIds": "[\"<yes_token_id>\", \"<no_token_id>\"]"
  }
]
```

> [!NOTE]
>
> 结果 ID 用于标识可交易的 YES 或 NO 余额。Gamma 在 `clobTokenIds` 中返回 CTF
> 结果 ID，在 `positionIds` 中返回 Polymarket Protocol V2 Position
> ID。这些字段是 JSON 编码数组。解析后，`outcomes[i]` 与相同索引处的 ID
> 对应。一个市场可能同时包含两组
> ID，因此不能仅根据字段是否存在来识别持仓系统。选择匹配的路径后，以字符串形式将资产
> ID 传给后续的价格、订单簿和订单请求。

## 身份验证

CLOB 身份验证包含两个层级：

| 层级 | 工作原理 | 目的 |
| - | - | - |
| L1 | 钱包对 EIP-712 消息进行签名 | 建立钱包控制权并创建或派生凭据 |
| L2 | 使用 API 凭据通过 HMAC-SHA256 对请求进行签名 | 验证私有 CLOB 请求 |

提交订单时，使用 L2 对请求进行身份验证，并使用钱包签名授权订单本身。

要验证私有 CLOB 请求，请遵循以下步骤：

**1. 创建 L1 类型化数据**

构建 `ClobAuth` 类型化数据负载。

```json clobAuthTypedData theme={null}
{
  "domain": {
    "name": "ClobAuthDomain",
    "version": "1",
    "chainId": 137
  },
  "types": {
    "ClobAuth": [
      { "name": "address", "type": "address" },
      { "name": "timestamp", "type": "string" },
      { "name": "nonce", "type": "uint256" },
      { "name": "message", "type": "string" }
    ]
  },
  "primaryType": "ClobAuth",
  "message": {
    "address": "<signer_address>",
    "timestamp": "<unix_seconds>",
    "nonce": "<nonce>",
    "message": "This message attests that I control the given wallet"
  }
}
```

提供以下值：

| 占位符 | 值 |
| - | - |
| `<signer_address>` | 由签名私钥控制的 Polygon 地址 |
| `<unix_seconds>` | 当前 Unix 时间戳（秒） |
| `<nonce>` | 凭据 nonce；除非管理多组凭据，否则使用 `0` |

**2. 创建 CLOB L1 签名**

使用控制 `<signer_address>` 的私钥对 `clobAuthTypedData` 进行签名。本示例使用 Viem。

```ts theme={null}
import { privateKeyToAccount } from "viem/accounts";

const signer = privateKeyToAccount("<SIGNER_PRIVATE_KEY>");
const clobL1Signature = await signer.signTypedData(clobAuthTypedData);
```

返回的 `clobL1Signature` 是该负载的 L1 签名。

**3. 创建或派生 CLOB API 凭证**

使用步骤 1 中的签名者地址、时间戳和 nonce，结合步骤 2 中的签名来创建凭证。如果该地址和 nonce 已有凭证，则直接派生它们。

```bash Create theme={null}
curl -X POST "https://clob.polymarket.com/auth/api-key" \
  -H "POLY_ADDRESS: <signer_address>" \
  -H "POLY_SIGNATURE: <clob_l1_signature>" \
  -H "POLY_TIMESTAMP: <unix_seconds>" \
  -H "POLY_NONCE: <nonce>"
```

```bash Derive theme={null}
curl "https://clob.polymarket.com/auth/derive-api-key" \
  -H "POLY_ADDRESS: <signer_address>" \
  -H "POLY_SIGNATURE: <clob_l1_signature>" \
  -H "POLY_TIMESTAMP: <unix_seconds>" \
  -H "POLY_NONCE: <nonce>"
```

响应包含用于 L2 认证的三个值：

```json Response theme={null}
{
  "apiKey": "<clob_api_key>",
  "secret": "<clob_api_secret>",
  "passphrase": "<clob_api_passphrase>"
}
```

```json Example theme={null}
{
  "apiKey": "7b1e2d60-6f9a-4dd7-8f3e-21b8f94c77a2",
  "secret": "Rnl2cWN0Rk5…c1ZzR1E9PQ==",
  "passphrase": "9fH3kL7m…2qW8xP4r"
}
```

| 字段 | 含义 |
| - | - |
| `apiKey` | API 凭证的唯一标识符 |
| `secret` | 用于通过 HMAC-SHA256 签署 L2 请求的 Base64 编码密钥 |
| `passphrase` | 通过 `POLY_PASSPHRASE` 请求头发送的凭证值 |

**4. 创建 CLOB L2 签名**

为需要身份验证的请求创建一个以秒为单位的新 Unix 时间戳。依次连接时间戳、大写 HTTP 方法、路由路径和与实际发送内容完全一致的序列化请求体，然后使用 API 凭证 `secret` 对结果进行签名。

示例请求使用 `GET /data/orders`，该请求没有主体：

```text theme={null}
clob_request_timestamp = <unix_seconds>
method = "GET"
request_path = "/data/orders"

message = clob_request_timestamp + method + request_path
clob_l2_signature = urlsafeBase64WithPadding(
  HMAC-SHA256(base64Decode(<clob_api_secret>), message)
)
```

对于包含请求体的请求，追加实际通过网络发送的序列化请求体。

**5. 发送经过身份验证的请求**

使用第 4 步中的时间戳和 L2 签名，以及第 3 步中的签名者地址和 API 凭据。此请求用于获取账户的未平仓订单。

```bash theme={null}
curl "https://clob.polymarket.com/data/orders" \
  -H "POLY_ADDRESS: <signer_address>" \
  -H "POLY_SIGNATURE: <clob_l2_signature>" \
  -H "POLY_TIMESTAMP: <clob_request_timestamp>" \
  -H "POLY_API_KEY: <clob_api_key>" \
  -H "POLY_PASSPHRASE: <clob_api_passphrase>"
```

L2 身份验证的 CLOB 请求使用相同的五个标头：

| 请求头 | 值 |
| - | - |
| `POLY_ADDRESS` | Polygon 签名者地址 |
| `POLY_SIGNATURE` | 第 4 步中的 HMAC-SHA256 签名 |
| `POLY_TIMESTAMP` | 用于构建签名的 Unix 时间戳 |
| `POLY_API_KEY` | API 凭据的 `apiKey` 值 |
| `POLY_PASSPHRASE` | API 凭据的 `passphrase` 值 |

## 后续步骤

> [card] [读取市场数据](https://docs.polymarket.com/cn/market-data/overview.md)
>
> 发现市场，并使用价格、订单簿和历史数据。

> [card] [订阅实时更新](https://docs.polymarket.com/cn/market-data/realtime-data.md)
>
> 实时流式传输市场和账户更新。

> [card] [下第一笔订单](https://docs.polymarket.com/cn/trading/quickstart.md)
>
> 设置账户并完成您的第一笔经过身份验证的交易。


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
