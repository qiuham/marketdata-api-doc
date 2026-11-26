---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/faq
api_type: Guide
updated_at: 2026-11-26 18:38:50.653788
---

# FAQ

## `getCurrentInstance` query is incorrect

When you are using `tarojs` to develop your mini program, sometimes query is incorrect with the api
`getCurrentInstance`. Make sure the getCurrentInstance is inside the useDidShow hook

```ts
useDidShow(() => {
  const query = getCurrentInstance().router.params;
});
```

---

# FAQ

## `getCurrentInstance` query is incorrect

When you are using `tarojs` to develop your mini program, sometimes query is incorrect with the api
`getCurrentInstance`. Make sure the getCurrentInstance is inside the useDidShow hook

```ts
useDidShow(() => {
  const query = getCurrentInstance().router.params;
});
```