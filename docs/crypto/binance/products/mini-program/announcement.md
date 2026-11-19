---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/announcement
api_type: Guide
updated_at: 2026-11-19 18:32:01.381273
---

# Announcement

## Mini Program Crucial Update

### Notice: Termination of Support for JS SDK <4.0

> Announcement Date: November 21, 2022

We hereby announce the cessation of support for JS SDK <4.0. Immediate action necessary: Upgrade
your JS SDK to ^4.x or later versions and confirm that your Mini Program functions seamlessly with
the most recent version of Native with SDK ^4.x.

For any assistance required, our team is readily available.

#### End Of Life (EOL) Notice

Our Mini Program hereby discontinues its support for the following JS SDK versions marking their End
of Life (EOL):

| Most Recent Supported Native Version | Correlated JS SDK Version | EOL Status           |
| ------------------------------------ | ------------------------- | -------------------- |
| 2.35                                 | JS SDK ^1.x               | Ended on 2021-09-09  |
| 2.46                                 | JS SDK ^2.x               | Ended on 2022-05-19  |
| 2.58                                 | JS SDK ^3.x               | Ending on 2022-12-22 |
|                                      | JS SDK ^4.x               | Continues LTS ⭐️     |

#### Key Notes on Breaking Changes

##### Deprecation of Template Tags `<style>` and `<br>`

Refrain from using `<style>` and `<br>` tags and instead, opt for CSS files.

🙅Discouraged Practice:

Implementing inline `<style>`

```jsx
<View className="index">
  <style
    dangerouslySetInnerHTML={{
      __html: `
      .index {
        background: #333;
      }
   `,
    }}
  />
  <View className="index-hd"></View>
</View>
```

Incorporating inline `<br>`

```jsx
<View className="title">
  Mini Program <br />
  Component Demos
</View>
```

##### Image Component Changes

Replacement element styles like `object-fit` have ceased to function. Kindly employ other styles or
prop modes as replacement.

The size of Image will not be auto-adjusted to the image size when both width and height are set to
`auto`.

The image event detail source `event.detail.src` has been removed.

🙅Incorrect Usage:

Employing `object-fit` style

```jsx
<Image className="image" src={imageSrc} />
```

```scss
.image {
  object-fit: cover; // 🙅 This style has been deprecated for img only
}
```

✅Correct Usage:

Implementing `mode`

```jsx
<Image mode="scaleToFill" src={imageSrc} /> // ✅ Recommended to use `mode`
```

##### Modifications to Text Component

The Text component confines its nesting to Text component only. Other components will now be
disabled within the Text component.

🙅Avoid:

Using `<View>` within `<Text>`

```jsx
<Text>
  <View>Mini Program</View>
  <View>Component Demos</View>
</Text>
```

✅Preferred:

Implement `<Text>` within `<Text>`

```jsx
<Text>
  <Text>Mini Program</Text>
  <Text>Component Demos</Text>
</Text>
```

##### Eviction of Deprecated Legacy Code

- The API `bn.twoFa` has been terminated.
- The global `env` has been abandoned, please use API `bn.env` as the alternate.
- The `entryPage` attribute from `app.json` has been scrapped, please use `entryPagePath` as its
  substitution.
- The error element `error._code` has been cancelled, use `error.errno` instead.
- **canIUseCustom**: Options of string type like `'myaction'` have been tossed out, please adopt
  `{ action: 'myaction' }` instead.
- **showModal**: The `response.status` has been revoked, prefer `response.confirm`/`response.cancel`
  instead.
- **request**: The function `response.json()` has been omitted, set `options.dataType` to `'json'`
  and use `response.data` instead.
- **request**: The `response.text()` has been deserted, opt to use `response.data` instead.
- **request**: The thenable return is no longer available, use `options.success`/`options.fail` as a
  substitute.

To attune to the new SDK ^4, consider re-uploading your MiniProgram project with

- CLI v2.4.22 by running `$ npm install -g @binance/mp-cli`
- And by selecting `MSV^4.0.2` on IDE v2.22.0.

### Announcement: End of support for JS SDK <3.0

> Date of announcement: 2022-03-10

Announcing the end of support for JS SDK <3.0. Action required: You need to upgrade to JS SDK ^3.x
or later and make sure your Mini Program can run on the latest version of Native with SDK ^3.x.

If you need any assistance, feel free to contact us.

#### EOL

