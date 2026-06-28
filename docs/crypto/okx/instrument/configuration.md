---
exchange: okx
source_url: https://www.okx.com/docs-v5/trick_en/#instrument-configuration
anchor_id: instrument-configuration
api_type: API
updated_at: 2026-01-15T17:46:44.071160
---

# Instrument configuration

Users can get the exchange instruments configuration from [`GET /api/v5/public/instruments`](/docs-v5/en/#public-data-rest-api-get-instruments).

Subsequent instrument updates, such as tick size changes and new listings will be published from the websocket [`instruments`](/docs-v5/en/#public-data-websocket-instruments-channel) channel.