---
api_type: reference
source_type: llms_txt
version: ''
scope: crypto
asset_class: prediction_market
domain: exchanges
provider: polymarket
provider_name: Polymarket
product: api
product_id: polymarket
source_url: 'https://docs.polymarket.com/cn/trading/wallet-activity'
updated_at: 2026-11-13
---

# 钱包活动

> 追踪与 Polymarket 钱包关联的持仓和活动。

使用钱包地址了解账户当前的风险敞口，并追踪其活动
随时间的变化。

## 未平仓持仓

查看钱包当前的结果敞口和未实现收益表现。

> [tab] TypeScript
>
> 在 `PublicClient` 或 `SecureClient` 上调用 `listPositions()`。
>
> ```ts theme={null}
> const address = "0x8ba1f109551bD432803012645Ac136ddd64DBA72";
>
> const pages = client.listPositions({ user: address, pageSize: 1 });
>
> for await (const page of pages) {
>   // page.items: Position[]
> }
> ```
>
> > [accordion] 输出：Position\[]
> >
> > ```ts Position Type theme={null}
> > // Trimmed for brevity.
> > type Position = {
> >   wallet: EvmAddress;
> >   assetId: TokenId | PositionId;
> >   conditionId: ConditionId;
> >   /** The current holding, in shares. */
> >   currentSize: DecimalString;
> >   avgPrice: DecimalString;
> >   /** Fee-exclusive entry basis in USD. */
> >   entryCostUsdc: DecimalString;
> >   /** Attributed BUY fees in USD (disclosure; already excluded from entryCostUsdc). */
> >   entryFeesUsdc: DecimalString;
> >   /** Always entryCostUsdc + entryFeesUsdc. */
> >   totalCostUsdc: DecimalString;
> >   currentPrice: DecimalString;
> >   currentValue: DecimalString;
> >   realizedPnl: DecimalString;
> >   /** currentValue - entryCostUsdc. */
> >   unrealizedPnl: DecimalString;
> >   /** Always realizedPnl + unrealizedPnl. */
> >   totalPnl: DecimalString;
> >   percentPnl: DecimalString;
> >   status: PositionStatus;
> >   redeemable: boolean;
> >   mergeable: boolean;
> >   negativeRisk: boolean;
> >   title?: string;
> >   slug?: string;
> >   eventSlug?: string;
> >   outcome?: string;
> >   outcomeIndex?: number;
> >   endDate?: IsoCalendarDateString;
> >   lastEventAt?: EpochMilliseconds;
> >   firstEntryAt?: EpochMilliseconds;
> > };
> > ```
> >
> > ```json Position Example theme={null}
> > [
> >   {
> >     "conditionId": "0x747dc809fb79e1b05be09c42d6179459a58de2ef3e40f02484a4e1260f741f75",
> >     "wallet": "0x8ba1f109551bd432803012645ac136ddd64dba72",
> >     "assetId": "107505882767731489358349912513945399560393482969656700824895970500493757150417",
> >     "currentSize": "125.5",
> >     "avgPrice": "0.42",
> >     "entryCostUsdc": "52.71",
> >     "entryFeesUsdc": "0",
> >     "totalCostUsdc": "52.71",
> >     "currentPrice": "0.49",
> >     "currentValue": "61.495",
> >     "realizedPnl": "0",
> >     "unrealizedPnl": "8.785",
> >     "totalPnl": "8.785",
> >     "percentPnl": "16.66",
> >     "status": "OPEN",
> >     "redeemable": false,
> >     "mergeable": false,
> >     "negativeRisk": false,
> >     "title": "Will the US confirm that aliens exist before 2027?",
> >     "slug": "will-the-us-confirm-that-aliens-exist-before-2027",
> >     "eventSlug": "will-the-us-confirm-that-aliens-exist-before-2027",
> >     "outcome": "Yes",
> >     "outcomeIndex": 0
> >   }
> > ]
> > ```
>
> `firstEntryAt` 是首次获取持仓的时间，以 Unix 纪元毫秒表示；未记录时为 `undefined`。获取方式包括买入、拆分、铸造、迁移和转入。

