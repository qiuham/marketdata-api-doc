---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/rest-api/get-api-key-info
api_type: REST
updated_at: 2026-05-27 20:02:00.721908
---

# Get API Key Info

**POST** `https://api.kraken.com/0/private/GetApiKeyInfo`

Retrieve information about the API key that is used to make the request, including its name, permissions, restrictions, and usage timestamps.

**API Key Permissions Required:** `None`

## Request

  * application/json

### Body**required**

**nonce** `integer<int64>` *required*

Nonce used in construction of `API-Sign` header

**otp** `string`

Two-factor authentication password (required only if 2FA is configured for the API key)

## Responses

  * 200

API key information retrieved.

  * application/json
* Schema

**Schema**

**result** `object`

API Key Information

**apiKeyName** string

Name/label assigned to the API key

**apiKey** string

The API key string

    ↳ **nonce** `string`

Current nonce value for the API key

**nonceWindow** integer<int64>

Custom nonce window value (0 if not configured)

    ↳ **permissions** `string[]`

List of permissions assigned to the API key. Values correspond to the API Key permission settings:

Value| API Key Permission  
---|---  
`query-funds`| Funds permissions - Query  
`add-funds`| Funds permissions - Deposit  
`withdraw-funds`| Funds permissions - Withdraw  
`earn-funds`| Funds permissions - Earn  
`query-open-trades`| Orders and trades - Query open orders & trades  
`query-closed-trades`| Orders and trades - Query closed orders & trades  
`modify-trades`| Orders and trades - Create & modify orders  
`close-trades`| Orders and trades - Cancel & close orders  
`query-ledger`| Data - Query ledger entries  
`export-data`| Data - Export data  
`create-ws-token`| WebSocket interface - On  
`add-withdraw-address`| Add withdrawal addresses  
`update-withdraw-address`| Update withdrawal addresses  
  
    ↳ **iban** `string`

IIBAN (Internal IBAN) of the account associated with the API key

**validUntil** string

Unix timestamp for key expiration (0 if not set)

**queryFrom** string

Unix timestamp for earliest allowed query date (0 if not set)

**queryTo** string

Unix timestamp for latest allowed query date (0 if not set)

**createdTime** string

Unix timestamp of when the API key was created

**modifiedTime** string

Unix timestamp of when the API key was last modified

**ipAllowlist** string[]

List of IP addresses or ranges allowed to use this API key (empty if not restricted)

**lastUsed** stringnullable

Unix timestamp of when the API key was last used (null if never used)

**error** `string[]`
* curl
  * python
  * go
  * nodejs
* CURL

    
    
    curl -L 'https://api.kraken.com/0/private/GetApiKeyInfo' \  
    -H 'Content-Type: application/json' \  
    -H 'Accept: application/json' \  
    -H 'API-Key: <API-Key>' \  
    -H 'API-Sign: <API-Sign>' \  
    -d '{  
      "nonce": 0,  
      "otp": "string"  
    }'  
    

Request Collapse all

Base URL

https://api.kraken.com/0

Auth

API-Key

API-Sign

Body required
    
    
    {
      "nonce": 0,
      "otp": "string"
    }