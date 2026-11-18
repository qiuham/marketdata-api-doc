---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/openservice/signature
api_type: Guide
updated_at: 2026-11-18 18:36:24.963175
---

# Description of External Interface Signature Authentication Algorithm

## <a name="signature"></a>Description of External Interface Signature Authentication Algorithm

### <a name="canonical"></a>Constructing Canonical Request String and Hashing

To use the **AK and SK** for signature generation and authentication, you first need to standardize
the content of the request and sign the content to call open APIs.

The pseudo-code of the HTTP request specification is as follows:

| <p>CanonicalRequest =</p><p>`      `HTTPRequestMethod + '\n' +</p><p>`      `CanonicalURI + '\n' +</p><p>`      `CanonicalQueryString + '\n' +</p><p>`      `HexEncode(Hash(RequestPayload))</p> |
| :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

#### <a name="method"></a>1. Construct HTTP Request Method (HTTPRequestMethod)

HTTP request method, ending with a newline character. Examples include GET, PUT, POST, etc. Here are
some examples of request methods:

| GET |
| :-- |

| POST |
| :--- |

#### <a name="uri"></a>2. Construct URI Parameter (CanonicalURI)

Definition: The Canonical URI, i.e. the request resource path, is the absolute path part of the URI.

Format: The URI paths are standardized according to RFC 3986, redundant and relative path parts are
removed, and each part of the path must be URI encoded. If the URI path does not end with "/", a "/"
is appended at the end.

| <p>GET</p><p>/mp-api/v1/apps/ozSQnakAm7apa6ew7crPYd/user-open-data/</p> |
| :---------------------------------------------------------------------- |

If the absolute path is empty, use a forward slash (/).

| <p>GET</p><p>/</p> |
| :----------------- |

| <p>POST</p><p>/mp-api/v1/apps/ozSQnakAm7apa6ew7crPYd/message/send/</p> |
| :--------------------------------------------------------------------- |

#### <a name="querystring"></a>3. Construct CanonicalQueryString

**Definition:** The query string, or an empty string if there are no query parameters. In other
words, the request after standardization presents an empty line without query parameters.

**Format:** The canonical query string needs to meet the following requirements:

Each parameter name and value is URI encoded according to the following rules:

- Do not URI encode any non-reserved characters as defined by RFC 3986. These include: A-Z, a-z,
  0-9, -, \_, ., and ~.
- All other characters are percent-encoded using the format %XY, where X and Y are hexadecimal
  characters (from 0-9 and A-F). For example, spaces must be encoded as %20, and special UTF-8
  characters must be formatted as "%XY%ZA%BC".

For each parameter, the format is "URI-encoded parameter name = URI-encoded parameter value". If
there is no parameter value, use an empty string instead, but don't omit the "=".

For example, the following string contains two parameters, where the value for the second parameter
'parm2' is empty.

| parm1=value1&parm2= |
| :------------------ |

Sort the parameter names in ascending order based on their character codes. This means that
parameter names starting with an uppercase 'F' sort before any names starting with a lowercase 'b'.

To create the canonical query string, begin with the first sorted parameter name.

| <p>GET</p><p>/mp-api/v1/apps/ozSQnakAm7apa6ew7crPYd/user-open-data/</p><p>openData=dGVzdGNvZGU</p> |
| :------------------------------------------------------------------------------------------------- |

| <p>POST</p><p>/mp-api/v1/apps/ozSQnakAm7apa6ew7crPYd/message/send/</p><p></p> |
| :---------------------------------------------------------------------------- |

#### <a name="payload"></a>4. The Body Content (RequestPayload)

**Definition:** The request message body. The message body undergoes two levels of conversion:
HexEncode(Hash(RequestPayload)), where Hash represents a function generating a message digest,
currently supporting the SHA-256 algorithm. HexEncode represents a function that returns the Base-16
encoding of the digest in lowercase letters. For instance, HexEncode("m") returns "6d", not "6D".
Each byte of input is represented as two hexadecimal characters.

When calculating the hash value of RequestPayload, for the scenario "RequestPayload==null", use an
empty string "" directly for calculation.

**Example:** This example uses a GET method, and the body is empty. The hash of the body (empty
string) is as follows:

| <p>GET</p><p>/mp-api/v1/apps/ozSQnakAm7apa6ew7crPYd/user-open-data/</p><p>openData=dGVzdGNvZGU</p><p>e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855</p> |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

| <p>POST</p><p>/mp-api/v1/apps/ozSQnakAm7apa6ew7crPYd/message/send/</p><p></p><p></p> |
| :----------------------------------------------------------------------------------- |

