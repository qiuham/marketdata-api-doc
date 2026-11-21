---
exchange: bitget
source_url: https://www.bitget.com/docs/uta/fastapi-integration-guide
api_type: Guide
updated_at: 2026-11-21 19:03:19.562674
---

# FastAPI Integration Guide

## Background

Welcome to Bitget! As a broker, when integrating with our FastAPI, it's important to follow Bitget's integration standards. This documentation provides a step-by-step guide to help you integrate with Bitget's FastAPI.

## Integration Preparation

This feature requires you to prepare the following materials and configure them in the management console:

:::info
For instructions on configuring them in the management console, please refer to the [OAuth Broker Fast API Self-Service Configuration Guide](https://www.bitget.com/support/articles/12560603899224).
:::

| Info | Description |
|:-----|:-------------|
| name | Platform name |
| contact | Contact method — email/phone number |
| ip | Server IP — common IP addresses used by the broker platform to access Bitget's API |
| logo (PNG) | Platform logo — PNG format (64 × 64 pixels resolution) |
| callbackUrl | Callback URL — for broker user info callbacks |
| rsaPublicKey (2048 bit) | Public key — based on the RSA algorithm; format: RSA PKCS8, 2048-bit |

:::tip{title="Updating IP Whitelist or Callback URL"}
If you need to adjust your registered IP whitelist or callback URL after the initial integration, you can manage them yourself. For detailed instructions, please refer to [Modify Broker IP/Callback URL](https://www.bitget.com/support/articles/12560603899224).
:::

Once configuration is complete, the management console will return the following:

| Parameter name | Parameter type | Description |
|:----------------|:-----------------|:--------------|
| clientId | String | Broker platform ID — unique tag assigned by Bitget |

### Technical Implementation

The following attributes are primarily used to support feature integration.

| Parameter name | Parameter type | Provider | Description |
|:----------------|:-----------------|:-----------|:--------------|
| clientId | String | Bitget | Broker platform ID — viewable in the management console once configuration is complete |
| callbackUrl | String | Broker user | Callback URL — used for broker user info callbacks |
| rsaPublicKey (2048 bit) | String | Broker user | Public key — based on the RSA algorithm, format: RSA PKCS8, 2048-bit |
| rsaPrivateKey (2048 bit) | String | Broker user | Private key — based on the RSA algorithm; format: RSA PKCS8, 2048-bit; kept by the broker, not shared with Bitget |

:::warning{title="Keep your private key secure"}
The `rsaPrivateKey` must be stored securely on the broker side and never shared with Bitget or any third party. Anyone in possession of the private key can decrypt user API key information and forge signatures.
:::

### Code Examples (Java)

Below are examples of signature, RSA encryption and decryption. These examples are designed for Java.

#### Utility Class

Both signature and RSA encryption/decryption are implemented based on this utility class.

```Java title="RsaUtil.java"
package xxx;

import org.springframework.util.Base64Utils;
import javax.crypto.Cipher;
import java.nio.charset.StandardCharsets;
import java.security.KeyFactory;
import java.security.PrivateKey;
import java.security.PublicKey;
import java.security.Signature;
import java.security.spec.PKCS8EncodedKeySpec;
import java.security.spec.X509EncodedKeySpec;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.Set;
import java.util.TreeSet;

public class RsaUtil {

    // Encrypt with RSA using a public key
    public static String encryptRSA(String plaintext, String publicKey) throws Exception {
        Cipher cipher = Cipher.getInstance("RSA");
        cipher.init(Cipher.ENCRYPT_MODE, getPublicKey(publicKey));
        byte[] encryptedBytes = cipher.doFinal(plaintext.getBytes(StandardCharsets.UTF_8));
        return Base64Utils.encodeToString(encryptedBytes);
    }

    // use private key for RSA decryption
    public static String decryptRSA(String encryptedData, String privateKey) throws Exception {
        Cipher cipher = Cipher.getInstance("RSA");
        cipher.init(Cipher.DECRYPT_MODE, getPrivateKey(privateKey));
        byte[] encryptedBytes = Base64Utils.decodeFromString(encryptedData);
        byte[] decryptedBytes = cipher.doFinal(encryptedBytes);
        return new String(decryptedBytes, StandardCharsets.UTF_8);
    }

    /**
     * DecodePublicKey
     *
     * @param key
     * @return
     */
    public static PublicKey getPublicKey(String key) throws Exception {
        byte[] byteKey = org.apache.commons.codec.binary.Base64.decodeBase64(key);
        X509EncodedKeySpec x509EncodedKeySpec = new X509EncodedKeySpec(byteKey);
        KeyFactory keyFactory = KeyFactory.getInstance("RSA");
        return keyFactory.generatePublic(x509EncodedKeySpec);
    }

    /**
     * DecodePrivateKey
     *
     * @param key
     * @return
     */
    public static PrivateKey getPrivateKey(String key) throws Exception {
        byte[] byteKey = org.apache.commons.codec.binary.Base64.decodeBase64(key);
        PKCS8EncodedKeySpec x509EncodedKeySpec = new PKCS8EncodedKeySpec(byteKey);
        KeyFactory keyFactory = KeyFactory.getInstance("RSA");
        return keyFactory.generatePrivate(x509EncodedKeySpec);
    }

    public static boolean verify(Map<String, String> map, String publicKey, String sign) throws Exception {
        String srcData = getSignData(map);
        byte[] keyBytes = getPublicKey(publicKey).getEncoded();
        X509EncodedKeySpec keySpec = new X509EncodedKeySpec(keyBytes);
        KeyFactory keyFactory = KeyFactory.getInstance("RSA");
        PublicKey key = keyFactory.generatePublic(keySpec);
        Signature signature = Signature.getInstance("SHA256withRSA");
        signature.initVerify(key);
        signature.update(srcData.getBytes());
        return signature.verify(Base64Utils.decodeFromString(sign));
    }

    /**
     * Signature
     *
     * @param data       data to be signed
     * @param privateKey the private key
     * @return signature
     */
    public static String sign(String data, String privateKey) throws Exception {
        byte[] keyBytes = getPrivateKey(privateKey).getEncoded();
        PKCS8EncodedKeySpec keySpec = new PKCS8EncodedKeySpec(keyBytes);
        KeyFactory keyFactory = KeyFactory.getInstance("RSA");
        PrivateKey key = keyFactory.generatePrivate(keySpec);
        Signature signature = Signature.getInstance("SHA256withRSA");
        signature.initSign(key);
        signature.update(data.getBytes());
        return Base64Utils.encodeToString(signature.sign());
    }

    /**
     * Get signature
     *
     * @param params parameter set excluding the secret key
     * @return
     */
    public static String getSignData(Map<String, String> params) {
        StringBuilder sb = new StringBuilder();
        // step1: sort the request parameters
        Set<String> keyset = params.keySet();
        TreeSet<String> sortSet = new TreeSet<String>();
        sortSet.addAll(keyset);
        Iterator<String> it = sortSet.iterator();
        // step2: link parameter key-values, append secret key, get string to encrypt
        while (it.hasNext()) {
            String key = it.next();
            String value = params.get(key);
            sb.append(key).append(value);
        }
        return sb.toString();
    }

    static String publicKey = "*****";

    static String privateKey = "*****";
}
```

#### Signature Usage Example

```Java
public static void main(String[] args) throws Exception {
    // Generate a signature
    Map<String, String> map = new HashMap<>();
    long l = System.currentTimeMillis();
    map.put("timestamp", String.valueOf(l));
    map.put("clientId", "1");
    map.put("clientUserId", "123");
    String sign = RsaUtil.sign(RsaUtil.getSignData(map), RsaUtil.privateKey);
    System.out.println(sign);
}
```

#### Examples of RSA Encryption and Decryption Usage

```Java
public static void main(String[] args) throws Exception {
    String xxStr = "hello world";
    // encrypt
    String encrypted = RsaUtil.encryptRSA(xxStr, RsaUtil.publicKey);
    System.out.println("encrypt by publicKey: " + encrypted);
    // decrypt
    System.out.println("decrypt by privateKey: " + RsaUtil.decryptRSA(encrypted, RsaUtil.privateKey));
}
```

## Function Implementation

Below is the detailed process for feature implementation — covering the APIs, parameters, and signature generation rules used in the OAuth authorization flow.

The flow has three steps: the broker redirects the user to Bitget's authorization page, Bitget calls back to the broker's interface with the user's API key, and Bitget redirects the user back to the broker's page with the authorization result.

### 1. Broker Redirects to the Bitget Authorization Page

When redirecting from the broker platform to Bitget's authorization page, the broker needs to include the following parameters in the URL.

The authorization page link is `https://www.bitget.com/en/account/oauth`.

| Parameter name | Parameter type | Description |
|:----------------|:-----------------|:--------------|
| clientUserId | String | Broker user ID — customizable by client |
| timestamp | String | Timestamp — Unix millisecond format; must be within 5 minutes before or after the current time, or the request is considered invalid. This timestamp is verified when the user clicks **Authorize** on the Bitget page |
| clientId | String | Broker platform ID |
| sign | String | Signature — format rule: `clientUserId[]timestamp[]clientId[]`. See [Code Examples (Java)](#code-examples-java) for signing details |
| redirectUrl | String | Redirection address — broker platform link automatically redirected to after authorization |
| serialNo | String | Random serial number — 1) the broker must validate the legitimacy of the callback request using this parameter; 2) for security reasons, bind `serialNo` to `clientUserId` and avoid using it across multiple accounts; 3) it's recommended to set an expiration time for `serialNo`, e.g. 10 minutes |

