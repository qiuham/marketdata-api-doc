---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/binance-pay-merchant/oauth-api-collection-create
api_type: Guide
updated_at: 2026-11-21 18:33:00.315606
---

# OAuth API : Create Collection

Query c2c supported currencies.

> - The host of OAuth API is https://accounts.binance.com
> - The request parameter of OAuth API is transferred as query string of requested url.
> - No need to add signature and API identity key to request header of OAuth API.

```
POST https://accounts.binance.com/oauth-api/v1/pay/c2c/collection/create
```

## Parameters(Query String of Requested URL):

| Name             | Type       | Mandatory | Description                                         |
| ---------------- | ---------- | --------- | --------------------------------------------------- |
| access_token     | String     | YES       |
| amount           | BigDecimal | YES       | collection order amount                             |
| currency         | String     | YES       | collection order currency                           |
| description      | String(50) | NO        | collection order note                               |
| clientTradeNo    | String(32) | YES       | trade no in client system, used as idempotent check |
| clientUserId     | String(32) | NO        | user id in client system                            |
| clientUserMobile | String(32) | NO        | user mobile in client system                        |
| notificationUrl  | String     | NO        | url for collection order status notification        |

## Response:

| Name    | Type                      | Mandatory | Description                                                                                                                    |
| ------- | ------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------ |
| code    | String                    | YES       | when success=false, the value is the result code                                                                               |
| message | String                    | NO        | when success=false, the value is error description                                                                             |
| data    | CreateCollectionOrderResp | NO        | when success=true, the value is the create collection result, refer to [CreateCollectionOrderResp](#createcollectionorderresp) |
| success | boolean                   | YES       |

### CreateCollectionOrderResp:

| Name          | Type   | Mandatory | Description                                                       |
| ------------- | ------ | --------- | ----------------------------------------------------------------- |
| orderId       | String | YES       |
| clientTradeNo | String | YES       |
| type          | String | YES       | collection order type, it always equals to pain text 'COLLECTION' |

```json
{
  "code": "000000",
  "message": null,
  "data": {
    "orderId": "12345",
    "clientTradeNo": "re3432",
    "type": "COLLECTION"
  },
  "success": true
}
```

### Result Code

| Name                                  | Code   | Reason                                       |
| ------------------------------------- | ------ | -------------------------------------------- |
| PAYMENT_INVALID_CURRENCY              | 403031 | Requested currency is not supported          |
| PAYMENT_ILLEGAL_AMOUNT                | 403040 | The amount is illegal, too small             |
| PAYMENT_C2C_TRADE_NO_DUPLICATED       | 403211 | clientTradeNo is duplicated                  |
| PAYMENT_RECEIVER_EXCEED_RECEIVE_LIMIT | 403706 | Recipient has exceeded fund receiving limit. |

---

# OAuth API : Create Collection

Query c2c supported currencies.

> - The host of OAuth API is https://accounts.binance.com
> - The request parameter of OAuth API is transferred as query string of requested url.
> - No need to add signature and API identity key to request header of OAuth API.

```
POST https://accounts.binance.com/oauth-api/v1/pay/c2c/collection/create
```

## Parameters(Query String of Requested URL):

| Name             | Type       | Mandatory | Description                                         |
| ---------------- | ---------- | --------- | --------------------------------------------------- |
| access_token     | String     | YES       |
| amount           | BigDecimal | YES       | collection order amount                             |
| currency         | String     | YES       | collection order currency                           |
| description      | String(50) | NO        | collection order note                               |
| clientTradeNo    | String(32) | YES       | trade no in client system, used as idempotent check |
| clientUserId     | String(32) | NO        | user id in client system                            |
| clientUserMobile | String(32) | NO        | user mobile in client system                        |
| notificationUrl  | String     | NO        | url for collection order status notification        |

## Response:

| Name    | Type                      | Mandatory | Description                                                                                                                    |
| ------- | ------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------ |
| code    | String                    | YES       | when success=false, the value is the result code                                                                               |
| message | String                    | NO        | when success=false, the value is error description                                                                             |
| data    | CreateCollectionOrderResp | NO        | when success=true, the value is the create collection result, refer to [CreateCollectionOrderResp](#createcollectionorderresp) |
| success | boolean                   | YES       |

### CreateCollectionOrderResp:

| Name          | Type   | Mandatory | Description                                                       |
| ------------- | ------ | --------- | ----------------------------------------------------------------- |
| orderId       | String | YES       |
| clientTradeNo | String | YES       |
| type          | String | YES       | collection order type, it always equals to pain text 'COLLECTION' |

```json
{
  "code": "000000",
  "message": null,
  "data": {
    "orderId": "12345",
    "clientTradeNo": "re3432",
    "type": "COLLECTION"
  },
  "success": true
}
```

### Result Code

| Name                                  | Code   | Reason                                       |
| ------------------------------------- | ------ | -------------------------------------------- |
| PAYMENT_INVALID_CURRENCY              | 403031 | Requested currency is not supported          |
| PAYMENT_ILLEGAL_AMOUNT                | 403040 | The amount is illegal, too small             |
| PAYMENT_C2C_TRADE_NO_DUPLICATED       | 403211 | clientTradeNo is duplicated                  |
| PAYMENT_RECEIVER_EXCEED_RECEIVE_LIMIT | 403706 | Recipient has exceeded fund receiving limit. |