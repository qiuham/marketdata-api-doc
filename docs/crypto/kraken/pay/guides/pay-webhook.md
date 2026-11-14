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
source_url: 'https://docs.kraken.com/pay/guides/pay-webhook'
updated_at: 2026-11-13
---

# Pay webhook notifications

> Handle Kraken Pay webhook notifications for payment status changes using JWT verification with ES256.

### Overview

Kraken Pay will notify your system via webhook when the payment status changes. You'll receive `POST` notifications for the following statuses:

```
- success
- failed
- cancelled
- expired
- declined
```

The payload is encoded and signed using [**JWT**](https://www.rfc-editor.org/rfc/rfc7519) with the `ES256` algorithm (ECDSA using P-256 and SHA-256) and the specified `kid`.
The `kid` is used to verify the signature by looking up the correct public key in the JWKS  available at **[https://www.kraken.com/.well-known/pay-callback-keys.json](https://www.kraken.com/.well-known/pay-callback-keys.json)**. \

A given `kid` will always point to the same key, so you can cache it forever.
You will only need to fetch the remote JWKS and update your local set if the JWT is signed with a new `kid`.

JWT expiration is set to 24 hours. **If you have to process the message past the expiry you can simply ignore it.**

### Claims

JWT claims have the following schema:

| Field | Type | Description |
| :- | :- | :- |
| `iss` | `string` | Issuer. Should always be `kraken-pay` |
| `aud` | `string` or `null` | Recipients that the JWT is intented for (unused) |
| `exp` | `number` | Expiration time. Unix timestamp in seconds |
| `payload.external_id` | `string` | Your unique ID for tracking the payment |
| `payload.status` | `string` | Payment status. `success`, `failed`, `cancelled`, `expired`, `declined` |
| `payload.customer_kraktag` | `string` or `null` | In the case of a pay request, Kraktag of the payer. In the case of a transfer or paylink, Kraktag of the recipient. If the notification is triggered by a cancelled or an expired paylink or pay request, this will be `null`. |

Because new fields could be added to the `payload` in the future, your deserialization implementation **should** handle unknown fields.

**Example**: Decoded JWT claims

```json theme={null}
{
  "iss": "kraken-pay",
  "aud": null,
  "exp": 1749547869,
  "payload": {
    "external_id": "GSoAAAAAAAA",
    "status": "success",
    "customer_kraktag": "bob"
  }
}
```

### Webhook response

On successful validation of the payload your endpoint **must** return a `200` code with the following `JSON` payload:

```json theme={null}
{
  "code": "success"
}
```

**Anything else will be treated as an error.**

### Examples

#### Decode and validate JWT

The following are Rust and PHP examples of how to decode the JWT and validate its signature.

| Type | Value |
| - | :- |
| Private key | <pre>-----BEGIN PRIVATE KEY----- MIGHAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBG0wawIBAQQgCfJ5HUY3VRpKR7rb f60ba2BMvRSoZCyqnscwBvf+HlGhRANCAARtlMp6bYdgBIuEn3b/tmIRnJ6O6+Zf 9NhKpuKPe7Vj76Vv5mohvNczcM0sWjo6OEQ6jngzD5wMTWIhXvRcyRtO -----END PRIVATE KEY-----  </pre> |
| Algorithm | `ES256` |
| kid | `test-pay-callback-1` |
| JWT | `eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6InRlc3QtcGF5LWNhbGxiYWNrLTEifQ.eyJpc3MiOiJrcmFrZW4tcGF5IiwiYXVkIjpudWxsLCJleHAiOjE3NDk1NDc4NjksInBheWxvYWQiOnsiZXh0ZXJuYWxfaWQiOiJHU29BQUFBQUFBQSIsInN0YXR1cyI6InN1Y2Nlc3MiLCJjdXN0b21lcl9rcmFrdGFnIjoiYm9iIn19.dmlaZ0sdPVodkytuv8IFUj4Sbn0wpywzW51itWCh7dHX-bELdhkwE8pVpIyRYGP42TtyBChbVKwXEfd2-uxTHQ` |

> [tab] Rust
>
> ```rust theme={null}
> use std::{str::FromStr, sync::LazyLock};
>
> use actix_web::{error, post, App, Error, HttpResponse, HttpServer};
> use anyhow::anyhow;
> use chrono::{serde::ts_seconds, DateTime, Utc};
> use jsonwebtoken::{decode_header, jwk::JwkSet, Algorithm, DecodingKey, TokenData, Validation};
> use serde::{Deserialize, Serialize};
> use url::Url;
>
> static JWT_VERIFIER: LazyLock<JwtVerifier> = LazyLock::new(|| JwtVerifier::new().unwrap());
>
> #[post("/")]
> async fn index(token: String) -> Result<HttpResponse, Error> {
>     let token_data = JWT_VERIFIER
>         .validate_via_kid(&token)
>         .await
>         .map_err(error::ErrorBadRequest)?;
>
>     // Do something with the payload
>     let notification = token_data.claims.payload;
>     println!("Got Kraken Pay notification: {notification:#?}");
>
>     Ok(HttpResponse::Ok().json(CallbackResponse {
>         code: PayResponseCode::Success,
>     }))
> }
>
> #[derive(Clone, Debug, Eq, PartialEq, Serialize, Deserialize)]
> pub enum PayResponseCode {
>     Success,
> }
>
> #[derive(Clone, Debug, Eq, PartialEq, Serialize, Deserialize)]
> pub struct CallbackResponse {
>     pub code: PayResponseCode,
> }
>
> #[actix_web::main]
> async fn main() -> std::io::Result<()> {
>     HttpServer::new(|| App::new().service(index))
>         .bind(("127.0.0.1", 8080))?
>         .run()
>         .await
> }
>
> #[derive(Clone, Debug, PartialEq, Eq, Serialize, Deserialize)]
> struct Claims {
>     /// Issuer.
>     iss: String,
>     /// Audience.
>     aud: Option<String>,
>     /// Time beyond which the JWT is no longer valid
>     #[serde(with = "ts_seconds")]
>     exp: DateTime<Utc>,
>     /// Notification payload
>     payload: Notification,
> }
>
> #[derive(Clone, Debug, Eq, PartialEq, Serialize, Deserialize)]
> struct Notification {
>     external_id: String,
>     status: PayStatus,
>     customer_kraktag: Option<String>,
> }
>
> #[derive(Clone, Debug, Eq, PartialEq, Serialize, Deserialize)]
> #[serde(rename_all = "kebab-case")]
> enum PayStatus {
>     Success,
>     Failed,
>     Cancelled,
>     Expired,
>     Declined,
> }
>
> struct JwtVerifier {
>     validation: Validation,
>     jwks: JwkSet,
>     jwks_url: Url,
>     http: reqwest::Client,
> }
>
> impl JwtVerifier {
>     fn new() -> anyhow::Result<Self> {
>         let mut validation = Validation::new(Algorithm::ES256);
>         validation.set_issuer(&["kraken-pay"]);
>
>         let jwks = jwk_set();
>         let http = reqwest::Client::builder()
>             .user_agent("Mozilla/5.0 (X11; Linux x86_64; rv:133.0) Gecko/20100101 Firefox/133.0")
>             .timeout(std::time::Duration::from_secs(10))
>             .build()?;
>         let jwks_url = Url::from_str("https://www.kraken.com/.well-known/pay-callback-keys.json")?;
>
>         Ok(Self {
>             validation,
>             jwks,
>             jwks_url,
>             http,
>         })
>     }
>
>     /// Validate JWT via `kid`. If the key is present in the local JWKS then read from it,
>     /// otherwise fetch the remote JWKS.
>     async fn validate_via_kid(&self, token: &str) -> anyhow::Result<TokenData<Claims>> {
>         let header = decode_header(token)?;
>         let kid = header.kid.as_deref().ok_or(anyhow!("JWT has no kid"))?;
>
>         let decoding_key = {
>             if let Some(jwk) = self.jwks.find(kid) {
>                 DecodingKey::from_jwk(jwk)?
>             } else {
>                 let jwks: JwkSet = self
>                     .http
>                     .get(self.jwks_url.clone())
>                     .send()
>                     .await?
>                     .json()
>                     .await?;
>                 let jwk = jwks.find(kid).ok_or(anyhow!("Cannot find key in jwks"))?;
>                 DecodingKey::from_jwk(jwk)?
>             }
>         };
>
>         Ok(jsonwebtoken::decode(
>             token,
>             &decoding_key,
>             &self.validation,
>         )?)
>     }
> }
>
> fn jwk_set() -> JwkSet {
>     let jwk_text = r#"{
>       "keys": [
>         {
>           "alg": "ES256",
>           "kty": "EC",
>           "kid": "test-pay-callback-1",
>           "crv": "P-256",
>           "x": "bZTKem2HYASLhJ92_7ZiEZyejuvmX_TYSqbij3u1Y-8",
>           "y": "pW_maiG81zNwzSxaOjo4RDqOeDMPnAxNYiFe9FzJG04"
>         }
>       ]
>     }"#;
>
>     serde_json::from_str(jwk_text).unwrap()
> }
> ```

> [tab] PHP
>
> ```php theme={null}
> <?php
>
> // This script uses composer to import the JWT library
> // $ composer require firebase/php-jwt
> // $ composer require paragonie/sodium_compat
> // $ php -S localhost:8080 listener.php
>
> require_once "vendor/autoload.php";
> use Firebase\JWT\JWK;
> use Firebase\JWT\JWT;
>
> // Local set of keys
> $jwks = json_decode(
>     '{
>         "keys": [
>           {
>             "alg": "ES256",
>             "kty": "EC",
>             "kid": "test-pay-callback-1",
>             "crv": "P-256",
>             "use": "sig",
>             "x": "bZTKem2HYASLhJ92_7ZiEZyejuvmX_TYSqbij3u1Y-8",
>             "y": "pW_maiG81zNwzSxaOjo4RDqOeDMPnAxNYiFe9FzJG04"
>           }
>         ]
>     }',
>     true
> );
>
>
> function get_method()
> {
>     return $_SERVER["REQUEST_METHOD"];
> }
>
> function get_request_data()
> {
>     return file_get_contents("php://input", true);
> }
>
> function send_response($response, $code = 200)
> {
>     http_response_code($code);
>     $response = json_encode($response);
>     error_log("Response: ". $response);
>     die($response);
> }
>
> function decode_headers($jwt)
> {
>     // Decode headers from the JWT string WITHOUT validation
>     list($headersB64, $payloadB64, $sig) = explode(".", $jwt);
>     $decoded = json_decode(base64_decode($headersB64), true);
>     return $decoded;
> }
>
>
> function update_jwks(&$jwks)
> {
>     $ch = curl_init();
>     curl_setopt($ch, CURLOPT_URL, "https://www.kraken.com/.well-known/pay-callback-keys.json");
>     curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
>     $output = curl_exec($ch);
>     curl_close($ch);
>     $remote_keys = json_decode($output, true);
>     $remote_keys = $remote_keys["keys"];
>
>     $jwks["keys"] = array_merge($jwks["keys"], $remote_keys);
> }
>
> function validate_jwt_via_kid($jwt, &$jwks)
> {
>     $headers = decode_headers($jwt);
>     $kid = $headers["kid"];
>     $keys = $jwks["keys"];
>
>     $found = false;
>     foreach ($keys as $key) {
>         if ($key["kid"] == $kid) {
>             $found = true;
>         }
>     }
>     if (!$found) {
>         throw new Exception("kid not found in JWKS");
>     }
>
>     $decoded = null;
>     try {
>         $keySet = JWK::parseKeySet($jwks);
>         $decoded = JWT::decode($jwt, $keySet);
>         $decoded = json_decode(json_encode($decoded), true);
>     } catch (Exception $e) {
>         $exception = $e->getMessage();
>         // Ignore expired token if needed
>         if ($exception == "Expired token") {
>             error_log("Ignoring expired token");
>             list($header, $payload, $signature) = explode(".", $jwt);
>             $decoded = base64_decode($payload);
>             $decoded = json_decode($decoded, true);
>         } else {
>             send_response(array(
>                 "code" => 400,
>                 "status" => "failed",
>                 "message" => $exception
>             ), 400);
>         }
>     }
>
>     $iss = $decoded["iss"];
>     if ($iss != "kraken-pay") {
>         send_response(array(
>             "code" => 400,
>             "status" => "failed",
>             "message" => "Unexpected issuer: " . $iss
>         ), 400);
>     }
>
>     return $decoded;
> }
>
> $method = get_method();
> if ($method === "POST") {
>     $data = get_request_data();
>     $decoded = null;
>     try {
>         $decoded = validate_jwt_via_kid($data, $jwks);
>     } catch (Exception $e) {
>         $exception = $e->getMessage();
>         if ($exception == "kid not found in JWKS") {
>             error_log("kid not found in JWKS, fetching remote JWKS");
>             update_jwks($jwks);
>             $decoded = validate_jwt_via_kid($data, $jwks);
>         }
>     }
>
>     // Do something with the payload
>     error_log("Got Kraken Pay notification: " . json_encode($decoded));
>
>     // All good
>     send_response([
>         "code" => "success",
>     ]);
> }
>
> // Error for any other method
> send_response(array(
>     "code" => 405,
>     "status" => "failed",
>     "message" => "Method not allowed"
> ), 405);
> ```
