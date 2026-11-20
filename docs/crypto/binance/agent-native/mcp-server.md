---
exchange: binance
source_url: https://developers.binance.com/en/docs/agent-native/mcp-server
api_type: Guide
updated_at: 2026-11-20 18:28:27.199451
---

# MCP Server

[Model Context Protocol](https://modelcontextprotocol.io/) (MCP) is an open standard that lets AI
agents and coding assistants connect to external tools and data sources over a single, well-defined
transport — instead of every integration needing its own custom API glue.

import { Link } from "zudoku/components";
import { Card, CardHeader, CardTitle, CardDescription } from "zudoku/ui/Card";
import { TrendingUp, ChevronRight } from "lucide-react";

export const IconTile = ({ children, label }) => (
  <span
    className="inline-flex h-10 w-10 items-center justify-center rounded-lg border bg-muted"
    aria-label={label}
    title={label}
  >
    {children}
  </span>
);

export const Badge = ({ children }) => (
  <span className="inline-flex items-center rounded-md border bg-muted px-2 py-1 text-xs font-semibold text-foreground">
    {children}
  </span>
);

export const CardLink = ({ to, title, description, children, badge }) => (
  <div className="not-prose group relative rounded-xl">
    <Link
      to={to}
      className="absolute inset-0 z-0 rounded-xl focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 focus-visible:ring-offset-background"
      aria-label={title}
    />
    <Card className="pointer-events-none flex h-full flex-col transition-all group-hover:-translate-y-0.5 group-hover:shadow-md">
      <CardHeader className="flex-1">
        <div className="flex items-center gap-2">
          {children}
          {badge && <Badge>{badge}</Badge>}
        </div>
        <CardTitle className="mt-3 text-base">{title}</CardTitle>
        <CardDescription className="mt-1">{description}</CardDescription>
        <span className="pointer-events-none mt-3 inline-flex items-center gap-1 text-xs font-medium text-primary">
          Learn more <ChevronRight className="h-3 w-3" />
        </span>
      </CardHeader>
    </Card>
  </div>
);

<div className="mt-4 grid grid-cols-1 gap-4 sm:grid-cols-2 not-prose">
  <CardLink
    to="/agent-native/mcp-server/agentic"
    title="Binance MCP Server"
    description="Connect your AI agent to Binance to read market data, check balances, and trade Spot / Margin / Convert / Futures inside a dedicated Agentic sub-account."
    badge="Trading"
  >
    <IconTile label="Binance MCP Server">
      <TrendingUp className="h-5 w-5" aria-hidden />
    </IconTile>
  </CardLink>
</div>

## Who this is for

- **Building a trading bot or want an AI agent to act on your Binance account?** Use the
  [Binance MCP Server](/agent-native/mcp-server/agentic).

---

# MCP Server

[模型上下文协议](https://modelcontextprotocol.io/)（Model Context
Protocol，MCP）是一个开放标准，让 AI
agent 和编程助手能够通过一套统一的传输方式连接外部工具和数据源，而不需要每个集成都单独写一套 API 对接代码。

import { Link } from "zudoku/components";
import { Card, CardHeader, CardTitle, CardDescription } from "zudoku/ui/Card";
import { TrendingUp, ChevronRight } from "lucide-react";

export const IconTile = ({ children, label }) => (
  <span
    className="inline-flex h-10 w-10 items-center justify-center rounded-lg border bg-muted"
    aria-label={label}
    title={label}
  >
    {children}
  </span>
);

export const Badge = ({ children }) => (
  <span className="inline-flex items-center rounded-md border bg-muted px-2 py-1 text-xs font-semibold text-foreground">
    {children}
  </span>
);

export const CardLink = ({ to, title, description, children, badge }) => (
  <div className="not-prose group relative rounded-xl">
    <Link
      to={to}
      className="absolute inset-0 z-0 rounded-xl focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 focus-visible:ring-offset-background"
      aria-label={title}
    />
    <Card className="pointer-events-none flex h-full flex-col transition-all group-hover:-translate-y-0.5 group-hover:shadow-md">
      <CardHeader className="flex-1">
        <div className="flex items-center gap-2">
          {children}
          {badge && <Badge>{badge}</Badge>}
        </div>
        <CardTitle className="mt-3 text-base">{title}</CardTitle>
        <CardDescription className="mt-1">{description}</CardDescription>
        <span className="pointer-events-none mt-3 inline-flex items-center gap-1 text-xs font-medium text-primary">
          了解更多 <ChevronRight className="h-3 w-3" />
        </span>
      </CardHeader>
    </Card>
  </div>
);

<div className="mt-4 grid grid-cols-1 gap-4 sm:grid-cols-2 not-prose">
  <CardLink
    to="/agent-native/mcp-server/agentic"
    title="Binance MCP Server"
    description="把你的 AI agent 连接到 Binance，读取市场数据、查询余额，并在专属的 Agentic 子账户内交易 Spot / Margin / Convert / 合约。"
    badge="交易"
  >
    <IconTile label="Binance MCP Server">
      <TrendingUp className="h-5 w-5" aria-hidden />
    </IconTile>
  </CardLink>
</div>

## 适用人群

- **在开发交易机器人，或者想让 AI agent 代表你操作 Binance 账户？** 用
  [Binance MCP Server](/agent-native/mcp-server/agentic)。