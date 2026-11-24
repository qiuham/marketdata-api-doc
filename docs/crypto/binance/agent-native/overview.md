---
exchange: binance
source_url: https://developers.binance.com/en/docs/agent-native/overview
api_type: Guide
updated_at: 2026-11-24 18:27:06.796575
---

# Agent Native

import { Link } from "zudoku/components";
import { Card, CardHeader, CardTitle, CardDescription } from "zudoku/ui/Card";
import {
  Bot,
  FileText,
  Plug,
  ChevronRight,
  Code2,
  Lightbulb,
  Users,
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

<div className="not-prose -mt-2 mb-8 rounded-2xl border bg-[radial-gradient(circle_at_top_right,rgba(240,185,11,0.08),transparent_50%)] p-6">
  <div className="flex items-center gap-3 mb-3">
    <div className="inline-flex h-12 w-12 items-center justify-center rounded-xl border bg-primary/10">
      <Bot className="h-6 w-6 text-primary" />
    </div>
    <div>
      <p className="text-xs font-semibold uppercase tracking-[0.16em] text-primary">
        Agent Native
      </p>
    </div>
  </div>
  <p className="text-sm leading-6 text-muted-foreground">
    Lightweight, AI-friendly access to Binance API documentation. Discover and
    load full documentation programmatically — built for AI tools, coding
    assistants, and autonomous agents.
  </p>
</div>

## Core Components

<div className="mt-1 text-sm text-muted-foreground">
  Choose the integration method that fits your use case.
</div>

<div className="mt-4 grid grid-cols-1 gap-4 sm:grid-cols-2 not-prose">
  <CardLink
    to="/agent-native/mcp-server"
    title="MCP Server"
    description="Connect AI agents and coding assistants over the Model Context Protocol — for trading or for documentation lookup."
    badge="MCP"
  >
    <IconTile label="MCP Server">
      <Plug className="h-5 w-5" aria-hidden />
    </IconTile>
  </CardLink>
  <CardLink
    to="/agent-native/llms-txt"
    title="llms.txt"
    description="A lightweight discovery protocol. AI tools fetch static files to understand what documentation is available and load full content."
    badge="Static files"
  >
    <IconTile label="llms.txt">
      <FileText className="h-5 w-5" aria-hidden />
    </IconTile>
  </CardLink>
</div>

---

## Quick Start

### Fetch documentation with llms.txt

```bash
# Summary — document titles, descriptions, and links
curl -s https://developers.binance.com/en/docs/llms.txt

# Full content — complete documentation in a single file
curl -s https://developers.binance.com/en/docs/llms-full.txt
```

---

## Who Is This For?

<div className="mt-1 text-sm text-muted-foreground">
  Whether you're building with AI IDEs or integrating documentation into agent
  pipelines, llms.txt fits a wide range of workflows.
</div>

<div className="mt-4 grid grid-cols-1 gap-4 sm:grid-cols-2 xl:grid-cols-3 not-prose">
  <ScenarioCard
    icon={Code2}
    title="Agent Framework Developers"
    description="Building with LangChain, CrewAI, or AutoGen? Feed llms.txt into your agent's context to ground responses in up-to-date Binance API documentation."
  />
  <ScenarioCard
    icon={Lightbulb}
    title="LLM Application Builders"
    description="Use llms.txt for context injection. Drop full documentation into any LLM-powered application without scraping or chunking pages yourself."
  />
  <ScenarioCard
    icon={Users}
    title="Prompt Engineers"
    description="Use llms.txt to feed complete Binance API documentation into any LLM. Perfect for building prompts with up-to-date API context."
  />
</div>

---

# Agent 原生

import { Link } from "zudoku/components";
import { Card, CardHeader, CardTitle, CardDescription } from "zudoku/ui/Card";
import {
  Bot,
  FileText,
  Plug,
  ChevronRight,
  Code2,
  Lightbulb,
  Users,
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

<div className="not-prose -mt-2 mb-8 rounded-2xl border bg-[radial-gradient(circle_at_top_right,rgba(240,185,11,0.08),transparent_50%)] p-6">
  <div className="flex items-center gap-3 mb-3">
    <div className="inline-flex h-12 w-12 items-center justify-center rounded-xl border bg-primary/10">
      <Bot className="h-6 w-6 text-primary" />
    </div>
    <div>
      <p className="text-xs font-semibold uppercase tracking-[0.16em] text-primary">
        Agent 原生
      </p>
    </div>
  </div>
  <p className="text-sm leading-6 text-muted-foreground">
    面向 AI 工具、编程助手和自主 Agent 的轻量级文档接入方式。让 AI
    系统能够以编程方式发现并加载 完整的 Binance API 文档。
  </p>
</div>

## 核心组件

<div className="mt-1 text-sm text-muted-foreground">
  选择适合您使用场景的集成方式。
</div>

<div className="mt-4 grid grid-cols-1 gap-4 sm:grid-cols-2 not-prose">
  <CardLink
    to="/agent-native/mcp-server"
    title="MCP Server"
    description="通过 Model Context Protocol 连接 AI agent 和编程助手——用于交易，或者用于文档查询。"
    badge="MCP"
  >
    <IconTile label="MCP Server">
      <Plug className="h-5 w-5" aria-hidden />
    </IconTile>
  </CardLink>
  <CardLink
    to="/agent-native/llms-txt"
    title="llms.txt"
    description="轻量级发现协议。AI 工具通过获取静态文件来了解可用文档并加载完整内容。"
    badge="静态文件"
  >
    <IconTile label="llms.txt">
      <FileText className="h-5 w-5" aria-hidden />
    </IconTile>
  </CardLink>
</div>

---

## 快速开始

### 通过 llms.txt 获取文档

```bash
# 摘要 — 文档标题、描述和链接
curl -s https://developers.binance.com/zh-CN/docs/llms.txt

# 完整内容 — 单个文件中的完整文档
curl -s https://developers.binance.com/zh-CN/docs/llms-full.txt
```

---

## 适用场景

<div className="mt-1 text-sm text-muted-foreground">
  无论您是使用 AI IDE 开发，还是将文档集成到 Agent 流水线中，llms.txt
  都能融入多种工作流。
</div>

<div className="mt-4 grid grid-cols-1 gap-4 sm:grid-cols-2 xl:grid-cols-3 not-prose">
  <ScenarioCard
    icon={Code2}
    title="Agent 框架开发者"
    description="使用 LangChain、CrewAI 或 AutoGen 构建？将 llms.txt 注入 Agent 上下文，让回答基于最新的 Binance API 文档。"
  />
  <ScenarioCard
    icon={Lightbulb}
    title="LLM 应用构建者"
    description="使用 llms.txt 进行上下文注入。无需自行抓取或切分页面即可将完整文档输入任何 LLM 驱动的应用。"
  />
  <ScenarioCard
    icon={Users}
    title="提示工程师"
    description="使用 llms.txt 将完整的 Binance API 文档输入任何 LLM。非常适合构建包含最新 API 上下文的提示词。"
  />
</div>