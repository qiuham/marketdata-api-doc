---
exchange: binance
source_url: https://developers.binance.com/en/docs/sdks-tools/overview
api_type: Guide
updated_at: 2026-11-28 18:26:43.608723
---

# SDKs & Tools

Build faster with official SDKs, tools, and reference implementations maintained by Binance.

import { Link, Typography, LanguageIcon } from "zudoku/components";
import {
  Card,
  CardHeader,
  CardTitle,
  CardDescription,
  CardFooter,
} from "zudoku/ui/Card";
import { ChevronRight, KeyRound, Terminal, Github, Bot } from "lucide-react";

export const OpenAILogo = ({ className }) => (
  <svg
    role="img"
    viewBox="0 0 24 24"
    fill="currentColor"
    aria-hidden
    className={className}
  >
    <path d="M22.2819 9.8211a5.9847 5.9847 0 0 0-.5157-4.9108 6.0462 6.0462 0 0 0-6.5098-2.9a6.0651 6.0651 0 0 0-10.0059 1.9958 5.9847 5.9847 0 0 0-3.9977 2.9 6.0462 6.0462 0 0 0 .7427 7.0966 5.98 5.98 0 0 0 .511 4.9107 6.051 6.051 0 0 0 6.5146 2.9001A5.9847 5.9847 0 0 0 13.2599 24a6.0557 6.0557 0 0 0 5.7718-4.2058 5.9894 5.9894 0 0 0 3.9977-2.9001 6.0557 6.0557 0 0 0-.7475-7.0729zm-9.022 12.6081a4.4755 4.4755 0 0 1-2.8764-1.0408l.1419-.0804 4.7783-2.7582a.7948.7948 0 0 0 .3927-.6813v-6.7369l2.02 1.1686a.071.071 0 0 1 .038.052v5.5826a4.504 4.504 0 0 1-4.4945 4.4944zm-9.6607-4.1254a4.4708 4.4708 0 0 1-.5346-3.0137l.1419.0852 4.783 2.7582a.7712.7712 0 0 0 .7806 0l5.8428-3.3685v2.3324a.0804.0804 0 0 1-.0332.0615L9.74 19.9502a4.4992 4.4992 0 0 1-6.1408-1.6464zM2.3408 7.8956a4.485 4.485 0 0 1 2.3655-1.9728V11.6a.7664.7664 0 0 0 .3879.6765l5.8144 3.3543-2.0201 1.1685a.0757.0757 0 0 1-.071 0l-4.8303-2.7865A4.504 4.504 0 0 1 2.3408 7.872zm16.5963 3.8558L13.1038 8.364 15.1192 7.2a.0757.0757 0 0 1 .071 0l4.8303 2.7913a4.4944 4.4944 0 0 1-.6765 8.1042v-5.6772a.79.79 0 0 0-.407-.667zm2.0107-3.0231l-.142-.0852-4.7735-2.7818a.7759.7759 0 0 0-.7854 0L9.409 9.2297V6.8974a.0662.0662 0 0 1 .0284-.0615l4.8303-2.7866a4.4992 4.4992 0 0 1 6.6802 4.66zM8.3065 12.863l-2.02-1.1638a.0804.0804 0 0 1-.038-.0567V6.0742a4.4992 4.4992 0 0 1 7.3757-3.4537l-.142.0805L8.704 5.459a.7948.7948 0 0 0-.3927.6813zm1.0976-2.3654l2.602-1.4998 2.6069 1.4998v2.9994l-2.5974 1.4997-2.6067-1.4997z" />
  </svg>
);

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

export const REGISTRY_ICONS = {
  npm: "https://cdn.simpleicons.org/npm",
  PyPI: "https://cdn.simpleicons.org/pypi",
  "crates.io": "https://cdn.simpleicons.org/rust",
  "pkg.go.dev": "https://cdn.simpleicons.org/go",
  NuGet: "https://cdn.simpleicons.org/nuget",
  Packagist: "https://cdn.simpleicons.org/packagist",
  RubyGems: "https://cdn.simpleicons.org/rubygems",
  Maven: "https://cdn.simpleicons.org/apachemaven",
};

