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
source_url: 'https://docs.kraken.com/api-reference/account-data/get-api-key-info'
updated_at: 2026-11-13
---

# Get API Key Info

> Retrieve information about the API key that is used to make the request, including its name, permissions, restrictions, and usage timestamps.

**API Key Permissions Required:** `None`




## OpenAPI

````yaml /openapi/spot-rest.yaml post /private/GetApiKeyInfo
openapi: 3.0.0
info:
  title: REST API
  version: 1.1.0
  description: ''
servers:
  - url: https://api.kraken.com/0
    description: Production Server
security:
  - API-Key: []
    API-Sign: []
tags:
  - name: Market Data
  - name: Account Data
  - name: Trading
  - name: Algo Trading
    description: >
      Algo Trading endpoints create and manage **strategies**: parent
      instructions that Kraken executes on your behalf as a series of regular
      child orders.


      The only strategy available today is **TWAP** (time-weighted average
      price). A TWAP buys or sells a total `volume` evenly between `starttm` and
      `expiretm`. How child orders are sized, timed and placed is managed by
      Kraken and may change as execution improves.


      An algo runs as a strategy. In Kraken Pro, TWAP strategies show under
      Bots.


      ### Strategy lifecycle


      `pending` → `open` → `closed` | `expired` | `cancelled`


      - `pending`: accepted, waiting for `starttm`.

      - `open`: running, child orders are being placed.

      - `closed`: the full `volume` was filled before `expiretm`.

      - `expired`: `expiretm` was reached before the full `volume` was filled.

      - `cancelled`: cancelled with `CancelStrategy`.


      TWAP child orders are immediate-or-cancel limit orders and do not rest on
      the book. Completed child orders appear in `ClosedOrders`, and fills
      appear in trade history. Use the strategy endpoints to monitor overall
      progress.
  - name: funding-beta
    x-group: Funding (Beta)
    x-displayName: Funding (Beta)
  - name: Funding
    x-group: Funding (Legacy)
    x-displayName: Funding (Legacy)
  - name: Subaccounts
    description: >-
      Subaccounts are currently only available to institutional clients. Please
      contact your Account Manager for more details.
  - name: Earn
    description: >
      The earn API allows interacting with all of Kraken's yield generating
      products. It replaces the old `/staking` part of the API.


      The different available earn products are represented by earn strategies.
      This corresponds to the legacy `Staking/Assets`. `Stake`/`Unstake` are
      replaced by `Allocate`/`Deallocate`.


      ### Overview of the available endpoints under `/Earn`:


      - `Strategies` - list all earn strategies for which you are eligible or
      have a balance.

      - `Allocations` - lists the balance in your earn account for each
      strategy. Requires the `Query Funds` API key permission.

      - `Allocate`/`Deallocate` - allocate/deallocate to an earn strategy
      through an async operation. Requires the `Earn Funds` API key permission.

      - `AllocateStatus`/`DeallocateStatus` - verifies the state of the last
      allocation/deallocation. Requires the `Earn Funds` or `Query Funds` API
      key permission.


      ### Example usage:


      ### Determine which funds are earning rewards:


      1. Call `Strategies` to obtain information about the relevant strategy.
      The `lock_type` field shows whether bonding/unbonding funds are earning
      yield. The relevant fields are `bonding_rewards`/`unbonding_rewards`.

      2. Call `Allocations` for the relevant strategy. From the previous step,
      for strategies where bonding/unbonding does not earn yield, substract
      these balances from `amount_allocated.total` to determine which balances
      are currently earning.


      ### Get allocatable balance:


      Call `/0/private/BalanceEx`, subtract `hold_trading` amount. Remaining
      balance is available for allocation to a strategy.


      ### Geo restrictions:


      Some earn strategies are not available in all geographic regions.
      `Strategies` will return only strategies available to the caller.
  - name: Transparency
