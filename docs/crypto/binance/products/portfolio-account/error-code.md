---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/portfolio-account/error-code
api_type: Guide
updated_at: 2026-11-27 18:30:09.832503
---

# Error Codes

Portfolio Account business errors are returned with HTTP status `400` and the error code `-9000`.
The `msg` field tells the errors apart.

```javascript
{
  "code": -9000,
  "msg": "Trading team has not enabled API data sharing for this portfolio"
}
```

| HTTP status | Code    | Message                                                            | Meaning                                                                                                                                                                                                                                       |
| ----------- | ------- | ------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 400         | `-9000` | `Not found portfolio info!`                                        | The portfolio information could not be found.                                                                                                                                                                                                 |
| 400         | `-9000` | `You have no holdings in this portfolio`                           | The account that owns the API key holds no allocations in the portfolio. Also returned when a key without the required role is used, for example a sub-account key on a trading-team endpoint, or a trading team key on an investor endpoint. |
| 400         | `-9000` | `Trading team has not enabled API data sharing for this portfolio` | The trading team has disabled API data sharing for this portfolio.                                                                                                                                                                            |

---

# 错误码

投资组合账户的业务错误以 HTTP 状态码 `400` 和错误码 `-9000` 返回，通过 `msg` 字段区分具体错误。

```javascript
{
  "code": -9000,
  "msg": "Trading team has not enabled API data sharing for this portfolio"
}
```

返回的 `msg` 为英文。

| HTTP 状态码 | 错误码  | 返回信息（msg）                                                    | 含义                                                                                                                                              |
| ----------- | ------- | ------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| 400         | `-9000` | `Not found portfolio info!`                                        | 未找到投资组合信息。                                                                                                                              |
| 400         | `-9000` | `You have no holdings in this portfolio`                           | API Key 所属账户在该投资组合中没有持仓。使用不具备所需角色的 Key 时也会返回，例如用子账户 Key 调用交易团队接口，或用交易团队 Key 调用投资人接口。 |
| 400         | `-9000` | `Trading team has not enabled API data sharing for this portfolio` | 交易团队已关闭该投资组合的 API 数据共享。                                                                                                         |