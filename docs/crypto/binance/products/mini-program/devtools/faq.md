---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/devtools/faq
api_type: Guide
updated_at: 2026-11-19 18:40:33.943234
---

# FAQ

For quick troubleshooting, we provide a detailed FAQ guide. You can browse it sequentially or use
specific keywords to perform a search.

For a simplified read, we've categorised the FAQs according to features: Simulator, Devtool Panels,
Upload, Network, Preview & Remote Debug, and Extension.

## Simulator

### Dark Mode `darkMode: false` is not working

At present, this feature is unsupported. You can verify it on the native side.

## Devtool Panels

### Excessive logs in console

For minimising console logs, follow these steps:

1. Go to the toolbar and select `Devtools -> openApp Devtool`.
2. Run script (`document.querySelectorAll('webview')[1].openDevTools()`) in the console panel.
3. Run script (`localStorage.setItem('devtool-debugger', '1')`) in the console panel.
4. Refresh window and run a test now 😄

A dedicated package will be released soon to fix this.

### BXML is empty

Upgrade your IDE to version 2.25.0 or later.

### Mocking API with different responses according to the parameters

1. Upgrade your IDE to version 2.26.0 or later.
2. Create multiple mock items each with different rules.

## Upload

### Encountered 400 error during upload

Click `details` and verify if the logo is displayed correctly. If not, ensure that your appid and
current environment are set correctly.

## Network

### Network requests failing

- Activate
  `Does not verify valid domain names, web-view (business domain names), TLS versions and HTTPS certificates`
  found in `Details - Local Settings`.

### Image component is blank

- Inspect the image node in BXML panel and confirm that the origin-src is correct. If not, review
  your code.

## Preview & Remote Debug

### Preview loading perpetually

Ensure your IDE version is 2.25.0 or above, then clear cache and try again.

### Preview error

Here is a list of common error codes, their causes, and remedies to assist developers in
troubleshooting quickly.

- `350002` means resource not found, please make sure you're using production package or change the
  env to be production if you're using development package. And make sure you app is in-house mode.
- `603301` means invalid (type invalid or cannot download, such as webp type image, not sure we have
  error code for this before)
- `603302` means image not found, please check the url of the image.
- `603501` means \_\_app.js is missing, please upgrade your IDE and try again.

---

# FAQ

For quick troubleshooting, we provide a detailed FAQ guide. You can browse it sequentially or use
specific keywords to perform a search.

For a simplified read, we've categorised the FAQs according to features: Simulator, Devtool Panels,
Upload, Network, Preview & Remote Debug, and Extension.

## Simulator

### Dark Mode `darkMode: false` is not working

At present, this feature is unsupported. You can verify it on the native side.

## Devtool Panels

### Excessive logs in console

For minimising console logs, follow these steps:

1. Go to the toolbar and select `Devtools -> openApp Devtool`.
2. Run script (`document.querySelectorAll('webview')[1].openDevTools()`) in the console panel.
3. Run script (`localStorage.setItem('devtool-debugger', '1')`) in the console panel.
4. Refresh window and run a test now 😄

A dedicated package will be released soon to fix this.

### BXML is empty

Upgrade your IDE to version 2.25.0 or later.

### Mocking API with different responses according to the parameters

1. Upgrade your IDE to version 2.26.0 or later.
2. Create multiple mock items each with different rules.

## Upload

### Encountered 400 error during upload

Click `details` and verify if the logo is displayed correctly. If not, ensure that your appid and
current environment are set correctly.

## Network

### Network requests failing

- Activate
  `Does not verify valid domain names, web-view (business domain names), TLS versions and HTTPS certificates`
  found in `Details - Local Settings`.

### Image component is blank

- Inspect the image node in BXML panel and confirm that the origin-src is correct. If not, review
  your code.

## Preview & Remote Debug

### Preview loading perpetually

Ensure your IDE version is 2.25.0 or above, then clear cache and try again.

### Preview error

Here is a list of common error codes, their causes, and remedies to assist developers in
troubleshooting quickly.

- `350002` means resource not found, please make sure you're using production package or change the
  env to be production if you're using development package. And make sure you app is in-house mode.
- `603301` means invalid (type invalid or cannot download, such as webp type image, not sure we have
  error code for this before)
- `603302` means image not found, please check the url of the image.
- `603501` means \_\_app.js is missing, please upgrade your IDE and try again.