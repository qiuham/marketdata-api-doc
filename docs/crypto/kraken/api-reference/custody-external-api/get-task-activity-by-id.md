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
source_url: 'https://docs.kraken.com/api-reference/custody-external-api/get-task-activity-by-id'
updated_at: 2026-11-13
---

# Get task activity by id

> Returns a single task activity and the curated task it belongs to. The embedded task uses the same flat atomic `instructions[]` model as Get task by id. Domain and organization scope are derived from the activity's task; there is no request `org_iiban`. Unknown, out-of-scope, and malformed activity identifiers all return `403`.

**Rate limit:** 200 requests per 30 seconds per IP.



## OpenAPI

````yaml /openapi/insto-custody-rest.yaml get /v0/insto/custody/tasks/activities/{activity_id}
openapi: 3.0.0
info:
  title: Insto Custody External REST API
  version: 1.0.0
  description: ''
servers:
  - url: https://api.kraken.com
    description: Production Server
security: []
tags:
  - name: Custody External API
paths:
  /v0/insto/custody/tasks/activities/{activity_id}:
    get:
      tags:
        - Custody External API
      summary: Get task activity by id
      description: >-
        Returns a single task activity and the curated task it belongs to. The
        embedded task uses the same flat atomic `instructions[]` model as Get
        task by id. Domain and organization scope are derived from the
        activity's task; there is no request `org_iiban`. Unknown, out-of-scope,
        and malformed activity identifiers all return `403`.


        **Rate limit:** 200 requests per 30 seconds per IP.
      operationId: getV0InstoCustodyTasksActivitiesId
      parameters:
        - in: path
          name: activity_id
          required: true
          description: Activity identifier, an `A`-prefixed 14-char base32 string.
          schema:
            type: string
            example: AABCDEFG23456A
          style: simple
      responses:
        '200':
          description: The requested task activity and its embedded curated task.
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    description: >-
                      Activity identifier, an `A`-prefixed 14-char base32
                      string.
                    type: string
                    example: AABCDEFG23456A
                  created_at:
                    description: RFC 3339 UTC timestamp when the activity occurred.
                    type: string
                    format: date-time
                    example: '2026-01-15T12:34:56Z'
                  type:
                    description: >-
                      Activity action discriminator (lowercase), e.g. `created`,
                      `review_approved`, `review_denied`, `executed`.
                    type: string
                    example: review_approved
                  state:
                    description: Task state at the time of the activity (lowercase).
                    type: string
                    example: pending
                  comment:
                    description: Reviewer-supplied comment, when present.
                    type: string
                    example: Transaction approved by finance team.
                  user:
                    description: >-
                      Resolved user or API-key details for the actor, when
                      available at read time.
                    type: object
                    properties:
                      full_name:
                        description: Display name of the actor.
                        type: string
                        example: Alex Doe
                      role:
                        description: Role of the actor at the time of the activity.
                        type: string
                        example: vault_admin
                      ip_address:
                        description: Source IP address recorded for the activity.
                        type: string
                        example: 203.0.113.10
                      iiban:
                        description: 16-char IIBAN identifying the actor.
                        type: string
                        example: ABCD EFGH IJKL MNOP
                  task:
                    description: >-
                      Curated details of the task this activity belongs to. Uses
                      flat atomic `instructions[]`; does not include `payload`,
                      `operations`, or a nested activity timeline.
                    type: object
                    properties:
                      id:
                        description: >-
                          Task identifier, an approval UUID (UUID v4).
                          T-prefixed identifiers are not accepted or returned.
                          Responses always emit lowercase. Requests accept any
                          letter case.
                        type: string
                        example: 550e8400-e29b-41d4-a716-446655440000
                      type:
                        description: >-
                          Coarse task-level discriminator. Always
                          `normalized_task`. Read the per-instruction `type`
                          inside `instructions[]` for the specific actions.
                        type: string
                        example: normalized_task
                      state:
                        description: >-
                          Lifecycle state of the task. One of `pending`,
                          `approved`, `rejected`, `canceled`, `expired`,
                          `failed`, `executed`.
                        type: string
                        example: pending
                      created_at:
                        description: RFC 3339 UTC timestamp when the task was created.
                        type: string
                        format: date-time
                        example: '2026-01-15T12:34:56Z'
                      updated_at:
                        description: RFC 3339 UTC timestamp when the task was last updated.
                        type: string
                        format: date-time
                        example: '2026-01-15T12:35:56Z'
                      expires_at:
                        description: >-
                          RFC 3339 UTC timestamp when the task expires if no
                          decision is reached.
                        type: string
                        format: date-time
                        example: '2026-01-16T12:34:56Z'
                  initiator:
                    description: User or API key that initiated the task.
                    type: object
                    properties:
                      full_name:
                        description: >-
                          Display name of the initiator at the time the task was
                          created.
                        type: string
                        example: Alex Doe
                      role:
                        description: >-
                          Role assigned to the initiator at the time the task
                          was created.
                        type: string
                        example: vault_admin
                      ip_address:
                        description: >-
                          Source IP address recorded when the task was
                          initiated.
                        type: string
                        example: 203.0.113.10
                      iiban:
                        description: >-
                          16-char IIBAN identifying the initiating user or API
                          key.
                        type: string
                        example: ABCD EFGH IJKL MNOP
                  quorum_type:
                    description: >-
                      Scope of the quorum required to advance the task. `domain`
                      for org-wide quorum, `vault` for vault-scoped quorum.
                    type: string
                    example: vault
                  can_review:
                    description: >-
                      True if the caller may still cast a review decision on
                      this task.
                    type: boolean
                    example: true
                  reviewer_statistics:
                    description: >-
                      Quorum counters for single-quorum tasks: how many assigned
                      reviewers have approved, denied, or not yet decided, and
                      how many approvals the task still needs. Omitted for
                      multi-quorum tasks. Use `subquorum_approvals` when
                      `reviewer_statistics_label` is `multiquorum`. For the
                      individual reviewers behind these counters, read
                      `activities`.
                    type: object
                    properties:
                      current_count:
                        description: >-
                          Total number of reviewers currently assigned to the
                          task.
                        type: integer
                        format: int32
                        example: 3
                      approved:
                        description: Number of reviewers who have approved.
                        type: integer
                        example: 2
                        format: int32
                      denied:
                        description: Number of reviewers who have denied.
                        type: integer
                        format: int32
                        example: 0
                      undecided:
                        description: >-
                          Number of assigned reviewers who have not yet cast a
                          decision.
                        type: integer
                        example: 1
                        format: int32
                      required_quorum:
                        description: >-
                          Number of approving reviewers required for the task to
                          advance.
                        type: integer
                        format: int32
                        example: 2
                    required:
                      - approved
                      - denied
                      - undecided
                  current_user_decision:
                    description: >-
                      The caller's own decision on this task. One of
                      `undecided`, `approved`, `denied`.
                    type: string
                    example: undecided
                  vault_info:
                    description: >-
                      Vault the task is scoped to. Omitted for domain-level
                      tasks that do not target a specific vault.
                    type: object
                    properties:
                      id:
                        description: >-
                          Vault identifier, a `V`-prefixed 14-char base32 string
                          with a final check character.
                        type: string
                        example: VABCDEF234567A
                      name:
                        description: Display name of the vault.
                        type: string
                        example: My Vault
                      status:
                        description: >-
                          Current vault lifecycle status (lowercase, e.g.
                          `active`, `archived`).
                        type: string
                        example: active
                      subquorum_config:
                        description: >-
                          Vault's current subquorum policy, the group structure
                          used to compute approvals on multi-quorum tasks.
                        type: object
                        properties:
                          groups:
                            type: array
                            items:
                              type: object
                              properties:
                                id:
                                  type: string
                                  example: 1ef8cecf-5d7b-4f83-9640-96d74db0e858
                                required:
                                  type: integer
                                  example: 2
                                  format: int32
                                members:
                                  type: array
                                  items:
                                    type: object
                                    properties:
                                      iiban:
                                        type: string
                                        example: ABCD EFGH IJKL MNOP
                                      full_name:
                                        type: string
                                        example: Alex Doe
                                      email:
                                        type: string
                                        example: alex.doe@example.com
                                      role:
                                        type: string
                                        example: vault_admin
                                    required:
                                      - iiban
                              required:
                                - id
                                - required
                                - members
                        required:
                          - groups
                    required:
                      - id
                  reviewer_statistics_label:
                    description: >-
                      Indicates which reviewer-tally field to consult.
                      `standard` means use `reviewer_statistics`; `multiquorum`
                      means use `subquorum_approvals`.
                    type: string
                    example: standard
                  subquorum_snapshot:
                    description: >-
                      Subquorum policy snapshot taken when the task was created.
                      Approvals are evaluated against this snapshot so a later
                      policy change cannot retroactively invalidate decisions
                      already cast.
                    type: object
                    properties:
                      groups:
                        description: Subquorum groups captured in the snapshot.
                        type: array
                        items:
                          type: object
                          properties:
                            id:
                              type: string
                              example: 1ef8cecf-5d7b-4f83-9640-96d74db0e858
                            required:
                              type: integer
                              example: 2
                              format: int32
                            members:
                              type: array
                              items:
                                type: object
                                properties:
                                  iiban:
                                    type: string
                                    example: ABCD EFGH IJKL MNOP
                                  full_name:
                                    type: string
                                    example: Alex Doe
                                  email:
                                    type: string
                                    example: alex.doe@example.com
                                  role:
                                    type: string
                                    example: vault_admin
                                required:
                                  - iiban
                          required:
                            - id
                            - required
                            - members
                    required:
                      - groups
                  subquorum_approvals:
                    description: >-
                      Per-group approval tally for multi-quorum tasks. Each
                      entry lists a group's ID and the IIBANs of members in that
                      group who have approved so far.
                    type: array
                    items:
                      type: object
                      properties:
                        group_id:
                          description: >-
                            Subquorum group identifier (UUID v4) matching an
                            entry in `subquorum_snapshot.groups`.
                          type: string
                          example: 1ef8cecf-5d7b-4f83-9640-96d74db0e858
                        approved_iibans:
                          description: IIBANs of group members who have approved the task.
                          type: array
                          items:
                            type: string
                            example: ABCD EFGH IJKL MNOP
                      required:
                        - group_id
                        - approved_iibans
                  instructions:
                    type: array
                    items:
                      oneOf:
                        - type: object
                          properties:
                            type:
                              type: string
                              enum:
                                - update_subquorum
                            version:
                              type: integer
                              format: int32
                            execution:
                              type: object
                              properties:
                                state:
                                  type: string
                                started_at:
                                  type: string
                                  format: date-time
                                  description: >-
                                    RFC 3339 UTC timestamp when instruction
                                    execution started. Omitted when execution
                                    has not started.
                                  example: '2026-01-15T12:34:56Z'
                                completed_at:
                                  type: string
                                  format: date-time
                                  description: >-
                                    RFC 3339 UTC timestamp when instruction
                                    execution completed. Omitted when execution
                                    has not completed.
                                  example: '2026-01-15T12:35:56Z'
                                error:
                                  type: string
                              required:
                                - state
                            vault_id:
                              type: string
                            groups:
                              type: array
                              items:
                                type: object
                                properties:
                                  id:
                                    type: string
                                  required:
                                    type: integer
                                    format: int32
                                  members:
                                    type: array
                                    items:
                                      type: object
                                      properties:
                                        iiban:
                                          type: string
                                        full_name:
                                          type: string
                                        email:
                                          type: string
                                        role:
                                          type: string
                                      required:
                                        - iiban
                                required:
                                  - id
                                  - required
                                  - members
                          required:
                            - version
                            - vault_id
                            - groups
                            - type
                          title: update_subquorum
                          description: >-
                            Add, remove, or change the sub-quorum groups that
                            approve activity on a vault.
                        - type: object
                          properties:
                            type:
                              type: string
                              enum:
                                - update_vault_user
                            version:
                              type: integer
                              format: int32
                            execution:
                              type: object
                              properties:
                                state:
                                  type: string
                                started_at:
                                  type: string
                                  format: date-time
                                  description: >-
                                    RFC 3339 UTC timestamp when instruction
                                    execution started. Omitted when execution
                                    has not started.
                                  example: '2026-01-15T12:34:56Z'
                                completed_at:
                                  type: string
                                  format: date-time
                                  description: >-
                                    RFC 3339 UTC timestamp when instruction
                                    execution completed. Omitted when execution
                                    has not completed.
                                  example: '2026-01-15T12:35:56Z'
                                error:
                                  type: string
                              required:
                                - state
                            vault_id:
                              type: string
                            operation_type:
                              type: string
                              enum:
                                - add
                                - remove
                            user:
                              type: string
                            reason:
                              type: string
                            vault_name:
                              type: string
                          required:
                            - version
                            - vault_id
                            - operation_type
                            - user
                            - type
                          title: update_vault_user
                          description: Grant or revoke a user's access to a vault.
                        - type: object
                          properties:
                            type:
                              type: string
                              enum:
                                - update_vault_policy
                            version:
                              type: integer
                              format: int32
                            execution:
                              type: object
                              properties:
                                state:
                                  type: string
                                started_at:
                                  type: string
                                  format: date-time
                                  description: >-
                                    RFC 3339 UTC timestamp when instruction
                                    execution started. Omitted when execution
                                    has not started.
                                  example: '2026-01-15T12:34:56Z'
                                completed_at:
                                  type: string
                                  format: date-time
                                  description: >-
                                    RFC 3339 UTC timestamp when instruction
                                    execution completed. Omitted when execution
                                    has not completed.
                                  example: '2026-01-15T12:35:56Z'
                                error:
                                  type: string
                              required:
                                - state
                            vault_id:
                              type: string
                            policy:
                              type: object
                              properties:
                                type:
                                  type: string
                                amount:
                                  type: string
                                required:
                                  type: integer
                                  format: int32
                                available:
                                  type: integer
                                  format: int32
                                enable:
                                  type: boolean
                              required:
                                - type
                          required:
                            - version
                            - vault_id
                            - policy
                            - type
                          title: update_vault_policy
                          description: Change a vault's approval policy.
                        - type: object
                          properties:
                            type:
                              type: string
                              enum:
                                - request_withdrawal
                            version:
                              type: integer
                              format: int32
                            execution:
                              type: object
                              properties:
                                state:
                                  type: string
                                started_at:
                                  type: string
                                  format: date-time
                                  description: >-
                                    RFC 3339 UTC timestamp when instruction
                                    execution started. Omitted when execution
                                    has not started.
                                  example: '2026-01-15T12:34:56Z'
                                completed_at:
                                  type: string
                                  format: date-time
                                  description: >-
                                    RFC 3339 UTC timestamp when instruction
                                    execution completed. Omitted when execution
                                    has not completed.
                                  example: '2026-01-15T12:35:56Z'
                                error:
                                  type: string
                              required:
                                - state
                            vault_id:
                              type: string
                            asset:
                              type: string
                            asset_class:
                              type: string
                            amount:
                              type: string
                            address_name:
                              type: string
                            fee_amount:
                              type: string
                              description: >-
                                Fee amount for the withdrawal, fixed-precision
                                decimal as string.
                              example: '0.00010000'
                            fee_asset:
                              type: string
                              description: Asset code the fee is charged in.
                              example: BTC
                            fee_asset_class:
                              type: string
                              description: >-
                                Asset class of the fee asset (e.g. `currency`,
                                `tokenized_asset`).
                              example: currency
                            fee_included:
                              type: boolean
                              description: >-
                                Whether the fee is included in the withdrawal
                                amount.
                              example: false
                            fee_level:
                              type: string
                              description: >-
                                Fee tier selected for the withdrawal (e.g.
                                `normal`).
                              example: normal
                            fee_quote_id:
                              type: string
                              description: >-
                                Identifier of the withdrawal fee quote the fee
                                was derived from, when a quote was used.
                              example: QABCDEF234567A
                            comment:
                              type: string
                            memo:
                              type: string
                            vault_name:
                              type: string
                            address:
                              type: string
                            wallet_custodian:
                              type: string
                            business_name:
                              type: string
                          required:
                            - version
                            - vault_id
                            - asset
                            - asset_class
                            - amount
                            - address_name
                            - fee
                            - type
                          title: request_withdrawal
                          description: >-
                            Withdraw assets from a vault to an allow-listed
                            external address.
                        - type: object
                          properties:
                            type:
                              type: string
                              enum:
                                - remove_org_user
                            version:
                              type: integer
                              format: int32
                            execution:
                              type: object
                              properties:
                                state:
                                  type: string
                                started_at:
                                  type: string
                                  format: date-time
                                  description: >-
                                    RFC 3339 UTC timestamp when instruction
                                    execution started. Omitted when execution
                                    has not started.
                                  example: '2026-01-15T12:34:56Z'
                                completed_at:
                                  type: string
                                  format: date-time
                                  description: >-
                                    RFC 3339 UTC timestamp when instruction
                                    execution completed. Omitted when execution
                                    has not completed.
                                  example: '2026-01-15T12:35:56Z'
                                error:
                                  type: string
                              required:
                                - state
                            org_iiban:
                              type: string
                            user_iiban:
                              type: string
                            reason:
                              type: string
                            user_full_name:
                              type: string
                            user_email:
                              type: string
                          required:
                            - version
                            - org_iiban
                            - user_iiban
                            - type
                          title: remove_org_user
                          description: Remove a user from the organization.
                        - type: object
                          properties:
                            type:
                              type: string
                              enum:
                                - create_user
                            version:
                              type: integer
                              format: int32
                            execution:
                              type: object
                              properties:
                                state:
                                  type: string
                                started_at:
                                  type: string
                                  format: date-time
                                  description: >-
                                    RFC 3339 UTC timestamp when instruction
                                    execution started. Omitted when execution
                                    has not started.
                                  example: '2026-01-15T12:34:56Z'
                                completed_at:
                                  type: string
                                  format: date-time
                                  description: >-
                                    RFC 3339 UTC timestamp when instruction
                                    execution completed. Omitted when execution
                                    has not completed.
                                  example: '2026-01-15T12:35:56Z'
                                error:
                                  type: string
                              required:
                                - state
                            user:
                              type: object
                              properties:
                                email:
                                  type: string
                                role:
                                  type: string
                                full_name:
                                  type: object
                                  properties:
                                    first_name:
                                      type: string
                                    middle_name:
                                      type: string
                                    last_name:
                                      type: string
                                  required:
                                    - first_name
                                    - last_name
                                language:
                                  type: string
                                timezone:
                                  type: string
                                attributes:
                                  type: array
                                  items:
                                    type: string
                              required:
                                - email
                                - role
                                - full_name
                            org_iiban:
                              type: string
                          required:
                            - version
                            - user
                            - type
                          title: create_user
                          description: Create a new organization user.
                        - type: object
                          properties:
                            type:
                              type: string
                              enum:
                                - update_withdrawal_address
                            version:
                              type: integer
                              format: int32
                            execution:
                              type: object
                              properties:
                                state:
                                  type: string
                                started_at:
                                  type: string
                                  format: date-time
                                  description: >-
                                    RFC 3339 UTC timestamp when instruction
                                    execution started. Omitted when execution
                                    has not started.
                                  example: '2026-01-15T12:34:56Z'
                                completed_at:
                                  type: string
                                  format: date-time
                                  description: >-
                                    RFC 3339 UTC timestamp when instruction
                                    execution completed. Omitted when execution
                                    has not completed.
                                  example: '2026-01-15T12:35:56Z'
                                error:
                                  type: string
                              required:
                                - state
                            vault_id:
                              type: string
                            operation_type:
                              type: string
                              enum:
                                - add
                                - remove
                            address:
                              type: object
                              properties:
                                asset:
                                  type: string
                                asset_class:
                                  type: string
                                address_name:
                                  type: string
                                method:
                                  type: string
                                info:
                                  type: object
                                  properties:
                                    address:
                                      type: string
                                    tag:
                                      type: string
                                    beneficiary:
                                      type: object
                                      properties:
                                        recipient:
                                          type: string
                                        type:
                                          type: string
                                        name:
                                          type: string
                                        last_name:
                                          type: string
                                        country:
                                          type: string
                                        province:
                                          type: string
                                        address_1:
                                          type: string
                                        address_2:
                                          type: string
                                        city:
                                          type: string
                                        postal_code:
                                          type: string
                                        vasp_name:
                                          type: string
                                description:
                                  type: string
                                reason:
                                  type: string
                              required:
                                - asset
                                - address_name
                                - method
                                - info
                            vault_name:
                              type: string
                          required:
                            - version
                            - vault_id
                            - operation_type
                            - address
                            - type
                          title: update_withdrawal_address
                          description: >-
                            Add, update, or remove an allow-listed withdrawal
                            address for a vault.
                        - type: object
                          properties:
                            type:
                              type: string
                              enum:
                                - update_user_permission
                            version:
                              type: integer
                              format: int32
                            execution:
                              type: object
                              properties:
                                state:
                                  type: string
                                started_at:
                                  type: string
                                  format: date-time
                                  description: >-
                                    RFC 3339 UTC timestamp when instruction
                                    execution started. Omitted when execution
                                    has not started.
                                  example: '2026-01-15T12:34:56Z'
                                completed_at:
                                  type: string
                                  format: date-time
                                  description: >-
                                    RFC 3339 UTC timestamp when instruction
                                    execution completed. Omitted when execution
                                    has not completed.
                                  example: '2026-01-15T12:35:56Z'
                                error:
                                  type: string
                              required:
                                - state
                            operation_type:
                              type: string
                              enum:
                                - update_role
                                - assign_attribute
                                - revoke_attribute
                            user:
                              type: object
                              properties:
                                iiban:
                                  type: string
                                full_name:
                                  type: string
                                email:
                                  type: string
                                role:
                                  type: string
                              required:
                                - iiban
                                - role
                            reason:
                              type: string
                            role:
                              type: string
                            attribute:
                              type: string
                            org_iiban:
                              type: string
                          required:
                            - version
                            - operation_type
                            - user
                            - type
                          title: update_user_permission
                          description: Change a user's role or attributes.
                        - type: object
                          properties:
                            type:
                              type: string
                              enum:
                                - request_staking_allocation
                            version:
                              type: integer
                              format: int32
                            execution:
                              type: object
                              properties:
                                state:
                                  type: string
                                started_at:
                                  type: string
                                  format: date-time
                                  description: >-
                                    RFC 3339 UTC timestamp when instruction
                                    execution started. Omitted when execution
                                    has not started.
                                  example: '2026-01-15T12:34:56Z'
                                completed_at:
                                  type: string
                                  format: date-time
                                  description: >-
                                    RFC 3339 UTC timestamp when instruction
                                    execution completed. Omitted when execution
                                    has not completed.
                                  example: '2026-01-15T12:35:56Z'
                                error:
                                  type: string
                              required:
                                - state
                            vault_id:
                              type: string
                            config_id:
                              type: string
                            amount:
                              type: string
                            fee_quote_id:
                              type: string
                            fee_level:
                              type: string
                            staking_period_seconds:
                              type: integer
                              format: int32
                            vault_name:
                              type: string
                          required:
                            - version
                            - vault_id
                            - amount
                            - fee_level
                            - type
                          title: request_staking_allocation
                          description: Allocate assets from a vault into staking.
                        - type: object
                          properties:
                            type:
                              type: string
                              enum:
                                - request_transfer_to_spot
                            version:
                              type: integer
                              format: int32
                            execution:
                              type: object
                              properties:
                                state:
                                  type: string
                                started_at:
                                  type: string
                                  format: date-time
                                  description: >-
                                    RFC 3339 UTC timestamp when instruction
                                    execution started. Omitted when execution
                                    has not started.
                                  example: '2026-01-15T12:34:56Z'
                                completed_at:
                                  type: string
                                  format: date-time
                                  description: >-
                                    RFC 3339 UTC timestamp when instruction
                                    execution completed. Omitted when execution
                                    has not completed.
                                  example: '2026-01-15T12:35:56Z'
                                error:
                                  type: string
                              required:
                                - state
                            vault_id:
                              type: string
                            tx_id:
                              type: string
                            amount:
                              type: string
                            asset:
                              type: string
                            asset_class:
                              type: string
                            iiban:
                              type: string
                            fee_amount:
                              type: string
                              description: >-
                                Fee amount for the transfer, fixed-precision
                                decimal as string.
                              example: '0.00010000'
                            fee_asset:
                              type: string
                              description: Asset code the fee is charged in.
                              example: BTC
                            fee_asset_class:
                              type: string
                              description: >-
                                Asset class of the fee asset (e.g. `currency`,
                                `tokenized_asset`).
                              example: currency
                            fee_included:
                              type: boolean
                              description: >-
                                Whether the fee is included in the transfer
                                amount.
                              example: false
                            fee_level:
                              type: string
                              description: >-
                                Fee tier selected for the transfer (e.g.
                                `normal`).
                              example: normal
                            fee_quote_id:
                              type: string
                              description: >-
                                Identifier of the fee quote the fee was derived
                                from, when a quote was used.
                              example: QABCDEF234567A
                            fee_quote_amount:
                              type: string
                              description: >-
                                Fee amount expressed in the quote asset, when a
                                quote conversion applies.
                              example: '5.00'
                            fee_quote_asset:
                              type: string
                              description: Quote asset the fee amount is expressed in.
                              example: USD
                            quote_amount:
                              type: string
                              description: >-
                                Transfer amount expressed in the quote asset,
                                when a quote conversion applies.
                              example: '50000.00'
                            quote_asset:
                              type: string
                              description: Quote asset the transfer amount is expressed in.
                              example: USD
                          required:
                            - version
                            - tx_id
                            - amount
                            - asset
                            - asset_class
                            - iiban
                            - type
                          title: request_transfer_to_spot
                          description: >-
                            Transfer assets from a vault to a linked Kraken spot
                            account.
                        - type: object
                          properties:
                            type:
                              type: string
                              enum:
                                - request_custody_transfer_to_spot
                            version:
                              type: integer
                              format: int32
                            execution:
                              type: object
                              properties:
                                state:
                                  type: string
                                started_at:
                                  type: string
                                  format: date-time
                                  description: >-
                                    RFC 3339 UTC timestamp when instruction
                                    execution started. Omitted when execution
                                    has not started.
                                  example: '2026-01-15T12:34:56Z'
                                completed_at:
                                  type: string
                                  format: date-time
                                  description: >-
                                    RFC 3339 UTC timestamp when instruction
                                    execution completed. Omitted when execution
                                    has not completed.
                                  example: '2026-01-15T12:35:56Z'
                                error:
                                  type: string
                              required:
                                - state
                            vault_id:
                              type: string
                            tx_id:
                              type: string
                            amount:
                              type: string
                            asset:
                              type: string
                            asset_class:
                              type: string
                            iiban:
                              type: string
                            fee_amount:
                              type: string
                              description: >-
                                Fee amount for the transfer, fixed-precision
                                decimal as string.
                              example: '0.00010000'
                            fee_asset:
                              type: string
                              description: Asset code the fee is charged in.
                              example: BTC
                            fee_asset_class:
                              type: string
                              description: >-
                                Asset class of the fee asset (e.g. `currency`,
                                `tokenized_asset`).
                              example: currency
                            fee_level:
                              type: string
                              description: >-
                                Fee tier selected for the transfer (e.g.
                                `normal`).
                              example: normal
                            fee_quote_id:
                              type: string
                              description: >-
                                Identifier of the fee quote the fee was derived
                                from, when a quote was used.
                              example: QABCDEF234567A
                            fee_quote_amount:
                              type: string
                              description: >-
                                Fee amount expressed in the quote asset, when a
                                quote conversion applies.
                              example: '5.00'
                            fee_quote_asset:
                              type: string
                              description: Quote asset the fee amount is expressed in.
                              example: USD
                            quote_amount:
                              type: string
                              description: >-
                                Transfer amount expressed in the quote asset,
                                when a quote conversion applies.
                              example: '50000.00'
                            quote_asset:
                              type: string
                              description: Quote asset the transfer amount is expressed in.
                              example: USD
                          required:
                            - version
                            - tx_id
                            - amount
                            - asset
                            - asset_class
                            - iiban
                            - type
                          title: request_custody_transfer_to_spot
                          description: >-
                            Transfer assets from custody to a linked Kraken spot
                            account.
                        - type: object
                          properties:
                            type:
                              type: string
                              enum:
                                - request_staking_deallocation
                            version:
                              type: integer
                              format: int32
                            execution:
                              type: object
                              properties:
                                state:
                                  type: string
                                started_at:
                                  type: string
                                  format: date-time
                                  description: >-
                                    RFC 3339 UTC timestamp when instruction
                                    execution started. Omitted when execution
                                    has not started.
                                  example: '2026-01-15T12:34:56Z'
                                completed_at:
                                  type: string
                                  format: date-time
                                  description: >-
                                    RFC 3339 UTC timestamp when instruction
                                    execution completed. Omitted when execution
                                    has not completed.
                                  example: '2026-01-15T12:35:56Z'
                                error:
                                  type: string
                              required:
                                - state
                            vault_id:
                              type: string
                            provider:
                              type: string
                            unbonding_period:
                              type: integer
                              format: int32
                            asset:
                              type: string
                            asset_class:
                              type: string
                            amount:
                              type: string
                            fee_amount:
                              type: string
                              description: >-
                                Fee amount for the deallocation, fixed-precision
                                decimal as string.
                              example: '0.00010000'
                            fee_asset:
                              type: string
                              description: Asset code the fee is charged in.
                              example: BTC
                            fee_asset_class:
                              type: string
                              description: >-
                                Asset class of the fee asset (e.g. `currency`,
                                `tokenized_asset`).
                              example: currency
                            fee_level:
                              type: string
                              description: >-
                                Fee tier selected for the deallocation (e.g.
                                `normal`).
                              example: normal
                            fee_quote_id:
                              type: string
                              description: >-
                                Identifier of the fee quote the fee was derived
                                from, when a quote was used.
                              example: QABCDEF234567A
                            fee_quote_amount:
                              type: string
                              description: >-
                                Fee amount expressed in the quote asset, when a
                                quote conversion applies.
                              example: '5.00'
                            fee_quote_asset:
                              type: string
                              description: Quote asset the fee amount is expressed in.
                              example: USD
                            quote_amount:
                              type: string
                              description: >-
                                Deallocation amount expressed in the quote
                                asset, when a quote conversion applies.
                              example: '50000.00'
                            quote_asset:
                              type: string
                              description: >-
                                Quote asset the deallocation amount is expressed
                                in.
                              example: USD
                          required:
                            - version
                            - provider
                            - asset
                            - asset_class
                            - amount
                            - type
                          title: request_staking_deallocation
                          description: Remove assets from staking back into a vault.
                        - type: object
                          properties:
                            type:
                              type: string
                              enum:
                                - request_pledge
                            version:
                              type: integer
                              format: int32
                            execution:
                              type: object
                              properties:
                                state:
                                  type: string
                                started_at:
                                  type: string
                                  format: date-time
                                  description: >-
                                    RFC 3339 UTC timestamp when instruction
                                    execution started. Omitted when execution
                                    has not started.
                                  example: '2026-01-15T12:34:56Z'
                                completed_at:
                                  type: string
                                  format: date-time
                                  description: >-
                                    RFC 3339 UTC timestamp when instruction
                                    execution completed. Omitted when execution
                                    has not completed.
                                  example: '2026-01-15T12:35:56Z'
                                error:
                                  type: string
                              required:
                                - state
                            vault_id:
                              type: string
                            amount:
                              type: string
                            asset:
                              type: string
                            asset_class:
                              type: string
                            user_id:
                              type: integer
                              format: int32
                            transaction_id:
                              type: string
                            quote_amount:
                              type: string
                            quote_asset:
                              type: string
                          required:
                            - version
                            - amount
                            - asset
                            - asset_class
                            - user_id
                            - transaction_id
                            - type
                          title: request_pledge
                          description: Pledge assets from a vault as collateral.
                        - type: object
                          properties:
                            type:
                              type: string
                              enum:
                                - request_pledge_release
                            version:
                              type: integer
                              format: int32
                            execution:
                              type: object
                              properties:
                                state:
                                  type: string
                                started_at:
                                  type: string
                                  format: date-time
                                  description: >-
                                    RFC 3339 UTC timestamp when instruction
                                    execution started. Omitted when execution
                                    has not started.
                                  example: '2026-01-15T12:34:56Z'
                                completed_at:
                                  type: string
                                  format: date-time
                                  description: >-
                                    RFC 3339 UTC timestamp when instruction
                                    execution completed. Omitted when execution
                                    has not completed.
                                  example: '2026-01-15T12:35:56Z'
                                error:
                                  type: string
                              required:
                                - state
                            vault_id:
                              type: string
                            amount:
                              type: string
                            asset:
                              type: string
                            asset_class:
                              type: string
                            user_id:
                              type: integer
                              format: int32
                            transaction_id:
                              type: string
                            quote_amount:
                              type: string
                            quote_asset:
                              type: string
                          required:
                            - version
                            - amount
                            - asset
                            - asset_class
                            - user_id
                            - transaction_id
                            - type
                          title: request_pledge_release
                          description: Release assets from an existing pledge.
                        - type: object
                          properties:
                            type:
                              type: string
                              enum:
                                - create_vault
                            version:
                              type: integer
                              format: int32
                            execution:
                              type: object
                              properties:
                                state:
                                  type: string
                                started_at:
                                  type: string
                                  format: date-time
                                  description: >-
                                    RFC 3339 UTC timestamp when instruction
                                    execution started. Omitted when execution
                                    has not started.
                                  example: '2026-01-15T12:34:56Z'
                                completed_at:
                                  type: string
                                  format: date-time
                                  description: >-
                                    RFC 3339 UTC timestamp when instruction
                                    execution completed. Omitted when execution
                                    has not completed.
                                  example: '2026-01-15T12:35:56Z'
                                error:
                                  type: string
                              required:
                                - state
                            name:
                              type: string
                            description:
                              type: string
                            policies:
                              type: array
                              items:
                                type: object
                                properties:
                                  type:
                                    type: string
                                  amount:
                                    type: string
                                  required:
                                    type: integer
                                    format: int32
                                  available:
                                    type: integer
                                    format: int32
                                  enable:
                                    type: boolean
                                required:
                                  - type
                            users:
                              type: array
                              items:
                                type: object
                                properties:
                                  iiban:
                                    type: string
                                  full_name:
                                    type: string
                                  email:
                                    type: string
                                  role:
                                    type: string
                                required:
                                  - iiban
                                  - role
                            withdrawal_addresses:
                              type: array
                              items:
                                type: object
                                properties:
                                  asset:
                                    type: string
                                  asset_class:
                                    type: string
                                  address_name:
                                    type: string
                                  method:
                                    type: string
                                  info:
                                    type: object
                                    properties:
                                      address:
                                        type: string
                                      tag:
                                        type: string
                                      beneficiary:
                                        type: object
                                        properties:
                                          recipient:
                                            type: string
                                          type:
                                            type: string
                                          name:
                                            type: string
                                          last_name:
                                            type: string
                                          country:
                                            type: string
                                          province:
                                            type: string
                                          address_1:
                                            type: string
                                          address_2:
                                            type: string
                                          city:
                                            type: string
                                          postal_code:
                                            type: string
                                          vasp_name:
                                            type: string
                                  description:
                                    type: string
                                  reason:
                                    type: string
                                required:
                                  - asset
                                  - address_name
                                  - method
                                  - info
                          required:
                            - version
                            - name
                            - policies
                            - users
                            - withdrawal_addresses
                            - type
                          title: create_vault
                          description: Create a new vault.
                        - type: object
                          properties:
                            type:
                              type: string
                              enum:
                                - update_vault
                            version:
                              type: integer
                              format: int32
                            execution:
                              type: object
                              properties:
                                state:
                                  type: string
                                started_at:
                                  type: string
                                  format: date-time
                                  description: >-
                                    RFC 3339 UTC timestamp when instruction
                                    execution started. Omitted when execution
                                    has not started.
                                  example: '2026-01-15T12:34:56Z'
                                completed_at:
                                  type: string
                                  format: date-time
                                  description: >-
                                    RFC 3339 UTC timestamp when instruction
                                    execution completed. Omitted when execution
                                    has not completed.
                                  example: '2026-01-15T12:35:56Z'
                                error:
                                  type: string
                              required:
                                - state
                            vault_id:
                              type: string
                            name:
                              type: string
                            description:
                              type: string
                            org_iiban:
                              type: string
                          required:
                            - version
                            - type
                          title: update_vault
                          description: Change the settings of an existing vault.
                        - type: object
                          properties:
                            type:
                              type: string
                              enum:
                                - update_domain_policy
                            version:
                              type: integer
                              format: int32
                            execution:
                              type: object
                              properties:
                                state:
                                  type: string
                                started_at:
                                  type: string
                                  format: date-time
                                  description: >-
                                    RFC 3339 UTC timestamp when instruction
                                    execution started. Omitted when execution
                                    has not started.
                                  example: '2026-01-15T12:34:56Z'
                                completed_at:
                                  type: string
                                  format: date-time
                                  description: >-
                                    RFC 3339 UTC timestamp when instruction
                                    execution completed. Omitted when execution
                                    has not completed.
                                  example: '2026-01-15T12:35:56Z'
                                error:
                                  type: string
                              required:
                                - state
                            policy:
                              type: object
                              properties:
                                type:
                                  type: string
                                required:
                                  type: integer
                                  format: int32
                                available:
                                  type: integer
                                  format: int32
                              required:
                                - type
                          required:
                            - version
                            - policy
                            - type
                          title: update_domain_policy
                          description: Change the organization-wide domain policy.
                        - type: object
                          properties:
                            type:
                              type: string
                              enum:
                                - update_user_status
                            version:
                              type: integer
                              format: int32
                            execution:
                              type: object
                              properties:
                                state:
                                  type: string
                                started_at:
                                  type: string
                                  format: date-time
                                  description: >-
                                    RFC 3339 UTC timestamp when instruction
                                    execution started. Omitted when execution
                                    has not started.
                                  example: '2026-01-15T12:34:56Z'
                                completed_at:
                                  type: string
                                  format: date-time
                                  description: >-
                                    RFC 3339 UTC timestamp when instruction
                                    execution completed. Omitted when execution
                                    has not completed.
                                  example: '2026-01-15T12:35:56Z'
                                error:
                                  type: string
                              required:
                                - state
                            operation_type:
                              type: string
                              enum:
                                - add
                                - remove
                            user:
                              type: object
                              properties:
                                iiban:
                                  type: string
                                full_name:
                                  type: string
                                email:
                                  type: string
                                role:
                                  type: string
                              required:
                                - iiban
                                - role
                            reason:
                              type: string
                            org_iiban:
                              type: string
                          required:
                            - version
                            - operation_type
                            - user
                            - type
                          title: update_user_status
                          description: >-
                            Change a user's status, such as activating or
                            deactivating them.
                        - type: object
                          properties:
                            type:
                              type: string
                              enum:
                                - create_api_user
                            version:
                              type: integer
                              format: int32
                            execution:
                              type: object
                              properties:
                                state:
                                  type: string
                                started_at:
                                  type: string
                                  format: date-time
                                  description: >-
                                    RFC 3339 UTC timestamp when instruction
                                    execution started. Omitted when execution
                                    has not started.
                                  example: '2026-01-15T12:34:56Z'
                                completed_at:
                                  type: string
                                  format: date-time
                                  description: >-
                                    RFC 3339 UTC timestamp when instruction
                                    execution completed. Omitted when execution
                                    has not completed.
                                  example: '2026-01-15T12:35:56Z'
                                error:
                                  type: string
                              required:
                                - state
                            operation_type:
                              type: string
                              enum:
                                - add
                            attributes:
                              type: array
                              items:
                                type: string
                            role:
                              type: string
                            name:
                              type: string
                            ip_allowlist:
                              type: array
                              items:
                                type: string
                            valid_until:
                              type: string
                            vaults:
                              type: array
                              items:
                                type: string
                            org_iiban:
                              type: string
                          required:
                            - version
                            - operation_type
                            - attributes
                            - role
                            - name
                            - ip_allowlist
                            - vaults
                            - type
                          title: create_api_user
                          description: Create a programmatic API user.
                        - type: object
                          properties:
                            type:
                              type: string
                              enum:
                                - update_api_user
                            version:
                              type: integer
                              format: int32
                            execution:
                              type: object
                              properties:
                                state:
                                  type: string
                                started_at:
                                  type: string
                                  format: date-time
                                  description: >-
                                    RFC 3339 UTC timestamp when instruction
                                    execution started. Omitted when execution
                                    has not started.
                                  example: '2026-01-15T12:34:56Z'
                                completed_at:
                                  type: string
                                  format: date-time
                                  description: >-
                                    RFC 3339 UTC timestamp when instruction
                                    execution completed. Omitted when execution
                                    has not completed.
                                  example: '2026-01-15T12:35:56Z'
                                error:
                                  type: string
                              required:
                                - state
                            operation_type:
                              type: string
                              enum:
                                - update_user
                                - update_role
                                - assign_attribute
                                - revoke_attribute
                                - add_vault
                                - remove_vault
                            ip_allowlist:
                              type: array
                              items:
                                type: string
                            valid_until:
                              type: string
                            user:
                              type: object
                              properties:
                                iiban:
                                  type: string
                                full_name:
                                  type: string
                                email:
                                  type: string
                                role:
                                  type: string
                              required:
                                - iiban
                                - role
                            reason:
                              type: string
                            role:
                              type: string
                            attribute:
                              type: string
                            vault:
                              type: object
                              properties:
                                id:
                                  type: string
                                iiban:
                                  type: string
                                name:
                                  type: string
                              required:
                                - id
                            org_iiban:
                              type: string
                          required:
                            - version
                            - operation_type
                            - ip_allowlist
                            - user
                            - type
                          title: update_api_user
                          description: Update an existing programmatic API user.
                      description: >-
                        A single atomic instruction. The type field selects the
                        variant and identifies the instruction type.
                    description: >-
                      List of atomic instructions that make up the task. Each
                      entry describes a single change; batch changes are
                      expanded into one entry per change.
                    required:
                      - id
                      - type
                      - state
                      - created_at
                      - updated_at
                      - expires_at
                      - initiator
                      - quorum_type
                      - can_review
                      - current_user_decision
                      - reviewer_statistics_label
                      - instructions
                required:
                  - id
                  - created_at
                  - type
                  - state
                  - task
        '400':
          description: >-
            Bad Request. The request failed validation. Examples: unknown filter
            value, malformed ID, or invalid date range.
          content:
            application/problem+json:
              schema:
                description: >-
                  Error responses follow `Problem Details for HTTP APIs`
                  ([rfc7807]).


                  [rfc7807]: https://datatracker.ietf.org/doc/html/rfc7807
                type: object
                properties:
                  type:
                    description: >-
                      URL uniquely identifying the error type relative to an
                      operation
                    type: string
                    enum:
                      - tag:kraken.com,2025:BadRequest
                    example: tag:kraken.com,2025:BadRequest
                  status:
                    description: HTTP status (provided for convenience)
                    type: integer
                    format: uint16
                    minimum: 0
                    example: 400
                  title:
                    description: Short human-readable summary
                    type: string
                    example: Bad Request
                  detail:
                    nullable: true
                    description: Help to solve the problem
                    type: string
                    example: Request failed validation.
                  instance:
                    nullable: true
                    description: Link to debug data for this particular error
                    type: string
                    example: https://debug.kraken.com/req/01HXYZABCDEF
                  data:
                    type: object
                    properties:
                      message:
                        type: string
                        example: Request failed validation.
                    required:
                      - message
                required:
                  - data
                  - status
                  - title
                  - type
        '403':
          description: >-
            Forbidden. The activity is unknown, out of scope, or the caller
            lacks access. Malformed activity identifiers also return this
            status.
          content:
            application/problem+json:
              schema:
                description: >-
                  Error responses follow `Problem Details for HTTP APIs`
                  ([rfc7807]).


                  [rfc7807]: https://datatracker.ietf.org/doc/html/rfc7807
                type: object
                properties:
                  type:
                    description: >-
                      URL uniquely identifying the error type relative to an
                      operation
                    type: string
                    enum:
                      - tag:kraken.com,2025:PermissionDenied
                    example: tag:kraken.com,2025:PermissionDenied
                  status:
                    description: HTTP status (provided for convenience)
                    type: integer
                    format: uint16
                    minimum: 0
                    example: 403
                  title:
                    description: Short human-readable summary
                    type: string
                    example: Forbidden
                  detail:
                    nullable: true
                    description: Help to solve the problem
                    type: string
                    example: Caller lacks access to the requested resource.
                  instance:
                    nullable: true
                    description: Link to debug data for this particular error
                    type: string
                    example: https://debug.kraken.com/req/01HXYZABCDEF
                  data:
                    type: object
                    properties:
                      message:
                        type: string
                        example: Caller lacks access to the requested resource.
                    required:
                      - message
                required:
                  - data
                  - status
                  - title
                  - type
        '500':
          description: >-
            Internal Server Error. An unhandled exception occurred while serving
            the request.
          content:
            application/problem+json:
              schema:
                oneOf:
                  - description: >-
                      Error responses follow `Problem Details for HTTP APIs`
                      ([rfc7807]).


                      [rfc7807]: https://datatracker.ietf.org/doc/html/rfc7807
                    type: object
                    properties:
                      type:
                        description: >-
                          URL uniquely identifying the error type relative to an
                          operation
                        type: string
                        enum:
                          - tag:kraken.com,2025:gateway/ReadUpstream
                        example: tag:kraken.com,2025:gateway/ReadUpstream
                      status:
                        description: HTTP status (provided for convenience)
                        type: integer
                        format: uint16
                        minimum: 0
                        example: 500
                      title:
                        description: Short human-readable summary
                        type: string
                        example: Internal Server Error
                      detail:
                        nullable: true
                        description: Help to solve the problem
                        type: string
                        example: Failed to read response from upstream custody service.
                      instance:
                        nullable: true
                        description: Link to debug data for this particular error
                        type: string
                        example: https://debug.kraken.com/req/01HXYZABCDEF
                      data:
                        description: Custom data attached to this problem
                    required:
                      - data
                      - status
                      - title
                      - type
                  - description: >-
                      Error responses follow `Problem Details for HTTP APIs`
                      ([rfc7807]).


                      [rfc7807]: https://datatracker.ietf.org/doc/html/rfc7807
                    type: object
                    properties:
                      type:
                        description: >-
                          URL uniquely identifying the error type relative to an
                          operation
                        type: string
                        enum:
                          - tag:kraken.com,2025:gateway/ReadUpstream
                        example: tag:kraken.com,2025:gateway/ReadUpstream
                      status:
                        description: HTTP status (provided for convenience)
                        type: integer
                        format: uint16
                        minimum: 0
                        example: 500
                      title:
                        description: Short human-readable summary
                        type: string
                        example: Internal Server Error
                      detail:
                        nullable: true
                        description: Help to solve the problem
                        type: string
                        example: Failed to read response from upstream custody service.
                      instance:
                        nullable: true
                        description: Link to debug data for this particular error
                        type: string
                        example: https://debug.kraken.com/req/01HXYZABCDEF
                      data:
                        description: Custom data attached to this problem
                    required:
                      - data
                      - status
                      - title
                      - type
                  - description: >-
                      Error responses follow `Problem Details for HTTP APIs`
                      ([rfc7807]).


                      [rfc7807]: https://datatracker.ietf.org/doc/html/rfc7807
                    type: object
                    properties:
                      type:
                        description: >-
                          URL uniquely identifying the error type relative to an
                          operation
                        type: string
                        enum:
                          - tag:kraken.com,2025:gateway/ReadUpstream
                        example: tag:kraken.com,2025:gateway/ReadUpstream
                      status:
                        description: HTTP status (provided for convenience)
                        type: integer
                        format: uint16
                        minimum: 0
                        example: 500
                      title:
                        description: Short human-readable summary
                        type: string
                        example: Internal Server Error
                      detail:
                        nullable: true
                        description: Help to solve the problem
                        type: string
                        example: Failed to read response from upstream custody service.
                      instance:
                        nullable: true
                        description: Link to debug data for this particular error
                        type: string
                        example: https://debug.kraken.com/req/01HXYZABCDEF
                      data:
                        description: Custom data attached to this problem
                    required:
                      - data
                      - status
                      - title
                      - type
                  - description: >-
                      Error responses follow `Problem Details for HTTP APIs`
                      ([rfc7807]).


                      [rfc7807]: https://datatracker.ietf.org/doc/html/rfc7807
                    type: object
                    properties:
                      type:
                        description: >-
                          URL uniquely identifying the error type relative to an
                          operation
                        type: string
                        enum:
                          - tag:kraken.com,2025:gateway/WriteResponse
                        example: tag:kraken.com,2025:gateway/WriteResponse
                      status:
                        description: HTTP status (provided for convenience)
                        type: integer
                        format: uint16
                        minimum: 0
                        example: 500
                      title:
                        description: Short human-readable summary
                        type: string
                        example: Internal Server Error
                      detail:
                        nullable: true
                        description: Help to solve the problem
                        type: string
                        example: Failed to write response to upstream custody service.
                      instance:
                        nullable: true
                        description: Link to debug data for this particular error
                        type: string
                        example: https://debug.kraken.com/req/01HXYZABCDEF
                      data:
                        description: Custom data attached to this problem
                    required:
                      - data
                      - status
                      - title
                      - type
                  - description: >-
                      Error responses follow `Problem Details for HTTP APIs`
                      ([rfc7807]).


                      [rfc7807]: https://datatracker.ietf.org/doc/html/rfc7807
                    type: object
                    properties:
                      type:
                        description: >-
                          URL uniquely identifying the error type relative to an
                          operation
                        type: string
                        enum:
                          - tag:kraken.com,2025:gateway/Connect
                        example: tag:kraken.com,2025:gateway/Connect
                      status:
                        description: HTTP status (provided for convenience)
                        type: integer
                        format: uint16
                        minimum: 0
                        example: 500
                      title:
                        description: Short human-readable summary
                        type: string
                        example: Internal Server Error
                      detail:
                        nullable: true
                        description: Help to solve the problem
                        type: string
                        example: Failed to connect to upstream custody service.
                      instance:
                        nullable: true
                        description: Link to debug data for this particular error
                        type: string
                        example: https://debug.kraken.com/req/01HXYZABCDEF
                      data:
                        description: Custom data attached to this problem
                    required:
                      - data
                      - status
                      - title
                      - type
                  - description: >-
                      Error responses follow `Problem Details for HTTP APIs`
                      ([rfc7807]).


                      [rfc7807]: https://datatracker.ietf.org/doc/html/rfc7807
                    type: object
                    properties:
                      type:
                        description: >-
                          URL uniquely identifying the error type relative to an
                          operation
                        type: string
                        enum:
                          - tag:kraken.com,2025:gateway/ReadUpstream
                        example: tag:kraken.com,2025:gateway/ReadUpstream
                      status:
                        description: HTTP status (provided for convenience)
                        type: integer
                        format: uint16
                        minimum: 0
                        example: 500
                      title:
                        description: Short human-readable summary
                        type: string
                        example: Internal Server Error
                      detail:
                        nullable: true
                        description: Help to solve the problem
                        type: string
                        example: Failed to read response from upstream custody service.
                      instance:
                        nullable: true
                        description: Link to debug data for this particular error
                        type: string
                        example: https://debug.kraken.com/req/01HXYZABCDEF
                      data:
                        description: Custom data attached to this problem
                    required:
                      - data
                      - status
                      - title
                      - type
                  - description: >-
                      Error responses follow `Problem Details for HTTP APIs`
                      ([rfc7807]).


                      [rfc7807]: https://datatracker.ietf.org/doc/html/rfc7807
                    type: object
                    properties:
                      type:
                        description: >-
                          URL uniquely identifying the error type relative to an
                          operation
                        type: string
                        enum:
                          - tag:kraken.com,2025:gateway/ReadUpstream
                        example: tag:kraken.com,2025:gateway/ReadUpstream
                      status:
                        description: HTTP status (provided for convenience)
                        type: integer
                        format: uint16
                        minimum: 0
                        example: 500
                      title:
                        description: Short human-readable summary
                        type: string
                        example: Internal Server Error
                      detail:
                        nullable: true
                        description: Help to solve the problem
                        type: string
                        example: Failed to read response from upstream custody service.
                      instance:
                        nullable: true
                        description: Link to debug data for this particular error
                        type: string
                        example: https://debug.kraken.com/req/01HXYZABCDEF
                      data:
                        description: Custom data attached to this problem
                    required:
                      - data
                      - status
                      - title
                      - type
                  - description: >-
                      Error responses follow `Problem Details for HTTP APIs`
                      ([rfc7807]).


                      [rfc7807]: https://datatracker.ietf.org/doc/html/rfc7807
                    type: object
                    properties:
                      type:
                        description: >-
                          URL uniquely identifying the error type relative to an
                          operation
                        type: string
                        enum:
                          - tag:kraken.com,2025:gateway/ReadUpstream
                        example: tag:kraken.com,2025:gateway/ReadUpstream
                      status:
                        description: HTTP status (provided for convenience)
                        type: integer
                        format: uint16
                        minimum: 0
                        example: 500
                      title:
                        description: Short human-readable summary
                        type: string
                        example: Internal Server Error
                      detail:
                        nullable: true
                        description: Help to solve the problem
                        type: string
                        example: Failed to read response from upstream custody service.
                      instance:
                        nullable: true
                        description: Link to debug data for this particular error
                        type: string
                        example: https://debug.kraken.com/req/01HXYZABCDEF
                      data:
                        description: Custom data attached to this problem
                    required:
                      - data
                      - status
                      - title
                      - type
                  - description: >-
                      Error responses follow `Problem Details for HTTP APIs`
                      ([rfc7807]).


                      [rfc7807]: https://datatracker.ietf.org/doc/html/rfc7807
                    type: object
                    properties:
                      type:
                        description: >-
                          URL uniquely identifying the error type relative to an
                          operation
                        type: string
                        enum:
                          - tag:kraken.com,2025:gateway/WriteResponse
                        example: tag:kraken.com,2025:gateway/WriteResponse
                      status:
                        description: HTTP status (provided for convenience)
                        type: integer
                        format: uint16
                        minimum: 0
                        example: 500
                      title:
                        description: Short human-readable summary
                        type: string
                        example: Internal Server Error
                      detail:
                        nullable: true
                        description: Help to solve the problem
                        type: string
                        example: Failed to write response to upstream custody service.
                      instance:
                        nullable: true
                        description: Link to debug data for this particular error
                        type: string
                        example: https://debug.kraken.com/req/01HXYZABCDEF
                      data:
                        description: Custom data attached to this problem
                    required:
                      - data
                      - status
                      - title
                      - type
                  - description: >-
                      Error responses follow `Problem Details for HTTP APIs`
                      ([rfc7807]).


                      [rfc7807]: https://datatracker.ietf.org/doc/html/rfc7807
                    type: object
                    properties:
                      type:
                        description: >-
                          URL uniquely identifying the error type relative to an
                          operation
                        type: string
                        enum:
                          - tag:kraken.com,2025:gateway/Fatal
                        example: tag:kraken.com,2025:gateway/Fatal
                      status:
                        description: HTTP status (provided for convenience)
                        type: integer
                        format: uint16
                        minimum: 0
                        example: 500
                      title:
                        description: Short human-readable summary
                        type: string
                        example: Internal Server Error
                      detail:
                        nullable: true
                        description: Help to solve the problem
                        type: string
                        example: >-
                          A fatal gateway error occurred while serving the
                          request.
                      instance:
                        nullable: true
                        description: Link to debug data for this particular error
                        type: string
                        example: https://debug.kraken.com/req/01HXYZABCDEF
                      data:
                        description: Custom data attached to this problem
                    required:
                      - data
                      - status
                      - title
                      - type
                  - description: >-
                      Error responses follow `Problem Details for HTTP APIs`
                      ([rfc7807]).


                      [rfc7807]: https://datatracker.ietf.org/doc/html/rfc7807
                    type: object
                    properties:
                      type:
                        description: >-
                          URL uniquely identifying the error type relative to an
                          operation
                        type: string
                        enum:
                          - tag:kraken.com,2025:Unknown
                        example: tag:kraken.com,2025:Unknown
                      status:
                        description: HTTP status (provided for convenience)
                        type: integer
                        format: uint16
                        minimum: 0
                        example: 500
                      title:
                        description: Short human-readable summary
                        type: string
                        example: Internal Server Error
                      detail:
                        nullable: true
                        description: Help to solve the problem
                        type: string
                        example: >-
                          An unexpected error occurred while serving the
                          request.
                      instance:
                        nullable: true
                        description: Link to debug data for this particular error
                        type: string
                        example: https://debug.kraken.com/req/01HXYZABCDEF
                      data:
                        type: object
                        properties:
                          message:
                            type: string
                            description: >-
                              Human-readable description of the underlying
                              failure.
                            example: Unhandled exception while servicing the request.
                          core_error:
                            type: string
                            description: Identifier for the originating error.
                            example: InternalError
                        required:
                          - message
                          - core_error
                        description: >-
                          Error-specific payload returned for an unhandled
                          exception.
                    required:
                      - data
                      - status
                      - title
                      - type
        '503':
          description: >-
            Service Unavailable. The upstream custody service could not be
            reached.
          content:
            application/problem+json:
              schema:
                description: >-
                  Error responses follow `Problem Details for HTTP APIs`
                  ([rfc7807]).


                  [rfc7807]: https://datatracker.ietf.org/doc/html/rfc7807
                type: object
                properties:
                  type:
                    description: >-
                      URL uniquely identifying the error type relative to an
                      operation
                    type: string
                    enum:
                      - tag:kraken.com,2025:gateway/Connect
                    example: tag:kraken.com,2025:gateway/Connect
                  status:
                    description: HTTP status (provided for convenience)
                    type: integer
                    format: uint16
                    minimum: 0
                    example: 503
                  title:
                    description: Short human-readable summary
                    type: string
                    example: Service Unavailable
                  detail:
                    nullable: true
                    description: Help to solve the problem
                    type: string
                    example: Downstream custody service is temporarily unreachable.
                  instance:
                    nullable: true
                    description: Link to debug data for this particular error
                    type: string
                    example: https://debug.kraken.com/req/01HXYZABCDEF
                  data:
                    description: Custom data attached to this problem
                required:
                  - data
                  - status
                  - title
                  - type
      security:
        - API Key Auth (key): []
          API Key Auth (signature): []
          API Key Auth (nonce): []
components:
  securitySchemes:
    API Key Auth (key):
      type: apiKey
      in: header
      name: api-key
    API Key Auth (signature):
      type: apiKey
      in: header
      name: api-sign
    API Key Auth (nonce):
      type: apiKey
      in: header
      name: api-nonce

````
