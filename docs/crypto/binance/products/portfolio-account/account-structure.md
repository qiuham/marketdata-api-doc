---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/portfolio-account/account-structure
api_type: Guide
updated_at: 2026-11-27 18:30:15.036409
---

# Account Structure

Portfolio Account uses a three-level model built on the Binance sub-account system.

```
Manager Parent Account
├── Portfolio Account #1              ← holds investor capital, NAV struck here
│   ├── Trading Sub-account 1         ← trading happens here
│   ├── Trading Sub-account 2
│   └── ... (5 by default)
└── Portfolio Account #2 ... up to 5
```

| Level                  | Role                                                                                                                                                          |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Manager Parent Account | The trading team's top-level account. Holds up to 5 Portfolio Accounts. Issues the API key used for all trading-team portfolio endpoints.                     |
| Portfolio Account      | One strategy. Receives investor subscription capital, holds the NAV series, and is the account from which redemptions settle. No trading occurs here.         |
| Trading Sub-account    | Where the team executes. 5 per Portfolio Account by default. Each has its own API key and trades through standard Binance spot, margin and futures endpoints. |

Investors hold allocations, not accounts. An investor is bound to a Portfolio Account and holds a
number of allocations in it. Position value is allocations × `navPerAllocation`.

Asset movement is closed. Capital can move only between a Portfolio Account and its own linked
Trading Sub-accounts. External transfers and withdrawals from these accounts are not permitted. All
assets remain in Binance custody throughout.

---

# 账户结构

投资组合账户采用三层模型，建立在币安子账户体系之上。

```
管理人母账户
├── 投资组合账户 #1                 ← 持有投资人资金，在此计算净值
│   ├── 交易子账户 1                ← 在此进行交易
│   ├── 交易子账户 2
│   └── ...（默认 5 个）
└── 投资组合账户 #2 ... 最多 5 个
```

| 层级         | 角色                                                                                                                    |
| ------------ | ----------------------------------------------------------------------------------------------------------------------- |
| 管理人母账户 | 交易团队的顶层账户，最多持有 5 个投资组合账户，并签发所有交易团队接口使用的 API Key。                                   |
| 投资组合账户 | 对应一个策略。接收投资人申购资金，持有净值序列，并作为赎回的结算账户。该账户内不进行交易。                              |
| 交易子账户   | 交易团队执行交易的账户。每个投资组合账户默认 5 个。每个子账户有独立的 API Key，通过标准的币安现货、杠杆和合约接口交易。 |

投资人持有的是份额，而不是账户。投资人被绑定到某个投资组合账户，并在其中持有一定数量的份额。持仓价值 = 份额 ×
`navPerAllocation`。

资产流转是封闭的。资金只能在投资组合账户与其关联的交易子账户之间划转，这些账户不允许对外转账或提现。所有资产始终由币安托管。