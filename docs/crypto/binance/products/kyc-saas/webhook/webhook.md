---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/kyc-saas/webhook/webhook
api_type: Guide
updated_at: 2026-11-20 18:39:59.221816
---

# Webhook

The webhook notifications function can be implemented by passing a `notifyUrl` when calling our KYC
endpoints to initialize KYC.

`notifyUrl` is a mandatory parameter when initiating KYC. If not required, you can pass a "."
instead.

:::warning

**`notifyUrl` cannot be modified once submitted.** The value is bound to the `kycUserId` at
submission time. There is currently no endpoint to change it, and resubmitting after a rejection
does **not** reset it. Point it at a stable endpoint before the first submission.

:::

Binance will send a POST request webhook to your notifyUrl when there are updates to the KYC record.

If the system's request to your notifyUrl fails, the system will auto retry as per the below policy:

- On first failure, retry in 3 minutes
- On second failure, retry in 5 minutes
- On third failure, retry in 10 minutes

### Request sample

```json
{
  "bizEntityKey": "BROKERKEY",
  "entityCustomerId": "45712345678999212345",
  "kycType": "USER",
  "eventType": "USER-STATUS",
  "eventVo": {
    "statusInfo": {
      "bizEntityKey": "BROKERKEY",
      "entityCustomerId": "45712345678999212345",
      "kycUserId": "45712345678999212345",
      "userType": "USER",
      "kycType": "USER",
      "kycStatus": "REJECT",
      "failReason": "This ID number has been used. Log in to your original account to complete the transaction.",
      "basicStatus": "PASS",
      "basicFailReason": "",
      "identityStatus": "REJECT",
      "identityFailReason": "This ID number has been used. Log in to your original account to complete the transaction.",
      "faceStatus": "REJECT",
      "faceFailReason": "This ID number has been used. Log in to your original account to complete the transaction.",
      "wckStatus": "INITIAL",
      "dbCreateTime": 1751010142158,
      "dbModifyTime": 1751010192997,
      "identityCompleteTime": 1751010192926,
      "faceCompleteTime": 1751010192931,
      "riskRateLevel": "MEDIUM",
      "riskRateScore": 31
    },
    "levelInfo": {
      "currentLevel": {
        "levelName": "INTERMEDIATE",
        "levelDesc": "INTERMEDIATE",
        "kycStatus": "REFUSED",
        "limit": {
          "fiatCurrency": "USD",
          "withdrawFiatDailyLimit": 20000,
          "cryptoCurrency": "BTC",
          "depositCryptoDailyLimit": -1,
          "withdrawCryptoDailyLimit": 100
        }
      },
      "kycPass": false,
      "hasMultipleLevels": false,
      "passedLevels": []
    },
    "basicInfo": {
      "id": 4581048056761212345,
      "bizEntityKey": "BROKERKEY",
      "bizKey": "BROKERKEY",
      "kycUserId": "45712345678999212345",
      "basicType": "USER",
      "basicStatus": "PASS",
      "firstName": "BO",
      "middleName": "testMiddleName",
      "lastName": "LI",
      "residentialCountry": "AE",
      "dob": "1986-08-14",
      "postalCode": "123456",
      "city": "bbb",
      "address": "aaa",
      "submitIp": "192.168.1.1",
      "dbCreateTime": 1751010142182,
      "dbModifyTime": 1751010142182,
      "country": "AE",
      "requestTime": 1751010142182,
      "requestIp": "192.168.1.1"
    }
  },
  "version": 1751010193080
}
```

### Notify Webhook Verification

1. Receive the webhook request body as String
2. Use the `HmacSHA256` algorithm to sign the request body String obtained in 1st step, and compare
   the value of request header - `X-SHA2-Signature` , if they are the same, then the request body is
   valid, otherwise invalid.

#### javascript example

```javascript
const crypto = require("crypto");

const secret = "<your_secret_key>";
const postData = "<webhook_request_body>";
const hash = crypto.createHmac("sha256", secret).update(postData).digest("hex");
```

#### java example

```java
import org.apache.commons.codec.binary.Hex;

import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;
import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;

public class App {
    public static void main(String[] args) throws Exception {

        String rawString = "<webhook_request_body>";
        Mac sha256Hmac = Mac.getInstance("HmacSHA256");
        SecretKeySpec secretKey = new SecretKeySpec("<your_secret_key>".getBytes(), "HmacSHA256");
        sha256Hmac.init(secretKey);
        String eventSignature = new String(Hex.encodeHex(sha256Hmac.doFinal(rawString.getBytes(StandardCharsets.UTF_8))));

        System.err.println(eventSignature);
    }
}
```

