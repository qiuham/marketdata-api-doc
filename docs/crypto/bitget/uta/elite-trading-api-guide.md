---
exchange: bitget
source_url: https://www.bitget.com/docs/uta/elite-trading-api-guide
api_type: Guide
updated_at: 2026-11-24 19:01:09.404700
---

# Elite Trading API Guide

This article explains how to create and use an Elite Trading API for Elite Trading Portfolio on Bitget. It also covers where to find the feature, what the API supports, and the current permission and usage limits.

---

## Overview

Elite Trading Portfolio now supports copy trading through API. You can create a dedicated Elite Trading API from the Bitget app or website and use it to manage futures copy trading more efficiently. This feature is designed for users who already have an Elite Trading Portfolio.

---

## Before you start

Make sure you have already completed the following:
- Created an Elite Trading Portfolio
- Logged in to the correct main account or sub-account
- Completed the required security verification setup

---

## Where to access Futures API Elite trading?

You can create and manage your Elite Trading API from both the app and web.

### On the Bitget app
Go to **Elite Trader Center → Elite Trading Portfolio → API Settings**  
Open the shortcut panel to find **API Settings**.

**Requirement:** You must already have an Elite Trading Portfolio.

### On the Bitget website
Go to **Personal Center → API Keys → Elite Trading API Key**

**Requirement:** You must already have an Elite Trading Portfolio and select the correct main account or sub-account.

---

## How to create an Elite Trading API?

You can create a Elite Trading API in three steps.

### Step 1: Open the Elite Trading API Management page
1. From the app or website, go to Elite Trading API Management.
2. Click **Create Elite Trading API** to start.

### Step 2: Complete security verification
1. Enter your passcode and complete the required security verification.
2. After verification is successful:
3. The system automatically generates an API Key
4. A default API name is assigned, such as Elite Trading 01

### Step 3: View and save your API credentials
1. After the API is created successfully, the page displays:
   - API Key
   - HMAC Key (Secret Key)
2. Store these credentials securely after creation.

---

## API limits and important rules

Please review the current scope before integration.

### API key limit per portfolio
Each Elite Trading Portfolio can create up to two API Keys.

### Supported features
The Elite Trading API currently supports:
- Placing orders for elite trading futures pairs
- Canceling orders
- Amending orders
- Querying elite trading positions
- Querying active orders
- Querying position history
- Querying order history
- Accessing Unified Account trading APIs, the same as the standard API

### Not supported
The Elite Trading API does not currently support:
- Spot trading
- Futures trading for non-elite-trading pairs
- Isolated margin mode
- One-way position mode
- Account mode switching

---

## API permissions

By default, a newly created Elite Trading API includes these permissions:
- Elite trading position read/write — View and modify elite trading positions
- Elite trading order read/write — Place, cancel, and amend orders
- Unified account trading read/write — Access standard trading APIs

You can also switch the API permission mode to **Read Only**.

---

## Important notes before deleting a Elite Trading API

You can remove an API key at any time. Please note the effects below.

### Delete a single API
When you delete one API key:
- That API key becomes invalid immediately
- It can no longer be used for any request

### Close the Elite Trading Portfolio
When you close the Elite Trading Portfolio:
- All API keys under that portfolio are deleted automatically

---

## Technical integration reference

The trading APIs used for Elite Trading Portfolio are the same as the Unified Account Trade APIs. This means you can directly integrate using the existing Unified Account trading interfaces for actions such as:
- Placing orders
- Modifying take-profit and stop-loss settings
- Canceling orders
- Querying order history

No separate trading API framework is required for this feature. For detailed endpoint-level development guidance, refer to the official API documentation.

---

## Tips for secure API usage

To protect your account and trading activity, we recommend that you:
- Store your API Key and Secret Key in a secure environment
- Limit access to trusted systems only
- Use Read Only mode when trading access is not required
- Delete unused API keys promptly
- Review portfolio-level API usage regularly

---

## FAQs

1. Who can create an Elite Trading API?  
   Only users who have already created an Elite Trading Portfolio can create an Elite Trading API.

2. Can I create an Elite Trading API on both the app and website?  
   Yes. You can create and manage your Elite Trading API from both the Bitget app and website.

3. How many API keys can I create for one Elite Trading Portfolio?  
   Each Elite Trading Portfolio can create up to two API Keys.

4. Does the Elite Trading API support spot trading?  
   No. The Elite Trading API currently does not support spot trading.

