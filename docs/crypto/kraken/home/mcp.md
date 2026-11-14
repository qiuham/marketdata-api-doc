---
api_type: reference
source_type: llms_txt
version: ''
scope: crypto
asset_class: digital_asset
domain: exchanges
provider: kraken
provider_name: Kraken
product: api
product_id: kraken
source_url: 'https://docs.kraken.com/home/mcp'
updated_at: 2026-11-13
---

# MCP server

> Give AI agents Kraken CLI commands as tools through the kraken-mcp Model Context Protocol server

kraken-cli ships a [Model Context Protocol](https://modelcontextprotocol.io) server, `kraken-mcp`, over stdio. It serves 152 of the CLI's commands as MCP tools that any MCP-compatible AI agent can call — Claude, Cursor, GitHub Copilot, Windsurf, and others.

Streams (WebSocket feeds, recording, replay, session start), interactive commands, and the local credential commands `auth switch` and `auth reset` stay CLI-only. A tool call is one request and one response; a stream never returns. Run streams with the CLI, for example `kraken record`, and read the results back with tools such as `kraken_tape_list` and `kraken_explain_pnl`, or `kraken_session_show` with the `workspace` service.

`kraken-mcp` comes with the CLI install. [Install the CLI](https://docs.kraken.com/home/cli.md) first.

## Quickstart

```bash theme={null}
kraken-mcp -s market,paper,feedback
```

This starts the server with market data, paper trading, and the feedback tool, which uploads the text you give it to Kraken. No credentials are required, and no tool can trade live or move funds.

## Client setup

> [tab] Claude Code
>
> Install the plugin, which adds the MCP server and the CLI's agent skills:
>
> ```text theme={null}
> /plugin marketplace add krakenfx/kraken-cli
> /plugin install kraken-cli@kraken
> ```
>
> Or register only the MCP server for your user:
>
> ```bash theme={null}
> claude mcp add --scope user kraken -- kraken-mcp -s market,paper,feedback
> ```
>
> The plugin asks for no API key. To add live trading, use `-s market,paper,trade` with a least-privilege API key (see [Authentication](#authentication)).
>
> Verify it is registered:
>
> ```bash theme={null}
> claude mcp list
> ```
>
> If it shows "Failed to connect", Claude Code cannot find `kraken-mcp` on its PATH. Quit Claude Code and start it again from a new terminal window, or register the full path, which works before `kraken-mcp` is on your PATH:
>
> ```bash theme={null}
> claude mcp add --scope user kraken -- "$HOME/.cargo/bin/kraken-mcp" -s market,paper,feedback
> ```
>
> If you set `CARGO_HOME`, use `$CARGO_HOME/bin/kraken-mcp` instead.

> [tab] Claude Desktop
>
> Edit `~/Library/Application Support/Claude/claude_desktop_config.json`:
>
> ```json theme={null}
> {
>   "mcpServers": {
>     "kraken": {
>       "command": "kraken-mcp",
>       "args": ["-s", "market,paper,feedback"]
>     }
>   }
> }
> ```
>
> Restart Claude Desktop to pick up the change.

> [tab] Cursor
>
> Create or edit `~/.cursor/mcp.json` (global) or `.cursor/mcp.json` in your project:
>
> ```json theme={null}
> {
>   "mcpServers": {
>     "kraken": {
>       "command": "kraken-mcp",
>       "args": ["-s", "market,paper,feedback"]
>     }
>   }
> }
> ```
>
> Reload the Cursor window after saving.

> [tab] VS Code (Copilot)
>
> Create or edit `.vscode/mcp.json` in your workspace:
>
> ```json theme={null}
> {
>   "servers": {
>     "kraken": {
>       "type": "stdio",
>       "command": "kraken-mcp",
>       "args": ["-s", "market,paper,feedback"]
>     }
>   }
> }
> ```

> [tab] Windsurf
>
> Edit `~/.codeium/windsurf/mcp_config.json`:
>
> ```json theme={null}
> {
>   "mcpServers": {
>     "kraken": {
>       "command": "kraken-mcp",
>       "args": ["-s", "market,paper,feedback"]
>     }
>   }
> }
> ```
>
> Restart Windsurf to apply.

Other MCP clients take the same command and arguments: `kraken-mcp -s market,paper,feedback`. Gemini CLI users can install the extension instead: `gemini extensions install https://github.com/krakenfx/kraken-cli`.

If a client reports "Failed to connect" or cannot start the server, set `command` to the full path that `command -v kraken-mcp` prints. Desktop apps often do not see the PATH your terminal uses.

## Services

Pass `-s <services>` to control which command groups are exposed. Multiple services are comma-separated.

| Service | Tools | Auth | Risk level | What it exposes |
| :- | :-: | :- | :- | :- |
| `market` | 11 | No | None | Ticker, orderbook, trades, OHLC, spreads, asset info, tape library |
| `account` | 18 | Yes | Read-only, except `export-retrieve` and `export-delete` (dangerous) | Balances, orders, trade history, ledgers, positions, exports |
| `paper` | 17 | No | Simulation; `reset` is dangerous | Spot paper trading with live prices, P\&L explanation, research lab |
| `workspace` | 20 | No | `reset` and `promote` are dangerous; live workspaces reach the real account | Paper and live workspaces, sessions, recipes, reports, extensions |
| `futures-paper` | 17 | No | None (simulation) | Futures paper trading |
| `feedback` | 1 | No | Uploads text to Kraken | Product feedback upload to Kraken |
| `trade` | 9 | Yes | Dangerous | Place, amend, and cancel live Spot orders |
| `futures` | 39 | Mixed | Dangerous | Futures market data and order entry |
| `earn` | 6 | Yes | Dangerous | Staking allocations and deallocations |
| `funding` | 10 | Yes | Dangerous | Deposits, withdrawals, and transfers |
| `subaccount` | 2 | Yes | Dangerous | Subaccount creation and transfers |
| `auth` | 2 | Mixed | Read-only | Credential status and validation |
| `all` | 152 | Mixed | Mixed | All of the above |

**Default** (no `-s` flag): `market`, `account`, `paper`, `workspace`, `feedback`.

### Dangerous tools

Tools marked dangerous (order placement, withdrawals, transfers, workspace promotion) need your approval for every call. The server asks you through MCP elicitation and runs the call only if you approve. A client that cannot show an elicitation gets no prompt from the server: the call runs when the model sets `acknowledged: true` in its arguments, so on such a client rely on the client's own tool-approval prompt. Start the server with `--allow-dangerous` to turn the gate off.

```bash theme={null}
# Ask for approval on every dangerous call
kraken-mcp -s all

# Turn the approval gate off (use in trusted, controlled environments only)
kraken-mcp -s all --allow-dangerous
```

## Authentication

Set credentials as environment variables in the client's MCP configuration, or in the shell that starts the server:

```bash theme={null}
export KRAKEN_API_KEY="your-key"
export KRAKEN_API_SECRET="your-secret"
kraken-mcp -s market,account,trade
```

Or store a key once in a terminal, with `kraken auth login` (browser sign-in, a restricted key with no withdrawal rights) or `kraken setup` (a key you created). The server reads the same active stored key as the CLI. `kraken-mcp` takes no `--api-key` or `--api-secret` flags.

## What agents can do

With `market`, `paper`, and `feedback`, an agent can:

* Query live prices, orderbooks, and recent trades for any pair
* Place and cancel paper trades against live prices
* List recorded tapes and explain a stopped session's P\&L

With `account`, it can read balances and open orders. With `trade` added, it can place, amend, and cancel live orders. With `funding`, it can initiate withdrawals. Scope services to the minimum your workflow requires.

## Safety notes

* The MCP server runs locally over stdio and is not exposed as a network service
* Use minimum-permission API keys scoped to what the agent actually needs
* The default service set places no live orders and moves no funds; its few dangerous tools (workspace promotion and reset, paper reset, export retrieval and deletion) still need approval, and so does creating a live workspace
* Treat agent sessions with live trading scope the same as a logged-in user session
* Set position size limits and pair allowlists at the API key level on Kraken's settings page

## Agent resources

The CLI ships supplementary resources for agent integration:

| Resource | Purpose |
| :- | :- |
| [AGENTS.md](https://github.com/krakenfx/kraken-cli/blob/main/AGENTS.md) | Full integration guide with patterns and constraints |
| [CONTEXT.md](https://github.com/krakenfx/kraken-cli/blob/main/CONTEXT.md) | Runtime context injected at session start |
| [agents/tool-catalog.json](https://github.com/krakenfx/kraken-cli/blob/main/agents/tool-catalog.json) | All 188 commands with parameter schemas; the `reach` field marks the 152 MCP tools |
| [agents/error-catalog.json](https://github.com/krakenfx/kraken-cli/blob/main/agents/error-catalog.json) | 10 error categories with retry guidance |
| [skills/](https://github.com/krakenfx/kraken-cli/tree/main/skills) | 59 pre-built workflow packages for common trading tasks |
| [CLAUDE.md](https://github.com/krakenfx/kraken-cli/blob/main/CLAUDE.md) | Claude-specific guidance for the CLI |
