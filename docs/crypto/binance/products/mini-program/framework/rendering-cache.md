---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/rendering-cache
api_type: Guide
updated_at: 2026-11-18 18:37:03.730316
---

# Initial Rendering Cache

### How Initial Rendering Cache Works

The initialization of a mini-program page is divided into two parts:

1. Logic layer initialization: Load essential mini-program code, initialize the page `this` object
   (which includes all `this` objects related to custom components), and then send relevant data to
   the view layer.
2. View layer initialization: Load essential mini-program code, then wait for the logic layer to be
   initialized and receive the data sent by the logic layer, and finally render the page.

During the startup of the page, especially during the cold startup of the mini-program and when
entering the first page, the logic layer initialization time is relatively long. During the page
initialization process, users will see the standard loading screen of the mini-program (during the
cold start) or may experience slight flashes of white screen (during the page jump process).

When the initial rendering cache is enabled, the view layer does not need to wait for the logic
layer to be initialized, it can directly display the rendering result of the initial page `data` to
the users in advance, which greatly advances the time when the page is visible to the users. Its
working principle is as follows:

1. After a mini-program page is opened for the first time, the rendering result of the initial data
   of the page is recorded and written to a persistent cache area (the cache can be retained for a
   long time, but it may be cleared due to mini-program updates, basic library updates, storage
   space recycling, and other reasons).
2. When this page is opened for the second time, check whether there is still the rendering result
   of the last initial data of this page in the cache. If there is, it will directly display the
   rendering result.
3. If the rendering result in the cache is displayed, this page cannot temporarily respond to user
   events, and can only respond to user events after the logic layer is initialized.

Using the initial rendering cache, you can:

- Quickly display parts of the page that will never change, such as the navigation bar.
- Display a skeleton page in advance to enhance the user experience.
- Display custom loading tips.
- Display advertisements in advance, and so on.

### Static Initial Rendering Cache

The easiest way to enable initial rendering cache is to add the configuration item
`"initialRenderingCache": "static"` in the page's json file:

```json
{
  "initialRenderingCache": "static"
}
```

After adding this configuration item, preview the mini-program homepage on your phone, then kill the
mini-program and re-enter it, the homepage will be rendered by the initial rendering cache.

Note: In this case, the initial rendering cache records the result of applying `data` to `BXML` on
the page and does not include the result of any `setData` (For tarojs, it will records the result of
first setData).

For example, if you want to display the words "loading" on the page, these words are controlled by
the `loading` data field:

```html
<view bn:if="{{loading}}">Loading</view>
```

In this case, `loading` should be specified in `data` as true:

```javascript
// Correct way
Page({
  data: {
    loading: true,
  },
});
```

And not through `setData` to set `loading` as true:

```javascript
// Incorrect way! Don't do this!
Page({
  data: {},
  onLoad: function () {
    this.setData({
      loading: true,
    });
  },
});
```

### Adding Dynamic Content to the Initial Rendering Cache

In some cases, the rendering result of just the page data might be somewhat limited. Sometimes, you
may want to display additional variable content, such as some advertisement.

In such cases, you can use the "dynamic" initial rendering cache. Firstly, you need to configure
`"initialRenderingCache": "dynamic"`:

```json
{
  "initialRenderingCache": "dynamic"
}
```

At this point, the initial rendering cache will not be automatically enabled. You still need to call
`this.setInitialRenderingCache(dynamicData)` in the page to enable it. Here, `dynamicData` is a set
of data, which participates in rendering the page's WXML along with `data`.

```javascript
Page({
  data: {
    loading: true
  },
  onReady: function() {
    this.({
      loadingHint: 'Loading'
    }, function() {
      this.setInitialRenderingCache()
    })
  }
})
```

```html
<view wx:if="{{loading}}">{{loadingHint}}</view>
```

In principle, under the approach of dynamically generating initial rendering cache, the page is
re-rendered in the background using dynamic data, which can be relatively demanding in terms of
resources. Therefore, it's best to avoid frequently calling `this.setInitialRenderingCache`. If you
call it multiple times within a single page, only the last call will take effect.

Please note:

- You should not call `this.setInitialRenderingCache` earlier than the `onReady` lifecycle of Page
  or the `ready` lifecycle of Component as it may negatively impact performance.