#### <a name="requeststring"></a>5. Hashing the Constructed Canonical Request String

| Lowercase(HexEncode(Hash.SHA256(CanonicalRequest))) |
| :-------------------------------------------------- |

**Example:** Here is how you would hash the canonical request string:

| <p>GET</p><p>/mp-api/v1/apps/ozSQnakAm7apa6ew7crPYd/user-open-data/</p><p>openData=dGVzdGNvZGU</p><p>e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855</p><p> </p><p># After encoding</p><p>e1b70e3bf69bd4be11ce20e94dc9f367e70bde420dc29ab591a6e06b8c3e872e</p> |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

```json body
// {"appId":"ozSQnakAm7apa6ew7crPYd","language":"en","parameters":[{"name":"result","value":"success"},{"name":"withdrawMoney","value":"100"}],"path":"pages/details/index?source=push","pushToken":"push_token_ozSQnakAm7apa6ew7crPYd_template1_ABVREdsgregsdfhy","template_id":"template1"}
```

| <p>POST</p><p>/mp-api/v1/apps/ozSQnakAm7apa6ew7crPYd/message/send/</p><p></p><p>Beac504b39b372cedaf81e272aadec27b590b00ccea0dc1607a290f6ba7722af</p><p></p><p># After encoding</p><p>647643a5642dceee80cafbfc89e6ead7ce59e70a80b598b814514b2fd9b1d432</p> |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

#### <a name="jwtpayload"></a>6. Assigning the Encoded String to the 'dig' Field of the JWT Payload

// GET

"payload":\{

`    `"iss":"APKADD5WRLZTBVTVCRJQ",

`    `"dig":"e1b70e3bf69bd4be11ce20e94dc9f367e70bde420dc29ab591a6e06b8c3e872e"

\}

//POST

"payload":\{

`    `"iss":"APKADD5WRLZTBVTVCRJQ",

`    `"dig":"647643a5642dceee80cafbfc89e6ead7ce59e70a80b598b814514b2fd9b1d432"

\}

### <a name="time"></a>Time in Signature

ts: timestamp, in seconds

"payload":\{

`    `"iss":"APKADD5WRLZTBVTVCRJQ",

`    `"dig":"e1b70e3bf69bd4be11ce20e94dc9f367e70bde420dc29ab591a6e06b8c3e872e",

`    `"ts":1647007152

\}

### <a name="jwtsign"></a>Generating JWT and Signing

#### <a name="paystruct"></a>1. Structure of JWT Payload

| **Name** | **Description**                                                                                                                                                                     | **Type** | **Required** |
| :------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------- | :----------- |
| iss      | The token issuer is AK of the access server or client.                                                                                                                              | string   | Yes          |
| dig      | The hashed HTTP canonical request string used to verify that the content has not been tampered with                                                                                 | string   | Yes          |
| ts       | <p>Signature time verification, which is a second-level GMT Unix Timestamp (the server will compare</p><p>this time with the server time, plus or minus cannot exceed 1 minute)</p> | number   | Yes          |

#### <a name="signtoken"></a>2. Using SK to Sign Token

The signature helps verify that the message hasn't been tampered with during transit. Moreover, for
tokens signed with a private key (SK), it confirms that the sender of the JWT is identical to what
they claim.

AK: APKADD5WRLZTBVTVCRJQ

SecretKey: KFFICLR4U72D0S4AB3W4LXECWVWEIE0DA2AAYKER514ZLV1U

"header":\{

`    `"alg":"HS256",

`    `"typ":"JWT"

\},

"payload":\{

`    `"iss":"APKADD5WRLZTBVTVCRJQ",

`    `"dig":"e1b70e3bf69bd4be11ce20e94dc9f367e70bde420dc29ab591a6e06b8c3e872e",

`    `"ts":1647007152

\},

"signature":"HMACSHA256(

`  `base64UrlEncode(header) + "." +

`  `base64UrlEncode(payload), "KFFICLR4U72D0S4AB3W4LXECWVWEIE0DA2AAYKER514ZLV1U")"

#### <a name="democode"></a>3. Sample Code Demo

##### <a name="javascript"></a>Javascript

