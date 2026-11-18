---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/login/web-integration
api_type: Guide
updated_at: 2026-11-18 02:00:27.004824
---

# Integrate Binance Login with your web application

# Using OAuth to Access Binance API

Binance APIs utilize the [OAuth 2.0](https://tools.ietf.org/html/rfc6749) protocol for
authentication and authorization. Binance supports common OAuth 2.0 scenarios such as those for web
server, single page (browser based), mobile and native applications. This document will guide you
through how your application communicates with Binance's OAuth 2.0 server to secure a user's consent
for performing an API request on his behalf.

To begin, your application must identify the necessary permissions, or `scopes`. Visit the
[Binance Developer Center](https://developers.binance.com/en/oauth-management), sign up for a
Binance entity account, and from there, navigate to your console to create an OAuth application and
get your own client ID and client secret. For now, Binance Login (Oauth2.0), is exclusively offered
to close ecosystem partners. Please reach to our business team for further information.

Depending on your specific application type, you can select one of the two different authorization
flows listed here:

1. For web applications, please refer to the ‘Authorization Code Flow’ section;
2. For browser-based applications as well as mobile and native applications, please refer to the
   ‘PCKE Flow’ section.

## 1. Authorization Code Flow

### Step 1. Redirect users to request Binance access and set authorization parameters.

```
GET https://accounts.binance.com/en/oauth/authorize?
    response_type=code&
    client_id=YOUR_CLIENT_ID&
    redirect_uri=YOUR_REDIRECT_URI&
    state=CSRF_TOKEN&
    scope=SCOPES
```

> ⚠️ The carriage returns of the above example are only for readability and should be removed in
> real world, as well as the following examples

When redirecting a user to Binance to authorize access to your application, your first step is to
create the authorization request.

| Parameters      | Description                                                                                                                          |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| `response_type` | **Required** Value `code`                                                                                                            |
| `client_id`     | **Required** The client ID of your application.                                                                                      |
| `redirect_uri`  | **required** The URL in your web application where users will be redirected after authorization. This value needs to be URL encoded. |
| `state`         | **Optional** The CSRF token to protect against CSRF (cross-site request forgery) attacks.                                            |
| `scope`         | **required** List of scopes enum your application requests access to, with comma (`,`) seperated.                                    |

Here is an Example of an authorization URL:

```
GET https://accounts.binance.com/en/oauth/authorize?
    response_type=code&
    client_id=a28f296f2cbe6c64b4d5dec24735d39b1b6fffcf&
    redirect_uri=https%3A%2F%2Fdomain.com%2Foauth%2Fcallback&
    state=377f36a4557ab5935b36&
    scope=user:openId,create:apikey
```

### Step 2. Binance prompts user for consent

In this step, the user decides whether to grant your application the requested access. At this
stage, Binance displays a consent window that shows the name of your application and the Binance API
services that it is requesting permission to access with the user's authorization credentials. The
user can then consent or refuse to grant access to your application.

Your application doesn't need to do anything at this stage as it waits for Binance's OAuth 2.0
server to redirect back.

### Step 3. Binance redirects back to your application

If the user approves your application, Binance's OAuth server will redirect back to your
`redirect_uri` with a temporary authorization `code` parameter.

If you specified a `state` parameter in step 1, the parameter will be included as well. If you
generate a random string or encode the hash of a cookie or another value that captures the client's
`state`, you can validate the response to additionally ensure that the request and response
originated in the same browser, providing protection against attacks such as cross-site request
forgery.

Example of the redirection:

```
GET https://domain.com/oauth/callback?
    code=cf6941ae8918b6a008f1377f36a4557ab5935b36&
    state=377f36a4557ab5935b36
```

> `state` is the same as the one in step 1

### Step 4. Exchange authorization code for refresh and access tokens

After your application receives the authorization `code`, it can exchange the authorization `code`
for an access token, which can be done by make a POST call:

```
POST https://accounts.binance.com/oauth/token?client_id=YOUR_CLIENT_ID&client_secret=YOUR_CLIENT_SECRET&grant_type=authorization_code&code=STEP3_CODE&redirect_uri=YOUR_REDIRECT_URI
```

| Parameter       | Description                                                                                                                          |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| `grant_type`    | **required** Value `authorization_code`                                                                                              |
| `code`          | **required** Step3 return code                                                                                                       |
| `client_id`     | **required** The client ID of your application.                                                                                      |
| `client_secret` | **required** The client secret of your application.                                                                                  |
| `redirect_uri`  | **required** The URL in your web application where users will be redirected after authorization. This value needs to be URL encoded. |

Example POST call:

```sh
curl https://accounts.binance.com/oauth/token \
  -X POST
  -d 'client_id=je-client&client_secret=je-client-secret&grant_type=authorization_code&code=95OfIm&redirect_uri=https%3A%2F%2Fdomain.com%2Foauth%2Fcallback'
```

After a successful request, a valid `access_token` will be returned in the response and it will be
invalid if it exceeds the `expires_in` time in the response, which is in seconds.

Here is an example response:

```json
{
  "access_token": "83f2bf51-a2c4-4c2e-b7c4-46cef6a8dba5",
  "refresh_token": "fb5587ee-d9cf-4cb5-a586-4aed72cc9bea",
  "scope": "read",
  "token_type": "bearer",
  "expires_in": 30714
}
```

### Step 5. Exchange refresh token for access tokens

If your access token is expired, you can use `refresh_token` to get a new access token, which can be
done by make a POST call:

```
POST https://accounts.binance.com/oauth/token?client_id=YOUR_CLIENT_ID&client_secret=YOUR_CLIENT_SECRET&grant_type=refresh_token&refresh_token=STEP4_REFRESH_TOKEN
```

| Parameter       | Description                                         |
| --------------- | --------------------------------------------------- |
| `grant_type`    | **required** Value `refresh_token`                  |
| `refresh_token` | **required** Step4 refresh token                    |
| `client_id`     | **required** The client ID of your application.     |
| `client_secret` | **required** The client secret of your application. |

Example POST call:

```
curl https://accounts.binance.com/oauth/token \
  -X POST
  -d 'client_id=je-client&client_secret=je-client-secret&grant_type=refresh_token&refresh_token=95OfIm
```

After a successful request, a valid `access_token` will be returned in the response and it will be
invalid if it exceeds the `expires_in` time in the response, which is in seconds.

Here is an example response:

```json
{
  "access_token": "83f2bf51-a2c4-4c2e-b7c4-46cef6a8dba5",
  "refresh_token": "fb5587ee-d9cf-4cb5-a586-4aed72cc9bea",
  "scope": "read",
  "token_type": "bearer",
  "expires_in": 30714
}
```

### Step 6. Calling Binance APIs

After you have a valid `access_token`, you can make your first API call:

```
curl 'https://www.binanceapis.com/oauth-api/v1/user-info' \
--header 'Authorization: Bearer {access_token}'
```

<!-- > ⚠️ Please use the query string or Bearer token to pass the access_token. -->

**Response:**

```json
{
  "code": "000000",
  "message": null,
  "data": {
    "userId": "e10e20b7f20947e7bd206b15ce3dae90",
    "email": "xx@xx.com"
  },
  "success": true
}
```

## 2. PKCE Flow

The PKCE extension prevents an attack where the authorization code is intercepted and exchanged for
an access token by a malicious client, by providing the authorization server with a way to verify
the same client instance that exchanges the authorization code is the same one that initiated the
flow. For more details, refer to https://tools.ietf.org/html/rfc7636

### Step 1. Redirect users to request Binance access and set authorization parameters.

```
GET https://accounts.binance.com/en/oauth/authorize?
    response_type=code&
    client_id=YOUR_CLIENT_ID&
    redirect_uri=YOUR_REDIRECT_URI&
    state=CSRF_TOKEN&
    scope=SCOPES&
    code_challenge=CODE_CHALLENGE&
    code_challenge_method=S256
```

> ⚠️ The carriage returns of the above example are only for readability and should be removed in
> real world, as well as the following examples

When redirecting a user to Binance to authorize access to your application, your first step is to
create the authorization request. You need create and store a new PKCE code_verifier, also will be
used in STEP4

Here is an Example of javascript generate code_verifier

```javascript
// Generate a secure random string using the browser crypto functions
function generateRandomString() {
  var array = new Uint32Array(28);
  window.crypto.getRandomValues(array);
  return Array.from(array, (dec) => ("0" + dec.toString(16)).substr(-2)).join("");
}
```

| Parameters       | Description                                                                                                                          |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| `response_type`  | **Required** Value `code`                                                                                                            |
| `client_id`      | **Required** The client ID of your application.                                                                                      |
| `redirect_uri`   | **required** The URL in your web application where users will be redirected after authorization. This value needs to be URL encoded. |
| `state`          | **Optional** The CSRF token to protect against CSRF (cross-site request forgery) attacks.                                            |
| `scope`          | **required** List of scopes enum your application requests access to, with comma (`,`) seperated.                                    |
| `code_challenge` | **required** Hash and base64-urlencode of code_verifier                                                                              |

Here is an Example of javascript generate code_challenge

```javascript
// Calculate the SHA256 hash of the input text.
function sha256(code_verifier) {
  const encoder = new TextEncoder();
  const data = encoder.encode(code_verifier);
  return window.crypto.subtle.digest("SHA-256", data);
}

// Base64-urlencodes the input string
function base64urlencode(hashed) {
  return btoa(String.fromCharCode.apply(null, new Uint8Array(hashed)))
    .replace(/\+/g, "-")
    .replace(/\//g, "_")
    .replace(/=+$/, "");
}

// Return the base64-urlencoded sha256 hash for the PKCE challenge
async function generateCodeChallenge(code_verifier) {
  hashed = await sha256(code_verifier);
  return base64urlencode(hashed);
}
```

Here is an Example of an authorization URL:

```
GET https://accounts.binance.com/en/oauth/authorize?
    response_type=code&
    client_id=a28f296f2cbe6c64b4d5dec24735d39b1b6fffcf&
    redirect_uri=https%3A%2F%2Fdomain.com%2Foauth%2Fcallback&
    state=377f36a4557ab5935b36&
    scope=user:openId,create:apikey&
    code_challenge=ARU184muFVaDi3LObH5YTZSxqA5ZdYPLspCl7wFwV0U
    code_challenge_method=S256
```

### Step 2. Binance prompts user for consent

In this step, the user decides whether to grant your application the requested access. At this
stage, Binance displays a consent window that shows the name of your application and the Binance API
services that it is requesting permission to access with the user's authorization credentials. The
user can then consent or refuse to grant access to your application.

Your application doesn't need to do anything at this stage as it waits for Binance's OAuth 2.0
server to redirect back.

### Step 3. Binance redirects back to your application

If the user approves your application, Binance's OAuth server will redirect back to your
`redirect_uri` with a temporary authorization `code` parameter.

If you specified a `state` parameter in step 1, the parameter will be included as well. If you
generate a random string or encode the hash of a cookie or another value that captures the client's
`state`, you can validate the response to additionally ensure that the request and response
originated in the same browser, providing protection against attacks such as cross-site request
forgery.

Example of the redirection:

```
GET https://domain.com/oauth/callback?
    code=cf6941ae8918b6a008f1377f36a4557ab5935b36&
    state=377f36a4557ab5935b36
```

> `state` is the same as the one in step 1

### Step 4. Exchange authorization code for refresh and access tokens

After your application receives the authorization `code`, it can exchange the authorization `code`
for an access token, which can be done by make a POST call:

```
POST https://accounts.binance.com/oauth/token?client_id=YOUR_CLIENT_ID&code_verifier=STEP1_CODE_VERIFIER&grant_type=authorization_code&code=STEP3_CODE&redirect_uri=YOUR_REDIRECT_URI
```

| Parameter       | Description                                                                                                                          |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| `grant_type`    | **required** Value `authorization_code`                                                                                              |
| `code`          | **required** Step3 return code                                                                                                       |
| `client_id`     | **required** The client ID of your application.                                                                                      |
| `code_verifier` | **required** The random secret code created and stored in STEP1                                                                      |
| `redirect_uri`  | **required** The URL in your web application where users will be redirected after authorization. This value needs to be URL encoded. |

Example POST call:

```sh
curl https://accounts.binance.com/oauth/token \
  -X POST
  -d 'client_id=je-client&code_verifier=65a4ecce1fe857067bec7a6887529531831ebe38e32da95fe0f322a2&grant_type=authorization_code&code=95OfIm&redirect_uri=https%3A%2F%2Fdomain.com%2Foauth%2Fcallback'
```

After a successful request, a valid `access_token` will be returned in the response and it will be
invalid if it exceeds the `expires_in` time in the response, which is in seconds.

Here is an example response:

```json
{
  "access_token": "83f2bf51-a2c4-4c2e-b7c4-46cef6a8dba5",
  "refresh_token": "fb5587ee-d9cf-4cb5-a586-4aed72cc9bea",
  "scope": "read",
  "token_type": "bearer",
  "expires_in": 30714
}
```

### Step 5. Exchange refresh token for access tokens

If your access token is expired, you can use `refresh_token` to get a new access token, which can be
done by make a POST call:

```
POST https://accounts.binance.com/oauth/token?client_id=YOUR_CLIENT_ID&client_secret=YOUR_CLIENT_SECRET&grant_type=refresh_token&refresh_token=STEP4_REFRESH_TOKEN
```

| Parameter       | Description                                         |
| --------------- | --------------------------------------------------- |
| `grant_type`    | **required** Value `refresh_token`                  |
| `refresh_token` | **required** Step4 refresh token                    |
| `client_id`     | **required** The client ID of your application.     |
| `client_secret` | **required** The client secret of your application. |

Example POST call:

```
curl https://accounts.binance.com/oauth/token \
  -X POST
  -d 'client_id=je-client&client_secret=je-client-secret&grant_type=refresh_token&refresh_token=95OfIm
```

After a successful request, a valid `access_token` will be returned in the response and it will be
invalid if it exceeds the `expires_in` time in the response, which is in seconds.

Here is an example response:

```json
{
  "access_token": "83f2bf51-a2c4-4c2e-b7c4-46cef6a8dba5",
  "refresh_token": "fb5587ee-d9cf-4cb5-a586-4aed72cc9bea",
  "scope": "read",
  "token_type": "bearer",
  "expires_in": 30714
}
```

### Step 6. Calling Binance APIs

After you have a valid `access_token`, you can make your first API call:

```
curl 'https://www.binanceapis.com/oauth-api/v1/user-info' \
--header 'Authorization: Bearer {access_token}'
```

**Response:**

```json
{
  "code": "000000",
  "message": null,
  "data": {
    "userId": "e10e20b7f20947e7bd206b15ce3dae90",
    "email": "xx@xx.com"
  },
  "success": true
}
```

---

# Integrate Binance Login with your web application

# Using OAuth to Access Binance API

Binance APIs utilize the [OAuth 2.0](https://tools.ietf.org/html/rfc6749) protocol for
authentication and authorization. Binance supports common OAuth 2.0 scenarios such as those for web
server, single page (browser based), mobile and native applications. This document will guide you
through how your application communicates with Binance's OAuth 2.0 server to secure a user's consent
for performing an API request on his behalf.

To begin, your application must identify the necessary permissions, or `scopes`. Visit the
[Binance Developer Center](https://developers.binance.com/en/oauth-management), sign up for a
Binance entity account, and from there, navigate to your console to create an OAuth application and
get your own client ID and client secret. For now, Binance Login (Oauth2.0), is exclusively offered
to close ecosystem partners. Please reach to our business team for further information.

Depending on your specific application type, you can select one of the two different authorization
flows listed here:

1. For web applications, please refer to the ‘Authorization Code Flow’ section;
2. For browser-based applications as well as mobile and native applications, please refer to the
   ‘PCKE Flow’ section.

## 1. Authorization Code Flow

### Step 1. Redirect users to request Binance access and set authorization parameters.

```
GET https://accounts.binance.com/en/oauth/authorize?
    response_type=code&
    client_id=YOUR_CLIENT_ID&
    redirect_uri=YOUR_REDIRECT_URI&
    state=CSRF_TOKEN&
    scope=SCOPES
```

> ⚠️ The carriage returns of the above example are only for readability and should be removed in
> real world, as well as the following examples

When redirecting a user to Binance to authorize access to your application, your first step is to
create the authorization request.

| Parameters      | Description                                                                                                                          |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| `response_type` | **Required** Value `code`                                                                                                            |
| `client_id`     | **Required** The client ID of your application.                                                                                      |
| `redirect_uri`  | **required** The URL in your web application where users will be redirected after authorization. This value needs to be URL encoded. |
| `state`         | **Optional** The CSRF token to protect against CSRF (cross-site request forgery) attacks.                                            |
| `scope`         | **required** List of scopes enum your application requests access to, with comma (`,`) seperated.                                    |

Here is an Example of an authorization URL:

```
GET https://accounts.binance.com/en/oauth/authorize?
    response_type=code&
    client_id=a28f296f2cbe6c64b4d5dec24735d39b1b6fffcf&
    redirect_uri=https%3A%2F%2Fdomain.com%2Foauth%2Fcallback&
    state=377f36a4557ab5935b36&
    scope=user:openId,create:apikey
```

### Step 2. Binance prompts user for consent

In this step, the user decides whether to grant your application the requested access. At this
stage, Binance displays a consent window that shows the name of your application and the Binance API
services that it is requesting permission to access with the user's authorization credentials. The
user can then consent or refuse to grant access to your application.

Your application doesn't need to do anything at this stage as it waits for Binance's OAuth 2.0
server to redirect back.

### Step 3. Binance redirects back to your application

If the user approves your application, Binance's OAuth server will redirect back to your
`redirect_uri` with a temporary authorization `code` parameter.

If you specified a `state` parameter in step 1, the parameter will be included as well. If you
generate a random string or encode the hash of a cookie or another value that captures the client's
`state`, you can validate the response to additionally ensure that the request and response
originated in the same browser, providing protection against attacks such as cross-site request
forgery.

Example of the redirection:

```
GET https://domain.com/oauth/callback?
    code=cf6941ae8918b6a008f1377f36a4557ab5935b36&
    state=377f36a4557ab5935b36
```

> `state` is the same as the one in step 1

### Step 4. Exchange authorization code for refresh and access tokens

After your application receives the authorization `code`, it can exchange the authorization `code`
for an access token, which can be done by make a POST call:

```
POST https://accounts.binance.com/oauth/token?client_id=YOUR_CLIENT_ID&client_secret=YOUR_CLIENT_SECRET&grant_type=authorization_code&code=STEP3_CODE&redirect_uri=YOUR_REDIRECT_URI
```

| Parameter       | Description                                                                                                                          |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| `grant_type`    | **required** Value `authorization_code`                                                                                              |
| `code`          | **required** Step3 return code                                                                                                       |
| `client_id`     | **required** The client ID of your application.                                                                                      |
| `client_secret` | **required** The client secret of your application.                                                                                  |
| `redirect_uri`  | **required** The URL in your web application where users will be redirected after authorization. This value needs to be URL encoded. |

Example POST call:

```sh
curl https://accounts.binance.com/oauth/token \
  -X POST
  -d 'client_id=je-client&client_secret=je-client-secret&grant_type=authorization_code&code=95OfIm&redirect_uri=https%3A%2F%2Fdomain.com%2Foauth%2Fcallback'
```

After a successful request, a valid `access_token` will be returned in the response and it will be
invalid if it exceeds the `expires_in` time in the response, which is in seconds.

Here is an example response:

```json
{
  "access_token": "83f2bf51-a2c4-4c2e-b7c4-46cef6a8dba5",
  "refresh_token": "fb5587ee-d9cf-4cb5-a586-4aed72cc9bea",
  "scope": "read",
  "token_type": "bearer",
  "expires_in": 30714
}
```

### Step 5. Exchange refresh token for access tokens

If your access token is expired, you can use `refresh_token` to get a new access token, which can be
done by make a POST call:

```
POST https://accounts.binance.com/oauth/token?client_id=YOUR_CLIENT_ID&client_secret=YOUR_CLIENT_SECRET&grant_type=refresh_token&refresh_token=STEP4_REFRESH_TOKEN
```

| Parameter       | Description                                         |
| --------------- | --------------------------------------------------- |
| `grant_type`    | **required** Value `refresh_token`                  |
| `refresh_token` | **required** Step4 refresh token                    |
| `client_id`     | **required** The client ID of your application.     |
| `client_secret` | **required** The client secret of your application. |

Example POST call:

```
curl https://accounts.binance.com/oauth/token \
  -X POST
  -d 'client_id=je-client&client_secret=je-client-secret&grant_type=refresh_token&refresh_token=95OfIm
```

After a successful request, a valid `access_token` will be returned in the response and it will be
invalid if it exceeds the `expires_in` time in the response, which is in seconds.

Here is an example response:

```json
{
  "access_token": "83f2bf51-a2c4-4c2e-b7c4-46cef6a8dba5",
  "refresh_token": "fb5587ee-d9cf-4cb5-a586-4aed72cc9bea",
  "scope": "read",
  "token_type": "bearer",
  "expires_in": 30714
}
```

### Step 6. Calling Binance APIs

After you have a valid `access_token`, you can make your first API call:

```
curl 'https://www.binanceapis.com/oauth-api/v1/user-info' \
--header 'Authorization: Bearer {access_token}'
```

<!-- > ⚠️ Please use the query string or Bearer token to pass the access_token. -->

**Response:**

```json
{
  "code": "000000",
  "message": null,
  "data": {
    "userId": "e10e20b7f20947e7bd206b15ce3dae90",
    "email": "xx@xx.com"
  },
  "success": true
}
```

## 2. PKCE Flow

The PKCE extension prevents an attack where the authorization code is intercepted and exchanged for
an access token by a malicious client, by providing the authorization server with a way to verify
the same client instance that exchanges the authorization code is the same one that initiated the
flow. For more details, refer to https://tools.ietf.org/html/rfc7636

### Step 1. Redirect users to request Binance access and set authorization parameters.

```
GET https://accounts.binance.com/en/oauth/authorize?
    response_type=code&
    client_id=YOUR_CLIENT_ID&
    redirect_uri=YOUR_REDIRECT_URI&
    state=CSRF_TOKEN&
    scope=SCOPES&
    code_challenge=CODE_CHALLENGE&
    code_challenge_method=S256
```

> ⚠️ The carriage returns of the above example are only for readability and should be removed in
> real world, as well as the following examples

When redirecting a user to Binance to authorize access to your application, your first step is to
create the authorization request. You need create and store a new PKCE code_verifier, also will be
used in STEP4

Here is an Example of javascript generate code_verifier

```javascript
// Generate a secure random string using the browser crypto functions
function generateRandomString() {
  var array = new Uint32Array(28);
  window.crypto.getRandomValues(array);
  return Array.from(array, (dec) => ("0" + dec.toString(16)).substr(-2)).join("");
}
```

| Parameters       | Description                                                                                                                          |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| `response_type`  | **Required** Value `code`                                                                                                            |
| `client_id`      | **Required** The client ID of your application.                                                                                      |
| `redirect_uri`   | **required** The URL in your web application where users will be redirected after authorization. This value needs to be URL encoded. |
| `state`          | **Optional** The CSRF token to protect against CSRF (cross-site request forgery) attacks.                                            |
| `scope`          | **required** List of scopes enum your application requests access to, with comma (`,`) seperated.                                    |
| `code_challenge` | **required** Hash and base64-urlencode of code_verifier                                                                              |

Here is an Example of javascript generate code_challenge

```javascript
// Calculate the SHA256 hash of the input text.
function sha256(code_verifier) {
  const encoder = new TextEncoder();
  const data = encoder.encode(code_verifier);
  return window.crypto.subtle.digest("SHA-256", data);
}

// Base64-urlencodes the input string
function base64urlencode(hashed) {
  return btoa(String.fromCharCode.apply(null, new Uint8Array(hashed)))
    .replace(/\+/g, "-")
    .replace(/\//g, "_")
    .replace(/=+$/, "");
}

// Return the base64-urlencoded sha256 hash for the PKCE challenge
async function generateCodeChallenge(code_verifier) {
  hashed = await sha256(code_verifier);
  return base64urlencode(hashed);
}
```

Here is an Example of an authorization URL:

```
GET https://accounts.binance.com/en/oauth/authorize?
    response_type=code&
    client_id=a28f296f2cbe6c64b4d5dec24735d39b1b6fffcf&
    redirect_uri=https%3A%2F%2Fdomain.com%2Foauth%2Fcallback&
    state=377f36a4557ab5935b36&
    scope=user:openId,create:apikey&
    code_challenge=ARU184muFVaDi3LObH5YTZSxqA5ZdYPLspCl7wFwV0U
    code_challenge_method=S256
```

### Step 2. Binance prompts user for consent

In this step, the user decides whether to grant your application the requested access. At this
stage, Binance displays a consent window that shows the name of your application and the Binance API
services that it is requesting permission to access with the user's authorization credentials. The
user can then consent or refuse to grant access to your application.

Your application doesn't need to do anything at this stage as it waits for Binance's OAuth 2.0
server to redirect back.

### Step 3. Binance redirects back to your application

If the user approves your application, Binance's OAuth server will redirect back to your
`redirect_uri` with a temporary authorization `code` parameter.

If you specified a `state` parameter in step 1, the parameter will be included as well. If you
generate a random string or encode the hash of a cookie or another value that captures the client's
`state`, you can validate the response to additionally ensure that the request and response
originated in the same browser, providing protection against attacks such as cross-site request
forgery.

Example of the redirection:

```
GET https://domain.com/oauth/callback?
    code=cf6941ae8918b6a008f1377f36a4557ab5935b36&
    state=377f36a4557ab5935b36
```

> `state` is the same as the one in step 1

### Step 4. Exchange authorization code for refresh and access tokens

After your application receives the authorization `code`, it can exchange the authorization `code`
for an access token, which can be done by make a POST call:

```
POST https://accounts.binance.com/oauth/token?client_id=YOUR_CLIENT_ID&code_verifier=STEP1_CODE_VERIFIER&grant_type=authorization_code&code=STEP3_CODE&redirect_uri=YOUR_REDIRECT_URI
```

| Parameter       | Description                                                                                                                          |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| `grant_type`    | **required** Value `authorization_code`                                                                                              |
| `code`          | **required** Step3 return code                                                                                                       |
| `client_id`     | **required** The client ID of your application.                                                                                      |
| `code_verifier` | **required** The random secret code created and stored in STEP1                                                                      |
| `redirect_uri`  | **required** The URL in your web application where users will be redirected after authorization. This value needs to be URL encoded. |

Example POST call:

```sh
curl https://accounts.binance.com/oauth/token \
  -X POST
  -d 'client_id=je-client&code_verifier=65a4ecce1fe857067bec7a6887529531831ebe38e32da95fe0f322a2&grant_type=authorization_code&code=95OfIm&redirect_uri=https%3A%2F%2Fdomain.com%2Foauth%2Fcallback'
```

After a successful request, a valid `access_token` will be returned in the response and it will be
invalid if it exceeds the `expires_in` time in the response, which is in seconds.

Here is an example response:

```json
{
  "access_token": "83f2bf51-a2c4-4c2e-b7c4-46cef6a8dba5",
  "refresh_token": "fb5587ee-d9cf-4cb5-a586-4aed72cc9bea",
  "scope": "read",
  "token_type": "bearer",
  "expires_in": 30714
}
```

### Step 5. Exchange refresh token for access tokens

If your access token is expired, you can use `refresh_token` to get a new access token, which can be
done by make a POST call:

```
POST https://accounts.binance.com/oauth/token?client_id=YOUR_CLIENT_ID&client_secret=YOUR_CLIENT_SECRET&grant_type=refresh_token&refresh_token=STEP4_REFRESH_TOKEN
```

| Parameter       | Description                                         |
| --------------- | --------------------------------------------------- |
| `grant_type`    | **required** Value `refresh_token`                  |
| `refresh_token` | **required** Step4 refresh token                    |
| `client_id`     | **required** The client ID of your application.     |
| `client_secret` | **required** The client secret of your application. |

Example POST call:

```
curl https://accounts.binance.com/oauth/token \
  -X POST
  -d 'client_id=je-client&client_secret=je-client-secret&grant_type=refresh_token&refresh_token=95OfIm
```

After a successful request, a valid `access_token` will be returned in the response and it will be
invalid if it exceeds the `expires_in` time in the response, which is in seconds.

Here is an example response:

```json
{
  "access_token": "83f2bf51-a2c4-4c2e-b7c4-46cef6a8dba5",
  "refresh_token": "fb5587ee-d9cf-4cb5-a586-4aed72cc9bea",
  "scope": "read",
  "token_type": "bearer",
  "expires_in": 30714
}
```

### Step 6. Calling Binance APIs

After you have a valid `access_token`, you can make your first API call:

```
curl 'https://www.binanceapis.com/oauth-api/v1/user-info' \
--header 'Authorization: Bearer {access_token}'
```

**Response:**

```json
{
  "code": "000000",
  "message": null,
  "data": {
    "userId": "e10e20b7f20947e7bd206b15ce3dae90",
    "email": "xx@xx.com"
  },
  "success": true
}
```