---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/about-mini-program
api_type: Guide
updated_at: 2026-11-19 18:32:03.119641
---

# About Mini Program

Positioned at the cutting edge of application technology, the Mini Program captures a new approach
to app creation. This document primarily delves into the contrasting facets of Mini Program
development relative to the traditional methodology of web projects. (Throughout this narrative, we
will utilize the acronym 'MP' to denote the Mini Program)

## Differentiating MP Development from Traditional Web Development

While the structure of MP development follows in the footsteps of web development—utilizing
JavaScript for creation, deploying CSS for styling, and eventually HTML for rendering—it introduces
a novel twist. The JavaScript code within MP operates in an autonomous environment named the "Logic
Layer", exclusive to each respective MP.

In conventional web development, the JavaScript and rendering threads within each page function in
separate domains. Conversely, within the MP, each JavaScript operating process and the rendering
process (view layer) enjoy autonomy—the rendering and updating of views doesn't deter the
simultaneous progression of JavaScript, and likewise, JavaScript's logic execution doesn't interfere
with the rendering and updates of the view. This foregrounds the primary point of focus:
JavaScript-driven view updates are inherently asynchronous, and JavaScript cannot directly access
the view's DOM.

![thread-model](/img/mini-program/mp-thread-model.png)

Web developers primarily engage with IE/Chrome/QQ browsers on PCs, and navigate Safari/Chrome
browsers and assorted WebViews on iOS or Android systems feature on mobile devices. In stark
contrast, MP developers work directly with Binance App on iOS, Android, and Binance DevTools.

## Experience the Mini Program Firsthand

Following the installation of the Binance app, you can access the mini-program by simply scanning
the provided QR code.

![qrcode](/img/mini-program/component-demo-public-qrcode.png)

---

# About Mini Program

Positioned at the cutting edge of application technology, the Mini Program captures a new approach
to app creation. This document primarily delves into the contrasting facets of Mini Program
development relative to the traditional methodology of web projects. (Throughout this narrative, we
will utilize the acronym 'MP' to denote the Mini Program)

## Differentiating MP Development from Traditional Web Development

While the structure of MP development follows in the footsteps of web development—utilizing
JavaScript for creation, deploying CSS for styling, and eventually HTML for rendering—it introduces
a novel twist. The JavaScript code within MP operates in an autonomous environment named the "Logic
Layer", exclusive to each respective MP.

In conventional web development, the JavaScript and rendering threads within each page function in
separate domains. Conversely, within the MP, each JavaScript operating process and the rendering
process (view layer) enjoy autonomy—the rendering and updating of views doesn't deter the
simultaneous progression of JavaScript, and likewise, JavaScript's logic execution doesn't interfere
with the rendering and updates of the view. This foregrounds the primary point of focus:
JavaScript-driven view updates are inherently asynchronous, and JavaScript cannot directly access
the view's DOM.

![thread-model](/img/mini-program/mp-thread-model.png)

Web developers primarily engage with IE/Chrome/QQ browsers on PCs, and navigate Safari/Chrome
browsers and assorted WebViews on iOS or Android systems feature on mobile devices. In stark
contrast, MP developers work directly with Binance App on iOS, Android, and Binance DevTools.

## Experience the Mini Program Firsthand

Following the installation of the Binance app, you can access the mini-program by simply scanning
the provided QR code.

![qrcode](/img/mini-program/component-demo-public-qrcode.png)