> [tab] Python
>
> 在已创建的 `AsyncPublicClient` 或 `AsyncSecureClient` 上调用 `list_positions()`。
>
> ```python theme={null}
> address = "0x8ba1f109551bD432803012645Ac136ddd64DBA72"
>
> pages = client.list_positions(
>     user=address,
>     page_size=1,
> )
>
> async for page in pages:
>     # page.items: tuple[Position, ...]
>     pass
> ```
>
> > [accordion] Output: Position
> >
> > ```python Position Type theme={null}
> > class Position:
> >     wallet: EvmAddress
> >     asset_id: ClobAssetId
> >     condition_id: ConditionId
> >     current_size: Decimal
> >     avg_price: Decimal
> >     entry_cost_usdc: Decimal
> >     entry_fees_usdc: Decimal
> >     total_cost_usdc: Decimal
> >     current_price: Decimal
> >     current_value: Decimal
> >     total_size: Decimal
> >     realized_pnl: Decimal
> >     unrealized_pnl: Decimal
> >     total_pnl: Decimal
> >     percent_pnl: Decimal
> >     percent_realized_pnl: Decimal
> >     status: PositionStatus
> >     redeemable: bool
> >     mergeable: bool
> >     negative_risk: bool
> >     archived: bool
> >     verified: bool
> >     title: str | None
> >     slug: str | None
> >     icon: str | None
> >     event_slug: str | None
> >     outcome: str | None
> >     opposite_outcome: str | None
> >     name: str | None
> >     profile_image: str | None
> >     event_id: EventId | None
> >     outcome_index: int | None
> >     opposite_asset_id: ClobAssetId | None
> >     end_date: date | None
> >     last_event_at: datetime | None
> >     first_entry_at: datetime | None
> > ```
> >
> > ```json Position Example theme={null}
> > {
> >   "wallet": "0x7c3db723f1d4d8cb9c550095203b686cb11e5c6b",
> >   "asset_id": "94476829201604408463453426454480212459887267917122244941405244686637914508323",
> >   "condition_id": "0x7ad403c3508f8e3912940fd1a913f227591145ca0614074208e0b962d5fcc422",
> >   "current_size": "400000.0",
> >   "avg_price": "0.5",
> >   "entry_cost_usdc": "200000.0",
> >   "entry_fees_usdc": "0.0",
> >   "total_cost_usdc": "200000.0",
> >   "current_price": "0.7545",
> >   "current_value": "301800.0",
> >   "total_size": "10386654.0",
> >   "realized_pnl": "0.0",
> >   "unrealized_pnl": "101800.0",
> >   "total_pnl": "101800.0",
> >   "percent_pnl": "50.9",
> >   "percent_realized_pnl": "-94.1886",
> >   "status": "OPEN",
> >   "redeemable": false,
> >   "mergeable": true,
> >   "negative_risk": true,
> >   "archived": false,
> >   "verified": true,
> >   "title": "Will JD Vance win the 2028 US Presidential Election?",
> >   "slug": "will-jd-vance-win-the-2028-us-presidential-election",
> >   "icon": "https://polymarket-upload.s3.us-east-2.amazonaws.com/will-jd-vance-win-the-2028-us-presidential-election-P-zEgXjCWbdY.png",
> >   "event_slug": "presidential-election-winner-2028",
> >   "outcome": "No",
> >   "opposite_outcome": "Yes",
> >   "name": "Car",
> >   "profile_image": "https://polymarket-upload.s3.us-east-2.amazonaws.com/profile-image-501613-aa434e55-7732-41b1-9650-83a9d1d716ef.png",
> >   "event_id": "31552",
> >   "outcome_index": 1,
> >   "opposite_asset_id": "16040015440196279900485035793550429453516625694844857319147506590755961451627",
> >   "end_date": "2028-11-07",
> >   "last_event_at": "2026-08-23T15:46:10Z",
> >   "first_entry_at": "2025-08-13T21:51:32Z"
> > }
> > ```
>
> `current_size` 的单位为份额。成本、价值和盈亏使用以 USDC 计的 `Decimal`。`entry_cost_usdc` 已排除手续费，不要再次减去 `entry_fees_usdc`。`first_entry_at` 是首次获取持仓的 UTC `datetime`；未记录时为 `None`。获取方式包括买入、拆分、铸造、迁移和转入。
>
> 仓位读取默认不限制时间。`full_history=True` 保持此行为，也包含没有活动时间戳的持仓。需要按最近活动时间筛选时，使用 `start` 和 `end`。

> [tab] API
>
> 列出钱包的未平仓持仓：
>
> ```bash theme={null}
> ADDRESS="0x8ba1f109551bD432803012645Ac136ddd64DBA72"
>
> curl "https://data-api.polymarket.com/v2/positions?user=$ADDRESS&limit=1"
> ```
>
> 响应包含钱包的未平仓持仓（为简洁起见省略了部分行字段）：
>
> > [accordion] 响应
> >
> > ```json theme={null}
> > {
> >   "data": [
> >     {
> >       "proxy_wallet": "0x8ba1f109551bD432803012645Ac136ddd64DBA72",
> >       "token_id": "107505882767731489358349912513945399560393482969656700824895970500493757150417",
> >       "condition_id": "0x747dc809fb79e1b05be09c42d6179459a58de2ef3e40f02484a4e1260f741f75",
> >       "status": "OPEN",
> >       "current_size": 125.5,
> >       "avg_price": 0.42,
> >       "entry_cost_usdc": 52.71,
> >       "current_price": 0.49,
> >       "current_value": 61.5,
> >       "unrealized_pnl": 8.79,
> >       "total_pnl": 8.79,
> >       "percent_pnl": 16.68,
> >       "redeemable": false,
> >       "mergeable": false,
> >       "title": "Will the US confirm that aliens exist before 2027?",
> >       "slug": "will-the-us-confirm-that-aliens-exist-before-2027",
> >       "event_slug": "will-the-us-confirm-that-aliens-exist-before-2027",
> >       "outcome": "Yes",
> >       "outcome_index": 0
> >     }
> >   ],
> >   "pagination": {
> >     "limit": 1,
> >     "offset": 0,
> >     "has_more": true,
> >     "next_cursor": "eyJkYXRhIjp7InR5cGUiOiJwb3NpdGlvbnMi…"
> >   }
> > }
> > ```
>
> 持仓的获取时间字段如下：
>
> | 字段 | 类型 |
> | - | - |
> | `first_entry_at` | integer |
>
> `first_entry_at` 是首次获取持仓的时间，以 Unix 纪元秒表示；未记录时为 `0`。获取方式包括买入、拆分、铸造、迁移和转入。
>
> 使用 `cursor` 参数携带 `pagination.next_cursor` 获取下一页。

### 按标题筛选持仓

将持仓限定为标题包含搜索词的市场，匹配不区分大小写。
此筛选适用于所有持仓状态，也适用于列出某个市场的持有人。

> [tab] TypeScript
>
> 在现有的 `PublicClient` 或 `SecureClient` 上向 `listPositions()` 传入 `title`：
>
> ```ts theme={null}
> const pages = client.listPositions({ user: address, title: "election" });
>
> for await (const page of pages) {
>   // page.items: Position[]
> }
> ```
>
> `title` 最多接受 200 个 Unicode 字符。空字符串或仅含空白字符的输入会禁用筛选。
> 其他模式保持原样；`%` 匹配任意字符序列，`_` 匹配一个字符。
> 分页器会在每一页保留 `title`，通过 `pages.from(nextCursor)` 恢复分页时也一样。