export const CardLink = ({
  to,
  title,
  description,
  children,
  github,
  registry,
  external,
}) => (
  <div className="not-prose group relative rounded-xl">
    <Link
      to={to}
      className="absolute inset-0 z-0 rounded-xl focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 focus-visible:ring-offset-background"
      aria-label={title}
    />
    <Card className="pointer-events-none flex h-full flex-col transition-all group-hover:-translate-y-0.5 group-hover:shadow-md">
      <CardHeader className="flex-1 content-start pb-3">
        <div className="flex flex-wrap gap-2">{children}</div>
        <CardTitle className="mt-3 text-base">{title}</CardTitle>
        {description ? (
          <CardDescription className="mt-1">{description}</CardDescription>
        ) : null}
      </CardHeader>
      {(github || registry || external) && (
        <CardFooter className="pointer-events-auto flex items-center gap-3 overflow-hidden border-t px-4 py-3">
          {external && (
            <a
              href={external.href}
              target="_blank"
              rel="noopener noreferrer"
              title={external.label}
              className="flex min-w-0 items-center gap-1.5 text-xs text-muted-foreground transition-colors hover:text-foreground"
            >
              {external.icon}
              <span className="truncate">{external.label}</span>
            </a>
          )}
          {github && (
            <a
              href={github}
              target="_blank"
              rel="noopener noreferrer"
              title="View on GitHub"
              className="flex shrink-0 items-center gap-1.5 text-xs text-muted-foreground transition-colors hover:text-foreground"
            >
              <Github className="h-3.5 w-3.5" aria-hidden />
              Git
            </a>
          )}
          {registry && (
            <a
              href={registry.href}
              target="_blank"
              rel="noopener noreferrer"
              title={`View on ${registry.label}`}
              className="flex min-w-0 items-center gap-1.5 text-xs text-muted-foreground transition-colors hover:text-foreground"
            >
              <img
                src={REGISTRY_ICONS[registry.label]}
                alt=""
                aria-hidden="true"
                className="h-3.5 w-3.5 shrink-0"
                loading="lazy"
              />
              <span className="truncate">{registry.label}</span>
            </a>
          )}
        </CardFooter>
      )}
    </Card>
  </div>
);

---

## Official API Connectors

<div className="mt-1 text-sm text-muted-foreground">
  Production-ready client libraries maintained by Binance for popular languages.
  Each connector includes request signing helpers, typed models, and runnable
  examples.
</div>

### REST API, WebSocket API & WebSocket Streams

<div className="mt-1 text-sm text-muted-foreground">
  Full-featured connectors covering REST endpoints, WebSocket API requests, and
  real-time WebSocket data streams.
</div>

<div className="mt-4 grid grid-cols-1 gap-4 sm:grid-cols-2 xl:grid-cols-4 not-prose">
  <CardLink
    to="/sdks-tools/connectors/javascript"
    title="JavaScript"
    description="Official JavaScript connector with request signing, typed models, and examples."
    github="https://github.com/binance/binance-connector-js"
    registry={{ href: "https://www.npmjs.com/~binance-bot", label: "npm" }}
  >
    <IconTile label="JavaScript"><LanguageIcon language="javascript" /></IconTile>
    <IconTile label="TypeScript"><LanguageIcon language="typescript" /></IconTile>
  </CardLink>

<CardLink
  to="/sdks-tools/connectors/python"
  title="Python"
  description="Official Python connector with request signing, typed models, and examples."
  github="https://github.com/binance/binance-connector-python"
  registry={{ href: "https://pypi.org/user/binance", label: "PyPI" }}
>
  <IconTile label="Python">
    <LanguageIcon language="python" />
  </IconTile>
</CardLink>

<CardLink
  to="/sdks-tools/connectors/rust"
  title="Rust"
  description="Official Rust connector with request signing, typed models, and examples."
  github="https://github.com/binance/binance-connector-rust"
  registry={{
    href: "https://crates.io/crates/binance-sdk",
    label: "crates.io",
  }}
>
  <IconTile label="Rust">
    <LanguageIcon language="rust" />
  </IconTile>
</CardLink>

