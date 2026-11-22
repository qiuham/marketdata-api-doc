---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/overview
api_type: Guide
updated_at: 2026-11-22 18:36:32.074896
---

# Overview

## File Architecture

A mini program consists of two layers: the app and the page. The app layer describes the complete
application, whereas the page layer delineates individual pages. Also, there is an optional
configuration detailing the entire project.

The core of a Mini Program is built on three files, which must be located in the project's root
directory:

| File     | Required | Purpose                                             |
| -------- | -------- | --------------------------------------------------- |
| app.js   | yes      | Houses Mini Program logic                           |
| app.json | yes      | Contains common Mini Program settings               |
| app.bxss | no       | Serves as a common style sheet for the Mini Program |

A page consists of 4 files, all of which must share a filename and be placed in the same folder.

| File Type | Required | Purpose                  |
| --------- | -------- | ------------------------ |
| js        | yes      | Defines page logic       |
| bxml      | Yes      | Describes page structure |
| json      | No       | Configures the page      |
| bxss      | No       | Styles the page          |

Below is the typical structure of a project's directory:

```
.
└── src/
    ├─ app.js
    ├── app.json
    ├── app.bxss
    └── pages/
        └── detail/
            ├── index.js
            ├── index.bxml
            ├── index.bxss
            └── index.json
```

## Code Architecture

The Mini Program framework includes two key components: the Logic Layer (App Service) and the View
Layer (View). A Mini Program is equipped with its own view layer languages, BXML and BXSS, and a
logic layer framework based on JavaScript. Additionally, there is a system for data transfer and
event coordination between the two layers, which allows developers to concentrate on data and logic.

### Reactive Data Binding

The reactive data binding system formulates the core of the framework. It offers a remarkably simple
means to ensure data and view synchronization. Modifying the data requires a simple alteration on
the logic layer, after which it will get updated on the view layer.

Here's a simple illustration:

Run a Preview with the Developer Tool

```html
<!-- This represents our View -->
<view> Hello {{name}}! </view>
<button bindtap="changeName">Click me!</button>
```

```javascript
// This is our data.
var helloData = {
  name: "Binance",
};

// Registration of a Page.
Page({
  data: helloData,
  changeName: function (e) {
    // Data change sent to the view
    this.setData({
      name: "World",
    });
  },
});
```

This example demonstrates how developers can use the framework to bind the 'name' in the logic layer
data to 'name' in the view layer. This ensures that 'Hello Binance!' appears when the page opens.
Upon clicking the button, the view layer sends 'changeName' events to the logic layer, which
identifies and executes the corresponding event handler. After triggering the callback function, the
logic layer executes setData to change the name in data from 'Binance' to 'World'. As this data is
bound to the view layer, 'Hello World!' automatically applies to the view layer.

Note: Since the framework does not run in the browser, certain JavaScript capabilities in the web
are not available, such as 'document', 'window', etc.

## Style File

The style file has additional features and includes a new size unit called 'rpx'.

### Style Size Unit

rpx (responsive pixel) is an adaptive size unit that adjusts according to screen width.

As per standard, the screen's width is set to 750rpx.

For instance, on an iPhone6, the screen's width is 375px with 750 physical pixels, therefore 750rpx
= 375px = 750 physical pixels, and 1rpx = 0.5px = 1 physical pixel.

| Device       | rpx to px (screen's width/750) | px to rpx (750/screen's width) |
| ------------ | ------------------------------ | ------------------------------ |
| iPhone5      | 1rpx = 0.42px                  | 1px = 2.34rpx                  |
| iPhone6      | 1rpx = 0.5px                   | 1px = 2rpx                     |
| iPhone6 Plus | 1rpx = 0.552px                 | 1px = 1.81rpx                  |

Suggestion: For the development of Binance Mini Programme, iPhone6 specifications could serve as a
standard reference for designers.

Attention: One should be aware that specific inevitable limitations may arise on exceedingly small
screens. As far as possible, please endeavor to avoid such scenarios.

### Style Import

By using the @import statement, external stylesheets can be incorporated. Following the @import
statement, the relative path of the external stylesheet has to be mentioned and the line must
conclude with a semicolon (;).

Example code:

```css
/** common.bxss **/
.small-p {
  padding: 5px;
}
```

```css
/** app.bxss **/
@import "common.bxss";
.middle-p {
  padding: 15px;
}
```

## Incorporating Third-party NPM Modules

Mini programs support the integration of third-party modules. Install the necessary module by
executing the following command in the project's root directory.

```bash
$ npm install i18n --save
```

