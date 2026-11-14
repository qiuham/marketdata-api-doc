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
source_url: 'https://docs.kraken.com/home/sdks'
updated_at: 2026-11-13
---

# SDKs

> Official Kraken SDKs for Spot and Derivatives, plus community libraries

> [card] [Go](https://docs.kraken.com/home/sdks/go.md)
>
> api-go. Spot and Derivatives, REST and WebSocket. The most complete coverage.

> [card] [Rust](https://docs.kraken.com/home/sdks/rust.md)
>
> kraken-sdk. Spot REST and WebSocket v2, plus Derivatives streams and order entry over the Unified WebSocket. Async-native.

## Which one to use

| | Go | Rust |
| :- | :- | :- |
| Spot | Yes | Yes |
| Derivatives | Yes | Yes |
| Status | Stable | Stable |

## Other tools

> [card] [kraken-cli](https://docs.kraken.com/home/cli.md)
>
> One install, three binaries: `kraken`, `kraken-mcp` and `kraken-shell`. 188 commands for Spot and Derivatives trading, paper trading, scripting, and AI agent support.

> [card] [MCP server](https://docs.kraken.com/home/mcp.md)
>
> `kraken-mcp` serves 152 of the CLI's commands as MCP tools for LLM agents.

## Community libraries

> [!NOTE]
>
> These libraries are not officially maintained by Kraken. Review before using in production.

| Library | Language | Scope | Repository |
| :- | :- | :- | :- |
| kraken-wsclient-py | Python | WebSocket only (Spot) | [github.com/krakenfx/kraken-wsclient-py](https://github.com/krakenfx/kraken-wsclient-py) |
| kraken-api-client | PHP | REST (example only) | [github.com/krakenfx/kraken-api-client](https://github.com/krakenfx/kraken-api-client) |