<CardLink
  to="/sdks-tools/connectors/cpp"
  title="C++"
  description="Official C++ connector with request signing, typed models, and examples."
  github="https://github.com/binance/binance-connector-cpp"
>
  <IconTile label="C++">
    <LanguageIcon language="cpp" />
  </IconTile>
</CardLink>

<CardLink
  to="/sdks-tools/connectors/go"
  title="Go"
  description="Official Go connector with request signing, typed models, and examples."
  github="https://github.com/binance/binance-connector-go"
  registry={{
    href: "https://pkg.go.dev/search?q=%2Fbinance%2Fbinance-connector-go%2Fclients",
    label: "pkg.go.dev",
  }}
>
  <IconTile label="Go">
    <LanguageIcon language="go" />
  </IconTile>
</CardLink>

<CardLink
  to="/sdks-tools/connectors/java"
  title="Java"
  description="Official Java connector with request signing, typed models, and examples."
  github="https://github.com/binance/binance-connector-java"
  registry={{
    href: "https://mvnrepository.com/artifact/io.github.binance",
    label: "Maven",
  }}
>
  <IconTile label="Java">
    <LanguageIcon language="java" />
  </IconTile>
</CardLink>

<CardLink
  to="/sdks-tools/connectors/dotnet"
  title=".NET"
  description="Official .NET connector with request signing, typed models, and examples."
  github="https://github.com/binance/binance-connector-dotnet"
  registry={{ href: "https://www.nuget.org/profiles/binance", label: "NuGet" }}
>
  <IconTile label=".NET">
    <LanguageIcon language="csharp" />
  </IconTile>
</CardLink>

<CardLink
  to="/sdks-tools/connectors/php"
  title="PHP"
  description="Official PHP connector with request signing, typed models, and examples (REST only)."
  github="https://github.com/binance/binance-connector-php"
  registry={{
    href: "https://packagist.org/packages/binance/binance-connector-php",
    label: "Packagist",
  }}
>
  <IconTile label="PHP">
    <LanguageIcon language="php" />
  </IconTile>
</CardLink>

  <CardLink
    to="/sdks-tools/connectors/ruby"
    title="Ruby"
    description="Official Ruby connector with request signing, typed models, and examples."
    github="https://github.com/binance/binance-connector-ruby"
    registry={{ href: "https://rubygems.org/gems/binance-connector-ruby", label: "RubyGems" }}
  >
    <IconTile label="Ruby"><LanguageIcon language="ruby" /></IconTile>
  </CardLink>
</div>

### FIX

<div className="mt-1 text-sm text-muted-foreground">
  Low-latency connectors for Binance's FIX API, designed for high-performance
  order entry and execution reporting.
</div>

<div className="mt-4 grid grid-cols-1 gap-4 sm:grid-cols-2 xl:grid-cols-4 not-prose">
  <CardLink
    to="/sdks-tools/connectors/fix-python"
    title="Python"
    description="Official Python FIX connector with request signing, typed models, and examples."
    github="https://github.com/binance/binance-fix-connector-python"
    registry={{
      href: "https://pypi.org/project/binance_fix_connector",
      label: "PyPI",
    }}
  >
    <IconTile label="Python">
      <LanguageIcon language="python" />
    </IconTile>
    <Badge>FIX</Badge>
  </CardLink>
</div>

---

## Developer Tools

<div className="mt-1 text-sm text-muted-foreground">
  Utilities that help you develop locally, validate signatures, and automate
  common workflows. Use these tools alongside the connectors to speed up testing
  and integration.
</div>

<div className="mt-4 grid grid-cols-1 gap-4 sm:grid-cols-2 xl:grid-cols-4 not-prose">
  <CardLink
    to="/sdks-tools/tools/binance-cli"
    title="Binance CLI"
    description="Run requests, inspect responses, and troubleshoot quickly from your terminal."
    github="https://github.com/binance/binance-cli"
  >
    <IconTile label="CLI">
      <Terminal className="h-5 w-5" aria-hidden />
    </IconTile>
  </CardLink>

