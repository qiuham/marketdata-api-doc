# MarketData API Docs

多市场交易、行情和极速柜台 API 文档库。这个仓库参考 `crypto-api-docs` 的组织方式，但抽象为更大的接口文档体系：`cn`、`us`、`crypto` 作为顶层范围；传统市场在范围下按资产类别组织，crypto 直接按提供方组织。

## 设计原则

- **范围优先**：顶层按 `cn`、`us`、`crypto` 组织；`cn` / `us` 下面再按 `stock`、`futures`、`options` 等资产类别分层。
- **路径保持短**：传统市场路径采用 `范围/资产/提供方/产品`，crypto 路径采用 `crypto/提供方`；业务类型如 `gateways`、`exchanges`、`brokers`、`data-vendors` 放在元数据和索引里。
- **产品独立**：每个接入对象都有独立 `product_id`，例如 `zhongtai-xtp`、`zhongtai-xtppro`。
- **文档统一**：落地为 Markdown，并使用 YAML frontmatter 记录来源、范围、资产类别、提供方、产品、接口类型和更新时间。
- **索引友好**：每个产品生成独立 JSON 索引，同时生成全局 `index/catalog.json`，方便 AI、搜索和后续工具读取。
- **采集可插拔**：公开网页、SDK、PDF、Word、头文件、本地手工文档都通过 adapter 或 ingest 流程进入同一套结构。

## 覆盖范围

> 此表由 `src/utils/readme_updater.py` 根据 `config/products/*.yaml` 和 `index/**/*.json` 自动生成。

| 范围 | 提供方 | 产品 | 状态 | 文档数量 | 最后更新 |
|------|--------|------|------|----------|----------|
| cn | 中泰证券 | [中泰 XTP 3.0](./docs/cn/stock/zhongtai/xtp/) | ✅ | 36 | 2026-07-06 |
| cn | 中泰证券 | [中泰 XTP Pro](./docs/cn/stock/zhongtai/xtppro/) | ✅ | 22 | 2026-07-03 |
| crypto | Binance | [Binance](./docs/crypto/binance/) | ✅ | 825 | 2026-07-01 |
| crypto | Bybit | [Bybit](./docs/crypto/bybit/) | ✅ | 501 | 2026-07-09 |
| crypto | Coinbase | [Coinbase](./docs/crypto/coinbase/) | ✅ | 75 | 2026-07-09 |
| crypto | Gate.io | [Gate.io](./docs/crypto/gateio/) | ✅ | 66 | 2026-05-27 |
| crypto | Hyperliquid | [Hyperliquid](./docs/crypto/hyperliquid/) | ✅ | 34 | 2026-07-09 |
| crypto | Kraken | [Kraken](./docs/crypto/kraken/) | ✅ | 243 | 2026-07-09 |
| crypto | OKX | [OKX](./docs/crypto/okx/) | ✅ | 513 | 2026-07-09 |

## 快速开始

```bash
# 查看产品清单
PYTHONPATH=. python src/main.py list

# 爬取单个产品
PYTHONPATH=. python src/main.py crawl -p zhongtai-xtp

# 生成全部产品索引和全局 catalog
PYTHONPATH=. python src/main.py index --all

# 刷新 README 自动内容
PYTHONPATH=. python src/main.py readme

# 校验配置、文档目录和索引
PYTHONPATH=. python src/main.py validate
```

## 项目结构

> 此结构由 `src/utils/readme_updater.py` 根据当前仓库文件自动生成。

```
marketdata-api-doc/
├── .github/
│   └── workflows/        # GitHub Actions
│       ├── crawl-docs.yml
│       └── validate.yml
├── config/
│   ├── scopes/           # cn / us / crypto 等顶层范围
│   │   ├── cn.yaml
│   │   ├── crypto.yaml
│   │   └── us.yaml
│   ├── products/         # 接入产品配置
│   │   ├── binance.yaml
│   │   ├── bybit.yaml
│   │   ├── coinbase.yaml
│   │   ├── gateio.yaml
│   │   ├── hyperliquid.yaml
│   │   ├── kraken.yaml
│   │   ├── okx.yaml
│   │   ├── zhongtai-xtp.yaml
│   │   └── zhongtai-xtppro.yaml
│   └── legacy/           # 兼容旧项目的源站配置
│       └── crypto/
│           ├── binance.yaml
│           ├── bybit.yaml
│           ├── coinbase.yaml
│           ├── gateio.yaml
│           ├── hyperliquid.yaml
│           ├── kraken.yaml
│           └── okx.yaml
├── docs/                 # Markdown 文档
│   ├── cn/
│   │   └── stock/
│   │       └── zhongtai/
│   │           ├── xtp/                            # 36 Markdown docs
│   │           └── xtppro/                         # 22 Markdown docs
│   ├── crypto/
│   │   ├── binance/                                # 825 Markdown docs
│   │   ├── bybit/                                  # 501 Markdown docs
│   │   ├── coinbase/                               # 75 Markdown docs
│   │   ├── gateio/                                 # 66 Markdown docs
│   │   ├── hyperliquid/                            # 34 Markdown docs
│   │   ├── kraken/                                 # 243 Markdown docs
│   │   └── okx/                                    # 513 Markdown docs
│   └── us/
├── index/                # JSON 索引（供 AI 读取）
│   ├── catalog.json
│   ├── cn/stock/zhongtai-xtp.json
│   ├── cn/stock/zhongtai-xtppro.json
│   ├── crypto/binance.json
│   ├── crypto/bybit.json
│   ├── crypto/coinbase.json
│   ├── crypto/gateio.json
│   ├── crypto/hyperliquid.json
│   ├── crypto/kraken.json
│   └── crypto/okx.json
├── src/
│   ├── adapters/         # 采集/导入适配器
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── crypto_legacy.py
│   │   ├── zhongtai_xtp.py
│   │   └── zhongtai_xtppro.py
│   ├── utils/            # 浏览器、Markdown、索引、路径、README 工具
│   │   ├── __init__.py
│   │   ├── browser.py
│   │   ├── config.py
│   │   ├── indexer.py
│   │   ├── markdown.py
│   │   ├── path_generator.py
│   │   └── readme_updater.py
│   └── main.py
├── requirements.txt
└── README.md
```

## Frontmatter 规范

每篇文档都应该带上前置信息，至少包含：

```yaml
id: zhongtai-xtp-2056206185257816066
scope: cn
asset_class: stock
domain: gateways
provider: zhongtai
product: xtp
product_id: zhongtai-xtp
api_type: market_data
source_type: http_api
source_url: https://xtp.zts.com.cn/jeecg-boot/xtp/tree/getTreeData?id=2056206185257816066
version: XTP 3.0
updated_at: 2026-05-18
```

## 已接入范围

- `cn/stock/zhongtai/xtp`：中泰 XTP 3.0，A 股极速交易柜台 API 文档。
- `cn/stock/zhongtai/xtppro`：中泰 XTP Pro，A 股极速交易柜台 Pro API 文档。
- `crypto/*`：已迁移 Binance、Bybit、Coinbase、Gate.io、Hyperliquid、Kraken、OKX。
- 后续可以按同一结构扩展到 `cn/futures`、`us/stock`、行情数据供应商和内部网关。
