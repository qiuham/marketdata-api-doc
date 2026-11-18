---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/router
api_type: Guide
updated_at: 2026-11-18 02:18:38.368255
---

# Router

## Routing API

In a mini-program, default routing features are presented and don't necessitate any further
configuration by the developer.

You just need to declare the pages in the configuration of the entrance file, then you can jump to
the destination page by utilizing the API provided by the mini-program. For example:

```javascript
// Navigate to the destination page and open a new page
bn.navigateTo({
  url: "/pages/page/path/name",
});
```

```javascript
// Navigate to the destination page and open it on the current page
bn.redirectTo({
  url: "/pages/page/path/name",
});
```

For a detailed description of the API, please refer to the [API](api) documentation.

## Route Passing

You can redirect by appending a query string parameter after all the jumped URLs. For example:

```javascript
// Pass in the parameters id=2&type=test
bn.navigateTo({
  url: "/pages/page/path/name?id=2&type=test",
});
```

In this case, the passed parameters will be available in the lifecycle method of the target page
once the jump is successful. This can be accessed through `getCurrentInstance().router.params`. For
the above navigation action, in the `onShow()` lifecycle of the target page:

```javascript
Page({
  onShow() {
    console.log(getCurrentInstance().router.params); // output { id: 2, type: 'test' }
  },
});
```

## EventChannel

When calling `navigateTo`, we can use `EventChannel` to facilitate communication between the opener
page and the opened page. For instance:

```javascript
// Page A
bn.navigateTo({
  url: "/pages/page/path/B",
  events: {
    // Add listeners to receive data from the opened page
    acceptDataFromOpenedPage: function (data) {
      console.log(data);
    },
    someEvent: function (data) {
      console.log(data);
    },
  },
}).then((res) => {
  // Send data to the opened page
  res.eventChannel.emit("acceptDataFromOpenerPage", { data: "I am the opener page" });
});
```

```javascript
// Page B
Page({
  onShow() {
    const eventChannel = getCurrentInstance().page.getOpenerEventChannel();
    // Send data to the opener page
    eventChannel.emit("acceptDataFromOpenedPage", { data: "I am the opened page" });
    eventChannel.emit("someEvent", { data: "test" });
    // Add listener to receive data from the opener page
    eventChannel.on("acceptDataFromOpenerPage", function (data) {
      console.log(data);
    });
  },
});
```

---

# Router

## Routing API

In a mini-program, default routing features are presented and don't necessitate any further
configuration by the developer.

You just need to declare the pages in the configuration of the entrance file, then you can jump to
the destination page by utilizing the API provided by the mini-program. For example:

```javascript
// Navigate to the destination page and open a new page
bn.navigateTo({
  url: "/pages/page/path/name",
});
```

```javascript
// Navigate to the destination page and open it on the current page
bn.redirectTo({
  url: "/pages/page/path/name",
});
```

For a detailed description of the API, please refer to the [API](api) documentation.

## Route Passing

You can redirect by appending a query string parameter after all the jumped URLs. For example:

```javascript
// Pass in the parameters id=2&type=test
bn.navigateTo({
  url: "/pages/page/path/name?id=2&type=test",
});
```

In this case, the passed parameters will be available in the lifecycle method of the target page
once the jump is successful. This can be accessed through `getCurrentInstance().router.params`. For
the above navigation action, in the `onShow()` lifecycle of the target page:

```javascript
Page({
  onShow() {
    console.log(getCurrentInstance().router.params); // output { id: 2, type: 'test' }
  },
});
```

## EventChannel

When calling `navigateTo`, we can use `EventChannel` to facilitate communication between the opener
page and the opened page. For instance:

```javascript
// Page A
bn.navigateTo({
  url: "/pages/page/path/B",
  events: {
    // Add listeners to receive data from the opened page
    acceptDataFromOpenedPage: function (data) {
      console.log(data);
    },
    someEvent: function (data) {
      console.log(data);
    },
  },
}).then((res) => {
  // Send data to the opened page
  res.eventChannel.emit("acceptDataFromOpenerPage", { data: "I am the opener page" });
});
```

```javascript
// Page B
Page({
  onShow() {
    const eventChannel = getCurrentInstance().page.getOpenerEventChannel();
    // Send data to the opener page
    eventChannel.emit("acceptDataFromOpenedPage", { data: "I am the opened page" });
    eventChannel.emit("someEvent", { data: "test" });
    // Add listener to receive data from the opener page
    eventChannel.on("acceptDataFromOpenerPage", function (data) {
      console.log(data);
    });
  },
});
```