# MarketData API Docs

多市场交易、行情和极速柜台 API 文档库。这个仓库参考 `crypto-api-docs` 的组织方式，但抽象为更大的接口文档体系：`cn`、`us`、`crypto` 作为顶层范围；传统市场在范围下按资产类别组织，crypto 直接按提供方组织。

## 设计原则

- **范围优先**：顶层按 `cn`、`us`、`crypto` 组织；`cn` / `us` 下面再按 `stock`、`futures`、`options` 等资产类别分层。
- **路径保持短**：传统市场路径采用 `范围/资产/提供方/产品`，crypto 路径采用 `crypto/提供方`；业务类型如 `gateways`、`exchanges`、`brokers`、`data-vendors` 放在元数据和索引里。
- **产品独立**：每个接入对象都有独立 `product_id`，例如 `binance`、`okx`。
- **文档统一**：落地为 Markdown，并使用 YAML frontmatter 记录来源、范围、资产类别、提供方、产品、接口类型和更新时间。
- **索引友好**：每个产品生成独立 JSON 索引，同时生成全局 `index/catalog.json`，方便 AI、搜索和后续工具读取。
- **采集可插拔**：公开网页、SDK、PDF、Word、头文件、本地手工文档都通过 adapter 或 ingest 流程进入同一套结构。

## 覆盖范围

> 此表由 `src/utils/readme_updater.py` 根据 `config/products/*.yaml` 和 `index/**/*.json` 自动生成。

| 范围 | 提供方 | 产品 | 状态 | 文档数量 | 最后更新 |
|------|--------|------|------|----------|----------|
| crypto | Binance | [Binance](./docs/crypto/binance/) | ✅ | 164 | 2026-11-13 |
| crypto | Bybit | [Bybit](./docs/crypto/bybit/) | ✅ | 546 | 2026-11-13 |
| crypto | Coinbase | [Coinbase](./docs/crypto/coinbase/) | ✅ | 78 | 2026-11-13 |
| crypto | Gate.io | [Gate.io](./docs/crypto/gateio/) | ✅ | 72 | 2026-11-13 |
| crypto | Hyperliquid | [Hyperliquid](./docs/crypto/hyperliquid/) | ✅ | 36 | 2026-11-13 |
| crypto | Kraken | [Kraken](./docs/crypto/kraken/) | ✅ | 447 | 2026-11-13 |
| crypto | OKX | [OKX](./docs/crypto/okx/) | ✅ | 519 | 2026-11-13 |
| crypto | Polymarket | [Polymarket](./docs/crypto/polymarket/) | ✅ | 561 | 2026-11-13 |

## 快速开始

```bash
# 查看产品清单
PYTHONPATH=. python src/main.py list

# 爬取单个产品
PYTHONPATH=. python src/main.py crawl -p okx

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
│   │   └── polymarket.yaml
│   └── legacy/           # 兼容旧项目的源站配置
│       └── crypto/
│           ├── binance.yaml
│           ├── bybit.yaml
│           ├── coinbase.yaml
│           ├── gateio.yaml
│           └── okx.yaml
├── docs/                 # Markdown 文档
│   └── crypto/
│       ├── binance/                                # 164 Markdown docs
│       ├── bybit/                                  # 546 Markdown docs
│       ├── coinbase/                               # 78 Markdown docs
│       ├── gateio/                                 # 72 Markdown docs
│       ├── hyperliquid/                            # 36 Markdown docs
│       ├── kraken/                                 # 447 Markdown docs
│       ├── okx/                                    # 519 Markdown docs
│       └── polymarket/                             # 561 Markdown docs
├── index/                # JSON 索引（供 AI 读取）
│   ├── catalog.json
│   ├── crypto/binance.json
│   ├── crypto/bybit.json
│   ├── crypto/coinbase.json
│   ├── crypto/gateio.json
│   ├── crypto/hyperliquid.json
│   ├── crypto/kraken.json
│   ├── crypto/okx.json
│   └── crypto/polymarket.json
├── src/
│   ├── adapters/         # 采集/导入适配器
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── crypto_legacy.py
│   │   └── llms_txt.py
│   ├── utils/            # 浏览器、Markdown、索引、路径、README 工具
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── indexer.py
│   │   ├── markdown.py
│   │   ├── path_generator.py
│   │   ├── quality.py
│   │   └── readme_updater.py
│   └── main.py
├── requirements.txt
└── README.md
```

## Frontmatter 规范

每篇文档都带上前置信息。例如 `docs/crypto/okx/affiliate.md`：

```yaml
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#affiliate
anchor_id: affiliate
api_type: API
updated_at: 2026-11-11 14:17:18.632567
```

## 采集方式

| 方式 | 用在哪 | 说明 |
|---|---|---|
| `llms_txt` | Hyperliquid、Kraken、Polymarket | 文档站每页加 `.md` 就是原文（GitBook、Mintlify）。页面列表取自 `llms.txt`，`llms.txt` 不全时取 `sitemap.xml`（Kraken）。直接 HTTP 下载，不开浏览器；可以顺带收 OpenAPI / AsyncAPI 规格（存在 `_specs/`） |
| `crypto_legacy` | 其余几家 | 用 `agent-browser` 打开网页取正文。多标签页并发时，存盘前核对当前标签页的网址，对不上就重开，还不对就跳过这一页 |

新加一家：文档站有 `llms.txt` 的，写一份 `config/products/<id>.yaml`（`adapter: llms_txt`）就够了，例子见 `config/products/polymarket.yaml`。

## 质量检查

爬完每一家都查一遍（`src/utils/quality.py`），出现下面任何一种就判这一家抓坏了，把它的目录退回上一次提交，其他家照常提交：

- 有 `# Untitled` 页（页面没打开）；
- 空页超过 5%；
- 内容完全相同、文件名不同的文件超过 2%（多标签页读错了标签）。

`python src/main.py validate` 也做同样的检查：默认只警告（抓不了的旧数据不挡别家提交），加 `--strict` 判失败。

## 已接入范围

- `crypto/*`：Binance、Bybit、Coinbase、Gate.io、Hyperliquid、Kraken、OKX、Polymarket。
- 后续可以按同一结构扩展到 `cn/futures`、`us/stock`、行情数据供应商和内部网关。
