---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/devtools/remote-debug
api_type: Guide
updated_at: 2026-11-20 18:39:41.594551
---

# Remote Debug

Developers can inspect logs and elements from the native IDE using remote debug.

## Environment

- native version >= 2.53.0
- sdk version >= 3.14.0

## Other Requirements

- ‼️ Your mobile device should be on the same local network as your computer.

- ‼️ Scan the QR code with the same Binance account that your IDE is logged into.

## How to Use

1. Click the Remote Debug Button located at the top of the IDE.

![remote-debug-icon](https://bin.bnbstatic.com/image/julia/docs/mp-ide/remote-debug/remote-debug-icon.png)

> You must be logged in before proceeding with this step.

2. Scan the QR code generated in the previous step.

![remote-debug-qrcode](https://bin.bnbstatic.com/image/julia/docs/mp-ide/remote-debug/remote-debug-qrcode.png)

3. A panel will appear after scanning the QR code.

![remote-debug-panel](https://bin.bnbstatic.com/image/julia/docs/mp-ide/remote-debug/remote-debug-panel.png)

4. You can perform various operations, inspect logs, and view elements using this panel. In the
   debugger for remote debugging, you can debug code in the Console panel, view the source code of a
   Mini Program, and perform breakpoint or single-step debugging in the Sources panel.

You can execute `bn` related functions within it.

![img](https://bin.bnbstatic.com/image/julia/docs/mini-program/remote-debug-bn.png)

5. The page will automatically refresh when any code changes. If you prefer it not to, you can click
   the off button.

![remote-debug-off](https://bin.bnbstatic.com/image/julia/docs/mp-ide/remote-debug/remote-debug-off.png)

## FAQ

Q: Failed to connect to IDE?

A: Ensure that your mobile device and IDE are on the same local network for the mobile device to
access the IDE via IP and port.

Q: Why is it loading all the time?

A: Try capturing the network requests to see which request is pending. The network might be
unstable, so please wait for a few minutes. If it still doesn't work, you can ask someone for help.

1. If the request URL starts with `/local-app-info/`, ask the IDE team for help.
2. If the request URL starts with `detail`, ask the BE team for help.
3. For other requests, ask the IOS or Android team for help.

Q: What's the difference between remote debug and preview?

A: Remote debug will pop up a `Remote Debug` window. Furthermore, remote debug will fetch
`worker-remote-debug.js` and `render-remote-debug.js`. These two files will replace Bridge with
WebSocketBridge. WebSocketBridge will forward all the requests for you.

---

# Remote Debug

Developers can inspect logs and elements from the native IDE using remote debug.

## Environment

- native version >= 2.53.0
- sdk version >= 3.14.0

## Other Requirements

- ‼️ Your mobile device should be on the same local network as your computer.

- ‼️ Scan the QR code with the same Binance account that your IDE is logged into.

## How to Use

1. Click the Remote Debug Button located at the top of the IDE.

![remote-debug-icon](https://bin.bnbstatic.com/image/julia/docs/mp-ide/remote-debug/remote-debug-icon.png)

> You must be logged in before proceeding with this step.

2. Scan the QR code generated in the previous step.

![remote-debug-qrcode](https://bin.bnbstatic.com/image/julia/docs/mp-ide/remote-debug/remote-debug-qrcode.png)

3. A panel will appear after scanning the QR code.

![remote-debug-panel](https://bin.bnbstatic.com/image/julia/docs/mp-ide/remote-debug/remote-debug-panel.png)

4. You can perform various operations, inspect logs, and view elements using this panel. In the
   debugger for remote debugging, you can debug code in the Console panel, view the source code of a
   Mini Program, and perform breakpoint or single-step debugging in the Sources panel.

You can execute `bn` related functions within it.

![img](https://bin.bnbstatic.com/image/julia/docs/mini-program/remote-debug-bn.png)

5. The page will automatically refresh when any code changes. If you prefer it not to, you can click
   the off button.

![remote-debug-off](https://bin.bnbstatic.com/image/julia/docs/mp-ide/remote-debug/remote-debug-off.png)

## FAQ

Q: Failed to connect to IDE?

A: Ensure that your mobile device and IDE are on the same local network for the mobile device to
access the IDE via IP and port.

Q: Why is it loading all the time?

A: Try capturing the network requests to see which request is pending. The network might be
unstable, so please wait for a few minutes. If it still doesn't work, you can ask someone for help.

1. If the request URL starts with `/local-app-info/`, ask the IDE team for help.
2. If the request URL starts with `detail`, ask the BE team for help.
3. For other requests, ask the IOS or Android team for help.

Q: What's the difference between remote debug and preview?

A: Remote debug will pop up a `Remote Debug` window. Furthermore, remote debug will fetch
`worker-remote-debug.js` and `render-remote-debug.js`. These two files will replace Bridge with
WebSocketBridge. WebSocketBridge will forward all the requests for you.