Example URL (make sure to URL-encode all parameters to prevent encoding issues or data loss during transfer):

```Plain Text
https://www.bitget.com/en/account/oauth?clientUserId=123&timestamp=1691117744470&clientId=1&redirectUrl=https://broker-domain/callback/url&sign=F9zeG9oUYzqwN94kSfoFy...&serialNo=123
```

#### Supplementary Information (Optional Configuration)

To help improve user registration conversion, Bitget supports including a referral code in the OAuth redirect URL. When a user is redirected to Bitget via OAuth and clicks **Sign Up**, the referral code included in the URL is automatically detected and pre-filled on the registration page — the user does not need to enter it manually.

Configuration steps:

1. Contact your Broker Operations or BD representative to configure an invitation link (long URL), e.g. `https://www.bitget.com/test?channelCode=abcde&vipCode=1234&languageType=1`.
2. Retrieve the referral code parameter from the invitation link, e.g. `vipCode=1234`.
3. Append this referral code parameter to your Bitget OAuth redirect URL to complete the configuration.

```Plain Text
https://www.bitget.com/account/oauth?clientUserId=123&timestamp=1691117744470&clientId=1&redirectUrl=https://broker-domain/callback/url&sign=F9zeG9oUYzqwN94kSfoFy...&serialNo=123&channelCode=abcde&vipCode=1234
```

