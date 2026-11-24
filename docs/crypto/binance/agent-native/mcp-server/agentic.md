---
exchange: binance
source_url: https://developers.binance.com/en/docs/agent-native/mcp-server/agentic
api_type: Guide
updated_at: 2026-11-24 18:27:36.722596
---

# Binance MCP Server

<!-- SYNCED FROM be/agentic-tools@d3e0564fcb973e8686974a42b8e063d4fc25d053 docs/binance-mcp-server.md on 2026-08-17 -->
<!-- This MCP server is operated by Binance's AI team; mirrored here as our discovery entry point. -->

<!-- To check for drift: git log d3e0564fcb973e8686974a42b8e063d4fc25d053..HEAD -- docs/binance-mcp-server.md in be/agentic-tools -->

<!-- Layout (hero/fact tiles/callout/scenario cards/tabs/step cards) is a local redesign on top of the -->
<!-- synced text above — if you resync content, re-apply these components rather than pasting plain markdown. -->

import { Callout } from "zudoku/ui/Callout";
import { Tabs, TabsList, TabsTrigger, TabsContent } from "zudoku/ui/Tabs";
import {
  TrendingUp,
  ShieldCheck,
  CheckCircle2,
  Wallet,
  ShoppingCart,
  Repeat,
  Eye,
} from "lucide-react";

export const IconTile = ({ children, label }) => (
  <span
    className="inline-flex h-10 w-10 items-center justify-center rounded-lg border bg-muted"
    aria-label={label}
    title={label}
  >
    {children}
  </span>
);

export const FactTile = ({ icon: Icon, label, value }) => (
  <div className="not-prose flex items-center gap-3 rounded-xl border bg-card p-4">
    <div className="inline-flex h-9 w-9 shrink-0 items-center justify-center rounded-lg border bg-muted/40">
      <Icon className="h-4 w-4 text-muted-foreground" aria-hidden />
    </div>
    <div className="min-w-0">
      <p className="text-xs text-muted-foreground">{label}</p>
      <p className="text-sm font-medium break-all">{value}</p>
    </div>
  </div>
);

export const ScenarioCard = ({ icon: Icon, title, description }) => (
  <div className="not-prose rounded-xl border bg-card p-4 transition-colors hover:border-primary/30 hover:bg-primary/5">
    <div className="mb-3 inline-flex h-10 w-10 items-center justify-center rounded-xl border bg-muted/40">
      <Icon className="h-5 w-5 text-muted-foreground" />
    </div>
    <h4 className="text-sm font-semibold">{title}</h4>
    <p className="mt-1 text-xs leading-5 text-muted-foreground">
      {description}
    </p>
  </div>
);

export const StepCard = ({ number, icon: Icon, title, quote, outcome }) => (
  <div className="not-prose rounded-xl border bg-card p-4">
    <div className="mb-3 flex items-center gap-2">
      <span className="inline-flex h-6 w-6 items-center justify-center rounded-full bg-primary text-xs font-semibold text-primary-foreground">
        {number}
      </span>
      <Icon className="h-4 w-4 text-muted-foreground" aria-hidden />
      <h4 className="text-sm font-semibold">{title}</h4>
    </div>
    <p className="text-sm italic text-muted-foreground">"{quote}"</p>
    <p className="mt-2 text-xs leading-5 text-muted-foreground">{outcome}</p>
  </div>
);

<div className="not-prose -mt-2 mb-6 rounded-2xl border bg-[radial-gradient(circle_at_top_right,rgba(240,185,11,0.08),transparent_50%)] p-6">
  <div className="flex items-center gap-3 mb-3">
    <div className="inline-flex h-12 w-12 items-center justify-center rounded-xl border bg-primary/10">
      <TrendingUp className="h-6 w-6 text-primary" />
    </div>
    <div>
      <p className="text-xs font-semibold uppercase tracking-[0.16em] text-primary">
        Binance MCP Server
      </p>
    </div>
  </div>
  <p className="text-sm leading-6 text-muted-foreground">
    Connect your AI agent to Binance with a single URL. Your agent can read
    market data, check balances, trade Spot / Margin / Convert / USDⓈ-M / COIN-M
    Futures, and move funds between wallets inside a dedicated Agentic
    sub-account — no local install, no API keys on your device.
  </p>
</div>

<div className="mb-6 grid grid-cols-1 gap-3 sm:grid-cols-2 not-prose">
  <FactTile
    icon={ShieldCheck}
    label="Withdrawal scope"
    value="Never available"
  />
  <FactTile
    icon={CheckCircle2}
    label="Every trade / transfer"
    value="Confirmed by you first"
  />
</div>

