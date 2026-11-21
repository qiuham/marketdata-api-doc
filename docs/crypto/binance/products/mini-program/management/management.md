---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/management/management
api_type: Guide
updated_at: 2026-11-21 18:37:14.481523
---

# Management Portal

import Mermaid from "../../../../components/Mermaid";

This document provides instructions on how to utilize the Mini Program Management Platform (MPP) for
managing your applications.

## Getting Started

Upon completing the code development, you will need to use MPP to publicize your mini program. MPP
oversees all the mini program apps that are published online, and it's only through upload, review,
and publication on MPP that users can access your mini program via the Binance App. The process of
utilizing MPP is depicted in the following figure:

<Mermaid
  value={`graph TD;
    A[Build your Mini Program] -->|bundle.zip| E(Upload to Management)
    E --> F(Set as Experience Version)
    E --> G(Submit for review)
    G -->|Pass review|H(Get the MP app on line)
    I(Register and login on Management) --> J(Create a new Mini Program App)
    J --> E
    H --> B(Shutdown the Mini Program)
    H --> C(Rollback to an old Version)
    H --> D(Access from Binance app)
    C --> D
    F --> D;`}
/>

## Logging In

You can access MPP at
[https://developers.binance.com/en/mpp](https://developers.binance.com/en/mpp), and use your Binance
Account credentials for login.

<code>
  Note: The platform is not currently accessible to the general public; a
  selected set of users can access the platform after thorough vetting.
</code>

## The Workspace

The Workspace is the developer's account. It can house many applications, each having its own
autonomous version and appId. A user can be associated with numerous Workspaces, with the ability to
choose their workspace via the drop-down menu.

![img](/img/mp-management/developer-account.png)

If a user is not a part of any Workspace, they will be redirected to the onboarding page to provide
business-related information. Subsequently, the Binance team will reach out to users through the
provided details to create their Workspace Account.

![img](/img/mp-management/onboarding.png)

## Applications

An application is the basic unit of Mini Program distribution. Each application comes with its
unique AppId, privileges, and version list.

### Creating Your Application

Owners or Editors in the Developer module can list or create an application.

![img](/img/mp-management/app-list.png)

### Modifying Application Settings

In the application's overview, you can view the details of the current app.

![img](/img/mp-management/app-info.png)

### Uploading a New Version

To publish a new application, we first need to create a bundle file using the CLI.

```bash
cd [path-to-your-project]
bmp build
```

It produces mini-program files in your directory, which can then be uploaded with Binance DevTools.

### Managing Application Versions

After uploading a new version, Version Management enables further administration. More information
can be found in [Mini Program Version Lifecycle](mini-program-version-lifecycle).

![img](/img/mp-management/app-version.png)

### Managing Application Development Settings

#### Service Domain and Business Domain

All the domains used in the mini program API, such as `request` and `websocket`, must be included in
the `Service Domain` list. Similarly, all the domains that can be accessed via the `<WebView />`
component should be listed under `Business Domain`.

![img](/img/mp-management/domain-configure.png)

## Accessing Your Application

Users can access live applications by employing the QRCode button in the Version Management panel.
For direct access to the Mini Program, users can scan the QRCode with the Binance App.

![img](/img/mp-management/app-experience-qrcode.png)

---

# Management Portal

import Mermaid from "../../../../components/Mermaid";

This document provides instructions on how to utilize the Mini Program Management Platform (MPP) for
managing your applications.

## Getting Started

Upon completing the code development, you will need to use MPP to publicize your mini program. MPP
oversees all the mini program apps that are published online, and it's only through upload, review,
and publication on MPP that users can access your mini program via the Binance App. The process of
utilizing MPP is depicted in the following figure:

<Mermaid
  value={`graph TD;
    A[Build your Mini Program] -->|bundle.zip| E(Upload to Management)
    E --> F(Set as Experience Version)
    E --> G(Submit for review)
    G -->|Pass review|H(Get the MP app on line)
    I(Register and login on Management) --> J(Create a new Mini Program App)
    J --> E
    H --> B(Shutdown the Mini Program)
    H --> C(Rollback to an old Version)
    H --> D(Access from Binance app)
    C --> D
    F --> D;`}
/>

## Logging In

You can access MPP at
[https://developers.binance.com/en/mpp](https://developers.binance.com/en/mpp), and use your Binance
Account credentials for login.

<code>
  Note: The platform is not currently accessible to the general public; a
  selected set of users can access the platform after thorough vetting.
</code>

## The Workspace

The Workspace is the developer's account. It can house many applications, each having its own
autonomous version and appId. A user can be associated with numerous Workspaces, with the ability to
choose their workspace via the drop-down menu.

![img](/img/mp-management/developer-account.png)

If a user is not a part of any Workspace, they will be redirected to the onboarding page to provide
business-related information. Subsequently, the Binance team will reach out to users through the
provided details to create their Workspace Account.

![img](/img/mp-management/onboarding.png)

## Applications

An application is the basic unit of Mini Program distribution. Each application comes with its
unique AppId, privileges, and version list.

### Creating Your Application

Owners or Editors in the Developer module can list or create an application.

![img](/img/mp-management/app-list.png)

### Modifying Application Settings

In the application's overview, you can view the details of the current app.

![img](/img/mp-management/app-info.png)

### Uploading a New Version

To publish a new application, we first need to create a bundle file using the CLI.

```bash
cd [path-to-your-project]
bmp build
```

It produces mini-program files in your directory, which can then be uploaded with Binance DevTools.

### Managing Application Versions

After uploading a new version, Version Management enables further administration. More information
can be found in [Mini Program Version Lifecycle](mini-program-version-lifecycle).

![img](/img/mp-management/app-version.png)

### Managing Application Development Settings

#### Service Domain and Business Domain

All the domains used in the mini program API, such as `request` and `websocket`, must be included in
the `Service Domain` list. Similarly, all the domains that can be accessed via the `<WebView />`
component should be listed under `Business Domain`.

![img](/img/mp-management/domain-configure.png)

## Accessing Your Application

Users can access live applications by employing the QRCode button in the Version Management panel.
For direct access to the Mini Program, users can scan the QRCode with the Binance App.

![img](/img/mp-management/app-experience-qrcode.png)