> [tab] Python
>
> 在现有的 `AsyncPublicClient` 或 `AsyncSecureClient` 上向 `list_positions()`
> 传入 `title`。同步客户端接受相同参数：
>
> ```python theme={null}
> pages = client.list_positions(user=address, title="election")
>
> async for page in pages:
>     # page.items: tuple[Position, ...]
>     pass
> ```
>
> `title` 最多接受 200 个 Unicode 字符。空字符串或仅含空白字符的输入会禁用筛选。
> 其他模式保持原样；`%` 匹配任意字符序列，`_` 匹配一个字符。
> 分页器会在每一页保留 `title`，通过 `pages.from_cursor(next_cursor)` 恢复分页时也一样。

> [tab] API
>
> 在持仓请求中发送 `title`：
>
> ```bash theme={null}
> curl --get "https://data-api.polymarket.com/v2/positions" \
>   --data-urlencode "user=$ADDRESS" \
>   --data-urlencode "title=election"
> ```
>
> `title` 最多接受 200 个 Unicode 字符。空字符串或仅含空白字符的输入会禁用筛选。
> 其他模式保持原样；SQL `LIKE` 通配符保留其含义：`%` 匹配任意字符序列，
> `_` 匹配一个字符。
> 每次携带 `cursor` 请求下一页时，都要重发相同的 `title` 和锚点。
> 游标不携带标题筛选，省略它会扩大后续页面的结果范围。

## 已平仓持仓

查看钱包已退出或已结算的持仓，包括
其已实现收益表现。