```javascript
import axios from "axios";
import crypto from "crypto";
import jwt from "jsonwebtoken";

const config = {
  ak: "xxx",
  sk: "xx",
  appId: "xx",
  template_id: "xx",
};

const payload = {
  appId: config.appId,
  pushToken: "xx",
  templateId: config.template_id,
  language: "en",
  path: "pages/index/index",
  parameters: [
    {
      name: "result",
      data: "test2",
    },
    {
      name: "withdrawMoney",
      data: "test3",
    },
  ],
};

function requestWrapper({ apiHost, ak, sk }) {
  return async function request(url, method, data) {
    const param = "";
    const hash = crypto.createHash("sha256");

    hash.update(JSON.stringify(data) || "");
    const bodyHash = hash.digest("hex");

    console.log(`bodyHash`, bodyHash);

    const body = `${method.toUpperCase()}
${url}${url.endsWith("/") ? "" : "/"}
${param}
${bodyHash}`;

    console.log(body);

    const newHash = crypto.createHash("sha256");
    newHash.update(body);

    const token = await new Promise((resolve, reject) => {
      jwt.sign(
        JSON.stringify({
          iss: ak,
          dig: newHash.digest("hex"),
          ts: Math.floor(Date.now() / 1000),
        }),
        sk,
        { header: { alg: "HS256", typ: "JWT" } },
        function (err, token) {
          if (err) {
            reject(err);
          } else {
            resolve(token || "");
          }
        },
      );
    });
    console.log(`token`, token);

    return axios
      .request({
        url,
        baseURL: apiHost,
        method,
        data: JSON.stringify(data),
        headers: {
          "X-Mp-Open-Api-Token": token,
        },
      })
      .then((res) => res.data);
  };
}

const res = await requestWrapper({
  apiHost: "https://dip-cb.binanceapi.com",
  ak: config.ak,
  sk: config.sk,
})(`/mp-api/v1/apps/${config.appId}/message/send`, "POST", payload);

console.log(res, res);
```

### <a name="_ri4zwlxh2ec5"></a>Making API Requests with JWT Token

When interacting with the API, the generated JWT token should be added to the HTTP header as
follows:

**X-Mp-Open-Api-Token**:
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJBUEtBREQ1V1JMWlRCVlRWQ1JKUSIsImRpZyI6ImUxYjcwZTNiZjY5YmQ0YmUxMWNlMjBlOTRkYzlmMzY3ZTcwYmRlNDIwZGMyOWFiNTkxYTZlMDZiOGMzZTg3MmUiLCJ0cyI6MTY0NzAwNzE1Mn0.7OD8RGEyRHs4ieTZg52v6z263nV0eePXDe7WJQYkVn8

---

# Description of External Interface Signature Authentication Algorithm

## <a name="signature"></a>Description of External Interface Signature Authentication Algorithm

### <a name="canonical"></a>Constructing Canonical Request String and Hashing

To use the **AK and SK** for signature generation and authentication, you first need to standardize
the content of the request and sign the content to call open APIs.

The pseudo-code of the HTTP request specification is as follows:

| <p>CanonicalRequest =</p><p>`      `HTTPRequestMethod + '\n' +</p><p>`      `CanonicalURI + '\n' +</p><p>`      `CanonicalQueryString + '\n' +</p><p>`      `HexEncode(Hash(RequestPayload))</p> |
| :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

#### <a name="method"></a>1. Construct HTTP Request Method (HTTPRequestMethod)

HTTP request method, ending with a newline character. Examples include GET, PUT, POST, etc. Here are
some examples of request methods:

| GET |
| :-- |

| POST |
| :--- |

#### <a name="uri"></a>2. Construct URI Parameter (CanonicalURI)

Definition: The Canonical URI, i.e. the request resource path, is the absolute path part of the URI.

Format: The URI paths are standardized according to RFC 3986, redundant and relative path parts are
removed, and each part of the path must be URI encoded. If the URI path does not end with "/", a "/"
is appended at the end.

| <p>GET</p><p>/mp-api/v1/apps/ozSQnakAm7apa6ew7crPYd/user-open-data/</p> |
| :---------------------------------------------------------------------- |

If the absolute path is empty, use a forward slash (/).

| <p>GET</p><p>/</p> |
| :----------------- |

| <p>POST</p><p>/mp-api/v1/apps/ozSQnakAm7apa6ew7crPYd/message/send/</p> |
| :--------------------------------------------------------------------- |

#### <a name="querystring"></a>3. Construct CanonicalQueryString

**Definition:** The query string, or an empty string if there are no query parameters. In other
words, the request after standardization presents an empty line without query parameters.

**Format:** The canonical query string needs to meet the following requirements:

Each parameter name and value is URI encoded according to the following rules:

- Do not URI encode any non-reserved characters as defined by RFC 3986. These include: A-Z, a-z,
  0-9, -, \_, ., and ~.
