---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/binance-pay-merchant/api-collection-result-query
api_type: Guide
updated_at: 2026-11-24 18:35:06.898055
---

# Query Collection Result

Query collection result API used for 3rd party application to collection order status

## EndPoint

```http request
POST https://bpay.binanceapi.com/binancepay/openapi/collection/query
```

## Request Parameters

| Attributes    | Type   | Required | Description                                                                                             |
| ------------- | ------ | -------- | ------------------------------------------------------------------------------------------------------- |
| orderId       | String | NO       | collection order id in binance pay system, either trade no or collection order id should be provided    |
| clientTradeNo | String | NO       | maximum length 32, trade no in client system, either trade no or collection order id should be provided |

## Response

| Name         | Type                     | Required | Description                                                                   |
| ------------ | ------------------------ | -------- | ----------------------------------------------------------------------------- |
| status       | String                   | YES      | status of the API request, "SUCCESS" or "FAIL"                                |
| code         | String                   | YES      | request result code, refer to [Result Code](#result-code)                     |
| data         | QueryCollectionOrderResp | YES      | response body, refer to [QueryCollectionOrderResp](#querycollectionorderresp) |
| errorMessage | string                   | YES      |

### QueryCollectionOrderResp:

| Attributes    | Type   | Required | Description                  |
| ------------- | ------ | -------- | ---------------------------- |
| orderId       | String | YES      |
| clientTradeNo | String | YES      | maximum length 32            |
| status        | String | YES      | "INITIAL", "PENDING", "PAID" |

## Result Code

## Result Code

<span id="result-code"></span>

| **Name**                               | **Code** | **Reason**                                                                    | **Solution**                                                                                   |
| -------------------------------------- | -------- | ----------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| UNKNOWN_ERROR                          | 400000   | An unknown error occurred while processing the request.                       | Try again later                                                                                |
| INVALID_REQUEST                        | 400001   | Parameter format is wrong or parameter transferring doesn't follow the rules. | Please check whether the parameters are correct.                                               |
| INVALID_SIGNATURE                      | 400002   | Incorrect signature result                                                    | Check whether the signature parameter and method comply with signature algorithm requirements. |
| INVALID_TIMESTAMP                      | 400003   | Timestamp for this request is outside of the time window.                     | Sync server clock                                                                              |
| INVALID_API_KEY_OR_IP                  | 400004   | API identity key not found or invalid.                                        | Check API identity key                                                                         |
| BAD_API_KEY_FMT                        | 400005   | API identity key format invalid.                                              | Check API identity key.                                                                        |
| BAD_HTTP_METHOD                        | 400006   | Request method not supported.                                                 | Check Request method.                                                                          |
| MEDIA_TYPE_NOT_SUPPORTED               | 400007   | Media type not supported.                                                     | Check Request Media type.                                                                      |
| INVALID_REQUEST_BODY                   | 400008   | Request body is not a valid json object.                                      | Check Request body                                                                             |
| PAYMENT_C2C_COLLECTION_ORDER_NOT_FOUND | 400207   | collection order not found                                                    | Check request property value                                                                   |

---

# Query Collection Result

Query collection result API used for 3rd party application to collection order status

## EndPoint

```http request
POST https://bpay.binanceapi.com/binancepay/openapi/collection/query
```

## Request Parameters

| Attributes    | Type   | Required | Description                                                                                             |
| ------------- | ------ | -------- | ------------------------------------------------------------------------------------------------------- |
| orderId       | String | NO       | collection order id in binance pay system, either trade no or collection order id should be provided    |
| clientTradeNo | String | NO       | maximum length 32, trade no in client system, either trade no or collection order id should be provided |

## Response

| Name         | Type                     | Required | Description                                                                   |
| ------------ | ------------------------ | -------- | ----------------------------------------------------------------------------- |
| status       | String                   | YES      | status of the API request, "SUCCESS" or "FAIL"                                |
| code         | String                   | YES      | request result code, refer to [Result Code](#result-code)                     |
| data         | QueryCollectionOrderResp | YES      | response body, refer to [QueryCollectionOrderResp](#querycollectionorderresp) |
| errorMessage | string                   | YES      |

### QueryCollectionOrderResp:

| Attributes    | Type   | Required | Description                  |
| ------------- | ------ | -------- | ---------------------------- |
| orderId       | String | YES      |
| clientTradeNo | String | YES      | maximum length 32            |
| status        | String | YES      | "INITIAL", "PENDING", "PAID" |

## Result Code

## Result Code

<span id="result-code"></span>

| **Name**                               | **Code** | **Reason**                                                                    | **Solution**                                                                                   |
| -------------------------------------- | -------- | ----------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| UNKNOWN_ERROR                          | 400000   | An unknown error occurred while processing the request.                       | Try again later                                                                                |
| INVALID_REQUEST                        | 400001   | Parameter format is wrong or parameter transferring doesn't follow the rules. | Please check whether the parameters are correct.                                               |
| INVALID_SIGNATURE                      | 400002   | Incorrect signature result                                                    | Check whether the signature parameter and method comply with signature algorithm requirements. |
| INVALID_TIMESTAMP                      | 400003   | Timestamp for this request is outside of the time window.                     | Sync server clock                                                                              |
| INVALID_API_KEY_OR_IP                  | 400004   | API identity key not found or invalid.                                        | Check API identity key                                                                         |
| BAD_API_KEY_FMT                        | 400005   | API identity key format invalid.                                              | Check API identity key.                                                                        |
| BAD_HTTP_METHOD                        | 400006   | Request method not supported.                                                 | Check Request method.                                                                          |
| MEDIA_TYPE_NOT_SUPPORTED               | 400007   | Media type not supported.                                                     | Check Request Media type.                                                                      |
| INVALID_REQUEST_BODY                   | 400008   | Request body is not a valid json object.                                      | Check Request body                                                                             |
| PAYMENT_C2C_COLLECTION_ORDER_NOT_FOUND | 400207   | collection order not found                                                    | Check request property value                                                                   |