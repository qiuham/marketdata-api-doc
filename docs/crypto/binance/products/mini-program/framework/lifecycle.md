---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/lifecycle
api_type: Guide
updated_at: 2026-11-22 18:36:33.547761
---

# Lifecycle

Developing Mini Programs with React comes with a few differences compared to using React on the web.

## The Entry Component

You have to register each mini program. You can do this by calling the App method in the file named
'app.js'. This will let the Mini Program use specific functions. These functions include: tracking
the lifecycle, listening for any errors, and detecting when a page cannot be found.

```javascript
//app.js
App({
  onLaunch(options) {
    // Do something initial when launch.
  },
  onShow(options) {
    // Do something when show.
  },
  onHide() {
    // Do something when hide.
  },
  onError(msg) {
    console.log(msg);
  },
  globalData: "I am global data",
});
```

A Mini Program has only one app instance, which is shared to all pages. Developers can obtain the
globally unique app instance by using the getApp method, and then obtain data in the app or call a
function registered with App by the developers.

```javascript
// xxx.js
const appInstance = getApp();
console.log(appInstance.globalData); // I am global data
```

## Entry Configuration

We can create a new file called 'app.json' for overall settings.

The way we set up this file is based on the mini program's global configuration.

```javascript
// app.json
{
  pages: ['pages/index/index'],
  window: {
    backgroundTextStyle: 'light',
    navigationBarBackgroundColor: '#fff',
    navigationBarTitleText: 'Title',
    navigationBarTextStyle: 'black',
  },
}
```

### onLaunch ()

It starts when the app launches.

### onShow ()

It starts when the app launches, or when it goes from the background to the front.

### onHide ()

It starts when the app goes from the front to the background.

### onError(err)

Listens for when the Mini Program has errors. For example, these errors can be from a broken script
or a problem with a function call. The 'err' is what the error is.

## Page

For every page in a Mini Program, we need to register a page instance. We do this by calling the
Page method in the js file that matches the page. This lets us set the page's initial data, life
cycle tracking function, and event handling function.

```javascript
// index.js
Page({
  data: {
    text: "This is page data.",
  },
  onLoad: function (options) {
    // Do some initialize when page load.
  },
  onReady: function () {
    // Do something when page ready.
  },
  onShow: function () {
    // Do something when page show.
  },
  onHide: function () {
    // Do something when page hide.
  },
  onUnload: function () {
    // Do something when page close.
  },
  onPullDownRefresh: function () {
    // Do something when pull down.
  },
  onReachBottom: function () {
    // Do something when page reach bottom.
  },
  onShareAppMessage: function () {
    // return custom share data when user share.
  },
  onPageScroll: function () {
    // Do something when page scroll
  },
  onTabItemTap(item) {
    console.log(item.index);
    console.log(item.pagePath);
    console.log(item.text);
  },
  // Event handler.
  viewTap: function () {
    this.setData(
      {
        text: "Set some data for updating view.",
      },
      function () {
        // this is setData callback
      },
    );
  },
});
```

### onTabItemTap

This happens every time a tab item is tapped.

#### Parameters

##### Object

| Property | Type   | Description                                 |
| -------- | ------ | ------------------------------------------- |
| index    | String | the position of the tab item, starting at 0 |
| pagePath | String | the location of the tab item                |
| text     | String | the written content of the tab item         |

## Page Configuration

For every page file (like. /pages/index/index.js), we can make a new . /pages/index/index.json file
for configuring the page.

```json
// file: pages/index/index.json
{
  "navigationBarTitleText": "Home"
}
```

### onLoad (options)

During this lifecycle, page navigation parameters can be obtained by calling
`getCurrentInstance().router`.

### onReady ()

At this point in the lifecycle, the Mini Program has already transferred the DOM nodes to the
rendering layer using APIs.

### onShow ()

This is triggered when the page is displayed or brought to the front.

### onHide ()

This is triggered when the page is hidden or moved to the background.

### onErr(err)

This listens for Mini Program errors such as a script error or API Calls.

### onPageScroll()

This listens for the user scrolling the page.

**Parameter Object object:**

| Property  | Type   | Description                                       |
| --------- | ------ | ------------------------------------------------- |
| scrollTop | Number | Scroll distance in the vertical direction (in px) |

