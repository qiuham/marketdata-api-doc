---
api_type: reference
source_type: llms_txt
version: ''
scope: crypto
asset_class: prediction_market
domain: exchanges
provider: polymarket
provider_name: Polymarket
product: api
product_id: polymarket
source_url: 'https://docs.polymarket.com/cn/trading/market-making'
updated_at: 2026-11-13
---

# 做市

> 在 Polymarket 上运行做市系统的指南。

做市商（MM）通过持续挂出买单和卖单来提供流动性。通过对市场双边报价，
做市商让其他交易者更容易成交，并在承担相应风险的同时力求赚取价差。

在 Polymarket 上，做市商能够增加订单簿深度、缩小价差、促进价格发现，
并在市场状况变化时承接交易流量。

> [!NOTE]
>
> 正在构建一个为用户路由订单的产品？请参阅[构建者
> 计划](https://docs.polymarket.com/cn/programs/builders/overview.md)。本页面向使用自有账户提供
> 流动性的交易者。

## 设置做市账户

在为市场报价之前，请先完成以下账户级要求。

**1. 连接账户**

创建或连接用于持有资金、仓位和订单的钱包，然后对集成进行身份验证。
有关支持的工作流，请参阅[钱包与身份验证](https://docs.polymarket.com/cn/trading/wallets-auth.md)。

**2. 为钱包充值**

钱包需要在 Polygon 上持有 pUSD 才能交易。如需存入其他受支持资产或
从其他网络转入资金，请使用[跨链桥](https://docs.polymarket.com/cn/trading/bridge/deposit.md)。

**3. 设置交易授权**

授权交易结果代币或持仓所需的合约。请参阅[设置交易
授权](https://docs.polymarket.com/cn/trading/wallets-auth.md#设置交易授权)。

## 报价与管理订单

### 构建双边报价

做市商围绕其公允价值维护买单和卖单，让其他交易者能够双向成交。
中间价反映当前订单簿状况，但报价策略仍需判断它是否代表公允价值，
以及围绕该价格承担多少风险。

在二元市场中，互补结果提供了另一种表达双边交易的方式。例如，
以 `0.48` 买入 NO，在经济效果上等同于以 `0.52` 卖出 YES。

提交报价前，请确认市场正在接受订单，并验证当前最小价格增量和
最小订单规模。有关这些约束，请参阅[市场详情](https://docs.polymarket.com/cn/market-data/market-details.md)。

### 选择订单类型

根据策略需要实现的目标选择订单类型：

| 类型 | 行为 | 适用场景 |
| - | - | - |
| 取消前有效（GTC） | 挂在订单簿上，直到成交或取消 | 被动报价的默认选择 |
| 指定日期前有效（GTD） | 挂在订单簿上，直到成交、取消或到期 | 让被动报价在已知时间到期 |
| 全部成交或取消（FOK） | 立即全部成交，否则取消 | 不接受部分成交时立即再平衡 |
| 部分成交后取消（FAK） | 立即成交可用数量，并取消剩余部分 | 允许部分成交时立即再平衡 |

GTC 和 GTD 是被动做市的主要订单类型。当订单必须增加流动性而不能
立即成交时，请添加[仅挂单选项](https://docs.polymarket.com/cn/trading/place-orders.md#仅挂单订单)。
FAK 和 FOK 是市价单用于立即再平衡的执行类型。

### 提交与维护订单

将相关价格档位作为[批次](https://docs.polymarket.com/cn/trading/place-orders.md#批量提交订单)
提交，以降低提交延迟。每个订单都会独立评估，因此应检查每项结果，
不要把整个批次视为一次统一的成功或失败。有关完整的订单工作流，
请参阅[下单](https://docs.polymarket.com/cn/trading/place-orders.md)。

提交后，报价会成为挂在订单簿上的订单。订单无法原地修改，因此更改
报价需要取消现有订单并提交替代订单：

* 当公允价值、库存或市场约束发生变化时，取消并替换未成交订单。
* 使用[实时市场数据](https://docs.polymarket.com/cn/market-data/realtime-data.md#市场数据流)保持本地订单簿最新。
* 通过[实时订单更新](https://docs.polymarket.com/cn/trading/realtime-order-updates.md)监控成交和订单变化。
* 重新连接后，在恢复策略前[获取未成交订单和近期
  交易](https://docs.polymarket.com/cn/trading/manage-orders.md)。

## 管理库存

库存是通过交易积累的结果持仓敞口。每次成交都会改变该敞口，以及可用于
新订单的 pUSD 或结果持仓，因此每项定价和规模决策都必须考虑库存。

买单使用可用 pUSD，卖单则需要相应的结果持仓。拆分 pUSD 会创建一组完整
结果持仓。合并完整持仓会返还 pUSD。市场结算后，赎回获胜持仓会释放
其价值。有关这些工作流，请参阅[管理持仓](https://docs.polymarket.com/cn/trading/positions/manage.md)。

### 库存策略

| 阶段 | 指南 |
| - | - |
| 报价前 | 估算预期订单规模，并准备足够的 pUSD 和结果持仓。确认所需交易授权已就绪。 |
| 交易期间 | 按市场和结果跟踪敞口。调整报价价格或规模以减小失衡，在结果持仓不足时拆分更多 pUSD，并合并完整持仓以释放资金。 |
| 退出时 | 取消该市场的剩余订单，合并不再需要的完整持仓，并有意识地保留或减少剩余方向性敞口。 |
| 结算后 | 确认市场已结算，赎回获胜仓位，并将释放的资金返还给策略。 |

多结果事件使用[负风险市场](https://docs.polymarket.com/cn/concepts/negative-risk.md)，这会改变完整持仓的
创建和合并方式。规划库存操作时，请考虑市场类型。

## 最佳实践

使用以下做法保持报价及时，并限制可避免的执行风险。

### 报价管理

* **双边报价** — 同时挂出买单和卖单，为两个方向提供流动性。
* **根据库存调整** — 根据当前仓位调整报价价格以管理敞口。
* **取消过时报价** — 市场状况变化时立即撤回订单。
* **对事件使用 GTD** — 在已知催化事件前让报价到期，以避免过时敞口。

### 延迟

* **批量提交订单** — 通过[单个请求](https://docs.polymarket.com/cn/trading/place-orders.md#批量提交订单)
  提交相关报价。
* **使用实时数据** — 订阅[市场更新](https://docs.polymarket.com/cn/market-data/realtime-data.md#市场数据流)，
  而不是轮询。

### 风险控制

* **设置规模限制：** 报价前检查结果持仓余额，不要超过可用库存。
* **使用价格保护** — 根据订单簿中间价验证价格，并拒绝异常值。
* **添加紧急停止机制** — 当错误或仓位限制要求策略停止时，
  [取消所有未成交订单](https://docs.polymarket.com/cn/trading/manage-orders.md#取消所有订单)。
* **监控成交** — 订阅[实时订单更新](https://docs.polymarket.com/cn/trading/realtime-order-updates.md)以跟踪执行。

## 计划与激励

除了通过成交获取的价差外，符合条件的做市活动还可通过两个独立计划获得激励。

> [card] [流动性奖励](https://docs.polymarket.com/cn/programs/liquidity-rewards.md)
>
> 通过在激励市场中维持符合条件的挂单流动性来获得奖励。

> [card] [挂单返佣](https://docs.polymarket.com/cn/programs/maker-rebates.md)
>
> 当挂单流动性在符合条件且启用手续费的市场中成交时获得返佣。

两个计划的资格、计算方式和支付方式各不相同。请参阅相应计划页面了解
当前条款。

## 支持

如需做市商入驻和支持，请联系
[support@polymarket.com](mailto:support@polymarket.com)。


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
