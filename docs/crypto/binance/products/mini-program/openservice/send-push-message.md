---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/openservice/send-push-message
api_type: Guide
updated_at: 2026-11-22 18:35:30.849009
---

# SendPushMessage

# <a name="sendPushMessage"></a>SendPushMessage

## <a name="workflow"></a>Workflow

![](/img/mp-management/mp-open-service-007.png)

1. The mini app invokes the JavaScript API function,
   `bn.requestSubscribeMessage({tmplIds: $template_ids})`, through the mini program framework. This
   action prompts an authorization pop-up for user approval, returning $template_ids and
   corresponding $push_tokens upon user consent.
2. The mini app transmits the $template_ids and $push_tokens to the merchant’s backend.
3. Backed by the $push_tokens and additional parameters, the backend system calls the
   'sendPushMessage' operation and forwards the message to the user.

Refer to the documentation for all required APIs.

Requirements:

Binance APP version >= 2.52.0

SDK version >= 3.13.0

## <a name="preparation"></a>Preparation

Please refer to [Preparation Of Open Service](/products/mini-program/openservice/preparation)

## <a name="mini-program"></a>Mini Program

Within the mini program, developers can invoke the `$ bn.requestSubscribeMessage()` JavaScript API
to trigger an authorization pop-up for users. Once user consent is obtained, the API returns
$template_ids and corresponding $push_tokens which can be utilized for message pushing on the
backend.

```javascript
const tmplIds = []
const info = await mpService.requestSubscribeMessage({
     tmplIds
})
tmplIds.forEach((id) => {
   if (!info[id] || info[id].type !== 'accept' || !info[id].token) {
      // not accept
      console.log(info[id].type)
      return;
   }
   api.sendToBackend(info[id]，info[id].token)
})
```

## <a name="backend"></a>Backend

### <a name="host"></a>SendPushMessage

**Host**: **dip-cb.binanceapi.com**

**POST** /mp-api/v1/apps/\{appId\}/message/send

**Parameters**

| **Parameter** | **Description**                                                                                     |
| :------------ | :-------------------------------------------------------------------------------------------------- |
| appId         | **required** The AppId of the mini program.                                                         |
| pushToken     | **required** The push_token obtained from previous steps.                                           |
| templateId    | **required** The templateId of the template.                                                        |
| language      | **required** The language of the message.                                                           |
| path          | **optional** Pages path when user clicks the message. By default, it is the path to the entry page. |
| parameters    | **required** Arrays of parameters to the template. Format is `[{"name":string, "value":string}]`.   |

Note:

1. The pushToken is valid only for seven days.
2. Each pushToken can only be used once.
3. You need to carry a JWT token in the `X-Mp-Open-Api-Token` header when you call this API. For
   generating the JWT token, please refer to
   [Description of External Interface Signature Authentication Algorithm](/products/mini-program/openservice/signature).

**Request**

```json
​​{
  "appId": "your-app-id-can-get-from-workspace",
  "pushToken": "push_token_****",
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
   ]
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

| ErrorCode | Remark                       |
| :-------- | :--------------------------- |
| 000000    | Success                      |
| 900001    | Invalid Parameter            |
| 900002    | JWT Authentication Failed    |
| 900003    | Unexpected Error             |
| 900230    | Invalid or Expired pushToken |
| 900231    | Rate Limit                   |

statusCode

| statusCode | Remark                                                                                  |
| :--------- | :-------------------------------------------------------------------------------------- |
| 000000     | Success                                                                                 |
| 900240     | The user has refused to receive all messages from the mini-program                      |
| 900241     | The user has declined to receive the message corresponding to the mini-program template |

---

# SendPushMessage

# <a name="sendPushMessage"></a>SendPushMessage

## <a name="workflow"></a>Workflow

![](/img/mp-management/mp-open-service-007.png)

1. The mini app invokes the JavaScript API function,
   `bn.requestSubscribeMessage({tmplIds: $template_ids})`, through the mini program framework. This
   action prompts an authorization pop-up for user approval, returning $template_ids and
   corresponding $push_tokens upon user consent.
2. The mini app transmits the $template_ids and $push_tokens to the merchant’s backend.
3. Backed by the $push_tokens and additional parameters, the backend system calls the
   'sendPushMessage' operation and forwards the message to the user.

Refer to the documentation for all required APIs.

Requirements:

Binance APP version >= 2.52.0

SDK version >= 3.13.0

## <a name="preparation"></a>Preparation

Please refer to [Preparation Of Open Service](/products/mini-program/openservice/preparation)

## <a name="mini-program"></a>Mini Program

Within the mini program, developers can invoke the `$ bn.requestSubscribeMessage()` JavaScript API
to trigger an authorization pop-up for users. Once user consent is obtained, the API returns
$template_ids and corresponding $push_tokens which can be utilized for message pushing on the
backend.

```javascript
const tmplIds = []
const info = await mpService.requestSubscribeMessage({
     tmplIds
})
tmplIds.forEach((id) => {
   if (!info[id] || info[id].type !== 'accept' || !info[id].token) {
      // not accept
      console.log(info[id].type)
      return;
   }
   api.sendToBackend(info[id]，info[id].token)
})
```

## <a name="backend"></a>Backend

### <a name="host"></a>SendPushMessage

**Host**: **dip-cb.binanceapi.com**

**POST** /mp-api/v1/apps/\{appId\}/message/send

**Parameters**

| **Parameter** | **Description**                                                                                     |
| :------------ | :-------------------------------------------------------------------------------------------------- |
| appId         | **required** The AppId of the mini program.                                                         |
| pushToken     | **required** The push_token obtained from previous steps.                                           |
| templateId    | **required** The templateId of the template.                                                        |
| language      | **required** The language of the message.                                                           |
| path          | **optional** Pages path when user clicks the message. By default, it is the path to the entry page. |
| parameters    | **required** Arrays of parameters to the template. Format is `[{"name":string, "value":string}]`.   |

Note:

1. The pushToken is valid only for seven days.
2. Each pushToken can only be used once.
3. You need to carry a JWT token in the `X-Mp-Open-Api-Token` header when you call this API. For
   generating the JWT token, please refer to
   [Description of External Interface Signature Authentication Algorithm](/products/mini-program/openservice/signature).

**Request**

```json
​​{
  "appId": "your-app-id-can-get-from-workspace",
  "pushToken": "push_token_****",
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
   ]
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

| ErrorCode | Remark                       |
| :-------- | :--------------------------- |
| 000000    | Success                      |
| 900001    | Invalid Parameter            |
| 900002    | JWT Authentication Failed    |
| 900003    | Unexpected Error             |
| 900230    | Invalid or Expired pushToken |
| 900231    | Rate Limit                   |

statusCode

| statusCode | Remark                                                                                  |
| :--------- | :-------------------------------------------------------------------------------------- |
| 000000     | Success                                                                                 |
| 900240     | The user has refused to receive all messages from the mini-program                      |
| 900241     | The user has declined to receive the message corresponding to the mini-program template |