---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/interface/hideToast
api_type: Guide
updated_at: 2026-11-18 18:45:56.630264
---

# bn.hideToast

▸ **hideToast**(): `Promise`<`void`\>

**`description`** The api to hide the toast created by showToast

**`remark`** supported jssdk >= 1.1.0

**`example`**

```ts
bn.showToast({
  title: "Success!",
  icon: "success",
  duration: 2000,
}).then(() => {
  setTimeout(() => {
    bn.hideToast().then(() => {
      console.log("manual hide the toast");
    });
  }, 1000);
});
```

Returns

`Promise`<`void`\>

---

# bn.hideToast

▸ **hideToast**(): `Promise`<`void`\>

**`description`** The api to hide the toast created by showToast

**`remark`** supported jssdk >= 1.1.0

**`example`**

```ts
bn.showToast({
  title: "Success!",
  icon: "success",
  duration: 2000,
}).then(() => {
  setTimeout(() => {
    bn.hideToast().then(() => {
      console.log("manual hide the toast");
    });
  }, 1000);
});
```

Returns

`Promise`<`void`\>