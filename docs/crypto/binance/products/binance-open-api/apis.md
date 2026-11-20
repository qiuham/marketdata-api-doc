---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/binance-open-api/apis
api_type: Guide
updated_at: 2026-11-20 18:34:39.974979
---

# OAuth 2.0 APIs for Binance APIs

## API 1. Get user info

```
curl 'https://www.binanceapis.com/oauth-api/v1/user-info' \
--header 'Authorization: Bearer {access_token}'
```

**Parameters:**

| Name         | Type   | Mandatory | Description |
| ------------ | ------ | --------- | ----------- |
| access_token | String | YES       |

**Response:**

```json
{
  "code": "000000",
  "message": null,
  "data": {
    "userId": "e10e20b7f20947e7bd206b15ce3dae90"
  },
  "success": true
}
```

## API 2. Revoke access_token

```
curl --request POST 'https://www.binanceapis.com/oauth-api/v1/revoke-token' \
--header 'Authorization: Bearer {access_token}'
```

**Parameters:**

| Name         | Type   | Mandatory | Description |
| ------------ | ------ | --------- | ----------- |
| access_token | String | YES       |

**Response:**

```json
{
  "code": "000000",
  "message": null,
  "data": true, // true means clear access_token success
  "success": true
}
```

---

# OAuth 2.0 APIs for Binance APIs

## API 1. Get user info

```
curl 'https://www.binanceapis.com/oauth-api/v1/user-info' \
--header 'Authorization: Bearer {access_token}'
```

**Parameters:**

| Name         | Type   | Mandatory | Description |
| ------------ | ------ | --------- | ----------- |
| access_token | String | YES       |

**Response:**

```json
{
  "code": "000000",
  "message": null,
  "data": {
    "userId": "e10e20b7f20947e7bd206b15ce3dae90"
  },
  "success": true
}
```

## API 2. Revoke access_token

```
curl --request POST 'https://www.binanceapis.com/oauth-api/v1/revoke-token' \
--header 'Authorization: Bearer {access_token}'
```

**Parameters:**

| Name         | Type   | Mandatory | Description |
| ------------ | ------ | --------- | ----------- |
| access_token | String | YES       |

**Response:**

```json
{
  "code": "000000",
  "message": null,
  "data": true, // true means clear access_token success
  "success": true
}
```