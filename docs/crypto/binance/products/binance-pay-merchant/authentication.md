---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/binance-pay-merchant/authentication
api_type: Guide
updated_at: 2026-11-25 18:33:50.063124
---

# Binance Pay API: Authentication

The Binance Pay API uses API keys to authenticate requests. You can view and manage your API keys in
the [Binance Merchant Admin Portal](https://merchant.binance.com/en).

Your API keys carry many privileges, so be sure to keep them secure! Do not share your secret API
keys in publicly accessible areas such as GitHub, client-side code, and so forth.

All API requests must be made over HTTPS. Calls made over plain HTTP will fail. API requests without
authentication will also fail.

## Apply API identity key and API secret key

1. Register Merchant Account at Binance
2. Login merchant account and create new API identity key/API secret key
   [Binance Merchant Admin Portal](https://merchant.binance.com/en).

## Decryption instructions for merchant data sharing

Decryption Steps:

1. **Convert the Secret Key to an AES Key**: Use the secret key used for order creation via OPEN API
   to generate an AES key. This is done by hashing the secret key with the SHA-256 algorithm.
2. **Extract IV and Encrypted Data**: Base64 decode the shared data string (like payerDetail) to get
   a byte array. The first 12 bytes represent the initialization vector (IV) and the remaining bytes
   represent the encrypted data.
3. **Decrypt the Data**: Initialize a decryption cipher using the AES key and IV. Decrypt the
   encrypted data and convert the resulting byte array into a UTF-8 encoded string.

Sample java code

```java
import javax.crypto.Cipher;
import javax.crypto.spec.GCMParameterSpec;
import javax.crypto.spec.SecretKeySpec;
import java.nio.charset.StandardCharsets;
import org.apache.commons.codec.binary.Base64;
import org.apache.commons.codec.digest.DigestUtils;

class Scratch {

  public static void main(String[] args) throws Exception {
    String secretKey = "<secretKey>"; // Replace with the secretKey used during the order creation via OPEN API
    String sharedData = "<sharedData>"; // Replace with your shared data string

    String decryptedContent = decrypt(sharedData, secretKey);
    System.out.println(decryptedContent);
  }

  public static String decrypt(String sharedData, String secretKey) throws Exception {
    // Convert the secretKey from the order creation via OPEN API to an AES key using SHA-256
    byte[] aesKeyBytes = DigestUtils.sha256(secretKey.getBytes(StandardCharsets.UTF_8));

    // Decode Base64 shared data and extract IV and encrypted data
    byte[] decodedContent = Base64.decodeBase64(sharedData);
    byte[] iv = new byte[12];
    byte[] encryptedData = new byte[decodedContent.length - 12];
    System.arraycopy(decodedContent, 0, iv, 0, 12);
    System.arraycopy(decodedContent, 12, encryptedData, 0, encryptedData.length);

    // Decrypt data using the AES key and IV
    SecretKeySpec secretKeySpec = new SecretKeySpec(aesKeyBytes, "AES");
    Cipher cipher = Cipher.getInstance("AES/GCM/NoPadding");
    cipher.init(Cipher.DECRYPT_MODE, secretKeySpec, new GCMParameterSpec(128, iv));
    byte[] decryptedBytes = cipher.doFinal(encryptedData);

    // Convert decrypted byte array back to string
    return new String(decryptedBytes, StandardCharsets.UTF_8);
  }

}
```

Sample Input

```
String secretKey = "eqzxjex2apzoei900ubweocnlkfuhxhox0fgbmrjjbwr6qc1qdgou7uj50nmfujr";
String sharedData = "qlbXoEGDxFVMo2+emWFmS2Unesyi7fMnSV0XTIS0J7ErxGjWZ/3yWAJ/NKalJwTzyXFXJpINNFEoMLGlteRlyqR4V330WIuaJmMAMUyXwdrFaNWHw+wPvs3eGm+radsdNnIJ56xqbH57ya4h/nSzyOw=";
```

Sample Output

```
{"firstName":"Chris","lastName":"Paul","dateOfBirth":"1994-02-04","nationality":"BR","countryOfResidence":"BR"}
```

---

# Binance Pay API: Authentication

The Binance Pay API uses API keys to authenticate requests. You can view and manage your API keys in
the [Binance Merchant Admin Portal](https://merchant.binance.com/en).

Your API keys carry many privileges, so be sure to keep them secure! Do not share your secret API
keys in publicly accessible areas such as GitHub, client-side code, and so forth.

All API requests must be made over HTTPS. Calls made over plain HTTP will fail. API requests without
authentication will also fail.

## Apply API identity key and API secret key

1. Register Merchant Account at Binance
2. Login merchant account and create new API identity key/API secret key
   [Binance Merchant Admin Portal](https://merchant.binance.com/en).

## Decryption instructions for merchant data sharing

Decryption Steps:

1. **Convert the Secret Key to an AES Key**: Use the secret key used for order creation via OPEN API
   to generate an AES key. This is done by hashing the secret key with the SHA-256 algorithm.
2. **Extract IV and Encrypted Data**: Base64 decode the shared data string (like payerDetail) to get
   a byte array. The first 12 bytes represent the initialization vector (IV) and the remaining bytes
   represent the encrypted data.
3. **Decrypt the Data**: Initialize a decryption cipher using the AES key and IV. Decrypt the
   encrypted data and convert the resulting byte array into a UTF-8 encoded string.

Sample java code

```java
import javax.crypto.Cipher;
import javax.crypto.spec.GCMParameterSpec;
import javax.crypto.spec.SecretKeySpec;
import java.nio.charset.StandardCharsets;
import org.apache.commons.codec.binary.Base64;
import org.apache.commons.codec.digest.DigestUtils;

class Scratch {

  public static void main(String[] args) throws Exception {
    String secretKey = "<secretKey>"; // Replace with the secretKey used during the order creation via OPEN API
    String sharedData = "<sharedData>"; // Replace with your shared data string

    String decryptedContent = decrypt(sharedData, secretKey);
    System.out.println(decryptedContent);
  }

  public static String decrypt(String sharedData, String secretKey) throws Exception {
    // Convert the secretKey from the order creation via OPEN API to an AES key using SHA-256
    byte[] aesKeyBytes = DigestUtils.sha256(secretKey.getBytes(StandardCharsets.UTF_8));

    // Decode Base64 shared data and extract IV and encrypted data
    byte[] decodedContent = Base64.decodeBase64(sharedData);
    byte[] iv = new byte[12];
    byte[] encryptedData = new byte[decodedContent.length - 12];
    System.arraycopy(decodedContent, 0, iv, 0, 12);
    System.arraycopy(decodedContent, 12, encryptedData, 0, encryptedData.length);

    // Decrypt data using the AES key and IV
    SecretKeySpec secretKeySpec = new SecretKeySpec(aesKeyBytes, "AES");
    Cipher cipher = Cipher.getInstance("AES/GCM/NoPadding");
    cipher.init(Cipher.DECRYPT_MODE, secretKeySpec, new GCMParameterSpec(128, iv));
    byte[] decryptedBytes = cipher.doFinal(encryptedData);

    // Convert decrypted byte array back to string
    return new String(decryptedBytes, StandardCharsets.UTF_8);
  }

}
```

Sample Input

```
String secretKey = "eqzxjex2apzoei900ubweocnlkfuhxhox0fgbmrjjbwr6qc1qdgou7uj50nmfujr";
String sharedData = "qlbXoEGDxFVMo2+emWFmS2Unesyi7fMnSV0XTIS0J7ErxGjWZ/3yWAJ/NKalJwTzyXFXJpINNFEoMLGlteRlyqR4V330WIuaJmMAMUyXwdrFaNWHw+wPvs3eGm+radsdNnIJ56xqbH57ya4h/nSzyOw=";
```

Sample Output

```
{"firstName":"Chris","lastName":"Paul","dateOfBirth":"1994-02-04","nationality":"BR","countryOfResidence":"BR"}
```