Starting May 19th 2022, the Mini Program will no longer support the following end of life (EOL) JS
SDK versions:

| Last supported Native version | JS SDK version | EOL               |
| ----------------------------- | -------------- | ----------------- |
| 2.35                          | JS SDK ^1.x    | EOL on 2021-09-09 |
| 2.46                          | JS SDK ^2.x    | EOL on 2022-05-19 |
|                               | JS SDK ^3.x    | Active LTS ✅     |

#### Release notes

The release note for each release. Please also check [Release Note](/docs/mini-program/release-note)
for more details.

| JS SDK Version              | Release note                                                                  |
| --------------------------- | ----------------------------------------------------------------------------- |
| 2.2.0 -> 3.0.0              | [3.0.0 (2021-11-18)](/docs/products/mini-program/release-note#300-2021-11-18) |
| 3.0.0 -> 3.1.0              | [3.1.0 (2021-12-09)](/docs/products/mini-program/release-note#310-2021-12-09) |
| 3.1.0 -> 3.2.4              | [3.2.4 (2021-12-30)](/docs/products/mini-program/release-note#324-2021-12-30) |
| 3.2.4 -> 3.3.0              | [3.3.0 (2022-01-20)](/docs/products/mini-program/release-note#330-2022-01-20) |
| 3.3.0 -> 3.4.2 (rollbacked) | [3.4.0 (2022-02-17)](/docs/products/mini-program/release-note#340-2022-02-17) |
| 3.4.2 -> 3.5.0              | [3.5.0 (2022-03-10)](/docs/products/mini-program/release-note#350-2022-03-10) |

#### Breaking changes Summary

##### Image component

Now default size of Image is `width: 320px; height: 240px;`

```diff
// Image Component size
+ width: 320px;
+ height: 240px;
```

##### Deprecated legacy code removed

- Component `DeprecatedInput` removed, please use `Input` component instead.
- Component `DeprecatedTextarea` removed, please use `Textarea` component instead.

```diff
import {
- DeprecatedInput,
- DeprecatedTextarea,
  Input,
  Textarea,
} from '@binance/mp-components'
```

- API `bn.getCurrentPages` removed, please use global `getCurrentPages` function instead.
- API `bn.getApp` removed, please use global `getApp` function instead.
- API `bn.getTabBar` removed.
- **requestPayment**: `options.noncestr` removed, please use `options.nonceStr` instead.
- **request**: `options.body` removed, please use `options.data` instead.
- **request**: `options.headers` removed, please use `options.header` instead.
- **connectSocket**: `options.headers` removed, please use `options.header` instead.
- **SocketTask**: callback payload of `onOpen` changed:

```diff
socketTask.onOpen({
- headers,
+ header
} => {})
```

To use the new SDK ^3, please re-upload MiniProgram with

- CLI v2.1.3 `$ npm install -g @binance/mp-cli`
- IDE v2.12.0 and select `MSV^3.2.0` on IDE

## Crucial Update to the Mini Program

### Notice: Termination of Support for JS SDK <3.0

> Bulletin Date: March 10, 2022

We hereby announce the discontinuation of support for JS SDK <3.0. Immediate Action Required: You
must upgrade to JS SDK ^3.x or newer and ensure that your Mini Program is compatible with the latest
version of Native featuring SDK ^3.x.

For any assistance required, feel free to get in touch.

#### End Of Life (EOL) Notice

Effective from May 19th, 2022, our Mini Program will cease supporting the following JS SDK versions:

| Latterly Supported Native Version | Correlated JS SDK Version | EOL Status       |
| --------------------------------- | ------------------------- | ---------------- |
| 2.35                              | JS SDK ^1.x               | Ended 2021-09-09 |
| 2.46                              | JS SDK ^2.x               | Ended 2022-05-19 |
|                                   | JS SDK ^3.x               | Active LTS ⭐️    |

#### Release Notes Insight

We document focus points of each release in our Release Notes. To capture meticulous updates, please
explore our [Release Note](/docs/products/mini-program/release-note).

| Transitional JS SDK Versions | Complementary Release Notes                                                   |
| ---------------------------- | ----------------------------------------------------------------------------- |
| 2.2.0 -> 3.0.0               | [3.0.0 (2021-11-18)](/docs/products/mini-program/release-note#300-2021-11-18) |
| 3.0.0 -> 3.1.0               | [3.1.0 (2021-12-09)](/docs/products/mini-program/release-note#310-2021-12-09) |
| 3.1.0 -> 3.2.4               | [3.2.4 (2021-12-30)](/docs/products/mini-program/release-note#324-2021-12-30) |
| 3.2.4 -> 3.3.0               | [3.3.0 (2022-01-20)](/docs/products/mini-program/release-note#330-2022-01-20) |
| 3.3.0 -> 3.4.2 (Rolled back) | [3.4.0 (2022-02-17)](/docs/products/mini-program/release-note#340-2022-02-17) |
| 3.4.2 -> 3.5.0               | [3.5.0 (2022-03-10)](/docs/products/mini-program/release-note#350-2022-03-10) |

#### Crucial Notes on Breaking Changes

##### Image Component Alterations

The current default Image measurements are `width: 320px; height: 240px;`

```diff
// Adjustment to Image Component Size
+ width: 320px;
+ height: 240px;
```

##### Expunction of Deprecated Legacy Code

- The `DeprecatedInput` component has been discarded. Please utilize the `Input` component as its
  replacement.
- The `DeprecatedTextarea` Component has been removed. You are advised to rely on the updated
  `Textarea` component.

```diff
import {
- DeprecatedInput,
- DeprecatedTextarea,
  Input,
  Textarea,
} from '@binance/mp-components'
```

- The `bn.getCurrentPages` API has been eliminated. Please use the global function `getCurrentPages`
  as its replacement.
- The `bn.getApp` API has been discarded. Please resort to the global function `getApp` as an
  alternate.
- The `bn.getTabBar` API has been dismissed.
- **requestPayment**: `options.noncestr` has been discarded. Please resort to `options.nonceStr` as
  its replacement.
- **request**: `options.body` has been terminated. Please adopt `options.data` as its replacement.
- **request**: `options.headers` has been eliminated. Please resort to `options.header` for its
  replacement.
- **connectSocket**: `options.headers` has been discarded. Please resort to `options.header` as an
  alternate.
- **SocketTask**: The callback payload of `onOpen` has been altered:

```diff
socketTask.onOpen({
- headers,
+ header
} => {})
```

To transition smoothly to the new SDK ^3, please follow these steps:

- Adopt CLI v2.1.3 by executing `$ npm install -g @binance/mp-cli`
- Choose `MSV^3.2.0` on IDE v2.12.0.

---

# Announcement

## Mini Program Crucial Update

### Notice: Termination of Support for JS SDK <4.0

> Announcement Date: November 21, 2022

We hereby announce the cessation of support for JS SDK <4.0. Immediate action necessary: Upgrade
your JS SDK to ^4.x or later versions and confirm that your Mini Program functions seamlessly with
the most recent version of Native with SDK ^4.x.

For any assistance required, our team is readily available.

#### End Of Life (EOL) Notice

Our Mini Program hereby discontinues its support for the following JS SDK versions marking their End
of Life (EOL):

| Most Recent Supported Native Version | Correlated JS SDK Version | EOL Status           |
| ------------------------------------ | ------------------------- | -------------------- |
| 2.35                                 | JS SDK ^1.x               | Ended on 2021-09-09  |
| 2.46                                 | JS SDK ^2.x               | Ended on 2022-05-19  |
| 2.58                                 | JS SDK ^3.x               | Ending on 2022-12-22 |
|                                      | JS SDK ^4.x               | Continues LTS ⭐️     |

#### Key Notes on Breaking Changes

##### Deprecation of Template Tags `<style>` and `<br>`

Refrain from using `<style>` and `<br>` tags and instead, opt for CSS files.

🙅Discouraged Practice:

Implementing inline `<style>`

```jsx
<View className="index">
  <style
    dangerouslySetInnerHTML={{
      __html: `
      .index {
        background: #333;
      }
   `,
    }}
  />
  <View className="index-hd"></View>
</View>
```

Incorporating inline `<br>`

```jsx
<View className="title">
  Mini Program <br />
  Component Demos
</View>
```

##### Image Component Changes

Replacement element styles like `object-fit` have ceased to function. Kindly employ other styles or
prop modes as replacement.

The size of Image will not be auto-adjusted to the image size when both width and height are set to
`auto`.

The image event detail source `event.detail.src` has been removed.

🙅Incorrect Usage:

Employing `object-fit` style

```jsx
<Image className="image" src={imageSrc} />
```

```scss
.image {
  object-fit: cover; // 🙅 This style has been deprecated for img only
}
```

✅Correct Usage:

Implementing `mode`

```jsx
<Image mode="scaleToFill" src={imageSrc} /> // ✅ Recommended to use `mode`
```

##### Modifications to Text Component

The Text component confines its nesting to Text component only. Other components will now be
disabled within the Text component.

🙅Avoid:

Using `<View>` within `<Text>`

```jsx
<Text>
  <View>Mini Program</View>
  <View>Component Demos</View>
</Text>
```

✅Preferred:

Implement `<Text>` within `<Text>`

```jsx
<Text>
  <Text>Mini Program</Text>
  <Text>Component Demos</Text>
</Text>
```

##### Eviction of Deprecated Legacy Code

- The API `bn.twoFa` has been terminated.
- The global `env` has been abandoned, please use API `bn.env` as the alternate.
- The `entryPage` attribute from `app.json` has been scrapped, please use `entryPagePath` as its
  substitution.
- The error element `error._code` has been cancelled, use `error.errno` instead.
- **canIUseCustom**: Options of string type like `'myaction'` have been tossed out, please adopt
  `{ action: 'myaction' }` instead.
- **showModal**: The `response.status` has been revoked, prefer `response.confirm`/`response.cancel`
  instead.
- **request**: The function `response.json()` has been omitted, set `options.dataType` to `'json'`
  and use `response.data` instead.
- **request**: The `response.text()` has been deserted, opt to use `response.data` instead.
- **request**: The thenable return is no longer available, use `options.success`/`options.fail` as a
  substitute.

To attune to the new SDK ^4, consider re-uploading your MiniProgram project with

- CLI v2.4.22 by running `$ npm install -g @binance/mp-cli`
- And by selecting `MSV^4.0.2` on IDE v2.22.0.

### Announcement: End of support for JS SDK <3.0

> Date of announcement: 2022-03-10

Announcing the end of support for JS SDK <3.0. Action required: You need to upgrade to JS SDK ^3.x
or later and make sure your Mini Program can run on the latest version of Native with SDK ^3.x.

If you need any assistance, feel free to contact us.

#### EOL

Starting May 19th 2022, the Mini Program will no longer support the following end of life (EOL) JS
SDK versions:

| Last supported Native version | JS SDK version | EOL               |
| ----------------------------- | -------------- | ----------------- |
| 2.35                          | JS SDK ^1.x    | EOL on 2021-09-09 |
| 2.46                          | JS SDK ^2.x    | EOL on 2022-05-19 |
|                               | JS SDK ^3.x    | Active LTS ✅     |

#### Release notes

The release note for each release. Please also check [Release Note](/docs/mini-program/release-note)
for more details.

| JS SDK Version              | Release note                                                                  |
| --------------------------- | ----------------------------------------------------------------------------- |
| 2.2.0 -> 3.0.0              | [3.0.0 (2021-11-18)](/docs/products/mini-program/release-note#300-2021-11-18) |
| 3.0.0 -> 3.1.0              | [3.1.0 (2021-12-09)](/docs/products/mini-program/release-note#310-2021-12-09) |
| 3.1.0 -> 3.2.4              | [3.2.4 (2021-12-30)](/docs/products/mini-program/release-note#324-2021-12-30) |
| 3.2.4 -> 3.3.0              | [3.3.0 (2022-01-20)](/docs/products/mini-program/release-note#330-2022-01-20) |
| 3.3.0 -> 3.4.2 (rollbacked) | [3.4.0 (2022-02-17)](/docs/products/mini-program/release-note#340-2022-02-17) |
| 3.4.2 -> 3.5.0              | [3.5.0 (2022-03-10)](/docs/products/mini-program/release-note#350-2022-03-10) |

#### Breaking changes Summary

##### Image component

Now default size of Image is `width: 320px; height: 240px;`

```diff
// Image Component size
+ width: 320px;
+ height: 240px;
```

##### Deprecated legacy code removed

- Component `DeprecatedInput` removed, please use `Input` component instead.
- Component `DeprecatedTextarea` removed, please use `Textarea` component instead.

```diff
import {
- DeprecatedInput,
- DeprecatedTextarea,
  Input,
  Textarea,
} from '@binance/mp-components'
```

- API `bn.getCurrentPages` removed, please use global `getCurrentPages` function instead.
- API `bn.getApp` removed, please use global `getApp` function instead.
- API `bn.getTabBar` removed.
- **requestPayment**: `options.noncestr` removed, please use `options.nonceStr` instead.
- **request**: `options.body` removed, please use `options.data` instead.
- **request**: `options.headers` removed, please use `options.header` instead.
- **connectSocket**: `options.headers` removed, please use `options.header` instead.
- **SocketTask**: callback payload of `onOpen` changed:

```diff
socketTask.onOpen({
- headers,
+ header
} => {})
```

To use the new SDK ^3, please re-upload MiniProgram with

- CLI v2.1.3 `$ npm install -g @binance/mp-cli`
- IDE v2.12.0 and select `MSV^3.2.0` on IDE

## Crucial Update to the Mini Program

### Notice: Termination of Support for JS SDK <3.0

> Bulletin Date: March 10, 2022

We hereby announce the discontinuation of support for JS SDK <3.0. Immediate Action Required: You
must upgrade to JS SDK ^3.x or newer and ensure that your Mini Program is compatible with the latest
version of Native featuring SDK ^3.x.

For any assistance required, feel free to get in touch.

#### End Of Life (EOL) Notice

Effective from May 19th, 2022, our Mini Program will cease supporting the following JS SDK versions:

| Latterly Supported Native Version | Correlated JS SDK Version | EOL Status       |
| --------------------------------- | ------------------------- | ---------------- |
| 2.35                              | JS SDK ^1.x               | Ended 2021-09-09 |
| 2.46                              | JS SDK ^2.x               | Ended 2022-05-19 |
|                                   | JS SDK ^3.x               | Active LTS ⭐️    |

#### Release Notes Insight

We document focus points of each release in our Release Notes. To capture meticulous updates, please
explore our [Release Note](/docs/products/mini-program/release-note).

| Transitional JS SDK Versions | Complementary Release Notes                                                   |
| ---------------------------- | ----------------------------------------------------------------------------- |
| 2.2.0 -> 3.0.0               | [3.0.0 (2021-11-18)](/docs/products/mini-program/release-note#300-2021-11-18) |
| 3.0.0 -> 3.1.0               | [3.1.0 (2021-12-09)](/docs/products/mini-program/release-note#310-2021-12-09) |
| 3.1.0 -> 3.2.4               | [3.2.4 (2021-12-30)](/docs/products/mini-program/release-note#324-2021-12-30) |
| 3.2.4 -> 3.3.0               | [3.3.0 (2022-01-20)](/docs/products/mini-program/release-note#330-2022-01-20) |
| 3.3.0 -> 3.4.2 (Rolled back) | [3.4.0 (2022-02-17)](/docs/products/mini-program/release-note#340-2022-02-17) |
| 3.4.2 -> 3.5.0               | [3.5.0 (2022-03-10)](/docs/products/mini-program/release-note#350-2022-03-10) |

#### Crucial Notes on Breaking Changes

##### Image Component Alterations

The current default Image measurements are `width: 320px; height: 240px;`

```diff
// Adjustment to Image Component Size
+ width: 320px;
+ height: 240px;
```

##### Expunction of Deprecated Legacy Code

- The `DeprecatedInput` component has been discarded. Please utilize the `Input` component as its
  replacement.
- The `DeprecatedTextarea` Component has been removed. You are advised to rely on the updated
  `Textarea` component.

```diff
import {
- DeprecatedInput,
- DeprecatedTextarea,
  Input,
  Textarea,
} from '@binance/mp-components'
```

- The `bn.getCurrentPages` API has been eliminated. Please use the global function `getCurrentPages`
  as its replacement.
- The `bn.getApp` API has been discarded. Please resort to the global function `getApp` as an
  alternate.
- The `bn.getTabBar` API has been dismissed.
- **requestPayment**: `options.noncestr` has been discarded. Please resort to `options.nonceStr` as
  its replacement.
- **request**: `options.body` has been terminated. Please adopt `options.data` as its replacement.
- **request**: `options.headers` has been eliminated. Please resort to `options.header` for its
  replacement.
- **connectSocket**: `options.headers` has been discarded. Please resort to `options.header` as an
  alternate.
- **SocketTask**: The callback payload of `onOpen` has been altered:

```diff
socketTask.onOpen({
- headers,
+ header
} => {})
```

To transition smoothly to the new SDK ^3, please follow these steps:

- Adopt CLI v2.1.3 by executing `$ npm install -g @binance/mp-cli`
- Choose `MSV^3.2.0` on IDE v2.12.0.