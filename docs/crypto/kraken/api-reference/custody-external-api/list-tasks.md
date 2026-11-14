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
source_url: 'https://docs.kraken.com/api-reference/custody-external-api/list-tasks'
updated_at: 2026-11-13
---

# List tasks

> Returns a paginated list of custody tasks (approval requests) visible to the authenticated user, filtered by the supplied query parameters and ordered by the requested column. Multi-valued filters are OR-ed within a field and AND-ed across fields. The public task identifier is `id`, the approval UUID. Task objects do not return `task_id` or `approval_id`. T-prefixed identifiers are not accepted or returned.

**Rate limit:** 200 requests per 30 seconds per IP.



## OpenAPI

````yaml /openapi/insto-custody-rest.yaml get /v0/insto/custody/tasks
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
  /v0/insto/custody/tasks:
    get:
      tags:
        - Custody External API
      summary: List tasks
      description: >-
        Returns a paginated list of custody tasks (approval requests) visible to
        the authenticated user, filtered by the supplied query parameters and
        ordered by the requested column. Multi-valued filters are OR-ed within a
        field and AND-ed across fields. The public task identifier is `id`, the
        approval UUID. Task objects do not return `task_id` or `approval_id`.
        T-prefixed identifiers are not accepted or returned.


        **Rate limit:** 200 requests per 30 seconds per IP.
      operationId: getV0InstoCustodyTasks
      parameters:
        - in: query
          name: org_iiban
          description: >-
            Restrict the result set to tasks owned by the specified
            organization, identified by its 16-char IIBAN. Defaults to the
            caller's organization when omitted.
          schema:
            type: string
            example: ABCD EFGH IJKL MNOP
          style: form
        - in: query
          name: limit
          description: >-
            Maximum number of tasks to return in the page. Defaults to 100 when
            omitted.
          schema:
            type: integer
            format: int32
            example: 100
          style: form
        - in: query
          name: offset
          description: >-
            Number of tasks to skip before the page begins, used together with
            `limit` for offset-based pagination. Defaults to 0 when omitted.
          schema:
            type: integer
            format: int32
            example: 0
          style: form
        - in: query
          name: state
          description: >-
            Restrict the result set to tasks in one or more lifecycle states.
            Allowed values: `pending`, `approved`, `rejected`, `denied` (alias
            of `rejected`), `canceled`, `expired`, `failed`, `executed`.
          schema:
            type: array
            items:
              type: string
              example: pending
          style: form
        - in: query
          name: current_user_decision
          description: >-
            Restrict the result set to tasks for which the caller has made the
            specified decision. One of `undecided`, `approved`, `denied`.
          schema:
            type: string
            example: undecided
          style: form
        - in: query
          name: id
          description: >-
            Restrict the result set to the supplied task ids. Each value is an
            approval UUID (UUID v4). T-prefixed identifiers are not accepted.
            Matching is case-insensitive.
          schema:
            type: array
            items:
              type: string
              example: 550e8400-e29b-41d4-a716-446655440000
          style: form
        - in: query
          name: vault_id
          description: >-
            Restrict the result set to tasks scoped to the supplied vault IDs.
            Each value is a `V`-prefixed 14-char base32 identifier with a final
            check character.
          schema:
            type: array
            items:
              type: string
              example: VABCDEF234567A
          style: form
        - in: query
          name: action
          description: >-
            Restrict the result set to tasks that contain one of the supplied
            action types. Accepts only the singular action names listed below
            (for example `request_withdrawal`, `create_vault`,
            `update_subquorum`). Multiple values are OR-ed.
          schema:
            type: array
            items:
              type: string
              example: request_withdrawal
              enum:
                - update_subquorum
                - update_vault_user
                - update_vault_policy
                - request_withdrawal
                - remove_org_user
                - create_user
                - request_staking_allocation
                - update_withdrawal_address
                - update_user_permission
                - create_vault
                - update_vault
                - update_domain_policy
                - update_user_status
                - request_transfer_to_spot
                - create_api_user
                - update_api_user
                - request_staking_deallocation
                - request_custody_transfer_to_spot
                - request_pledge
                - request_pledge_release
          style: form
        - in: query
          name: created_at_from
          description: >-
            Include only tasks created at or after this RFC 3339 UTC timestamp
            (inclusive), e.g. 2026-01-15T12:34:56Z; the Z (UTC) offset is
            required.
          schema:
            $ref: '#/components/schemas/google.protobuf.Timestamp'
          example: '2026-01-15T12:34:56Z'
          style: form
        - in: query
          name: created_at_to
          description: >-
            Include only tasks created at or before this RFC 3339 UTC timestamp
            (inclusive), e.g. 2026-01-15T12:34:56Z; the Z (UTC) offset is
            required.
          schema:
            $ref: '#/components/schemas/google.protobuf.Timestamp'
          example: '2026-01-15T12:34:56Z'
          style: form
        - in: query
          name: updated_at_from
          description: >-
            Include only tasks last updated at or after this RFC 3339 UTC
            timestamp (inclusive), e.g. 2026-01-15T12:34:56Z; the Z (UTC) offset
            is required.
          schema:
            $ref: '#/components/schemas/google.protobuf.Timestamp'
          example: '2026-01-15T12:34:56Z'
          style: form
        - in: query
          name: updated_at_to
          description: >-
            Include only tasks last updated at or before this RFC 3339 UTC
            timestamp (inclusive), e.g. 2026-01-15T12:34:56Z; the Z (UTC) offset
            is required.
          schema:
            $ref: '#/components/schemas/google.protobuf.Timestamp'
          example: '2026-01-15T12:34:56Z'
          style: form
        - in: query
          name: expires_at_from
          description: >-
            Include only tasks expiring at or after this RFC 3339 UTC timestamp
            (inclusive), e.g. 2026-01-15T12:34:56Z; the Z (UTC) offset is
            required.
          schema:
            $ref: '#/components/schemas/google.protobuf.Timestamp'
          example: '2026-01-15T12:34:56Z'
          style: form
        - in: query
          name: expires_at_to
          description: >-
            Include only tasks expiring at or before this RFC 3339 UTC timestamp
            (inclusive), e.g. 2026-01-15T12:34:56Z; the Z (UTC) offset is
            required.
          schema:
            $ref: '#/components/schemas/google.protobuf.Timestamp'
          example: '2026-01-15T12:34:56Z'
          style: form
        - in: query
          name: sort
          description: >-
            Ordering as a single `field:direction` token (direction optional,
            defaults to `desc`). Only one column is supported. Allowed fields:
            `id`, `state`, `vault_id`, `created_at`, `updated_at`, `expires_at`.
            Defaults to `created_at:desc`.
          schema:
            type: string
            example: created_at:desc
          style: form
      responses:
        '200':
          description: Page of task summaries matching the requested filters.
          content:
            application/json:
              schema:
                type: object
                properties:
                  result:
                    description: >-
                      Page of task summaries matching the requested filters,
                      ordered by the requested column.
                    type: array
                    items:
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
                            Coarse task-level discriminator. Every task is
                            exposed in the instruction-normalized model, so this
                            is always `normalized_task`. Use `instruction_types`
                            for the specific actions the task performs.
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
                          description: >-
                            RFC 3339 UTC timestamp when the task was last
                            updated.
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
                                Display name of the initiator at the time the
                                task was created.
                              type: string
                              example: Jane Doe
                            role:
                              description: >-
                                Role assigned to the initiator at the time the
                                task was created.
                              type: string
                              example: admin
                            ip_address:
                              description: >-
                                Source IP address recorded when the task was
                                initiated.
                              type: string
                              example: 203.0.113.42
                            iiban:
                              description: >-
                                16-char IIBAN identifying the initiating user or
                                API key.
                              type: string
                              example: ABCD EFGH IJKL MNOP
                        quorum_type:
                          description: >-
                            Scope of the quorum required to advance the task.
                            `domain` for org-wide quorum, `vault` for
                            vault-scoped quorum.
                          type: string
                          example: vault
                        can_review:
                          description: >-
                            True if the caller may still cast a review decision
                            on this task.
                          type: boolean
                          example: true
                        reviewer_statistics:
                          description: >-
                            Quorum counters for single-quorum tasks: how many
                            assigned reviewers have approved, denied, or not yet
                            decided, and how many approvals the task still
                            needs. Omitted for multi-quorum tasks. Use
                            `subquorum_approvals` when
                            `reviewer_statistics_label` is `multiquorum`. For
                            the individual reviewers behind these counters, read
                            `activities`.
                          type: object
                          properties:
                            current_count:
                              description: >-
                                Total number of reviewers currently assigned to
                                the task.
                              type: integer
                              format: int32
                              example: 3
                            approved:
                              description: Number of reviewers who have approved.
                              type: integer
                              format: int32
                              example: 1
                            denied:
                              description: Number of reviewers who have denied.
                              type: integer
                              format: int32
                              example: 0
                            undecided:
                              description: >-
                                Number of assigned reviewers who have not yet
                                cast a decision.
                              type: integer
                              format: int32
                              example: 2
                            required_quorum:
                              description: >-
                                Number of approving reviewers required for the
                                task to advance.
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
                            Vault the task is scoped to. Omitted for
                            domain-level tasks that do not target a specific
                            vault.
                          type: object
                          properties:
                            id:
                              description: >-
                                Vault identifier, a `V`-prefixed 14-char base32
                                string with a final check character.
                              type: string
                              example: VABCDEF234567A
                            name:
                              description: Display name of the vault.
                              type: string
                              example: Treasury Vault
                            status:
                              description: >-
                                Current vault lifecycle status (lowercase, e.g.
                                `active`, `archived`).
                              type: string
                              example: active
                            subquorum_config:
                              description: >-
                                Vault's current subquorum policy, the group
                                structure used to compute approvals on
                                multi-quorum tasks.
                              type: object
                              properties:
                                groups:
                                  description: >-
                                    Subquorum groups defined on the vault. A
                                    multi-quorum task advances when each group's
                                    `required` count of approvals is met.
                                  type: array
                                  items:
                                    type: object
                                    properties:
                                      id:
                                        description: Subquorum group identifier (UUID v4).
                                        type: string
                                        example: 11111111-2222-4333-8444-555555555555
                                      required:
                                        description: >-
                                          Number of group members whose approval
                                          is needed to satisfy this group's
                                          quorum.
                                        type: integer
                                        format: int32
                                        example: 2
                                      members:
                                        description: Members of the subquorum group.
                                        type: array
                                        items:
                                          type: object
                                          properties:
                                            iiban:
                                              description: 16-char IIBAN of the group member.
                                              type: string
                                              example: ABCD EFGH IJKL MNOP
                                            full_name:
                                              description: >-
                                                Display name of the member, when
                                                resolvable at read time.
                                              type: string
                                              example: Jane Doe
                                            email:
                                              description: >-
                                                Email address of the member, when
                                                resolvable at read time.
                                              type: string
                                              example: jane.doe@example.com
                                            role:
                                              description: >-
                                                Role of the member at read time
                                                (lowercase).
                                              type: string
                                              example: admin
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
                            `standard` means use `reviewer_statistics`;
                            `multiquorum` means use `subquorum_approvals`.
                          type: string
                          example: standard
                        instruction_types:
                          description: >-
                            The set of action types bundled into the task. These
                            are the same singular action names accepted by the
                            `action` query filter, so a value here can be passed
                            straight back as a filter.
                          type: array
                          items:
                            type: string
                            enum:
                              - update_subquorum
                              - update_vault_user
                              - update_vault_policy
                              - request_withdrawal
                              - remove_org_user
                              - create_user
                              - request_staking_allocation
                              - update_withdrawal_address
                              - update_user_permission
                              - create_vault
                              - update_vault
                              - update_domain_policy
                              - update_user_status
                              - request_transfer_to_spot
                              - create_api_user
                              - update_api_user
                              - request_staking_deallocation
                              - request_custody_transfer_to_spot
                              - request_pledge
                              - request_pledge_release
                            description: Action type of one instruction in the task.
                            example: request_withdrawal
                        subquorum_snapshot:
                          description: >-
                            Subquorum policy snapshot taken when the task was
                            created. Approvals are evaluated against this
                            snapshot so a later policy change cannot
                            retroactively invalidate decisions already cast.
                          type: object
                          properties:
                            groups:
                              description: Subquorum groups captured in the snapshot.
                              type: array
                              items:
                                type: object
                                properties:
                                  id:
                                    description: Subquorum group identifier (UUID v4).
                                    type: string
                                    example: 11111111-2222-4333-8444-555555555555
                                  required:
                                    description: >-
                                      Number of group members whose approval is
                                      needed to satisfy this group's quorum.
                                    type: integer
                                    format: int32
                                    example: 2
                                  members:
                                    description: >-
                                      Members of the subquorum group as captured
                                      at task-creation time.
                                    type: array
                                    items:
                                      type: object
                                      properties:
                                        iiban:
                                          description: 16-char IIBAN of the group member.
                                          type: string
                                          example: ABCD EFGH IJKL MNOP
                                        full_name:
                                          description: >-
                                            Display name of the member, when
                                            resolvable at read time.
                                          type: string
                                          example: Jane Doe
                                        email:
                                          description: >-
                                            Email address of the member, when
                                            resolvable at read time.
                                          type: string
                                          example: jane.doe@example.com
                                        role:
                                          description: >-
                                            Role of the member at read time
                                            (lowercase).
                                          type: string
                                          example: admin
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
                            Per-group approval tally for multi-quorum tasks.
                            Each entry lists a group's ID and the IIBANs of
                            members in that group who have approved so far.
                          type: array
                          items:
                            type: object
                            properties:
                              group_id:
                                description: >-
                                  Subquorum group identifier (UUID v4) matching
                                  an entry in `subquorum_snapshot.groups`.
                                type: string
                                example: 11111111-2222-4333-8444-555555555555
                              approved_iibans:
                                description: >-
                                  IIBANs of group members who have approved the
                                  task.
                                type: array
                                items:
                                  type: string
                                  example: ABCD EFGH IJKL MNOP
                            required:
                              - group_id
                              - approved_iibans
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
                        - instruction_types
                  total:
                    description: >-
                      Total number of tasks matching the filters, prior to
                      pagination.
                    type: integer
                    format: int32
                    example: 42
                required:
                  - result
                  - total
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
                        example: 'Unknown filter value for state: ''archived''.'
                    required:
                      - message
                required:
                  - data
                  - status
                  - title
                  - type
        '403':
          description: >-
            Forbidden. The caller lacks access to the requested task, vault, or
            organization scope.
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
                    example: The caller is not authorized to perform this action.
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
                        example: >-
                          Caller lacks access to the requested task, vault, or
                          organization scope.
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
                    example: Failed to connect to upstream custody service.
                  instance:
                    nullable: true
                    description: Link to debug data for this particular error
                    type: string
                    example: https://debug.kraken.com/req/01HXYZABCDEF
                  data:
                    description: Custom data attached to this problem
                    example: {}
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
  schemas:
    google.protobuf.Timestamp:
      type: string
      format: date-time
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