### 2. Bitget Callback to Broker Interface

Once the user completes authorization on the page, Bitget will automatically initiate a request to the broker's callback interface.

- Request type: `POST`
- Request URL: to be discussed between both parties
- Content-Type: `application/x-www-form-urlencoded`

| Parameter name | Parameter type | Description |
|:----------------|:-----------------|:--------------|
| openId | String | Encrypted Bitget user ID |
| userId | String | Bitget user ID — returned exclusively for whitelisted users; returned as empty otherwise |
| clientUserId | String | Broker user ID |
| timestamp | String | Timestamp — Unix millisecond format; if the difference from the current time exceeds 5 minutes, the request is considered invalid |
| sign | String | Signature — decrypt with `privateKey` to obtain `serialNo` |
| data | String | Encrypted API key information — decrypt with `privateKey` to obtain the user's `apiKey`, `passphrase`, and `secret` |

#### Additional Information

1. Decrypt `sign` using `privateKey` and verify it matches `serialNo`. If not, the request is invalid.
2. Decrypt `data` using `privateKey` to obtain the API key information in JSON format:

```JSON
{
    "apiKey": "bg_xxxxxxxxxx",
    "passphrase": "***",
    "secret": "xxxxxxxxxxxxxxxxxxxxxxx"
}
```

