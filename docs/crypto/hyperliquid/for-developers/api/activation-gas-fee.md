---
exchange: hyperliquid
source_url: https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/api/activation-gas-fee
api_type: REST
updated_at: 2026-05-27 18:51:15.677760
---

# Activation gas fee

New HyperCore accounts require 1 quote token (e.g., 1 USDC, 1 USDT, or 1 USDH) of fees for the first transaction which has the new account as destination address. This applies regardless of the asset being transfered to the new account. 

Unactivated accounts cannot send CoreWriter actions. Contract deployers who do not want this one-time behavior could manually send an activation transaction to the EVM contract address on HyperCore.