<CardLink
  to="/sdks-tools/tools/asymmetric-key-generator"
  title="Key Generator"
  description="Generate and manage asymmetric keys used for request signing and authentication."
  github="https://github.com/binance/asymmetric-key-generator"
>
  <IconTile label="Key Generator">
    <KeyRound className="h-5 w-5" aria-hidden />
  </IconTile>
</CardLink>
</div>

---

## Integrations

<div className="mt-1 text-sm text-muted-foreground">
  Use Binance directly from AI agents and assistants. These integrations bring
  Binance capabilities into the tools and platforms you already work in.
</div>

<div className="mt-4 grid grid-cols-1 gap-4 sm:grid-cols-2 xl:grid-cols-4 not-prose">
  <CardLink
    to="/sdks-tools/integrations/skills-hub"
    title="Skills Hub"
    description="Open marketplace of AI agent skills for crypto trading, wallet tracking, and DeFi."
    github="https://github.com/binance/binance-skills-hub"
  >
    <IconTile label="Skills Hub">
      <Bot className="h-5 w-5" aria-hidden />
    </IconTile>
  </CardLink>

  <CardLink
    to="/sdks-tools/integrations/chatgpt"
    title="ChatGPT"
    description="Explore Binance public, read-only market data using natural language inside ChatGPT."
    external={{
      href: "https://chatgpt.com/plugins/plugin_asdk_app_6965faefe2b081919a998e14aa25f738?q=binance",
      label: "Open in ChatGPT",
      icon: <OpenAILogo className="h-3.5 w-3.5 shrink-0" />,
    }}
  >
    <IconTile label="ChatGPT">
      <OpenAILogo className="h-5 w-5" />
    </IconTile>
  </CardLink>
</div>

---

## Sample Applications

<div className="mt-1 text-sm text-muted-foreground">
  End-to-end reference implementations you can run, modify, and use as a
  starting point. Ideal for learning message formats and recommended flows.
</div>

<div className="mt-4 grid grid-cols-1 gap-4 sm:grid-cols-2 xl:grid-cols-4 not-prose">
  <CardLink
    to="/sdks-tools/sample-apps/sbe-cpp"
    title="SBE Sample App (C++)"
    description="Reference SBE integration showing encoding/decoding and message handling."
    github="https://github.com/binance/binance-sbe-cpp-sample-app"
  >
    <IconTile label="C++">
      <LanguageIcon language="cpp" />
    </IconTile>
    <Badge>SBE</Badge>
  </CardLink>

<CardLink
  to="/sdks-tools/sample-apps/sbe-rust"
  title="SBE Sample App (Rust)"
  description="Reference SBE integration demonstrating a modern async-friendly implementation."
  github="https://github.com/binance/binance-sbe-rust-sample-app"
>
  <IconTile label="Rust">
    <LanguageIcon language="rust" />
  </IconTile>
  <Badge>SBE</Badge>
</CardLink>

  <CardLink
    to="/sdks-tools/sample-apps/sbe-java"
    title="SBE Sample App (Java)"
    description="Reference SBE integration for JVM environments with practical examples."
    github="https://github.com/binance/binance-sbe-java-sample-app"
  >
    <IconTile label="Java">
      <LanguageIcon language="java" />
    </IconTile>
    <Badge>SBE</Badge>
  </CardLink>
</div>

---

## Postman Collections

<div className="mt-1 text-sm text-muted-foreground">
  Ready-made Postman collections to explore endpoints quickly and share
  reproducible requests. Great for debugging, onboarding, and testing against
  different environments.
</div>

<div className="mt-4 grid grid-cols-1 gap-4 sm:grid-cols-2 xl:grid-cols-4 not-prose">
  <CardLink
    to="/sdks-tools/postman/collections"
    title="Postman Collections"
    description="Import collections and start sending requests in minutes."
    github="https://github.com/binance/binance-api-postman"
  >
    <IconTile label="Postman">
      <img
        src="https://cdn.simpleicons.org/postman"
        alt="Postman"
        className="h-6 w-6"
        loading="lazy"
      />
    </IconTile>
  </CardLink>
</div>

---

# SDK 与工具

官方连接器、开发者工具和示例应用，帮助您高效集成 Binance
API。选择语言或工具开始使用，并按照各个包中的快速入门与示例进行集成。

