---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/network/createEventSource
api_type: Guide
updated_at: 2026-11-21 18:44:58.845906
---

# bn.createEventSource

▸ **createEventSource**(`url`): `undefined` \| `EventSource`

**`description`** Create a EventSource Instance

**`remark`** supported jssdk >= 4.43.0

**`remark`** must apply the permission of createEventSource (ENABLE_NETWORK_SSE) for the
mini-program

**`remark`** not support EventSource's configuration options yet

**`remark`** mdn https://developer.mozilla.org/en-US/docs/Web/API/EventSource

**`example`**

```js
const eventsource = bn.createEventSource("https://sse.dev/test?interval=5");
eventsource.onmessage = (res) => {
  console.log(res.data);
};
eventsource.onopen = (res) => {
  console.log(res);
};
eventsource.onerror = () => {
  console.log("error");
};
eventsource.addEventListener("custom", (res) => {
  console.log(res.data);
});
eventsource.close();
```

Parameters

| Name  | Type     |
| :---- | :------- |
| `url` | `string` |

Returns

`undefined` \| `EventSource`

---

# bn.createEventSource

▸ **createEventSource**(`url`): `undefined` \| `EventSource`

**`description`** Create a EventSource Instance

**`remark`** supported jssdk >= 4.43.0

**`remark`** must apply the permission of createEventSource (ENABLE_NETWORK_SSE) for the
mini-program

**`remark`** not support EventSource's configuration options yet

**`remark`** mdn https://developer.mozilla.org/en-US/docs/Web/API/EventSource

**`example`**

```js
const eventsource = bn.createEventSource("https://sse.dev/test?interval=5");
eventsource.onmessage = (res) => {
  console.log(res.data);
};
eventsource.onopen = (res) => {
  console.log(res);
};
eventsource.onerror = () => {
  console.log("error");
};
eventsource.addEventListener("custom", (res) => {
  console.log(res.data);
});
eventsource.close();
```

Parameters

| Name  | Type     |
| :---- | :------- |
| `url` | `string` |

Returns

`undefined` \| `EventSource`