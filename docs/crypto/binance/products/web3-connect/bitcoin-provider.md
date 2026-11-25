---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/web3-connect/bitcoin-provider
api_type: Guide
updated_at: 2026-11-25 18:27:45.655879
---

# Bitcoin Provider

## Bitcoin Provider API

### Provider Detection

```javascript
// binancew3w.bitcoin
if (window.binancew3w.bitcoin) {
  console.log("Bitcoin Provider is detected!");
}

// we also proxy window.unisat, but some of the APIs are different
if (window.unisat && window.unisat.isBinance) {
  console.log("Bitcoin Provider is detected!");
}
```

## Connecting to Bitcoin

Connecting" or "logging in" to Binance Web3 Wallet effectively means "to access the user's Bitcoin
account(s)".

We recommend that you provide a button to allow the user to connect Binance Web3 Wallet to your
dapp. Clicking this button should call the following method:

```javascript
binancew3w.bitcoin.requestAccounts();
```

## Methods

### requestAccounts

```javascript
binancew3w.bitcoin.requestAccounts();
```

Connect the current account.

#### Parameters

none

#### Returns

`Promise` returns `string[]` : Address of current account.

#### Example

```javascript
try {
  let accounts = await window.binancew3w.bitcoin.requestAccounts();
  console.log('connect success', accounts);
} catch (e) {
  console.log('connect failed');
}
> connect success ['tb1qrn7tvhdf6wnh790384ahj56u0xaa0kqgautnnz']
```

### getAccounts

```javascript
binancew3w.bitcoin.getAccounts();
```

Get address of current account

#### Parameters

none

#### Returns

`Promise` returns `string` : Address of current account.

#### Example

```javascript
try {
  let accounts = await window.binancew3w.bitcoin.getAccounts();
  console.log('connect success', accounts);
} catch (e) {
  console.log('connect failed');
}
> connect success ['tb1qrn7tvhdf6wnh790384ahj56u0xaa0kqgautnnz']
```

### getNetwork

```javascript
binancew3w.bitcoin.getNetwork();
```

Get network of current account

#### Parameters

none

#### Returns

`Promise` returns `string` : `livenet` `testnet` or `signet`

#### Example

```javascript
try {
  let accounts = await window.binancew3w.bitcoin.getNetwork();
  console.log('connect network', accounts);
} catch (e) {
  console.log('connect failed', e);
}
> 'livenet'
```

### switchNetwork

```javascript
binancew3w.bitcoin.switchNetwork(network);
```

Switch network

#### Parameters

- `network` - `string`: the network. `livenet` `testnet` or `signet`

#### Returns

none

#### Example

```javascript
try {
  let res = await window.binancew3w.bitcoin.switchNetwork("livenet");
  console.log(res)
} catch (e) {
  console.error(e)
}
> true
```

### getPublicKey

```javascript
binancew3w.bitcoin.getPublicKey();
```

Get publicKey of current account

#### Parameters

none

#### Returns

`Promise` returns `string` : publicKey (no tweak for taproot)

#### Example

```javascript
try {
  let res = await window.binancew3w.bitcoin.getPublicKey();
  console.log(res)
} catch (e) {
  console.log(e);
}
> 03cbaedc26f03fd3ba02fc936f338e980c9e2172c5e23128877ed46827e935296f
```

### getBalance

```javascript
binancew3w.bitcoin.getBalance();
```

Get BTC balance

#### Parameters

none

#### Returns

- `Promise` returns `Object` :
  - `confirmed` - `number`: the confirmed satoshis
  - `unconfirmed` - `number`: the unconfirmed satoshis
  - `total` - `number`: the total satoshis

#### Example

```javascript
try {
  let res = await window.binancew3w.bitcoin.getBalance();
  console.log(res)
} catch (e) {
  console.log(e);
}

> {
    "confirmed":0,
    "unconfirmed":100000,
    "total":100000
  }
```

### signMessage

```javascript
binancew3w.signMessage(msg[, type])
```

sign message

#### Parameters

- `msg` - `string`: a string to sign
- `type` - `string`: (Optional) "ecdsa" | "bip322-simple". default is "ecdsa"

#### Returns

- `Promise` returns `string`: the signature

#### Example

```javascript
// sign by ecdsa
try {
  let res = await window.binancew3w.bitcoin.signMessage("abcdefghijk123456789");
  console.log(res)
} catch (e) {
  console.log(e);
}

> G+LrYa7T5dUMDgQduAErw+i6ebK4GqTXYVWIDM+snYk7Yc6LdPitmaqM6j+iJOeID1CsMXOJFpVopvPiHBdulkE=


// sign by bip322-simple
try {
  let res = await window.binancew3w.bitcoin.signMessage("abcdefghijk123456789","bip322-simple");
  console.log(res)
} catch (e) {
  console.log(e);
}

> AkcwRAIgeHUcjr0jODaR7GMM8cenWnIj0MYdGmmrpGyMoryNSkgCICzVXWrLIKKp5cFtaCTErY7FGNXTFe6kuEofl4G+Vi5wASECaIeVi8xMtvjATqSSYPDRDjEsQbr0hSUpU7FHJNtVKqw=
```

