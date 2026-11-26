---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/basics/MPApiError
api_type: Guide
updated_at: 2026-11-26 18:49:30.767672
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