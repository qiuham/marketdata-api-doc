---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/web3-dapp/self-testing
api_type: Guide
updated_at: 2026-11-26 18:28:24.659232
---

# DApp Self-Testing Manual

_SDK integration, DApps listing are independent. Well-tested DApps will help to reduce partly
campaign workload._

## Summary

For all parties interested in cooperating with Binance Web3 Wallet, this manual contains all
relevant information, including
[integrating the Binance Web3 Connect SDK](/products/web3-connect/introduction) and **joining the
Binance Web3 Wallet Dapp Zone**.

**Self-testing** by the project party is essential. The Binance Web3 Wallet team strongly recommends
that all projects complete self-testing according to the provided instructions to maximize user
experience.

Binance reserves the right to reject applications from projects that demonstrate low testing
quality. Please read the following information carefully.

## How to test dApp

1. Type your url in the latest Binance Web3 wallet browser.
2. Test all the features in DApps. You could refer to the following test case checklist for
   guidance.

![browser-entry](/img/web3-dapp/browser-entry.png)

## Frequent Problems

### Error Code : ‘Network not supported for this wallet’

Project website should detect and change to the corresponding chain when users connect. For BEVM,
check the `window.ethereum` chainId to change to the correct chain.

### IOS/Android Login Problem

Check SDK status and Internet/VPN connection.

### RPC problem

When testing on chain actions, projects might find the gas fee abnormally high. In this situation,
projects could try the test with Trust Wallet and other Wallets like Metamask. If it only happens in
Trust Wallet and Binance Wallet, it would be Binance’s RPC issue. Please contact Jasmine G
@P0kEjasmine if this happens.

### Mobile Login Issue

Ensure that the Binance App version for both IOS and Android is updated to the **latest version**.

## Test Case Checklist

### SDK

| Category         | Feature (Web, IOS and Android)                                                                                       |
| ---------------- | -------------------------------------------------------------------------------------------------------------------- |
| Connect Wallet   | Can get wallet address and chainID.                                                                                  |
| Send Transaction | The whole transaction process should be successful and can be checked on the chain.                                  |
| Sign message     | The signature value should be valid                                                                                  |
| Logo exposure    | E.g.<br/><img src={import('../../../public/img/web3-dapp/logo-exposure.png').default} style={{maxWidth: '300px'}} /> |

### dApps

| Category         | Feature (IOS and Android)                                                             |
| ---------------- | ------------------------------------------------------------------------------------- |
| Connect Wallet   | Wallet connects successfully and stably. (Without page redirection)                   |
|                  | Binance Logo Exposure Success (Web & App)                                             |
| Send Transaction | All send transaction cases are successful. (e.g. Swap, Approve, etc.)                 |
|                  | The gas fee is in the normal range.                                                   |
| User Experience  | The font size and icons are displayed appropriately.                                  |
|                  | All the URLs in the dApp can be opened in Binance directly.                           |
|                  | The project will automatically switch to the user's current chain if it is supported. |
|                  | All cases should be checked in both IOS and Android                                   |

---

# DApp Self-Testing Manual

_SDK integration, DApps listing are independent. Well-tested DApps will help to reduce partly
campaign workload._

## Summary

For all parties interested in cooperating with Binance Web3 Wallet, this manual contains all
relevant information, including
[integrating the Binance Web3 Connect SDK](/products/web3-connect/introduction) and **joining the
Binance Web3 Wallet Dapp Zone**.

**Self-testing** by the project party is essential. The Binance Web3 Wallet team strongly recommends
that all projects complete self-testing according to the provided instructions to maximize user
experience.

Binance reserves the right to reject applications from projects that demonstrate low testing
quality. Please read the following information carefully.

## How to test dApp

1. Type your url in the latest Binance Web3 wallet browser.
2. Test all the features in DApps. You could refer to the following test case checklist for
   guidance.

![browser-entry](/img/web3-dapp/browser-entry.png)

## Frequent Problems

### Error Code : ‘Network not supported for this wallet’

Project website should detect and change to the corresponding chain when users connect. For BEVM,
check the `window.ethereum` chainId to change to the correct chain.

### IOS/Android Login Problem

Check SDK status and Internet/VPN connection.

### RPC problem

When testing on chain actions, projects might find the gas fee abnormally high. In this situation,
projects could try the test with Trust Wallet and other Wallets like Metamask. If it only happens in
Trust Wallet and Binance Wallet, it would be Binance’s RPC issue. Please contact Jasmine G
@P0kEjasmine if this happens.

### Mobile Login Issue

Ensure that the Binance App version for both IOS and Android is updated to the **latest version**.

## Test Case Checklist

### SDK

| Category         | Feature (Web, IOS and Android)                                                                                       |
| ---------------- | -------------------------------------------------------------------------------------------------------------------- |
| Connect Wallet   | Can get wallet address and chainID.                                                                                  |
| Send Transaction | The whole transaction process should be successful and can be checked on the chain.                                  |
| Sign message     | The signature value should be valid                                                                                  |
| Logo exposure    | E.g.<br/><img src={import('../../../public/img/web3-dapp/logo-exposure.png').default} style={{maxWidth: '300px'}} /> |

### dApps

| Category         | Feature (IOS and Android)                                                             |
| ---------------- | ------------------------------------------------------------------------------------- |
| Connect Wallet   | Wallet connects successfully and stably. (Without page redirection)                   |
|                  | Binance Logo Exposure Success (Web & App)                                             |
| Send Transaction | All send transaction cases are successful. (e.g. Swap, Approve, etc.)                 |
|                  | The gas fee is in the normal range.                                                   |
| User Experience  | The font size and icons are displayed appropriately.                                  |
|                  | All the URLs in the dApp can be opened in Binance directly.                           |
|                  | The project will automatically switch to the user's current chain if it is supported. |
|                  | All cases should be checked in both IOS and Android                                   |