### signPsbt

```javascript
binancew3w.signPsbt(psbtHex[, options])
```

Sign PSBT

This method will traverse all inputs that match the current address to sign.

#### Parameters

- `psbtHex` - `string`: the hex string of psbt to sign
- `options` - `object`:
  - `autoFinalized` - `boolean`: whether finalize inputs signed by user's wallet after signing,
    default is `true`
  - `toSignInputs` - `array`:
    - `index` - `number`: which input to sign
    - `address` - `string`: (at least specify either an address or a publicKey) Which corresponding
      private key to use for signing
    - `publicKey` - `string`: (at least specify either an address or a publicKey) Which
      corresponding private key to use for signing
    - `sighashTypes` - `number[]`: (optionals) sighashTypes
    - `disableTweakSigner` - `boolean`: (optionals) When signing and unlocking Taproot addresses,
      the tweakSigner is used by default for signature generation. Enabling this allows for signing
      with the original private key.

#### Returns

- `Promise` returns `string`: the hex string of signed psbt

#### Example

```javascript
try {
  let res = await window.binancew3w.bitcoin.signPsbt("70736274ff01007d....", {
    autoFinalized: false,
    toSignInputs: [
      {
        index: 0,
        address: "tb1q8h8....mjxzny",
      },
      {
        index: 1,
        publicKey: "tb1q8h8....mjxzny",
        sighashTypes: [1],
      },
      {
        index: 2,
        publicKey: "02062...8779693f",
      },
    ],
  });
  console.log(res);
} catch (e) {
  console.log(e);
}

binancew3w.bitcoin.signPsbt("xxxxxxxx", {
  toSignInputs: [{ index: 0, publicKey: "xxxxxx", disableTweakSigner: true }],
  autoFinalized: false,
});
```

## Events

### accountsChanged

```javascript
binancew3w.bitcoin.on('accountsChanged', handler: (accounts: Array<string>) => void);
bitnancew3w.bitcoin.removeListener('accountsChanged', handler: (accounts: Array<string>) => void);
```

The accountsChanged will be emitted whenever the user's exposed account address changes.

### networkChanged

```javascript
binancew3w.bitcoin.on('networkChanged', handler: (network: string) => void);
binancew3w.bitcoin.removeListener('networkChanged', handler: (network: string) => void);
```

The networkChanged will be emitted whenever the user's network changes.

---

# Bitcoin Provider

## Bitcoin Provider API

### Provider Detection

```javascript
// binancew3w.bitcoin
if (window.binancew3w.bitcoin) {
  console.log("Bitcoin Provider is detected!");
}

// we also proxy window.unisat, but some of the APIs are different
if (window.unisat && window.unisat.isBinance) {
  console.log("Bitcoin Provider is detected!");
}
```

## Connecting to Bitcoin

Connecting" or "logging in" to Binance Web3 Wallet effectively means "to access the user's Bitcoin
account(s)".

We recommend that you provide a button to allow the user to connect Binance Web3 Wallet to your
dapp. Clicking this button should call the following method:

```javascript
binancew3w.bitcoin.requestAccounts();
```

## Methods

### requestAccounts

```javascript
binancew3w.bitcoin.requestAccounts();
```

Connect the current account.

#### Parameters

none

#### Returns

`Promise` returns `string[]` : Address of current account.

#### Example

```javascript
try {
  let accounts = await window.binancew3w.bitcoin.requestAccounts();
  console.log('connect success', accounts);
} catch (e) {
  console.log('connect failed');
}
> connect success ['tb1qrn7tvhdf6wnh790384ahj56u0xaa0kqgautnnz']
```

### getAccounts

```javascript
binancew3w.bitcoin.getAccounts();
```

Get address of current account

#### Parameters

none

#### Returns

`Promise` returns `string` : Address of current account.

#### Example

```javascript
try {
  let accounts = await window.binancew3w.bitcoin.getAccounts();
  console.log('connect success', accounts);
} catch (e) {
  console.log('connect failed');
}
> connect success ['tb1qrn7tvhdf6wnh790384ahj56u0xaa0kqgautnnz']
```

### getNetwork

```javascript
binancew3w.bitcoin.getNetwork();
```

Get network of current account

#### Parameters

none

#### Returns

`Promise` returns `string` : `livenet` `testnet` or `signet`

#### Example

```javascript
try {
  let accounts = await window.binancew3w.bitcoin.getNetwork();
  console.log('connect network', accounts);
} catch (e) {
  console.log('connect failed', e);
}
> 'livenet'
```

### switchNetwork

```javascript
binancew3w.bitcoin.switchNetwork(network);
```

Switch network

#### Parameters

- `network` - `string`: the network. `livenet` `testnet` or `signet`

