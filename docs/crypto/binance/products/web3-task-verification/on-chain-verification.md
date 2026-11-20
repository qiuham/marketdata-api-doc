---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/web3-task-verification/on-chain-verification
api_type: Guide
updated_at: 2026-11-20 18:28:57.882660
---

# Binance Web3 ON-Chain API Specification

## Web3 API description

- Binance's Partners need to follow the API specification in this doc in order to integrate with
  Binance.

## API Specification​

### EVM Compatible Blockchains

#### VerificationProvider

```solidity
abstract contract VerificationProvider {
  // verify is to check if the user is verified in the partner's system
  function verify(address addr) external view virtual returns (bool pass, string memory message);
}
```

You are required to implement the `VerificationProvider` contract in your smart contract. The
`verify` function should return `true` if the verification is successful, otherwise `false`. The
`message` should contain the reason for the failure.

#### Example

```solidity
contract Example is VerificationProvider {
  function verify(address user) external view override returns (bool pass, string memory message)
  {
    if (user == address(0)) {
      return (false, "Invalid address");
    }

    return (true, "Verified");
  }
}
```

### Non EVM Compatible Blockchains

Currently, We do not support non EVM compatible blockchains. Please refer to
[off-chain verfication.](/docs/products/web3-task-verification/apis)

---

# Binance Web3 ON-Chain API Specification

## Web3 API description

- Binance's Partners need to follow the API specification in this doc in order to integrate with
  Binance.

## API Specification​

### EVM Compatible Blockchains

#### VerificationProvider

```solidity
abstract contract VerificationProvider {
  // verify is to check if the user is verified in the partner's system
  function verify(address addr) external view virtual returns (bool pass, string memory message);
}
```

You are required to implement the `VerificationProvider` contract in your smart contract. The
`verify` function should return `true` if the verification is successful, otherwise `false`. The
`message` should contain the reason for the failure.

#### Example

```solidity
contract Example is VerificationProvider {
  function verify(address user) external view override returns (bool pass, string memory message)
  {
    if (user == address(0)) {
      return (false, "Invalid address");
    }

    return (true, "Verified");
  }
}
```

### Non EVM Compatible Blockchains

Currently, We do not support non EVM compatible blockchains. Please refer to
[off-chain verfication.](/docs/products/web3-task-verification/apis)