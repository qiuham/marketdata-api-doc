---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/management/gray-release
api_type: Guide
updated_at: 2026-11-19 18:39:45.735991
---

# Mini Progrram Gray Release

This document outlines the concept of Gray Release in the context of Mini-Programs.

Before you launch each new version of a mini program, you must select a release strategy. If it's
the program's first version, a full release is mandatory.

## Gray Release Policies

1. Full Release
2. Scale Release
3. Whitelist Release

### Full Release

A Full Release implies that the version will be launched outright.

### Scale Release

A Scale Release signifies that only a portion of users can access the new version; the rest will
access the prior version. For example, if developers opt for a 10% scale release, only 10% of users
(based on SDK compatibility) can access this new version.

Example:

| MV    | MSV           | Published Time |                    |
| ----- | ------------- | -------------- | ------------------ |
| 1.2.0 | ^1.0.0/^2.0.0 | 2020/10/20     | Full Release       |
| 1.2.1 | ^2.0.0        | 2020/10/21     | Full Release       |
| 1.2.2 | ^2.0.0        | 2020/10/22     | Gray Release (10%) |

| NV     | Binded SV   | Loaded MV               |
| ------ | ----------- | ----------------------- |
| 2.36.0 | 1.3.0       | `1.2.0`                 |
| 2.36.1 | 1.3.0/2.1.0 | 90% `1.2.1` 10% `1.2.2` |
| 2.36.2 | 2.1.0       | 90% `1.2.1` 10% `1.2.2` |

### Whitelist Release

A Whitelist Release is designed for granting specific users access. Developers can insert users'
device IDs onto the list to grant them access to the new version.

## Release Flow

Whitelist -> Gray Release -> Full Release

Once an audit version is approved, developers can set it up for a gray release.

![Image](/img/mp-management/release-option.png)

![Image](/img/mp-management/gray-release-setting.png)

After setting the gray release strategy, the version can now go live. If already released,
developers can adjust the release strategy.

![Image](/img/mp-management/set-gray-release.png)

Important Notes:

1. If a gray release is in progress, the rollback and new version publishing actions will be
   blocked.
2. Developers can deprecate a gray release version if any issues are found post-release.

## Frequently Asked Questions

1. Can I have multiple versions in gray release status at the same time?

   No, only one version can be in gray release status at a time (either scale release or whitelist
   release).

---

# Mini Progrram Gray Release

This document outlines the concept of Gray Release in the context of Mini-Programs.

Before you launch each new version of a mini program, you must select a release strategy. If it's
the program's first version, a full release is mandatory.

## Gray Release Policies

1. Full Release
2. Scale Release
3. Whitelist Release

### Full Release

A Full Release implies that the version will be launched outright.

### Scale Release

A Scale Release signifies that only a portion of users can access the new version; the rest will
access the prior version. For example, if developers opt for a 10% scale release, only 10% of users
(based on SDK compatibility) can access this new version.

Example:

| MV    | MSV           | Published Time |                    |
| ----- | ------------- | -------------- | ------------------ |
| 1.2.0 | ^1.0.0/^2.0.0 | 2020/10/20     | Full Release       |
| 1.2.1 | ^2.0.0        | 2020/10/21     | Full Release       |
| 1.2.2 | ^2.0.0        | 2020/10/22     | Gray Release (10%) |

| NV     | Binded SV   | Loaded MV               |
| ------ | ----------- | ----------------------- |
| 2.36.0 | 1.3.0       | `1.2.0`                 |
| 2.36.1 | 1.3.0/2.1.0 | 90% `1.2.1` 10% `1.2.2` |
| 2.36.2 | 2.1.0       | 90% `1.2.1` 10% `1.2.2` |

### Whitelist Release

A Whitelist Release is designed for granting specific users access. Developers can insert users'
device IDs onto the list to grant them access to the new version.

## Release Flow

Whitelist -> Gray Release -> Full Release

Once an audit version is approved, developers can set it up for a gray release.

![Image](/img/mp-management/release-option.png)

![Image](/img/mp-management/gray-release-setting.png)

After setting the gray release strategy, the version can now go live. If already released,
developers can adjust the release strategy.

![Image](/img/mp-management/set-gray-release.png)

Important Notes:

1. If a gray release is in progress, the rollback and new version publishing actions will be
   blocked.
2. Developers can deprecate a gray release version if any issues are found post-release.

## Frequently Asked Questions

1. Can I have multiple versions in gray release status at the same time?

   No, only one version can be in gray release status at a time (either scale release or whitelist
   release).