import { Link, Typography, LanguageIcon } from "zudoku/components";
import {
  Card,
  CardHeader,
  CardTitle,
  CardDescription,
  CardFooter,
} from "zudoku/ui/Card";
import { ChevronRight, KeyRound, Terminal, Github, Bot } from "lucide-react";

export const OpenAILogo = ({ className }) => (
  <svg
    role="img"
    viewBox="0 0 24 24"
    fill="currentColor"
    aria-hidden
    className={className}
  >
    <path d="M22.2819 9.8211a5.9847 5.9847 0 0 0-.5157-4.9108 6.0462 6.0462 0 0 0-6.5098-2.9a6.0651 6.0651 0 0 0-10.0059 1.9958 5.9847 5.9847 0 0 0-3.9977 2.9 6.0462 6.0462 0 0 0 .7427 7.0966 5.98 5.98 0 0 0 .511 4.9107 6.051 6.051 0 0 0 6.5146 2.9001A5.9847 5.9847 0 0 0 13.2599 24a6.0557 6.0557 0 0 0 5.7718-4.2058 5.9894 5.9894 0 0 0 3.9977-2.9001 6.0557 6.0557 0 0 0-.7475-7.0729zm-9.022 12.6081a4.4755 4.4755 0 0 1-2.8764-1.0408l.1419-.0804 4.7783-2.7582a.7948.7948 0 0 0 .3927-.6813v-6.7369l2.02 1.1686a.071.071 0 0 1 .038.052v5.5826a4.504 4.504 0 0 1-4.4945 4.4944zm-9.6607-4.1254a4.4708 4.4708 0 0 1-.5346-3.0137l.1419.0852 4.783 2.7582a.7712.7712 0 0 0 .7806 0l5.8428-3.3685v2.3324a.0804.0804 0 0 1-.0332.0615L9.74 19.9502a4.4992 4.4992 0 0 1-6.1408-1.6464zM2.3408 7.8956a4.485 4.485 0 0 1 2.3655-1.9728V11.6a.7664.7664 0 0 0 .3879.6765l5.8144 3.3543-2.0201 1.1685a.0757.0757 0 0 1-.071 0l-4.8303-2.7865A4.504 4.504 0 0 1 2.3408 7.872zm16.5963 3.8558L13.1038 8.364 15.1192 7.2a.0757.0757 0 0 1 .071 0l4.8303 2.7913a4.4944 4.4944 0 0 1-.6765 8.1042v-5.6772a.79.79 0 0 0-.407-.667zm2.0107-3.0231l-.142-.0852-4.7735-2.7818a.7759.7759 0 0 0-.7854 0L9.409 9.2297V6.8974a.0662.0662 0 0 1 .0284-.0615l4.8303-2.7866a4.4992 4.4992 0 0 1 6.6802 4.66zM8.3065 12.863l-2.02-1.1638a.0804.0804 0 0 1-.038-.0567V6.0742a4.4992 4.4992 0 0 1 7.3757-3.4537l-.142.0805L8.704 5.459a.7948.7948 0 0 0-.3927.6813zm1.0976-2.3654l2.602-1.4998 2.6069 1.4998v2.9994l-2.5974 1.4997-2.6067-1.4997z" />
  </svg>
);

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

export const REGISTRY_ICONS = {
  npm: "https://cdn.simpleicons.org/npm",
  PyPI: "https://cdn.simpleicons.org/pypi",
  "crates.io": "https://cdn.simpleicons.org/rust",
  "pkg.go.dev": "https://cdn.simpleicons.org/go",
  NuGet: "https://cdn.simpleicons.org/nuget",
  Packagist: "https://cdn.simpleicons.org/packagist",
  RubyGems: "https://cdn.simpleicons.org/rubygems",
  Maven: "https://cdn.simpleicons.org/apachemaven",
};

