---
exchange: bitget
source_url: https://www.bitget.com/docs/uta/uta-intro
api_type: Guide
updated_at: 2026-11-18 08:36:47.213579
---

# Unified Trading Account

The unified account is a next-generation trading system introduced by Bitget, designed to allow users to trade spot and various derivatives using multiple crypto assets within a single account. This system simplifies the trading process by eliminating the need for fund transfers between different accounts. Moreover, profits and losses across different products can be calculated and offset together, enhancing capital efficiency.

## Comparison of Account Mode

The Unified Account provides users with three new account modes to satisfy the trading preferences and needs of different users: Spot + Isolated Margin Mode, Stablecoin Margin Mode, and Multi-Asset Margin Mode.<br/>
*Note: These modes were previously named Isolated margin mode, Basic Mode, and Advanced Mode respectively. The API enum values (`isolated` / `basic` / `advanced`) remain unchanged.*

| Account mode | Feature | Available products | Margin support |
|--------------|---------|-------------------|----------------|
| Spot + Isolated Margin Mode | Each position carries independent risk, and PnL from one position does not affect others | 1. Spot<br/>2. USDT-M Futures (isolated margin)<br/>3. USDC-M Futures (isolated margin) | Collateral settings are not supported |
| Stablecoin Margin Mode | Improves capital efficiency, but only supports stablecoins as margin (no multi-asset collateral). | 1. Spot<br/>2. USDT-M Futures (cross/isolated margin)<br/>3. USDC-M Futures (cross/isolated margin) | USDT- and USDC-margined pairs share the same margin pool. Collateral settings are not supported |
| Multi-Asset Margin Mode | Multiple assets can be used as margin based on their respective collateral ratios. Supports cross-currency risk hedging and maximizes capital efficiency. | 1. Spot<br/>2. Spot margin<br/>3. USDT-M Futures (cross/isolated margin)<br/>4. USDC-M Futures (cross/isolated margin)<br/>5. Coin-M Futures (cross/isolated margin) | Collateral settings are supported. |

In **Multi-Asset Margin Mode**, all assets across product types can be used as shared margin, and PnL can be mutually offset.
Please refer to [this document](https://www.bitget.com/support/articles/12560603839176) for details.

## Asset-related Terminology

| Term | Explanation |
|:-----|:------------|
| Equity | The total equity of a specific coin in the cross margin account.<br/>_Coin equity = Balance + Frozen margin + unrealized PnL_ |
| Balance | The balance of a specific coin in the account. |
| Available | The current available balance of a specific coin in the account for opening positions.<br/>_Available = Balance + unrealized PnL_ |
| UnrealisedPnL | The total profits of all futures positions settled in a specific coin in the account.<br/>_Unrealized profits = Profits of USDT-M perpetual futures positions in cross margin mode + profits of USDC-M perpetual futures positions in cross margin mode + profits of coin-M perpetual futures positions in cross margin mode_ |
| Debt | Debt = ABS(min(balance + unrealized PnL, 0)) |
| Account equity | The net value of all coin assets in the account converted into fiat currency.<br/>_Account equity = sum (coin equity × coin in USD price)_ |
| Maintenance margin | The total maintenance margin of all cross margin positions in the account.<br/>_Maintenance margin = Sum[quantity of coin in cross margin positions × coin price]_<br/>_Maintenance margin = Position value × maintenance margin rate_ |
| Margin rate | A risk measurement indicator for cross margin accounts.<br/>_Cross margin account's margin ratio = (maintenance margin + partial liquidation transaction fees) ÷ Account equity_.<br/>Both maintenance margin and partial liquidation transaction fees are calculated by adding the position size and the open order size. |

---

# 统一账户

统一账户（Unified Account）是 Bitget 面向广大用户推出的新一代交易系统，支持在一个账户中使用多币种资产同时交易现货和各类衍生品。这将会为用户的交易提供极大的便利，不再需要在多个账户之间进行资金划转，且不同业务线的盈亏可以互相抵消，有效地提升了用户的资金利用率。

## 账户模式

统一账户为用户提供了三种新的账户模式：现货+逐仓模式、稳定币保证金模式和多币种保证金模式，以满足不同用户的交易偏好与需求。

*注：上述模式原名称分别为逐仓模式、基础模式、进阶模式，API 枚举值（`isolated` / `basic` / `advanced`）保持不变。*

| 账户模式 | 特性 | 可交易产品 | 保证金支持 |
|----------|------|-----------|-----------|
| 现货+逐仓模式 | 各交易仓位风险独立、相互隔离；单仓位盈亏不影响其他仓位 | 1. 现货<br/>2. USDT 逐仓合约<br/>3. USDC 逐仓合约 | 不支持抵押品设置 |
| 稳定币保证金模式 | 提升资金利用率；但保证金仍限定在稳定币体系内；不支持多币种资产作为统一抵押 | 1. 现货<br/>2. USDT 全/逐仓合约<br/>3. USDC 全/逐仓合约 | USDT 与 USDC 计价产品共用同一保证金池；不支持抵押品设置 |
| 多币种保证金模式 | 多币种资产按折扣率折算为保证金；支持跨币种风险对冲；资金利用率最高 | 1. 现货<br/>2. 现货杠杆<br/>3. USDT 全/逐仓合约<br/>4. USDC 全/逐仓合约<br/>5. 币本位全/逐仓合约 | 支持抵押品设置 |

*多币种保证金模式下，所有产品类型的资产均可作为共享保证金使用，且盈亏可相互抵消，具体请参考 [此文档](https://www.bitget.com/zh-CN/support/articles/12560603839176)。*

## 资产相关名词

| 名词 | 解释 |
|:-----|:-----|
| 权益 | 跨保证金账户中特定币种的总权益。币种权益 = 余额 + 冻结保证金 + 未实现盈亏 |
| 余额 | 账户中特定币种的余额 |
| 可用 | 账户中特定币种用于开仓的当前可用余额。可用 = 余额 + 未实现盈亏 |
| 未实现盈亏 | 账户中以特定币种结算的所有合约仓位的总盈亏。未实现盈亏 = USDT 合约在全仓模式下的盈亏 + USDC 合约在全仓模式下的盈亏 + 币本位合约在全仓模式下的盈亏 |
| 负债 | 负债 = ABS(min(余额 + 未实现盈亏, 0)) |
| 账户权益 | 账户中所有币种资产转换为法币后的净值。账户权益 = sum (币种权益 × 币种的美元价格) |
| 维持保证金 | 账户中所有全仓仓位的总维持保证金。维持保证金 = Sum[全仓仓位中币种的数量 × 币种价格]；维持保证金 = 仓位价值 × 维持保证金率 |
| 保证金率 | 用于衡量全仓账户风险的指标。全仓账户的保证金率 = (维持保证金 + 部分强平交易手续费) ÷ 账户权益。维持保证金和部分强平交易手续费都通过将仓位大小和挂单大小相加来计算 |