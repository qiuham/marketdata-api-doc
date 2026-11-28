---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/management/mini-program-version-lifecycle
api_type: Guide
updated_at: 2026-11-28 18:36:34.461616
---

# Mini Program Version Lifecycle

A Mini Program Version progresses through several statuses.

## Develop Status

When a mini program version is uploaded from Devtool, it appears on the Develop table, which keeps
track of all historical versions.

![[Development table image](/img/mp-management/version-develop-table.png)

At this juncture, developers can access this version by scanning a QR code for
[experience version](trial-version#2-access-to-an-experience-version-on-mini-program-platform).

## Audit Status

Upon submitting a mini program version for review from the Develop status, the version transitions
to the Audit status. It now awaits review from the mini program platform team. Note that only one
version can be at the Audit status based on the same Mini Service Version (MSV).

![Audit review image](/img/mp-management/version-audit-review.png)

## Approval Status

Once a mini program version is approved, developers are able to set a
[gray release strategy](gray-release) and proceed to launch.

![Release option image](/img/mp-management/release-option.png)

## Gray Release Online Status

Upon going live, users who meet the criteria of the gray release strategy can access this version.
Developers can also modify the gray release strategy. If issues are found with this version, it can
be deprecated.

![Set gray release image](/img/mp-management/set-gray-release.png)

## Online Full Release Status

When a version achieves full release, it becomes accessible to all users. At this stage, developers
can either rollback to a previous version based on MSV or deprecate the entire series of versions
based on MSV.

![Version online image](/img/mp-management/version-online.png)

---

# Mini Program Version Lifecycle

A Mini Program Version progresses through several statuses.

## Develop Status

When a mini program version is uploaded from Devtool, it appears on the Develop table, which keeps
track of all historical versions.

![[Development table image](/img/mp-management/version-develop-table.png)

At this juncture, developers can access this version by scanning a QR code for
[experience version](trial-version#2-access-to-an-experience-version-on-mini-program-platform).

## Audit Status

Upon submitting a mini program version for review from the Develop status, the version transitions
to the Audit status. It now awaits review from the mini program platform team. Note that only one
version can be at the Audit status based on the same Mini Service Version (MSV).

![Audit review image](/img/mp-management/version-audit-review.png)

## Approval Status

Once a mini program version is approved, developers are able to set a
[gray release strategy](gray-release) and proceed to launch.

![Release option image](/img/mp-management/release-option.png)

## Gray Release Online Status

Upon going live, users who meet the criteria of the gray release strategy can access this version.
Developers can also modify the gray release strategy. If issues are found with this version, it can
be deprecated.

![Set gray release image](/img/mp-management/set-gray-release.png)

## Online Full Release Status

When a version achieves full release, it becomes accessible to all users. At this stage, developers
can either rollback to a previous version based on MSV or deprecate the entire series of versions
based on MSV.

![Version online image](/img/mp-management/version-online.png)