export const CardLink = ({
  to,
  title,
  description,
  children,
  github,
  registry,
  external,
}) => (
  <div className="not-prose group relative rounded-xl">
    <Link
      to={to}
      className="absolute inset-0 z-0 rounded-xl focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 focus-visible:ring-offset-background"
      aria-label={title}
    />
    <Card className="pointer-events-none flex h-full flex-col transition-all group-hover:-translate-y-0.5 group-hover:shadow-md">
      <CardHeader className="flex-1 content-start pb-3">
        <div className="flex flex-wrap gap-2">{children}</div>
        <CardTitle className="mt-3 text-base">{title}</CardTitle>
        {description ? (
          <CardDescription className="mt-1">{description}</CardDescription>
        ) : null}
      </CardHeader>
      {(github || registry || external) && (
        <CardFooter className="pointer-events-auto flex items-center gap-3 overflow-hidden border-t px-4 py-3">
          {external && (
            <a
              href={external.href}
              target="_blank"
              rel="noopener noreferrer"
              title={external.label}
              className="flex min-w-0 items-center gap-1.5 text-xs text-muted-foreground transition-colors hover:text-foreground"
            >
              {external.icon}
              <span className="truncate">{external.label}</span>
            </a>
          )}
          {github && (
            <a
              href={github}
              target="_blank"
              rel="noopener noreferrer"
              title="View on GitHub"
              className="flex shrink-0 items-center gap-1.5 text-xs text-muted-foreground transition-colors hover:text-foreground"
            >
              <Github className="h-3.5 w-3.5" aria-hidden />
              Git
            </a>
          )}
          {registry && (
            <a
              href={registry.href}
              target="_blank"
              rel="noopener noreferrer"
              title={`View on ${registry.label}`}
              className="flex min-w-0 items-center gap-1.5 text-xs text-muted-foreground transition-colors hover:text-foreground"
            >
              <img
                src={REGISTRY_ICONS[registry.label]}
                alt=""
                aria-hidden="true"
                className="h-3.5 w-3.5 shrink-0"
                loading="lazy"
              />
              <span className="truncate">{registry.label}</span>
            </a>
          )}
        </CardFooter>
      )}
    </Card>
  </div>
);

---

## 官方 API 连接器

<div className="mt-1 text-sm text-muted-foreground">
  由 Binance 官方维护的生产级客户端库，覆盖主流编程语言。
  每个连接器均包含请求签名工具、类型化模型以及可运行示例。
</div>

### REST API、WebSocket API 与 WebSocket Streams

<div className="mt-1 text-sm text-muted-foreground">
  全功能连接器，涵盖 REST 接口、WebSocket API 请求以及实时 WebSocket 数据流。
</div>

<div className="mt-4 grid grid-cols-1 gap-4 sm:grid-cols-2 xl:grid-cols-4 not-prose">
  <CardLink
    to="/sdks-tools/connectors/javascript"
    title="JavaScript"
    description="官方 JavaScript 连接器，包含请求签名、类型模型与示例代码。"
    github="https://github.com/binance/binance-connector-js"
    registry={{ href: "https://www.npmjs.com/~binance-bot", label: "npm" }}
  >
    <IconTile label="JavaScript"><LanguageIcon language="javascript" /></IconTile>
    <IconTile label="TypeScript"><LanguageIcon language="typescript" /></IconTile>
  </CardLink>

<CardLink
  to="/sdks-tools/connectors/python"
  title="Python"
  description="官方 Python 连接器，包含请求签名、类型模型与示例代码。"
  github="https://github.com/binance/binance-connector-python"
  registry={{ href: "https://pypi.org/user/binance", label: "PyPI" }}
>
  <IconTile label="Python">
    <LanguageIcon language="python" />
  </IconTile>
</CardLink>

<CardLink
  to="/sdks-tools/connectors/rust"
  title="Rust"
  description="官方 Rust 连接器，包含请求签名、类型模型与示例代码。"
  github="https://github.com/binance/binance-connector-rust"
  registry={{
    href: "https://crates.io/crates/binance-sdk",
    label: "crates.io",
  }}
>
  <IconTile label="Rust">
    <LanguageIcon language="rust" />
  </IconTile>
</CardLink>

<CardLink
  to="/sdks-tools/connectors/cpp"
  title="C++"
  description="官方 C++ 连接器，包含请求签名、类型模型与示例代码。"
  github="https://github.com/binance/binance-connector-cpp"
