---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/binance-pay-merchant/oauth-api-c2c-currency-query
api_type: Guide
updated_at: 2026-11-25 18:33:41.128191
---

# OAuth API : Query Supported Currency

Query c2c supported currencies.

> - The host of OAuth API is https://accounts.binance.com
> - The request parameter of OAuth API is transferred as query string of requested url.
> - No need to add signature and API identity key to request header of OAuth API.

```
GET https://accounts.binance.com/oauth-api/v1/pay/c2c/querySupportCurrency
```

## Parameters(Query String of Requested URL):

| Name         | Type   | Mandatory | Description |
| ------------ | ------ | --------- | ----------- |
| access_token | String | YES       |

## Response:

| Name    | Type                            | Mandatory | Description                                                                                                               |
| ------- | ------------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------- |
| code    | String                          | YES       | when success=false, the value is the result code                                                                          |
| message | String                          | NO        | when success=false, the value is error description                                                                        |
| data    | List<QuerySupportCurrencyResp\> | NO        | when success=true, the value is the query currency result, refer to [QuerySupportCurrencyResp](#querysupportcurrencyresp) |
| success | boolean                         | YES       |

### QuerySupportCurrencyResp:

| Attributes | Type   | Mandatory | Description                                                          |
| ---------- | ------ | --------- | -------------------------------------------------------------------- |
| assetCode  | String | YES       |
| assetName  | String | YES       |
| logoUrl    | String | YES       | Icon of the asset, please contact us in order to display it properly |

```json
{
  "code": "000000",
  "message": null,
  "data": [
    {
      "assetCode": "BTC",
      "assetName": "Bitcoin",
      "logoUrl": "https://bin.bnbstatic.com/image/admin_mgs_image_upload/20201110/87496d50-2408-43e1-ad4c-78b47b448a6a.png"
    },
    {
      "assetCode": "BNB",
      "assetName": "BNB",
      "logoUrl": "https://bin.bnbstatic.com/image/admin_mgs_image_upload/20201110/550eda20-1b9a-4bc7-9a65-e4a329e8bb57.png"
    }
  ],
  "success": true
}
```

---

# OAuth API : Query Supported Currency

Query c2c supported currencies.

> - The host of OAuth API is https://accounts.binance.com
> - The request parameter of OAuth API is transferred as query string of requested url.
> - No need to add signature and API identity key to request header of OAuth API.

```
GET https://accounts.binance.com/oauth-api/v1/pay/c2c/querySupportCurrency
```

## Parameters(Query String of Requested URL):

| Name         | Type   | Mandatory | Description |
| ------------ | ------ | --------- | ----------- |
| access_token | String | YES       |

## Response:

| Name    | Type                            | Mandatory | Description                                                                                                               |
| ------- | ------------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------- |
| code    | String                          | YES       | when success=false, the value is the result code                                                                          |
| message | String                          | NO        | when success=false, the value is error description                                                                        |
| data    | List<QuerySupportCurrencyResp\> | NO        | when success=true, the value is the query currency result, refer to [QuerySupportCurrencyResp](#querysupportcurrencyresp) |
| success | boolean                         | YES       |

### QuerySupportCurrencyResp:

| Attributes | Type   | Mandatory | Description                                                          |
| ---------- | ------ | --------- | -------------------------------------------------------------------- |
| assetCode  | String | YES       |
| assetName  | String | YES       |
| logoUrl    | String | YES       | Icon of the asset, please contact us in order to display it properly |

```json
{
  "code": "000000",
  "message": null,
  "data": [
    {
      "assetCode": "BTC",
      "assetName": "Bitcoin",
      "logoUrl": "https://bin.bnbstatic.com/image/admin_mgs_image_upload/20201110/87496d50-2408-43e1-ad4c-78b47b448a6a.png"
    },
    {
      "assetCode": "BNB",
      "assetName": "BNB",
      "logoUrl": "https://bin.bnbstatic.com/image/admin_mgs_image_upload/20201110/550eda20-1b9a-4bc7-9a65-e4a329e8bb57.png"
    }
  ],
  "success": true
}
```