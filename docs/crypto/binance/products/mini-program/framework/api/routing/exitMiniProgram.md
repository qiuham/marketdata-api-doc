---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/routing/exitMiniProgram
api_type: Guide
updated_at: 2026-11-24 18:44:32.320406
---

# bn.exitMiniProgram

▸ **exitMiniProgram**(`options?`): `Promise`<{}\>

**`description`** Exit the miniprogram. There must be a click behavior to call successfully

Parameters

| Name       | Type                     | Description               |
| :--------- | :----------------------- | :------------------------ |
| `options?` | `ExitMiniProgramOptions` | Exit mini program options |

Returns

`Promise`<{}\>

---

## Interface: ExitMiniProgramOptions

| Name  | Type      | Description                                                                                                    |
| :---- | :-------- | :------------------------------------------------------------------------------------------------------------- |
| force | `boolean` | **`description`** Is the mini program killed when exit, default is false**`remark`** supported jssdk >= 4.7.0  |
| url   | `string`  | **`description`** The URL to redirect to when the mini program is exited**`remark`** supported jssdk >= 4.47.0 |

---

# bn.exitMiniProgram

▸ **exitMiniProgram**(`options?`): `Promise`<{}\>

**`description`** Exit the miniprogram. There must be a click behavior to call successfully

Parameters

| Name       | Type                     | Description               |
| :--------- | :----------------------- | :------------------------ |
| `options?` | `ExitMiniProgramOptions` | Exit mini program options |

Returns

`Promise`<{}\>

---

## Interface: ExitMiniProgramOptions

| Name  | Type      | Description                                                                                                    |
| :---- | :-------- | :------------------------------------------------------------------------------------------------------------- |
| force | `boolean` | **`description`** Is the mini program killed when exit, default is false**`remark`** supported jssdk >= 4.7.0  |
| url   | `string`  | **`description`** The URL to redirect to when the mini program is exited**`remark`** supported jssdk >= 4.47.0 |