---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/web3-connect/change-log
api_type: Changelog
updated_at: 2026-11-21 18:27:04.747560
---

# Change Log

## 2026-10-30

- Breaking change:
  - Deprecated and removed `getDeeplink` from the Binance Web3 Connect EVM provider docs. The method
    generated a DeepLink (`bnc`) and universal link (`http`) that open a DApp in the Binance DApp
    browser. Externally supplied DeepLinks can no longer open the DApp browser, so the method is no
    longer exposed. Integrations that still call `getDeeplink` from `@binance/w3w-utils` must stop
    using it.

---

# Change Log

## 2026-10-30

- Breaking change:
  - Deprecated and removed `getDeeplink` from the Binance Web3 Connect EVM provider docs. The method
    generated a DeepLink (`bnc`) and universal link (`http`) that open a DApp in the Binance DApp
    browser. Externally supplied DeepLinks can no longer open the DApp browser, so the method is no
    longer exposed. Integrations that still call `getDeeplink` from `@binance/w3w-utils` must stop
    using it.