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
source_url: 'https://docs.kraken.com/exchange/api-reference/unified-fix/logon'
updated_at: 2026-11-13
---

# Logon

> Authenticate and establish a FIX session

FIX
session: admin
35=A

The Logon message (`35=A`) must be the **first message** sent after establishing the TCP connection. It authenticates the session and sets session-level parameters.

If logon succeeds, Kraken responds with a Logon message. If it fails, Kraken sends a Logout with a reason, or silently closes the connection.

> [!WARNING]
>
> All FIX connections require **TLS**. The server rejects plain TCP connections with a TLS alert. Use `TLSv1.2` or higher. Certificate verification can be skipped for UAT; use full verification in production.

***

## Session Types

Kraken FIX offers two session types that use **different TargetCompIDs** and have different authentication requirements:

| | Market Data | Trading |
| - | - | - |
| **TargetCompID (56)** | `KRAKEN-MD` | `KRAKEN-TRD` |
| **Authentication required** | No | Yes (API Key + Password) |
| **Fields 553, 554, 5025** | Not required | Required |
| **Purpose** | Subscribe to order book, trades, OHLC | Place/cancel orders, account data |

> [!NOTE]
>
> Spot and Derivatives use separate SenderCompIDs. Your Derivatives SenderCompID will have a `DRV` suffix. Both are provided by Kraken during onboarding.

***

## Fields

**header** *required*

35=`A`

**98 - EncryptMethod** `integer` *required*

Always set to `0` (None).

**108 - HeartBtInt** `integer` *required*

Heartbeat interval in seconds. Recommended value: `60`.

**553 - UserName** `string`

