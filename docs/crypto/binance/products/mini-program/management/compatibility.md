---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/management/compatibility
api_type: Guide
updated_at: 2026-11-28 18:36:39.933877
---

# Multiple Versions Compatible Solution

#### Abbreviations

- MV -> Mini-Program APP version
- MSV -> Required minimum SDK version
- SV -> SDK version
- NV -> Binance APP version

## Introduction

This document presents a solution to manage compatibility across multiple versions. The Mini-Program
APP version (MV) will be loaded based on the binding relationship between the SDK version (SV) and
the Binance App version (NV). This compatibility solution is applicable from Binance APP version
2.36.0 onwards.

## Why the Need for a Multiple Version Solution?

The native Binance APP always loads the latest version of the Mini-Program APP. However, it's not
feasible to load different Mini-Program APP versions for various Binance APP versions. Thus, the
need for a multiple version solution.

## SDK Compatibility

SDKs with the same major version offer backward compatibility.

## Which Mini-Program APP Version will be Loaded on Binance APP?

Based on the binding relationship between SDK versions and Binance APP versions, the latest
published Mini-Program version will be loaded. Its Minimum SDK Version (MSV) will correspond to the
major SDK version bound to the Binance App.

Example:

| MV    | MSV           | Published Time |
| ----- | ------------- | -------------- |
| 1.2.0 | ^1.0.0/^2.0.0 | 2020/10/20     |
| 1.2.1 | ^2.0.0        | 2020/10/21     |

| NV     | Binded SV   | Loaded MV |
| ------ | ----------- | --------- |
| 2.36.0 | 1.3.0       | `1.2.0`   |
| 2.36.1 | 1.3.0/2.1.0 | `1.2.1`   |
| 2.36.2 | 2.1.0       | `1.2.1`   |

---

# Multiple Versions Compatible Solution

#### Abbreviations

- MV -> Mini-Program APP version
- MSV -> Required minimum SDK version
- SV -> SDK version
- NV -> Binance APP version

## Introduction

This document presents a solution to manage compatibility across multiple versions. The Mini-Program
APP version (MV) will be loaded based on the binding relationship between the SDK version (SV) and
the Binance App version (NV). This compatibility solution is applicable from Binance APP version
2.36.0 onwards.

## Why the Need for a Multiple Version Solution?

The native Binance APP always loads the latest version of the Mini-Program APP. However, it's not
feasible to load different Mini-Program APP versions for various Binance APP versions. Thus, the
need for a multiple version solution.

## SDK Compatibility

SDKs with the same major version offer backward compatibility.

## Which Mini-Program APP Version will be Loaded on Binance APP?

Based on the binding relationship between SDK versions and Binance APP versions, the latest
published Mini-Program version will be loaded. Its Minimum SDK Version (MSV) will correspond to the
major SDK version bound to the Binance App.

Example:

| MV    | MSV           | Published Time |
| ----- | ------------- | -------------- |
| 1.2.0 | ^1.0.0/^2.0.0 | 2020/10/20     |
| 1.2.1 | ^2.0.0        | 2020/10/21     |

| NV     | Binded SV   | Loaded MV |
| ------ | ----------- | --------- |
| 2.36.0 | 1.3.0       | `1.2.0`   |
| 2.36.1 | 1.3.0/2.1.0 | `1.2.1`   |
| 2.36.2 | 2.1.0       | `1.2.1`   |