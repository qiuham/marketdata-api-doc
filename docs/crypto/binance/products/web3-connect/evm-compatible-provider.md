---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/web3-connect/evm-compatible-provider
api_type: Guide
updated_at: 2026-11-27 18:28:23.146770
---

# EVM-Compatible Provider

## Binance Web3 Wallet Provider API

The Provider API is a JavaScript API that connects wallets with dApps. The dApps you visit can
access your wallet, read on-chain data, sign messages, and send transactions.

Below are some common usage examples

```tsx
// Wallet connection
if (typeof window.binancew3w.ethereum !== "undefined") {
  try {
    const accounts = await window.binancew3w.ethereum.request({
      method: "eth_requestAccounts",
    });
    console.log("connected:", accounts[0]);
  } catch (error) {
    console.error("connection rejected:", error);
  }
} else {
  alert("Please install wallet!");
}

// Send transaction
const transactionParameters = {
  from: accounts[0], // sender address
  to: "0xRecipientAddress", // recipient address
  value: "0xDE0B6B3A7640000",
  gasLimit: "0x5208", // 21000 gas
};

try {
  const txHash = await window.binancew3w.ethereum.request({
    method: "eth_sendTransaction",
    params: [transactionParameters],
  });
  console.log("Transaction hash:", txHash);
} catch (error) {
  console.error("Transaction failed:", error);
}

// Switch accounts
window.binancew3w.ethereum.on("accountsChanged", (accounts) => {
  if (accounts.length === 0) {
    console.log("Wallet has been disconnected");
  } else {
    console.log("Current account:", accounts[0]);
  }
});

// Switch chains
window.binancew3w.ethereum.on("chainChanged", (chainId) => {
  console.log("Current chain id:", chainId);
});
```

## Installation

The installation process may vary depending on the technology stack you are using.

## Integration

### Integration with RainbowKit 2.x

Add Packages

```shell
npm install @binance/w3w-rainbow-connector-v2 @rainbow-me/rainbowkit@2.1.2 wagmi@2.x viem@2.x @tanstack/react-query
```

Usage

```typescript
import '@rainbow-me/rainbowkit/styles.css'
import { connectorsForWallets, RainbowKitProvider, WalletList } from '@rainbow-me/rainbowkit'
import { injectedWallet } from '@rainbow-me/rainbowkit/wallets'
import { WagmiProvider, createConfig, http } from 'wagmi'
import { bsc, mainnet, sepolia } from 'wagmi/chains'
import { QueryClient, QueryClientProvider } from '@tanstack/react-query'
import binanceWallet from '@binance/w3w-rainbow-connector-v2'

const WALLET_CONNECT_PROJECT_ID = 'xxxxxxxxxx'
const APP_NAME = 'xxx'

const recommendedWalletList: WalletList = [
  {
    groupName: 'Recommended',
    wallets: [
      injectedWallet,
      binanceWallet,
    ],
  },
]
const connectors = connectorsForWallets(
  recommendedWalletList,
  { projectId: WALLET_CONNECT_PROJECT_ID, appName: APP_NAME }
)

const config = createConfig({
  ssr: true,
  connectors,
  chains: [mainnet, sepolia, bsc],
  transports: {
    [mainnet.id]: http(),
    [sepolia.id]: http(),
    [bsc.id]: http(),
  },
})

const queryClient = new QueryClient()

export default function RainbowProvider({ children }) {
  return (
    <WagmiProvider config={config}>
      <QueryClientProvider client={queryClient}>
        <RainbowKitProvider>{children}</RainbowKitProvider>
      </QueryClientProvider>
    </WagmiProvider>
  )
}

```

### Integration with BlockNative

Add Packages

```shell
npm install @web3-onboard/core @binance/w3w-blocknative-connector
```

Usage

```typescript
import Onboard from "@web3-onboard/core";
import binanceModule from "@binance/w3w-blocknative-connector";

// initialize the module with options
const binance = binanceModule({ options: { lng: "en" } });

// can also initialize with no options...
// const binance = binanceModule()

const onboard = Onboard({
  // ... other Onboard options
  wallets: [
    binance,
    //... other wallets
  ],
});

const connectedWallets = await onboard.connectWallet();
console.log(connectedWallets);
```

### Integration with wagmi v2

