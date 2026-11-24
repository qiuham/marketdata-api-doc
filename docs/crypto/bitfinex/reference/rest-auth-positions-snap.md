---
api_type: reference
source_type: llms_txt
version: ''
scope: crypto
asset_class: digital_asset
domain: exchanges
provider: bitfinex
provider_name: Bitfinex
product: api
product_id: bitfinex
source_url: 'https://docs.bitfinex.com/reference/rest-auth-positions-snap'
updated_at: 2026-11-24
---

# Positions Snapshot

Returns position snapshots of user positions between the specified start and end perimiters. Snapshots are taken daily.

#### Response data

| Index    | Field                     | Type                                                                | Description                                                                 |
| :------- | :------------------------ | :------------------------------------------------------------------ | :-------------------------------------------------------------------------- |
| \[0...n] | POSITION\_SNAPSHOT\_ARRAY | [Position snapshot array](#position-snapshot-entry-arrays-index-0n) | Each index contains one of the n\` current user's position snapshot entries |

#### Position snapshot entry arrays (index \[0...n])

<HTMLBlock>{`
<table>
  <thead>
    <tr>
      <th>Index</th>
      <th>Field</th>
      <th>Type</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>[0]</td>
      <td>SYMBOL</td>
      <td>string</td>
      <td>Pair (tBTCUSD, …).</td>
    </tr>
    <tr>
      <td>[1]</td>
      <td>STATUS</td>
      <td>string</td>
      <td>Status (ACTIVE).</td>
    </tr>
    <tr>
      <td>[2]</td>
      <td>AMOUNT</td>
      <td>float</td>
      <td>Size of the position. A positive value indicates a long position; a negative value indicates a short position.</td>
    </tr>
    <tr>
      <td>[3]</td>
      <td>BASE_PRICE</td>
      <td>float</td>
      <td>Base price of the position. (Average traded price of the previous orders of the position)</td>
    </tr>
    <tr>
      <td>[4]</td>
      <td>FUNDING</td>
      <td>float</td>
      <td>Funding amount</td>
    </tr>
    <tr>
      <td>[5]</td>
      <td>FUNDING_TYPE</td>
      <td>int</td>
      <td>0 for daily, 1 for term.</td>
    </tr>
    <tr>
      <td colspan="4">
        <div class="placeholders">[ . . . ]</div>
      </td>
    </tr>
    <tr>
      <td>[11]</td>
      <td>POSITION_ID</td>
      <td>int</td>
      <td>Position identifier</td>
    </tr>
    <tr>
      <td>[12]</td>
      <td>MTS_CREATE</td>
      <td>int</td>
      <td>Timestamp of creation (millis)</td>
    </tr>
    <tr>
      <td>[13]</td>
      <td>MTS_UPDATE</td>
      <td>int</td>
      <td>Timestamp of last update (millis)</td>
    </tr>
    <tr>
      <td colspan="4">
        <div class="placeholders">[ . . . ]</div>
      </td>
    </tr>
  </tbody>
</table>



<style>
  td:has(div.placeholders) {
    background-color: #ebebeb
  }
  
  .placeholders {
    height: 10px;
    text-align: center;
    font-size: 16px;
    
    line-height: 8px;
  }
</style>
`}</HTMLBlock>

**Ratelimit**: 90 req/min

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "api-settings",
    "version": "2"
  },
  "servers": [
    {
      "url": "https://api.bitfinex.com/v2"
    }
  ],
  "security": [
    {}
  ],
  "paths": {
    "/auth/r/positions/snap": {
      "post": {
        "summary": "Positions Snapshot",
        "description": "Returns position snapshots of user positions between the specified start and end perimiters. Snapshots are taken daily.",
        "operationId": "rest-auth-positions-snap",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "start": {
                    "type": "integer",
                    "description": "Millisecond start time"
                  },
                  "end": {
                    "type": "integer",
                    "description": "Millisecond end time"
                  },
                  "limit": {
                    "type": "integer",
                    "description": "Number of records (Max 500)",
                    "default": "50"
                  },
                  "id": {
                    "type": "integer",
                    "description": "Position id (can be passed to retrieve a specific position)"
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "200",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "\n[\n  [\n  'tETHUSD', //SYMBOL\t\n  'ACTIVE', //STATUS\n  -0.2, //AMOUNT\n  167.01, //BASE_PRICE\n  0, //FUNDING\n  0, //FUNDING TYPE\n  null, //PLACEHOLDER\n  null, //PLACEHOLDER\n  null, //PLACEHOLDER\n  null, //PLACEHOLDER\n  null, //PLACEHOLDER\n  142661142, //POSITION_ID\n  1579552390000, //MTS_CREATE\n  1579552390000, //MTS_UPDATE\n  null, //PLACEHOLDER\n  null, //PLACEHOLDER\n  null, //PLACEHOLDER\n  null, //PLACEHOLDER\n  null, //PLACEHOLDER\n  null //PLACEHOLDER\n\t], //POSITION_SNAPSHOT_ARRAY\n  ...\n]"
                  }
                }
              }
            }
          },
          "400": {
            "description": "400",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {}
                }
              }
            }
          }
        }
      }
    }
  },
  "x-readme": {
    "headers": [],
    "explorer-enabled": true,
    "proxy-enabled": true
  },
  "x-readme-fauxas": true
}
```
