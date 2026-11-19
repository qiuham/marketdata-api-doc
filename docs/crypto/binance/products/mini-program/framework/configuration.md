---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/configuration
api_type: Guide
updated_at: 2026-11-19 18:40:11.301258
---

# Configuration

The `app.json` file, located in the root directory of Mini Program, is utilized to impose global
configurations on Mini Programs. The contents of this file should be a JSON object encompassing the
following properties:

### Configuration Items

| Property      | Type                           | Default Value | Required | Description                                                             |
| ------------- | ------------------------------ | ------------- | -------- | ----------------------------------------------------------------------- |
| entryPagePath | `string`                       | -             | ✓        | index page name                                                         |
| pages         | `string[]`                     | -             | ✓        | Page Path List                                                          |
| window        | `Object`                       | -             | -        | Global default window behavior                                          |
| tabBar        | `Object`                       | -             | -        | Behavior of the `tab` bar at the bottom of the page.                    |
| subPackages   | `Object[]`                     | -             | -        | subPackage structure configuration.                                     |
| darkmode      | `boolean`                      | -             | -        | whether app is in darkmode                                              |
| theme         | `{light?:Object,dark?:Object}` | -             | -        | theme configuration, basically replaced by themeLocation                |
| themeLocation | `string`                       | -             | -        | Indicate the location of theme.json,it's required when darkmode is true |

### window