---

# Webhook

The webhook notifications function can be implemented by passing a `notifyUrl` when calling our KYC
endpoints to initialize KYC.

`notifyUrl` is a mandatory parameter when initiating KYC. If not required, you can pass a "."
instead.

:::warning

**`notifyUrl` cannot be modified once submitted.** The value is bound to the `kycUserId` at
submission time. There is currently no endpoint to change it, and resubmitting after a rejection
does **not** reset it. Point it at a stable endpoint before the first submission.

:::

Binance will send a POST request webhook to your notifyUrl when there are updates to the KYC record.

If the system's request to your notifyUrl fails, the system will auto retry as per the below policy:

- On first failure, retry in 3 minutes
- On second failure, retry in 5 minutes
- On third failure, retry in 10 minutes

### Request sample

```json
{
  "bizEntityKey": "BROKERKEY",
  "entityCustomerId": "45712345678999212345",
  "kycType": "USER",
  "eventType": "USER-STATUS",
  "eventVo": {
    "statusInfo": {
      "bizEntityKey": "BROKERKEY",
      "entityCustomerId": "45712345678999212345",
      "kycUserId": "45712345678999212345",
      "userType": "USER",
      "kycType": "USER",
      "kycStatus": "REJECT",
      "failReason": "This ID number has been used. Log in to your original account to complete the transaction.",
      "basicStatus": "PASS",
      "basicFailReason": "",
      "identityStatus": "REJECT",
      "identityFailReason": "This ID number has been used. Log in to your original account to complete the transaction.",
      "faceStatus": "REJECT",
      "faceFailReason": "This ID number has been used. Log in to your original account to complete the transaction.",
      "wckStatus": "INITIAL",
      "dbCreateTime": 1751010142158,
      "dbModifyTime": 1751010192997,
      "identityCompleteTime": 1751010192926,
      "faceCompleteTime": 1751010192931,
      "riskRateLevel": "MEDIUM",
      "riskRateScore": 31
    },
    "levelInfo": {
      "currentLevel": {
        "levelName": "INTERMEDIATE",
        "levelDesc": "INTERMEDIATE",
        "kycStatus": "REFUSED",
        "limit": {
          "fiatCurrency": "USD",
          "withdrawFiatDailyLimit": 20000,
          "cryptoCurrency": "BTC",
          "depositCryptoDailyLimit": -1,
          "withdrawCryptoDailyLimit": 100
        }
      },
      "kycPass": false,
      "hasMultipleLevels": false,
      "passedLevels": []
    },
    "basicInfo": {
      "id": 4581048056761212345,
      "bizEntityKey": "BROKERKEY",
      "bizKey": "BROKERKEY",
      "kycUserId": "45712345678999212345",
      "basicType": "USER",
      "basicStatus": "PASS",
      "firstName": "BO",
      "middleName": "testMiddleName",
      "lastName": "LI",
      "residentialCountry": "AE",
      "dob": "1986-08-14",
      "postalCode": "123456",
      "city": "bbb",
      "address": "aaa",
      "submitIp": "192.168.1.1",
      "dbCreateTime": 1751010142182,
      "dbModifyTime": 1751010142182,
      "country": "AE",
      "requestTime": 1751010142182,
      "requestIp": "192.168.1.1"
    }
  },
  "version": 1751010193080
}
```

### Notify Webhook Verification

1. Receive the webhook request body as String
2. Use the `HmacSHA256` algorithm to sign the request body String obtained in 1st step, and compare
   the value of request header - `X-SHA2-Signature` , if they are the same, then the request body is
   valid, otherwise invalid.

#### javascript example

```javascript
const crypto = require("crypto");

const secret = "<your_secret_key>";
const postData = "<webhook_request_body>";
const hash = crypto.createHmac("sha256", secret).update(postData).digest("hex");
```

#### java example

```java
import org.apache.commons.codec.binary.Hex;

import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;
import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;

public class App {
    public static void main(String[] args) throws Exception {

        String rawString = "<webhook_request_body>";
        Mac sha256Hmac = Mac.getInstance("HmacSHA256");
        SecretKeySpec secretKey = new SecretKeySpec("<your_secret_key>".getBytes(), "HmacSHA256");
        sha256Hmac.init(secretKey);
        String eventSignature = new String(Hex.encodeHex(sha256Hmac.doFinal(rawString.getBytes(StandardCharsets.UTF_8))));

        System.err.println(eventSignature);
    }
}
```