- All other characters are percent-encoded using the format %XY, where X and Y are hexadecimal
  characters (from 0-9 and A-F). For example, spaces must be encoded as %20, and special UTF-8
  characters must be formatted as "%XY%ZA%BC".

For each parameter, the format is "URI-encoded parameter name = URI-encoded parameter value". If
there is no parameter value, use an empty string instead, but don't omit the "=".

For example, the following string contains two parameters, where the value for the second parameter
'parm2' is empty.

| parm1=value1&parm2= |
| :------------------ |

Sort the parameter names in ascending order based on their character codes. This means that
parameter names starting with an uppercase 'F' sort before any names starting with a lowercase 'b'.

To create the canonical query string, begin with the first sorted parameter name.

| <p>GET</p><p>/mp-api/v1/apps/ozSQnakAm7apa6ew7crPYd/user-open-data/</p><p>openData=dGVzdGNvZGU</p> |
| :------------------------------------------------------------------------------------------------- |

| <p>POST</p><p>/mp-api/v1/apps/ozSQnakAm7apa6ew7crPYd/message/send/</p><p></p> |
| :---------------------------------------------------------------------------- |

#### <a name="payload"></a>4. The Body Content (RequestPayload)

**Definition:** The request message body. The message body undergoes two levels of conversion:
HexEncode(Hash(RequestPayload)), where Hash represents a function generating a message digest,
currently supporting the SHA-256 algorithm. HexEncode represents a function that returns the Base-16
encoding of the digest in lowercase letters. For instance, HexEncode("m") returns "6d", not "6D".
Each byte of input is represented as two hexadecimal characters.

When calculating the hash value of RequestPayload, for the scenario "RequestPayload==null", use an
empty string "" directly for calculation.

**Example:** This example uses a GET method, and the body is empty. The hash of the body (empty
string) is as follows:

| <p>GET</p><p>/mp-api/v1/apps/ozSQnakAm7apa6ew7crPYd/user-open-data/</p><p>openData=dGVzdGNvZGU</p><p>e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855</p> |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

| <p>POST</p><p>/mp-api/v1/apps/ozSQnakAm7apa6ew7crPYd/message/send/</p><p></p><p></p> |
| :----------------------------------------------------------------------------------- |

#### <a name="requeststring"></a>5. Hashing the Constructed Canonical Request String

| Lowercase(HexEncode(Hash.SHA256(CanonicalRequest))) |
| :-------------------------------------------------- |

**Example:** Here is how you would hash the canonical request string:

| <p>GET</p><p>/mp-api/v1/apps/ozSQnakAm7apa6ew7crPYd/user-open-data/</p><p>openData=dGVzdGNvZGU</p><p>e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855</p><p> </p><p># After encoding</p><p>e1b70e3bf69bd4be11ce20e94dc9f367e70bde420dc29ab591a6e06b8c3e872e</p> |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

```json body
// {"appId":"ozSQnakAm7apa6ew7crPYd","language":"en","parameters":[{"name":"result","value":"success"},{"name":"withdrawMoney","value":"100"}],"path":"pages/details/index?source=push","pushToken":"push_token_ozSQnakAm7apa6ew7crPYd_template1_ABVREdsgregsdfhy","template_id":"template1"}
```

| <p>POST</p><p>/mp-api/v1/apps/ozSQnakAm7apa6ew7crPYd/message/send/</p><p></p><p>Beac504b39b372cedaf81e272aadec27b590b00ccea0dc1607a290f6ba7722af</p><p></p><p># After encoding</p><p>647643a5642dceee80cafbfc89e6ead7ce59e70a80b598b814514b2fd9b1d432</p> |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

#### <a name="jwtpayload"></a>6. Assigning the Encoded String to the 'dig' Field of the JWT Payload

// GET

"payload":\{

`    `"iss":"APKADD5WRLZTBVTVCRJQ",

`    `"dig":"e1b70e3bf69bd4be11ce20e94dc9f367e70bde420dc29ab591a6e06b8c3e872e"

\}

//POST

"payload":\{

`    `"iss":"APKADD5WRLZTBVTVCRJQ",

`    `"dig":"647643a5642dceee80cafbfc89e6ead7ce59e70a80b598b814514b2fd9b1d432"

\}

### <a name="time"></a>Time in Signature

ts: timestamp, in seconds

"payload":\{

`    `"iss":"APKADD5WRLZTBVTVCRJQ",

`    `"dig":"e1b70e3bf69bd4be11ce20e94dc9f367e70bde420dc29ab591a6e06b8c3e872e",

`    `"ts":1647007152

\}