| Property                     | Type       | Default Value | Required | Description                                                                                                                                                                                                                                                                           |
| ---------------------------- | ---------- | ------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| navigationBarBackgroundColor | `HexColor` | #000000       | -        | The navigation bar background color                                                                                                                                                                                                                                                   |
| navigationBarButtonColor     | `HexColor` | #707A8A       | -        | The button color in the navigation.                                                                                                                                                                                                                                                   |
| navigationBarTitleText       | `string`   | -             | ✓        | Title text of the navigation bar                                                                                                                                                                                                                                                      |
| navigationBarTextStyle       | `string`   | white         | -        | The title color of the navigation bar, only supports black or white                                                                                                                                                                                                                   |
| navigationStyle              | `string`   | default       | -        | The navigation bar style. Only the following values are supported. `default`: the default style. `custom`: custom navigation bar, only retains the Mini Program control button in the upper-right corner, click [here](/docs/mini-program/framework/extended#navigation) for details. |
| backgroundTextStyle          | `string`   | dark          | -        | The pull-down loading style, only dark and light are supported.                                                                                                                                                                                                                       |
| backgroundColor              | `HexColor` | #ffffff       | -        | The background color of the window.                                                                                                                                                                                                                                                   |

### tabBar

Should the Mini Program operate as a multi-tab application (employing a tab bar at the lower or
upper part of the application interface for toggling between tabs), the tabBar configuration setting
allows you to define the interaction with the tab bar, as well as control the specific pages that
appear when the user alternates between the given tabs.

| Property        | Type       | Default Value | Required | Description                                                                              |
| --------------- | ---------- | ------------- | -------- | ---------------------------------------------------------------------------------------- |
| color           | `HexColor` |               | ✓        | The default color of the tab bar text, only supports hex color codes.                    |
| selectedColor   | `HexColor` |               | ✓        | The color of the tab bar text when being selected, only supports hex color codes.        |
| backgroundColor | `HexColor` |               | ✓        | The color of the tab bar background, only supports hex color codes.                      |
| borderStyle     | `string`   | black         |          | The border color of the tab bar, only supports `black` and `white`.                      |
| list            | `array`    |               | ✓        | The tab list (see the `list` property description), supports 2 to 5 tabs.                |
| position        | `string`   | bottom        |          | The tabBar position, only supports `bottom` and `top`.                                   |
| custom          | `boolean`  | false         |          | A custom tabBar, click [here](/docs/mini-program/framework/extended#tabbar) for details. |

The list property accepts an array, **which can only configure 2 to 5 tabs**. The tabs are listed in
the order of the array. Each item is an object with the following properties:

| Property         | Type     | Default Value | Required | Description                                                                                                                                                                                                          |
| ---------------- | -------- | ------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| pagePath         | `string` |               | ✓        | The page path, which must be defined first in pages.                                                                                                                                                                 |
| text             | `string` |               | ✓        | The text of tab buttons.                                                                                                                                                                                             |
| iconPath         | `string` |               |          | The image path. The size of the icon is limited to 40 KB, suggested dimensions: 81px by 81px, online images are not supported. **When `position` is set to `top`, the icon is not displayed.**                       |
| selectedIconPath | `string` |               |          | The image path for the selected icon. The size of the icon is limited to 40 KB, suggested dimensions: 81px by 81px, online images are not supported. **When `position` is set to `top`, the icon is not displayed.** |

### subPackages

In certain scenarios, developers might need to segment a Mini Program into distinct subunits,
bundling these subsidiary packages into separate subpackages during construction, hence enabling
users to load them on an as-needed basis.

During the development of a subpackage project, one or more subpackages may appear. Every
subpackaged Mini Program should encompass a main package embodying the default start page/TabBar
page, along with common resources and necessary JS scripts used by all subpackages. The subdivisions
of sub-packages are subject to the developer's configuration.

Upon initiating the Mini Program, the user's device downloads the main package by default, launching
the pages housed within the main package. When a user navigates to a page within a subpackage, the
related subpackage is downloaded and displayed upon successful completion of the download.

> Supported from SDK ^3.2.0, IDE ^2.9.0 and Native ^2.40.0

| Property    | Type       | Default Value | Required | Description                        |
| ----------- | ---------- | ------------- | -------- | ---------------------------------- |
| root        | `string`   |               | ✓        | root of subPackage                 |
| name        | `string`   |               |          | alias name                         |
| pages       | `string[]` |               | ✓        | page list related to root          |
| independent | `boolean`  |               | ✓        | If it is an independent subPackage |

### useExtendedLib

This indicates the extra library that's needed. Right now, you can use this for:

- react

When you set useExtendedLib, it's like you're adding the newest version of that library's npm
Package. The good part is, this doesn't make your Mini Program package bigger. The RC (Release
Candidate) tool version lets you add references in sub-packages. You can use it like this:

Use `true` to get the latestVersion.

```json
{
  "useExtendedLib": {
    "react": true
  }
}
```

You can also specify the exact version you want to use.

```json
{
  "useExtendedLib": {
    "react": "17.0.2"
  }
}
```

### prefetchRules

Data prefetching lets the Mini Program start a request early when it's first turned on, and it saves
the response from the request. Then, when you actually make the request, you can use the saved data
to cut down on the time for network requests. Here's how it works:

![img](https://bin.bnbstatic.com/image/julia/docs/mini-program/prefetch-flow.png)

#### Configure prefetch rules

Data prefetching rules need to be configured in app.json, examples are as follows:

```json
{
  "prefetchRules": {
    // launch path that need to be configured with prefetch requests
    "pages/index/index": {
      // request url
      "https://developer.binance.com/${pageid}": {
        // request method
        "method": "POST",
        // request header
        "header": {
          "token": "${token}"
        },
        // request body
        "data": {
          "pageSize": "${pageSize}",
          "pageNum": 1
        },
        // request response type
        "responseType": "text",
        "hitPrefetchExtraRules": {
          "requiredQueryKeys": ["testid"],
          "requiredHeaderKeys": ["token"]
        }
      }
    },
    // match all launch paths
    "*": {
      // local file path, language is the variable
      "file://nezha-i18n-data_${language}.json": {
        // whether to wait for the file download to complete when starting the mini program
        "mandatory": true
      }
    }
  }
}
```

#### Configure variables

To make requests dynamic, we use configuration variables. These have the format ${variable}. To
assign the variable, we replace the text ${variable} in the prefetchRules configuration string with
the value of the variable.

#### Variable data source

Configuration variables can come from three places, listed by priority:

1. The query parameters in the Mini Program's page route
2. Data that developers have saved in storage
3. Data from the getSystemInfo interface, such as language

When the client looks for a variable, it starts with the highest priority source. If it finds the
variable there, it stops looking. If not, it checks the next source. If it can't find the variable
in any of the sources, it won't make the request.

#### Request url

The url is the basic part of a request. With a complete url, we can start a request. Right now, we
can use a variable in the path and query of a url, but not in the host.

For example, let's say the prefetch configuration is set up a certain way. If the page route is
pages/index/index?pageid=1000, and the developer stored the pageSize variable with a value of 10,
then the final prefetch request will be https://developer.binance.com/1000?pagesize=10&pagenum=1

```json
{
  "prefetchRules": {
    "pages/index/index": {
      "https://developer.binance.com/${pageid}?pagesize=${pageSize}&pagenum=1": {}
    }
  }
}
```

#### Request parameters

The value of the request address serves as the request parameters. These include method, header,
data, and responseType, which correspond to the bn.request API's parameters. These parameters also
support configuration variables. Here is a table outlining the default values rules for method,
header, data, and responseType:

| Property     | Type               | Default Value                        | Required | Description                                           |
| ------------ | ------------------ | ------------------------------------ | -------- | ----------------------------------------------------- |
| header       | `object`           | {'content-type': 'application/json'} |          | Request header                                        |
| method       | `string`           | GET                                  |          | Request method, support GET, POST                     |
| data         | `string or object` | null                                 |          | Request data, needs to be consistent to hit the cache |
| responseType | `string`           | text                                 |          | Response data type, optional value: text              |

For example, suppose the request parameters are configured as follows:

```json
{
  "https://developer.binance.com/${pageid}": {
    "method": "POST",
    "header": {
      "token": "${token}"
    },
    "data": {
      "pageSize": "${pageSize}",
      "pageNum": 1
    }
  }
}
```

If the page route is pages/index/index?pageid=1000, the developer has stored the pageSize variable
with a value of 10, and also stored the token variable with a value of test_token, then the
parameters of the final prefetch request would look like this:

```json
{
  "https://developer.binance.com/1000": {
    "method": "POST",
    "header": {
      "token": "test_token"
    },
    "data": {
      "pageSize": "10",
      "pageNum": 1
    }
  }
}
```

#### Use prefetch cache

The bn.request function includes an extra parameter, usePrefetchCache, and the return data includes
the attribute isPrefetch to indicate whether the data was prefetched. Here's an example:

```json
{
  "prefetchRules": {
    "pages/index/index": {
      "https://developer1.binance.com/${sid}?testid=${testid}&testdata=${sData}": {
        "method": "POST",
        "header": {
          "testCookie": "${sCookie}",
          "token": "xxxs1823730"
        },
        "data": {
          "mData": "${mData}"
        },
        "responseType": ""
      }
    }
  }
}
```

```js
//storage
const testCookie = bn.getStorageSync("sData");
const sCookie = bn.getStorageSync("sCookie");
const mData = bn.getStorageSync("mData");

//request
const token = "xxxs1823730";
const { sid, testid } = option.query;
const url = `https://developer1.binance.com/${sid}?testid=${testid}&testdata=${sData}`;
const header = { testCookie, token };
const data = { mData };

bn.request({
  url,
  header,
  data,
  method: "POST",
  dataType: "json",
  responseType: "text",
  usePrefetchCache: true,
  success: (res) => {
    console.log("Whether the returned data is from prefetching:", res.isPrefetch);
    console.log("Response data:", res.data);
  },
});
```

#### Configure Matching rules

Like the example at the beginning. You can configure `"hitPrefetchExtraRules"` property to control
the behavior of matching rules.

This property includes two keys:

```json
{
  "prefetchRules": {
    "pages/index/index": {
      "https://developer.binance.com/?a=${a}&b=bbb": {
        "header": { "c": "${c}", "d": "ddd" },
        "hitPrefetchExtraRules": {
          "requiredQueryKeys": ["a", "b"],
          "requiredHeaderKeys": ["c"]
        }
      }
    }
  }
}
```

![img](https://bin.bnbstatic.com/image/julia/docs/mini-program/match-rule.png)

When native get a prefetchRule, need to replace the variable first and get the accurate url &
parameters, and parse the accurate url to query keys and values (eg. query key is **a**, query value
might be **aaa** in above example). If **requiredQueryKeys** is not declared or is a empty array, it
will be considered as using exact match.

| requiredQueryKeys                            | Rule URL / Request URL                                                                  | hit |
| -------------------------------------------- | --------------------------------------------------------------------------------------- | --- |
| []                                           | https://developer.binance.com/?a=aaa&b=bbb / https://developer.binance.com/?b=bbb&a=aaa | yes |
| [] a is extra                                | https://developer.binance.com/?b=bbb / https://developer.binance.com/?b=bbb&a=aaa       | no  |
| [] a is missing                              | https://developer.binance.com/?b=bbb&a=aaa / https://developer.binance.com/?b=bbb       | no  |
| ["b"] a is extra                             | https://developer.binance.com/?b=bbb / https://developer.binance.com/?b=bbb&a=aaa       | yes |
| ["b"] a is different                         | https://developer.binance.com/?b=bbb&a=ccc / https://developer.binance.com/?b=bbb&a=aaa | yes |
| ["b"] a is missing                           | https://developer.binance.com/?b=bbb&a=aaa / https://developer.binance.com/?b=bbb       | yes |
| ["b"] b is missing                           | https://developer.binance.com/?b=bbb&a=aaa / https://developer.binance.com/?a=aaa       | no  |
| ["b"] b is different                         | https://developer.binance.com/?b=bbb&a=aaa / https://developer.binance.com/?b=ccc&a=aaa | no  |
| ["a", "b"]                                   | https://developer.binance.com/?b=bbb&a=aaa / https://developer.binance.com/?b=aaa&a=aaa | no  |
| ["c", "b"] c is not in rule url, exact match | https://developer.binance.com/?b=bbb&a=aaa / https://developer.binance.com/?a=ccc&b=bbb | no  |
| [b] b is not in rule url, exact match        | https://developer.binance.com/?a=aaa / https://developer.binance.com/?b=bbb             | no  |

The behavior of requiredHeaderKeys is similar to requiredQueryKeys, but it effects header field, not
query of url

#### File Prefetch

Besides prefetching network requests, we also support prefetching files. The file prefetch
configuration is similar to the network request configuration, but the value of the request address
is the local file path. The file path also supports configuration variables.

For example, if the file prefetch rules are set up as follows:

```json
{
  "prefetchRules": {
    "pages/index/index": {
      "file://nezha-i18n-data_${language}.json": {
        "mandatory": true
      }
    }
  }
}
```

If the page route is pages/index/index, and the client language is zh_CN, the variable 'language'
will be replaced with 'zh_CN', which is retrieved from the getSystemInfo API. Therefore, the final
prefetch request will be file://nezha-i18n-data_zh_CN.json.

Upon launching the mini-program, the client will immediately begin downloading the
file://nezha-i18n-data_zh_CN.json file using parallel download. If the value of `mandatory` is set
as `true`, the mini-program will only launch once the file has successfully downloaded. If it's not
set as `true`, the mini-program will launch immediately without waiting for the file to be
downloaded (non-blocking).

Developers can then use the bn.getFileSystemManager API to read the contents of the file. Here's an
example:

```js
const fs = bn.getFileSystemManager();
const filePath = "file://nezha-i18n-data_zh_CN.json";
const res = fs.readFileSync(filePath, "utf8");
console.log("File content:", res);
```

## Page Configuration

For each Mini Program page, you may use the .json file that shares the same name as the Mini Program
to configure the window behaviors of that page. The configuration items in the current page will
overwrite the corresponding `window` configuration items in the app.json file. The file content of
this json file should be a JSON object. Here's an example:

```json
{
  "navigationBarBackgroundColor": "#ffffff",
  "navigationBarTextStyle": "black",
  "navigationBarTitleText": "Binance API feature demo",
  "backgroundColor": "#eeeeee",
  "backgroundTextStyle": "light",
  "initialRenderingCache": "static",
  "staticTemplate": {
    "enable": true,
    "removeSkeleton": true,
    "data": { "list": [] }
  }
}
```

| Property              | Type                                                    | Default Value | Required | Description                                                                 |
| --------------------- | ------------------------------------------------------- | ------------- | -------- | --------------------------------------------------------------------------- |
| initialRenderingCache | `"static"`\|`"dynamic"`                                 |               | -        | Enable rendering cache.                                                     |
| staticTemplate        | `{enable:boolean,removeSkeleton?:boolean,data?:Object}` |               | -        | Page template can render as static template based on data in configuration. |

## DarkMode

We provide developers the ability to incorporate Dark Mode in their applets.

### Enable DarkMode

To enable Dark Mode, set `{ "darkmode" : true }` in the `app.json` file. Once enabled, all basic
components will display different default styles based on the system theme. The navigation bar and
tab bar will automatically switch according to the following configuration.

### Related Configuration

When `{ "darkmode": true }` is set in app.json, certain applet configuration items can be set via
variables, enabling definition of colors or icons under different themes in the variable
configuration file as follows:

1. Configure `themeLocation` in `app.json`, specifying the path to the variable configuration file
   `theme.json`. For instance, to add `theme.json` in the root directory, configure
   `{"themeLocation": "/path/to/theme.json"}`
2. Define related variables in `theme.json`.
3. In `app.json`, reference variables that start with `@`.

Properties that support configuration through variables include:

1. The window property of the global configuration and the property under the page configuration
   - navigationBarBackgroundColor
   - navigationBarTextStyle
   - backgroundColor
   - backgroundTextStyle
   - backgroundColorTop
   - backgroundColorBottom

2. Global configuration properties of window.tabBar
   - color
   - selectedColor
   - backgroundColor
   - borderStyle
   - list
     - iconPath
     - selectedIconPath

### Variable configuration file theme.json

The `theme.json` file is used for variable definitions related to the color theme. Prioritize
setting the path to `theme.json` in `themeLocation`, as the variable configuration cannot be read
otherwise.

The configuration file must contain the following properties:

| Attribute | Type   | Required | Description                        |
| --------- | ------ | -------- | ---------------------------------- |
| light     | object | Yes      | Variables definition in light mode |
| dark      | object | Yes      | Variables definition in dark mode  |

Both light and dark modes can define variable names and values in the key: value format, as shown
below:

```js
{
  "light": {
    "navBgColor": "#f6f6f6",
    "navTxtStyle": "black"
  },
  "dark": {
    "navBgColor": "#191919",
    "navTxtStyle": "white"
  }
}
```

After the definition is completed, it can be referenced at the beginning of `@` in the relevant
properties of the `global configuration` or `page configuration`, for example:

```js
// global configuration
{
  "window": {
    "navigationBarBackgroundColor": "@navBgColor",
    "navigationBarTextStyle": "@navTxtStyle"
  }
}
// page configuration
{
  "navigationBarBackgroundColor": "@navBgColor",
  "navigationBarTextStyle": "@navTxtStyle"
}
```

### Configuration example

`app.json` (the example omits configuration items other than those related to the theme)

```js
{
    "window": {
        "navigationBarBackgroundColor": "@navBgColor",
        "navigationBarTextStyle": "@navTxtStyle",
        "backgroundColor": "@bgColor",
        "backgroundTextStyle": "@bgTxtStyle",
        "backgroundColorTop": "@bgColorTop",
        "backgroundColorBottom": "@bgColorBottom"
    },
    "tabBar": {
        "color": "@tabFontColor",
        "selectedColor": "@tabSelectedColor",
        "backgroundColor": "@tabBgColor",
        "borderStyle": "@tabBorderStyle",
        "list": [{
            "iconPath": "@iconPath1",
            "selectedIconPath": "@selectedIconPath1"
        }, {
            "iconPath": "@iconPath2",
            "selectedIconPath": "@selectedIconPath2"
        }]
    }
}
```

`theme.json`

```js
{
    "light": {
        "navBgColor": "#f6f6f6",
        "navTxtStyle": "black",
        "bgColor": "#ffffff",
        "bgTxtStyle": "light",
        "bgColorTop": "#eeeeee",
        "bgColorBottom": "#efefef",
        "tabFontColor": "#000000",
        "tabSelectedColor": "#3cc51f",
        "tabBgColor": "#ffffff",
        "tabBorderStyle": "black",
        "iconPath1": "image/icon1_light.png",
        "selectedIconPath1": "image/selected_icon1_light.png",
        "iconPath2": "image/icon2_light.png",
        "selectedIconPath2": "image/selected_icon2_light.png",
    },
    "dark": {
        "navBgColor": "#191919",
        "navTxtStyle": "white",
        "bgColor": "#1f1f1f",
        "bgTxtStyle": "dark",
        "bgColorTop": "#191919",
        "bgColorBottom": "#1f1f1f",
        "tabFontColor": "#ffffff",
        "tabSelectedColor": "#51a937",
        "tabBgColor": "#191919",
        "tabBorderStyle": "white",
        "iconPath1": "image/icon1_dark.png",
        "selectedIconPath1": "image/selected_icon1_dark.png",
        "iconPath2": "image/icon2_dark.png",
        "selectedIconPath2": "image/selected_icon2_dark.png",
    }
}

```

### Get the current system theme

If `"darkmode": true` is declared in `app.json`, the output of `bn.getSystemInfo` or
`bn.getSystemInfoSync` will include a theme attribute, the value of which can be either 'light' or
'dark'.

If `app.json` does not include the `"darkmode": true` declaration, the theme attribute is
inaccessible (meaning, 'theme' would be undefined).

### Listening for Theme Switching Events

There are two ways to monitor for theme switching:

1. In `App()`, insert the `onThemeChange` callback function. This callback will get triggered when
   the theme switches.
2. Utilize `bn.onThemeChange` to monitor for theme changes. You can cancel the monitoring using
   `bn.offThemeChange`.

### BXSS Adaptation

In `BXSS`, we support theme adaptation through the media query `prefers-color-scheme`. This approach
is consistent with the adaptation method used in Web. See the example below:

```css
/* normal css style begin */
.case-background {
  background: white;
}
.case-text {
  color: black;
}
/* normal css style end */

@media (prefers-color-scheme: dark) {
  /* style under DarkMode start */
  .case-background {
    background: #1b1b1b;
  }
  .case-text {
    color: #ffffff;
  }
  /* style under DarkMode end */
}
```

---

# Configuration

The `app.json` file, located in the root directory of Mini Program, is utilized to impose global
configurations on Mini Programs. The contents of this file should be a JSON object encompassing the
following properties:

### Configuration Items

| Property      | Type                           | Default Value | Required | Description                                                             |
| ------------- | ------------------------------ | ------------- | -------- | ----------------------------------------------------------------------- |
| entryPagePath | `string`                       | -             | ✓        | index page name                                                         |
| pages         | `string[]`                     | -             | ✓        | Page Path List                                                          |
| window        | `Object`                       | -             | -        | Global default window behavior                                          |
| tabBar        | `Object`                       | -             | -        | Behavior of the `tab` bar at the bottom of the page.                    |
| subPackages   | `Object[]`                     | -             | -        | subPackage structure configuration.                                     |
| darkmode      | `boolean`                      | -             | -        | whether app is in darkmode                                              |
| theme         | `{light?:Object,dark?:Object}` | -             | -        | theme configuration, basically replaced by themeLocation                |
| themeLocation | `string`                       | -             | -        | Indicate the location of theme.json,it's required when darkmode is true |

### window

| Property                     | Type       | Default Value | Required | Description                                                                                                                                                                                                                                                                           |
| ---------------------------- | ---------- | ------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| navigationBarBackgroundColor | `HexColor` | #000000       | -        | The navigation bar background color                                                                                                                                                                                                                                                   |
| navigationBarButtonColor     | `HexColor` | #707A8A       | -        | The button color in the navigation.                                                                                                                                                                                                                                                   |
| navigationBarTitleText       | `string`   | -             | ✓        | Title text of the navigation bar                                                                                                                                                                                                                                                      |
| navigationBarTextStyle       | `string`   | white         | -        | The title color of the navigation bar, only supports black or white                                                                                                                                                                                                                   |
| navigationStyle              | `string`   | default       | -        | The navigation bar style. Only the following values are supported. `default`: the default style. `custom`: custom navigation bar, only retains the Mini Program control button in the upper-right corner, click [here](/docs/mini-program/framework/extended#navigation) for details. |
| backgroundTextStyle          | `string`   | dark          | -        | The pull-down loading style, only dark and light are supported.                                                                                                                                                                                                                       |
| backgroundColor              | `HexColor` | #ffffff       | -        | The background color of the window.                                                                                                                                                                                                                                                   |

### tabBar

Should the Mini Program operate as a multi-tab application (employing a tab bar at the lower or
upper part of the application interface for toggling between tabs), the tabBar configuration setting
allows you to define the interaction with the tab bar, as well as control the specific pages that
appear when the user alternates between the given tabs.

| Property        | Type       | Default Value | Required | Description                                                                              |
| --------------- | ---------- | ------------- | -------- | ---------------------------------------------------------------------------------------- |
| color           | `HexColor` |               | ✓        | The default color of the tab bar text, only supports hex color codes.                    |
| selectedColor   | `HexColor` |               | ✓        | The color of the tab bar text when being selected, only supports hex color codes.        |
| backgroundColor | `HexColor` |               | ✓        | The color of the tab bar background, only supports hex color codes.                      |
| borderStyle     | `string`   | black         |          | The border color of the tab bar, only supports `black` and `white`.                      |
| list            | `array`    |               | ✓        | The tab list (see the `list` property description), supports 2 to 5 tabs.                |
| position        | `string`   | bottom        |          | The tabBar position, only supports `bottom` and `top`.                                   |
| custom          | `boolean`  | false         |          | A custom tabBar, click [here](/docs/mini-program/framework/extended#tabbar) for details. |

The list property accepts an array, **which can only configure 2 to 5 tabs**. The tabs are listed in
the order of the array. Each item is an object with the following properties:

| Property         | Type     | Default Value | Required | Description                                                                                                                                                                                                          |
| ---------------- | -------- | ------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| pagePath         | `string` |               | ✓        | The page path, which must be defined first in pages.                                                                                                                                                                 |
| text             | `string` |               | ✓        | The text of tab buttons.                                                                                                                                                                                             |
| iconPath         | `string` |               |          | The image path. The size of the icon is limited to 40 KB, suggested dimensions: 81px by 81px, online images are not supported. **When `position` is set to `top`, the icon is not displayed.**                       |
| selectedIconPath | `string` |               |          | The image path for the selected icon. The size of the icon is limited to 40 KB, suggested dimensions: 81px by 81px, online images are not supported. **When `position` is set to `top`, the icon is not displayed.** |

### subPackages

In certain scenarios, developers might need to segment a Mini Program into distinct subunits,
bundling these subsidiary packages into separate subpackages during construction, hence enabling
users to load them on an as-needed basis.

During the development of a subpackage project, one or more subpackages may appear. Every
subpackaged Mini Program should encompass a main package embodying the default start page/TabBar
page, along with common resources and necessary JS scripts used by all subpackages. The subdivisions
of sub-packages are subject to the developer's configuration.

Upon initiating the Mini Program, the user's device downloads the main package by default, launching
the pages housed within the main package. When a user navigates to a page within a subpackage, the
related subpackage is downloaded and displayed upon successful completion of the download.

> Supported from SDK ^3.2.0, IDE ^2.9.0 and Native ^2.40.0

| Property    | Type       | Default Value | Required | Description                        |
| ----------- | ---------- | ------------- | -------- | ---------------------------------- |
| root        | `string`   |               | ✓        | root of subPackage                 |
| name        | `string`   |               |          | alias name                         |
| pages       | `string[]` |               | ✓        | page list related to root          |
| independent | `boolean`  |               | ✓        | If it is an independent subPackage |

### useExtendedLib

This indicates the extra library that's needed. Right now, you can use this for:

- react

When you set useExtendedLib, it's like you're adding the newest version of that library's npm
Package. The good part is, this doesn't make your Mini Program package bigger. The RC (Release
Candidate) tool version lets you add references in sub-packages. You can use it like this:

Use `true` to get the latestVersion.

```json
{
  "useExtendedLib": {
    "react": true
  }
}
```

You can also specify the exact version you want to use.

```json
{
  "useExtendedLib": {
    "react": "17.0.2"
  }
}
```

### prefetchRules

Data prefetching lets the Mini Program start a request early when it's first turned on, and it saves
the response from the request. Then, when you actually make the request, you can use the saved data
to cut down on the time for network requests. Here's how it works:

![img](https://bin.bnbstatic.com/image/julia/docs/mini-program/prefetch-flow.png)

#### Configure prefetch rules

Data prefetching rules need to be configured in app.json, examples are as follows:

```json
{
  "prefetchRules": {
    // launch path that need to be configured with prefetch requests
    "pages/index/index": {
      // request url
      "https://developer.binance.com/${pageid}": {
        // request method
        "method": "POST",
        // request header
        "header": {
          "token": "${token}"
        },
        // request body
        "data": {
          "pageSize": "${pageSize}",
          "pageNum": 1
        },
        // request response type
        "responseType": "text",
        "hitPrefetchExtraRules": {
          "requiredQueryKeys": ["testid"],
          "requiredHeaderKeys": ["token"]
        }
      }
    },
    // match all launch paths
    "*": {
      // local file path, language is the variable
      "file://nezha-i18n-data_${language}.json": {
        // whether to wait for the file download to complete when starting the mini program
        "mandatory": true
      }
    }
  }
}
```

#### Configure variables

To make requests dynamic, we use configuration variables. These have the format ${variable}. To
assign the variable, we replace the text ${variable} in the prefetchRules configuration string with
the value of the variable.

#### Variable data source

Configuration variables can come from three places, listed by priority:

1. The query parameters in the Mini Program's page route
2. Data that developers have saved in storage
3. Data from the getSystemInfo interface, such as language

When the client looks for a variable, it starts with the highest priority source. If it finds the
variable there, it stops looking. If not, it checks the next source. If it can't find the variable
in any of the sources, it won't make the request.

#### Request url

The url is the basic part of a request. With a complete url, we can start a request. Right now, we
can use a variable in the path and query of a url, but not in the host.

For example, let's say the prefetch configuration is set up a certain way. If the page route is
pages/index/index?pageid=1000, and the developer stored the pageSize variable with a value of 10,
then the final prefetch request will be https://developer.binance.com/1000?pagesize=10&pagenum=1

```json
{
  "prefetchRules": {
    "pages/index/index": {
      "https://developer.binance.com/${pageid}?pagesize=${pageSize}&pagenum=1": {}
    }
  }
}
```

#### Request parameters

The value of the request address serves as the request parameters. These include method, header,
data, and responseType, which correspond to the bn.request API's parameters. These parameters also
support configuration variables. Here is a table outlining the default values rules for method,
header, data, and responseType:

| Property     | Type               | Default Value                        | Required | Description                                           |
| ------------ | ------------------ | ------------------------------------ | -------- | ----------------------------------------------------- |
| header       | `object`           | {'content-type': 'application/json'} |          | Request header                                        |
| method       | `string`           | GET                                  |          | Request method, support GET, POST                     |
| data         | `string or object` | null                                 |          | Request data, needs to be consistent to hit the cache |
| responseType | `string`           | text                                 |          | Response data type, optional value: text              |

For example, suppose the request parameters are configured as follows:

```json
{
  "https://developer.binance.com/${pageid}": {
    "method": "POST",
    "header": {
      "token": "${token}"
    },
    "data": {
      "pageSize": "${pageSize}",
      "pageNum": 1
    }
  }
}
```

If the page route is pages/index/index?pageid=1000, the developer has stored the pageSize variable
with a value of 10, and also stored the token variable with a value of test_token, then the
parameters of the final prefetch request would look like this:

```json
{
  "https://developer.binance.com/1000": {
    "method": "POST",
    "header": {
      "token": "test_token"
    },
    "data": {
      "pageSize": "10",
      "pageNum": 1
    }
  }
}
```

#### Use prefetch cache

The bn.request function includes an extra parameter, usePrefetchCache, and the return data includes
the attribute isPrefetch to indicate whether the data was prefetched. Here's an example:

```json
{
  "prefetchRules": {
    "pages/index/index": {
      "https://developer1.binance.com/${sid}?testid=${testid}&testdata=${sData}": {
        "method": "POST",
        "header": {
          "testCookie": "${sCookie}",
          "token": "xxxs1823730"
        },
        "data": {
          "mData": "${mData}"
        },
        "responseType": ""
      }
    }
  }
}
```

```js
//storage
const testCookie = bn.getStorageSync("sData");
const sCookie = bn.getStorageSync("sCookie");
const mData = bn.getStorageSync("mData");

//request
const token = "xxxs1823730";
const { sid, testid } = option.query;
const url = `https://developer1.binance.com/${sid}?testid=${testid}&testdata=${sData}`;
const header = { testCookie, token };
const data = { mData };

bn.request({
  url,
  header,
  data,
  method: "POST",
  dataType: "json",
  responseType: "text",
  usePrefetchCache: true,
  success: (res) => {
    console.log("Whether the returned data is from prefetching:", res.isPrefetch);
    console.log("Response data:", res.data);
  },
});
```

#### Configure Matching rules

Like the example at the beginning. You can configure `"hitPrefetchExtraRules"` property to control
the behavior of matching rules.

This property includes two keys:

```json
{
  "prefetchRules": {
    "pages/index/index": {
      "https://developer.binance.com/?a=${a}&b=bbb": {
        "header": { "c": "${c}", "d": "ddd" },
        "hitPrefetchExtraRules": {
          "requiredQueryKeys": ["a", "b"],
          "requiredHeaderKeys": ["c"]
        }
      }
    }
  }
}
```

![img](https://bin.bnbstatic.com/image/julia/docs/mini-program/match-rule.png)

When native get a prefetchRule, need to replace the variable first and get the accurate url &
parameters, and parse the accurate url to query keys and values (eg. query key is **a**, query value
might be **aaa** in above example). If **requiredQueryKeys** is not declared or is a empty array, it
will be considered as using exact match.

| requiredQueryKeys                            | Rule URL / Request URL                                                                  | hit |
| -------------------------------------------- | --------------------------------------------------------------------------------------- | --- |
| []                                           | https://developer.binance.com/?a=aaa&b=bbb / https://developer.binance.com/?b=bbb&a=aaa | yes |
| [] a is extra                                | https://developer.binance.com/?b=bbb / https://developer.binance.com/?b=bbb&a=aaa       | no  |
| [] a is missing                              | https://developer.binance.com/?b=bbb&a=aaa / https://developer.binance.com/?b=bbb       | no  |
| ["b"] a is extra                             | https://developer.binance.com/?b=bbb / https://developer.binance.com/?b=bbb&a=aaa       | yes |
| ["b"] a is different                         | https://developer.binance.com/?b=bbb&a=ccc / https://developer.binance.com/?b=bbb&a=aaa | yes |
| ["b"] a is missing                           | https://developer.binance.com/?b=bbb&a=aaa / https://developer.binance.com/?b=bbb       | yes |
| ["b"] b is missing                           | https://developer.binance.com/?b=bbb&a=aaa / https://developer.binance.com/?a=aaa       | no  |
| ["b"] b is different                         | https://developer.binance.com/?b=bbb&a=aaa / https://developer.binance.com/?b=ccc&a=aaa | no  |
| ["a", "b"]                                   | https://developer.binance.com/?b=bbb&a=aaa / https://developer.binance.com/?b=aaa&a=aaa | no  |
| ["c", "b"] c is not in rule url, exact match | https://developer.binance.com/?b=bbb&a=aaa / https://developer.binance.com/?a=ccc&b=bbb | no  |
| [b] b is not in rule url, exact match        | https://developer.binance.com/?a=aaa / https://developer.binance.com/?b=bbb             | no  |

The behavior of requiredHeaderKeys is similar to requiredQueryKeys, but it effects header field, not
query of url

#### File Prefetch

Besides prefetching network requests, we also support prefetching files. The file prefetch
configuration is similar to the network request configuration, but the value of the request address
is the local file path. The file path also supports configuration variables.

For example, if the file prefetch rules are set up as follows:

```json
{
  "prefetchRules": {
    "pages/index/index": {
      "file://nezha-i18n-data_${language}.json": {
        "mandatory": true
      }
    }
  }
}
```

If the page route is pages/index/index, and the client language is zh_CN, the variable 'language'
will be replaced with 'zh_CN', which is retrieved from the getSystemInfo API. Therefore, the final
prefetch request will be file://nezha-i18n-data_zh_CN.json.

Upon launching the mini-program, the client will immediately begin downloading the
file://nezha-i18n-data_zh_CN.json file using parallel download. If the value of `mandatory` is set
as `true`, the mini-program will only launch once the file has successfully downloaded. If it's not
set as `true`, the mini-program will launch immediately without waiting for the file to be
downloaded (non-blocking).

Developers can then use the bn.getFileSystemManager API to read the contents of the file. Here's an
example:

```js
const fs = bn.getFileSystemManager();
const filePath = "file://nezha-i18n-data_zh_CN.json";
const res = fs.readFileSync(filePath, "utf8");
console.log("File content:", res);
```

## Page Configuration

For each Mini Program page, you may use the .json file that shares the same name as the Mini Program
to configure the window behaviors of that page. The configuration items in the current page will
overwrite the corresponding `window` configuration items in the app.json file. The file content of
this json file should be a JSON object. Here's an example:

```json
{
  "navigationBarBackgroundColor": "#ffffff",
  "navigationBarTextStyle": "black",
  "navigationBarTitleText": "Binance API feature demo",
  "backgroundColor": "#eeeeee",
  "backgroundTextStyle": "light",
  "initialRenderingCache": "static",
  "staticTemplate": {
    "enable": true,
    "removeSkeleton": true,
    "data": { "list": [] }
  }
}
```

| Property              | Type                                                    | Default Value | Required | Description                                                                 |
| --------------------- | ------------------------------------------------------- | ------------- | -------- | --------------------------------------------------------------------------- |
| initialRenderingCache | `"static"`\|`"dynamic"`                                 |               | -        | Enable rendering cache.                                                     |
| staticTemplate        | `{enable:boolean,removeSkeleton?:boolean,data?:Object}` |               | -        | Page template can render as static template based on data in configuration. |

## DarkMode

We provide developers the ability to incorporate Dark Mode in their applets.

### Enable DarkMode

To enable Dark Mode, set `{ "darkmode" : true }` in the `app.json` file. Once enabled, all basic
components will display different default styles based on the system theme. The navigation bar and
tab bar will automatically switch according to the following configuration.

### Related Configuration

When `{ "darkmode": true }` is set in app.json, certain applet configuration items can be set via
variables, enabling definition of colors or icons under different themes in the variable
configuration file as follows:

1. Configure `themeLocation` in `app.json`, specifying the path to the variable configuration file
   `theme.json`. For instance, to add `theme.json` in the root directory, configure
   `{"themeLocation": "/path/to/theme.json"}`
2. Define related variables in `theme.json`.
3. In `app.json`, reference variables that start with `@`.

Properties that support configuration through variables include:

1. The window property of the global configuration and the property under the page configuration
   - navigationBarBackgroundColor
   - navigationBarTextStyle
   - backgroundColor
   - backgroundTextStyle
   - backgroundColorTop
   - backgroundColorBottom

2. Global configuration properties of window.tabBar
   - color
   - selectedColor
   - backgroundColor
   - borderStyle
   - list
     - iconPath
     - selectedIconPath

### Variable configuration file theme.json

The `theme.json` file is used for variable definitions related to the color theme. Prioritize
setting the path to `theme.json` in `themeLocation`, as the variable configuration cannot be read
otherwise.

The configuration file must contain the following properties:

| Attribute | Type   | Required | Description                        |
| --------- | ------ | -------- | ---------------------------------- |
| light     | object | Yes      | Variables definition in light mode |
| dark      | object | Yes      | Variables definition in dark mode  |

Both light and dark modes can define variable names and values in the key: value format, as shown
below:

```js
{
  "light": {
    "navBgColor": "#f6f6f6",
    "navTxtStyle": "black"
  },
  "dark": {
    "navBgColor": "#191919",
    "navTxtStyle": "white"
  }
}
```

After the definition is completed, it can be referenced at the beginning of `@` in the relevant
properties of the `global configuration` or `page configuration`, for example:

```js
// global configuration
{
  "window": {
    "navigationBarBackgroundColor": "@navBgColor",
    "navigationBarTextStyle": "@navTxtStyle"
  }
}
// page configuration
{
  "navigationBarBackgroundColor": "@navBgColor",
  "navigationBarTextStyle": "@navTxtStyle"
}
```

### Configuration example

`app.json` (the example omits configuration items other than those related to the theme)

```js
{
    "window": {
        "navigationBarBackgroundColor": "@navBgColor",
        "navigationBarTextStyle": "@navTxtStyle",
        "backgroundColor": "@bgColor",
        "backgroundTextStyle": "@bgTxtStyle",
        "backgroundColorTop": "@bgColorTop",
        "backgroundColorBottom": "@bgColorBottom"
    },
    "tabBar": {
        "color": "@tabFontColor",
        "selectedColor": "@tabSelectedColor",
        "backgroundColor": "@tabBgColor",
        "borderStyle": "@tabBorderStyle",
        "list": [{
            "iconPath": "@iconPath1",
            "selectedIconPath": "@selectedIconPath1"
        }, {
            "iconPath": "@iconPath2",
            "selectedIconPath": "@selectedIconPath2"
        }]
    }
}
```

`theme.json`

```js
{
    "light": {
        "navBgColor": "#f6f6f6",
        "navTxtStyle": "black",
        "bgColor": "#ffffff",
        "bgTxtStyle": "light",
        "bgColorTop": "#eeeeee",
        "bgColorBottom": "#efefef",
        "tabFontColor": "#000000",
        "tabSelectedColor": "#3cc51f",
        "tabBgColor": "#ffffff",
        "tabBorderStyle": "black",
        "iconPath1": "image/icon1_light.png",
        "selectedIconPath1": "image/selected_icon1_light.png",
        "iconPath2": "image/icon2_light.png",
        "selectedIconPath2": "image/selected_icon2_light.png",
    },
    "dark": {
        "navBgColor": "#191919",
        "navTxtStyle": "white",
        "bgColor": "#1f1f1f",
        "bgTxtStyle": "dark",
        "bgColorTop": "#191919",
        "bgColorBottom": "#1f1f1f",
        "tabFontColor": "#ffffff",
        "tabSelectedColor": "#51a937",
        "tabBgColor": "#191919",
        "tabBorderStyle": "white",
        "iconPath1": "image/icon1_dark.png",
        "selectedIconPath1": "image/selected_icon1_dark.png",
        "iconPath2": "image/icon2_dark.png",
        "selectedIconPath2": "image/selected_icon2_dark.png",
    }
}

```

### Get the current system theme

If `"darkmode": true` is declared in `app.json`, the output of `bn.getSystemInfo` or
`bn.getSystemInfoSync` will include a theme attribute, the value of which can be either 'light' or
'dark'.

If `app.json` does not include the `"darkmode": true` declaration, the theme attribute is
inaccessible (meaning, 'theme' would be undefined).

### Listening for Theme Switching Events

There are two ways to monitor for theme switching:

1. In `App()`, insert the `onThemeChange` callback function. This callback will get triggered when
   the theme switches.
2. Utilize `bn.onThemeChange` to monitor for theme changes. You can cancel the monitoring using
   `bn.offThemeChange`.

### BXSS Adaptation

In `BXSS`, we support theme adaptation through the media query `prefers-color-scheme`. This approach
is consistent with the adaptation method used in Web. See the example below:

```css
/* normal css style begin */
.case-background {
  background: white;
}
.case-text {
  color: black;
}
/* normal css style end */

@media (prefers-color-scheme: dark) {
  /* style under DarkMode start */
  .case-background {
    background: #1b1b1b;
  }
  .case-text {
    color: #ffffff;
  }
  /* style under DarkMode end */
}
```