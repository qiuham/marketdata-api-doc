---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/media/getImageInfo
api_type: Guide
updated_at: 2026-11-23 18:45:55.913678
---

# bn.getImageInfo

▸ **getImageInfo**(`options`): `Promise`<`ImageInfoResponse`\>

**`description`** Get image detail information

**`example`**

```js
bn.getImageInfo({
  src: "https://bin.bnbstatic.com/image/julia/new-hompage/foreground-image-light.png",
}).then((info) => {
  console.log(info);
});
```

Parameters

| Name      | Type                     | Description   |
| :-------- | :----------------------- | :------------ |
| `options` | `ImageInfoRequestOption` | Image options |

Returns

`Promise`<`ImageInfoResponse`\>

Image detail information

## Interface: ImageInfoRequestOption

| Name | Type     | Description                                                         |
| :--- | :------- | :------------------------------------------------------------------ |
| src  | `string` | Image src path, support network path, local path, code package path |

## Interface: ImageInfoResponse

| Name        | Type     | Description                           |
| :---------- | :------- | :------------------------------------ |
| width       | `number` | Image original width in px            |
| height      | `number` | Image original height in px           |
| path        | `string` | Local path of Image                   |
| orientation | `string` | Device orientation when taking photos |
| type        | `string` | Image format, for example 'jpeg'      |

---

# bn.getImageInfo

▸ **getImageInfo**(`options`): `Promise`<`ImageInfoResponse`\>

**`description`** Get image detail information

**`example`**

```js
bn.getImageInfo({
  src: "https://bin.bnbstatic.com/image/julia/new-hompage/foreground-image-light.png",
}).then((info) => {
  console.log(info);
});
```

Parameters

| Name      | Type                     | Description   |
| :-------- | :----------------------- | :------------ |
| `options` | `ImageInfoRequestOption` | Image options |

Returns

`Promise`<`ImageInfoResponse`\>

Image detail information

## Interface: ImageInfoRequestOption

| Name | Type     | Description                                                         |
| :--- | :------- | :------------------------------------------------------------------ |
| src  | `string` | Image src path, support network path, local path, code package path |

## Interface: ImageInfoResponse

| Name        | Type     | Description                           |
| :---------- | :------- | :------------------------------------ |
| width       | `number` | Image original width in px            |
| height      | `number` | Image original height in px           |
| path        | `string` | Local path of Image                   |
| orientation | `string` | Device orientation when taking photos |
| type        | `string` | Image format, for example 'jpeg'      |