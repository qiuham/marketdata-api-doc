---
exchange: bitget
source_url: https://www.bitget.com/docs/uta/sdk/java
api_type: Guide
updated_at: 2026-11-27 19:02:07.491320
---

# Java

Official Java SDK for the Bitget API.

**Code path**:`com.bitget.openapi.api.v2`

## Install

Add the Maven dependency:

```xml
<dependency>
  <groupId>com.bitget.openapi</groupId>
  <artifactId>bitget-java-sdk-api</artifactId>
  <version>{version}</version>
</dependency>
```

Or clone and build from source:

```bash
git clone https://github.com/BitgetLimited/v3-bitget-api-sdk.git
cd bitget-java-sdk-api
mvn clean install
```

## Usage

Initialize the REST client with your credentials:

```java
ClientParameter parameter = ClientParameter.builder()
    .apiKey(apiKey)
    .secretKey(secretKey)
    .passphrase(passphrase)
    .baseUrl(baseUrl)
    .build();

BitgetRestClient client = BitgetRestClient.builder()
    .configuration(parameter)
    .build();
```

More: [Java SDK](https://github.com/BitgetLimited/v3-bitget-api-sdk/tree/master/bitget-java-sdk-api)

---

# Java

Bitget 官方 Java SDK。

**代码路径**：`com.bitget.openapi.api.v2`

## 安装

Add the Maven dependency:

```xml
<dependency>
  <groupId>com.bitget.openapi</groupId>
  <artifactId>bitget-java-sdk-api</artifactId>
  <version>{version}</version>
</dependency>
```

Or clone and build from source:

```bash
git clone https://github.com/BitgetLimited/v3-bitget-api-sdk.git
cd bitget-java-sdk-api
mvn clean install
```

## 使用

Initialize the REST client with your credentials:

```java
ClientParameter parameter = ClientParameter.builder()
    .apiKey(apiKey)
    .secretKey(secretKey)
    .passphrase(passphrase)
    .baseUrl(baseUrl)
    .build();

BitgetRestClient client = BitgetRestClient.builder()
    .configuration(parameter)
    .build();
```

更多：[Java SDK](https://github.com/BitgetLimited/v3-bitget-api-sdk/tree/master/bitget-java-sdk-api)