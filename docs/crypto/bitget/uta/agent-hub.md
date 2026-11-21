---
exchange: bitget
source_url: https://www.bitget.com/docs/uta/agent-hub
api_type: Guide
updated_at: 2026-11-21 19:03:02.010788
---

# Agent Hub

**Skip the exchange. Connect Agenthub, say one sentence, and an agent trades tokenized US stocks and crypto in your Bitget account from Claude, Cursor, Codex, or the Personal Agents Grok bot, Muse, and Dot.**

In Claude, Cursor, Codex, or the Personal Agents Grok bot, Muse, and Dot, connect `https://agent.bitget.com/mcp` and sign in to Bitget in the browser when the page asks. Read what it can do, then how to connect.

:::info{title="About the old version"}
The second half of this article is the old install path. That product will be maintained less and less. It is only here so people who already installed it can look up the old commands.
:::

[Landing page](https://www.bitget.com/activity-hub/agent-hub) · [API Docs](https://www.bitget.com/api-doc/common/intro) · [Telegram](https://telegram.me/+o1tYqQ_lXxllYjgy)

## Contents

```text
Bitget Agenthub
├── What you can do
├── How to connect
├── Product structure
│   ├── Agentic account
│   ├── Trading MCP
│   └── Data MCP
├── Safety
├── FAQ
└── Links
```

---

## 1. Current version (use this one)

### What you can do

:::tip{title="Who it's for"}
Agenthub **is for people who want an agent to trade crypto and tokenized US stocks:** watch the market · read the tape · place trades · manage the account · write a strategy · do research.
:::

The hard part of trading with AI is not the strategy. It is jumping back and forth: you ask the AI, then place the order yourself, then come back to the chat. Agenthub puts both steps in one place. You say one sentence. It does the rest. Market data does not need a login. Trading, account checks, and tokenized US stocks do. Sign in once in the browser.

| You say | What happens |
|-|-|
| "BTC price" · "4h candles" · "funding rate" | Live market data. No login. |
| "Market-buy 0.1 BTC" · "Open a BTC long" · "Buy a little rAAPL" | Trade crypto, or tokenized US stocks such as Apple, Tesla, and NVIDIA. Login required. |
| "Check my balance" · "Show transfers and deposits" | Account balances and funding records. Login required. |
| "When does Apple pay a dividend, and is the market closed today?" · "What is rAAPL worth?" | Dividends, market holidays, and valuation for the stock. Login required. |

---

### How to connect

Paste the text in the box below to your AI. It connects Agenthub and opens a browser so you can sign in to Bitget. You need that login to place orders and view the account. If you only want market prices this time and do not want to sign in, add this line: market data only, do not sign in yet.

:::info{title="Fastest way to start"}
Send this to your AI — it will install Agenthub:

```text title="Prompt for your AI"
Read https://www.bitget.com/support/articles/12560603894122 and finish Bitget Agentic account authorization.
```
:::

:::warning{title="Before you switch"}
1. If an old Bitget stdio MCP or CLI is still on this computer, remove it and use Agenthub. The authorization flow above is enough to start using Agenthub.
2. If you already authorized an Agentic account (formerly called an Agent sub-account), close the positions and open orders first, then remove the old setup. An Agentic account authorized through the old MCP does not work with the new MCP. When you authorize, create a new account.
:::

---

### Product structure

Agenthub has three parts. The Agentic account is how you sign in and how you see the money in that account. Trading is for crypto and for tokenized US stocks such as Apple, Tesla, and NVIDIA. Data is for market prices, and for dividends, holidays, and valuation on those tokenized stocks.

#### (1) Agentic account

An Agentic account is a separate trading account. Its funds are not the same as your main account. After you sign in in the browser, you can trade in this account. You do not type an API Key.

To disconnect it: open the sub-account page and choose Disconnect Agent. Clear unfilled orders first. You can move the money back yourself.

| What you want | Where |
|-|-|
| Disconnect the agent | [Sub-account page](https://www.bitget.com/account/sub-account) |
| Not connected, connect again | [Agentic account page](https://www.bitget.com/account/center/agent-subaccount-mcp) |

New accounts do not have an API Key. If an older account still has one, you cannot delete that Key by itself on the website. Clear the orders, move the assets out, then delete the Agentic sub-account yourself. Its old name was Agent sub-account. The AI will not delete the account for you.

Before every trade, you see what is about to run. It is sent only after you agree.

#### (2) Trading MCP

22 endpoints. All of them require a login. You confirm before an order is sent. Tokenized US stocks such as Apple, Tesla, and NVIDIA use this same order flow.

| Area | Endpoints | Auth | What it covers | For example |
|-|-|-|-|-|
| Place orders | 3 | Login | Market or limit orders<br/>Submit several orders at once<br/>Strategy orders<br/>Spot<br/>Futures<br/>Tokenized US stocks such as Apple, Tesla, and NVIDIA | "Market-buy 0.1 BTC"<br/>"Open a BTC long"<br/>"Place these three limit orders together"<br/>"Buy a little of Apple's tokenized stock" |
| Change orders | 3 | Login | Change the price or size of a normal order<br/>Change a strategy order<br/>Change several orders at once | "Move this order to 65000"<br/>"Raise the take-profit on the strategy order"<br/>"Reprice these orders together" |
| Cancel and close | 6 | Login | Cancel one order<br/>Cancel a strategy order<br/>Cancel several orders<br/>Cancel every open order<br/>Cancel everything after a countdown<br/>Close all positions | "Cancel this order"<br/>"Cancel every BTC order"<br/>"Close the long in one step" |
| Look up | 10 | Login | Open positions<br/>Position history<br/>Position risk rank<br/>Open orders<br/>Open strategy orders<br/>Order history<br/>One order's details<br/>Fills<br/>How much more you can open | "What's my position?"<br/>"What did I close yesterday?"<br/>"Did this order fill?"<br/>"How much more can I open?" |

Not here: buying stocks inside a US brokerage account, CFDs, tax, collateralized lending, or institutional lending.

#### (3) Data MCP

| Area | Endpoints | Auth | What it covers | For example |
|-|-|-|-|-|
| Market data | 35 | No login | Current and historical candles<br/>Latest prices<br/>Order book<br/>Recent trades<br/>Current and historical funding rates<br/>Open interest and its cap<br/>Position tiers<br/>Long/short ratio<br/>Taker buy and sell volume<br/>Liquidation history<br/>Spot flow and large-account net inflow<br/>Index components<br/>Discount rate<br/>Risk reserve<br/>Proof of reserves<br/>Cash dividends<br/>Splits and reverse splits | "BTC price"<br/>"4h candles"<br/>"What's the funding rate?"<br/>"Show the book"<br/>"How much just got liquidated?" |
| Tokenized US stocks | 14 | Login | Stock profile<br/>Market open or closed<br/>Holiday calendar<br/>Halts and resumptions<br/>Book and trades<br/>Dividends and splits<br/>Valuation<br/>Earnings estimates<br/>Company overview<br/>Share-count changes<br/>Major holders<br/>Management holdings<br/>Insider trades | "Is Apple's market closed today?"<br/>"When does NVIDIA pay a dividend?"<br/>"What is Tesla's tokenized stock worth?"<br/>"Who are the major holders?" |
| Crypto research | 40 | No login | Tradable markets and token profiles<br/>Spot candles<br/>Spot prices<br/>Spot book<br/>Spot trades<br/>Spot taker flow<br/>Spot large trades<br/>Mark price<br/>Futures candles<br/>Funding rate<br/>Open interest<br/>Long/short ratio<br/>Liquidations<br/>Futures large trades<br/>On-chain flows<br/>Buy and sell signals<br/>Exchange inflows and outflows<br/>Active addresses<br/>Stablecoin changes<br/>Unlock schedule<br/>Corporate holdings<br/>ETF holdings<br/>Miner holdings<br/>Country holdings<br/>Technical indicators<br/>Hyperliquid long/short<br/>Hyperliquid PnL<br/>Hyperliquid positions<br/>Hyperliquid whale trades | "Which pairs does BTC trade on?"<br/>"Is on-chain money flowing in or out?"<br/>"When is the next unlock?"<br/>"Are Hyperliquid whales long or short?" |
| US stock research | 21 | No login | Company profile and live quote<br/>Historical candles<br/>Management<br/>Earnings calendar<br/>Balance sheet<br/>Income statement<br/>Cash flow<br/>Financial ratios<br/>Valuation<br/>Dividends<br/>Insider trades<br/>Major holders<br/>Institutional holdings<br/>Analyst price targets<br/>Earnings estimates<br/>Revenue estimates | "What's Apple trading at?"<br/>"Show NVIDIA's latest earnings"<br/>"When is Tesla's next dividend?"<br/>"Are institutions adding or cutting?" |
| ETFs | 3 | No login | Profile<br/>Holdings<br/>Performance | "What does this ETF hold?"<br/>"How has it done lately?" |
| News | 1 | No login | Search financial news by keyword | "Any NVIDIA news today?" |
| Sentiment | 2 | No login | Crypto Fear and Greed<br/>Broader market sentiment | "Is the market fearful or greedy?" |

---

### Safety

Sign-in happens in the browser. Do not hand an API Key to the AI, and do not put one in a config file. Every trade waits for your confirmation.

Change your email, phone, or two-factor settings on the Bitget website yourself. Withdrawals, and moving money from the main account into the Agentic account, are also done on the website.

---

### FAQ

**Q: Do I still create an API Key?**

**A:** No.

**Q: Do I need to sign in just to see prices?**

**A:** No. Trading, account actions, and Reality tokenized-stock details require a login.

**Q: What about the old tools later in this article?**

**A:** Those are the old install, and they will be maintained less and less. Agenthub uses only `https://agent.bitget.com/mcp`.

**Q: How do I revoke access?**

**A:** Disconnect the agent on the sub-account page. Clear unfilled orders first.

**Q: The login page will not open.**

**A:** Check that you can open bitget.com. If you cannot, turn on a proxy, then ask the agent to authorize again.

**Q: How do I delete an API Key on an old account?**

**A:** Clear the orders, move the assets out, then delete that Agentic sub-account yourself. You cannot delete only the Key on the website.

---

### Links

| Resource | Address |
|-|-|
| Agenthub landing page | https://www.bitget.com/activity-hub/agent-hub |
| Cloud MCP | https://agent.bitget.com/mcp |
| Sub-account page | https://www.bitget.com/account/sub-account |
| Agentic account page | https://www.bitget.com/account/center/agent-subaccount-mcp |
| Telegram | https://telegram.me/+o1tYqQ_lXxllYjgy |

---

## 2. Legacy system (being phased out)

:::warning{title="Legacy"}
This is the old version. It will be maintained less and less. Use Agenthub above. If you already installed the old tools, the commands are here.
:::

```text
Legacy system (being phased out)
├── What the old version could do
├── Old install paths
├── Old Agentic (local MCP, API Key on this device)
├── Old CLI · bgc
├── Old Signal
├── Old SDK
├── Old safety notes
└── Old FAQ
```

Runs as a local process on your device · API Keys are signed on this device with HMAC-SHA256 and never pass through a third-party server · MIT licensed

[GitHub](https://github.com/Bitget-AI/agent_hub) · [API docs](https://www.bitget.com/api-doc/common/intro) · [Get an API Key](https://www.bitget.com/en/api-management) (legacy only) · [Telegram](https://telegram.me/+o1tYqQ_lXxllYjgy)

### What the old version could do

:::tip{title="Who it's for"}
Agenthub **is for people who want AI to trade crypto and tokenized US stocks:** watch the market · read the tape · place trades · manage the account · write a strategy · do research.
:::

The hard part of trading with AI is not the strategy. It is jumping back and forth: you ask the AI, then place the order yourself, then come back to the chat. Agenthub puts both steps in one place. You say one sentence. It does the rest.

| You say | What happens |
|-|-|
| "Market-buy 0.1 BTC" · "Open a BTC long at 10x" | Spot or futures order |
| "Check my balance" · "Move 500 USDT to the futures account" | Account lookup and a transfer |
| "BTC price" · "4h candles" · "funding rate" | Live market data (no API Key) |
| "Is sentiment too greedy or too fearful?" · "What matters in the news today?" | Market analysis (no account) |

:::warning{title="Risk"}
AI can be wrong. You are responsible for orders. Practice on the demo account first.
:::

### Old install paths

Pick the path for the AI tool you use.

:::info{title="Fastest start"}
Send this to Claude Code or Cursor. It installs the legacy Skill and local MCP, then opens the browser for authorization.

```text title="Prompt for your AI"
Do only the legacy first-time install. Node.js 20+ is required. Do not run upgrade-all. Do not ask me to create or paste an API Key. Do not build the authorization URL yourself.
1. Run npx @bitget-ai/bitget-agent-skill --target all --skill agentic. The --skill agentic flag is required. Version must be 3.3.0 or newer.
2. Run npm i -g @bitget-ai/bitget-agent-mcp. Do not set BITGET_API_*.
3. Stop in this chat once the MCP is registered. Ask me to open a new chat, then call authorize_start to open the browser. After I log in and approve, confirm with get_auth_status. If bitget.com will not open, check the local proxy first, then authorize again.
```
:::

:::info{title="Overview"}
The same install works for every tool listed on that path. The CLI command, for example, is the same on Claude Code, Codex, and OpenClaw. After it runs, it detects the tools you already have and deploys into them.
:::

| I use… | Path | One-step install |
|-|-|-|
| Claude Desktop · Cursor · Windsurf · ChatGPT Desktop · Codex (OAuth in one step, no Key to type) | Old MCP server | `npx -y @bitget-ai/bitget-agent-mcp` |
| Claude Code · Codex CLI · OpenClaw | CLI · bgc | `npx @bitget-ai/bitget-agent-installer upgrade-all --target all` |
| Market analysis only, no trading | Signal | `npx @bitget-ai/bitget-signal --target all` |
| Not sure / I want everything | Full set | `npx @bitget-ai/bitget-agent-installer upgrade-all --target all` |

:::tip{title="Note"}
The MCP server command in the table only starts the process. It does not write your AI tool's config. You, or the AI, still have to edit that file. The steps are under Old Agentic below. The row that used to point at `https://agent.bitget.com/mcp` now belongs in part 1. Do not install that address here as a read-only data service.
:::

**Requirement**: [Node.js 20 or newer](https://nodejs.org/). Check with `node -v`.

### Old Agentic (local MCP, API Key on this device)

An Agentic account is a separate trading account connected with OAuth. Its funds stay apart from the main account. After authorization, MCP and CLI tools can trade in that account. You do not type a Key. This setup stores the credentials on your device.

Paste this to your AI. It will walk you through browser OAuth and install the tools.

```text title="Prompt for your AI"
Do only the legacy first-time install. Node.js 20+ is required. Do not run upgrade-all. Do not ask me to create or paste an API Key. Do not build the authorization URL yourself.
1. Run npx @bitget-ai/bitget-agent-skill --target all --skill agentic. The --skill agentic flag is required. Version must be 3.3.0 or newer.
2. Run npm i -g @bitget-ai/bitget-agent-mcp. Do not set BITGET_API_*.
3. Stop in this chat once the MCP is registered. Ask me to open a new chat, then call authorize_start to open the browser. After I log in and approve, confirm with get_auth_status. If bitget.com will not open, check the local proxy first, then authorize again.
```

:::info{title="When to use"}
Use this if your AI tool has a window: Claude Desktop, Cursor, Windsurf, ChatGPT Desktop, or Codex. Each sentence you type becomes an action on your Bitget account.
:::

The steps are the same for every tool. The command stays `npx -y @bitget-ai/bitget-agent-mcp`. Only the config file location changes.

**About this authorization**

Before you trade, move funds from the main account to the Agentic account on the website. The agent cannot transfer or withdraw for you. Once the credentials are saved, the trading tools work without restarting the agent. If the link drops or the credentials expire, run OAuth again.

**Manual setup**

**Step 1** — Open your AI tool's MCP config.

**Step 2** — Add the block below. Do not put an API Key in it. The first time you use a trading tool, the AI opens the browser for OAuth. Bitget issues the credentials and they are saved locally.

```json title="mcp config"
{
  "mcpServers": {
    "bitget": {
      "command": "npx",
      "args": ["-y", "@bitget-ai/bitget-agent-mcp"]
    }
  }
}
```

**Step 3** — Quit the AI tool completely and open it again.

**Step 4** — Ask `What is the BTC price?` A quote means the basic setup works. Then ask something that needs trading permission, such as your account balance. The AI opens the browser for OAuth.

**Modes**

| Situation | Extra args | What it does |
|-|-|-|
| Practice on the demo account first | `"--paper-trading"` | Uses a Demo Key. Real assets stay put. |
| Look only, do not trade | `"--read-only"` | Blocks orders and transfers. |
| Prices only, no account | `"--modules", "market"` | No API Key. |

:::tip{title="Cursor users"}
Cursor holds about 40 MCP tools in total, and Bitget uses about 14 by default. If they do not all load, turn other MCP servers off, or start with `--modules market` so only market data loads.
:::

**Proxy**

If you need a VPN or proxy, add an `env` block to the MCP config. This is only for the network. It is not part of account authorization. Use your own proxy address.

```json title="Proxy config"
"env": {
  "HTTPS_PROXY": "your proxy, for example http://127.0.0.1:port",
  "NODE_USE_ENV_PROXY": "1"
}
```

:::info{title="Why NODE_USE_ENV_PROXY"}
`NODE_USE_ENV_PROXY=1` makes Node.js itself use the proxy. Without it, some requests skip the proxy.
:::

**What the AI can do after install**

| Module | Loaded by default | Covers | Needs authorization |
|-|-|-|-|
| `market` | Yes | Prices, candles, funding, order book, open interest | No |
| `trade` | Yes | Place, cancel, and edit orders; positions; strategy orders | Yes |
| `account` | Yes | Balances, transfers, deposits, withdrawals, sub-accounts | Yes |
| `strategy` | On request | Trigger orders, take-profit and stop-loss, planned orders | Yes |
| `cryptoloans` | On request | Borrow, repay, collateralized loans | Yes |
| `tax` | On request | Tax record lookup | Yes |

**Try these**

```text
What is the BTC price?
Check my USDT balance and list my futures positions.
On the demo account, open a BTC long, 10x, 0.01 BTC.
Check the BTC price, then place a limit buy 2% below it.
```

### Old CLI · bgc

:::info{title="When to use"}
Use this with a terminal AI (Claude Code, Codex CLI, OpenClaw), or when you want to type Bitget commands yourself.
:::

```text title="Prompt for your terminal AI"
Install the Bitget Agent Hub terminal tools. Node.js 20+ is required:
npx @bitget-ai/bitget-agent-installer upgrade-all --target all
When it finishes, verify with `bgc --version` and `bgc discover`, and show me the output.
```

```bash
npx @bitget-ai/bitget-agent-installer upgrade-all --target all
```

That installs the `bgc` CLI, the trading Skill, and the market-analysis Skill, and deploys them to Claude Code, Codex, and OpenClaw.

**API Key**

`bgc` still needs an API Key typed in by you. Create one on the [API management page](https://www.bitget.com/en/api-management). Enable **Read + Trade**, and save the API Key, Secret Key, and Passphrase. A **Demo Key** plus `--paper-trading` is the safer way to practice.

```bash
export BITGET_API_KEY="your API Key"
export BITGET_SECRET_KEY="your Secret Key"
export BITGET_PASSPHRASE="your Passphrase"
```

:::tip{title="Tip"}
Put those three lines in `~/.zshrc` or `~/.bashrc`. Public prices do not need a Key. Balances and orders do.
:::

**Check the install**

```bash
bgc --version
bgc discover
bgc market --action tickers --category SPOT --symbol BTCUSDT
```

| Verb | What it does | Example |
|-|-|-|
| `market` | Prices, candles, funding (public) | `bgc market --action tickers --symbol BTCUSDT` |
| `order` | Place, cancel, edit, and look up orders | `bgc order --action place --side buy --qty 0.1` |
| `position` | Positions, close, leverage | `bgc position --action info --category linear` |
| `strategy_order` | Trigger orders, take-profit and stop-loss | `bgc strategy_order --action open` |
| `account_overview` | Snapshot of assets, positions, and fees | `bgc account_overview --coin USDT` |
| `transfer_funds` | Move funds between accounts | `bgc transfer_funds --fromType spot --amount 100` |
| `deposit` | Deposit address and records | `bgc deposit --action address --coin USDT` |
| `withdraw` | Withdraw (high risk, needs `--confirm`) | `bgc withdraw --coin USDT --amount 100 --confirm` |
| `loan` | Borrow and repay | `bgc loan --action borrow --coin USDT` |
| `subaccount` | Sub-accounts | `bgc subaccount --action list` |
| `tax` | Tax records | `bgc tax --action history --year 2024` |
| `discover` | List available actions | `bgc discover --domain trade` |

**Safety flags**

| Flag | Effect |
|-|-|
| `--dry-run` | Build the request and do not send it |
| `--read-only` | Block every write |
| `--paper-trading` | Use the demo environment |
| `--confirm` | Second confirmation for high-risk actions such as withdrawals |

**Legacy Skill (used with the CLI, Key typed in by you)**

A Skill is a note installed into the AI tool. It tells the AI when to call `bgc`, how to build the command, and when to ask you before a write. `upgrade-all` already includes it. To install only the Skill:

```bash
npx @bitget-ai/bitget-agent-skill --target all
```

| `--target` | Installs into |
|-|-|
| `claude` | Claude Code |
| `codex` | Codex CLI |
| `openclaw` | OpenClaw |
| `all` | All of the above |

:::tip{title="Note"}
Without `--skill agentic`, this command installs the manual-Key instructions. Agenthub's instructions are in How to connect, above.
:::

### Old Signal

No Bitget account and no API Key. Install puts five Skill files on this device and registers a public remote MCP data service (`https://datahub.noxiaohao.com/mcp`) as the source.

| You can ask… | Source |
|-|-|
| "How does a Fed hike hit BTC?" | `macro-analyst` — rates, yield curve, cross-asset correlation |
| "Are whales sending coins to exchanges?" | `market-intel` — on-chain flow, ETF net inflow, DeFi TVL |
| "How is sentiment?" | `sentiment-analyst` — sentiment index, funding, long/short positioning |
| "Is BTC's RSI overbought?" | `technical-analysis` — indicators calculated from candles |
| "What mattered in crypto news today?" | `news-briefing` — news aggregation |

```bash
npx @bitget-ai/bitget-signal --target all
```

:::tip{title="Python dependencies"}
`technical-analysis` needs pandas and numpy. If you want indicators, run `pip install pandas numpy` first. Restart the AI tool after install.
:::

### Old SDK

For developers embedding this in their own project: a custom MCP, a quant strategy, or automated trading.

```bash
npm install @bitget-ai/bitget-agent-sdk
```

```typescript
import { loadConfig, buildTools, BitgetRestClient, safeInvoke } from "@bitget-ai/bitget-agent-sdk";

const config = loadConfig({ modules: "all", readOnly: true });
const client = new BitgetRestClient(config);
const tools = buildTools(config);
const ctx = { config, client };

const market = tools.find((t) => t.name === "market")!;
const res = await safeInvoke(market, { action: "tickers", category: "SPOT", symbol: "BTCUSDT" }, ctx);

if (res.ok) console.log(res.data);
else console.error(res.error);
```

| Parameter | Default | Meaning |
|-|-|-|
| `surface` | `"intent"` | `"intent"` is the short verb set; `"full"` exposes every action |
| `modules` | `"account,trade,market"` | Comma-separated module names, or `"all"` |
| `readOnly` | `false` | Drop every write tool |
| `paperTrading` | `false` | Route to the Bitget demo environment |
| `baseUrl` | `https://api.bitget.com` | Override with `BITGET_API_BASE_URL` |

More: [agent-sdk](https://github.com/Bitget-AI/agent-sdk)

**Requires**: Node.js 20 or newer · ESM only · no runtime dependencies · TypeScript types included

### Old safety notes

Credentials stay on this device. API Keys are read only from environment variables. Requests are signed locally with HMAC-SHA256 and sent straight to `api.bitget.com`. Agentic credentials follow the same rule: after OAuth, the MCP or SDK stores them locally. The AI never asks you to type or paste them.

| Control | What it does |
|-|-|
| **Demo mode** | `--paper-trading` sends requests to the Bitget demo environment |
| **Read-only** | `--read-only` removes every write tool at startup |
| **Preview** | `--dry-run` builds the full request and does not send it |
| **High-risk confirmation** | Withdrawals and cancel-all need an explicit `--confirm` |

Start on the demo account. When you create an API Key, enable only what you need. Leave withdrawals off if you do not need them.

### Old FAQ

**Q: My AI tool is not on the list. Can I use it?**

**A:** Any client that speaks MCP can connect. A terminal AI that can run commands can use `bgc`.

**Q: Do prices need an API Key?**

**A:** No. A Key is only for balances, orders, and transfers.

**Q: Does the AI see my API Key?**

**A:** No. The Key is read from a local environment variable and is not uploaded.

**Q: What is the difference between a Key I create and an Agentic account?**

**A:** A Key you create on the website shares the main-account balance. The old Agentic account enters a separate pool of funds through OAuth, and the MCP or SDK stores the credentials on this device.

**Q: Bitget tools did not all load in Cursor.**

**A:** Turn other MCP servers off, or add `--modules market` to the start args.

**Q: Will the AI ask before it places an order?**

**A:** Yes. The Skill asks and waits before a write. Withdrawals also need `--confirm`.

**Q: Is there a fee?**

**A:** Agenthub itself is MIT-licensed and free. Trading fees follow your Bitget account tier.

**Q: Where do I report a problem?**

**A:** [GitHub Issues](https://github.com/Bitget-AI/agent_hub/issues). Email security issues to security@bitget.com. Do not post them in public.

| Resource | Address |
|-|-|
| Agent Hub | https://github.com/Bitget-AI/agent_hub |
| MCP server | https://github.com/Bitget-AI/agent-mcp |
| CLI (bgc) | https://github.com/Bitget-AI/agent-cli |
| Skill | https://github.com/Bitget-AI/agent-skill |
| Signal | https://github.com/Bitget-AI/bitget-signal |
| SDK | https://github.com/Bitget-AI/agent-sdk |
| Bitget API docs | https://www.bitget.com/api-doc/common/intro |
| API Key management | https://www.bitget.com/en/api-management |
| Telegram | https://telegram.me/+o1tYqQ_lXxllYjgy |

:::warning{title="Risk disclaimer"}
Crypto and tokenized US stock trading can lose money, and AI can be wrong. Check everything yourself and accept the results. This tool is not investment advice.
:::

---

# Agent Hub

**不用打开交易所，接入 Agenthub 说一句话，Agent 帮你直接在 Claude、Cursor、Codex，以及 Grok bot、Muse、Dot 这些 Personal Agent 里操作你的 Bitget 账户交易美股和加密货币。**

在 Claude、Cursor、Codex，或 Grok bot、Muse、Dot 这些 Personal Agent 里接上 `https://agent.bitget.com/mcp`，按页面提示在浏览器里登录 Bitget 即可。先看能做什么，再看怎么接入。

:::info{title="关于旧版本"}
文章后半部分是旧版本的安装办法，以后会慢慢不再维护旧版本产品能力，只留给已经装过的人查原来的命令。
:::

[落地页](https://www.bitget.com/activity-hub/agent-hub) · [API 文档](https://www.bitget.com/api-doc/common/intro) · [Telegram 社群](https://telegram.me/+o1tYqQ_lXxllYjgy)

## 文档目录

```text
Bitget Agenthub
├── 能做什么
├── 怎么接入
├── 具体产品架构
│   ├── Agentic 账户
│   ├── 交易相关的 MCP
│   └── 数据相关的 MCP
├── 安全须知
├── FAQ
└── 链接
```

---

## 一、最新版本（优先使用这版本）

### 能做什么

:::tip{title="适合谁"}
Agenthub **适合想用 Agent 交易加密货币和代币化美股的用户：** AI 辅助看盘 · 分析行情 · 执行操作 · 管理账户 · 写策略 · 做研究。
:::

用 AI 做交易这件事，最麻烦的不是策略，是要在 AI 和交易所之间反复切换——问完 AI 再去手动下单，看完行情再回来对话。Agenthub 把这两步合并：你只需要在 AI 里说一句话，剩下的它来做。看行情不用登录。要交易、查账户、看代币化美股，先在浏览器里登录一次。

| 你对 AI 说 | 实际发生的事 |
|-|-|
| 「BTC 现价」「4h K 线」「资金费率」 | 实时行情，不用登录 |
| 「市价买 0.1 BTC」「开 BTC 多仓」「买一点 rAAPL」 | 买卖加密货币，也可以买苹果、特斯拉、英伟达这类美股代币。要先登录 |
| 「查余额」「看看划转和充值记录」 | 账户查询和资金记录，要先登录 |
| 「苹果什么时候分红、今天休市吗」「rAAPL 这只美股现在的估值」 | 查看美股的分红、休市和估值。要先登录 |

---

### 怎么接入

把下面方框里的话发给你的 AI。它会接上 Agenthub，并打开浏览器让你登录 Bitget。登录之后才能下单、查看账户。如果这次只看行情、先不登录，发的时候补一句：只看行情，先不要登录。

:::info{title="最快上手"}
把下面这段话发给 AI，它会帮你快速安装 Agenthub：

```text title="粘贴给 AI 的指令"
请阅读【https://www.bitget.com/support/articles/12560603894122】完成 Bitget Agentic 账户授权。
```
:::

:::warning{title="接入前注意"}
1. 电脑上如果还留着旧版 Bitget stdio MCP / CLI，清除并改用新版 Agenthub 相关能力（走一遍上述的授权流程即可使用新版 Agenthub 相关能力）。
2. 如果之前有授权过 Agentic 账户（旧名为 Agent 子账户），请处理相关仓位和委托订单，再去清除相关配置。之前用旧版 MCP 授权过的 Agentic 账户无法直接兼容新版 MCP，授权时请选择新建账户。
:::

---

### 具体产品架构

Agenthub 由三块组成。Agentic 账户用来登录，也用来看这个账户里的钱。交易用来买卖加密货币，以及苹果、特斯拉、英伟达这类美股代币。数据用来看行情，也用来看这些美股代币的分红、休市和估值。

#### （1）Agentic 账户

Agentic 账户是独立的交易账户，资金和主账户分开。在浏览器里登录之后，就可以在这个账户里交易，不用手填 API Key。

想断开这个 Agentic 账户的连接：打开子账户管理页，点「断开 Agent 连接」。断开前，先处理还没成交的委托。钱可以自己转回去。

| 要做的事 | 去哪里 |
|-|-|
| 断开 Agent 连接 | [子账户管理页](https://www.bitget.com/account/sub-account) |
| 当前没连接，重新连接 | [Agentic 账户页](https://www.bitget.com/account/center/agent-subaccount-mcp) |

新账户没有 API Key。以前的账户如果还留着 Key，不能在网页上单独删掉那把 Key。先清空订单，把资产转出，再自己删除这个 Agentic 子账户。它以前的名字是 Agent 子账户。AI 不会替你删账户。

每次交易前，你会先看到要执行的内容。你同意之后，才会真正下单。

#### （2）交易相关的 MCP

共 22 个接口，都要先登录。下单前会先让你确认。苹果、特斯拉、英伟达这类美股代币也走这套下单。

| 大类 | 接口数 | 鉴权 | 能力 | 例如 |
|-|-|-|-|-|
| 下单 | 3 | 要登录 | 普通下单（市价、限价）<br/>一次提交多笔<br/>创建策略单<br/>现货<br/>合约<br/>苹果、特斯拉、英伟达这类美股代币 | 「市价买 0.1 BTC」<br/>「开 BTC 多仓」<br/>「这三笔限价单一起下」<br/>「买一点苹果的美股代币」 |
| 改单 | 3 | 要登录 | 改普通单的价格或数量<br/>改策略单<br/>一次改多笔 | 「把这单改成 65000」<br/>「策略单止盈调高一点」<br/>「这几笔一起改价」 |
| 撤单和平仓 | 6 | 要登录 | 撤一笔普通单<br/>撤策略单<br/>一次撤多笔<br/>撤掉全部当前委托<br/>倒计时后全部撤掉<br/>一键平仓 | 「撤掉这一单」<br/>「撤掉所有 BTC 委托」<br/>「一键平掉多仓」 |
| 查看 | 10 | 要登录 | 当前仓位<br/>历史仓位<br/>仓位风险排名<br/>当前委托<br/>当前策略单<br/>历史委托<br/>单笔订单详情<br/>成交明细<br/>最多还能开多少 | 「现在仓位多少」<br/>「昨天平掉的仓」<br/>「这单成交了没」<br/>「最多还能开多少」 |

不在这里：美股账户里的股票直连、差价合约（CFD）、税务、质押借贷、机构借贷。

#### （3）数据相关的 MCP

| 大类 | 接口数 | 鉴权 | 能力 | 例如 |
|-|-|-|-|-|
| 行情 | 35 | 不用登录 | 当前和历史 K 线<br/>最新行情<br/>买卖盘深度<br/>最近成交<br/>当前和历史资金费率<br/>未平仓量和限仓<br/>仓位档位<br/>多空比<br/>主动买卖量<br/>历史爆仓<br/>现货资金流向和大户净流入<br/>指数成分<br/>折扣率<br/>风险准备金<br/>储备金证明<br/>派息记录<br/>拆合记录 | 「BTC 现价」<br/>「4h K 线」<br/>「资金费率多少」<br/>「买盘卖盘深度」<br/>「最近爆了多少」 |
| 美股代币资料 | 14 | 要登录 | 股票信息<br/>开闭市状态<br/>休市日历<br/>停牌和复牌<br/>买卖盘和成交<br/>分红和拆分<br/>估值<br/>盈利预测<br/>公司概况<br/>股本变动<br/>主要股东<br/>管理层持股<br/>内部人交易 | 「苹果今天休市吗」<br/>「英伟达什么时候分红」<br/>「特斯拉这只美股现在怎么估值」<br/>「特斯拉主要股东有哪些」 |
| 加密货币研究 | 40 | 不用登录 | 可交易市场和代币资料<br/>现货 K 线<br/>现货行情<br/>深度<br/>成交<br/>主动买卖<br/>大单<br/>合约标记价格<br/>合约 K 线<br/>资金费率<br/>持仓<br/>多空比<br/>清算<br/>合约大单<br/>链上资金<br/>买卖信号<br/>交易所流入流出<br/>活跃地址<br/>稳定币变化<br/>解锁日程<br/>公司持仓<br/>ETF 持仓<br/>矿企持仓<br/>国家持仓<br/>技术指标<br/>Hyperliquid 多空<br/>Hyperliquid 盈亏<br/>Hyperliquid 仓位<br/>Hyperliquid 鲸鱼交易 | 「BTC 有哪些交易对」<br/>「链上资金在流入还是流出」<br/>「下次解锁什么时候」<br/>「Hyperliquid 上大户在做多还是做空」 |
| 美股研究 | 21 | 不用登录 | 公司资料和实时报价<br/>历史 K 线<br/>管理层<br/>财报日历<br/>资产负债表<br/>利润表<br/>现金流量表<br/>财务指标<br/>估值<br/>分红<br/>内部人交易<br/>主要股东<br/>机构持仓<br/>分析师目标价<br/>盈利预期<br/>营收预期 | 「苹果现在多少钱」<br/>「看一下英伟达最新财报」<br/>「特斯拉下次分红」<br/>「机构在加仓还是减仓」 |
| ETF | 3 | 不用登录 | 基本信息<br/>持仓明细<br/>市场表现 | 「这只 ETF 持有哪些股票」<br/>「最近表现怎么样」 |
| 新闻 | 1 | 不用登录 | 按关键词检索财经新闻 | 「今天有什么和英伟达相关的新闻」 |
| 市场情绪 | 2 | 不用登录 | 加密市场恐慌贪婪指数<br/>综合市场情绪指数 | 「现在市场是恐慌还是贪婪」 |

---

### 安全须知

登录在浏览器里完成。不用把 API Key 交给 AI，也不用写进配置。每次交易前都会先让你确认。

改邮箱、手机、双重验证，请在 Bitget 网页上自己做。提币，以及从主账户把钱转入 Agentic 账户，也请在网页上自己完成。

---

### FAQ

**Q: 还要自己创建 API Key 吗？**

**A:** 不用。

**Q: 只看行情要登录吗？**

**A:** 不用。交易、账户、Reality 需要登录。

**Q: 和文章后面的旧工具是什么关系？**

**A:** 那些是以前装在电脑上的办法，以后会慢慢不再维护。Agenthub 只用 `https://agent.bitget.com/mcp`。

**Q: 怎么取消授权？**

**A:** 在子账户管理页断开 Agent 连接。断开前先处理未成交挂单。

**Q: 登录页打不开怎么办？**

**A:** 先确认自己能打开 bitget.com。打不开就开代理，然后让 Agent 再授权一次。

**Q: 旧账户上的 API Key 怎么删？**

**A:** 先清空订单、转出资产，再自己删除该 Agentic 子账户。不能在网页上单独删掉那把 Key。

---

### 链接

| 资源 | 地址 |
|-|-|
| Agenthub 落地页 | https://www.bitget.com/activity-hub/agent-hub |
| 云端 MCP | https://agent.bitget.com/mcp |
| 子账户管理页 | https://www.bitget.com/account/sub-account |
| Agentic 账户页 | https://www.bitget.com/account/center/agent-subaccount-mcp |
| Telegram 社群 | https://telegram.me/+o1tYqQ_lXxllYjgy |

---

## 二、旧版体系（后续会逐渐弃用）

:::warning{title="旧版"}
以下是旧版，以后会慢慢不再维护。请先用上面的 Agenthub。已经在电脑上装过旧工具的人，可以在这里查原来的命令。
:::

```text
旧版体系（后续会逐渐弃用）
├── 旧版能做什么
├── 旧版安装路径
├── 旧版 Agentic（本地 MCP，本机 API Key）
├── 旧版 CLI · bgc
├── 旧版 Signal
├── 旧版 SDK
├── 旧版安全须知
└── 旧版 FAQ
```

以本地进程方式运行在你的设备上 · API Key 经 HMAC-SHA256 在本机签名，不经任何第三方服务器 · MIT 开源

[GitHub](https://github.com/Bitget-AI/agent_hub) · [API 文档](https://www.bitget.com/api-doc/common/intro) · [获取 API Key](https://www.bitget.com/en/api-management)（只给旧版） · [Telegram 社群](https://telegram.me/+o1tYqQ_lXxllYjgy)

### （旧版）能做什么

:::tip{title="适合谁"}
Agenthub **适合想用 AI 交易加密货币和代币化美股的用户：** AI 辅助看盘 · 分析行情 · 执行操作 · 管理账户 · 写策略 · 做研究。
:::

用 AI 做交易这件事，最麻烦的不是策略，是要在 AI 和交易所之间反复切换——问完 AI 再去手动下单，看完行情再回来对话。AgentHub 把这两步合并：你只需要在 AI 里说一句话，剩下的它来做。

| 你对 AI 说 | 实际发生的事 |
|-|-|
| 「市价买 0.1 BTC」「开 BTC 多仓 10 倍杠杆」 | 现货 / 合约下单 |
| 「查余额」「把 500U 划到合约账户」 | 账户查询 & 资金划转 |
| 「BTC 现价」「4h K 线」「资金费率」 | 实时行情（无需 API Key） |
| 「现在市场情绪是过度乐观还是过度悲观？」「今天有什么重要消息？」 | 市场分析（无需账户） |

:::warning{title="风险提示"}
AI 可能误判，下单结果由你负责。强烈建议先用模拟盘演练。
:::

### （旧版）安装路径

根据你用的 AI 工具选择：

:::info{title="最快上手"}
把下面这段话发给 Claude Code 或 Cursor。它会按旧版装上 Skill 和本地 MCP，并打开浏览器完成授权。

```text title="粘贴给 AI 的指令"
请只做旧版首次安装。需要 Node.js 20+。不要运行 upgrade-all，不要让我创建或粘贴 API Key，不要自己拼授权链接。
1. 运行 npx @bitget-ai/bitget-agent-skill --target all --skill agentic。必须带 --skill agentic，版本不低于 3.3.0。
2. 运行 npm i -g @bitget-ai/bitget-agent-mcp。不要配置 BITGET_API_*。
3. 这一场对话刚注册完 MCP 就停。请我新开一场对话，再调用 authorize_start 打开浏览器。我登录并授权后，用 get_auth_status 确认完成。打不开 bitget.com 时，先检查本机代理，再重新授权。
```
:::

:::info{title="说明"}
同一路径下的安装方式对所有列出的工具通用。比如 CLI 的安装命令，在 Claude Code、Codex、OpenClaw 上步骤完全一样，运行后会自动识别并部署到你已安装的工具。
:::

| 我用的是… | 对应路径 | 一键安装 |
|-|-|-|
| Claude Desktop · Cursor · Windsurf · ChatGPT Desktop · Codex（支持 OAuth 一键连接，无需手动配 Key） | 旧版 MCP Server | `npx -y @bitget-ai/bitget-agent-mcp` |
| Claude Code · Codex CLI · OpenClaw | CLI · bgc | `npx @bitget-ai/bitget-agent-installer upgrade-all --target all` |
| 只需市场分析，不交易 | Signal | `npx @bitget-ai/bitget-signal --target all` |
| 不确定 / 全部都要 | 全套 | `npx @bitget-ai/bitget-agent-installer upgrade-all --target all` |

:::tip{title="注意"}
表格中 MCP Server 的一键命令只是启动 MCP 进程，并不会自动写入你的 AI 工具配置文件。你仍需手动（或让 AI）完成配置文件的修改，具体步骤见下方旧版 Agentic。原来指向 `https://agent.bitget.com/mcp` 的那一行已挪到第一部分，不要在旧版里再把它当成只读数据服务来装。
:::

**前置条件**：[Node.js ≥ 20](https://nodejs.org/)（运行 `node -v` 确认版本）

### （旧版）Agentic（本地 MCP，本机 API Key）

Agentic 账户是通过 OAuth 授权连接的独立交易账户，与主账户资金分开。授权后，MCP/CLI 工具即获得该账户下的交易权限，无需你手填 Key。这一套会把凭证保存在本机。

把下面这段话直接粘贴给你的 AI，它会引导你完成浏览器 OAuth 并安装好对应工具：

```text title="粘贴给 AI 的指令"
请只做旧版首次安装。需要 Node.js 20+。不要运行 upgrade-all，不要让我创建或粘贴 API Key，不要自己拼授权链接。
1. 运行 npx @bitget-ai/bitget-agent-skill --target all --skill agentic。必须带 --skill agentic，版本不低于 3.3.0。
2. 运行 npm i -g @bitget-ai/bitget-agent-mcp。不要配置 BITGET_API_*。
3. 这一场对话刚注册完 MCP 就停。请我新开一场对话，再调用 authorize_start 打开浏览器。我登录并授权后，用 get_auth_status 确认完成。打不开 bitget.com 时，先检查本机代理，再重新授权。
```

:::info{title="适用场景"}
如果你用的是有图形界面的 AI 工具（Claude Desktop、Cursor、Windsurf、ChatGPT Desktop、Codex），选这个。你在对话里说的每一条指令都会被转化为对你 Bitget 账户的实际操作。
:::

以下安装步骤对所有工具通用，核心命令 `npx -y @bitget-ai/bitget-agent-mcp` 不变。唯一的区别是配置文件的位置。

**关于这次授权**

交易前需先在 Web 端把资金从主账户划转到 Agentic 账户，Agent 无法代办划转和提币。凭证落盘后交易工具即可用，无需重启 Agent；断链或凭证失效时需重新走一遍 OAuth。

**手动配置**

**Step 1** — 打开你的 AI 工具 MCP 配置文件。

**Step 2** — 将以下内容添加到配置文件中。注意不需要填写任何 API Key：启动后首次使用交易类工具时，AI 会自动引导你完成浏览器 OAuth 授权，凭证由 Bitget 服务端签发并自动保存在本地：

```json title="mcp 配置"
{
  "mcpServers": {
    "bitget": {
      "command": "npx",
      "args": ["-y", "@bitget-ai/bitget-agent-mcp"]
    }
  }
}
```

**Step 3** — 完全退出并重启 AI 工具。

**Step 4** — 在 AI 对话里输入「BTC 现价是多少？」，收到行情数据说明基础配置成功。再问一句需要交易权限的话（比如查一下我的账户余额），AI 会自动打开浏览器引导你完成 OAuth 授权。

**按需调整模式**

| 场景 | 追加参数 | 说明 |
|-|-|-|
| 先用模拟盘熟悉 | `"--paper-trading"` | 使用 Demo Key，不动真实资产 |
| 只查询不操作 | `"--read-only"` | 禁止所有下单和划转操作 |
| 只看行情、不需要账户 | `"--modules", "market"` | 无需配置 API Key |

:::tip{title="Cursor 用户"}
Cursor 支持的 MCP 工具总数约为 40 个，Bitget 默认占用约 14 个。如果工具没有完整加载，尝试关闭其他 MCP，或用 `--modules market` 只加载行情模块。
:::

**代理配置**

如果你需要通过 VPN 或代理访问网络，在 MCP 配置里加入 env 块（仅用于代理网络配置，与账户授权无关，填入你自己的代理地址）：

```json title="代理配置"
"env": {
  "HTTPS_PROXY": "你的代理地址，例如 http://127.0.0.1:端口号",
  "NODE_USE_ENV_PROXY": "1"
}
```

:::info{title="为什么要加 NODE_USE_ENV_PROXY"}
`NODE_USE_ENV_PROXY=1` 确保 Node.js 的网络请求也走代理，否则部分请求可能绕过代理。
:::

**装完后 AI 能做什么**

| 模块 | 默认加载 | 涵盖操作 | 是否需要授权 |
|-|-|-|-|
| `market` | 是 | 行情价格 · K 线 · 资金费率 · 订单簿 · 持仓量 | 否 |
| `trade` | 是 | 下单 · 撤单 · 改单 · 查持仓 · 策略单 | 是 |
| `account` | 是 | 账户余额 · 资金划转 · 充值 · 提现 · 子账户管理 | 是 |
| `strategy` | 按需 | 触发单 · 止盈止损单 · 计划委托 | 是 |
| `cryptoloans` | 按需 | 借币 · 还款 · 质押贷款 | 是 |
| `tax` | 按需 | 税务记录查询 | 是 |

**试试这几句话**

```text
BTC 现价是多少？
查一下我的 USDT 余额，再看看有哪些合约持仓
帮我在模拟盘开一个 BTC 多仓，10 倍杠杆，0.01 BTC
先看一下 BTC 现价，再帮我挂一个比现价低 2% 的限价买单
```

### （旧版）CLI · bgc

:::info{title="适用场景"}
如果你用的是终端类 AI 工具（Claude Code、Codex CLI、OpenClaw），或者希望在终端里直接敲命令操作 Bitget，选这个。
:::

```text title="粘贴给终端 AI 的指令"
请执行以下命令安装 Bitget Agent Hub 终端工具（需要 Node.js 20+）：
npx @bitget-ai/bitget-agent-installer upgrade-all --target all
安装完成后帮我验证：运行 `bgc --version` 和 `bgc discover`，把结果告诉我。
```

```bash
npx @bitget-ai/bitget-agent-installer upgrade-all --target all
```

这条命令会安装 bgc CLI、交易 Skill 和市场分析 Skill，并自动部署到 Claude Code / Codex / OpenClaw。

**配置 API Key**

bgc 目前仍需手动配置 API Key。还没有 API Key？前往 [API 管理页面](https://www.bitget.com/en/api-management) 创建，勾选 **Read + Trade**，保存 API Key、Secret Key、Passphrase。建议先创建 **Demo Key** 配合 `--paper-trading` 练手。

```bash
export BITGET_API_KEY="你的 API Key"
export BITGET_SECRET_KEY="你的 Secret Key"
export BITGET_PASSPHRASE="你的 Passphrase"
```

:::tip{title="小贴士"}
建议把这三行写入 `~/.zshrc` 或 `~/.bashrc`。查看公开行情不需要 Key，账户操作和下单必须配置。
:::

**验证安装**

```bash
bgc --version
bgc discover
bgc market --action tickers --category SPOT --symbol BTCUSDT
```

| 动词 | 说明 | 示例 |
|-|-|-|
| `market` | 行情 · K 线 · 资金费率（公开数据） | `bgc market --action tickers --symbol BTCUSDT` |
| `order` | 下单 · 撤单 · 改单 · 查订单 | `bgc order --action place --side buy --qty 0.1` |
| `position` | 查持仓 · 平仓 · 设杠杆 | `bgc position --action info --category linear` |
| `strategy_order` | 触发单 · 止盈止损 | `bgc strategy_order --action open` |
| `account_overview` | 账户快照（资产 + 持仓 + 手续费） | `bgc account_overview --coin USDT` |
| `transfer_funds` | 账户间资金划转 | `bgc transfer_funds --fromType spot --amount 100` |
| `deposit` | 充值地址与记录 | `bgc deposit --action address --coin USDT` |
| `withdraw` | 提现（高风险，需 `--confirm`） | `bgc withdraw --coin USDT --amount 100 --confirm` |
| `loan` | 借币 · 还款 | `bgc loan --action borrow --coin USDT` |
| `subaccount` | 子账户管理 | `bgc subaccount --action list` |
| `tax` | 税务记录 | `bgc tax --action history --year 2024` |
| `discover` | 查看所有可用操作 | `bgc discover --domain trade` |

**安全标志：**

| 标志 | 作用 |
|-|-|
| `--dry-run` | 预览请求，不实际发送 |
| `--read-only` | 禁止所有写操作 |
| `--paper-trading` | 切换到模拟盘 |
| `--confirm` | 高风险操作（如提现）的二次确认 |

**旧版 Skill（配合 CLI，手填 Key）**

Skill 是一份装进 AI 工具里的说明文件，告诉 AI 什么时候该调用 bgc、怎么拼命令、写操作前如何提示你确认。使用 CLI 一键安装时（`upgrade-all`）已自动包含。如需单独部署：

```bash
npx @bitget-ai/bitget-agent-skill --target all
```

| `--target` | 部署到 |
|-|-|
| `claude` | Claude Code |
| `codex` | Codex CLI |
| `openclaw` | OpenClaw |
| `all` | 以上全部 |

:::tip{title="注意"}
这条不带 `--skill agentic` 的命令，装的是手配 Key 的说明。Agenthub 的说明在上面的「怎么接入」。
:::

### （旧版）Signal

不需要 Bitget 账户，也不需要 API Key。安装后会在本地部署 5 个 Skill 文件，并注册一个远程公开 MCP 数据服务（`https://datahub.noxiaohao.com/mcp`）作为数据源。

| 你可以问… | 数据来源 |
|-|-|
| 「美联储加息对 BTC 有什么影响？」 | `macro-analyst` — 宏观数据，利率 · 收益率曲线 · 跨资产相关性 |
| 「鲸鱼最近在往交易所转币吗？」 | `market-intel` — 链上流向 · ETF 资金净流入 · DeFi TVL |
| 「现在市场情绪怎么样？」 | `sentiment-analyst` — 情绪指数 · 资金费率 · 多空持仓比 |
| 「BTC 的 RSI 超买了吗？」 | `technical-analysis` — K 线后计算技术指标 |
| 「今天加密市场有什么重要新闻？」 | `news-briefing` — 新闻聚合 |

```bash
npx @bitget-ai/bitget-signal --target all
```

:::tip{title="技术指标依赖 Python"}
`technical-analysis` 依赖 pandas 和 numpy。需要技术指标时先执行 `pip install pandas numpy`。安装完成后重启 AI 工具。
:::

### （旧版）SDK

给要在自己项目里集成的开发者。构建自定义 MCP、量化策略或自动化交易时直接用 SDK。

```bash
npm install @bitget-ai/bitget-agent-sdk
```

```typescript
import { loadConfig, buildTools, BitgetRestClient, safeInvoke } from "@bitget-ai/bitget-agent-sdk";

const config = loadConfig({ modules: "all", readOnly: true });
const client = new BitgetRestClient(config);
const tools = buildTools(config);
const ctx = { config, client };

const market = tools.find((t) => t.name === "market")!;
const res = await safeInvoke(market, { action: "tickers", category: "SPOT", symbol: "BTCUSDT" }, ctx);

if (res.ok) console.log(res.data);
else console.error(res.error);
```

| 参数 | 默认值 | 说明 |
|-|-|-|
| `surface` | `"intent"` | intent 为精选动词；full 暴露所有操作 |
| `modules` | `"account,trade,market"` | 逗号分隔的模块名，或 all |
| `readOnly` | `false` | 移除所有写工具 |
| `paperTrading` | `false` | 路由到 Bitget Demo 环境 |
| `baseUrl` | `https://api.bitget.com` | 可用 BITGET_API_BASE_URL 覆盖 |

更多：[agent-sdk](https://github.com/Bitget-AI/agent-sdk)

**环境要求：** Node.js ≥ 20 · ESM only · 零运行时依赖 · 包含 TypeScript 类型

### （旧版）安全须知

AgentHub 在设计上保证你的凭证不离开本机：API Key 只从环境变量读取，所有请求在本地完成 HMAC-SHA256 签名后直连 `api.bitget.com`。Agentic 账户的凭证遵循同样原则：OAuth 完成后由 MCP/SDK 在本地保存，AI 不会手动填写或粘贴它。

| 机制 | 说明 |
|-|-|
| **模拟盘模式** | `--paper-trading` 将请求路由到 Bitget Demo 环境 |
| **只读模式** | `--read-only` 在启动时移除所有写工具 |
| **预览模式** | `--dry-run` 构建完整请求但不发送 |
| **高风险确认** | 提现、全撤等操作需要显式加 `--confirm` |

建议从模拟盘开始。创建 API Key 时按最小权限原则，不需要提现就不要开启。

### （旧版）FAQ

**Q: 我的 AI 工具不在列表里，能用吗？**

**A:** 支持 MCP 协议的客户端都可以接入；支持调用外部命令的终端 AI 可以使用 bgc。

**Q: 查行情需要 API Key 吗？**

**A:** 不需要。只有查余额、下单、划转才需要 Key。

**Q: API Key 会暴露给 AI 吗？**

**A:** 不会。Key 只从本地环境变量读取，不上传服务器。

**Q: 手配 API Key 和 Agentic 账户有什么区别？**

**A:** 手配 API Key 在网页创建，共用主账户余额。旧版 Agentic 账户通过 OAuth 进入独立资金域，凭证由 MCP/SDK 保存在本机。

**Q: Cursor 里 Bitget 工具没加载全？**

**A:** 可以关闭其他 MCP，或在启动参数里加 `--modules market`。

**Q: AI 下单前会让我确认吗？**

**A:** 会。Skill 会在写操作前提示并等待确认。提现还要额外加 `--confirm`。

**Q: 收费吗？**

**A:** AgentHub 本身 MIT 开源免费。交易手续费按 Bitget 账户等级计算。

**Q: 遇到问题去哪反馈？**

**A:** [GitHub Issues](https://github.com/Bitget-AI/agent_hub/issues)。安全漏洞发邮件至 security@bitget.com，不要在公开渠道发布。

| 资源 | 地址 |
|-|-|
| Agent Hub（总入口） | https://github.com/Bitget-AI/agent_hub |
| MCP Server | https://github.com/Bitget-AI/agent-mcp |
| CLI（bgc） | https://github.com/Bitget-AI/agent-cli |
| Skill | https://github.com/Bitget-AI/agent-skill |
| Signal | https://github.com/Bitget-AI/bitget-signal |
| SDK | https://github.com/Bitget-AI/agent-sdk |
| Bitget API 文档 | https://www.bitget.com/api-doc/common/intro |
| API Key 管理 | https://www.bitget.com/en/api-management |
| Telegram 社群 | https://telegram.me/+o1tYqQ_lXxllYjgy |

:::warning{title="风险提示"}
加密货币与代币化美股交易具有高风险，AI 可能误判。你须自行核对所有信息并承担全部后果。本工具不构成任何投资建议。
:::