**Note: Defining this method in a page should only be done when necessary to reduce potential
performance impacts. Also, be cautious of repeated executions in onPageScroll, it could increase
communication time.**

_Example of a child component in a page_

```js
Page({
  onPageScroll({ scrollTop }) {
    console.log("onPageScroll", scrollTop);
  },
});
```

### onReachBottom()

This listens for the user scrolling to the bottom of the page.

- You can set the trigger distance `onReachBottomDistance` in the `app.json` window option or in the
  Page Configuration.
- This event only triggers once when the page scrolls within the trigger distance.

_Example of a child component in a page_

```js
Page({
  onReachBottom() {
    console.log("onPageReachBottom");
  },
});
```

### onShareAppMessage(Object)

Listen to user-initiated share actions, such as clicking on the in-page share button
`open-type="share"`, the top-right menu "Share", or executing `bn.showSharePanel`, and customize the
shared content.

#### Parameters

##### Object

| Property | Type   | Description                                                                                                             |
| -------- | ------ | ----------------------------------------------------------------------------------------------------------------------- |
| from     | String | Share event source: `button`: in-page share button, `menu`: top-right retweet menu, `code`: Execute `bn.showSharePanel` |
| target   | String | If `from` value is `button`, then `target` is the triggered share `button`, otherwise `undefined`                       |

This event handler requires a return of an Object or Promise to customize the shared content:

| field    | Type     | Description                                                                      | Default value             |
| :------- | :------- | :------------------------------------------------------------------------------- | :------------------------ |
| title    | String   | Share title                                                                      | Current Mini Program name |
| desc     | String   | Description                                                                      |                           |
| imageUrl | String   | Custom image path, should be a network image path. Supports PNG and JPG formats. | Uses default screenshot   |
| path     | Function | Share path. Must be a full path starting with /                                  | Current page path         |
| success  | Function | Callback function when the user forwards on                                      |                           |

```javascript
Page({
  onShareAppMessage(...args) {
    console.log('onShareAppMessage', args)
    return Promise.resolve({
      title: 'my title',
      desc: 'mydesc',
      imageUrl: 'https://public.bnbstatic.com/static/images/common/ogImage.jpg',
      path: 'pages/extended/pages/share/share?p=1',
      success: res => console.log('shareResult', res.shareResult)),
    }
  })
})
```

---

# Lifecycle

Developing Mini Programs with React comes with a few differences compared to using React on the web.

## The Entry Component

You have to register each mini program. You can do this by calling the App method in the file named
'app.js'. This will let the Mini Program use specific functions. These functions include: tracking
the lifecycle, listening for any errors, and detecting when a page cannot be found.

```javascript
//app.js
App({
  onLaunch(options) {
    // Do something initial when launch.
  },
  onShow(options) {
    // Do something when show.
  },
  onHide() {
    // Do something when hide.
  },
  onError(msg) {
    console.log(msg);
  },
  globalData: "I am global data",
});
```

A Mini Program has only one app instance, which is shared to all pages. Developers can obtain the
globally unique app instance by using the getApp method, and then obtain data in the app or call a
function registered with App by the developers.

```javascript
// xxx.js
const appInstance = getApp();
console.log(appInstance.globalData); // I am global data
```

## Entry Configuration

We can create a new file called 'app.json' for overall settings.

The way we set up this file is based on the mini program's global configuration.

```javascript
// app.json
{
  pages: ['pages/index/index'],
  window: {
    backgroundTextStyle: 'light',
    navigationBarBackgroundColor: '#fff',
    navigationBarTitleText: 'Title',
    navigationBarTextStyle: 'black',
  },
}
```

### onLaunch ()

It starts when the app launches.

### onShow ()

It starts when the app launches, or when it goes from the background to the front.

### onHide ()

It starts when the app goes from the front to the background.

### onError(err)

Listens for when the Mini Program has errors. For example, these errors can be from a broken script
or a problem with a function call. The 'err' is what the error is.

## Page

For every page in a Mini Program, we need to register a page instance. We do this by calling the
Page method in the js file that matches the page. This lets us set the page's initial data, life
cycle tracking function, and event handling function.