>
  <IconTile label="C++">
    <LanguageIcon language="cpp" />
  </IconTile>
</CardLink>

<CardLink
  to="/sdks-tools/connectors/go"
  title="Go"
  description="官方 Go 连接器，包含请求签名、类型模型与示例代码。"
  github="https://github.com/binance/binance-connector-go"
  registry={{
    href: "https://pkg.go.dev/search?q=%2Fbinance%2Fbinance-connector-go%2Fclients",
    label: "pkg.go.dev",
  }}
>
  <IconTile label="Go">
    <LanguageIcon language="go" />
  </IconTile>
</CardLink>

<CardLink
  to="/sdks-tools/connectors/java"
  title="Java"
  description="官方 Java 连接器，包含请求签名、类型模型与示例代码。"
  github="https://github.com/binance/binance-connector-java"
  registry={{
    href: "https://mvnrepository.com/artifact/io.github.binance",
    label: "Maven",
  }}
>
  <IconTile label="Java">
    <LanguageIcon language="java" />
  </IconTile>
</CardLink>

<CardLink
  to="/sdks-tools/connectors/dotnet"
  title=".NET"
  description="官方 .NET 连接器，包含请求签名、类型模型与示例代码。"
  github="https://github.com/binance/binance-connector-dotnet"
  registry={{ href: "https://www.nuget.org/profiles/binance", label: "NuGet" }}
>
  <IconTile label=".NET">
    <LanguageIcon language="csharp" />
  </IconTile>
</CardLink>

<CardLink
  to="/sdks-tools/connectors/php"
  title="PHP"
  description="官方 PHP 连接器，包含请求签名、类型模型与示例代码（仅支持 REST）。"
  github="https://github.com/binance/binance-connector-php"
  registry={{
    href: "https://packagist.org/packages/binance/binance-connector-php",
    label: "Packagist",
  }}
>
  <IconTile label="PHP">
    <LanguageIcon language="php" />
  </IconTile>
</CardLink>

  <CardLink
    to="/sdks-tools/connectors/ruby"
    title="Ruby"
    description="官方 Ruby 连接器，包含请求签名、类型模型与示例代码。"
    github="https://github.com/binance/binance-connector-ruby"
    registry={{ href: "https://rubygems.org/gems/binance-connector-ruby", label: "RubyGems" }}
  >
    <IconTile label="Ruby"><LanguageIcon language="ruby" /></IconTile>
  </CardLink>
</div>

### FIX

<div className="mt-1 text-sm text-muted-foreground">
  适用于 Binance FIX API 的低延迟连接器，专为高性能报单与成交回报场景设计。
</div>

<div className="mt-4 grid grid-cols-1 gap-4 sm:grid-cols-2 xl:grid-cols-4 not-prose">
  <CardLink
    to="/sdks-tools/connectors/fix-python"
    title="Python"
    description="官方 Python FIX 连接器，支持 FIX 协议，包含请求签名、类型模型与示例代码。"
    github="https://github.com/binance/binance-fix-connector-python"
    registry={{
      href: "https://pypi.org/project/binance_fix_connector",
      label: "PyPI",
    }}
  >
    <IconTile label="Python">
      <LanguageIcon language="python" />
    </IconTile>
    <Badge>FIX</Badge>
  </CardLink>
</div>

---

## 开发者工具

<div className="mt-1 text-sm text-muted-foreground">
  帮助您进行本地开发、签名验证以及自动化常见工作流程的实用工具。
  建议结合官方连接器一起使用，以加快测试与集成效率。
</div>

<div className="mt-4 grid grid-cols-1 gap-4 sm:grid-cols-2 xl:grid-cols-4 not-prose">
  <CardLink
    to="/sdks-tools/tools/binance-cli"
    title="Binance CLI"
    description="通过命令行发送请求、查看响应并快速排查问题。"
    github="https://github.com/binance/binance-cli"
  >
    <IconTile label="CLI">
      <Terminal className="h-5 w-5" aria-hidden />
    </IconTile>
  </CardLink>

