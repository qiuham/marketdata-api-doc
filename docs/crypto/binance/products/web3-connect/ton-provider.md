---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/web3-connect/ton-provider
api_type: Guide
updated_at: 2026-11-27 18:28:16.241202
---

# Ton Provider

# Ton Provider

## Introduction[](https://developers.devfdg.net/docs/binance-w3w/ton-provider#ton-provider-api)

Binance Web3 Wallet's TON API is fully compliant with
the [Ton Connect protocol](https://docs.ton.org/develop/dapps/ton-connect/protocol/). By connecting
to our TON API Provider, you can use
the [TON Connect SDK](https://docs.ton.org/develop/dapps/ton-connect/developers) to integrate with
Binance Web3 Wallet.

There are 2 ways to integrate with Binance Web3 Wallet:

JS Bridge API: for apps opened within the wallet; or when the wallet is a browser extension.

HTTP Bridge API: for apps opened outside the wallet

The last section, “Interactions”, provides detailed instructions on implementing specific Binance
Web3 Wallet interactions. Especially for conducting airdrop campaigns, some interactions are more
desirable than others.

## JS Bridge API[](https://developers.devfdg.net/docs/binance-w3w/ton-provider#js-bridge-api)

When the dapp is opened in the Binance Web3 Wallet browser, the `window.binancew3w` object will be
injected into the global scope. The object contains the `tonconnect` object, which is the bridge
object for the TON Connect protocol.

### Provider Detection[](https://developers.devfdg.net/docs/binance-w3w/ton-provider#provider-detection)

```js
window.binancew3w.tonconnect;
```

The data structure of the object it points to is as follows:

```js
interface TonConnectBridge {
  deviceInfo: DeviceInfo
  walletInfo?: WalletInfo
  protocolVersion: number
  connect(protocolVersion: number, message: ConnectRequest): Promise<ConnectEvent>
  restoreConnection(): Promise<ConnectEvent>
  send(message: AppRequest): Promise<WalletResponse>
  listen(callback: (event: WalletEvent) => void): () => void
}

```

The version of Ton Connect supported by Binance Web3 Wallet is currently 2. For more information,
see [ton-connect bridge api](https://docs.ton.org/develop/dapps/ton-connect/protocol/bridge) and [ton-connect requests and responses](https://docs.ton.org/develop/dapps/ton-connect/protocol/requests-responses)

### Example[](https://developers.devfdg.net/docs/binance-w3w/ton-provider#example)

To connect to our wallet to get the wallet address as an identifier and the necessary parameters
used to sign the transaction:

```js
const result = await window.binancew3w.tonconnect.connect(2, {
  manifestUrl: "https://example.com/manifest.json",
  items: [{ name: "ton_addr" }],
});

if (result.event === "connect") {
  console.log(result.payload.items, result.payload.device);
}
if (result.event === "connect_error") {
  console.error(result.payload.error.code, result.payload.error.message);
}
```

## HTTP Bridge API[](https://developers.devfdg.net/docs/binance-w3w/ton-provider#http-bridge-api)

If the dapp is not opened in the Binance Web3 Wallet browser, the `window.binancew3w` object will
not be injected into the global scope. In this case, the dapp can use the
[HTTP bridge API](https://github.com/ton-blockchain/ton-connect/blob/main/bridge.md) to interact
with the wallet.

### Provider Detection[](https://developers.devfdg.net/docs/binance-w3w/ton-provider#provider-detection-1)

Let say dapp with ID A connects to the bridge to listen to incoming requests from wallet with ID B.

```bash
request
    GET https://bridge.tonapi.io/bridge/events?client_id=<to_hex_str(A)>

    Accept: text/event-stream

```

Sending message from client A to client B. Bridge returns error if ttl is too high.

```bash
request
    POST https://bridge.tonapi.io/bridge/message?client_id=<to_hex_str(A)>?to=<to_hex_str(B)>&ttl=300&topic=sendTransaction

    body: <base64_encoded_message>

```

Dapp need to encrypt the message before sending it to the bridge with id of client B as public key.
And client B will decrypt the message with its private key.

When the bridge receives a message base64_encoded_message from client A addressed to client B, it
generates a message BridgeMessage:

```json
{
  "from": <to_hex_str(A)>,
  "message": <base64_encoded_message>
}

```

Client B send a message to client A. Client A will receive a message from the bridge.

Dapp need to decrypt the message with its private key(id of client A).

```json
{
  "from": <to_hex_str(B)>,
  "message": <base64_encoded_message>
}

```

## Interactions

To offer clarity on certain Binance Web3 Wallet interactions which is most appropriate for your
dApp.

### Directly Open Binance Web3 Wallet

If you want to open Binance Web3 wallet directly without the user selecting a wallet, you can follow
the steps below:

1. Add a button with the text `Binance Web3 Connect`
2. Add the following code.

> Assume the id of the button above is binance-w3w-connect.

```js
import TonConnectUI from "@tonconnect/ui";

// create an instance of TonConnectUI
const tonConnectUI = new TonConnectUI({
  manifestUrl: "https://ton-connect.github.io/demo-dapp-with-react-ui/tonconnect-manifest.json",
  buttonRootId: "your-button-root-id",
});

// add event listener to the button
document.querySelector("#binance-w3w-connect").addEventListener("click", async () => {
  await tonConnectUI.openSingleWalletModal("binanceWeb3TonWallet");
});
```

After that, when the user clicks the `Binance Web3 Connect` button, the Binance wallet app will be
opened directly.

### Call Specific Page or Action

If you want to open a specific page like swap, bridge or earn, you can request from us for a
Universal Link with relevant parameters. Use the Universal Link in a button to trigger the page
connection.

#### Available Page

Here are some pages you can open:

- **swap**

#### Parameters

Depending on the action, you may need to include additional parameters:

For Swap,

- pageName string: swap
- fromNetwork string?: ETH or TON or SOL
- toNetwork string?: ETH or TON or SOL
- fromTokenAddress string?: Token contract address of asset to swap from (If unavailable, skip this
  parameter)
- toTokenAddress string?: Token contract address of asset to swap to (If unavailable, skip this
  parameter)
- tab string?: Specific tab within a page; swap or bridge

#### Universal Link Construction

Here is how to construct the link:

```bash
https://app.binance.com/uni-qr/ww{pageName}?fromNetwork={string}&fromTokenAddress={string}&toNetwork={string}&toTokenAddress={string}&tab={string}
```

#### Implementation

To implement these universal links in your application:

1. Construct the appropriate URL based on the desired action and parameters.
2. Use the URL to create a clickable link or button in your app's interface.
3. When the user interacts with the link, it will open the Binance Web3 Wallet app (if installed) or
   redirect to the Binance app download page.

#### Example Code

Open swap page for 1 USDT to Ton on Ton chain.

```bash
https://app.binance.com/uni-qr/wwswap?fromNetwork=TON&fromTokenAddress=EQCxE6mUtQJKFnGfaROTKOt1lZbDiiX1kCixRv7Nw2Id_sDs&toNetwork=TON&toTokenAddress=0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
```

## Conclusion[](https://developers.devfdg.net/docs/binance-w3w/ton-provider#conclusion)

The Binance Web3 Wallet browser provides both JS bridge API and HTTP bridge API for dapps to
interact with the wallet. Dapps can use the JS bridge API when the dapp is opened in the Binance
Web3 Wallet browser, and use the HTTP bridge API when the dapp is not opened in the Binance Web3
Wallet browser.

We strongly recommend that dapps
use [ton-connect](https://docs.ton.org/develop/dapps/ton-connect/developers) to integrate with
Binance Web3 Wallet, as it provides a more secure and reliable way to interact with the wallet. You
don't need to care about which bridge API to use, ton-connect will automatically choose the
appropriate bridge API based on the environment. Also you don't need to care about the encryption
and decryption of messages, ton-connect will handle it for you

Refer to Interactions especially when discussing with our BD/PM to decide on a suitable UI/UX for
users.

---

# Ton Provider

# Ton Provider

## Introduction[](https://developers.devfdg.net/docs/binance-w3w/ton-provider#ton-provider-api)

Binance Web3 Wallet's TON API is fully compliant with
the [Ton Connect protocol](https://docs.ton.org/develop/dapps/ton-connect/protocol/). By connecting
to our TON API Provider, you can use
the [TON Connect SDK](https://docs.ton.org/develop/dapps/ton-connect/developers) to integrate with
Binance Web3 Wallet.

There are 2 ways to integrate with Binance Web3 Wallet:

JS Bridge API: for apps opened within the wallet; or when the wallet is a browser extension.

HTTP Bridge API: for apps opened outside the wallet

The last section, “Interactions”, provides detailed instructions on implementing specific Binance
Web3 Wallet interactions. Especially for conducting airdrop campaigns, some interactions are more
desirable than others.

## JS Bridge API[](https://developers.devfdg.net/docs/binance-w3w/ton-provider#js-bridge-api)

When the dapp is opened in the Binance Web3 Wallet browser, the `window.binancew3w` object will be
injected into the global scope. The object contains the `tonconnect` object, which is the bridge
object for the TON Connect protocol.

### Provider Detection[](https://developers.devfdg.net/docs/binance-w3w/ton-provider#provider-detection)

```js
window.binancew3w.tonconnect;
```

The data structure of the object it points to is as follows:

```js
interface TonConnectBridge {
  deviceInfo: DeviceInfo
  walletInfo?: WalletInfo
  protocolVersion: number
  connect(protocolVersion: number, message: ConnectRequest): Promise<ConnectEvent>
  restoreConnection(): Promise<ConnectEvent>
  send(message: AppRequest): Promise<WalletResponse>
  listen(callback: (event: WalletEvent) => void): () => void
}

```

The version of Ton Connect supported by Binance Web3 Wallet is currently 2. For more information,
see [ton-connect bridge api](https://docs.ton.org/develop/dapps/ton-connect/protocol/bridge) and [ton-connect requests and responses](https://docs.ton.org/develop/dapps/ton-connect/protocol/requests-responses)

### Example[](https://developers.devfdg.net/docs/binance-w3w/ton-provider#example)

To connect to our wallet to get the wallet address as an identifier and the necessary parameters
used to sign the transaction:

```js
const result = await window.binancew3w.tonconnect.connect(2, {
  manifestUrl: "https://example.com/manifest.json",
  items: [{ name: "ton_addr" }],
});

if (result.event === "connect") {
  console.log(result.payload.items, result.payload.device);
}
if (result.event === "connect_error") {
  console.error(result.payload.error.code, result.payload.error.message);
}
```

## HTTP Bridge API[](https://developers.devfdg.net/docs/binance-w3w/ton-provider#http-bridge-api)

If the dapp is not opened in the Binance Web3 Wallet browser, the `window.binancew3w` object will
not be injected into the global scope. In this case, the dapp can use the
[HTTP bridge API](https://github.com/ton-blockchain/ton-connect/blob/main/bridge.md) to interact
with the wallet.

### Provider Detection[](https://developers.devfdg.net/docs/binance-w3w/ton-provider#provider-detection-1)

Let say dapp with ID A connects to the bridge to listen to incoming requests from wallet with ID B.

```bash
request
    GET https://bridge.tonapi.io/bridge/events?client_id=<to_hex_str(A)>

    Accept: text/event-stream

```

Sending message from client A to client B. Bridge returns error if ttl is too high.

```bash
request
    POST https://bridge.tonapi.io/bridge/message?client_id=<to_hex_str(A)>?to=<to_hex_str(B)>&ttl=300&topic=sendTransaction

    body: <base64_encoded_message>

```

Dapp need to encrypt the message before sending it to the bridge with id of client B as public key.
And client B will decrypt the message with its private key.

When the bridge receives a message base64_encoded_message from client A addressed to client B, it
generates a message BridgeMessage:

```json
{
  "from": <to_hex_str(A)>,
  "message": <base64_encoded_message>
}

```

Client B send a message to client A. Client A will receive a message from the bridge.

Dapp need to decrypt the message with its private key(id of client A).

```json
{
  "from": <to_hex_str(B)>,
  "message": <base64_encoded_message>
}

```

## Interactions

To offer clarity on certain Binance Web3 Wallet interactions which is most appropriate for your
dApp.

### Directly Open Binance Web3 Wallet

If you want to open Binance Web3 wallet directly without the user selecting a wallet, you can follow
the steps below:

1. Add a button with the text `Binance Web3 Connect`
2. Add the following code.

> Assume the id of the button above is binance-w3w-connect.

```js
import TonConnectUI from "@tonconnect/ui";

// create an instance of TonConnectUI
const tonConnectUI = new TonConnectUI({
  manifestUrl: "https://ton-connect.github.io/demo-dapp-with-react-ui/tonconnect-manifest.json",
  buttonRootId: "your-button-root-id",
});

// add event listener to the button
document.querySelector("#binance-w3w-connect").addEventListener("click", async () => {
  await tonConnectUI.openSingleWalletModal("binanceWeb3TonWallet");
});
```

After that, when the user clicks the `Binance Web3 Connect` button, the Binance wallet app will be
opened directly.

### Call Specific Page or Action

If you want to open a specific page like swap, bridge or earn, you can request from us for a
Universal Link with relevant parameters. Use the Universal Link in a button to trigger the page
connection.

#### Available Page

Here are some pages you can open:

- **swap**

#### Parameters

Depending on the action, you may need to include additional parameters:

For Swap,

- pageName string: swap
- fromNetwork string?: ETH or TON or SOL
- toNetwork string?: ETH or TON or SOL
- fromTokenAddress string?: Token contract address of asset to swap from (If unavailable, skip this
  parameter)
- toTokenAddress string?: Token contract address of asset to swap to (If unavailable, skip this
  parameter)
- tab string?: Specific tab within a page; swap or bridge

#### Universal Link Construction

Here is how to construct the link:

```bash
https://app.binance.com/uni-qr/ww{pageName}?fromNetwork={string}&fromTokenAddress={string}&toNetwork={string}&toTokenAddress={string}&tab={string}
```

#### Implementation

To implement these universal links in your application:

1. Construct the appropriate URL based on the desired action and parameters.
2. Use the URL to create a clickable link or button in your app's interface.
3. When the user interacts with the link, it will open the Binance Web3 Wallet app (if installed) or
   redirect to the Binance app download page.

#### Example Code

Open swap page for 1 USDT to Ton on Ton chain.

```bash
https://app.binance.com/uni-qr/wwswap?fromNetwork=TON&fromTokenAddress=EQCxE6mUtQJKFnGfaROTKOt1lZbDiiX1kCixRv7Nw2Id_sDs&toNetwork=TON&toTokenAddress=0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
```

## Conclusion[](https://developers.devfdg.net/docs/binance-w3w/ton-provider#conclusion)

The Binance Web3 Wallet browser provides both JS bridge API and HTTP bridge API for dapps to
interact with the wallet. Dapps can use the JS bridge API when the dapp is opened in the Binance
Web3 Wallet browser, and use the HTTP bridge API when the dapp is not opened in the Binance Web3
Wallet browser.

We strongly recommend that dapps
use [ton-connect](https://docs.ton.org/develop/dapps/ton-connect/developers) to integrate with
Binance Web3 Wallet, as it provides a more secure and reliable way to interact with the wallet. You
don't need to care about which bridge API to use, ton-connect will automatically choose the
appropriate bridge API based on the environment. Also you don't need to care about the encryption
and decryption of messages, ton-connect will handle it for you

Refer to Interactions especially when discussing with our BD/PM to decide on a suitable UI/UX for
users.