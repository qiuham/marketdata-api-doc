---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/interface/showModal
api_type: Guide
updated_at: 2026-11-18 18:45:34.858056
---

# bn.showModal

▸ **showModal**(`options?`): `Promise`<`ModalResult`\>

Displays the modal dialog box.

Parameters

| Name       | Type                           |
| :--------- | :----------------------------- |
| `options?` | `Optional`<`CmdModalOptions`\> |

Returns

`Promise`<`ModalResult`\>

Modal result

## Optional

Ƭ **Optional**<`T`\>: `Object`

Type parameters

| Name |
| :--- |
| `T`  |

## Interface: CmdModalOptions

| Name         | Type      | Description                                                       |
| :----------- | :-------- | :---------------------------------------------------------------- |
| title        | `string`  | Prompt title                                                      |
| content      | `string`  | Prompt content                                                    |
| confirmText? | `string`  | The text of the "OK "button, not more than 4 characters           |
| showCancel?  | `boolean` | Indicates whether to display the "Cancel" button, default is true |
| cancelText?  | `string`  | The text of the "Cancel" button, not more than 4 characters       |

## Interface: ModalResult

| Name     | Type      | Description                                                                                   |
| :------- | :-------- | :-------------------------------------------------------------------------------------------- |
| confirm? | `boolean` | When the value is "true", it indicates that the user tapped the "OK" button.                  |
| cancel?  | `boolean` | When the value is "true", it indicates that the user tapped the "Cancel" button.              |
| status?  | `boolean` | **`deprecated`** When the value is "true", it indicates that the user tapped the "OK" button. |

---

# bn.showModal

▸ **showModal**(`options?`): `Promise`<`ModalResult`\>

Displays the modal dialog box.

Parameters

| Name       | Type                           |
| :--------- | :----------------------------- |
| `options?` | `Optional`<`CmdModalOptions`\> |

Returns

`Promise`<`ModalResult`\>

Modal result

## Optional

Ƭ **Optional**<`T`\>: `Object`

Type parameters

| Name |
| :--- |
| `T`  |

## Interface: CmdModalOptions

| Name         | Type      | Description                                                       |
| :----------- | :-------- | :---------------------------------------------------------------- |
| title        | `string`  | Prompt title                                                      |
| content      | `string`  | Prompt content                                                    |
| confirmText? | `string`  | The text of the "OK "button, not more than 4 characters           |
| showCancel?  | `boolean` | Indicates whether to display the "Cancel" button, default is true |
| cancelText?  | `string`  | The text of the "Cancel" button, not more than 4 characters       |

## Interface: ModalResult

| Name     | Type      | Description                                                                                   |
| :------- | :-------- | :-------------------------------------------------------------------------------------------- |
| confirm? | `boolean` | When the value is "true", it indicates that the user tapped the "OK" button.                  |
| cancel?  | `boolean` | When the value is "true", it indicates that the user tapped the "Cancel" button.              |
| status?  | `boolean` | **`deprecated`** When the value is "true", it indicates that the user tapped the "OK" button. |