<CardLink
  to="/sdks-tools/tools/asymmetric-key-generator"
  title="密钥生成器"
  description="生成并管理用于请求签名与身份认证的非对称密钥。"
  github="https://github.com/binance/asymmetric-key-generator"
>
  <IconTile label="Key Generator">
    <KeyRound className="h-5 w-5" aria-hidden />
  </IconTile>
</CardLink>
</div>

---

## 集成

<div className="mt-1 text-sm text-muted-foreground">
  直接在 AI Agent 与助手中使用 Binance。这些集成将 Binance
  能力带入您已在使用的工具与平台。
</div>

<div className="mt-4 grid grid-cols-1 gap-4 sm:grid-cols-2 xl:grid-cols-4 not-prose">
  <CardLink
    to="/sdks-tools/integrations/skills-hub"
    title="Skills Hub"
    description="开放式 AI Agent 技能市场，涵盖加密交易、钱包追踪与 DeFi 能力。"
    github="https://github.com/binance/binance-skills-hub"
  >
    <IconTile label="Skills Hub">
      <Bot className="h-5 w-5" aria-hidden />
    </IconTile>
  </CardLink>

  <CardLink
    to="/sdks-tools/integrations/chatgpt"
    title="ChatGPT"
    description="在 ChatGPT 中使用自然语言探索币安公开的只读行情数据。"
    external={{
      href: "https://chatgpt.com/plugins/plugin_asdk_app_6965faefe2b081919a998e14aa25f738?q=binance",
      label: "在 ChatGPT 中打开",
      icon: <OpenAILogo className="h-3.5 w-3.5 shrink-0" />,
    }}
  >
    <IconTile label="ChatGPT">
      <OpenAILogo className="h-5 w-5" />
    </IconTile>
  </CardLink>
</div>

---

## 示例应用

<div className="mt-1 text-sm text-muted-foreground">
  可运行的端到端参考实现，您可以直接运行、修改，并作为项目起点。
  适用于学习消息格式与推荐的交互流程。
</div>

<div className="mt-4 grid grid-cols-1 gap-4 sm:grid-cols-2 xl:grid-cols-4 not-prose">
  <CardLink
    to="/sdks-tools/sample-apps/sbe-cpp"
    title="SBE 示例应用（C++）"
    description="展示 SBE 编码/解码及消息处理流程的参考实现。"
    github="https://github.com/binance/binance-sbe-cpp-sample-app"
  >
    <IconTile label="C++">
      <LanguageIcon language="cpp" />
    </IconTile>
    <Badge>SBE</Badge>
  </CardLink>

<CardLink
  to="/sdks-tools/sample-apps/sbe-rust"
  title="SBE 示例应用（Rust）"
  description="现代异步友好型 SBE 集成示例。"
  github="https://github.com/binance/binance-sbe-rust-sample-app"
>
  <IconTile label="Rust">
    <LanguageIcon language="rust" />
  </IconTile>
  <Badge>SBE</Badge>
</CardLink>

  <CardLink
    to="/sdks-tools/sample-apps/sbe-java"
    title="SBE 示例应用（Java）"
    description="适用于 JVM 环境的 SBE 集成示例与实践。"
    github="https://github.com/binance/binance-sbe-java-sample-app"
  >
    <IconTile label="Java">
      <LanguageIcon language="java" />
    </IconTile>
    <Badge>SBE</Badge>
  </CardLink>
</div>

---

## Postman 集合

<div className="mt-1 text-sm text-muted-foreground">
  预构建的 Postman 集合，可快速探索接口并共享可复现请求。
  适用于调试、快速上手以及不同环境测试。
</div>

<div className="mt-4 grid grid-cols-1 gap-4 sm:grid-cols-2 xl:grid-cols-4 not-prose">
  <CardLink
    to="/sdks-tools/postman/collections"
    title="Postman 集合"
    description="导入集合，几分钟内即可开始发送请求。"
    github="https://github.com/binance/binance-api-postman"
  >
    <IconTile label="Postman">
      <img
        src="/postman-icon.svg"
        alt="Postman"
        className="h-6 w-6"
        loading="lazy"
      />
    </IconTile>
  </CardLink>
</div>