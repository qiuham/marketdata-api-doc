---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/media/createChartContext
api_type: Guide
updated_at: 2026-11-23 18:46:03.393724
---

# bn.createChartContext

▸ **createChartContext**<`T`\>(`chartId`, `options?`): `ChartContext`<`T`\>

**`description`** return a chart instance for given chart id

**`remark`** supported jssdk >= 4.14.0

**`example`**

```js
const chartContext = bn.createChartContext("chartId");
cameraContext.setOption({
  tooltip: {
    formatter: {
      type: "function",
      value: ["params", 'return "$" + params[0].data'],
    },
  },
});
```

Type parameters

| Name | Type |
| :--- | :--- |
| `T`  | `""` |

Parameters

| Name                  | Type     |
| :-------------------- | :------- |
| `chartId`             | `string` |
| `options?`            | `Object` |
| `options.rendererId?` | `number` |

Returns

`ChartContext`<`T`\>

## ChartContext

Ƭ **ChartContext**<`T`\>: `T` extends `"flutter"` ? `FlCharts` : `ECharts`

Type parameters

| Name | Type |
| :--- | :--- |
| `T`  | `""` |

---

## Interface: FlCharts

| Name      | Type                                        | Description |
| :-------- | :------------------------------------------ | :---------- |
| setOption | (`options`, `duration?`, `curves?`): `void` |             |
| resize    | (`options`): `void`                         |             |

### setOption

▸ **setOption**(`options`, `duration?`, `curves?`): `void`

Parameters

| Name        | Type                          |
| :---------- | :---------------------------- |
| `options`   | `FlChartLineChartDataOptions` |
| `duration?` | `number`                      |
| `curves?`   | `string`                      |

Returns

`void`

---

### resize

▸ **resize**(`options`): `void`

Parameters

| Name      | Type  |
| :-------- | :---- |
| `options` | `any` |

Returns

`void`

## Interface: FlChartLineChartDataOptions

| Name                      | Type                        | Description |
| :------------------------ | :-------------------------- | :---------- |
| lineBarsData?             | `FlChartLineChartBarData`[] |             |
| titlesData?               | `FlChartTitlesDataOptions`  |             |
| lineTouchData?            | `LineTouchDataOptions`      |             |
| showingTooltipIndicators? | `number`[]                  |             |
| gridData?                 | `FlChartGridDataOptions`    |             |
| minX?                     | `number`                    |             |
| maxX?                     | `number`                    |             |
| baselineX?                | `number`                    |             |
| minY?                     | `number`                    |             |
| maxY?                     | `number`                    |             |
| baselineY?                | `number`                    |             |
| clipData?                 | `string`                    |             |
| backgroundColor?          | [`string`]                  |             |

---

# bn.createChartContext

▸ **createChartContext**<`T`\>(`chartId`, `options?`): `ChartContext`<`T`\>

**`description`** return a chart instance for given chart id

**`remark`** supported jssdk >= 4.14.0

**`example`**

```js
const chartContext = bn.createChartContext("chartId");
cameraContext.setOption({
  tooltip: {
    formatter: {
      type: "function",
      value: ["params", 'return "$" + params[0].data'],
    },
  },
});
```

Type parameters

| Name | Type |
| :--- | :--- |
| `T`  | `""` |

Parameters

| Name                  | Type     |
| :-------------------- | :------- |
| `chartId`             | `string` |
| `options?`            | `Object` |
| `options.rendererId?` | `number` |

Returns

`ChartContext`<`T`\>

## ChartContext

Ƭ **ChartContext**<`T`\>: `T` extends `"flutter"` ? `FlCharts` : `ECharts`

Type parameters

| Name | Type |
| :--- | :--- |
| `T`  | `""` |

---

## Interface: FlCharts

| Name      | Type                                        | Description |
| :-------- | :------------------------------------------ | :---------- |
| setOption | (`options`, `duration?`, `curves?`): `void` |             |
| resize    | (`options`): `void`                         |             |

### setOption

▸ **setOption**(`options`, `duration?`, `curves?`): `void`

Parameters

| Name        | Type                          |
| :---------- | :---------------------------- |
| `options`   | `FlChartLineChartDataOptions` |
| `duration?` | `number`                      |
| `curves?`   | `string`                      |

Returns

`void`

---

### resize

▸ **resize**(`options`): `void`

Parameters

| Name      | Type  |
| :-------- | :---- |
| `options` | `any` |

Returns

`void`

## Interface: FlChartLineChartDataOptions

| Name                      | Type                        | Description |
| :------------------------ | :-------------------------- | :---------- |
| lineBarsData?             | `FlChartLineChartBarData`[] |             |
| titlesData?               | `FlChartTitlesDataOptions`  |             |
| lineTouchData?            | `LineTouchDataOptions`      |             |
| showingTooltipIndicators? | `number`[]                  |             |
| gridData?                 | `FlChartGridDataOptions`    |             |
| minX?                     | `number`                    |             |
| maxX?                     | `number`                    |             |
| baselineX?                | `number`                    |             |
| minY?                     | `number`                    |             |
| maxY?                     | `number`                    |             |
| baselineY?                | `number`                    |             |
| clipData?                 | `string`                    |             |
| backgroundColor?          | [`string`]                  |             |