paths:
  /private/GetApiKeyInfo:
    post:
      tags:
        - Account Data
      summary: Get API Key Info
      description: >
        Retrieve information about the API key that is used to make the request,
        including its name, permissions, restrictions, and usage timestamps.


        **API Key Permissions Required:** `None`
      operationId: getApiKeyInfo
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                nonce:
                  $ref: '#/components/schemas/nonce'
                otp:
                  type: string
                  description: >-
                    Two-factor authentication password (required only if 2FA is
                    configured for the API key)
              required:
                - nonce
      responses:
        '200':
          description: API key information retrieved.
          content:
            application/json:
              schema:
                type: object
                properties:
                  result:
                    title: ApiKeyInfo
                    description: API Key Information
                    type: object
                    properties:
                      api_key_name:
                        type: string
                        description: Name/label assigned to the API key
                      api_key:
                        type: string
                        description: The API key string
                      nonce:
                        type: string
                        description: Current nonce value for the API key
                      nonce_window:
                        type: integer
                        format: int64
                        description: Custom nonce window value (0 if not configured)
                      permissions:
                        type: array
                        items:
                          type: string
                        description: >
                          List of permissions assigned to the API key. Values
                          correspond to the API Key permission settings:


                          | Value | API Key Permission |

                          |---|---|

                          | `query-funds` | Funds permissions - Query |

                          | `add-funds` | Funds permissions - Deposit |

                          | `withdraw-funds` | Funds permissions - Withdraw |

                          | `earn-funds` | Funds permissions - Earn |

                          | `query-open-trades` | Orders and trades - Query open
                          orders & trades |

                          | `query-closed-trades` | Orders and trades - Query
                          closed orders & trades |

                          | `modify-trades` | Orders and trades - Create &
                          modify orders |

                          | `close-trades` | Orders and trades - Cancel & close
                          orders |

                          | `query-ledger` | Data - Query ledger entries |

                          | `export-data` | Data - Export data |

                          | `create-ws-token` | WebSocket interface - On |

                          | `add-withdraw-address` | Add withdrawal addresses |

                          | `update-withdraw-address` | Update withdrawal
                          addresses |
                      iban:
                        type: string
                        description: >-
                          IIBAN (Internal IBAN) of the account associated with
                          the API key
                      valid_until:
                        type: string
                        description: Unix timestamp for key expiration (0 if not set)
                      query_from:
                        type: string
                        description: >-
                          Unix timestamp for earliest allowed query date (0 if
                          not set)
                      query_to:
                        type: string
                        description: >-
                          Unix timestamp for latest allowed query date (0 if not
                          set)
                      created_time:
                        type: string
                        description: Unix timestamp of when the API key was created
                      modified_time:
                        type: string
                        description: Unix timestamp of when the API key was last modified
                      ip_allowlist:
                        type: array
                        items:
                          type: string
                        description: >-
                          List of IP addresses or ranges allowed to use this API
                          key (empty if not restricted)
                      last_used:
                        type: string
                        nullable: true
                        description: >-
                          Unix timestamp of when the API key was last used (null
                          if never used)
                  error:
                    $ref: '#/components/schemas/error'
                example:
                  error: []
                  result:
                    apiKeyName: my-api-key
                    apiKey: 4/SDrDBcOOPnm3nPlNfEMMJDeRcIVqPz+QhRxIodyZbI9po/aVRiHsgX
                    nonce: '1772627060997'
                    nonceWindow: 0
                    permissions:
                      - query-funds
                      - withdraw-funds
                      - query-open-trades
                      - modify-trades
                    iban: AA88 N84G WOAK NMOI
                    validUntil: '0'
                    queryFrom: '0'
                    queryTo: '0'
                    createdTime: '1772542900'
                    modifiedTime: '1772543095'
                    ipAllowlist: []
                    lastUsed: '1772627061'
components:
  schemas:
    nonce:
      description: Nonce used in construction of `API-Sign` header
      type: integer
      format: int64
    error:
      type: array
      items:
        description: Kraken API error
        type: string
        example: EGeneral:Invalid arguments
  securitySchemes:
    API-Key:
      type: apiKey
      description: The "API-Key" header should contain your API key.
      name: API-Key
      in: header
    API-Sign:
      type: apiKey
      description: >-
        Authenticated requests should be signed with the "API-Sign" header,
        using a signature generated with your private key, nonce, encoded
        payload, and URI path.
      name: API-Sign
      in: header

````
