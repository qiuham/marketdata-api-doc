---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/finance/rwa/place-order
api_type: REST
updated_at: 2026-07-18 19:01:07.962476
---

# MMWS Integration

Market Maker WebSocket (MMWS) is a dedicated WebSocket access path for market makers and institutional clients. It provides a more stable portal for private, trade, public market data, and SBE WebSocket traffic.

MMWS is designed for connection stability. It can reduce unexpected disconnects, reduce delayed pushes, and avoid handshake failures caused by frequent reconnect attempts. It does not guarantee lower absolute latency than the regular public WebSocket endpoint.

## Supported paths

MMWS supports the following V5 WebSocket paths:

Type| Path  
---|---  
Private stream| `/v5/private`  
Trade| `/v5/trade`  
Linear market data| `/v5/public/linear`  
Inverse market data| `/v5/public/inverse`  
Spot market data| `/v5/public/spot`  
Option market data| `/v5/public/option`  
Spread market data| `/v5/public/spread`  
Spot SBE market data| `/v5/public-sbe/spot`  
Linear SBE market data| `/v5/public-sbe/linear`  
Inverse SBE market data| `/v5/public-sbe/inverse`  
  
Use the dedicated hostname provided by Bybit with the same WebSocket path structure:
    
    
    wss://{MMWS hostname}/v5/private  
    wss://{MMWS hostname}/v5/trade  
    wss://{MMWS hostname}/v5/public/linear  
    

## Access setup

To request MMWS access, provide the IP addresses or CIDR ranges that will connect to MMWS. Bybit supports up to 10 IP entries or CIDR ranges for whitelisting. CIDR ranges are recommended when your infrastructure may scale or rotate within a fixed network block.

After approval, Bybit will provide private MMWS hostnames for your account. Keep these hostnames confidential. If malicious traffic is detected through the assigned hostnames, Bybit may disable them urgently.

## Integration steps

  1. Confirm the WebSocket paths your system needs, including whether you require JSON streams, SBE streams, or order entry through `/v5/trade`.
  2. Send your source IP addresses or CIDR ranges to your Bybit contact for whitelisting.
  3. Replace the public WebSocket hostname with the dedicated MMWS hostname provided by Bybit.
  4. Keep the same authentication, subscription, ping/pong, reconnect, and message parsing logic used by the standard V5 WebSocket API.
  5. Monitor disconnect frequency, delayed push events, and reconnect behavior after migration.



## Operational notes

  * MMWS is a stability-focused access path, not a guaranteed latency shortcut.
  * Do not share the assigned MMWS hostnames outside your approved infrastructure.
  * If your source IP changes, update the whitelist before routing production traffic through the dedicated hostname.
  * For SBE payload structure and channel details, see [SBE Basic Information](/docs/v5/sbe/sbe-basic-info).

---

# MMWS 接入指南

Market Maker WebSocket (MMWS) 是面向做市商與機構客戶的專屬 WebSocket 接入路徑。它為私有頻道、交易頻道、公共行情頻道以及 SBE WebSocket 流量提供更穩定的入口。

MMWS 的設計重點是連線穩定性。它可以減少非預期斷線、降低推送延遲發生率，並避免因頻繁重連而導致的握手失敗。不過，MMWS 並不保證相較標準 stream.bybit.com 具備絕對延遲優勢。

## 支援路徑

MMWS 支援以下 WebSocket 路徑:

類型| 路徑  
---|---  
私有頻道| `/v5/private`  
交易| `/v5/trade`  
SBE交易| `/v5/trade/-sbe` (6月主網)  
Linear 行情| `/v5/public/linear`  
Inverse 行情| `/v5/public/inverse`  
現貨行情| `/v5/public/spot`  
期權行情| `/v5/public/option`  
Spread 行情| `/v5/public/spread`  
現貨 SBE 行情| `/v5/public-sbe/spot`  
Linear SBE 行情| `/v5/public-sbe/linear`  
Inverse SBE 行情| `/v5/public-sbe/inverse`  
  
使用 Bybit 提供的專屬 hostname，並保持相同的 WebSocket 路徑結構:
    
    
    wss://{MMWS hostname}/v5/private  
    wss://{MMWS hostname}/v5/trade  
    wss://{MMWS hostname}/v5/public/linear  
    

## 接入配置

如需申請 MMWS 接入，請提供將連線至 MMWS 的 IP 位址或 CIDR 範圍。Bybit 支援最多 10 個 IP 條目或 CIDR 範圍用於白名單配置。若您的基礎設施可能在固定網段內擴展或輪換，建議使用 CIDR 範圍。

審核通過後，Bybit 會為您的帳戶提供私有 MMWS hostname。請對這些 hostname 保密。若 Bybit 偵測到透過已分配 hostname 發起的惡意流量，Bybit 可能會緊急停用相關 hostname。

## 接入步驟

  1. 確認系統需要使用的 WebSocket 路徑，包括是否需要 JSON 流、SBE 流，或透過 `/v5/trade` 進行下單。
  2. 將源 IP 位址或 CIDR 範圍提交給您的 Bybit 對接人，用於白名單配置。
  3. 將 stream.bybit.com 替換為 Bybit 提供的專屬 MMWS hostname。
  4. 保持與 stream.bybit.com 相同的鑑權、訂閱、ping/pong、重連和消息解析邏輯。
  5. 遷移後監控斷線頻率、推送延遲事件以及重連行為。



## 運維注意事項

  * MMWS 是以穩定性為重點的接入路徑，並不是保證低延遲的捷徑。
  * 不要在已批准的基礎設施之外分享已分配的 MMWS hostname。
  * 若源 IP 發生變更，請先更新白名單，再將生產流量路由到專屬 hostname。
  * 關於 SBE payload 結構和頻道詳情，請參考 [SBE 基本信息](/docs/zh-TW/v5/sbe/sbe-basic-info)。