Add Packages

```shell
npm install wagmi@2.x viem@2.x @tanstack/react-query @binance/w3w-wagmi-connector-v2
```

Integrate with your projects

```tsx
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { http, createConfig, WagmiProvider } from "wagmi";
import { injected } from "wagmi/connectors";
import { getWagmiConnectorV2 } from "@binance/w3w-wagmi-connector-v2";
import { bsc, mainnet, sepolia } from "wagmi/chains";

const connector = getWagmiConnectorV2();

const config = createConfig({
  chains: [mainnet, sepolia, bsc],
  connectors: [injected(), connector()],
  transports: {
    [mainnet.id]: http(),
    [sepolia.id]: http(),
    [bsc.id]: http(),
  },
});
const queryClient = new QueryClient();

export default function WagmiV2() {
  return (
    <WagmiProvider config={config}>
      <QueryClientProvider client={queryClient}>
        <Home />
      </QueryClientProvider>
    </WagmiProvider>
  );
}
```

Use wagmi v2 API

[wagmi v2](https://wagmi.sh/) provides many useful API for you to use, here is a basic example.

```tsx
import { Connector, useConnect, useDisconnect, useSignMessage } from "wagmi";

function WalletOption({ connector, onClick }: { connector: Connector; onClick: () => void }) {
  const [ready, setReady] = React.useState(false);

  React.useEffect(() => {
    (async () => {
      const provider = await connector.getProvider();
      setReady(!!provider);
    })();
  }, [connector]);

  return (
    <button disabled={!ready} onClick={onClick}>
      {connector.name}
    </button>
  );
}

function Home() {
  const { connectors, connect } = useConnect();
  const { disconnect } = useDisconnect();
  const { signMessage, data } = useSignMessage();

  return (
    <main>
      <section>
        <h2>wagmi v2 connector</h2>
        <div>
          {connectors.map((connector) => (
            <WalletOption key={connector.uid} connector={connector} onClick={() => connect({ connector })} />
          ))}
        </div>
        <button onClick={() => disconnect()}>disconnect</button>
        <button onClick={() => signMessage()}>signMessage</button>
      </section>
    </main>
  );
}
```

#### Get connector by id from wagmi

If you need to getConnector by id, you can use the following code

```tsx
const connector = connectors.find((connector) => {
  return connector.id === "BinanceW3WSDK" || connector.id === "wallet.binance.com";
});
```

### Wagmi injected connector

If you like to inject Binance web3 wallet, you can use the following code

```tsx
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { http, createConfig, WagmiProvider } from "wagmi"; // wagmi v2 API
import { injected } from "wagmi/connectors";
import { bsc, mainnet, sepolia } from "wagmi/chains";

const config = createConfig({
  ssr: true,
  chains: [mainnet, sepolia, bsc],
  connectors: [
    injected({
      target: {
        // Provide the injected target to avoid window.ethereum provider overwrite conflict
        id: "wallet.binance.com",
        name: "Binance Wallet Injected",
        provider: () => window.binancew3w.ethereum,
      },
    }),
  ],
  transports: {
    [mainnet.id]: http(),
    [sepolia.id]: http(),
    [bsc.id]: http(),
  },
});
const queryClient = new QueryClient();

export default function WagmiV2Injected() {
  return (
    <WagmiProvider config={config}>
      <QueryClientProvider client={queryClient}>
        <Home />
      </QueryClientProvider>
    </WagmiProvider>
  );
}
```

## Utility

### isInBinance

Return `true` if the dApp is in the dApp browser of the Binance Web3 Wallet.

```ts
import { isInBinance } from "@binance/w3w-utils";
isInBinance(); // return boolean

// Or you can detect without install any packages
window.ethereum.isBinance; // boolean
```

## Example code

Here is the example project which integrating the SDK. <https://github.com/sunopar/test-sdk>

## Troubleshooting

### buffer is not defined

While using wagmi or Rainbowkit, if you are using regular React(not SSR), you may encounter the
error `buffer is not defined`.

You can try to install `buffer` package.

```shell
npm install buffer
```

```tsx
// src/index.ts
import { Buffer } from "buffer";
window.Buffer = Buffer;
```

```html
// public/index.html
<script>
  var global = global || window;
</script>
```

### Non-React project

For Non-React project, you can refer this example
<https://github.com/sunopar/test-sdk/blob/main/src/app/ethereum/page.js>

---

# EVM-Compatible Provider

## Binance Web3 Wallet Provider API

The Provider API is a JavaScript API that connects wallets with dApps. The dApps you visit can
access your wallet, read on-chain data, sign messages, and send transactions.

Below are some common usage examples

```tsx
// Wallet connection
if (typeof window.binancew3w.ethereum !== "undefined") {
  try {
    const accounts = await window.binancew3w.ethereum.request({
      method: "eth_requestAccounts",
    });
    console.log("connected:", accounts[0]);
  } catch (error) {
    console.error("connection rejected:", error);
  }
} else {
  alert("Please install wallet!");
}

// Send transaction
const transactionParameters = {
  from: accounts[0], // sender address
  to: "0xRecipientAddress", // recipient address
  value: "0xDE0B6B3A7640000",
  gasLimit: "0x5208", // 21000 gas
};

try {
  const txHash = await window.binancew3w.ethereum.request({
    method: "eth_sendTransaction",
    params: [transactionParameters],
  });
  console.log("Transaction hash:", txHash);
} catch (error) {
  console.error("Transaction failed:", error);
}

// Switch accounts
window.binancew3w.ethereum.on("accountsChanged", (accounts) => {
  if (accounts.length === 0) {
    console.log("Wallet has been disconnected");
  } else {
    console.log("Current account:", accounts[0]);
  }
});

// Switch chains
window.binancew3w.ethereum.on("chainChanged", (chainId) => {
  console.log("Current chain id:", chainId);
});
```

## Installation

The installation process may vary depending on the technology stack you are using.

## Integration

### Integration with RainbowKit 2.x

Add Packages

```shell
npm install @binance/w3w-rainbow-connector-v2 @rainbow-me/rainbowkit@2.1.2 wagmi@2.x viem@2.x @tanstack/react-query
```

Usage

```typescript
import '@rainbow-me/rainbowkit/styles.css'
import { connectorsForWallets, RainbowKitProvider, WalletList } from '@rainbow-me/rainbowkit'
import { injectedWallet } from '@rainbow-me/rainbowkit/wallets'
import { WagmiProvider, createConfig, http } from 'wagmi'
import { bsc, mainnet, sepolia } from 'wagmi/chains'
import { QueryClient, QueryClientProvider } from '@tanstack/react-query'
import binanceWallet from '@binance/w3w-rainbow-connector-v2'

const WALLET_CONNECT_PROJECT_ID = 'xxxxxxxxxx'
const APP_NAME = 'xxx'

const recommendedWalletList: WalletList = [
  {
    groupName: 'Recommended',
    wallets: [
      injectedWallet,
      binanceWallet,
    ],
  },
]
const connectors = connectorsForWallets(
  recommendedWalletList,
  { projectId: WALLET_CONNECT_PROJECT_ID, appName: APP_NAME }
)

const config = createConfig({
  ssr: true,
  connectors,
  chains: [mainnet, sepolia, bsc],
  transports: {
    [mainnet.id]: http(),
    [sepolia.id]: http(),
    [bsc.id]: http(),
  },
})

const queryClient = new QueryClient()

export default function RainbowProvider({ children }) {
  return (
    <WagmiProvider config={config}>
      <QueryClientProvider client={queryClient}>
        <RainbowKitProvider>{children}</RainbowKitProvider>
      </QueryClientProvider>
    </WagmiProvider>
  )
}

```

### Integration with BlockNative

Add Packages

```shell
npm install @web3-onboard/core @binance/w3w-blocknative-connector
```

Usage

```typescript
import Onboard from "@web3-onboard/core";
import binanceModule from "@binance/w3w-blocknative-connector";

// initialize the module with options
const binance = binanceModule({ options: { lng: "en" } });

// can also initialize with no options...
// const binance = binanceModule()

const onboard = Onboard({
  // ... other Onboard options
  wallets: [
    binance,
    //... other wallets
  ],
});

const connectedWallets = await onboard.connectWallet();
console.log(connectedWallets);
```

### Integration with wagmi v2

Add Packages

```shell
npm install wagmi@2.x viem@2.x @tanstack/react-query @binance/w3w-wagmi-connector-v2
```

Integrate with your projects

```tsx
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { http, createConfig, WagmiProvider } from "wagmi";
import { injected } from "wagmi/connectors";
import { getWagmiConnectorV2 } from "@binance/w3w-wagmi-connector-v2";
import { bsc, mainnet, sepolia } from "wagmi/chains";

const connector = getWagmiConnectorV2();

const config = createConfig({
  chains: [mainnet, sepolia, bsc],
  connectors: [injected(), connector()],
  transports: {
    [mainnet.id]: http(),
    [sepolia.id]: http(),
    [bsc.id]: http(),
  },
});
const queryClient = new QueryClient();

export default function WagmiV2() {
  return (
    <WagmiProvider config={config}>
      <QueryClientProvider client={queryClient}>
        <Home />
      </QueryClientProvider>
    </WagmiProvider>
  );
}
```

Use wagmi v2 API

[wagmi v2](https://wagmi.sh/) provides many useful API for you to use, here is a basic example.

```tsx
import { Connector, useConnect, useDisconnect, useSignMessage } from "wagmi";

function WalletOption({ connector, onClick }: { connector: Connector; onClick: () => void }) {
  const [ready, setReady] = React.useState(false);

  React.useEffect(() => {
    (async () => {
      const provider = await connector.getProvider();
      setReady(!!provider);
    })();
  }, [connector]);

  return (
    <button disabled={!ready} onClick={onClick}>
      {connector.name}
    </button>
  );
}

function Home() {
  const { connectors, connect } = useConnect();
  const { disconnect } = useDisconnect();
  const { signMessage, data } = useSignMessage();

  return (
    <main>
      <section>
        <h2>wagmi v2 connector</h2>
        <div>
          {connectors.map((connector) => (
            <WalletOption key={connector.uid} connector={connector} onClick={() => connect({ connector })} />
          ))}
        </div>
        <button onClick={() => disconnect()}>disconnect</button>
        <button onClick={() => signMessage()}>signMessage</button>
      </section>
    </main>
  );
}
```

#### Get connector by id from wagmi

If you need to getConnector by id, you can use the following code

```tsx
const connector = connectors.find((connector) => {
  return connector.id === "BinanceW3WSDK" || connector.id === "wallet.binance.com";
});
```

### Wagmi injected connector

If you like to inject Binance web3 wallet, you can use the following code

```tsx
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { http, createConfig, WagmiProvider } from "wagmi"; // wagmi v2 API
import { injected } from "wagmi/connectors";
import { bsc, mainnet, sepolia } from "wagmi/chains";

const config = createConfig({
  ssr: true,
  chains: [mainnet, sepolia, bsc],
  connectors: [
    injected({
      target: {
        // Provide the injected target to avoid window.ethereum provider overwrite conflict
        id: "wallet.binance.com",
        name: "Binance Wallet Injected",
        provider: () => window.binancew3w.ethereum,
      },
    }),
  ],
  transports: {
    [mainnet.id]: http(),
    [sepolia.id]: http(),
    [bsc.id]: http(),
  },
});
const queryClient = new QueryClient();

export default function WagmiV2Injected() {
  return (
    <WagmiProvider config={config}>
      <QueryClientProvider client={queryClient}>
        <Home />
      </QueryClientProvider>
    </WagmiProvider>
  );
}
```

## Utility

### isInBinance

Return `true` if the dApp is in the dApp browser of the Binance Web3 Wallet.

```ts
import { isInBinance } from "@binance/w3w-utils";
isInBinance(); // return boolean

// Or you can detect without install any packages
window.ethereum.isBinance; // boolean
```

## Example code

Here is the example project which integrating the SDK. <https://github.com/sunopar/test-sdk>

## Troubleshooting

### buffer is not defined

While using wagmi or Rainbowkit, if you are using regular React(not SSR), you may encounter the
error `buffer is not defined`.

You can try to install `buffer` package.

```shell
npm install buffer
```

```tsx
// src/index.ts
import { Buffer } from "buffer";
window.Buffer = Buffer;
```

```html
// public/index.html
<script>
  var global = global || window;
</script>
```

### Non-React project

For Non-React project, you can refer this example
<https://github.com/sunopar/test-sdk/blob/main/src/app/ethereum/page.js>