> [tab] TypeScript
>
> 同一个方法覆盖持仓的全生命周期：调用 `listPositions()` 并传入
> `status: PositionStatus.Closed`。已平仓的行沿用同一 `Position` 结构，携带已实现
> 的经济数据（`currentSize` 是接近 0 的残值，结果体现在 `realizedPnl`），默认按已实现
> 盈亏排序。
>
> 此示例使用已有的 `PublicClient` 或 `SecureClient`。如尚未创建客户端，请先[创建公共客户端](https://docs.polymarket.com/cn/getting-started/typescript.md)。
>
> ```ts theme={null}
> import {
>   PositionSortBy,
>   PositionStatus,
>   SortDirection,
> } from "@polymarket/client";
>
> const pages = client.listPositions({
>   user: address,
>   status: PositionStatus.Closed,
>   sortBy: PositionSortBy.Price,
>   sortDirection: SortDirection.Desc,
>   pageSize: 1,
> });
>
> for await (const page of pages) {
>   // page.items: Position[]
> }
> ```
>
> > [accordion] 输出：Position\[]
> >
> > ```json Position Example theme={null}
> > [
> >   {
> >     "conditionId": "0x747dc809fb79e1b05be09c42d6179459a58de2ef3e40f02484a4e1260f741f75",
> >     "wallet": "0x8ba1f109551bd432803012645ac136ddd64dba72",
> >     "assetId": "7305630249804085635496399869905769372294302716159034447326228509068694952392",
> >     "currentSize": "0",
> >     "avgPrice": "0.58",
> >     "entryCostUsdc": "145",
> >     "totalCostUsdc": "145",
> >     "realizedPnl": "34.25",
> >     "unrealizedPnl": "0",
> >     "totalPnl": "34.25",
> >     "status": "CLOSED",
> >     "redeemable": false,
> >     "title": "Will the US confirm that aliens exist before 2027?",
> >     "outcome": "No",
> >     "outcomeIndex": 1
> >   }
> > ]
> > ```
>
> 按 `user` 查询且 `status` 为 `PositionStatus.Closed` 时，`PositionSortBy.Tokens`、`CurrentValue`、`Price` 与 `UnrealizedPnl` 均按已实现盈亏排序，并保留请求的 `sortDirection`。因此，此示例按已实现盈亏降序排列。`RealizedPnl`、`TotalPnl` 与 `Timestamp` 保留各自语义。仅按市场查询的 CLOSED 列表不受此回退规则影响。
>
> 继续分页时保留原请求的筛选条件与 `sortBy`，不要改写为 `RealizedPnl`。旧残值排序游标可能触发 `RequestRejectedError`，错误消息包含 `positions order changed; restart pagination without cursor`。SDK 会将错误交给调用方，不会自动重启。明确丢弃该游标，然后用原请求且不传 `cursor` 重新开始。重启可能再次返回已读取的行。

> [tab] Python
>
> 在已创建的 `AsyncPublicClient` 或 `AsyncSecureClient` 上调用 `list_positions()`。
> 如尚未创建客户端，请先[创建公共客户端](https://docs.polymarket.com/cn/getting-started/python.md)。
>
> ```python theme={null}
> pages = client.list_positions(
>     user=address,
>     status="CLOSED",
>     sort_by="PRICE",
>     sort_direction="DESC",
>     page_size=1,
> )
>
> async for page in pages:
>     # page.items: tuple[Position, ...]
>     pass
> ```
>
> 已关闭仓位与未平仓仓位使用相同的 `Position` 模型。使用 `realized_pnl` 读取已实现盈亏。安全客户端可省略 `user`，读取已认证钱包的仓位。
>
> 按 `user` 查询且 `status="CLOSED"` 时，`sort_by` 的 `TOKENS`、`CURRENT_VALUE`、`PRICE` 与 `UNREALIZED_PNL` 均按已实现盈亏排序，并保留 `sort_direction`。因此，此示例按已实现盈亏降序排列。`REALIZED_PNL`、`TOTAL_PNL` 与 `TIMESTAMP` 保留各自语义。仅按市场查询的 CLOSED 列表不受此回退规则影响。
>
> 继续分页时保留原筛选条件与 `sort_by`，不要改写为 `REALIZED_PNL`。旧残值排序游标可能触发 `RequestRejectedError`，错误消息包含 `positions order changed; restart pagination without cursor`。SDK 会将错误交给调用方，不会自动重启。明确丢弃该游标，然后用原请求且不传 `cursor` 重新开始。重启可能再次返回已读取的行。

> [tab] API
>
> 已平仓持仓由同一路由通过 `status` 过滤器提供：
>
> ```bash theme={null}
> curl "https://data-api.polymarket.com/v2/positions?user=$ADDRESS&status=CLOSED&sort_by=PRICE&sort_direction=DESC&limit=1"
> ```
>
> 响应包含钱包的已平仓持仓（为简洁起见省略了部分行字段）：
>
> > [accordion] 响应
> >
> > ```json theme={null}
> > {
> >   "data": [
> >     {
> >       "proxy_wallet": "0x8ba1f109551bD432803012645Ac136ddd64DBA72",
> >       "token_id": "7305630249804085635496399869905769372294302716159034447326228509068694952392",
> >       "condition_id": "0x747dc809fb79e1b05be09c42d6179459a58de2ef3e40f02484a4e1260f741f75",
> >       "status": "CLOSED",
> >       "current_size": 0,
> >       "total_size": 250,
> >       "avg_price": 0.58,
> >       "current_price": 0,
> >       "realized_pnl": 34.25,
> >       "total_pnl": 34.25,
> >       "last_event_at": 1782752879,
> >       "title": "Will the US confirm that aliens exist before 2027?",
> >       "slug": "will-the-us-confirm-that-aliens-exist-before-2027",
> >       "event_slug": "will-the-us-confirm-that-aliens-exist-before-2027",
> >       "outcome": "No",
> >       "outcome_index": 1
> >     }
> >   ],
> >   "pagination": {
> >     "limit": 1,
> >     "offset": 0,
> >     "has_more": true,
> >     "next_cursor": "eyJkYXRhIjp7InR5cGUiOiJwb3NpdGlvbnMi…"
> >   }
> > }
> > ```
>
> 按 `user` 查询且 `status=CLOSED` 时，`sort_by` 的 `TOKENS`、`CURRENT_VALUE`、`PRICE` 与 `UNREALIZED_PNL` 均按已实现盈亏排序，并保留 `sort_direction`。`REALIZED_PNL`、`TOTAL_PNL` 与 `TIMESTAMP` 保留各自语义。仅按市场查询的 CLOSED 列表不受此回退规则影响。
>
> 使用返回的 `pagination.next_cursor` 继续分页，保留原筛选条件与请求的 `sort_by`。旧残值排序游标会返回 HTTP `400`，消息为 `invalid cursor: positions order changed; restart pagination without cursor`。明确丢弃该游标，用原请求且不传 `cursor` 重新开始。不要通过修改排序值或反复重试同一游标来恢复。重启可能再次返回已读取的行。

## 按价格排序持仓

按当前有效价格排列钱包持仓，找出价格最低或最高的结果。

> [tab] TypeScript
>
> 在已创建的 `PublicClient` 或 `SecureClient` 上调用 `listPositions()`，
> 使用未平仓持仓示例中的 `address`。
>
> ```ts theme={null}
> import { PositionSortBy, SortDirection } from "@polymarket/client";
>
> const pages = client.listPositions({
>   user: address,
>   sortBy: PositionSortBy.Price,
>   sortDirection: SortDirection.Asc,
> });
>
> for await (const page of pages) {
>   // page.items: Position[]
> }
> ```
>
> `PositionSortBy.Price` 按 `currentPrice` 排序。使用 `SortDirection.Desc` 将最高价格
> 排在前面。分页器会在后续页面中保留所选排序。

> [tab] Python
>
> 在已创建的 `AsyncPublicClient` 或 `AsyncSecureClient` 上调用 `list_positions()`，
> 使用未平仓持仓示例中的 `address`。同步客户端接受相同的排序选项。
>
> ```python theme={null}
> pages = client.list_positions(
>     user=address,
>     sort_by="PRICE",
>     sort_direction="ASC",
> )
>
> async for page in pages:
>     # page.items: tuple[Position, ...]
>     pass
> ```
>
> `sort_by="PRICE"` 按 `current_price` 排序。使用 `sort_direction="DESC"` 将最高价格
> 排在前面。分页器会在后续页面中保留所选排序。

> [tab] API
>
> 使用未平仓持仓示例中的 `ADDRESS` 请求钱包持仓：
>
> ```bash theme={null}
> curl "https://data-api.polymarket.com/v2/positions?user=$ADDRESS&sort_by=PRICE&sort_direction=ASC&limit=100"
> ```
>
> `sort_by=PRICE` 按 `current_price` 排序。使用 `sort_direction=DESC` 将最高价格排在前面。
> 获取后续页面时，将 `pagination.next_cursor` 作为 `cursor` 传入，并保留相同的排序参数。

可赎回持仓始终将获胜持仓排在亏损持仓之前，再在各组内应用所选的价格顺序。
请求按价格排序时，钱包的已平仓持仓会按已实现盈亏排序。

未指定排序时，可合并持仓按代币数量排序，已平仓持仓按已实现盈亏排序，
其他持仓按当前价值排序。默认方向为降序。

## 活动历史

追踪钱包在交易及其他活动中的时间线。

> [tab] TypeScript
>
> 在已有的 `PublicClient` 或 `SecureClient` 上调用 `listActivity()`。如尚未创建客户端，请先[创建公共客户端](https://docs.polymarket.com/cn/getting-started/typescript.md)。
>
> ```ts theme={null}
> import { ActivityType } from "@polymarket/client";
>
> const pages = client.listActivity({ user: address, pageSize: 1 });
>
> for await (const page of pages) {
>   for (const activity of page.items) {
>     if (
>       (activity.type === ActivityType.TRADE ||
>         activity.type === ActivityType.REDEEM) &&
>       activity.isCombo
>     ) {
>       console.log(
>         activity.conditionId,
>         activity.outcome,
>         activity.outcomeIndex,
>       );
>     }
>   }
> }
> ```
>
> 对 `TRADE`、`SPLIT`、`MERGE` 与 `REDEEM`，先检查 `type`，再检查 `isCombo`。`true` 表示 Combo 活动，`false` 表示普通市场活动。`RedeemActivity` 是 `ClobRedeemActivity | ComboRedemptionActivity`。Combo 记录的 `conditionId` 使用 `ComboConditionId`。Combo 拆分、合并与赎回的标题可能不可用，也不对应单个市场或事件的 URL slug。
>
> Combo 的 `outcome` 与 `outcomeIndex` 描述整体篮子代币的 Yes/No 一侧，不是所选单腿的标签。未知标签或索引保持 `undefined`，已知索引 `0` 会保留。自动赎回也归入 `ActivityType.REDEEM`。
>
> 这次 0.x API 更新为 `SplitActivity`、`MergeActivity` 与 `RedeemActivity`
> 添加 Combo 变体，属于源码兼容性变更。之前仅检查 `type` 就读取市场 URL 的代码，还需检查
> `!isCombo`。例如，在同一个活动迭代器中读取普通市场 URL：
>
> ```ts theme={null}
> const pages = client.listActivity({ user: address });
> for await (const page of pages) {
>   for (const activity of page.items) {
>     if (
>       (activity.type === ActivityType.SPLIT ||
>         activity.type === ActivityType.MERGE ||
>         activity.type === ActivityType.REDEEM) &&
>       !activity.isCombo
>     ) {
>       console.log(activity.slug, activity.eventSlug);
>     }
>   }
> }
> ```
>
> 普通记录返回 `isCombo: false`。手动构造普通拆分、合并与赎回对象时可省略此字段。
>
> `Activity` 是可辨识联合类型。`type` 字段用于标识
> 每个变体：
>
> > [accordion] 输出：Activity\[]
> >
> > ```ts Activity Union theme={null}
> > type Activity =
> >   | TradeActivity
> >   | SplitActivity
> >   | MergeActivity
> >   | RedeemActivity
> >   | ConversionActivity
> >   | MigrationActivity
> >   | RewardActivity
> >   | MakerRebateActivity
> >   | ReferralRewardActivity
> >   | YieldActivity
> >   | DepositActivity
> >   | WithdrawalActivity
> >   | TakerRebateActivity
> >   | TipActivity;
> > ```
> >
> > ```json Activity Example theme={null}
> > [
> >   {
> >     "type": "TRADE",
> >     "isCombo": false,
> >     "wallet": "0x8ba1f109551bD432803012645Ac136ddd64DBA72",
> >     "timestamp": 1782752879000,
> >     "transactionHash": "0x4f3d2c1b0a9876543210fedcba9876543210fedcba9876543210fedcba987654",
> >     "conditionId": "0x747dc809fb79e1b05be09c42d6179459a58de2ef3e40f02484a4e1260f741f75",
> >     "assetId": "107505882767731489358349912513945399560393482969656700824895970500493757150417",
> >     "side": "BUY",
> >     "shares": "25",
> >     "amount": "12.25",
> >     "price": "0.49",
> >     "title": "Will the US confirm that aliens exist before 2027?",
> >     "slug": "will-the-us-confirm-that-aliens-exist-before-2027",
> >     "eventSlug": "will-the-us-confirm-that-aliens-exist-before-2027",
> >     "outcome": "Yes",
> >     "outcomeIndex": 0
> >   },
> >   {
> >     "type": "REWARD",
> >     "wallet": "0x8ba1f109551bD432803012645Ac136ddd64DBA72",
> >     "timestamp": 1782752979000,
> >     "transactionHash": "0x7a6b5c4d3e2f109876543210fedcba9876543210fedcba9876543210fedcba98",
> >     "amount": "5"
> >   }
> > ]
> > ```

> [tab] Python
>
> 在已有的 `AsyncPublicClient` 或 `AsyncSecureClient` 上调用 `list_activity()`。如尚未创建客户端，请先[创建公共客户端](https://docs.polymarket.com/cn/getting-started/python.md)。
>
> ```python theme={null}
> from polymarket import ComboTradeActivity, RedeemActivity
>
> pages = client.list_activity(user=address, page_size=1)
>
> async for page in pages:
>     for activity in page.items:
>         if isinstance(activity, (ComboTradeActivity, RedeemActivity)) and activity.is_combo:
>             print(activity.condition_id, activity.outcome, activity.outcome_index)
> ```
>
> 检查交易与赎回的 `is_combo`，识别 Combo 活动。`ComboTradeActivity` 的 `is_combo` 为 `True`，使用 `ComboConditionId`。所有赎回仍返回 `RedeemActivity`，保留 `ConditionId`。通过 `is_combo` 区分整体篮子与普通市场。现有 `isinstance(activity, RedeemActivity)` 检查也包含 Combo 赎回。
>
> Combo 的 `outcome` 与 `outcome_index` 描述整体篮子代币的 Yes/No 一侧，不是所选单腿的标签。未知标签或索引保持 `None`，已知索引 `0` 会保留。自动赎回也归入 `REDEEM`。
>
> 使用 `activity_types` 筛选活动类型。读取完整历史时设置 `full_history=True`，并省略 `start` 和 `end`。
>
> ```python theme={null}
> pages = client.list_activity(
>     user=address,
>     activity_types=["DEPOSIT", "WITHDRAWAL"],
>     full_history=True,
> )
> ```
>
> > [accordion] Output: Activity
> >
> > ```python Activity Union theme={null}
> > Activity = (
> >     TradeActivity
> >     | ComboTradeActivity
> >     | SplitActivity
> >     | MergeActivity
> >     | RedeemActivity
> >     | ConversionActivity
> >     | RewardActivity
> >     | DepositActivity
> >     | WithdrawalActivity
> >     | MakerRebateActivity
> >     | TakerRebateActivity
> >     | ReferralRewardActivity
> >     | YieldActivity
> >     | MigrationActivity
> >     | TipActivity
> >     | UnknownActivity
> > )
> > ```
> >
> > ```json Activity Example theme={null}
> > [
> >   {
> >     "wallet": "0x7c3db723f1d4d8cb9c550095203b686cb11e5c6b",
> >     "timestamp": "2026-09-08T16:56:49Z",
> >     "transaction_hash": "0xa661459fc2483ddb4e5c7d13c76347fa2b1fb2faae10eed484c810ae46c471dd",
> >     "name": "Car",
> >     "pseudonym": "Peppery-Capital",
> >     "bio": "what is your plan",
> >     "profile_image": "https://polymarket-upload.s3.us-east-2.amazonaws.com/profile-image-501613-aa434e55-7732-41b1-9650-83a9d1d716ef.png",
> >     "profile_image_optimized": null,
> >     "type": "TRADE",
> >     "is_combo": false,
> >     "condition_id": "0x0a91645ed98ad09817e051a17466cff087b920393aefba0fe74e8735fc192f15",
> >     "asset_id": "98255364887669934733864645030488537034263699416357729920734267612805930214172",
> >     "side": "BUY",
> >     "shares": "14.285715",
> >     "amount": "13.285715",
> >     "price": "0.9300000035",
> >     "outcome": "Yes",
> >     "outcome_index": 0,
> >     "title": "LAPTOP FDV above $25M one day after launch?",
> >     "slug": "laptop-fdv-above-25m-one-day-after-launch",
> >     "icon": "https://polymarket-upload.s3.us-east-2.amazonaws.com/laptop-fdv-above-25m-one-day-after-launch-UQwx2GeHcu_f.jpg",
> >     "event_slug": "laptop-fdv-above-one-day-after-launch"
> >   }
> > ]
> > ```

> [tab] API
>
> 列出钱包活动：
>
> ```bash theme={null}
> curl "https://data-api.polymarket.com/v2/activity?user=$ADDRESS&limit=1"
> ```
>
> 该接口默认排除存款和提款记录，即使 `type` 请求了它们。要获取这些记录，
> 请传入 `exclude_deposits_withdrawals=false`。
>
> 响应包含钱包活动（为简洁起见省略了部分行字段）：
>
> > [accordion] 响应
> >
> > ```json theme={null}
> > {
> >   "data": [
> >     {
> >       "proxy_wallet": "0x8ba1f109551bD432803012645Ac136ddd64DBA72",
> >       "timestamp": 1782752879,
> >       "condition_id": "0x747dc809fb79e1b05be09c42d6179459a58de2ef3e40f02484a4e1260f741f75",
> >       "type": "TRADE",
> >       "size": 25,
> >       "usdc_size": 12.25,
> >       "transaction_hash": "0x4f3d2c1b0a9876543210fedcba9876543210fedcba9876543210fedcba987654",
> >       "price": 0.49,
> >       "token_id": "107505882767731489358349912513945399560393482969656700824895970500493757150417",
> >       "side": "BUY",
> >       "title": "Will the US confirm that aliens exist before 2027?",
> >       "slug": "will-the-us-confirm-that-aliens-exist-before-2027",
> >       "event_slug": "will-the-us-confirm-that-aliens-exist-before-2027",
> >       "outcome": "Yes",
> >       "outcome_index": 0
> >     }
> >   ],
> >   "pagination": {
> >     "limit": 1,
> >     "offset": 0,
> >     "has_more": true,
> >     "next_cursor": "eyJkYXRhIjp7InR5cGUiOiJhY3Rpdml0eSI…"
> >   }
> > }
> > ```
>
> 对 `TRADE`、`SPLIT`、`MERGE` 与 `REDEEM` 记录，`is_combo=true` 表示 Combo 活动。普通活动省略此字段。Combo 交易与赎回的 `outcome` 与 `outcome_index` 是整体篮子代币的 Yes/No 标签与槽位，不是所选单腿的结果。自动赎回也返回 `type=REDEEM`。空标签与索引 `999` 表示信息不可用。索引 `0` 是已知值。保留返回的 `condition_id` 宽度，不要通过 ID 前缀判断活动类型。

## 通知

通知为已连接账户提供短期保留的未读事件记录。
CLOB 会将这些记录保留 48 小时。

### 列出通知

> [tab] TypeScript
>
> 在 `SecureClient` 上调用 `fetchNotifications()`：
>
> ```ts theme={null}
> const notifications = await client.fetchNotifications();
>
> // notifications: Notification[]
> ```
>
> > [accordion] 输出：Notification\[]
> >
> > ```ts Notification Type theme={null}
> > type Notification = {
> >   id: NotificationId;
> >   owner: string;
> >   payload: unknown;
> >   timestamp: EpochMilliseconds;
> >   type: number;
> > };
> > ```
> >
> > ```json Notification Example theme={null}
> > [
> >   {
> >     "id": 1,
> >     "owner": "f4f247b7-4ac7-ff29-a152-04fda0a8755a",
> >     "type": 2,
> >     "payload": {
> >       "order_id": "0x72c66a1f70c00ac5e5eb9ce0452b7d118bc4869f8b822a1a8d8580c16e3ca83e"
> >     },
> >     "timestamp": 1675277676000
> >   }
> > ]
> > ```

> [tab] Python
>
> 在 `AsyncSecureClient` 上调用 `get_notifications()`。同步
> `SecureClient` 也提供相同方法：
>
> ```python theme={null}
> notifications = await client.get_notifications()
>
> # notifications: tuple[Notification, ...]
> ```
>
> > [accordion] 输出：tuple\[Notification, ...]
> >
> > ```python Notification Type theme={null}
> > class Notification:
> >     id: int
> >     owner: str
> >     type: int
> >     payload: Any
> >     timestamp: datetime
> > ```
> >
> > ```json Notification Example theme={null}
> > [
> >   {
> >     "id": 1,
> >     "owner": "f4f247b7-4ac7-ff29-a152-04fda0a8755a",
> >     "type": 2,
> >     "payload": {
> >       "order_id": "0x72c66a1f70c00ac5e5eb9ce0452b7d118bc4869f8b822a1a8d8580c16e3ca83e"
> >     },
> >     "timestamp": "2023-02-01T18:54:36Z"
> >   }
> > ]
> > ```

> [tab] API
>
> 列出账户的未读通知：
>
> ```bash theme={null}
> curl -G "https://clob.polymarket.com/notifications" \
>   -H "POLY_ADDRESS: <signer_address>" \
>   -H "POLY_SIGNATURE: <clob_l2_signature>" \
>   -H "POLY_TIMESTAMP: <clob_request_timestamp>" \
>   -H "POLY_API_KEY: <clob_api_key>" \
>   -H "POLY_PASSPHRASE: <clob_api_passphrase>" \
>   --data-urlencode "signature_type=<signature_type>"
> ```
>
> 使用 [API
> 身份验证](https://docs.polymarket.com/cn/getting-started/api.md#身份验证)中的签名者地址和 CLOB API 凭据，
> 创建新的 `<clob_request_timestamp>`，并为
> `GET /notifications` 生成 `<clob_l2_signature>`。`signature_type`
> 查询参数不属于签名路径：
>
> ```text theme={null}
> message = <clob_request_timestamp> + "GET" + "/notifications"
>
> clob_l2_signature = urlsafeBase64WithPadding(
>   HMAC-SHA256(base64Decode(<clob_api_secret>), message)
> )
> ```
>
> 根据已连接账户的[钱包
> 类型](https://docs.polymarket.com/cn/trading/wallets-auth.md#钱包类型)选择 `signature_type`：
>
> | 钱包 | `signature_type` |
> | - | -: |
> | 存款钱包 | `3` |
> | 代理钱包 | `1` |
> | Safe 钱包 | `2` |
> | EOA | `0` |
>
> 响应包含未读通知：
>
> ```json theme={null}
> [
>   {
>     "id": 1,
>     "owner": "f4f247b7-4ac7-ff29-a152-04fda0a8755a",
>     "type": 2,
>     "payload": {
>       "order_id": "0x72c66a1f70c00ac5e5eb9ce0452b7d118bc4869f8b822a1a8d8580c16e3ca83e"
>     },
>     "timestamp": 1675277676
>   }
> ]
> ```

### 丢弃通知

处理通知后将其标记为已读。列出未读通知时，已丢弃的通知
将不再出现。

> [tab] TypeScript
>
> 使用通知 ID 在 `SecureClient` 上调用 `dropNotifications()`：
>
> ```ts theme={null}
> await client.dropNotifications({
>   ids: notifications.map(({ id }) => String(id)),
> });
> ```

> [tab] Python
>
> 在 `AsyncSecureClient` 上调用 `drop_notifications()`。同步
> `SecureClient` 也提供相同方法：
>
> ```python theme={null}
> await client.drop_notifications(
>     ids=[notification.id for notification in notifications],
> )
> ```

> [tab] API
>
> 将通知 ID 作为逗号分隔的列表发送：
>
> ```bash theme={null}
> curl -X DELETE -G "https://clob.polymarket.com/notifications" \
>   -H "POLY_ADDRESS: <signer_address>" \
>   -H "POLY_SIGNATURE: <clob_l2_signature>" \
>   -H "POLY_TIMESTAMP: <clob_request_timestamp>" \
>   -H "POLY_API_KEY: <clob_api_key>" \
>   -H "POLY_PASSPHRASE: <clob_api_passphrase>" \
>   --data-urlencode "ids=1,2"
> ```
>
> 使用 [API
> 身份验证](https://docs.polymarket.com/cn/getting-started/api.md#身份验证)中的签名者地址和 CLOB API 凭据，
> 创建新的 `<clob_request_timestamp>`，并为
> `DELETE /notifications` 生成 `<clob_l2_signature>`。`ids`
> 查询参数不属于签名路径：
>
> ```text theme={null}
> message = <clob_request_timestamp> + "DELETE" + "/notifications"
>
> clob_l2_signature = urlsafeBase64WithPadding(
>   HMAC-SHA256(base64Decode(<clob_api_secret>), message)
> )
> ```
>
> 请求成功时返回 `OK`。

## 投资组合价值

读取钱包当前的投资组合价值。

> [tab] TypeScript
>
> 在 `PublicClient` 或 `SecureClient` 上调用 `fetchPortfolioValue()`。返回单个对象：
> 钱包按市值计价的投资组合价值（USDC，保留四位小数）。
>
> ```ts theme={null}
> const portfolioValue = await client.fetchPortfolioValue({ user: address });
>
> // portfolioValue: PortfolioValue
> ```
>
> > [accordion] 输出：PortfolioValue
> >
> > ```ts PortfolioValue Type theme={null}
> > type PortfolioValue = {
> >   wallet: EvmAddress;
> >   /** Total marked portfolio value, in USDC, rounded to four decimals. */
> >   value: DecimalString;
> > };
> > ```
> >
> > ```json PortfolioValue Example theme={null}
> > {
> >   "wallet": "0x8ba1f109551bd432803012645ac136ddd64dba72",
> >   "value": "1842.37"
> > }
> > ```

> [tab] Python
>
> 在已创建的 `AsyncPublicClient` 或 `AsyncSecureClient` 上调用 `get_portfolio_value()`。
>
> ```python theme={null}
> portfolio_value = await client.get_portfolio_value(user=address)
>
> # portfolio_value: PortfolioValue
> ```
>
> > [accordion] Output: PortfolioValue
> >
> > ```python PortfolioValue Type theme={null}
> > class PortfolioValue:
> >     wallet: EvmAddress
> >     value: Decimal
> > ```
> >
> > ```json PortfolioValue Example theme={null}
> > {
> >   "wallet": "0x7c3db723f1d4d8cb9c550095203b686cb11e5c6b",
> >   "value": "684953.8942"
> > }
> > ```
>
> 结果为一个 `PortfolioValue` 对象。`value` 是钱包以 USDC 计的投资组合市值。

> [tab] API
>
> 获取钱包的投资组合价值：
>
> ```bash theme={null}
> curl "https://data-api.polymarket.com/v2/value?user=$ADDRESS"
> ```
>
> 响应包含钱包当前的投资组合价值：
>
> > [accordion] 响应
> >
> > ```json theme={null}
> > {
> >   "data": {
> >     "proxy_wallet": "0x8ba1f109551bD432803012645Ac136ddd64DBA72",
> >     "value": 1842.37
> >   }
> > }
> > ```

## 钱包统计

查看钱包的历史交易统计。

> [tab] TypeScript
>
> 在 `PublicClient` 或 `SecureClient` 上调用 `fetchUserStats()`。
>
> ```ts theme={null}
> const stats = await client.fetchUserStats({ user: address });
>
> // stats: UserStats | null
> const tradedMarketCount = stats?.tradedMarketCount;
> ```
>
> `tradedMarketCount` 统计已交易的不同市场数量，而非成交笔数。未知用户的 `stats` 为 `null`。

> [tab] Python
>
> 在已创建的 `AsyncPublicClient` 或 `AsyncSecureClient` 上调用 `get_user_stats()`。
>
> ```python theme={null}
> stats = await client.get_user_stats(user=address)
>
> # stats: UserStats | None
> traded_market_count = stats.traded_market_count if stats is not None else None
> ```
>
> `traded_market_count` 计算不同市场的数量，而不是成交笔数。没有统计数据时，`stats` 为 `None`。安全客户端默认使用已认证钱包作为 `user`。

> [tab] API
>
> 获取钱包的资料统计：
>
> ```bash theme={null}
> curl "https://data-api.polymarket.com/v2/user-stats?user=$ADDRESS"
> ```
>
> `data.trades` 统计已交易的不同市场数量，替代 `/traded` 的计数。未知用户返回 `data: null`。

## 钱包盈亏历史

查看钱包累计盈亏随时间的变化。

> [tab] TypeScript
>
> 在 `PublicClient` 或 `SecureClient` 上调用 `fetchUserPnl()`。
>
> ```ts theme={null}
> const pnl = await client.fetchUserPnl({ user: address });
>
> // pnl: UserPnlSeries
> const points = pnl.points;
> // points: UserPnlPoint[]
> ```
>
> 默认获取一天内每小时的数据。`points` 按时间升序排列，每个点都是累计值。金额为 `null` 表示不可用，并非零。

> [tab] Python
>
> 在已创建的 `AsyncPublicClient` 或 `AsyncSecureClient` 上调用 `get_user_pnl()`。
>
> ```python theme={null}
> pnl = await client.get_user_pnl(user=address, interval="1d", fidelity="1h")
>
> # pnl: UserPnlSeries
> points = pnl.points
> # points: tuple[UserPnlPoint, ...]
> ```
>
> `points` 为累计值，按时间从早到晚排列。不要将其相加作为期间收益。不可用的可选金额保持为 `None`。盈亏单位为 USDC，成交量单位为份额。

> [tab] API
>
> 获取最近一天的累计盈亏观测：
>
> ```bash theme={null}
> curl "https://data-api.polymarket.com/v2/user-pnl?user=$ADDRESS&interval=1d&fidelity=1h"
> ```
>
> `data.points` 包含按时间升序排列的累计观测。不要将这些点相加作为期间收益，也不要将不可用金额视为零。

## 钱包交易量

查看钱包在所选时间段内的交易量。

> [tab] TypeScript
>
> 在 `PublicClient` 或 `SecureClient` 上调用 `fetchUserVolume()`。
>
> ```ts theme={null}
> const volume = await client.fetchUserVolume({
>   user: address,
>   window: { start: new Date("2026-09-01T00:00:00Z") },
> });
>
> // volume: UserVolume
> ```
>
> `volume.volume` 以份额计量，`volume.volumeUsdc` 以美元计量，`volume.tradeCount` 统计成交笔数。时间边界扩展为完整的 UTC 日。

> [tab] Python
>
> 在已创建的 `AsyncPublicClient` 或 `AsyncSecureClient` 上调用 `get_user_volume()`。
>
> ```python theme={null}
> from datetime import UTC, datetime
>
> volume = await client.get_user_volume(
>     user=address,
>     start=datetime(2026, 9, 1, tzinfo=UTC),
> )
>
> # volume: UserVolume
> ```
>
> `volume.volume` 的单位为份额，`volume.volume_usdc` 的单位为 USDC，`volume.trade_count` 计算成交笔数。时间边界向下取整到 UTC 日期。读取完整历史时设置 `full_history=True`，并省略 `start` 和 `end`。

> [tab] API
>
> 获取九月初以来的交易量：
>
> ```bash theme={null}
> curl "https://data-api.polymarket.com/v2/user-volume?user=$ADDRESS&start=1788220800"
> ```
>
> `data.volume` 以份额计量，`data.volume_usdc` 以美元计量，`data.trade_count` 统计成交笔数。`start`/`end` 使用 Unix 秒，并扩展为完整的 UTC 日。


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
