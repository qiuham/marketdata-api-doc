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
source_url: 'https://docs.polymarket.com/cn/resources/contracts'
updated_at: 2026-11-13
---

# 合约

> Polymarket 合约地址、审计和源代码仓库

以下合约部署在 Polygon 主网，chain ID 为 `137`。如果合约分别列出 proxy 和 implementation 地址，请使用 proxy 地址。

## 共用抵押品与钱包

pUSD 抵押品系统和账户钱包支持两种持仓系统。CTF 抵押品适配器在 pUSD 与 CTF 合约使用的抵押品之间转移价值。

### 抵押品

| 合约 | 地址 |
| - | - |
| pUSD CollateralToken proxy | [`0xC011a7E12a19f7B1f670d46F03B03f3342E82DFB`](https://polygonscan.com/address/0xC011a7E12a19f7B1f670d46F03B03f3342E82DFB) |
| pUSD CollateralToken implementation | [`0xCe84E053301A82937F90ee2C2c1889cAb1db25dE`](https://polygonscan.com/address/0xCe84E053301A82937F90ee2C2c1889cAb1db25dE) |
| CollateralOnramp | [`0x93070a847efEf7F70739046A929D47a521F5B8ee`](https://polygonscan.com/address/0x93070a847efEf7F70739046A929D47a521F5B8ee) |
| CollateralOfframp | [`0x2957922Eb93258b93368531d39fAcCA3B4dC5854`](https://polygonscan.com/address/0x2957922Eb93258b93368531d39fAcCA3B4dC5854) |
| PermissionedRamp | [`0xebC2459Ec962869ca4c0bd1E06368272732BCb08`](https://polygonscan.com/address/0xebC2459Ec962869ca4c0bd1E06368272732BCb08) |
| CtfCollateralAdapter | [`0xAdA100Db00Ca00073811820692005400218FcE1f`](https://polygonscan.com/address/0xAdA100Db00Ca00073811820692005400218FcE1f) |
| NegRiskCtfCollateralAdapter | [`0xadA2005600Dec949baf300f4C6120000bDB6eAab`](https://polygonscan.com/address/0xadA2005600Dec949baf300f4C6120000bDB6eAab) |

### 钱包工厂合约

| 合约 | 地址 |
| - | - |
| Deposit Wallet Factory | [`0x00000000000Fb5C9ADea0298D729A0CB3823Cc07`](https://polygonscan.com/address/0x00000000000Fb5C9ADea0298D729A0CB3823Cc07) |
| Deposit Wallet Beacon | [`0x7A18EDfe055488A3128f01F563e5B479D92ffc3a`](https://polygonscan.com/address/0x7A18EDfe055488A3128f01F563e5B479D92ffc3a) |
| Gnosis Safe Factory | [`0xaacfeea03eb1561c4e67d661e40682bd20e3541b`](https://polygonscan.com/address/0xaacfeea03eb1561c4e67d661e40682bd20e3541b) |
| Polymarket Proxy Factory | [`0xaB45c5A4B0c941a2F231C04C3f49182e1A254052`](https://polygonscan.com/address/0xaB45c5A4B0c941a2F231C04C3f49182e1A254052) |

## CTF 合约

以下合约管理并交换 CTF 结果余额。

| 合约 | 地址 |
| - | - |
| Conditional Tokens | [`0x4D97DCd97eC945f40cF65F87097ACe5EA0476045`](https://polygonscan.com/address/0x4D97DCd97eC945f40cF65F87097ACe5EA0476045) |
| CTF Exchange | [`0xE111180000d2663C0091e4f400237545B87B996B`](https://polygonscan.com/address/0xE111180000d2663C0091e4f400237545B87B996B) |
| Neg Risk CTF Exchange | [`0xe2222d279d744050d28e00520010520000310F59`](https://polygonscan.com/address/0xe2222d279d744050d28e00520010520000310F59) |
| Neg Risk Adapter（CTF 负风险交易授权） | [`0xd91E80cF2E7be2e162c6513ceD06f1dD0dA35296`](https://polygonscan.com/address/0xd91E80cF2E7be2e162c6513ceD06f1dD0dA35296) |

在 CTF 负风险市场下单时，CLOB 仍会检查 Neg Risk Adapter 的 pUSD 和 Conditional
Tokens 授权。请与其他[交易授权](https://docs.polymarket.com/cn/trading/wallets-auth.md#设置交易授权)一并授予。
此 Neg Risk Adapter（`0xd91E80cF2E7be2e162c6513ceD06f1dD0dA35296`）与
NegRiskCtfCollateralAdapter（`0xadA2005600Dec949baf300f4C6120000bDB6eAab`）是不同的合约；授权
NegRiskCtfCollateralAdapter 并不会授予 Neg Risk Adapter 所需的授权。

## Polymarket Protocol V2 合约

PositionManager 管理 ERC-1155 余额。Position ID 将每项操作路由到 BinaryModule、NegRiskModule 或 CombinatorialModule。

| 合约 | Proxy | Implementation |
| - | - | - |
| PositionManager | [`0x006F54F7f9A22e0000CC2AB60031000000ae9fEF`](https://polygonscan.com/address/0x006F54F7f9A22e0000CC2AB60031000000ae9fEF) | [`0xCc5De1e9D14a7AB75E872E23FC9D605518Bac2D0`](https://polygonscan.com/address/0xCc5De1e9D14a7AB75E872E23FC9D605518Bac2D0) |
| Exchange | [`0xe3333700cA9d93003F00f0F71f8515005F6c00Aa`](https://polygonscan.com/address/0xe3333700cA9d93003F00f0F71f8515005F6c00Aa) | [`0x641b40ec414a076b9e79E703Fc7BF4EBEC248Bb7`](https://polygonscan.com/address/0x641b40ec414a076b9e79E703Fc7BF4EBEC248Bb7) |
| Router | [`0x12121212006e4CD160D18e3f00711DA5c3372600`](https://polygonscan.com/address/0x12121212006e4CD160D18e3f00711DA5c3372600) | [`0x91fA5E2F12a308A13DefdB6aaF80B71DBe9B7696`](https://polygonscan.com/address/0x91fA5E2F12a308A13DefdB6aaF80B71DBe9B7696) |
| BinaryModule | [`0x1000008dD9001B968442c1000017eaE6E0dA00Ba`](https://polygonscan.com/address/0x1000008dD9001B968442c1000017eaE6E0dA00Ba) | [`0xf6428c0B5fa9361c0708CDdb95468cf54C56e9A2`](https://polygonscan.com/address/0xf6428c0B5fa9361c0708CDdb95468cf54C56e9A2) |
| NegRiskModule | [`0x200000900045e3B6259600682756002200028933`](https://polygonscan.com/address/0x200000900045e3B6259600682756002200028933) | [`0x39a5B01a100edF811f2748aa37B1313715Ded70e`](https://polygonscan.com/address/0x39a5B01a100edF811f2748aa37B1313715Ded70e) |
| CombinatorialModule | [`0x30000034706C7d8e12009DAB006Be20000c031A8`](https://polygonscan.com/address/0x30000034706C7d8e12009DAB006Be20000c031A8) | [`0xf96968a44022B17240B42c557693E7C383d2d8a3`](https://polygonscan.com/address/0xf96968a44022B17240B42c557693E7C383d2d8a3) |

## 结算合约

### CTF

| 合约 | 地址 |
| - | - |
| UmaCtfAdapter v3.1.0 | [`0x157Ce2d672854c848c9b79C49a8Cc6cc89176a49`](https://polygonscan.com/address/0x157Ce2d672854c848c9b79C49a8Cc6cc89176a49) |
| UmaCtfAdapter v2.0.0 | [`0x6A9D222616C90FcA5754cd1333cFD9b7fb6a4F74`](https://polygonscan.com/address/0x6A9D222616C90FcA5754cd1333cFD9b7fb6a4F74) |
| UmaCtfAdapter v1.0.0 | [`0xCB1822859cEF82Cd2Eb4E6276C7916e692995130`](https://polygonscan.com/address/0xCB1822859cEF82Cd2Eb4E6276C7916e692995130) |

### Polymarket Protocol V2

OracleAggregator 从支持的 reporter 模块接收结果，并将最终结果发送给管理该 condition 的模块。

| 合约 | Proxy | Implementation |
| - | - | - |
| OracleAggregator | [`0x0A0a0A0A8B00C51b7D810501b03F230028C04a87`](https://polygonscan.com/address/0x0A0a0A0A8B00C51b7D810501b03F230028C04a87) | [`0x822e8A97AF8005073F2f6E88435D692E33ab6082`](https://polygonscan.com/address/0x822e8A97AF8005073F2f6E88435D692E33ab6082) |
| OOReporterModule | [`0x000012e0009c84078c4924fba808A41b9f67527f`](https://polygonscan.com/address/0x000012e0009c84078c4924fba808A41b9f67527f) | [`0xBd49A21677Da630fF5Efec52B7309d0Ada685d81`](https://polygonscan.com/address/0xBd49A21677Da630fF5Efec52B7309d0Ada685d81) |
| ChainlinkReporterModule | [`0xc12EC12E0000326890Ca5560dEf5EB5C22b16814`](https://polygonscan.com/address/0xc12EC12E0000326890Ca5560dEf5EB5C22b16814) | [`0x70545d95653a4a7B1c2F47f6a9383E36EaAA55b2`](https://polygonscan.com/address/0x70545d95653a4a7B1c2F47f6a9383E36EaAA55b2) |
| EOAReporterModule | [`0x8Ef9D6d668798b1f363b305D916F30739d2b0419`](https://polygonscan.com/address/0x8Ef9D6d668798b1f363b305D916F30739d2b0419) | [`0x5fe0280873f5539da12B6b5b37484E0B0c28Ab14`](https://polygonscan.com/address/0x5fe0280873f5539da12B6b5b37484E0B0c28Ab14) |

## 赎回与迁移

| 合约 | Proxy | Implementation |
| - | - | - |
| AutoRedeemer | [`0xa1200000d0002264C9a1698e001292D00E1b00af`](https://polygonscan.com/address/0xa1200000d0002264C9a1698e001292D00E1b00af) | [`0x64860bFD14fCcaAc09cd36f347784a9616AfB66C`](https://polygonscan.com/address/0x64860bFD14fCcaAc09cd36f347784a9616AfB66C) |

AutoRedeemer 支持 Conditional Tokens 和 PositionManager 中已结算的余额。CTF 到 PositionManager 的迁移由上表中的 BinaryModule 和 NegRiskModule 实现。Polymarket 必须先注册 condition 或事件，持仓者才能迁移。

用于索引赎回和迁移的事件及标识符请参阅[链上持仓数据](https://docs.polymarket.com/cn/resources/onchain-position-data.md)。

## 安全

### 审计

* [Polymarket Protocol V2 审计报告](https://github.com/Polymarket/polymarket-v2/tree/main/audit)
* [CTF Exchange 审计报告](https://github.com/Polymarket/ctf-exchange-v2/tree/main/audits)

安全漏洞可以通过 [Cantina 漏洞赏金计划](https://cantina.xyz/bounties/ff945ca2-2a6e-4b83-b1b6-7a0cd3b94bea)报告。

## 源代码

> [card] [Conditional Tokens](https://github.com/gnosis/conditional-tokens-contracts)
>
> ERC-1155 持仓和 CTF 结算

> [card] [CTF Exchange](https://github.com/Polymarket/ctf-exchange-v2)
>
> CTF 订单撮合和结算

> [card] [Polymarket Protocol V2](https://github.com/Polymarket/polymarket-v2)
>
> PositionManager、模块、路由、结算和 exchange 合约


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
