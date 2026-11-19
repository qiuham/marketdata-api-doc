---
exchange: binance
source_url: https://developers.binance.com/en/docs/sdks-tools/integrations/skills-hub
api_type: Guide
updated_at: 2026-11-19 18:28:43.232816
---

# Binance Skills Hub

The Binance Skills Hub is an open marketplace of AI agent skills that give any LLM-powered agent
native access to Binance crypto capabilities — token search, on-chain trading, wallet tracking,
smart-money signals, and DeFi protocol interactions.

Skills are framework-agnostic and work with Claude Code, LangChain, CrewAI, OpenClaw, and custom
agent stacks.

For the full skill catalogue, installation options, authentication setup, and contribution
guidelines, see the [binance-skills-hub](https://github.com/binance/binance-skills-hub) repository
on GitHub.

## How it works

Each skill is a self-contained module that exposes a set of capabilities an AI agent can invoke
through natural language. Skills follow the
[Model Context Protocol (MCP)](https://modelcontextprotocol.io/) standard, so any MCP-compatible
agent can discover and call them without custom integration code.

Skills are split into two categories:

- **Read-only skills** — query market data, wallet balances, token info, trending tokens,
  smart-money activity, DeFi protocol stats, and trading signals
- **Read + Write skills** — execute on-chain operations such as token transfers, swaps, and limit
  orders via the Agentic Wallet

The hub is open source and community-extensible — anyone can contribute new skills by following the
repository's contribution guide.

## Supported environments

- Node.js 22+
- Any MCP-compatible AI agent (Claude Code, OpenClaw, custom clients)
- Python agents via LangChain / CrewAI adapters

## Getting started

Install skills from the hub:

```bash
npx skills add https://github.com/binance/binance-skills-hub
```

Refer to the repository README for authentication setup, available skills, and usage examples.

## Typical use cases

- Adding crypto market data and trading capabilities to any AI agent
- Building autonomous trading bots with natural-language interfaces
- Monitoring wallet balances and smart-money flows from an agent
- Integrating DeFi analytics into research or reporting workflows
- Prototyping agent-driven strategies without writing API integration code

---

# Binance 技能中心（Skills Hub）

Binance Skills Hub 是一个开放的 AI
Agent 技能市场，可让任何 LLM 驱动的 Agent 原生访问币安加密能力——代币搜索、链上交易、钱包追踪、聪明钱信号和 DeFi 协议交互。

Skills 与框架无关，可配合 Claude Code、LangChain、CrewAI、OpenClaw 及自定义 Agent 架构使用。

如需查看完整技能目录、安装选项、认证配置及贡献指南，请访问 GitHub 上的
[binance-skills-hub](https://github.com/binance/binance-skills-hub) 仓库。

## 工作原理

每个 Skill 是一个独立模块，暴露一组 AI Agent 可通过自然语言调用的能力。Skills 遵循
[Model Context Protocol (MCP)](https://modelcontextprotocol.io/)
标准，任何兼容 MCP 的 Agent 无需自定义集成代码即可发现并调用。

Skills 分为两类：

- **只读技能** — 查询行情数据、钱包余额、代币信息、热门代币、聪明钱动态、DeFi 协议数据及交易信号
- **读写技能** — 通过 Agentic Wallet 执行链上操作，如代币转账、兑换和限价单

Skills Hub 为开源项目，支持社区扩展——任何人都可按照仓库的贡献指南提交新技能。

## 支持的环境

- Node.js 22+
- 任何兼容 MCP 的 AI Agent（Claude Code、OpenClaw、自定义客户端）
- 通过 LangChain / CrewAI 适配器支持 Python Agent

## 快速开始

从 Hub 安装技能：

```bash
npx skills add https://github.com/binance/binance-skills-hub
```

认证配置、可用技能列表及使用示例请参阅仓库 README。

## 典型使用场景

- 为任意 AI Agent 添加加密行情与交易能力
- 构建具有自然语言界面的自主交易机器人
- 通过 Agent 监控钱包余额与聪明钱动态
- 将 DeFi 分析集成到研究或报告工作流
- 无需编写 API 集成代码即可快速原型化 Agent 交易策略