### <a name="jwtsign"></a>Generating JWT and Signing

#### <a name="paystruct"></a>1. Structure of JWT Payload

| **Name** | **Description**                                                                                                                                                                     | **Type** | **Required** |
| :------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------- | :----------- |
| iss      | The token issuer is AK of the access server or client.                                                                                                                              | string   | Yes          |
| dig      | The hashed HTTP canonical request string used to verify that the content has not been tampered with                                                                                 | string   | Yes          |
| ts       | <p>Signature time verification, which is a second-level GMT Unix Timestamp (the server will compare</p><p>this time with the server time, plus or minus cannot exceed 1 minute)</p> | number   | Yes          |

#### <a name="signtoken"></a>2. Using SK to Sign Token

The signature helps verify that the message hasn't been tampered with during transit. Moreover, for
tokens signed with a private key (SK), it confirms that the sender of the JWT is identical to what
they claim.

AK: APKADD5WRLZTBVTVCRJQ

SecretKey: KFFICLR4U72D0S4AB3W4LXECWVWEIE0DA2AAYKER514ZLV1U

"header":\{

`    `"alg":"HS256",

`    `"typ":"JWT"

\},

"payload":\{

`    `"iss":"APKADD5WRLZTBVTVCRJQ",

`    `"dig":"e1b70e3bf69bd4be11ce20e94dc9f367e70bde420dc29ab591a6e06b8c3e872e",

`    `"ts":1647007152

\},

"signature":"HMACSHA256(

`  `base64UrlEncode(header) + "." +

`  `base64UrlEncode(payload), "KFFICLR4U72D0S4AB3W4LXECWVWEIE0DA2AAYKER514ZLV1U")"

#### <a name="democode"></a>3. Sample Code Demo

##### <a name="javascript"></a>Javascript

```javascript
import axios from "axios";
import crypto from "crypto";
import jwt from "jsonwebtoken";

const config = {
  ak: "xxx",
  sk: "xx",
  appId: "xx",
  template_id: "xx",
};

const payload = {
  appId: config.appId,
  pushToken: "xx",
  templateId: config.template_id,
  language: "en",
  path: "pages/index/index",
  parameters: [
    {
      name: "result",
      data: "test2",
    },
    {
      name: "withdrawMoney",
      data: "test3",
    },
  ],
};

function requestWrapper({ apiHost, ak, sk }) {
  return async function request(url, method, data) {
    const param = "";
    const hash = crypto.createHash("sha256");

    hash.update(JSON.stringify(data) || "");
    const bodyHash = hash.digest("hex");

    console.log(`bodyHash`, bodyHash);

    const body = `${method.toUpperCase()}
${url}${url.endsWith("/") ? "" : "/"}
${param}
${bodyHash}`;

    console.log(body);

    const newHash = crypto.createHash("sha256");
    newHash.update(body);

    const token = await new Promise((resolve, reject) => {
      jwt.sign(
        JSON.stringify({
          iss: ak,
          dig: newHash.digest("hex"),
          ts: Math.floor(Date.now() / 1000),
        }),
        sk,
        { header: { alg: "HS256", typ: "JWT" } },
        function (err, token) {
          if (err) {
            reject(err);
          } else {
            resolve(token || "");
          }
        },
      );
    });
    console.log(`token`, token);

    return axios
      .request({
        url,
        baseURL: apiHost,
        method,
        data: JSON.stringify(data),
        headers: {
          "X-Mp-Open-Api-Token": token,
        },
      })
      .then((res) => res.data);
  };
}

const res = await requestWrapper({
  apiHost: "https://dip-cb.binanceapi.com",
  ak: config.ak,
  sk: config.sk,
})(`/mp-api/v1/apps/${config.appId}/message/send`, "POST", payload);

console.log(res, res);
```

### <a name="_ri4zwlxh2ec5"></a>Making API Requests with JWT Token

When interacting with the API, the generated JWT token should be added to the HTTP header as
follows:

**X-Mp-Open-Api-Token**:
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJBUEtBREQ1V1JMWlRCVlRWQ1JKUSIsImRpZyI6ImUxYjcwZTNiZjY5YmQ0YmUxMWNlMjBlOTRkYzlmMzY3ZTcwYmRlNDIwZGMyOWFiNTkxYTZlMDZiOGMzZTg3MmUiLCJ0cyI6MTY0NzAwNzE1Mn0.7OD8RGEyRHs4ieTZg52v6z263nV0eePXDe7WJQYkVn8