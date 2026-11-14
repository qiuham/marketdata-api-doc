---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/spot/faqs/api_key_types
api_type: REST
updated_at: 2026-11-13 20:24:32.564850
---

# API Key Types

Binance APIs require an API key to access authenticated endpoints for trading, account history, etc.

We support several types of API keys:

  * Ed25519 (recommended)
  * HMAC
  * RSA



This document provides an overview of supported API keys.

**We recommend to use Ed25519 API keys** as it should provide the best performance and security out of all supported key types.

Read [REST API](/en/docs/products/spot/rest-api#signed-endpoint-security) or [WebSocket API](/en/docs/products/spot/web-socket-api#request-security) documentation to learn how to use different API keys.

### Ed25519

Ed25519 keys use asymmetric cryptography. You share your public key with Binance and use the private key to sign API requests. Binance API uses the public key to verify your signature.

Ed25519 keys provide security comparable to 3072-bit RSA keys, but with considerably smaller key, smaller signature size, and faster signature computation.

**We recommend to use Ed25519 API keys.**

Sample Ed25519 key:
    
    
    Code
    
    -----BEGIN PUBLIC KEY-----
    MCowBQYDK2VwAyEAgmDRTtj2FA+wzJUIlAL9ly1eovjLBu7uXUFR+jFULmg=
    -----END PUBLIC KEY-----

Sample Ed25519 signature:
    
    
    Code
    
    E7luAubOlcRxL10iQszvNCff+xJjwJrfajEHj1hOncmsgaSB4NE+A/BbQhCWwit/usNJ32/LeTwDYPoA7Qz4BA==

### HMAC

HMAC keys use symmetric cryptography. Binance generates and shares with you a secret key which you use to sign API requests. Binance API uses the same shared secret key to verify your signature.

HMAC signatures are quick to compute and compact.  However, the shared secret must be shared between multiple parties which is less secure than asymmetric cryptography used by Ed25519 or RSA keys.

**HMAC keys are deprecated.** We recommend to migrate to asymmetric API keys, such as Ed25519 or RSA.

Sample HMAC key:
    
    
    Code
    
    Fhs4lGae2qAi6VNjbJjebUAwXrIChb7mlf372UOICMwdKaNdNBGKtfdeUff2TTTT

Sample HMAC signature:
    
    
    Code
    
    7f3fc79c57d7a70d2b644ad4589672f4a5d55a62af2a336a0af7d4896f8d48b8

### RSA

RSA keys use asymmetric cryptography.  You share your public key with Binance and use the private key to sign API requests.  Binance API uses the public key to verify your signature.

We support 2048 and 4096 bit RSA keys.

While RSA keys are more secure than HMAC keys, RSA signatures are much larger than HMAC and Ed25519 which can lead to a degradation to performance.

Sample RSA key (2048 bits):
    
    
    Code
    
    -----BEGIN PUBLIC KEY-----
    MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAyfKiFXpcOhF5rX1XxePN
    akwN7Etwtn3v05cZNY+ftDHbVZHs/kY6Ruj5lhxVFAq5dv7Ba9/4jPijXuMuIc6Y
    8nUlqtrrxC8DEOAczw9SKATDYZN9nbLfYlbBFfHzRQUXdAtYCPI6XtxmJBS7aOBb
    4nZe1SVm+bhLrp0YQnx2P0s+37qkGeVn09m6w9MnWxjgCkkYFPWQkXIu5qOnwx6p
    NfqDmFD7d7dUc/6PZQ1bKFALu/UETsobmBk82ShbrBhlc0JXuhf9qBR7QASjHjFQ
    2N+VF2PfH8dm5prZIpz/MFKPkBW4Yuss0OXiD+jQt1J2JUKspLqsIqoXjHQQGjL7
    3wIDAQAB
    -----END PUBLIC KEY-----

Sample RSA signature (2048 bits):
    
    
    Code
    
    wS6q6h77AvH1TqwInoTDdWIIubRCiUP4RLG++GI24twL3BMtX0EEV+YT1eH8Hb8bLe0Rb9OhOHbt1CC3aurzoCTgZvhNek47mg+Bpu8fwQ7eRkXEiWBx5C8BNN73JwnnkZw4UzYvqiwAs162jToV8AL0eN043KJ3MEKCy3C6nyeYOFSg+1Cp637KtAZk3z7aHknSu7/PXSPuwMIpBgFctf8YKGZFAVRbgwlcgUDhXyaGts6OFePGy0jkZKJHawb/w5hoatatsfVmVC4hZ8fsfystQ9k5DNjTm7ROApWaXy9BsfAYcj13O424mqlpkKG4EGnIjOIWB/pRDDQEm2O/xg==

Was this page helpful?

Last modified on November 12, 2026

[Terms of Use](/en/docs/products/spot/demo-mode/DEMO-TERMS-OF-USE)[Commission Rates](/en/docs/products/spot/faqs/commission_faq)

---

# API Key 类型

币安 API 需要 API Key 才能访问经过身份验证的接口以进行交易，账户历史记录等。

我们支持多种类型的 API key：

  * Ed25519（推荐）
  * HMAC
  * RSA



本文档概述了受支持的 API Keys。

**我们建议使用 Ed25519 API keys** ，因为它在所有受支持的 API key 类型中提供最佳性能和安全性。

请读 [REST API](/zh-CN/docs/products/spot/rest-api#%E8%AF%B7%E6%B1%82%E9%89%B4%E6%9D%83%E7%B1%BB%E5%9E%8B) 或者 [WebSocket API](/zh-CN/docs/products/spot/web-socket-api#%E8%AF%B7%E6%B1%82%E9%89%B4%E6%9D%83%E7%B1%BB%E5%9E%8B) 文档以了解如何使用不同的 API Key 类型。

### Ed25519

Ed25519 keys 使用非对称加密技术。您只与币安共享您的 public key 并在本地使用 private key 签署 API 请求。币安 API 会使用 public key 来验证您的请求签名。

Ed25519 Keys 提供与 3072 bits 的 RSA keys 相当的安全性，但是 key 更小，签名更小，签名的计算更快。

**我们建议使用 Ed25519 API keys**

Ed25519 key 例子:
    
    
    Code
    
    -----BEGIN PUBLIC KEY-----
    MCowBQYDK2VwAyEAgmDRTtj2FA+wzJUIlAL9ly1eovjLBu7uXUFR+jFULmg=
    -----END PUBLIC KEY-----

Ed25519 签名例子:
    
    
    Code
    
    E7luAubOlcRxL10iQszvNCff+xJjwJrfajEHj1hOncmsgaSB4NE+A/BbQhCWwit/usNJ32/LeTwDYPoA7Qz4BA==

### HMAC

HMAC keys 使用对称加密技术。币安生成并与您共享一个 secret key，您可以使用该 secret key 对 API 请求进行签名。币安 API 使用相同的共享 secret key 来验证您的请求签名。

HMAC 签名可以快速计算和压缩。 但是，由于共享 secret key 必须在多方之间共享，这就不如 Ed25519 或 RSA keys 使用的非对称加密技术那么安全。

**不建议使用 HMAC keys。** 我们建议换成并使用非对称 API Keys，例如 Ed25519 或 RSA。

HMAC key 例子:
    
    
    Code
    
    Fhs4lGae2qAi6VNjbJjebUAwXrIChb7mlf372UOICMwdKaNdNBGKtfdeUff2TTTT

HMAC 签名例子:
    
    
    Code
    
    7f3fc79c57d7a70d2b644ad4589672f4a5d55a62af2a336a0af7d4896f8d48b8

### RSA

RSA keys 使用非对称加密技术。  您只与币安共享您的 public key 并在本地使用 private key 签署 API 请求。币安 API 会使用 public key 来验证您的请求签名。

我们支持 2048 和 4096 bits 的 RSA keys。

虽然 RSA keys 比 HMAC keys 更安全，RSA 签名比 HMAC 和 Ed25519 大很多，这会降低性能。

RSA (2048 bits) 例子:
    
    
    Code
    
    -----BEGIN PUBLIC KEY-----
    MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAyfKiFXpcOhF5rX1XxePN
    akwN7Etwtn3v05cZNY+ftDHbVZHs/kY6Ruj5lhxVFAq5dv7Ba9/4jPijXuMuIc6Y
    8nUlqtrrxC8DEOAczw9SKATDYZN9nbLfYlbBFfHzRQUXdAtYCPI6XtxmJBS7aOBb
    4nZe1SVm+bhLrp0YQnx2P0s+37qkGeVn09m6w9MnWxjgCkkYFPWQkXIu5qOnwx6p
    NfqDmFD7d7dUc/6PZQ1bKFALu/UETsobmBk82ShbrBhlc0JXuhf9qBR7QASjHjFQ
    2N+VF2PfH8dm5prZIpz/MFKPkBW4Yuss0OXiD+jQt1J2JUKspLqsIqoXjHQQGjL7
    3wIDAQAB
    -----END PUBLIC KEY-----

RSA (2048 bits) 签名例子::
    
    
    Code
    
    wS6q6h77AvH1TqwInoTDdWIIubRCiUP4RLG++GI24twL3BMtX0EEV+YT1eH8Hb8bLe0Rb9OhOHbt1CC3aurzoCTgZvhNek47mg+Bpu8fwQ7eRkXEiWBx5C8BNN73JwnnkZw4UzYvqiwAs162jToV8AL0eN043KJ3MEKCy3C6nyeYOFSg+1Cp637KtAZk3z7aHknSu7/PXSPuwMIpBgFctf8YKGZFAVRbgwlcgUDhXyaGts6OFePGy0jkZKJHawb/w5hoatatsfVmVC4hZ8fsfystQ9k5DNjTm7ROApWaXy9BsfAYcj13O424mqlpkKG4EGnIjOIWB/pRDDQEm2O/xg==

此页面是否有帮助？

Last modified on November 12, 2026

[模拟交易使用条款](/zh-CN/docs/products/spot/demo-mode/DEMO-TERMS-OF-USE)[佣金率](/zh-CN/docs/products/spot/faqs/commission_faq)