---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/media/setInnerAudioOption
api_type: Guide
updated_at: 2026-11-24 18:45:28.411944
---

# bn.setInnerAudioOption

▸ **setInnerAudioOption**(`options`): `Promise`<`void`\>

**`description`** Set the options of InnerAudioContext. Set to take effect globally for the current
Mini Program

Parameters

| Name      | Type                  | Description               |
| :-------- | :-------------------- | :------------------------ |
| `options` | `SetInnerAudioOption` | InnerAudioContext options |

Returns

`Promise`<`void`\>

## Interface: SetInnerAudioOption

| Name            | Type      | Description                                                                                                                                    |
| :-------------- | :-------- | :--------------------------------------------------------------------------------------------------------------------------------------------- |
| mixWithOther?   | `boolean` | To mix with other audio, set to true After that, the music in other apps will not be terminated.                                               |
| obeyMuteSwitch? | `boolean` | Whether to follow the "Mute" switch. It is true by default. If it is set to false, the audio file still sounds even if the "Mute" switch is on |
| speakerOn?      | `boolean` | true - playing on speakerphone, false - earpiece speaker, default is true                                                                      |

---

# bn.setInnerAudioOption

▸ **setInnerAudioOption**(`options`): `Promise`<`void`\>

**`description`** Set the options of InnerAudioContext. Set to take effect globally for the current
Mini Program

Parameters

| Name      | Type                  | Description               |
| :-------- | :-------------------- | :------------------------ |
| `options` | `SetInnerAudioOption` | InnerAudioContext options |

Returns

`Promise`<`void`\>

## Interface: SetInnerAudioOption

| Name            | Type      | Description                                                                                                                                    |
| :-------------- | :-------- | :--------------------------------------------------------------------------------------------------------------------------------------------- |
| mixWithOther?   | `boolean` | To mix with other audio, set to true After that, the music in other apps will not be terminated.                                               |
| obeyMuteSwitch? | `boolean` | Whether to follow the "Mute" switch. It is true by default. If it is set to false, the audio file still sounds even if the "Mute" switch is on |
| speakerOn?      | `boolean` | true - playing on speakerphone, false - earpiece speaker, default is true                                                                      |