<Callout type="caution" title="Risks">
  You are responsible for the trades your AI agent places. AI can make mistakes,
  act on outdated or hallucinated information, or send incorrect parameters —
  always verify before execution. Trading derivatives and margin carries
  substantial risk. See [Disclosures](#disclosures) below.
</Callout>

## What's an MCP?

Model Context Protocol (MCP) is an open standard that lets AI agents connect to external apps and
services. Instead of just answering questions, an AI with MCP access can take actions on your
behalf.

## What your agent can do

<div className="mt-4 grid grid-cols-1 gap-4 sm:grid-cols-2 not-prose">
  <ScenarioCard
    icon={TrendingUp}
    title="Check the market"
    description={
      '"What’s the current BTCUSDT price and 24h change?" — tickers, order books, candlesticks, funding rates.'
    }
  />
  <ScenarioCard
    icon={Wallet}
    title="Check your balance"
    description={
      '"Show my Agentic account balance across all wallets." — plus a read-only view of your main account.'
    }
  />
  <ScenarioCard
    icon={ShoppingCart}
    title="Trade"
    description={
      '"Buy $100 of BNB at market on spot." — Spot, Margin, Convert, USDⓈ-M Futures, and COIN-M Futures.'
    }
  />
  <ScenarioCard
    icon={Repeat}
    title="Move funds between wallets"
    description={
      '"Move 2,000 USDT from my Spot wallet to my USDⓈ-M wallet." — inside your Agentic sub-account only.'
    }
  />
</div>

## What your agent can access

When you connect, you choose which scopes to grant. Start with the least you need:

- **Market data** (public, no auth) — tickers, order books, candles, funding
- **Account** — Agentic sub-account balance, positions, bills; optional read-only view of your main
  account
- **Trade** — spot, margin, convert, futures (only what you grant and your account is authorized
  for)
- **Transfer** — move funds between wallets inside the same Agentic sub-account only

There is **no withdrawal scope**. Your agent can never move funds out of the sub-account to an
external address.

## Before you start

1. Log in to [Binance.com](https://www.binance.com) in your desktop browser — this feature is built
   for desktop, not mobile.
2. Make sure the AI client you plan to use is installed and open: Claude Code, Claude Desktop, Codex
   CLI, ChatGPT on the web, ChatGPT/Codex Desktop, VS Code, or Grok Bot.

<Callout type="caution" title="Don't paste the endpoint into a chat">
  Never paste the MCP endpoint into an AI chat and ask it to install the server,
  and never open the endpoint directly in your browser. Follow the setup steps
  for your client in the tabs below instead.
</Callout>

## Connect your AI agent

<Tabs defaultValue="claude-code" className="not-prose">
  <TabsList className="h-auto flex-wrap">
    <TabsTrigger value="claude-code">Claude Code</TabsTrigger>
    <TabsTrigger value="claude-desktop">Claude Desktop</TabsTrigger>
    <TabsTrigger value="codex-cli">Codex CLI</TabsTrigger>
    <TabsTrigger value="chatgpt-web">ChatGPT on the web</TabsTrigger>
    <TabsTrigger value="chatgpt-desktop">ChatGPT/Codex Desktop</TabsTrigger>
    <TabsTrigger value="vscode">VS Code</TabsTrigger>
    <TabsTrigger value="grok">Grok Bot</TabsTrigger>
    <TabsTrigger value="other">Other</TabsTrigger>
  </TabsList>

  <TabsContent value="claude-code" className="mt-4 rounded-lg border bg-card p-4">

**Step 1:** Open Terminal on macOS/Linux or PowerShell on Windows.

<br />

![macOS/Linux Terminal](/img/agent-native-mcp-server/install-macos-terminal.jpg)

<br />

![Windows PowerShell](/img/agent-native-mcp-server/install-windows-powershell.jpg)

<br />

**Step 2:** Run the following command to add the Binance MCP server:

```bash
claude mcp add binance-mcp-server --transport http https://agent.binance.com/mcp/agentic
```

<br />

![Claude Code terminal after adding the server](/img/agent-native-mcp-server/claude-code-mcp-add-command.png)

<br />

**Step 3:** Open the `/mcp` menu and select **binance-mcp-server**.

<br />

![Claude Code /mcp menu showing binance-mcp-server](/img/agent-native-mcp-server/claude-code-mcp-menu.png)

<br />

**Step 4:** Authenticate to authorize the connection.

<br />

![Binance Agentic Account Access consent screen](/img/agent-native-mcp-server/oauth-consent-claude-code.png)

  </TabsContent>

  <TabsContent value="claude-desktop" className="mt-4 rounded-lg border bg-card p-4">

**Step 1:** Open **Settings** and go to **Connectors**.

<br />

![Claude Desktop Connectors settings](/img/agent-native-mcp-server/claude-desktop-connectors.png)

<br />

**Step 2:** Click **Add custom connector**, then paste the URL below into the connector URL field:

```text
https://agent.binance.com/mcp/agentic
```

<br />

![Add custom connector dialog with the Binance MCP Server URL](/img/agent-native-mcp-server/claude-desktop-add-connector.png)

<br />

**Step 3:** Authenticate to authorize the connection.

**Step 4:** Return to Claude Desktop and confirm that **binance-mcp-server** shows as connected.

  </TabsContent>

  <TabsContent value="codex-cli" className="mt-4 rounded-lg border bg-card p-4">

**Step 1:** Open Terminal on macOS/Linux or PowerShell on Windows.

<br />

![macOS/Linux Terminal](/img/agent-native-mcp-server/install-macos-terminal.jpg)

<br />

![Windows PowerShell](/img/agent-native-mcp-server/install-windows-powershell.jpg)

<br />

**Step 2:** Run the following command to add the Binance MCP server:

```bash
codex mcp add binance-mcp-server --url https://agent.binance.com/mcp/agentic --oauth-client-id codex
```

<br />

![Codex CLI terminal after adding the server](/img/agent-native-mcp-server/codex-cli-mcp-add-command.png)

<br />

**Step 3:** Authenticate to authorize the connection.

<br />

![Binance Agentic Account Access consent screen for Codex](/img/agent-native-mcp-server/oauth-consent-codex.png)

  </TabsContent>

  <TabsContent value="chatgpt-web" className="mt-4 rounded-lg border bg-card p-4">

**Step 1:** Enable **Developer Mode** under **Settings → Security and login**.

<br />

![ChatGPT Developer Mode setting](/img/agent-native-mcp-server/chatgpt-web-developer-mode.png)

<br />

**Step 2:** Open **Plugins** and click the **"+"** button (**New Plugin**).

<br />

![ChatGPT Plugins page](/img/agent-native-mcp-server/chatgpt-web-plugins.png)

<br />

**Step 3:** Enter a name for the plugin, paste the URL below into the plugin URL field, and then
click **Create**:

```text
https://agent.binance.com/mcp/agentic
```

<br />

![New Plugin dialog with the Binance MCP Server URL](/img/agent-native-mcp-server/chatgpt-web-new-plugin.png)

<br />

**Step 4:** Authenticate to authorize the connection.

<br />

![Binance Agentic Account Access consent screen for ChatGPT](/img/agent-native-mcp-server/oauth-consent-chatgpt-web.png)

<br />

**Step 5:** Return to ChatGPT and confirm that **binance-mcp-server** is available in Plugins.

  </TabsContent>

  <TabsContent value="chatgpt-desktop" className="mt-4 rounded-lg border bg-card p-4">

**Step 1:** Install Codex CLI, if you haven't already.

<br />

![macOS/Linux Terminal](/img/agent-native-mcp-server/install-macos-terminal.jpg)

<br />

![Windows PowerShell](/img/agent-native-mcp-server/install-windows-powershell.jpg)

<br />

For macOS/Linux:

```bash
curl -fsSL https://chatgpt.com/codex/install.sh | sh
```

For Windows:

```bash
powershell -ExecutionPolicy ByPass -c "irm https://chatgpt.com/codex/install.ps1 | iex"
```

**Step 2:** Open a new terminal and run the following command to add the Binance MCP server:

```bash
codex mcp add binance-mcp-server --url https://agent.binance.com/mcp/agentic --oauth-client-id codex
```

<br />

![Terminal running the codex mcp add command](/img/agent-native-mcp-server/chatgpt-codex-desktop-mcp-add-command.png)

<br />

**Step 3:** Authenticate to authorize the connection.

**Step 4:** Open the Codex/ChatGPT desktop app — your account should be connected.

  </TabsContent>

  <TabsContent value="vscode" className="mt-4 rounded-lg border bg-card p-4">

**Step 1:** Open the Chat panel and click the gear icon.

<br />

![VS Code Chat panel settings](/img/agent-native-mcp-server/vscode-chat-settings.png)

<br />

**Step 2:** Select **MCP Servers**, click **+**, then select **HTTP (HTTP or Server-Sent Events)**.

<br />

![Add MCP server dialog with the HTTP option selected](/img/agent-native-mcp-server/vscode-mcp-servers-add-http.png)

<br />

**Step 3:** Paste the URL below into the server URL field, enter `binance-mcp-server` as the server
name, and confirm:

```text
https://agent.binance.com/mcp/agentic
```

**Step 4:** Authenticate to authorize the connection.

<br />

![Binance Agentic Account Access consent screen for VS Code](/img/agent-native-mcp-server/oauth-consent-vscode.png)

  </TabsContent>

  <TabsContent value="grok" className="mt-4 rounded-lg border bg-card p-4">

**Step 1:** Open Grok Bot and enter the following prompt:

```
add binance-mcp-server to this bot, use below settings:
url = "https://agent.binance.com/mcp/agentic"
oauth_client_id = "grok"
```

**Step 2:** When prompted, authenticate to authorize the connection.

<br />

![Grok Bot chat confirming the Binance MCP server was added](/img/agent-native-mcp-server/grok-add-mcp-prompt.png)

  </TabsContent>

  <TabsContent value="other" className="mt-4 rounded-lg border bg-card p-4">

Our team will continue expanding support to other platforms. If you'd like us to support a specific
platform, please contact Binance Customer Support via
[Live Chat](https://www.binance.com/en/chat?sourceEntry=4).

  </TabsContent>
</Tabs>

## Check that the connection works

1. In your AI client's chat, enter: **"Use the Binance MCP Server to show the current BTCUSDT price
   and 24-hour change."**
2. Confirm the response shows the Binance MCP tool being used and returns live BTCUSDT market data.

## Open and fund an Agentic sub-account

Your agent trades inside a dedicated sub-account, isolated from your main account. If you don't have
one, the onboarding flow prompts you to create one when you first authorize.

The sub-account starts empty. Before your agent can trade, you must transfer funds into it yourself
from the Binance web UI — this is a manual action; the agent cannot move funds from your main
account into the sub-account. Funding an Agentic account works the same way as funding any other
sub-account: go to **Profile → Dashboard → Sub-account → Asset Management** and click **Transfer**
to move assets between your master account and the sub-account instantly, with no fees. Fund it via:

[https://www.binance.com/en/my/sub-account/asset-management/transfer?asset=BTC](https://www.binance.com/en/my/sub-account/asset-management/transfer?asset=BTC)

We recommend funding it with only what you're willing to let the agent trade.

Note: the **Transfer** scope only lets the agent move funds _between wallets inside_ the sub-account
(e.g. Spot → USDⓈ-M). It cannot pull funds from your main account — that first deposit is always the
manual step above.

## Example: your first session

Once connected and funded, you interact in plain language. The agent reads live data and asks you to
confirm before anything that moves funds or places an order.

<div className="mt-4 grid grid-cols-1 gap-4 sm:grid-cols-2 not-prose">
  <StepCard
    number={1}
    icon={Eye}
    title="Check the market (read-only — runs immediately)"
    quote="What's BTCUSDT trading at, and how's it moved over 24h?"
    outcome="The agent pulls the live ticker and summarizes price and 24h change. No confirmation needed — reads never touch your balance."
  />
  <StepCard
    number={2}
    icon={Wallet}
    title="Check your balance"
    quote="What do I have in my Agentic account?"
    outcome="The agent reads your sub-account balances across Spot, Margin, and Futures wallets. If it's empty, fund it first (see above)."
  />
  <StepCard
    number={3}
    icon={ShoppingCart}
    title="Place a trade (write — the agent confirms first)"
    quote="Buy $100 of BNB at market on spot."
    outcome="The agent restates the order — symbol, side, type, amount — and waits for your yes before sending it. Always verify the details here; this is the step that spends real funds."
  />
  <StepCard
    number={4}
    icon={CheckCircle2}
    title="Verify the result"
    quote="Did that fill? What's my BNB balance now?"
    outcome="The agent checks the order status and your updated balance."
  />
</div>

This confirm-before-execute pattern applies to every non-read action — orders, cancels, and
transfers between your sub-account wallets.

## Manage your Agentic account

You can manage your Agentic account directly from [Binance.com](https://www.binance.com), without
your agent.

Go to **Profile → Dashboard → Sub-account → Account Management**. Here you'll see all your
sub-accounts, including your Agentic accounts. Agentic accounts are distinguishable by their
sub-account type, shown as **Agentic virtual sub**.

From here you can perform four actions:

1. **Transfer** — fund or withdraw funds from the sub-account.
2. **View permissions** — verify your Agentic account permissions. Note: if you wish to update these
   permissions, you'll need to disconnect your agent and reconnect it to the MCP server.
3. **Disconnect agents** — select one or more agents to disconnect. You can re-connect your agents
   to this account later if you wish. You can transfer your funds back via **Sub-account Management
   → Asset Management**.
4. **Emergency stop** — in a single step, disconnect all connected agents and cancel all spot,
   margin, and futures positions and orders in this Agentic account. You can re-connect your agents
   to this account again later if you wish. You can transfer your funds back via **Sub-account
   Management → Asset Management**.

## Troubleshooting

- **I opened the endpoint in my browser** — close the page and follow the connection steps for your
  AI client above instead.
- **I pasted the endpoint into the AI chat** — remove the connection the AI created, then repeat the
  exact setup steps in this guide.
- **The command isn't recognized** — confirm the required AI client or CLI is installed, reopen
  Terminal or PowerShell, and try again.
- **The server was added but can't be used** — reconnect it, authenticate, and repeat the connection
  check above.
- Make sure the endpoint is exactly `https://agent.binance.com/mcp/agentic`.
- **Market data works but account or trading actions don't** — reconnect and grant the **Account**
  or **Trade** scope you need.
- If a trade fails with an insufficient-balance error, the sub-account has no funds — transfer funds
  into it first (see "Open and fund an Agentic sub-account").
- If the authorization expired, disconnect and reconnect the Binance MCP Server.
- To revoke access: **Profile → Dashboard → Sub-account → Account Management → Disconnect agents**.

## Getting help

If you need help while integrating:

- Review the relevant documentation first
- Check available tools, examples, and sample applications
- Contact Binance Customer Support via [Live Chat](https://www.binance.com/en/chat?sourceEntry=4) if
  you need further assistance

## Disclosures

Disclaimer: The Binance MCP Server is a Binance AI Tool that facilitates AI-assisted trading and
does not constitute any advice. Binance is not responsible for losses resulting from agent-generated
decisions. You are solely responsible for supervising your agent's activity, configuring scopes, and
verifying actions. Use of AI Tools may be subject to additional
[Binance Product Terms](https://www.binance.com/en/about-legal/product-terms), where applicable. For
more information, see our [Terms of Use](https://www.binance.com/en/terms), and
[Risk Warning](https://www.binance.com/en/risk-warning) and
[AI Policy and Terms](https://www.binance.com/en/about-legal/AI-Policy). For Binance FZE users, the
use of Binance AI may be subject to additional
[Binance Product Terms](https://www.binance.com/en/about-legal/product-terms), where applicable. For
more information on the terms applicable to Binance FZE users, please refer to our
[Terms of Use](https://www.binance.com/en/terms),
[Risk Warning](https://www.binance.com/en/risk-warning) and
[AI Policy and Terms](https://www.binance.com/en/about-legal/AI-Policy).

---

# Binance MCP Server

<!-- SYNCED FROM be/agentic-tools@d3e0564fcb973e8686974a42b8e063d4fc25d053 docs/binance-mcp-server.md on 2026-08-17 -->
<!-- This MCP server is operated by Binance's AI team; mirrored here as our discovery entry point. -->

<!-- To check for drift: git log d3e0564fcb973e8686974a42b8e063d4fc25d053..HEAD -- docs/binance-mcp-server.md in be/agentic-tools -->

<!-- Layout (hero/fact tiles/callout/scenario cards/tabs/step cards) is a local redesign on top of the -->
<!-- synced text above — if you resync content, re-apply these components rather than pasting plain markdown. -->

import { Callout } from "zudoku/ui/Callout";
import { Tabs, TabsList, TabsTrigger, TabsContent } from "zudoku/ui/Tabs";
import {
  TrendingUp,
  ShieldCheck,
  CheckCircle2,
  Wallet,
  ShoppingCart,
  Repeat,
  Eye,
} from "lucide-react";

export const IconTile = ({ children, label }) => (
  <span
    className="inline-flex h-10 w-10 items-center justify-center rounded-lg border bg-muted"
    aria-label={label}
    title={label}
  >
    {children}
  </span>
);

export const FactTile = ({ icon: Icon, label, value }) => (
  <div className="not-prose flex items-center gap-3 rounded-xl border bg-card p-4">
    <div className="inline-flex h-9 w-9 shrink-0 items-center justify-center rounded-lg border bg-muted/40">
      <Icon className="h-4 w-4 text-muted-foreground" aria-hidden />
    </div>
    <div className="min-w-0">
      <p className="text-xs text-muted-foreground">{label}</p>
      <p className="text-sm font-medium break-all">{value}</p>
    </div>
  </div>
);

export const ScenarioCard = ({ icon: Icon, title, description }) => (
  <div className="not-prose rounded-xl border bg-card p-4 transition-colors hover:border-primary/30 hover:bg-primary/5">
    <div className="mb-3 inline-flex h-10 w-10 items-center justify-center rounded-xl border bg-muted/40">
      <Icon className="h-5 w-5 text-muted-foreground" />
    </div>
    <h4 className="text-sm font-semibold">{title}</h4>
    <p className="mt-1 text-xs leading-5 text-muted-foreground">
      {description}
    </p>
  </div>
);

export const StepCard = ({ number, icon: Icon, title, quote, outcome }) => (
  <div className="not-prose rounded-xl border bg-card p-4">
    <div className="mb-3 flex items-center gap-2">
      <span className="inline-flex h-6 w-6 items-center justify-center rounded-full bg-primary text-xs font-semibold text-primary-foreground">
        {number}
      </span>
      <Icon className="h-4 w-4 text-muted-foreground" aria-hidden />
      <h4 className="text-sm font-semibold">{title}</h4>
    </div>
    <p className="text-sm italic text-muted-foreground">"{quote}"</p>
    <p className="mt-2 text-xs leading-5 text-muted-foreground">{outcome}</p>
  </div>
);

<div className="not-prose -mt-2 mb-6 rounded-2xl border bg-[radial-gradient(circle_at_top_right,rgba(240,185,11,0.08),transparent_50%)] p-6">
  <div className="flex items-center gap-3 mb-3">
    <div className="inline-flex h-12 w-12 items-center justify-center rounded-xl border bg-primary/10">
      <TrendingUp className="h-6 w-6 text-primary" />
    </div>
    <div>
      <p className="text-xs font-semibold uppercase tracking-[0.16em] text-primary">
        Binance MCP Server
      </p>
    </div>
  </div>
  <p className="text-sm leading-6 text-muted-foreground">
    一个 URL 就能把你的 AI agent 连接到 Binance。你的 agent
    可以读取市场数据、查询余额，并在专属的 Agentic 子账户内交易 Spot / Margin /
    Convert / USDⓈ-M / COIN-M 合约，还能在子账户各钱包之间转账——
    不需要本地安装，不需要把 API key 放在你的设备上。
  </p>
</div>

<div className="mb-6 grid grid-cols-1 gap-3 sm:grid-cols-2 not-prose">
  <FactTile icon={ShieldCheck} label="提现权限" value="永远不会开放" />
  <FactTile icon={CheckCircle2} label="每一笔交易/转账" value="都先经你确认" />
</div>

<Callout type="caution" title="风险">
  你的 AI agent 下的每一笔交易，责任都在你自己。AI
  可能出错，可能基于过时或幻觉出来的信息行动，也可能发出错误的参数——执行前务必自行核实。交易衍生品和杠杆产品有很大风险，详见下方[Disclosures](#disclosures)。
</Callout>

## MCP 是什么？

Model Context Protocol（MCP）是一个开放标准，让 AI
agent 能够连接外部应用和服务。有了 MCP 接入权限，AI 不再只是回答问题，还可以代表你执行操作。

## 你的 agent 能做什么

<div className="mt-4 grid grid-cols-1 gap-4 sm:grid-cols-2 not-prose">
  <ScenarioCard
    icon={TrendingUp}
    title="查看市场"
    description={
      '"BTCUSDT 现在的价格是多少，24 小时涨跌幅多少？" —— 最新价格、订单簿、K 线、资金费率。'
    }
  />
  <ScenarioCard
    icon={Wallet}
    title="查询余额"
    description={
      '"查一下我的 Agentic 账户在所有钱包里的余额。" —— 以及主账户的只读视图。'
    }
  />
  <ScenarioCard
    icon={ShoppingCart}
    title="交易"
    description={
      '"在 spot 用市价买 100 美元的 BNB。" —— Spot、Margin、Convert、USDⓈ-M 合约、COIN-M 合约。'
    }
  />
  <ScenarioCard
    icon={Repeat}
    title="在钱包之间转账"
    description={
      '"把 2,000 USDT 从我的 Spot 钱包转到 USDⓈ-M 钱包。" —— 仅限 Agentic 子账户内部。'
    }
  />
</div>

## 你的 agent 能访问什么

连接时，你自己选择授予哪些权限范围。建议先给最小必要权限：

- **市场数据**（公开，无需鉴权）——最新价格、订单簿、K 线、资金费率
- **账户**——Agentic 子账户余额、仓位、账单；可选授予主账户的只读视图
- **交易**——spot、margin、convert、合约（仅限你授权且账户本身有权限的部分）
- **转账**——只能在同一个 Agentic 子账户内部的钱包之间转账

**没有提现权限**。你的 agent 永远无法把资金从子账户转到外部地址。

## 开始之前

1. 在桌面浏览器里登录
   [Binance.com](https://www.binance.com)——这个功能是给桌面端设计的，不支持移动端。
2. 确认你要用的 AI 客户端已经安装并打开：Claude Code、Claude Desktop、Codex CLI、ChatGPT on the
   web、ChatGPT/Codex Desktop、VS Code 或 Grok Bot。

<Callout type="caution" title="不要把 endpoint 粘进对话">
  不要把 MCP endpoint 粘贴到 AI 对话里让它帮你安装，也不要在浏览器里直接打开这个
  endpoint。请按下方各客户端 tab 里的步骤操作。
</Callout>

## 连接你的 AI agent

<Tabs defaultValue="claude-code" className="not-prose">
  <TabsList className="h-auto flex-wrap">
    <TabsTrigger value="claude-code">Claude Code</TabsTrigger>
    <TabsTrigger value="claude-desktop">Claude Desktop</TabsTrigger>
    <TabsTrigger value="codex-cli">Codex CLI</TabsTrigger>
    <TabsTrigger value="chatgpt-web">ChatGPT on the web</TabsTrigger>
    <TabsTrigger value="chatgpt-desktop">ChatGPT/Codex Desktop</TabsTrigger>
    <TabsTrigger value="vscode">VS Code</TabsTrigger>
    <TabsTrigger value="grok">Grok Bot</TabsTrigger>
    <TabsTrigger value="other">其他</TabsTrigger>
  </TabsList>

  <TabsContent value="claude-code" className="mt-4 rounded-lg border bg-card p-4">

**第 1 步：** 打开 macOS/Linux 上的 Terminal，或 Windows 上的 PowerShell。

<br />

![macOS/Linux Terminal](/img/agent-native-mcp-server/install-macos-terminal.jpg)

<br />

![Windows PowerShell](/img/agent-native-mcp-server/install-windows-powershell.jpg)

<br />

**第 2 步：** 运行以下命令添加 Binance MCP server：

```bash
claude mcp add binance-mcp-server --transport http https://agent.binance.com/mcp/agentic
```

<br />

![添加完成后的 Claude Code 终端](/img/agent-native-mcp-server/claude-code-mcp-add-command.png)

<br />

**第 3 步：** 打开 `/mcp` 菜单，选择 **binance-mcp-server**。

<br />

![Claude Code /mcp 菜单显示 binance-mcp-server](/img/agent-native-mcp-server/claude-code-mcp-menu.png)

<br />

**第 4 步：** 完成身份验证以授权连接。

<br />

![Binance Agentic Account Access 授权确认页](/img/agent-native-mcp-server/oauth-consent-claude-code.png)

  </TabsContent>

  <TabsContent value="claude-desktop" className="mt-4 rounded-lg border bg-card p-4">

**第 1 步：** 打开 **Settings**，进入 **Connectors**。

<br />

![Claude Desktop Connectors 设置页](/img/agent-native-mcp-server/claude-desktop-connectors.png)

<br />

**第 2 步：** 点击 **Add custom connector**，把下面的 URL 粘贴到 connector URL 输入框里：

```text
https://agent.binance.com/mcp/agentic
```

<br />

![Add custom connector 对话框，已填入 Binance MCP Server URL](/img/agent-native-mcp-server/claude-desktop-add-connector.png)

<br />

**第 3 步：** 完成身份验证以授权连接。

**第 4 步：** 回到 Claude Desktop，确认 **binance-mcp-server** 显示为已连接。

  </TabsContent>

  <TabsContent value="codex-cli" className="mt-4 rounded-lg border bg-card p-4">

**第 1 步：** 打开 macOS/Linux 上的 Terminal，或 Windows 上的 PowerShell。

<br />

![macOS/Linux Terminal](/img/agent-native-mcp-server/install-macos-terminal.jpg)

<br />

![Windows PowerShell](/img/agent-native-mcp-server/install-windows-powershell.jpg)

<br />

**第 2 步：** 运行以下命令添加 Binance MCP server：

```bash
codex mcp add binance-mcp-server --url https://agent.binance.com/mcp/agentic --oauth-client-id codex
```

<br />

![添加完成后的 Codex CLI 终端](/img/agent-native-mcp-server/codex-cli-mcp-add-command.png)

<br />

**第 3 步：** 完成身份验证以授权连接。

<br />

![Codex 的 Binance Agentic Account Access 授权确认页](/img/agent-native-mcp-server/oauth-consent-codex.png)

  </TabsContent>

  <TabsContent value="chatgpt-web" className="mt-4 rounded-lg border bg-card p-4">

**第 1 步：** 在 **Settings → Security and login** 里开启 **Developer Mode**。

<br />

![ChatGPT Developer Mode 设置](/img/agent-native-mcp-server/chatgpt-web-developer-mode.png)

<br />

**第 2 步：** 打开 **Plugins**，点击 **"+"** 按钮（**New Plugin**）。

<br />

![ChatGPT Plugins 页面](/img/agent-native-mcp-server/chatgpt-web-plugins.png)

<br />

**第 3 步：** 给插件命名，把下面的 URL 粘贴到 plugin URL 输入框里，然后点击 **Create**：

```text
https://agent.binance.com/mcp/agentic
```

<br />

![New Plugin 对话框，已填入 Binance MCP Server URL](/img/agent-native-mcp-server/chatgpt-web-new-plugin.png)

<br />

**第 4 步：** 完成身份验证以授权连接。

<br />

![ChatGPT 的 Binance Agentic Account Access 授权确认页](/img/agent-native-mcp-server/oauth-consent-chatgpt-web.png)

<br />

**第 5 步：** 回到 ChatGPT，确认 **binance-mcp-server** 已出现在 Plugins 里。

  </TabsContent>

  <TabsContent value="chatgpt-desktop" className="mt-4 rounded-lg border bg-card p-4">

**第 1 步：** 如果还没安装 Codex CLI，先安装它。

<br />

![macOS/Linux Terminal](/img/agent-native-mcp-server/install-macos-terminal.jpg)

<br />

![Windows PowerShell](/img/agent-native-mcp-server/install-windows-powershell.jpg)

<br />

macOS/Linux：

```bash
curl -fsSL https://chatgpt.com/codex/install.sh | sh
```

Windows：

```bash
powershell -ExecutionPolicy ByPass -c "irm https://chatgpt.com/codex/install.ps1 | iex"
```

**第 2 步：** 打开一个新终端，运行以下命令添加 Binance MCP server：

```bash
codex mcp add binance-mcp-server --url https://agent.binance.com/mcp/agentic --oauth-client-id codex
```

<br />

![运行 codex mcp add 命令的终端](/img/agent-native-mcp-server/chatgpt-codex-desktop-mcp-add-command.png)

<br />

**第 3 步：** 完成身份验证以授权连接。

**第 4 步：** 打开 Codex/ChatGPT 桌面应用——你的账户应该已经连接。

  </TabsContent>

  <TabsContent value="vscode" className="mt-4 rounded-lg border bg-card p-4">

**第 1 步：** 打开 Chat 面板，点击齿轮图标。

<br />

![VS Code Chat 面板设置](/img/agent-native-mcp-server/vscode-chat-settings.png)

<br />

**第 2 步：** 选择 **MCP Servers**，点击 **+**，再选择 **HTTP (HTTP or Server-Sent Events)**。

<br />

![Add MCP server 对话框，已选中 HTTP 选项](/img/agent-native-mcp-server/vscode-mcp-servers-add-http.png)

<br />

**第 3 步：** 把下面的 URL 粘贴到 server URL 输入框里，输入 `binance-mcp-server`
作为 server 名称并确认：

```text
https://agent.binance.com/mcp/agentic
```

**第 4 步：** 完成身份验证以授权连接。

<br />

![VS Code 的 Binance Agentic Account Access 授权确认页](/img/agent-native-mcp-server/oauth-consent-vscode.png)

  </TabsContent>

  <TabsContent value="grok" className="mt-4 rounded-lg border bg-card p-4">

**第 1 步：** 打开 Grok Bot，输入以下提示词：

```
add binance-mcp-server to this bot, use below settings:
url = "https://agent.binance.com/mcp/agentic"
oauth_client_id = "grok"
```

**第 2 步：** 出现提示时，完成身份验证以授权连接。

<br />

![Grok Bot 对话确认 Binance MCP server 已添加](/img/agent-native-mcp-server/grok-add-mcp-prompt.png)

  </TabsContent>

  <TabsContent value="other" className="mt-4 rounded-lg border bg-card p-4">

我们团队会持续扩展对其他平台的支持。如果你希望我们支持某个特定平台，请通过[在线客服](https://www.binance.com/zh-CN/chat?sourceEntry=4)联系 Binance 客服。

  </TabsContent>
</Tabs>

## 确认连接是否成功

1. 在你的 AI 客户端对话里输入：**"Use the Binance MCP Server to show the current BTCUSDT price and
   24-hour change."**
2. 确认返回结果显示调用了 Binance MCP 工具，并返回了实时的 BTCUSDT 行情数据。

## 开通并给 Agentic 子账户充值

你的 agent 在一个专属的子账户内交易，与你的主账户是隔离的。如果你还没有这个子账户，第一次授权时的引导流程会提示你创建。

子账户刚开通时是空的。在 agent 能交易之前，你需要自己从 Binance 网页端把资金转进去——这是一个手动操作，agent 无法把资金从你的主账户转进子账户。给 Agentic 账户充值的方式跟给其他子账户充值一样：进入
**Profile → Dashboard → Sub-account → Asset Management**，点击
**Transfer**，即可在主账户和子账户之间即时转账，无手续费。入口：

[https://www.binance.com/en/my/sub-account/asset-management/transfer?asset=BTC](https://www.binance.com/en/my/sub-account/asset-management/transfer?asset=BTC)

建议只转入你愿意让 agent 交易的那部分资金。

注意：**Transfer** 权限只允许 agent 在子账户*内部*的钱包之间转账（比如 Spot →
USDⓈ-M）。它不能从你的主账户拉取资金——首次入金始终是上面这个手动步骤。

## 示例：你的第一次使用

连接并充值完成后，你就可以用自然语言跟它交互了。agent 会先读取实时数据，在任何涉及资金变动或下单的操作之前都会先让你确认。

<div className="mt-4 grid grid-cols-1 gap-4 sm:grid-cols-2 not-prose">
  <StepCard
    number={1}
    icon={Eye}
    title="查看市场（只读——立即执行）"
    quote="BTCUSDT 现在交易价格多少，24 小时怎么变化的？"
    outcome="agent 拉取实时行情，总结价格和 24 小时涨跌幅。不需要确认——只读操作不会动到你的余额。"
  />
  <StepCard
    number={2}
    icon={Wallet}
    title="查看余额"
    quote="我的 Agentic 账户里有什么？"
    outcome="agent 读取你子账户在 Spot、Margin、Futures 各钱包的余额。如果是空的，先按上面的方法充值。"
  />
  <StepCard
    number={3}
    icon={ShoppingCart}
    title="下单交易（写操作——agent 会先确认）"
    quote="在 spot 用市价买 100 美元的 BNB。"
    outcome="agent 会复述这笔订单的细节——交易对、方向、类型、金额——并等你回复确认之后才会真正下单。这一步动用真实资金，务必仔细核对。"
  />
  <StepCard
    number={4}
    icon={CheckCircle2}
    title="确认结果"
    quote="成交了吗？我现在的 BNB 余额是多少？"
    outcome="agent 会查询订单状态和你更新后的余额。"
  />
</div>

这种"先确认再执行"的模式适用于所有非只读操作——下单、撤单，以及子账户各钱包之间的转账。

## 管理你的 Agentic 账户

你也可以直接在 [Binance.com](https://www.binance.com) 上管理你的 Agentic 账户，不需要通过 agent。

进入 **Profile → Dashboard → Sub-account → Account
Management**，这里能看到你所有的子账户，包括 Agentic 账户。Agentic 账户在子账户类型里会标注为
**Agentic virtual sub**。

在这里你可以做四件事：

1. **Transfer**——给子账户充值或提现。
2. **View
   permissions**——查看你的 Agentic 账户权限。注意：如果想修改这些权限，需要先断开 agent 连接，再重新连接到 MCP
   server。
3. **Disconnect
   agents**——选择一个或多个 agent 断开连接。之后如果你想要，还可以重新连接。资金可以通过
   **Sub-account Management → Asset Management** 转回来。
4. **Emergency
   stop**——一步操作断开所有已连接的 agent，并取消这个 Agentic 账户里所有 spot、margin、合约的仓位和挂单。之后如果你想要，还可以重新连接 agent。资金可以通过
   **Sub-account Management → Asset Management** 转回来。

## 故障排查

- **我在浏览器里打开了这个 endpoint**——关闭页面，改按上面对应 AI 客户端的连接步骤操作。
- **我把 endpoint 粘贴到了 AI 对话里**——删除 AI 创建的那个连接，再按本指南的步骤重新操作一遍。
- **命令无法识别**——确认所需的 AI 客户端或 CLI 已经安装，重新打开 Terminal 或 PowerShell 再试一次。
- **server 添加成功但用不了**——重新连接、完成身份验证，再重复一遍上面的连接检查。
- 确认 endpoint 完全是 `https://agent.binance.com/mcp/agentic`。
- **市场数据能用，但账户或交易操作不行**——重新连接，并授予你需要的 **Account** 或 **Trade** 权限。
- 如果交易因为余额不足失败，说明子账户里没有资金——先按"开通并给 Agentic 子账户充值"那一节转入资金。
- 如果授权过期了，断开重连一次 Binance MCP Server。
- 撤销访问权限：**Profile → Dashboard → Sub-account → Account Management → Disconnect agents**。

## 获取帮助

如果在接入过程中需要帮助：

- 先查阅相关文档
- 检查现有的工具、示例和示例应用
- 如需进一步帮助，请通过[在线客服](https://www.binance.com/zh-CN/chat?sourceEntry=4)联系 Binance 客服

## Disclosures

Disclaimer：Binance MCP Server 是 Binance 提供的一项 AI
Tool，用于提供 AI 辅助交易能力，不构成任何建议。因 agent 生成的决策导致的损失，Binance 不承担责任。你需要自行负责监督 agent 的活动、配置权限范围，并核实每一步操作。使用 AI
Tools 可能还需遵守额外的
[Binance Product Terms](https://www.binance.com/en/about-legal/product-terms)（如适用）。更多信息详见我们的
[Terms of Use](https://www.binance.com/en/terms)、[Risk Warning](https://www.binance.com/en/risk-warning)
以及 [AI Policy and Terms](https://www.binance.com/en/about-legal/AI-Policy)。对于 Binance
FZE 用户，使用 Binance AI 可能还需遵守额外的
[Binance Product Terms](https://www.binance.com/en/about-legal/product-terms)（如适用）。有关适用于 Binance
FZE 用户的条款，更多信息请参阅我们的
[Terms of Use](https://www.binance.com/en/terms)、[Risk Warning](https://www.binance.com/en/risk-warning)
以及 [AI Policy and Terms](https://www.binance.com/en/about-legal/AI-Policy)。