:::warning{title="Store API key information securely"}
The decrypted `apiKey`, `passphrase`, and `secret` grant trading access to the user's Bitget account. Store them securely (e.g. encrypted at rest) and never expose them in logs, client-side code, or error messages.
:::

After receiving Bitget's request, the broker should respond with:

```JSON
{
    "code": "00000",
    "msg": "success",
    "requestTime": "1671258739383"
}
```

### 3. Bitget Redirects to Broker's Page

Regardless of the authorization result, Bitget will append the following parameters to the URL and redirect to the broker's page.

| Parameter name | Parameter type | Description |
|:----------------|:-----------------|:--------------|
| clientUserId | String | Broker user ID |
| sign | String | Signature — the `serialNo` encrypted with the public key; needs to be decrypted |
| state | String | Authorization status — encrypted with the public key; needs to be decrypted. `SUCCESS` = authorization successful, `FAIL` = authorization failure |

Example:

```HTTP
https://broker-domain/callback/url?sign=sahkduhas1237hkNAQGS&clientUserId=123&state=DHJSAshaj
```

#### Additional Information

1. Decrypt `sign` using `privateKey` and verify it matches `serialNo`. If not, the request is invalid.
2. It's recommended to query `clientUserId` using `serialNo` and verify it matches the `clientUserId` in the current URL. If not, the request is invalid.

## FAQ

### 1. Does the created API Key have withdrawal permission?

The created API Key has read and write permissions, excluding withdrawal and P2P permissions.

### 2. Is the created API Key automatically bound to the configured whitelist IP addresses?

Yes.

### 3. After the IP whitelist is updated, will the created API Key be updated automatically?

Yes, the bound IP addresses will be updated automatically.

---

# FastAPI 接入指南

## 背景

欢迎与 Bitget 交易所合作，您作为 Broker 在接入我们的 FastAPI 时，需要按照我们给出的标准进行接入。在本文档中，我们将为您介绍如何接入到 Bitget 的 FastAPI。

## 接入准备

该功能需要您准备以下资料，并在管理后台进行配置：

