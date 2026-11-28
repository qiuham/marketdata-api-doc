---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/web3-connect/cosmos-provider
api_type: Guide
updated_at: 2026-11-28 18:27:32.164227
---

# Cosmos Provider

## Cosmos Provider API

### Provider Detection

```javascript
// binancew3w.keplr
if (window.binancew3w.keplr) {
  console.log("Cosmos Provider is detected!");
}
```

## Connecting to Cosmos

If Binance Web3 Wallet is locked, you can unlock the wallet by using
window.binancew3w.keplr.enable(chainIds). You'll be required to grant the webpage permission to
access Keplr if such permission wasn't previously granted.

The enable method can receive one or more chain IDs as an array. When passing the chain ID array,
you can simultaneously request the permissions of all chains that haven't been authorized. If you
cancel the unlocking or are denied permission, an error will show.

```javascript
const chainId = "cosmoshub-4";
// Enabling before using the Keplr is recommended.
// This method will ask the user whether to allow access if they haven't visited this website.
// Also, it will request that the user unlock the wallet if the wallet is locked.
await window.binancew3w.keplr.enable(chainId);
```

## Methods

### signArbitrary

This request will sign any information, which is equivalent to the signMessage (any) of the previous
chains.

Connect the current account.

#### Parameters

- `chainId` - `string`
- `signerAddress` - `string`
- `data` - `string`

#### Returns

`Promise` returns `object` :

- `signature` - `string`
- `signDoc` - `object`

#### Example

```javascript
const res = await window.binancew3w.keplr.signArbitrary({
    "osmosis-1",
    "osmo1sxqwesgp7253fdv985csvz95fwc0q53ulldggl",
    'test cosmos'
    }
);
```

### signAmino

This request signs in a fixed format, similar to the signAmino method of OfflineSigner of cosmjs.
Parameters are objects, and signDoc is a fixed format.

#### Parameters

- `chainId` - `string`
- `signerAddress` - `string`
- `signDoc` - `object`

#### Returns

`Promise` returns `object` :

- `signature` - `string`
- `signed` - `boolean`

#### Example

```javascript
const res =  const res = await window.binancew3w.keplr.signAmino(
      "osmosis-1",
      "osmo1sxqwesgp7253fdv985csvz95fwc0q53ulldggl",
      {
        account_number: "707744",
        chain_id: "osmosis-1",
        fee: {
          gas: "500000",
          amount: [
            {
              denom: "uosmo",
              amount: "12500"
            }
          ]
        },
        memo: "",
        msgs: [
          {
            type: "osmosis/gamm/swap-exact-amount-in",
            value: {
              routes: [
                {
                  pool_id: "795",
                  token_out_denom: "uosmo"
                },
                {
                  pool_id: "1",
                  token_out_denom:
                    "ibc/27394FB092D2ECCD56123C74F36E4C1F926001CEADA9CA97EA622B25F41E5EB2"
                }
              ],
              sender: "osmo1sxqwesgp7253fdv985csvz95fwc0q53ulldggl",
              token_in: {
                amount: "10000",
                denom:
                  "ibc/2DA9C149E9AD2BD27FEFA635458FB37093C256C1A940392634A16BEA45262604"
              },
              token_out_min_amount: "553"
            }
          }
        ],
        sequence: "54"
      }
    );
```

---

# Cosmos Provider

## Cosmos Provider API

### Provider Detection

```javascript
// binancew3w.keplr
if (window.binancew3w.keplr) {
  console.log("Cosmos Provider is detected!");
}
```

## Connecting to Cosmos

If Binance Web3 Wallet is locked, you can unlock the wallet by using
window.binancew3w.keplr.enable(chainIds). You'll be required to grant the webpage permission to
access Keplr if such permission wasn't previously granted.

The enable method can receive one or more chain IDs as an array. When passing the chain ID array,
you can simultaneously request the permissions of all chains that haven't been authorized. If you
cancel the unlocking or are denied permission, an error will show.

```javascript
const chainId = "cosmoshub-4";
// Enabling before using the Keplr is recommended.
// This method will ask the user whether to allow access if they haven't visited this website.
// Also, it will request that the user unlock the wallet if the wallet is locked.
await window.binancew3w.keplr.enable(chainId);
```

## Methods

### signArbitrary

This request will sign any information, which is equivalent to the signMessage (any) of the previous
chains.

Connect the current account.

#### Parameters

- `chainId` - `string`
- `signerAddress` - `string`
- `data` - `string`

#### Returns

`Promise` returns `object` :

- `signature` - `string`
- `signDoc` - `object`

#### Example

```javascript
const res = await window.binancew3w.keplr.signArbitrary({
    "osmosis-1",
    "osmo1sxqwesgp7253fdv985csvz95fwc0q53ulldggl",
    'test cosmos'
    }
);
```

### signAmino

This request signs in a fixed format, similar to the signAmino method of OfflineSigner of cosmjs.
Parameters are objects, and signDoc is a fixed format.

#### Parameters

- `chainId` - `string`
- `signerAddress` - `string`
- `signDoc` - `object`

#### Returns

`Promise` returns `object` :

- `signature` - `string`
- `signed` - `boolean`

#### Example

```javascript
const res =  const res = await window.binancew3w.keplr.signAmino(
      "osmosis-1",
      "osmo1sxqwesgp7253fdv985csvz95fwc0q53ulldggl",
      {
        account_number: "707744",
        chain_id: "osmosis-1",
        fee: {
          gas: "500000",
          amount: [
            {
              denom: "uosmo",
              amount: "12500"
            }
          ]
        },
        memo: "",
        msgs: [
          {
            type: "osmosis/gamm/swap-exact-amount-in",
            value: {
              routes: [
                {
                  pool_id: "795",
                  token_out_denom: "uosmo"
                },
                {
                  pool_id: "1",
                  token_out_denom:
                    "ibc/27394FB092D2ECCD56123C74F36E4C1F926001CEADA9CA97EA622B25F41E5EB2"
                }
              ],
              sender: "osmo1sxqwesgp7253fdv985csvz95fwc0q53ulldggl",
              token_in: {
                amount: "10000",
                denom:
                  "ibc/2DA9C149E9AD2BD27FEFA635458FB37093C256C1A940392634A16BEA45262604"
              },
              token_out_min_amount: "553"
            }
          }
        ],
        sequence: "54"
      }
    );
```