Note: Please bear in mind that the third-party module's browser-related web capabilities, such as
DOM operations or window.location, are unavailable.

---

# Overview

## File Architecture

A mini program consists of two layers: the app and the page. The app layer describes the complete
application, whereas the page layer delineates individual pages. Also, there is an optional
configuration detailing the entire project.

The core of a Mini Program is built on three files, which must be located in the project's root
directory:

| File     | Required | Purpose                                             |
| -------- | -------- | --------------------------------------------------- |
| app.js   | yes      | Houses Mini Program logic                           |
| app.json | yes      | Contains common Mini Program settings               |
| app.bxss | no       | Serves as a common style sheet for the Mini Program |

A page consists of 4 files, all of which must share a filename and be placed in the same folder.

| File Type | Required | Purpose                  |
| --------- | -------- | ------------------------ |
| js        | yes      | Defines page logic       |
| bxml      | Yes      | Describes page structure |
| json      | No       | Configures the page      |
| bxss      | No       | Styles the page          |

Below is the typical structure of a project's directory:

```
.
└── src/
    ├─ app.js
    ├── app.json
    ├── app.bxss
    └── pages/
        └── detail/
            ├── index.js
            ├── index.bxml
            ├── index.bxss
            └── index.json
```

## Code Architecture

The Mini Program framework includes two key components: the Logic Layer (App Service) and the View
Layer (View). A Mini Program is equipped with its own view layer languages, BXML and BXSS, and a
logic layer framework based on JavaScript. Additionally, there is a system for data transfer and
event coordination between the two layers, which allows developers to concentrate on data and logic.

### Reactive Data Binding

The reactive data binding system formulates the core of the framework. It offers a remarkably simple
means to ensure data and view synchronization. Modifying the data requires a simple alteration on
the logic layer, after which it will get updated on the view layer.

Here's a simple illustration:

Run a Preview with the Developer Tool

```html
<!-- This represents our View -->
<view> Hello {{name}}! </view>
<button bindtap="changeName">Click me!</button>
```

```javascript
// This is our data.
var helloData = {
  name: "Binance",
};

// Registration of a Page.
Page({
  data: helloData,
  changeName: function (e) {
    // Data change sent to the view
    this.setData({
      name: "World",
    });
  },
});
```

This example demonstrates how developers can use the framework to bind the 'name' in the logic layer
data to 'name' in the view layer. This ensures that 'Hello Binance!' appears when the page opens.
Upon clicking the button, the view layer sends 'changeName' events to the logic layer, which
identifies and executes the corresponding event handler. After triggering the callback function, the
logic layer executes setData to change the name in data from 'Binance' to 'World'. As this data is
bound to the view layer, 'Hello World!' automatically applies to the view layer.

Note: Since the framework does not run in the browser, certain JavaScript capabilities in the web
are not available, such as 'document', 'window', etc.

## Style File

The style file has additional features and includes a new size unit called 'rpx'.

### Style Size Unit

rpx (responsive pixel) is an adaptive size unit that adjusts according to screen width.

As per standard, the screen's width is set to 750rpx.

For instance, on an iPhone6, the screen's width is 375px with 750 physical pixels, therefore 750rpx
= 375px = 750 physical pixels, and 1rpx = 0.5px = 1 physical pixel.

| Device       | rpx to px (screen's width/750) | px to rpx (750/screen's width) |
| ------------ | ------------------------------ | ------------------------------ |
| iPhone5      | 1rpx = 0.42px                  | 1px = 2.34rpx                  |
| iPhone6      | 1rpx = 0.5px                   | 1px = 2rpx                     |
| iPhone6 Plus | 1rpx = 0.552px                 | 1px = 1.81rpx                  |

Suggestion: For the development of Binance Mini Programme, iPhone6 specifications could serve as a
standard reference for designers.

Attention: One should be aware that specific inevitable limitations may arise on exceedingly small
screens. As far as possible, please endeavor to avoid such scenarios.

### Style Import

By using the @import statement, external stylesheets can be incorporated. Following the @import
statement, the relative path of the external stylesheet has to be mentioned and the line must
conclude with a semicolon (;).

Example code:

```css
/** common.bxss **/
.small-p {
  padding: 5px;
}
```

```css
/** app.bxss **/
@import "common.bxss";
.middle-p {
  padding: 15px;
}
```

## Incorporating Third-party NPM Modules

Mini programs support the integration of third-party modules. Install the necessary module by
executing the following command in the project's root directory.

```bash
$ npm install i18n --save
```

Note: Please bear in mind that the third-party module's browser-related web capabilities, such as
DOM operations or window.location, are unavailable.