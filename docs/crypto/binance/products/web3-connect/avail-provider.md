---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/web3-connect/avail-provider
api_type: Guide
updated_at: 2026-11-21 18:27:07.859363
---

# Avail Provider

## Avail Provider API

Binance Web3 Wallet's Avail API is fully compliant with the
[polkadot extension](https://polkadot.js.org/docs/extension/). Dapps can use it to integrate with
Binance Web3 Wallet.

### Provider Detection

We will inject the `window.injectedWeb3` object into the global scope. The object contains the
`binancew3w` object, which is the bridge object for the Avail protocol.

```js
window.injectedWeb3 = {
  'binancew3w': {
    // semver for the package
    version: '1.0.0',
    // this is called to enable the injection, and returns an injected
    // object containing the accounts, signer and provider interfaces
    // (or it will reject if not authorized)
    enable (originName: string): Promise<Injected>
  }
}
```

You can get the provider object by calling `window.injectedWeb3['binancew3w'].enable('my dapp')`.
and then use the `accounts` and `signer` interfaces to interact with the injected account.

```js
const provider = await window.injectedWeb3["subwallet-js"].enable("my dapp");
const allAccounts = provider.accounts.get();
const AVAIL_GENESIS_HASH = isTest ? "0xd3d2f3a3495dc597434a99d7d449ebad6616db45e4e4f178f31cc6fa14378b70" : "0xb91746b45e0346cc2f815a520b9c6cb4d5c0902af848db0a80f85932d2e8276a";
if (allAccounts.length > 0) {
  console.log("Injected accounts:", allAccounts);
  for (let i = 0; i < allAccounts.length; i++) {
    if (allAccounts[i].genesisHash === AVAIL_GENESIS_HASH) {
      console.log("Injected avail account:", allAccounts[i]);
    }
  }
}
```

You can also use the `@polkadot/extension-dapp` package to detect the provider:

```js
const AVAIL_GENESIS_HASH = isTest ? "0xd3d2f3a3495dc597434a99d7d449ebad6616db45e4e4f178f31cc6fa14378b70" : "0xb91746b45e0346cc2f815a520b9c6cb4d5c0902af848db0a80f85932d2e8276a";
const allAccounts = await web3Accounts();
if (allAccounts.length > 0) {
  console.log("Injected accounts:", allAccounts);
  for (let i = 0; i < allAccounts.length; i++) {
    if (allAccounts[i].genesisHash === AVAIL_GENESIS_HASH) {
      console.log("Injected avail account:", allAccounts[i]);
    }
  }
}
```

## Injection information

And here is the related interfaces:

```ts
interface Injected {
  // the interface for Accounts, as detailed below
  readonly accounts: Accounts;
  // the standard Signer interface for the API, as detailed below
  readonly signer: Signer;
}

interface Account = {
  // ss-58 encoded address
  readonly address: string;
  // the genesisHash for this account (empty if applicable to all)
  readonly genesisHash?: string;
  // (optional) name for display
  readonly name?: string;
};

// exposes accounts
interface Accounts {
  // retrieves the list of accounts for right now
  get: () => Promise<Account[]>;
  // (optional) subscribe to all accounts, updating as they change
  subscribe?: (cb: (accounts: Account[]) => any) => () => void
}

// a signer that communicates with the extension via sendMessage
interface Signer {
    /**
     * @description signs an extrinsic payload from a serialized form
     */
    signPayload?: (payload: SignerPayloadJSON) => Promise<SignerResult>;
    /**
     * @description signs a raw payload, only the bytes data as supplied
     */
    signRaw?: (raw: SignerPayloadRaw) => Promise<SignerResult>;
}
```

## Provide metadata

You may need to provide metadata for the wallet, such as the chain name, chain type, color, genesis
hash, icon, and meta calls.

```js
// the address we use to use for signing, as injected
const SENDER = '5DTestUPts3kjeXSTMyerHihn1uwMfLj8vU8sqF7qYrFabHE';

// finds an injector for an address
const injector = await web3FromAddress(SENDER);
injector.metadata.provide({
    chain: 'Avail DA Mainnet',
    chainType: 'substrate',
    color: '#1B1E26',
    genesisHash: '0xb91746b45e0346cc2f815a520b9c6cb4d5c0902af848db0a80f85932d2e8276a',
    icon: 'substrate',
    metaCalls: ...
})
```

## signAndSend

You can use the `signAndSend` method to sign and send a transaction.

```js
import { web3Accounts, web3Enable, web3FromAddress } from '@polkadot/extension-dapp';

// returns an array of all the injected sources
// (this needs to be called first, before other requests)
const allInjected = await web3Enable('my cool dapp');

// returns an array of { address, meta: { name, source } }
// meta.source contains the name of the extension that provides this account
const allAccounts = await web3Accounts();

// the address we use to use for signing, as injected
const SENDER = '5DTestUPts3kjeXSTMyerHihn1uwMfLj8vU8sqF7qYrFabHE';

// finds an injector for an address
const injector = await web3FromAddress(SENDER);

// sign and send our transaction - notice here that the address of the account
// (as retrieved injected) is passed through as the param to the `signAndSend`,
// the API then calls the extension to present to the user and get it signed.
// Once complete, the api sends the tx + signature via the normal process
api.tx.balances
  .transfer('5C5555yEXUcmEJ5kkcCMvdZjUo7NGJiQJMS7vZXEeoMhj3VQ', 123456)
  .signAndSend(SENDER, { signer: injector.signer }, (status) => { ... });
```

---

# Avail Provider

## Avail Provider API

Binance Web3 Wallet's Avail API is fully compliant with the
[polkadot extension](https://polkadot.js.org/docs/extension/). Dapps can use it to integrate with
Binance Web3 Wallet.

### Provider Detection

We will inject the `window.injectedWeb3` object into the global scope. The object contains the
`binancew3w` object, which is the bridge object for the Avail protocol.

```js
window.injectedWeb3 = {
  'binancew3w': {
    // semver for the package
    version: '1.0.0',
    // this is called to enable the injection, and returns an injected
    // object containing the accounts, signer and provider interfaces
    // (or it will reject if not authorized)
    enable (originName: string): Promise<Injected>
  }
}
```

You can get the provider object by calling `window.injectedWeb3['binancew3w'].enable('my dapp')`.
and then use the `accounts` and `signer` interfaces to interact with the injected account.

```js
const provider = await window.injectedWeb3["subwallet-js"].enable("my dapp");
const allAccounts = provider.accounts.get();
const AVAIL_GENESIS_HASH = isTest ? "0xd3d2f3a3495dc597434a99d7d449ebad6616db45e4e4f178f31cc6fa14378b70" : "0xb91746b45e0346cc2f815a520b9c6cb4d5c0902af848db0a80f85932d2e8276a";
if (allAccounts.length > 0) {
  console.log("Injected accounts:", allAccounts);
  for (let i = 0; i < allAccounts.length; i++) {
    if (allAccounts[i].genesisHash === AVAIL_GENESIS_HASH) {
      console.log("Injected avail account:", allAccounts[i]);
    }
  }
}
```

You can also use the `@polkadot/extension-dapp` package to detect the provider:

```js
const AVAIL_GENESIS_HASH = isTest ? "0xd3d2f3a3495dc597434a99d7d449ebad6616db45e4e4f178f31cc6fa14378b70" : "0xb91746b45e0346cc2f815a520b9c6cb4d5c0902af848db0a80f85932d2e8276a";
const allAccounts = await web3Accounts();
if (allAccounts.length > 0) {
  console.log("Injected accounts:", allAccounts);
  for (let i = 0; i < allAccounts.length; i++) {
    if (allAccounts[i].genesisHash === AVAIL_GENESIS_HASH) {
      console.log("Injected avail account:", allAccounts[i]);
    }
  }
}
```

## Injection information

And here is the related interfaces:

```ts
interface Injected {
  // the interface for Accounts, as detailed below
  readonly accounts: Accounts;
  // the standard Signer interface for the API, as detailed below
  readonly signer: Signer;
}

interface Account = {
  // ss-58 encoded address
  readonly address: string;
  // the genesisHash for this account (empty if applicable to all)
  readonly genesisHash?: string;
  // (optional) name for display
  readonly name?: string;
};

// exposes accounts
interface Accounts {
  // retrieves the list of accounts for right now
  get: () => Promise<Account[]>;
  // (optional) subscribe to all accounts, updating as they change
  subscribe?: (cb: (accounts: Account[]) => any) => () => void
}

// a signer that communicates with the extension via sendMessage
interface Signer {
    /**
     * @description signs an extrinsic payload from a serialized form
     */
    signPayload?: (payload: SignerPayloadJSON) => Promise<SignerResult>;
    /**
     * @description signs a raw payload, only the bytes data as supplied
     */
    signRaw?: (raw: SignerPayloadRaw) => Promise<SignerResult>;
}
```

## Provide metadata

You may need to provide metadata for the wallet, such as the chain name, chain type, color, genesis
hash, icon, and meta calls.

```js
// the address we use to use for signing, as injected
const SENDER = '5DTestUPts3kjeXSTMyerHihn1uwMfLj8vU8sqF7qYrFabHE';

// finds an injector for an address
const injector = await web3FromAddress(SENDER);
injector.metadata.provide({
    chain: 'Avail DA Mainnet',
    chainType: 'substrate',
    color: '#1B1E26',
    genesisHash: '0xb91746b45e0346cc2f815a520b9c6cb4d5c0902af848db0a80f85932d2e8276a',
    icon: 'substrate',
    metaCalls: ...
})
```

## signAndSend

You can use the `signAndSend` method to sign and send a transaction.

```js
import { web3Accounts, web3Enable, web3FromAddress } from '@polkadot/extension-dapp';

// returns an array of all the injected sources
// (this needs to be called first, before other requests)
const allInjected = await web3Enable('my cool dapp');

// returns an array of { address, meta: { name, source } }
// meta.source contains the name of the extension that provides this account
const allAccounts = await web3Accounts();

// the address we use to use for signing, as injected
const SENDER = '5DTestUPts3kjeXSTMyerHihn1uwMfLj8vU8sqF7qYrFabHE';

// finds an injector for an address
const injector = await web3FromAddress(SENDER);

// sign and send our transaction - notice here that the address of the account
// (as retrieved injected) is passed through as the param to the `signAndSend`,
// the API then calls the extension to present to the user and get it signed.
// Once complete, the api sends the tx + signature via the normal process
api.tx.balances
  .transfer('5C5555yEXUcmEJ5kkcCMvdZjUo7NGJiQJMS7vZXEeoMhj3VQ', 123456)
  .signAndSend(SENDER, { signer: injector.signer }, (status) => { ... });
```