- If you want to disable the initial rendering cache, you can call
  `this.clearInitialRenderingCache()`.

---

# Initial Rendering Cache

### How Initial Rendering Cache Works

The initialization of a mini-program page is divided into two parts:

1. Logic layer initialization: Load essential mini-program code, initialize the page `this` object
   (which includes all `this` objects related to custom components), and then send relevant data to
   the view layer.
2. View layer initialization: Load essential mini-program code, then wait for the logic layer to be
   initialized and receive the data sent by the logic layer, and finally render the page.

During the startup of the page, especially during the cold startup of the mini-program and when
entering the first page, the logic layer initialization time is relatively long. During the page
initialization process, users will see the standard loading screen of the mini-program (during the
cold start) or may experience slight flashes of white screen (during the page jump process).

When the initial rendering cache is enabled, the view layer does not need to wait for the logic
layer to be initialized, it can directly display the rendering result of the initial page `data` to
the users in advance, which greatly advances the time when the page is visible to the users. Its
working principle is as follows:

1. After a mini-program page is opened for the first time, the rendering result of the initial data
   of the page is recorded and written to a persistent cache area (the cache can be retained for a
   long time, but it may be cleared due to mini-program updates, basic library updates, storage
   space recycling, and other reasons).
2. When this page is opened for the second time, check whether there is still the rendering result
   of the last initial data of this page in the cache. If there is, it will directly display the
   rendering result.
3. If the rendering result in the cache is displayed, this page cannot temporarily respond to user
   events, and can only respond to user events after the logic layer is initialized.

Using the initial rendering cache, you can:

- Quickly display parts of the page that will never change, such as the navigation bar.
- Display a skeleton page in advance to enhance the user experience.
- Display custom loading tips.
- Display advertisements in advance, and so on.

### Static Initial Rendering Cache

The easiest way to enable initial rendering cache is to add the configuration item
`"initialRenderingCache": "static"` in the page's json file:

```json
{
  "initialRenderingCache": "static"
}
```

After adding this configuration item, preview the mini-program homepage on your phone, then kill the
mini-program and re-enter it, the homepage will be rendered by the initial rendering cache.

Note: In this case, the initial rendering cache records the result of applying `data` to `BXML` on
the page and does not include the result of any `setData` (For tarojs, it will records the result of
first setData).

For example, if you want to display the words "loading" on the page, these words are controlled by
the `loading` data field:

```html
<view bn:if="{{loading}}">Loading</view>
```

In this case, `loading` should be specified in `data` as true:

```javascript
// Correct way
Page({
  data: {
    loading: true,
  },
});
```

And not through `setData` to set `loading` as true:

```javascript
// Incorrect way! Don't do this!
Page({
  data: {},
  onLoad: function () {
    this.setData({
      loading: true,
    });
  },
});
```

### Adding Dynamic Content to the Initial Rendering Cache

In some cases, the rendering result of just the page data might be somewhat limited. Sometimes, you
may want to display additional variable content, such as some advertisement.

In such cases, you can use the "dynamic" initial rendering cache. Firstly, you need to configure
`"initialRenderingCache": "dynamic"`:

```json
{
  "initialRenderingCache": "dynamic"
}
```

At this point, the initial rendering cache will not be automatically enabled. You still need to call
`this.setInitialRenderingCache(dynamicData)` in the page to enable it. Here, `dynamicData` is a set
of data, which participates in rendering the page's WXML along with `data`.

```javascript
Page({
  data: {
    loading: true
  },
  onReady: function() {
    this.({
      loadingHint: 'Loading'
    }, function() {
      this.setInitialRenderingCache()
    })
  }
})
```

```html
<view wx:if="{{loading}}">{{loadingHint}}</view>
```

In principle, under the approach of dynamically generating initial rendering cache, the page is
re-rendered in the background using dynamic data, which can be relatively demanding in terms of
resources. Therefore, it's best to avoid frequently calling `this.setInitialRenderingCache`. If you
call it multiple times within a single page, only the last call will take effect.

Please note:

- You should not call `this.setInitialRenderingCache` earlier than the `onReady` lifecycle of Page
  or the `ready` lifecycle of Component as it may negatively impact performance.
- If you want to disable the initial rendering cache, you can call
  `this.clearInitialRenderingCache()`.