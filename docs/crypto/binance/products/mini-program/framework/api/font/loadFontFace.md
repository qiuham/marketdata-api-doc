---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/font/loadFontFace
api_type: Guide
updated_at: 2026-11-24 18:46:11.608126
---

# bn.loadFontFace

▸ **loadFontFace**(`payload`): `Promise`<`LoadFontFaceResponse`\>

**`description`** Dynamic load network font, file address should be download type.

**`example`**

```js
bn.loadFontFace({
  family: "Bitstream Wedding band Serif Bold",
  source: 'url("https://sungd.github.io/Pacific.ttf")',
  success: console.log,
});
```

Parameters

| Name      | Type                  |
| :-------- | :-------------------- |
| `payload` | `LoadFontFacePayload` |

Returns

`Promise`<`LoadFontFaceResponse`\>

status: when success is 'loaded', otherwise, it's failed

## LoadFontFacePayload

Ƭ **LoadFontFacePayload**: `Object`

Type declaration

| Name            | Type                                                                                                                        | Description                                                                                |
| :-------------- | :-------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------- |
| `family`        | `string`                                                                                                                    | Defined font name                                                                          |
| `source`        | `string`                                                                                                                    | The address of the font resource. The suggested format is TTF and Woff                     |
| `scopes?`       | (`"webview"` \| `"native"`)[]                                                                                               | Font scope, optional value is webview / Native, default Webview                            |
| `desc?`         | { `style?`: `"normal"` \| `"italic"` \| `"oblique"` \| \`oblique ${string}\` ; `variant?`: `string` ; `weight?`: `string` } | Optional font descriptor                                                                   |
| `desc.style?`   | `"normal"` \| `"italic"` \| `"oblique"` \| \`oblique ${string}\`                                                            | Font style, optional value is normal / italic / oblique                                    |
| `desc.variant?` | `string`                                                                                                                    | Sets font display text for small uppercase letters, optional normal / small-caps / inherit |
| `desc.weight?`  | `string`                                                                                                                    | Font size, optional value is normal / bold / 100 / 200../ 900                              |
| `success?`      | (`res`: `Omit`<`LoadFontFaceResponse`, `"status"`\>) => `void`                                                              | -                                                                                          |
| `fail?`         | (`res`: `Omit`<`LoadFontFaceResponse`, `"status"`\>) => `void`                                                              | -                                                                                          |
| `complete?`     | (`res`: `Omit`<`LoadFontFaceResponse`, `"status"`\>) => `void`                                                              | -                                                                                          |

## LoadFontFaceResponse

Ƭ **LoadFontFaceResponse**: `Object`

Type declaration

| Name      | Type                    | Description                                         |
| :-------- | :---------------------- | :-------------------------------------------------- |
| `status?` | `"loaded"` \| `"error"` | when success is 'loaded', when fail, it's undefined |
| `errMsg`  | `string`                | when success is ''                                  |
| `code?`   | `number` \| `string`    | -                                                   |

---

## LoadFontFaceResponse

Ƭ **LoadFontFaceResponse**: `Object`

Type declaration

| Name      | Type                    | Description                                         |
| :-------- | :---------------------- | :-------------------------------------------------- |
| `status?` | `"loaded"` \| `"error"` | when success is 'loaded', when fail, it's undefined |
| `errMsg`  | `string`                | when success is ''                                  |
| `code?`   | `number` \| `string`    | -                                                   |

---

---

# bn.loadFontFace

▸ **loadFontFace**(`payload`): `Promise`<`LoadFontFaceResponse`\>

**`description`** Dynamic load network font, file address should be download type.

**`example`**

```js
bn.loadFontFace({
  family: "Bitstream Wedding band Serif Bold",
  source: 'url("https://sungd.github.io/Pacific.ttf")',
  success: console.log,
});
```

Parameters

| Name      | Type                  |
| :-------- | :-------------------- |
| `payload` | `LoadFontFacePayload` |

Returns

`Promise`<`LoadFontFaceResponse`\>

status: when success is 'loaded', otherwise, it's failed

## LoadFontFacePayload

Ƭ **LoadFontFacePayload**: `Object`

Type declaration

| Name            | Type                                                                                                                        | Description                                                                                |
| :-------------- | :-------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------- |
| `family`        | `string`                                                                                                                    | Defined font name                                                                          |
| `source`        | `string`                                                                                                                    | The address of the font resource. The suggested format is TTF and Woff                     |
| `scopes?`       | (`"webview"` \| `"native"`)[]                                                                                               | Font scope, optional value is webview / Native, default Webview                            |
| `desc?`         | { `style?`: `"normal"` \| `"italic"` \| `"oblique"` \| \`oblique ${string}\` ; `variant?`: `string` ; `weight?`: `string` } | Optional font descriptor                                                                   |
| `desc.style?`   | `"normal"` \| `"italic"` \| `"oblique"` \| \`oblique ${string}\`                                                            | Font style, optional value is normal / italic / oblique                                    |
| `desc.variant?` | `string`                                                                                                                    | Sets font display text for small uppercase letters, optional normal / small-caps / inherit |
| `desc.weight?`  | `string`                                                                                                                    | Font size, optional value is normal / bold / 100 / 200../ 900                              |
| `success?`      | (`res`: `Omit`<`LoadFontFaceResponse`, `"status"`\>) => `void`                                                              | -                                                                                          |
| `fail?`         | (`res`: `Omit`<`LoadFontFaceResponse`, `"status"`\>) => `void`                                                              | -                                                                                          |
| `complete?`     | (`res`: `Omit`<`LoadFontFaceResponse`, `"status"`\>) => `void`                                                              | -                                                                                          |

## LoadFontFaceResponse

Ƭ **LoadFontFaceResponse**: `Object`

Type declaration

| Name      | Type                    | Description                                         |
| :-------- | :---------------------- | :-------------------------------------------------- |
| `status?` | `"loaded"` \| `"error"` | when success is 'loaded', when fail, it's undefined |
| `errMsg`  | `string`                | when success is ''                                  |
| `code?`   | `number` \| `string`    | -                                                   |

---

## LoadFontFaceResponse

Ƭ **LoadFontFaceResponse**: `Object`

Type declaration

| Name      | Type                    | Description                                         |
| :-------- | :---------------------- | :-------------------------------------------------- |
| `status?` | `"loaded"` \| `"error"` | when success is 'loaded', when fail, it's undefined |
| `errMsg`  | `string`                | when success is ''                                  |
| `code?`   | `number` \| `string`    | -                                                   |

---