5. What happens if I close my Elite Trading Portfolio?  
   If you close the Elite Trading Portfolio, all API keys under that portfolio are deleted automatically.

---

# 带单 API 交易指南

本文介绍了如何在 Bitget 上为**带单项目**创建和使用**带单 API**，包括功能入口、支持的操作范围，以及当前的权限设置与使用限制。

## 概览

带单项目现已支持通过 API 进行跟单交易。您可以在 Bitget App 或网页端创建专属的**带单 API**，更高效地管理合约跟单交易。  
本功能适用于已创建**带单项目**的用户。

## 开始之前

请确认您已完成以下准备工作：

- 已创建**带单项目**
- 已登录正确的主账户或子账户
- 已完成必要的安全验证设置

## 如何访问带单 API？

您可以在 App 端和网页端创建及管理**带单交易 API**。

### Bitget App 端

前往：**带单中心** → **带单项目** → **API 设置**  
也可打开快捷面板，找到 **API 设置**。

**要求**: 您必须已创建带单项目。

### Bitget 网页端

前往：**用户中心** → **API 密钥** → **带单 API 密钥**

**要求**: 您必须已创建带单项目，并选择正确的主账户或子账户。

## 如何创建带单交易 API？

创建带单 API 共分三步。

### 第一步：进入带单 API 管理页面

1. 在 App 端或网页端，进入**带单 API**管理页面。
2. 点击**创建带单 API**开始操作。

### 第二步：完成安全验证

1. 请输入密码并完成所需的安全验证。
2. 验证成功后：
3. 系统会自动生成**API 密钥**
   - 系统自动分配默认 API 名称，例如：**带单交易01**

### 第三步：查看并保存 API 凭证

1. API 创建成功后，页面将显示：
   - **API 密钥**
   - **HMAC 密钥（私钥）**
2. 请在创建后妥善保管上述凭证。

## API 限制与重要规则

请在集成前仔细了解当前范围。

### 每个带单项目的 API 密钥数量上限

每个**带单项目**最多可创建**2 个 API 密钥**。

### 支持的功能

带单 API 目前支持以下操作：

- 为合约带单交易币对下单
- 撤销订单
- 修改订单
- 查询带单交易持仓
- 查询当前委托订单
- 查询历史持仓
- 查询订单历史记录
- 访问**统一账户**交易 API，与标准 API 相同

### 不支持的功能

带单 API 目前不支持以下操作：

- 现货交易
- 非带单币对的合约交易
- 逐仓保证金模式
- 单向持仓模式
- 账户模式切换

## API 权限

新创建的带单 API 默认包含以下权限：

- **带单交易持仓读写** — 查看和修改带单交易持仓
- **带单交易订单读写** — 下单、撤单和修改订单
- **UTA 交易读写** — 访问标准交易 API

您也可以将 API 权限模式切换为**只读**。

## 删除带单 API 前的注意事项

您可以随时删除 API 密钥，请注意以下影响。

### 删除单个 API

删除某个 API 密钥后：

- 该 API 密钥立即失效
- 无法再用于任何请求

### 关闭带单项目

关闭**带单项目**后：

- 该项目下的所有 API 密钥都将自动删除

## 技术集成参考

**带单项目**使用的交易 API 与 **UTA 交易 API** 相同。  
这意味着您可以直接使用现有的 UTA 交易接口进行集成，支持的操作包括：

- 下单
- 修改止盈止损设置
- 撤销订单
- 查询订单历史记录

本功能无需单独搭建交易 API 框架。  
如需详细的接口级开发指引，请参阅官方 **API 文档**。

## API 安全使用建议

为保护您的账户和交易安全，建议您：

- 将 **API 密钥**和**私钥**存储在安全的环境中
- 仅限受信任的系统访问
- 在不需要交易权限时，使用**只读**模式
- 及时删除不再使用的 API 密钥
- 定期审查项目层级的 API 使用情况

## 常见问题

### 1. 谁可以创建带单 API？

仅已创建带单项目的用户可以创建带单 API。

### 2. 可以在 App 端和网页端同时创建带单 API 吗？

可以。您可以在 Bitget App 端和网页端创建及管理带单 API。

### 3. 每个带单项目可以创建多少个 API 密钥？

每个带单项目最多可创建 2 个 API 密钥。

### 4. 带单 API 支持现货交易吗？

不支持。带单 API 目前不支持现货交易。

### 5. 如果我关闭带单项目会发生什么？

关闭带单项目后，该项目下的所有 API 密钥将被自动删除。