Your FIX API Key. Create it in [Kraken Pro settings](https://pro.kraken.com/app/settings/api) with **FIX** as the key type.

Condition: Trading session only

**554 - Password** `string`

HMAC-SHA512 signature. See [Password Generation](#password-generation) below.

Condition: Trading session only

**5025 - Nonce** `string`

Current timestamp in milliseconds since Unix epoch, as a string.

> [!WARNING]
>
> The nonce must be within **±5 seconds** of Kraken's server time. Clock drift is the most common cause of logon failures. Use NTP to keep your system clock in sync.

Condition: Trading session only

**109 - ClientID** `integer`

Associates this connection with another connection (e.g. linking a trading session to a market data session).

**141 - ResetSeqNumFlag** `boolean`

If `Y`, both sides reset their sequence numbers to `1`. Use on initial connect or after a session reset. Default: `N`.

**8674 - CancelOrdersOnDisconnect** `integer`

Controls what happens to open orders if the session disconnects.

**Possible values:**

* `0` — Cancel all open orders placed during this session *(default)*
* `1` — Leave open orders in place after disconnect

**5030 - ForceResetClOrdID** `boolean`

Resets your ClOrdID sequence on re-logon. Use in emergencies only. Default: `N`.

**5051 - Rebased** `boolean`

Applies to xStocks trading only.

* `N` — Orders and execution reports use SPV token quantities *(default)*
* `Y` — Orders and execution reports use underlying equity quantities (Kraken applies the multiplier automatically)

**trailer** *required*

***

## Password Generation

The password is computed as:

```
base64( HMAC-SHA512( base64decode(API_Secret), SHA256(MessageInput + Nonce) ) )
```

**MessageInput** is the concatenation of these fields using the FIX separator (SOH = `\x01`):

```
35=A  +SOH+  34=<MsgSeqNum>  +SOH+  49=<SenderCompID>  +SOH+  56=KRAKEN-TRD  +SOH+  553=<API_Key>  +SOH
```

> [!WARNING]
>
> The API Secret must be **base64-decoded** before use as the HMAC key.

Both the `Nonce` (tag 5025) and the value used in `MessageInput` must be **identical**. Generate nonce once and use it in both places.

```python Python theme={null}
import base64
import hashlib
import hmac
import time

SOH = "\x01"

def get_password(msg_seq_num: str, sender_comp_id: str, api_key: str, api_secret: str):
    nonce = str(int(time.time() * 1000))

    message_input = (
        f"35=A{SOH}"
        f"34={msg_seq_num}{SOH}"
        f"49={sender_comp_id}{SOH}"
        f"56=KRAKEN-TRD{SOH}"
        f"553={api_key}{SOH}"
    )

    sha256_hash = hashlib.sha256((message_input + nonce).encode("utf-8")).digest()
    hmac_hash = hmac.new(base64.b64decode(api_secret), sha256_hash, hashlib.sha512)
    password = base64.b64encode(hmac_hash.digest()).decode("utf-8")

    return password, nonce
```

```javascript Node.js theme={null}
const crypto = require('crypto');

const SOH = '\x01';

function getPassword(msgSeqNum, senderCompId, apiKey, apiSecret) {
  const nonce = Date.now().toString();

  const messageInput =
    `35=A${SOH}` +
    `34=${msgSeqNum}${SOH}` +
    `49=${senderCompId}${SOH}` +
    `56=KRAKEN-TRD${SOH}` +
    `553=${apiKey}${SOH}`;

  const sha256Hash = crypto
    .createHash('sha256')
    .update(messageInput + nonce, 'utf8')
    .digest();

  const password = crypto
    .createHmac('sha512', Buffer.from(apiSecret, 'base64'))
    .update(sha256Hash)
    .digest('base64');

  return { password, nonce };
}
```

```java Java theme={null}
import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;
import java.security.MessageDigest;
import java.util.Base64;

public class FIXAuth {
    private static final char SOH = '\u0001';

    public static String[] getPassword(
            String msgSeqNum, String senderCompId,
            String apiKey, String apiSecret) throws Exception {

        String nonce = String.valueOf(System.currentTimeMillis());

        String messageInput =
            "35=A" + SOH +
            "34=" + msgSeqNum + SOH +
            "49=" + senderCompId + SOH +
            "56=KRAKEN-TRD" + SOH +
            "553=" + apiKey + SOH;

        byte[] sha256Hash = MessageDigest
            .getInstance("SHA-256")
            .digest((messageInput + nonce).getBytes("UTF-8"));

        Mac hmac = Mac.getInstance("HmacSHA512");
        hmac.init(new SecretKeySpec(Base64.getDecoder().decode(apiSecret), "HmacSHA512"));
        String password = Base64.getEncoder().encodeToString(hmac.doFinal(sha256Hash));

        return new String[]{ password, nonce };
    }
}
```

```go Go theme={null}
package main

import (
	"crypto/hmac"
	"crypto/sha256"
	"crypto/sha512"
	"encoding/base64"
	"fmt"
	"strconv"
	"time"
)

const SOH = "\x01"

func getPassword(msgSeqNum, senderCompID, apiKey, apiSecret string) (password, nonce string, err error) {
	nonce = strconv.FormatInt(time.Now().UnixMilli(), 10)

	messageInput :=
		"35=A" + SOH +
		"34=" + msgSeqNum + SOH +
		"49=" + senderCompID + SOH +
		"56=KRAKEN-TRD" + SOH +
		"553=" + apiKey + SOH

	sha256Hash := sha256.Sum256([]byte(messageInput + nonce))

	secretBytes, err := base64.StdEncoding.DecodeString(apiSecret)
	if err != nil {
		return "", "", fmt.Errorf("failed to decode API secret: %w", err)
	}

	mac := hmac.New(sha512.New, secretBytes)
	mac.Write(sha256Hash[:])
	password = base64.StdEncoding.EncodeToString(mac.Sum(nil))

	return password, nonce, nil
}
```

```csharp C# theme={null}
using System;
using System.Security.Cryptography;
using System.Text;

public static class FIXAuth
{
    private const char SOH = '\x01';

    public static (string Password, string Nonce) GetPassword(
        string msgSeqNum, string senderCompId,
        string apiKey, string apiSecret)
    {
        string nonce = DateTimeOffset.UtcNow.ToUnixTimeMilliseconds().ToString();

        string messageInput =
            $"35=A{SOH}" +
            $"34={msgSeqNum}{SOH}" +
            $"49={senderCompId}{SOH}" +
            $"56=KRAKEN-TRD{SOH}" +
            $"553={apiKey}{SOH}";

        byte[] sha256Hash = SHA256.HashData(Encoding.UTF8.GetBytes(messageInput + nonce));

        using var hmac = new HMACSHA512(Convert.FromBase64String(apiSecret));
        string password = Convert.ToBase64String(hmac.ComputeHash(sha256Hash));

        return (password, nonce);
    }
}
```

***

## Message Examples

```text Spot MD Logon (client → server) theme={null}
8=FIX.4.4|9=76|35=A|34=1|49=CLIENT|56=KRAKEN-MD|52=20260407-14:32:01.000|98=0|108=30|141=Y|10=089|
```

```text Spot TRD Logon (client → server) theme={null}
8=FIX.4.4|9=77|35=A|34=1|49=CLIENT|56=KRAKEN-TRD|52=20260407-14:32:01.000|98=0|108=30|141=Y|10=179|
```

```text Spot TRD Logon Ack (server → client) theme={null}
8=FIX.4.4|9=77|35=A|34=1|49=KRAKEN-TRD|56=CLIENT|52=20260407-14:32:01.000|98=0|108=30|141=Y|10=179|
```

```text Futures TRD Logon (client → server) theme={null}
8=FIX.4.4|9=85|35=A|34=1|49=CLIENT-DRV|56=KRAKEN-DRV-TRD|52=20260407-14:32:01.000|98=0|108=30|141=Y|10=228|
```

```text Futures TRD Logon Ack (server → client) theme={null}
8=FIX.4.4|9=85|35=A|34=1|49=KRAKEN-DRV-TRD|56=CLIENT-DRV|52=20260407-14:32:01.000|98=0|108=30|141=Y|10=228|
```
