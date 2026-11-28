---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/media/openDocument
api_type: Guide
updated_at: 2026-11-28 18:43:50.943864
---

# bn.openDocument

▸ **openDocument**(`options?`): `Promise`<{}\>

**`description`** Open document file

**`remark`** supported jssdk >= 4.26.0

**`example`**

```ts
await bn.openDocument({
  filePath: "/root/xxx.pdf",
  fileType: "pdf",
});
```

Parameters

| Name       | Type                  |
| :--------- | :-------------------- |
| `options?` | `OpenDocumentOptions` |

Returns

`Promise`<{}\>

## OpenDocumentOptions

Ƭ **OpenDocumentOptions**: `Object`

Type declaration

| Name        | Type                                                                         | Description                                                         |
| :---------- | :--------------------------------------------------------------------------- | :------------------------------------------------------------------ |
| `filePath`  | `string`                                                                     | local file path, support temporary path returned by bn.downloadFile |
| `fileType?` | `"doc"` \| `"docx"` \| `"xls"` \| `"xlsx"` \| `"ppt"` \| `"pptx"` \| `"pdf"` | file type, valid values are doc, docx, xls, xlsx, ppt, pptx, pdf    |

---

# bn.openDocument

▸ **openDocument**(`options?`): `Promise`<{}\>

**`description`** Open document file

**`remark`** supported jssdk >= 4.26.0

**`example`**

```ts
await bn.openDocument({
  filePath: "/root/xxx.pdf",
  fileType: "pdf",
});
```

Parameters

| Name       | Type                  |
| :--------- | :-------------------- |
| `options?` | `OpenDocumentOptions` |

Returns

`Promise`<{}\>

## OpenDocumentOptions

Ƭ **OpenDocumentOptions**: `Object`

Type declaration

| Name        | Type                                                                         | Description                                                         |
| :---------- | :--------------------------------------------------------------------------- | :------------------------------------------------------------------ |
| `filePath`  | `string`                                                                     | local file path, support temporary path returned by bn.downloadFile |
| `fileType?` | `"doc"` \| `"docx"` \| `"xls"` \| `"xlsx"` \| `"ppt"` \| `"pptx"` \| `"pdf"` | file type, valid values are doc, docx, xls, xlsx, ppt, pptx, pdf    |