:::info
管理后台配置方式请参考[OAuth Broker Fast API 配置自助管理指南](https://www.bitget.com/zh-CN/support/articles/12560603899224)
:::

| 信息 | 说明 |
|:-----|:-----|
| name | 平台名称 |
| contact | 联系方式 — 邮箱或手机号 |
| ip | 服务器 IP — Broker 平台调用 Bitget API 接口的常用 IP 地址 |
| logo（PNG） | 平台 Logo — 文件格式为 PNG，像素要求为 64 × 64 |
| callbackUrl | 回调地址 — 用于 Broker 用户信息回传 |
| rsaPublicKey（2048 bit） | 公钥 — 基于 RSA 算法；格式规则为 RSA PKCS8 2048 位 |

:::tip{title="后续调整 IP 白名单或回调地址"}
完成初次接入后，如需调整已登记的 IP 白名单或回调地址，可自助管理。具体操作请参见：[修改 Broker IP/回调地址](https://www.bitget.com/zh-CN/support/articles/12560603899224)。
:::

配置成功后，管理后台会返回以下信息：

| 参数名称 | 参数类型 | 说明 |
|:---------|:---------|:-----|
| clientId | String | Broker 平台 ID — 由 Bitget 分配的唯一标识 |

### 技术实现

下面涉及到的一些属性信息，主要用于对接功能实现。

| 参数名称 | 参数类型 | 提供方 | 描述 |
|:---------|:---------|:-------|:-----|
| clientId | String | Bitget | Broker 平台 ID — 管理后台配置完成后可查看 |
| callbackUrl | String | Broker 客户 | 回调地址 — 用于 Broker 用户信息回传 |
| rsaPublicKey（2048 bit） | String | Broker 客户 | 公钥 — 基于 RSA 算法，格式规则为 RSA PKCS8 2048 位 |
| rsaPrivateKey（2048 bit） | String | Broker 客户 | 私钥 — 基于 RSA 算法；格式规则为 RSA PKCS8 2048 位；由 Broker 自行保管，无需提供给 Bitget |

:::warning{title="请妥善保管私钥"}
`rsaPrivateKey` 必须由 Broker 一方安全保存，切勿提供给 Bitget 或任何第三方。一旦私钥泄露，他人可解密用户的 API Key 信息并伪造签名。
:::

### 代码示例（Java）

下面是签名和 RSA 加密解密的代码示例，均基于 Java 实现。

#### 工具类

签名以及 RSA 加密/解密都基于下面的工具类实现。

```Java title="RsaUtil.java"
package xxx;

import org.springframework.util.Base64Utils;
import javax.crypto.Cipher;
import java.nio.charset.StandardCharsets;
import java.security.KeyFactory;
import java.security.PrivateKey;
import java.security.PublicKey;
import java.security.Signature;
import java.security.spec.PKCS8EncodedKeySpec;
import java.security.spec.X509EncodedKeySpec;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.Set;
import java.util.TreeSet;

public class RsaUtil {

    // 使用公钥进行 RSA 加密
    public static String encryptRSA(String plaintext, String publicKey) throws Exception {
        Cipher cipher = Cipher.getInstance("RSA");
        cipher.init(Cipher.ENCRYPT_MODE, getPublicKey(publicKey));
        byte[] encryptedBytes = cipher.doFinal(plaintext.getBytes(StandardCharsets.UTF_8));
        return Base64Utils.encodeToString(encryptedBytes);
    }

    // 使用私钥进行 RSA 解密
    public static String decryptRSA(String encryptedData, String privateKey) throws Exception {
        Cipher cipher = Cipher.getInstance("RSA");
        cipher.init(Cipher.DECRYPT_MODE, getPrivateKey(privateKey));
        byte[] encryptedBytes = Base64Utils.decodeFromString(encryptedData);
        byte[] decryptedBytes = cipher.doFinal(encryptedBytes);
        return new String(decryptedBytes, StandardCharsets.UTF_8);
    }

    /**
     * 解码 PublicKey
     *
     * @param key
     * @return
     */
    public static PublicKey getPublicKey(String key) throws Exception {
        byte[] byteKey = org.apache.commons.codec.binary.Base64.decodeBase64(key);
        X509EncodedKeySpec x509EncodedKeySpec = new X509EncodedKeySpec(byteKey);
        KeyFactory keyFactory = KeyFactory.getInstance("RSA");
        return keyFactory.generatePublic(x509EncodedKeySpec);
    }

    /**
     * 解码 PrivateKey
     *
     * @param key
     * @return
     */
    public static PrivateKey getPrivateKey(String key) throws Exception {
        byte[] byteKey = org.apache.commons.codec.binary.Base64.decodeBase64(key);
        PKCS8EncodedKeySpec x509EncodedKeySpec = new PKCS8EncodedKeySpec(byteKey);
        KeyFactory keyFactory = KeyFactory.getInstance("RSA");
        return keyFactory.generatePrivate(x509EncodedKeySpec);
    }

    public static boolean verify(Map<String, String> map, String publicKey, String sign) throws Exception {
        String srcData = getSignData(map);
        byte[] keyBytes = getPublicKey(publicKey).getEncoded();
        X509EncodedKeySpec keySpec = new X509EncodedKeySpec(keyBytes);
        KeyFactory keyFactory = KeyFactory.getInstance("RSA");
        PublicKey key = keyFactory.generatePublic(keySpec);
        Signature signature = Signature.getInstance("SHA256withRSA");
        signature.initVerify(key);
        signature.update(srcData.getBytes());
        return signature.verify(Base64Utils.decodeFromString(sign));
    }

    /**
     * 签名
     *
     * @param data       待签名数据
     * @param privateKey 私钥
     * @return 签名
     */
    public static String sign(String data, String privateKey) throws Exception {
        byte[] keyBytes = getPrivateKey(privateKey).getEncoded();
        PKCS8EncodedKeySpec keySpec = new PKCS8EncodedKeySpec(keyBytes);
        KeyFactory keyFactory = KeyFactory.getInstance("RSA");
        PrivateKey key = keyFactory.generatePrivate(keySpec);
        Signature signature = Signature.getInstance("SHA256withRSA");
        signature.initSign(key);
        signature.update(data.getBytes());
        return Base64Utils.encodeToString(signature.sign());
    }

    /**
     * 得到签名
     *
     * @param params 参数集合，不含 secretKey
     * @return
     */
    public static String getSignData(Map<String, String> params) {
        StringBuilder sb = new StringBuilder();
        // step1：先对请求参数排序
        Set<String> keyset = params.keySet();
        TreeSet<String> sortSet = new TreeSet<String>();
        sortSet.addAll(keyset);
        Iterator<String> it = sortSet.iterator();
        // step2：把参数的 key value 链接起来，secretKey 放在最后面，得到要加密的字符串
        while (it.hasNext()) {
            String key = it.next();
            String value = params.get(key);
            sb.append(key).append(value);
        }
        return sb.toString();
    }

    static String publicKey = "*****";

    static String privateKey = "*****";
}
```

#### 签名使用示例

```Java
public static void main(String[] args) throws Exception {
    // 生成签名
    Map<String, String> map = new HashMap<>();
    long l = System.currentTimeMillis();
    map.put("timestamp", String.valueOf(l));
    map.put("clientId", "1");
    map.put("clientUserId", "123");
    String sign = RsaUtil.sign(RsaUtil.getSignData(map), RsaUtil.privateKey);
    System.out.println(sign);
}
```

#### RSA 加密和解密使用示例

```Java
public static void main(String[] args) throws Exception {
    String xxStr = "hello world";
    // encrypt
    String encrypted = RsaUtil.encryptRSA(xxStr, RsaUtil.publicKey);
    System.out.println("encrypt by publicKey: " + encrypted);
    // decrypt
    System.out.println("decrypt by privateKey: " + RsaUtil.decryptRSA(encrypted, RsaUtil.privateKey));
}
```

## 功能实现

下面是功能实现的具体过程，其中涉及到了接口、参数、签名生成规则等 OAuth 授权流程细节。

整体流程分为三步：Broker 跳转 Bitget 授权页面、Bitget 携带用户 API Key 回调 Broker 接口、Bitget 携带授权结果跳转回 Broker 页面。

### 1. Broker 跳转 Bitget 授权页面

从 Broker 平台跳转到 Bitget 的授权页面时，需要 Broker 在 URL 中携带以下参数。

Bitget 授权页面链接为 `https://www.bitget.com/account/oauth`。

| 参数名 | 参数类型 | 描述 |
|:-------|:---------|:-----|
| clientUserId | String | Broker 用户 ID — 客户自定义 |
| timestamp | String | 时间戳 — Unix 毫秒格式；请传入当前时间前后 5 分钟内的时间戳，超出范围会被认为无效请求；用户在 Bitget 页面点击授权时会校验该时间戳 |
| clientId | String | Broker 平台 ID |
| sign | String | 签名 — 格式规则为 `clientId[]clientUserId[]timestamp[]`；实际使用请参考[代码示例（Java）](#代码示例java) |
| redirectUrl | String | 重定向地址 — 授权完成后自动跳转的 Broker 平台链接 |
| serialNo | String | 随机序列号 — 1）在回调接口中，Broker 需要通过此参数校验回调接口请求的合法性；2）出于安全考虑，请将 `serialNo` 与 `clientUserId` 关联，不要在多个账户间混用；3）出于安全考虑，建议为 `serialNo` 设置有效期，例如 10 分钟 |

示例 URL（请将参数进行 URL 编码，防止参数在传输过程中转译丢失）：

```Plain Text
https://www.bitget.com/account/oauth?clientUserId=123&timestamp=1691117744470&clientId=1&redirectUrl=https://broker-domain/callback/url&sign=F9zeG9oUYzqwN94kSfoFy...&serialNo=123
```

#### 补充说明（可选配置）

为帮助提升用户注册转化，Bitget 支持在 OAuth 跳转链接中携带邀请码（Referral Code）。当用户通过 OAuth 跳转至 Bitget 页面后点击**注册**，系统会自动识别链接中携带的邀请码，并在注册页面自动填充，无需用户手动输入。

配置方式：

1. 联系 Broker 运营或 BD，在后台配置邀请链接（长链接），例如 `https://www.bitget.com/test?channelCode=abcde&vipCode=1234&languageType=1`。
2. 从邀请链接中获取邀请码参数，例如 `vipCode=1234`。
3. 将该邀请码参数追加至 Bitget OAuth 跳转链接后，即可完成配置。

```Plain Text
https://www.bitget.com/account/oauth?clientUserId=123&timestamp=1691117744470&clientId=1&redirectUrl=https://broker-domain/callback/url&sign=F9zeG9oUYzqwN94kSfoFy...&serialNo=123&channelCode=abcde&vipCode=1234
```

### 2. Bitget 回调 Broker 接口

一旦用户在页面完成授权，Bitget 将自动请求 Broker 回调接口。

- 请求类型：`POST`
- 请求 URL：双方商议
- Content-Type：`application/x-www-form-urlencoded`

| 参数名 | 参数类型 | 描述 |
|:-------|:---------|:-----|
| openId | String | 加密后的 Bitget user ID |
| userId | String | Bitget user ID — 仅白名单用户返回，非白名单用户返回为空 |
| clientUserId | String | Broker 用户 ID |
| timestamp | String | 时间戳 — Unix 毫秒格式；请验证该时间与当前时间的差值是否超过 5 分钟，如超出范围请视作无效请求 |
| sign | String | 签名 — 请通过 `privateKey` 解密，解密后可获得 `serialNo` |
| data | String | 加密后的 API Key 信息 — 请通过 `privateKey` 解密，解密后可获得用户 `apiKey`、`passphrase` 及 `secret` |

#### 其他说明

1. 请使用 `privateKey` 对 `sign` 进行解密，并校验结果是否与 `serialNo` 一致，若不一致则说明请求不合法。
2. 请使用 `privateKey` 对 `data` 进行解密，解密结果为 JSON 格式的用户 API Key 信息：

```JSON
{
    "apiKey": "bg_xxxxxxxxxx",
    "passphrase": "***",
    "secret": "xxxxxxxxxxxxxxxxxxxxxxx"
}
```

:::warning{title="请妥善保管 API Key 信息"}
解密后得到的 `apiKey`、`passphrase`、`secret` 可用于操作用户的 Bitget 账户交易权限，请安全存储（如加密存储），切勿在日志、前端代码或错误信息中暴露这些信息。
:::

Bitget 请求后，Broker 需按照如下格式返回响应参数：

```JSON
{
    "code": "00000",
    "msg": "success",
    "requestTime": "1671258739383"
}
```

### 3. Bitget 跳转回 Broker 页面

授权结果无论成功还是失败，Bitget 都会将下列参数添加至 URL，并跳转到 Broker 页面。

| 参数名 | 参数类型 | 描述 |
|:-------|:---------|:-----|
| clientUserId | String | Broker 平台的用户 ID |
| sign | String | 签名 — 通过 publicKey 加密后的 `serialNo`，需要进行解密 |
| state | String | 授权状态 — 通过 publicKey 加密后的 `state`，需要进行解密；`SUCCESS` 表示授权成功，`FAIL` 表示授权失败 |

示例：

```HTTP
https://broker-domain/callback/url?sign=sahkduhas1237hkNAQGS&clientUserId=123&state=DHJSAshaj
```

#### 其他说明

1. 请使用 `privateKey` 对 `sign` 进行解密，并校验结果是否与 `serialNo` 一致，若不一致则说明请求不合法。
2. 建议通过 `serialNo` 查询 `clientUserId`，并判断是否与当前 URL 中的 `clientUserId` 一致，若不一致则说明请求不合法。

## FAQ

### 1. 创建的 API Key 是否有提币权限？

创建的 API Key 为读写权限，其中不包含提币和 P2P 权限。

### 2. 创建的 API Key 是否自动绑定配置的白名单 IP 地址？

是的。

### 3. 更新 IP 白名单后，创建的 API Key 是否会自动更新？

是的，会自动更新绑定 IP。