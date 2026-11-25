---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/agentic-wallet/quickstart/install-agentic-wallet
api_type: Guide
updated_at: 2026-11-25 18:42:11.141719
---

# Install Agentic Wallet

Two steps to start operating on-chain through natural language with your AI Agent.

---

## Prerequisites

**Node.js 18+** — required by the Skills installer.

**Binance Account & MPC Wallet**

1. You need a Binance account to get started
2. After signing in to Binance, create an MPC Wallet in the Binance App — this is required before
   you can create an Agentic Wallet

---

## Step 1: Install Skills

```bash
npx skills add binance/binance-skills-hub/skills/binance-web3/binance-agentic-wallet
```

> If the `baw` CLI is not installed, Skills will detect this and install it automatically on first
> use.

---

## Step 2: Sign In

Once installed, say this to your AI Agent:

> "Sign in to Binance Agentic Wallet"

The Agent will return a signin link. If you click this link on mobile, you will be directly
redirected to the Binance App. If you open it on the web, you will need to scan the QR code in the
page using the Binance App and confirm the signin in the App.

If this is your first time signing in, the Binance App will walk you through the Agentic Wallet
creation process. Once complete, you'll land on the Agentic Wallet management page.

To sign out, tell your AI:

> "Sign out"

---

## Security Recommendations

Security rules can only be configured in the Binance App — the AI can read them but cannot modify
them. For first-time setup, we recommend:

- Set a small daily limit (e.g., $50) to start
- Restrict tradable tokens to the Limited scope
- Set high-risk transaction handling to "Require App confirmation"

To modify: **Binance App → Agentic Wallet management page → Settings icon (top right)**

---

## Next Steps

→ [Use Cases Overview](../use-cases/overview.md)

---

# 安装 Agentic Wallet

完成以下两步即可通过 AI 自然语言驱动链上操作。

---

## 前置条件

**Node.js 18+**：Skills 安装程序需要 Node.js 18 或以上版本。

**Binance 账号 & MPC Wallet**

1. 您需要首先拥有一个币安账号
2. 注册登录好币安账号后，您需要先创建一个 App 端 MPC Wallet，从而拥有创建 Agentic Wallet 的权限

---

## 第一步：安装 Skills

```bash
npx skills add binance/binance-skills-hub/skills/binance-web3/binance-agentic-wallet
```

> 如果你尚未安装 `baw` CLI，Skills 会在第一次使用时自动完成安装。

---

## 第二步：登录

安装完成后，在 AI Agent 中直接说：

> "登录 Binance Agentic Wallet"

Agent 会返回一个登录链接。如果您在移动端点击该链接，将直接跳转至 Binance
App；如果您在网页端打开，则需要使用 Binance App 扫描二维码，并在 App 内确认登录。

如果这是您第一次登录，我们会在 Binance App 中为您走完整个标准创建流程，创建完成后，您会进入 Agentic
Wallet 管理页。

如需登出，直接告诉 AI：

> "退出登录"

---

## 安全设置建议

安全规则仅在 Binance App 中配置，AI 只能读取，无法修改。建议初次使用时：

- 每日限额设置为较小金额（如 $50）
- 可交易代币限定为有限代币范围
- 异常交易处理设为"需 App 二次确认"

如需修改：**Binance App → Agentic Wallet 管理页 → 右上角设置图标**

---

## 下一步

→ [使用场景概览](../use-cases/overview.md)