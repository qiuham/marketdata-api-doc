---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/basics/MPApiError
api_type: Guide
updated_at: 2026-11-28 18:46:45.796308
---

# bn.MPApiError

• **MPApiError**:

**`description`** Standard error class for all errors thrown by Mini Program API.

**`example`**

```ts
try {
  const res = await bn.getSystemInfo();
} catch (err) {
  err instanceof bn.MPApiError; // true
}
```

---

# bn.MPApiError

• **MPApiError**:

**`description`** Standard error class for all errors thrown by Mini Program API.

**`example`**

```ts
try {
  const res = await bn.getSystemInfo();
} catch (err) {
  err instanceof bn.MPApiError; // true
}
```