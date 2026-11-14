---
api_type: reference
source_type: llms_txt
version: ''
scope: crypto
asset_class: digital_asset
domain: exchanges
provider: kraken
provider_name: Kraken
product: api
product_id: kraken
source_url: 'https://docs.kraken.com/institutional/api-reference/prime-fix/logon'
updated_at: 2026-11-13
---

# Logon

> Authenticate and establish a FIX session using HMAC SHA-256 signature-based authentication.

The Logon message is used to authenticate and establish a FIX session. It includes signature-based authentication using HMAC SHA-256.

> [tab] FIX Specification
>
> **header** *required*
>
> MsgType `A`
>
> **108 - HeartBtInt** `integer` *required*
>
> Note same value used by both sides.
>
> **141 - ResetSeqNumFlag** `boolean`
>
> Indicates both sides of a FIX session should reset sequence numbers.
>
> **96 - RawData** `string` *required*
>
> Contains signature (see below for creating a signature).
>
> **554 - Password** `string` *required*
>
> Contains the API Key for the Customer user.
>
> **trailer** *required*

> [tab] Example
>
> **Logon Request:**
>
> ```text theme={null}
> 8=FIX.4.4|9=143|35=A|34=1|49=CUSTOMER|52=20220915-18:29:58.756|56={{ Customer }}|95=44|96=ZduZiNxyxS7_4UPDesOryd9KVEecg9LAqqTRR79Pp20=|98=0|108=60|141=Y|554=PMsU9ypImeJ0ad9X39ngzPYRA|10=248|
> ```
>
> **Logon Response:**
>
> ```text theme={null}
> 8=FIX.4.4|9=78|35=A|34=1|49={{ Customer }}|52=20220915-18:29:58.765|56=CUSTOMER|98=0|108=60|141=Y|10=255|
> ```

## Creating a Signature

The signature is created by concatenating:

* SendingTime (52) as a string
* ASCII 01 value
* SeqNum (34) as a string
* ASCII 01 value
* SenderCompID (49)
* ASCII 01 value
* TargetCompID (56)

This string is then signed using the HMAC SHA-256 Algorithm and the API Secret for the API Key.

### Sample Java Code

```java theme={null}
/**
 * Takes a Message, an apiKey and apiSecret and uses the HMAC-SHA256 algorithm to
 * sign a FIX message by appending the sending-time sequenceNumber, SenderCompID 
 * and TargetCompID with \u0001 separator and signing using the secret, putting it 
 * into the RawBytes in Base64 encoding.
 */
private static void signLogon(final Message message,
                              final SessionID sessionId,
                              final String apiKey,
                              final String apiSecret) throws FieldNotFound {
    final var senderCompId = sessionId.getSenderCompID();
    final var targetCompId = sessionId.getTargetCompID();
    final var sendingTime = message.getString(SendingTime.FIELD);
    final var seqNum = message.getInt(MsgSeqNum.FIELD);
    final var sep = "\u0001";
    
    final var hmac = sign(apiSecret, sendingTime + sep + seqNum + sep + 
                         senderCompId + sep + targetCompId);
    
    message.setString(Password.FIELD, apiKey);
    message.setInt(RawDataLength.FIELD, hmac.length());
    message.setString(RawData.FIELD, hmac);
}

private static String sign(final String apiSecret, final String data) {
    final var mac = HmacUtils.getInitializedMac(HmacAlgorithms.HMAC_SHA_256,
                                               apiSecret.getBytes());
    final var encodedBytes = mac.doFinal(data.getBytes());
    final var encoder = Base64.getUrlEncoder(); //URL Safe Base64
    return encoder.encodeToString(encodedBytes);
}
```

> [!NOTE]
>
> **Dependencies**
>
> This sample relies on Apache Commons-Codec and QuickFIX for Java.
