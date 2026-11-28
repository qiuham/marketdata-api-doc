---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/openservice/open-service
api_type: Guide
updated_at: 2026-11-28 18:36:16.409583
---

# Open Service

# <a name="Overview"></a>Overview

The Mini Program Open Service facilitates access to users' openid or enables message pushing to
users. This document provides a detailed workflow for integrating with the Mini Program Open
Service.

# <a name="Terminology"></a>Terminology

- MiniApp: The mini application developed by the merchant.
- MPFramework: The mini program framework that extends the JS API to the mini application.
- User: The end users of Binance.
- Backend: The merchant's backend.
- OpenService: The mini program platform's Open Service, which avails APIs for accessing user
  information or pushing messages to users.

# <a name="OpenAPI"></a>OpenAPI

These are the currently supported OpenAPIs:

- [GetUserOpenId](/products/mini-program/openservice/get-open-data) - Access user's openid.

- [SendPushMessage](/products/mini-program/openservice/send-push-message) - Send template messages
  to users.

- [BroadcastMessage](/products/mini-program/openservice/broadcast-message) - Broadcast template
  messages to users.

- [UploadFile](/products/mini-program/openservice/upload-file) - Upload files to the mini program
  service to obtain a fileID for future use.

- [GetFileStatus](/products/mini-program/openservice/get-file-status) - Check the successful upload
  of a file.

- [CreateSKUInAudit](/products/mini-program/openservice/create-sku-in-audit) - Create a new sku for
  a mini program. Any newly created sku will need to be audited.

- [GetSKU](/products/mini-program/openservice/get-sku) - Retrieve a specific SKU and its current
  audit and online state.

- [ListSKUs](/products/mini-program/openservice/list-skus) - List all SKUs for a mini program, with
  optional filtering by audit status.

- [UpdateSKU](/products/mini-program/openservice/update-sku) - Update sku information for a mini
  program. Except for selling price and discount percentage, updates will need to be audited.

- [ActivateSKU](/products/mini-program/openservice/activate-sku) - Activate or deactivate a specific
  sku.

- [GetUserPayId](/products/mini-program/openservice/get-user-pay-id) - Acquire Binance PayID for a
  given OpenID.

Appendix:

- [Description of External Interface Signature Authentication Algorithm](/products/mini-program/openservice/signature)

- [Language Code](/products/mini-program/openservice/appendix)

- [SKU Category List](/products/mini-program/openservice/appendix)

---

# Open Service

# <a name="Overview"></a>Overview

The Mini Program Open Service facilitates access to users' openid or enables message pushing to
users. This document provides a detailed workflow for integrating with the Mini Program Open
Service.

# <a name="Terminology"></a>Terminology

- MiniApp: The mini application developed by the merchant.
- MPFramework: The mini program framework that extends the JS API to the mini application.
- User: The end users of Binance.
- Backend: The merchant's backend.
- OpenService: The mini program platform's Open Service, which avails APIs for accessing user
  information or pushing messages to users.

# <a name="OpenAPI"></a>OpenAPI

These are the currently supported OpenAPIs:

- [GetUserOpenId](/products/mini-program/openservice/get-open-data) - Access user's openid.

- [SendPushMessage](/products/mini-program/openservice/send-push-message) - Send template messages
  to users.

- [BroadcastMessage](/products/mini-program/openservice/broadcast-message) - Broadcast template
  messages to users.

- [UploadFile](/products/mini-program/openservice/upload-file) - Upload files to the mini program
  service to obtain a fileID for future use.

- [GetFileStatus](/products/mini-program/openservice/get-file-status) - Check the successful upload
  of a file.

- [CreateSKUInAudit](/products/mini-program/openservice/create-sku-in-audit) - Create a new sku for
  a mini program. Any newly created sku will need to be audited.

- [GetSKU](/products/mini-program/openservice/get-sku) - Retrieve a specific SKU and its current
  audit and online state.

- [ListSKUs](/products/mini-program/openservice/list-skus) - List all SKUs for a mini program, with
  optional filtering by audit status.

- [UpdateSKU](/products/mini-program/openservice/update-sku) - Update sku information for a mini
  program. Except for selling price and discount percentage, updates will need to be audited.

- [ActivateSKU](/products/mini-program/openservice/activate-sku) - Activate or deactivate a specific
  sku.

- [GetUserPayId](/products/mini-program/openservice/get-user-pay-id) - Acquire Binance PayID for a
  given OpenID.

Appendix:

- [Description of External Interface Signature Authentication Algorithm](/products/mini-program/openservice/signature)

- [Language Code](/products/mini-program/openservice/appendix)

- [SKU Category List](/products/mini-program/openservice/appendix)