#### Returns

none

#### Example

```javascript
try {
  let res = await window.binancew3w.bitcoin.switchNetwork("livenet");
  console.log(res)
} catch (e) {
  console.error(e)
}
> true
```

### getPublicKey

```javascript
binancew3w.bitcoin.getPublicKey();
```

Get publicKey of current account

#### Parameters

none

#### Returns

`Promise` returns `string` : publicKey (no tweak for taproot)

#### Example

```javascript
try {
  let res = await window.binancew3w.bitcoin.getPublicKey();
  console.log(res)
} catch (e) {
  console.log(e);
}
> 03cbaedc26f03fd3ba02fc936f338e980c9e2172c5e23128877ed46827e935296f
```

### getBalance

```javascript
binancew3w.bitcoin.getBalance();
```

Get BTC balance

#### Parameters

none

#### Returns

- `Promise` returns `Object` :
  - `confirmed` - `number`: the confirmed satoshis
  - `unconfirmed` - `number`: the unconfirmed satoshis
  - `total` - `number`: the total satoshis

#### Example

```javascript
try {
  let res = await window.binancew3w.bitcoin.getBalance();
  console.log(res)
} catch (e) {
  console.log(e);
}

> {
    "confirmed":0,
    "unconfirmed":100000,
    "total":100000
  }
```

### signMessage

```javascript
binancew3w.signMessage(msg[, type])
```

sign message

#### Parameters

- `msg` - `string`: a string to sign
- `type` - `string`: (Optional) "ecdsa" | "bip322-simple". default is "ecdsa"

#### Returns

- `Promise` returns `string`: the signature

#### Example

```javascript
// sign by ecdsa
try {
  let res = await window.binancew3w.bitcoin.signMessage("abcdefghijk123456789");
  console.log(res)
} catch (e) {
  console.log(e);
}

> G+LrYa7T5dUMDgQduAErw+i6ebK4GqTXYVWIDM+snYk7Yc6LdPitmaqM6j+iJOeID1CsMXOJFpVopvPiHBdulkE=


// sign by bip322-simple
try {
  let res = await window.binancew3w.bitcoin.signMessage("abcdefghijk123456789","bip322-simple");
  console.log(res)
} catch (e) {
  console.log(e);
}

> AkcwRAIgeHUcjr0jODaR7GMM8cenWnIj0MYdGmmrpGyMoryNSkgCICzVXWrLIKKp5cFtaCTErY7FGNXTFe6kuEofl4G+Vi5wASECaIeVi8xMtvjATqSSYPDRDjEsQbr0hSUpU7FHJNtVKqw=
```

### signPsbt

```javascript
binancew3w.signPsbt(psbtHex[, options])
```

Sign PSBT

This method will traverse all inputs that match the current address to sign.

#### Parameters

- `psbtHex` - `string`: the hex string of psbt to sign
- `options` - `object`:
  - `autoFinalized` - `boolean`: whether finalize inputs signed by user's wallet after signing,
    default is `true`
  - `toSignInputs` - `array`:
    - `index` - `number`: which input to sign
    - `address` - `string`: (at least specify either an address or a publicKey) Which corresponding
      private key to use for signing
    - `publicKey` - `string`: (at least specify either an address or a publicKey) Which
      corresponding private key to use for signing
    - `sighashTypes` - `number[]`: (optionals) sighashTypes
    - `disableTweakSigner` - `boolean`: (optionals) When signing and unlocking Taproot addresses,
      the tweakSigner is used by default for signature generation. Enabling this allows for signing
      with the original private key.

#### Returns

- `Promise` returns `string`: the hex string of signed psbt

#### Example

```javascript
try {
  let res = await window.binancew3w.bitcoin.signPsbt("70736274ff01007d....", {
    autoFinalized: false,
    toSignInputs: [
      {
        index: 0,
        address: "tb1q8h8....mjxzny",
      },
      {
        index: 1,
        publicKey: "tb1q8h8....mjxzny",
        sighashTypes: [1],
      },
      {
        index: 2,
        publicKey: "02062...8779693f",
      },
    ],
  });
  console.log(res);
} catch (e) {
  console.log(e);
}

binancew3w.bitcoin.signPsbt("xxxxxxxx", {
  toSignInputs: [{ index: 0, publicKey: "xxxxxx", disableTweakSigner: true }],
  autoFinalized: false,
});
```

## Events

### accountsChanged

```javascript
binancew3w.bitcoin.on('accountsChanged', handler: (accounts: Array<string>) => void);
bitnancew3w.bitcoin.removeListener('accountsChanged', handler: (accounts: Array<string>) => void);
```

The accountsChanged will be emitted whenever the user's exposed account address changes.

### networkChanged

```javascript
binancew3w.bitcoin.on('networkChanged', handler: (network: string) => void);
binancew3w.bitcoin.removeListener('networkChanged', handler: (network: string) => void);
```

The networkChanged will be emitted whenever the user's network changes.