---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/openservice/broadcast-message
api_type: Guide
updated_at: 2026-11-23 18:37:51.005442
---

# BroadcastMessage

# <a name="BroadcastMessage"></a>BroadcastMessage

## <a name="workflow"></a>Workflow

![](/img/mp-management/mp-open-service-012.png)

1. Backed by the $template_id and additional parameters, the backend system calls the
   'BroadcastMessage' operation.
2. BD review the broadcast message request
3. Once the BD approve the broadcast message request, open service will forward the message to the
   users.

Refer to the documentation for all required APIs.

Requirements:

Binance APP version >= 2.82.0

SDK version >= 4.0.0

## <a name="preparation"></a>Preparation

Please refer to [Preparation Of Open Service](/products/mini-program/openservice/preparation)

## <a name="backend"></a>Backend

### <a name="host"></a>BroadcastMessage

**Host**: **dip-cb.binanceapi.com**

**POST** /mp-api/v1/apps/\{appId\}/message/broadcast

**Parameters**

| **Parameter**  | **Description**                                                                                                                                          |
| :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------- |
| appId          | **required** The AppId of the mini program.                                                                                                              |
| templateId     | **required** The templateId of the template.                                                                                                             |
| language       | **required** The language of the message.                                                                                                                |
| path           | **optional** Pages path when user clicks the message. By default, it is the path to the entry page.                                                      |
| parameters     | **required** Arrays of parameters to the template. Format is `[{"name":string, "value":string}]`.                                                        |
| preview        | **option** bool, The default is false. If it is true, it will only be sent to the users specified in experienceUids.                                     |
| experienceUids | **option** bool Array\<String\> The default is an empty array, used to set the user collection for previewing broadcast messages. Supports up to 5 uids. |

Note:

1. You need to carry a JWT token in the `X-Mp-Open-Api-Token` header when you call this API. For
   generating the JWT token, please refer to
   [Description of External Interface Signature Authentication Algorithm](/products/mini-program/openservice/signature).
   2 We support previewing broadcast messages. You only need to set the preview field to true, and
   specify the experience user uid set (up to 5) in experienceUids to preview the format of the
   message.

**Request**

```json
​​{
  "appId": "your-app-id-can-get-from-workspace",
  "templateId": "1344****",
  "language": "en",
  "path": "pages/details/index?source=***",
  "parameters": [
       {
           "name": "result",
           "value": "success"
       },
       {
           "name": "withdrawMoney",
           "value": "100"
       }
   ],
   "preview":true,
   "experienceUids":["123"]
}
```

**Response**

**HTTP 200**

```json
{
  "code": "000000",
  "message": null,
  "data": {
    "statusCode": "000000"
  },
  "success": true
}
```

Code

| ErrorCode | Remark                    |
| :-------- | :------------------------ |
| 000000    | Success                   |
| 900001    | Invalid Parameter         |
| 900002    | JWT Authentication Failed |
| 900003    | Unexpected Error          |
| 900231    | Rate Limit                |

statusCode

| statusCode | Remark                                                                                  |
| :--------- | :-------------------------------------------------------------------------------------- |
| 000000     | Success                                                                                 |
| 900240     | The user has refused to receive all messages from the mini-program                      |
| 900241     | The user has declined to receive the message corresponding to the mini-program template |

---

# BroadcastMessage

# <a name="BroadcastMessage"></a>BroadcastMessage

## <a name="workflow"></a>Workflow

![](/img/mp-management/mp-open-service-012.png)

1. Backed by the $template_id and additional parameters, the backend system calls the
   'BroadcastMessage' operation.
2. BD review the broadcast message request
3. Once the BD approve the broadcast message request, open service will forward the message to the
   users.

Refer to the documentation for all required APIs.

Requirements:

Binance APP version >= 2.82.0

SDK version >= 4.0.0

## <a name="preparation"></a>Preparation

Please refer to [Preparation Of Open Service](/products/mini-program/openservice/preparation)

## <a name="backend"></a>Backend

### <a name="host"></a>BroadcastMessage

**Host**: **dip-cb.binanceapi.com**

**POST** /mp-api/v1/apps/\{appId\}/message/broadcast

**Parameters**

| **Parameter**  | **Description**                                                                                                                                          |
| :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------- |
| appId          | **required** The AppId of the mini program.                                                                                                              |
| templateId     | **required** The templateId of the template.                                                                                                             |
| language       | **required** The language of the message.                                                                                                                |
| path           | **optional** Pages path when user clicks the message. By default, it is the path to the entry page.                                                      |
| parameters     | **required** Arrays of parameters to the template. Format is `[{"name":string, "value":string}]`.                                                        |
| preview        | **option** bool, The default is false. If it is true, it will only be sent to the users specified in experienceUids.                                     |
| experienceUids | **option** bool Array\<String\> The default is an empty array, used to set the user collection for previewing broadcast messages. Supports up to 5 uids. |

Note:

1. You need to carry a JWT token in the `X-Mp-Open-Api-Token` header when you call this API. For
   generating the JWT token, please refer to
   [Description of External Interface Signature Authentication Algorithm](/products/mini-program/openservice/signature).
   2 We support previewing broadcast messages. You only need to set the preview field to true, and
   specify the experience user uid set (up to 5) in experienceUids to preview the format of the
   message.

**Request**

```json
​​{
  "appId": "your-app-id-can-get-from-workspace",
  "templateId": "1344****",
  "language": "en",
  "path": "pages/details/index?source=***",
  "parameters": [
       {
           "name": "result",
           "value": "success"
       },
       {
           "name": "withdrawMoney",
           "value": "100"
       }
   ],
   "preview":true,
   "experienceUids":["123"]
}
```

**Response**

**HTTP 200**

```json
{
  "code": "000000",
  "message": null,
  "data": {
    "statusCode": "000000"
  },
  "success": true
}
```

Code

| ErrorCode | Remark                    |
| :-------- | :------------------------ |
| 000000    | Success                   |
| 900001    | Invalid Parameter         |
| 900002    | JWT Authentication Failed |
| 900003    | Unexpected Error          |
| 900231    | Rate Limit                |

statusCode

| statusCode | Remark                                                                                  |
| :--------- | :-------------------------------------------------------------------------------------- |
| 000000     | Success                                                                                 |
| 900240     | The user has refused to receive all messages from the mini-program                      |
| 900241     | The user has declined to receive the message corresponding to the mini-program template |