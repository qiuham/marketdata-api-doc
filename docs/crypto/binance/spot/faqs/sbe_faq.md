---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/spot/faqs/sbe_faq
api_type: REST
updated_at: 2026-11-13 20:24:37.094619
---

# Simple Binary Encoding (SBE) FAQ

The goal of this document is to explain:

  * How to receive SBE responses in the SPOT API.
  * How to decode SBE responses.



SBE is a serialization format used for low-latency.

This implementation is based on the FIX SBE specification.

  * [GitHub repository](https://github.com/FIXTradingCommunity/fix-simple-binary-encoding)
  * [HTML document](https://www.fixtrading.org/standards/sbe-online)



### How to get an SBE response

#### REST API

  * The `Accept` header must include `application/sbe`.
  * Provide the schema ID and version in the `X-MBX-SBE` header as `<ID>:<VERSION>`.



Sample request (REST):
    
    
    Code
    
    curl -sX GET -H "Accept: application/sbe" -H "X-MBX-SBE: 1:0" 'https://api.binance.com/api/v3/exchangeInfo?symbol=BTCUSDT'

**Notes:**

  * If you provide only `application/sbe` in the Accept header:
    * If SBE is not enabled in the exchange, you will receive an HTTP **406 Not Acceptable**.
    * If the `<ID>:<VERSION>` provided in the `X-MBX-SBE` header is malformed or invalid, the response will be an SBE-encoded error.
    * If the `X-MBX-SBE` header is missing, the response will be an SBE-encoded error.
  * If you provide both `application/sbe` and `application/json` in the Accept header:
    * If SBE is not enabled in the exchange, the response will fall back to JSON.
    * If the `<ID>:<VERSION>` provided in the `X-MBX-SBE` header is malformed or invalid, the response will fall back to JSON.
    * If the `X-MBX-SBE` header is missing, the response will fall back to JSON.



#### WebSocket API

  * In the connection URL, add `responseFormat=sbe`.
  * Provide the schema ID and version in the parameters `sbeSchemaId=<SCHEMA_ID>` and `sbeSchemaVersion=<SCHEMA_VERSION>` respectively.



Sample request (WebSocket):
    
    
    Code
    
    id=$(date +%s%3N)
    method="exchangeInfo"
    params='{"symbol":"BTCUSDT"}'
    
    request=$( jq -n \
            --arg id "$id" \
            --arg method "$method" \
            --argjson params "$params" \
            '{id: $id, method: $method, params: $params}' )
    
    response=$(echo $request | websocat -n1 'wss://ws-api.binance.com:443/ws-api/v3?responseFormat=sbe&sbeSchemaId=1&sbeSchemaVersion=0')

**Notes:**

  * If you provide only `responseFormat=sbe` in the connection URL:
    * If SBE is not enabled in the exchange, the response will be HTTP 400.
    * If the `sbeSchemaId=<SCHEMA_ID>` or `sbeSchemaVersion=<SCHEMA_VERSION>` are malformed or invalid, the response will be HTTP 400.
  * If you provide both `responseFormat=sbe` and `responseFormat=json`, the response will be HTTP 400.
  * All error responses during the HTTP handshake are encoded as JSON with the `Content-Type` header set to `application/json;charset=UTF-8`.
  * Once a WebSocket session has been successfully established with SBE enabled, all method responses within that session are encoded in SBE, even in the event SBE becomes disabled.
    * This means that if SBE is disabled while your WebSocket connection is active, you will receive an SBE-encoded "SBE is not enabled" error in response to any subsequent request.
  * As of writing, we do not recommend using `websocat` to send any request as we have observed issues in how it decodes binary frames. The sample above is only used for reference to show the URL to get an SBE response.



#### FIX API

See FIX API's [SBE section](/en/docs/products/spot/fix-api#fix-sbe) for detailed information.

Please continue reading below also.

### Supported APIs

REST API, WebSocket API and FIX API for SPOT support SBE.

### SBE Schema

  * The schema to use both for the live exchange and SPOT Testnet will be saved in this repository [here](/en/docs/products/spot/sbe/schemas/introduction).
  * Any updates to the schema will be noted in the [CHANGELOG](/en/docs/products/spot/CHANGELOG).



### Regarding Legacy support

  * SBE schemas are versioned via two XML attributes, `id` and `version`.
    * `id` is incremented when a breaking change is introduced. When this occurs, `version` is reset to 0.
    * `version` is incremented when a non-breaking change is introduced. When this occurs, `id` is not modified.
  * When a new schema is live the old schema becomes deprecated. **Deprecation occurs even when the new schema only introduces non-breaking changes.**
  * A deprecated schema will be supported **for at least 6 months after deprecation**. For example given this hypothetical timeline:
    * January 3024: Schema id 1 version 0 is released. This is the first version so this is usable once SBE is enabled in the exchange.
    * March 3024: Schema id 1 version 1 is released. This schema introduces a non-breaking change.
      * Schema id 1 version 0 is deprecated, but can still be used for at least another 6 months.
    * August 3024: Schema id 2 version 0 is released. This schema introduces a breaking change.
      * Schema id 1 version 0 is deprecated, but can still be used for at least another 1 month.
      * Schema id 1 version 1 is deprecated, but can still be used for at least another 6 months.
      * September 3024: 6 months have passed since the release of Schema id 1 version 1.
        * Schema id 1 version 0 is retired.
    * February 3025: Schema id 2 version 1 is released. This schema introduces a non-breaking change.
      * Schema id 1 version 1 is retired.
      * Schema id 2 version 0 is deprecated, but can still be used for at least another 6 months.
  * For REST API requests specifying a deprecated `<ID>:<VERSION>` in their `X-MBX-SBE` header:
    * the HTTP responses will contain a `X-MBX-SBE-DEPRECATED` header
    * the SBE responses will be encoded in the highest compatible schema
      * For example, as of 2025-08-27, requests for `X-MBX-SBE: 3:0` will receive responses encoded in schema `3:1`. An SBE decoder for schema `3:0` is expected to decode schema `3:1` gracefully as detailed in the [FIX SBE Specification](https://www.fixtrading.org/standards/sbe-online/#schema-extension-mechanism).
  * For WebSocket API connections specifying a deprecated `sbeSchemaId` and `sbeSchemaVersion` in their connection URL:
    * the field `sbeSchemaIdVersionDeprecated` will be set to `true` in all `WebSocketResponse` SBE messages
    * all SBE responses will be encoded in the highest compatible schema
      * For example, as of 2025-08-27, requests for `sbeSchemaId=3&sbeSchemaVersion=0` will receive responses encoded in schema `3:1`. An SBE decoder for schema `3:0` is expected to decode schema `3:1` gracefully as detailed in the [FIX SBE Specification](https://www.fixtrading.org/standards/sbe-online/#schema-extension-mechanism).
  * For FIX API, when an SBE request message header specifies a deprecated `schemaId` and `version`:
    * the field `sbeSchemaIdVersionDeprecated` will be set to `true` in the `LogonAck` message
    * all SBE response messages will be encoded using the highest schema version for the provided `schemaId`
  * Requests specifying a retired schemaId/version will fail with HTTP 400 (REST & WebSocket) or reject message (FIX API) .
  * In SBE Schema [3:0](/en/docs/products/spot/sbe/schemas/spot_3_0.xml), a `validValue` named `NonRepresentable` was added to each `enum`. Receipt of this value indicates that additional data is available when using the latest schema.
  * In SBE Schema [3:1](/en/docs/products/spot/sbe/schemas/spot_3_1.xml), a message named `NonRepresentableMessage` was added. Receipt of this message indicates that additional data is available when using the latest schema. This message may be received as a top-level message or embedded in a `data` field when the `data` field's `type` is `messageData`, `messageData8`, `messageData16`, `optionalMessageData`, or `optionalMessageData16`.
  * JSON file regarding the schema life-cycle with the dates of the latest, deprecated, and retired schemas for both the live exchange and SPOT Testnet will be saved in this repository [here](/en/docs/products/spot/sbe/schemas/introduction).  Below is an example JSON based on the hypothetical timeline above:


    
    
    Code
    
    {
      "environment": "PROD",
      "latestSchema": {
        "id": 2,
        "version": 1,
        "releaseDate": "3025-02-01"
      },
      "deprecatedSchemas": [
        {
          "id": 2,
          "version": 0,
          "releaseDate": "3024-08-01",
          "deprecatedDate": "3025-02-01"
        }
      ],
      "retiredSchemas": [
        {
          "id": 1,
          "version": 1,
          "releaseDate": "3024-03-01",
          "deprecatedDate": "3024-08-01",
          "retiredDate": "3025-02-01"
        },
        {
          "id": 1,
          "version": 0,
          "releaseDate": "3024-01-01",
          "deprecatedDate": "3024-03-01",
          "retiredDate": "3024-09-01"
        }
      ]
    }

### Generate SBE decoders:

  1. Download the schema:
     * REST/WebSocket API:
       * [`spot_prod_latest.xml`](/en/docs/products/spot/sbe/schemas/spot_prod_latest.xml) for the live exchange.
       * [`spot_testnet_latest.xml`](/en/docs/products/spot/sbe/schemas/spot_testnet_latest.xml) for [SPOT Testnet](https://testnet.binance.vision).
     * FIX API:
       * [`spot_fix_prod_latest.xml`](/en/docs/products/spot/sbe/schemas/spot_fix_prod_latest.xml) for the live exchange.
       * [`spot_fix_testnet_latest.xml`](/en/docs/products/spot/sbe/schemas/spot_fix_testnet_latest.xml) for [SPOT Testnet](https://testnet.binance.vision).
  2. Clone and build [`simple-binary-encoding`](https://github.com/real-logic/simple-binary-encoding):


    
    
    Code
    
     $ git clone https://github.com/real-logic/simple-binary-encoding.git
     $ cd simple-binary-encoding
     $ ./gradlew

  3. Run the SbeTool code generator. (Here are samples for [Java](https://github.com/binance/binance-sbe-java-sample-app), [C++](https://github.com/binance/binance-sbe-cpp-sample-app) and [Rust](https://github.com/binance/binance-sbe-rust-sample-app) decoding the payload from Exchange Information.)



#### Decimal field encoding

Unlike the FIX SBE specification, decimal fields have their mantissa and exponent fields encoded separately as primitive fields in order to minimize payload size and the number of encoded fields within messages.

#### Timestamp field encoding

Timestamps in SBE responses are in microseconds. This differs from JSON responses, which contain millisecond timestamps by default.

#### Custom field attributes in the schema file

A few field attributes prefixed with `mbx:` were added to the schema file for documentation purposes:

  * `mbx:exponent`: Points to the exponent field corresponding to the mantissa field
  * `mbx:jsonPath`: Contains the name of the equivalent field in the JSON response
  * `mbx:jsonValue`: Contains the name of the equivalent ENUM value in the JSON response
  * `mbx:defaultJsonValue`: Contains the default value of the JSON response.



Was this page helpful?

Last modified on November 12, 2026

[Pegged orders](/en/docs/products/spot/faqs/pegged_orders)[Smart Order Routing (SOR)](/en/docs/products/spot/faqs/sor_faq)

---

# 简单二进制编码（SBE）常见问题

本文档的目标是解释下列疑问:

  * 如何在现货交易API中启用 `SBE` 响应。
  * 如何对 `SBE` 的响应进行解码。



SBE 是一种用于实现低延迟的序列化格式。

本实现是基于 `FIX SBE` 规范。

  * [GitHub repository](https://github.com/FIXTradingCommunity/fix-simple-binary-encoding)
  * [HTML document](https://www.fixtrading.org/standards/sbe-online)



### 如何获取 SBE 响应

#### REST API

  * `Accept` 报文头必须包含 `application/sbe`。
  * 在 `X-MBX-SBE` 报文头中以 `<ID>:<VERSION>` 的形式提供 `schema ID` 和 `version`。



样本请求(REST):
    
    
    Code
    
    curl -sX GET -H "Accept: application/sbe" -H "X-MBX-SBE: 1:0" 'https://api.binance.com/api/v3/exchangeInfo?symbol=BTCUSDT'

**注意：**

  * 如果你只在 `Accept` 报文头中提供了 `application/sbe`
    * 如果交易所不支持 `SBE`，你将收到一个**406 不可接受** 的响应。
    * 如果在 `X-MBX-SBE` 报文头中提供的 XML 模式是属于格式错误或不正确的情况，那你得到的响应将会是一个 `SBE` 解码错误。
    * 如果 `X-MBX-SBE` 报文头缺失，那你得到的响应将会是一个 `SBE` 解码错误。
  * 如果你在 `Accept` 报文头中同时提供了 `application/sbe` 和 `application/json`：
    * 如果交易所不支持 `SBE`，那么响应将会被回退到 `JSON`。
    * 如果在 `X-MBX-SBE` 报文头中提供的 XML 模式是属于格式错误或不正确的情况，那么响应将会被回退到 `JSON`。
    * 如果 `X-MBX-SBE` 报文头缺失，那么响应将会被回退到 `JSON`。



#### WebSocket API

  * 在请求的URL中添加 `responseFormat=sbe`。
  * 添加schema ID 和 version 到参数 `sbeSchemaId=<SCHEMA_ID>` 和 `sbeSchemaVersion=<SCHEMA_VERSION>`。



样本请求 (WebSocket):
    
    
    Code
    
    id=$(date +%s%3N)
    method="exchangeInfo"
    params='{"symbol":"BTCUSDT"}'
    
    request=$( jq -n \
            --arg id "$id" \
            --arg method "$method" \
            --argjson params "$params" \
            '{id: $id, method: $method, params: $params}' )
    
    response=$(echo $request | websocat -n1 'wss://ws-api.binance.com:443/ws-api/v3?responseFormat=sbe&sbeSchemaId=1&sbeSchemaVersion=0')

**注意：**

  * 如果你只在连接URL中添加 `responseFormat=sbe` :
    * 如果交易所没有开启 SBE，请求返回 HTTP 400.
    * 如果 `sbeSchemaId=<SCHEMA_ID>` 或者 `sbeSchemaVersion=<SCHEMA_VERSION>` 格式不正确或者无效，请求返回 HTTP 400.
  * 如果你同时提供 `responseFormat=sbe` 和 `responseFormat=json`, 请求返回 HTTP 400.
  * 在HTTP握手期间的所有错误响应都编码为JSON，`Content-Type`头设置为`application/json;charset=UTF-8`.
  * 一旦成功建立了启用了SBE的WebSocket会话，在该会话中的所有方法响应都编码为SBE，即使在SBE被禁用的情况下也是如此。
    * 这意味着，如果在您的WebSocket连接处于活动状态时禁用了SBE，那么在对您的后续请求做出响应时，您将会收到一个被SBE编码了的“SBE未启用”错误。
  * 就目前而言，我们不建议使用`websocat`发送任何请求，因为我们观察到了它解码二进制帧的问题。上面的样本仅用作参考，显示获取SBE响应的URL。



#### FIX API

详情请参见 FIX API 的 [SBE 部分](/zh-CN/docs/products/spot/fix-api#fix-sbe)

### 支持的 APIs

REST API、WebSocket API 和 FIX API 对现货（SPOT）支持 `SBE`。

### SBE 模式

  * 将被使用的模式 (schema) 会被保存在此仓库 (repository) 中，[请看这里](/zh-CN/docs/products/spot/sbe/schemas/introduction)。
  * 对于模式的任何更新将会被记录在[更改日志](/zh-CN/docs/products/spot/CHANGELOG)中。



#### 关于对旧版本的支持：

  * SBE 模式通过两个 XML 属性进行版本控制，`id` 和 `version`。
    * 当引入破坏性更改时，`id` 会增加。当这种情况发生时，`version` 会被重置为0。
    * 当引入非破坏性更改时，`version` 会增加。当这种情况发生时，`id` 不会被修改。
  * 当新模式发布时，旧模式会被废止。 **即便新模式只引入非破坏性更改，这种情况也会导致废止。**
  * 已废止的模式将在被废止后**依然得到至少6个月的支持** 。用以下这个假设的时间线为例:
    * 3024年1月：发布模式 id 1 version 0。这是第一版，一旦交易所启用 `SBE`，用户就立刻可以开始使用该模式。
    * 3024年3月：发布模式 id 1 version 1。这个模式引入了一个非破坏性的变化。
      * 模式 id 1 version 0 此时已被废止，但还可以至少再被使用6个月。
    * 3024年8月：发布模式 id 2 version 0。这个模式引入了一个破坏性的变化。
      * 模式 id 1 version 0 已被废止，但还可以再被使用至少1个月。
      * 模式 id 1 version 1 此时已被废止，但还可以再被使用至少6个月。
    * 3024年9月：自模式 id 1 version 1 发布以来已经过去6个月。
      * 模式 id 1 version 0 已被停用。
    * 3025年2月：发布模式id 2 版本 1。这个模式引入了一个非破坏性的变化。
      * 模式 id 1 version 1 已被停用。
      * 模式 id 2 version 0 此时已被废止，但还可以再被使用至少另外6个月。
  * 当 REST API 请求中在 `X-MBX-SBE` 头部里指定了已废止的 `<ID>:<VERSION>` 时：
    * HTTP 响应将包含 `X-MBX-SBE-DEPRECATED` 头部
    * SBE 响应将使用可兼容的最高版本模式进行编码
      * 例如，从2025-08-27 开始，针对 `X-MBX-SBE: 3:0` 的请求将收到以模式 `3:1` 进行编码的响应。根据 [FIX SBE 规范](https://www.fixtrading.org/standards/sbe-online/#schema-extension-mechanism)，模式 `3:0` 的 SBE 解码器应该能够顺利地对模式 `3:1` 进行解码。
  * 当 WebSocket API 连接 URL 中指定了已废止的 `sbeSchemaId` 和 `sbeSchemaVersion` 时：
    * 所有 `WebSocketResponse` SBE 消息中的字段 `sbeSchemaIdVersionDeprecated` 将被设置为 `true`
    * 所有 SBE 响应将使用可兼容的最高版本模式进行编码
      * 例如，从2025-08-27 开始，针对 `sbeSchemaId=3&sbeSchemaVersion=0` 的请求将收到以模式 `3:1` 进行编码的响应。根据 [FIX SBE 规范](https://www.fixtrading.org/standards/sbe-online/#schema-extension-mechanism)，模式 `3:0` 的 SBE 解码器应该能够顺利地对模式 `3:1` 进行解码。
  * 对于 FIX API，当 SBE 请求消息头指定了已弃用的 `schemaId` 和 `version` 时：
    * 在 `LogonAck` 消息中，字段 `sbeSchemaIdVersionDeprecated` 将被设置为 `true`
    * 所有 SBE 响应消息将使用所提供 `schemaId` 的最高模式版本进行编码
  * 指定已废弃的 schemaId/version 的请求将失败，返回 HTTP 400（REST 和 WebSocket）或拒绝消息（FIX API）。
  * 在 SBE 模式 [3:0](/zh-CN/docs/products/spot/sbe/schemas/spot_3_0.xml) 中，为每个 `enum` 添加了名为 `NonRepresentable` 的 `validValue`。接收到该值表示使用最新模式时有额外数据可用。
  * 在 SBE 模式 [3:1](/zh-CN/docs/products/spot/sbe/schemas/spot_3_1.xml) 中，添加了名为 `NonRepresentableMessage` 的消息。接收到该消息表示使用最新模式时有额外数据可用。该消息可能作为顶层消息接收，或当 `data` 字段的 `type` 为 `messageData`、`messageData8`、`messageData16`、`optionalMessageData` 或 `optionalMessageData16` 时嵌入在 `data` 字段中。
  * 关于模式生命周期的 `JSON` 文件将被保存在此仓库中，[请看这里](/zh-CN/docs/products/spot/sbe/schemas/introduction)。这个文件包含了关于实时交易所和现货测试网的最新、被废止和被停用模式的具体发生日期。 以下是一个基于上述假设时间线的 `JSON` 示例：


    
    
    Code
    
    {
      "environment": "PROD",
      "latestSchema": {
        "id": 2,
        "version": 1,
        "releaseDate": "3025-02-01"
      },
      "deprecatedSchemas": [
        {
          "id": 2,
          "version": 0,
          "releaseDate": "3024-08-01",
          "deprecatedDate": "3025-02-01"
        }
      ],
      "retiredSchemas": [
        {
          "id": 1,
          "version": 1,
          "releaseDate": "3024-03-01",
          "deprecatedDate": "3024-08-01",
          "retiredDate": "3025-02-01"
        },
        {
          "id": 1,
          "version": 0,
          "releaseDate": "3024-01-01",
          "deprecatedDate": "3024-03-01",
          "retiredDate": "3024-09-01"
        }
      ]
    }

### 生成解码器：

  1. 下载模式：


  * REST/WebSocket API：
    * [`spot_prod_latest.xml`](/zh-CN/docs/products/spot/sbe/schemas/spot_prod_latest.xml) 用于实时交易所。
    * [`spot_testnet_latest.xml`](/zh-CN/docs/products/spot/sbe/schemas/spot_testnet_latest.xml) 用于[现货测试网](https://testnet.binance.vision)。
  * FIX API：
    * [`spot_fix_prod_latest.xml`](/zh-CN/docs/products/spot/sbe/schemas/spot_fix_prod_latest.xml) 用于实时交易所。
    * [`spot_fix_testnet_latest.xml`](/zh-CN/docs/products/spot/sbe/schemas/spot_fix_testnet_latest.xml) 用于[现货测试网](https://testnet.binance.vision)。


  2. 克隆并构建 [`simple-binary-encoding`](https://github.com/real-logic/simple-binary-encoding)：


    
    
    Code
    
     $ git clone https://github.com/real-logic/simple-binary-encoding.git
     $ cd simple-binary-encoding
     $ ./gradlew

  3. 运行 `SbeTool` 代码生成器。（请参考这里分别使用[Java](https://github.com/binance/binance-sbe-java-sample-app), [C++](https://github.com/binance/binance-sbe-cpp-sample-app) 和 [Rust](https://github.com/binance/binance-sbe-rust-sample-app) 解码交易所信息 payload 的样本。）



#### 十进制字段编码

不同于 `FIX SBE` 的规范，十进制字段的尾数和指数字段被单独编码为原始字段，以便使负载量和消息内编码字段的数量达到最小化。

#### 时间戳字段编码

SBE响应中的时间戳(Timestamps)是以微秒为单位。这与包含毫秒时间戳的JSON响应不同。

#### 模式文件中的自定义字段属性

在模式文件中添加了一些以 `mbx:` 为前缀的字段属性，供文档使用：

  * `mbx:exponent`：指向对应于尾数字段的指数域
  * `mbx:jsonPath`：包含了 `JSON` 响应中相应字段的名称
  * `mbx:jsonValue`: 包含了 `JSON` 响应中等价 `ENUM` 值的名称
  * `mbx:defaultJsonValue`：包含 JSON 响应的默认值。



此页面是否有帮助？

Last modified on November 12, 2026

[挂钩订单（Pegged orders）](/zh-CN/docs/products/spot/faqs/pegged_orders)[智能订单路由 (SOR)](/zh-CN/docs/products/spot/faqs/sor_faq)