```javascript
// index.js
Page({
  data: {
    text: "This is page data.",
  },
  onLoad: function (options) {
    // Do some initialize when page load.
  },
  onReady: function () {
    // Do something when page ready.
  },
  onShow: function () {
    // Do something when page show.
  },
  onHide: function () {
    // Do something when page hide.
  },
  onUnload: function () {
    // Do something when page close.
  },
  onPullDownRefresh: function () {
    // Do something when pull down.
  },
  onReachBottom: function () {
    // Do something when page reach bottom.
  },
  onShareAppMessage: function () {
    // return custom share data when user share.
  },
  onPageScroll: function () {
    // Do something when page scroll
  },
  onTabItemTap(item) {
    console.log(item.index);
    console.log(item.pagePath);
    console.log(item.text);
  },
  // Event handler.
  viewTap: function () {
    this.setData(
      {
        text: "Set some data for updating view.",
      },
      function () {
        // this is setData callback
      },
    );
  },
});
```

### onTabItemTap

This happens every time a tab item is tapped.

#### Parameters

##### Object

| Property | Type   | Description                                 |
| -------- | ------ | ------------------------------------------- |
| index    | String | the position of the tab item, starting at 0 |
| pagePath | String | the location of the tab item                |
| text     | String | the written content of the tab item         |

## Page Configuration

For every page file (like. /pages/index/index.js), we can make a new . /pages/index/index.json file
for configuring the page.

```json
// file: pages/index/index.json
{
  "navigationBarTitleText": "Home"
}
```

### onLoad (options)

During this lifecycle, page navigation parameters can be obtained by calling
`getCurrentInstance().router`.

### onReady ()

At this point in the lifecycle, the Mini Program has already transferred the DOM nodes to the
rendering layer using APIs.

### onShow ()

This is triggered when the page is displayed or brought to the front.

### onHide ()

This is triggered when the page is hidden or moved to the background.

### onErr(err)

This listens for Mini Program errors such as a script error or API Calls.

### onPageScroll()

This listens for the user scrolling the page.

**Parameter Object object:**

| Property  | Type   | Description                                       |
| --------- | ------ | ------------------------------------------------- |
| scrollTop | Number | Scroll distance in the vertical direction (in px) |

**Note: Defining this method in a page should only be done when necessary to reduce potential
performance impacts. Also, be cautious of repeated executions in onPageScroll, it could increase
communication time.**

_Example of a child component in a page_

```js
Page({
  onPageScroll({ scrollTop }) {
    console.log("onPageScroll", scrollTop);
  },
});
```

### onReachBottom()

This listens for the user scrolling to the bottom of the page.

- You can set the trigger distance `onReachBottomDistance` in the `app.json` window option or in the
  Page Configuration.
- This event only triggers once when the page scrolls within the trigger distance.

_Example of a child component in a page_

```js
Page({
  onReachBottom() {
    console.log("onPageReachBottom");
  },
});
```

### onShareAppMessage(Object)

Listen to user-initiated share actions, such as clicking on the in-page share button
`open-type="share"`, the top-right menu "Share", or executing `bn.showSharePanel`, and customize the
shared content.

#### Parameters

##### Object

| Property | Type   | Description                                                                                                             |
| -------- | ------ | ----------------------------------------------------------------------------------------------------------------------- |
| from     | String | Share event source: `button`: in-page share button, `menu`: top-right retweet menu, `code`: Execute `bn.showSharePanel` |
| target   | String | If `from` value is `button`, then `target` is the triggered share `button`, otherwise `undefined`                       |

This event handler requires a return of an Object or Promise to customize the shared content:

| field    | Type     | Description                                                                      | Default value             |
| :------- | :------- | :------------------------------------------------------------------------------- | :------------------------ |
| title    | String   | Share title                                                                      | Current Mini Program name |
| desc     | String   | Description                                                                      |                           |
| imageUrl | String   | Custom image path, should be a network image path. Supports PNG and JPG formats. | Uses default screenshot   |
| path     | Function | Share path. Must be a full path starting with /                                  | Current page path         |
| success  | Function | Callback function when the user forwards on                                      |                           |

```javascript
Page({
  onShareAppMessage(...args) {
    console.log('onShareAppMessage', args)
    return Promise.resolve({
      title: 'my title',
      desc: 'mydesc',
      imageUrl: 'https://public.bnbstatic.com/static/images/common/ogImage.jpg',
      path: 'pages/extended/pages/share/share?p=1',
      success: res => console.log('shareResult', res.shareResult)),
    }
  })
})
```