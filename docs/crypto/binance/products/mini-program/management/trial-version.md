---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/management/trial-version
api_type: Guide
updated_at: 2026-11-19 18:39:39.553999
---

# How To Set A Trial Version

In this guide, we introduce two methods to validate your mini program version on real devices.

## 1. Setting the Preview Version on Devtools

While developing your mini program in Devtools, you may want to verify its behavior on real devices.
You can do this by clicking the "Preview" button, which generates a QR code. Scanning this QR code
allows you to experience this version in real-time.

![Image](/img/mp-management/set-preview-version.png)

> Note: Only the developer who generated the QR code will have access to the preview version. As of
> Devtools version 2.17.0 (and beyond) and Binance app version 2.48.0 (and later), the preview QR
> code no longer has any access control for a 15-minute validity period.

## 2. Accessing an Experience Version on the Mini Program Platform

### Uploading a Version to the Mini Program Platform

### Obtaining an Experience QR Code

![Image](/img/mp-management/get-experience-qrcode.png)

### Selecting the Host App and Generating a QR Code

![Image](/img/mp-management/create-qrcode.png)

### Adding Experience Members

Share the QR code with others, and they can scan it using their Binance app. This QR code remains
valid for 7 days.

Different version QR codes function independently, effective from Binance app 2.48.0 onwards.
Developers can test multiple versions simultaneously. If the app version is less than 2.48.0, all QR
codes will be redirected to the latest created QR code version.

If developers wish to access the experience version QR code, they need to be added to the experience
member list.

![Image](/img/mp-management/set-experience-member.png)

Developers can add either a user ID or a device ID to the whitelist. The user ID refers to the
Binance user ID, and they can find their device ID within their app via: Settings > About > Device
ID.

![Image](/img/mp-management/experience-member.png)

---

# How To Set A Trial Version

In this guide, we introduce two methods to validate your mini program version on real devices.

## 1. Setting the Preview Version on Devtools

While developing your mini program in Devtools, you may want to verify its behavior on real devices.
You can do this by clicking the "Preview" button, which generates a QR code. Scanning this QR code
allows you to experience this version in real-time.

![Image](/img/mp-management/set-preview-version.png)

> Note: Only the developer who generated the QR code will have access to the preview version. As of
> Devtools version 2.17.0 (and beyond) and Binance app version 2.48.0 (and later), the preview QR
> code no longer has any access control for a 15-minute validity period.

## 2. Accessing an Experience Version on the Mini Program Platform

### Uploading a Version to the Mini Program Platform

### Obtaining an Experience QR Code

![Image](/img/mp-management/get-experience-qrcode.png)

### Selecting the Host App and Generating a QR Code

![Image](/img/mp-management/create-qrcode.png)

### Adding Experience Members

Share the QR code with others, and they can scan it using their Binance app. This QR code remains
valid for 7 days.

Different version QR codes function independently, effective from Binance app 2.48.0 onwards.
Developers can test multiple versions simultaneously. If the app version is less than 2.48.0, all QR
codes will be redirected to the latest created QR code version.

If developers wish to access the experience version QR code, they need to be added to the experience
member list.

![Image](/img/mp-management/set-experience-member.png)

Developers can add either a user ID or a device ID to the whitelist. The user ID refers to the
Binance user ID, and they can find their device ID within their app via: Settings > About > Device
ID.

![Image](/img/mp-management/experience-member.png)