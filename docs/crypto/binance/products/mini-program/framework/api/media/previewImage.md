---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/media/previewImage
api_type: Guide
updated_at: 2026-11-28 18:43:49.648275
---

# bn.previewImage

▸ **previewImage**(`options`): `Promise`<`void`\>

Preview the picture in full screen on the new page. Preview the process of the user can save
pictures, send to friends and other operations.

Parameters

| Name      | Type                  |
| :-------- | :-------------------- |
| `options` | `PreviewImageOptions` |

Returns

`Promise`<`void`\>

## Interface: PreviewImageOptions

| Name            | Type                          | Description                                             |
| :-------------- | :---------------------------- | :------------------------------------------------------ |
| urls            | `string`[]                    | A list of links to images that need to be previewed     |
| current?        | `string`                      | Displays long press menu                                |
| showmenu?       | `boolean`                     | Link to currently displayed picture                     |
| referrerPolicy? | `"origin"` \| `"no-referrer"` | origin: Send the full referrer no-referrer: Do not send |

---

# bn.previewImage

▸ **previewImage**(`options`): `Promise`<`void`\>

Preview the picture in full screen on the new page. Preview the process of the user can save
pictures, send to friends and other operations.

Parameters

| Name      | Type                  |
| :-------- | :-------------------- |
| `options` | `PreviewImageOptions` |

Returns

`Promise`<`void`\>

## Interface: PreviewImageOptions

| Name            | Type                          | Description                                             |
| :-------------- | :---------------------------- | :------------------------------------------------------ |
| urls            | `string`[]                    | A list of links to images that need to be previewed     |
| current?        | `string`                      | Displays long press menu                                |
| showmenu?       | `boolean`                     | Link to currently displayed picture                     |
| referrerPolicy? | `"origin"` \| `"no-referrer"` | origin: Send the full referrer no-referrer: Do not send |