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
source_url: 'https://docs.polymarket.com/cn/api-reference/rfq-trades/authentication'
updated_at: 2026-11-13
---

# 身份验证

> 使用你的合作伙伴 API 密钥签署每个 RFQ 交易合作伙伴 API 请求，以及交易状态流的握手请求。

每个请求都使用你的合作伙伴 API 密钥签名。Polymarket 仅根据密钥识别你的平台，从不依据请求体，因此请求只能读取和创建你自己的交易。

API 密钥用于识别你的平台，但不授权转移资金：每个交易对手方通过其[订单签名](https://docs.polymarket.com/partners/rfq-trades.md#sign-the-orders)授权自己的一方。

## 你的 API 密钥

Polymarket 在合作伙伴接入时为每个合作伙伴签发 API 密钥：

* **密钥 ID**：公开部分，随每个请求发送。
* **Secret**：base64url 编码的字符串，通过安全渠道一次性提供。用作 HMAC 密钥前，请先将其解码为字节。

## 签署请求

除 `GET /v1/time` 外，每个请求都需要签名：

**1. 创建请求时间戳**

首先，为每个请求创建一个以秒为单位的新 Unix 时间戳。它与服务器时间的偏差必须在 30 秒以内，无论偏快还是偏慢。请参阅[保持时钟同步](#保持时钟同步)。

**2. 创建请求签名**

然后，将时间戳、大写 HTTP 方法、请求路径和实际发送的序列化请求体直接连接，不加分隔符。再使用经 base64url 解码的 API 密钥 secret 对结果签名：

```text theme={null}
rfq_timestamp = <unix_seconds>
method = "POST"
request_path = "/v1/rfq-trades/validate"
body = <exact_serialized_request_body>

message = rfq_timestamp + method + request_path + body
rfq_signature = urlsafeBase64WithPadding(
  HMAC-SHA256(base64UrlDecode(<rfq_secret>), message)
)
```

其中：

* `request_path` 仅为 URL 路径，查询字符串不参与签名。
* `body` 是实际发送的字节。`GET` 请求的请求体为空。请只序列化一次请求体，并在签名和请求中复用同一字符串，以避免键顺序或空白字符导致的不一致。
* `rfq_signature` 使用**带填充**的 base64url 编码（RFC 4648 §5），不是十六进制，也不是标准 base64。

以下辅助函数为请求生成三个请求头：

```typescript TypeScript theme={null}
import { createHmac } from "node:crypto";

const keyId = process.env.RFQ_KEY_ID!;
const secret = Buffer.from(process.env.RFQ_SECRET!, "base64url");

function signRequest(method: string, path: string, body = "") {
  const timestamp = Math.floor(Date.now() / 1000).toString();
  const signature = createHmac("sha256", secret)
    .update(timestamp + method.toUpperCase() + path + body)
    .digest("base64") // Node's "base64url" digest drops the padding.
    .replace(/\+/g, "-")
    .replace(/\//g, "_");

  return {
    "RFQ-Key-Id": keyId,
    "RFQ-Timestamp": timestamp,
    "RFQ-Signature": signature,
  };
}

const body = JSON.stringify({ marketId: "253591" /* ... */ });
await fetch(
  "https://external-rfq-partner.polymarket.com/v1/rfq-trades/validate",
  {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      ...signRequest("POST", "/v1/rfq-trades/validate", body),
    },
    body,
  },
);
```

```python Python theme={null}
import base64
import hashlib
import hmac
import os
import time

KEY_ID = os.environ["RFQ_KEY_ID"]
SECRET = base64.urlsafe_b64decode(os.environ["RFQ_SECRET"])


def sign_request(method: str, path: str, body: bytes = b"") -> dict[str, str]:
    timestamp = str(int(time.time()))
    message = timestamp.encode() + method.upper().encode() + path.encode() + body
    digest = hmac.new(SECRET, message, hashlib.sha256).digest()
    return {
        "RFQ-Key-Id": KEY_ID,
        "RFQ-Timestamp": timestamp,
        "RFQ-Signature": base64.urlsafe_b64encode(digest).decode(),
    }
```

> [accordion] 测试向量
>
> 使用以下输入检查你的实现：
>
> | 输入 | 值 |
> | - | - |
> | Secret（base64url） | `MDEyMzQ1Njc4OWFiY2RlZjAxMjM0NTY3ODlhYmNkZWY=` |
> | `RFQ-Timestamp` | `1753185296` |
> | 方法 | `POST` |
> | 路径 | `/v1/rfq-trades/validate` |
> | 请求体 | `{"marketId":"253591"}` |
> | 预期的 `RFQ-Signature` | `H-yYb9AqRHJ7ysPVyqTxdT83YWWUB8KvS4okVchrrcU=` |

**3. 发送经过身份验证的请求**

最后，将密钥 ID、时间戳和签名作为请求头发送。此请求用于验证一笔交易的条款：

```bash theme={null}
curl -X POST "https://external-rfq-partner.polymarket.com/v1/rfq-trades/validate" \
  -H "Content-Type: application/json" \
  -H "RFQ-Key-Id: <rfq_key_id>" \
  -H "RFQ-Timestamp: <rfq_timestamp>" \
  -H "RFQ-Signature: <rfq_signature>" \
  --data '{
    "marketId": "253591",
    "operation": "split",
    "price": "0.65",
    "shares": "1500000000",
    "parties": {
      "yes": { "maker": "<yes_deposit_wallet>", "signatureType": 3 },
      "no": { "maker": "<no_deposit_wallet>", "signatureType": 3 }
    }
  }'
```

每个经过身份验证的请求都使用相同的三个请求头：

| 请求头 | 值 |
| - | - |
| `RFQ-Key-Id` | 你的 API 密钥 ID |
| `RFQ-Timestamp` | 用于构建签名的 Unix 时间戳 |
| `RFQ-Signature` | 上一步生成的签名 |

## 保持时钟同步

`RFQ-Timestamp` 与服务器时间的偏差必须在 30 秒以内，无论偏快还是偏慢。请通过 NTP 保持时钟同步。如果请求开始返回 `401`，请将你的时钟与服务器时钟比较：`GET /v1/time` 无需身份验证。

```bash theme={null}
curl "https://external-rfq-partner.polymarket.com/v1/time"
```

响应体返回服务器时间：

```json theme={null}
{ "serverTime": "2026-07-24T12:34:56Z", "timestamp": 1784896496 }
```

`timestamp` 是以 Unix 秒表示的服务器时间，格式与 `RFQ-Timestamp` 相同。

## WebSocket 身份验证

交易状态流只在升级请求时进行一次身份验证。像任何 `GET` 请求一样签名（请求体为空），并在握手时发送相同的三个请求头：

```text theme={null}
message = <rfq_timestamp> + "GET" + "/v1/ws/rfq-trades"
```

之后，该流只推送你自己的交易。请参阅[跟踪交易](https://docs.polymarket.com/partners/rfq-trades.md#track-the-trade)。

## 身份验证错误

身份验证失败的请求返回 `401`，错误码为 `authentication_failed`。缺少请求头、时间戳不是整数 Unix 秒、时间戳超出 30 秒窗口，这几种情况各有不同的错误消息。出于安全考虑，未知或已撤销的密钥 ID 与签名不匹配共用同一条通用消息。


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
