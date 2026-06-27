---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/futures-api/auth/check-v-3-api-key
api_type: REST
updated_at: 2026-05-27 19:44:46.668800
---

# Check v3 API key

**GET** `https://futures.kraken.com/api/auth/v1/api-keys/v3/check`

Verify API key access and return the authenticated key's details.

## Responses

  * 200
  * 401

API key authentication is valid and details have been returned.

  * application/json
* Schema

**Schema**

**apiKey** string<base64>required

API key that signed the request.

**Example:**`Gom9BsP75m41c9fuY6oJk/unMWaDZjYIcTP4/5kqPvtzdbj5JU5/Fyeb`

**accountUid** string<uuid>required

UID of the account that the API key belongs to.

**iiban** `object` *required*

IIBAN of the account that the API key belongs to.

oneOf
* Iiban
* MOD2

****string

Account IIBAN, if Kraken customer.

**Possible values:** Value must match regular expression `^AA[A-Z0-9]{2} [A-Z0-9]{4} [A-Z0-9]{4} [A-Z0-9]{4}$`

**Example:**`AA08 N84G CPAR UN7A`

**createdAt** string<date-time>required

Date-time that the API key was created.

**Example:**`2019-08-24T14:15:22Z`

    ↳ **permissions** `object` *required*

Permissions of the API key.

        ↳ **general** `ApiKeyV3AccessLevel (string)` *required*

Tier of access granted to an API key.

**Possible values:** [`NO_ACCESS`, `READ_ONLY`, `FULL_ACCESS`]

        ↳ **transfer** `ApiKeyV3AccessLevel (string)` *required*

Tier of access granted to an API key.

**Possible values:** [`NO_ACCESS`, `READ_ONLY`, `FULL_ACCESS`]

**allowedCidrBlock** objectrequired

oneOf
* ApiKeyAllowedCidrBlock
* MOD2

****string

Range of IP addresses that may use the API key.

**Example:**`192.168.0.0/16`

**allowedCidrBlocks** string<cidr>[]required

Ranges of IP addresses that may use the API key.

API key is not found or request signature is invalid.

  * application/json
* Schema

**Schema**

**error** `string` *required*

**message** `string` *required*

**suberror** `string | nullnullable` *required*

#### Authorization: apikey
    
    
    **name:** [apikey](/api/docs/futures-api/auth/ancile-authentication-service-public-api#authentication)**type:** apiKey**description:** API Key with any permissions.**in:** header**x-inlineDescription:** true
    
    
    **name:** [authent](/api/docs/futures-api/auth/ancile-authentication-service-public-api#authentication)**type:** apiKey**description:** Request signature.**in:** header**x-inlineDescription:** true

  * curl
  * python
  * go
  * nodejs
  * php
* CURL

    
    
    curl -L 'https://futures.kraken.com/api/auth/v1/api-keys/v3/check' \  
    -H 'Accept: application/json' \  
    -H 'apikey: <apikey>' \  
    -H 'authent: <authent>'  
    

Request Collapse all

Base URL

https://futures.kraken.com/api/auth/v1

Auth

api-key-any

request-signature