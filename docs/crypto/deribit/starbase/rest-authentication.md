---
exchange: deribit
source_url: https://docs.deribit.com/starbase/rest-authentication
api_type: Starbase
updated_at: 2026-11-28 18:58:41.669143
---

# REST Order Gateway Authentication

> Authenticate requests to the Starbase REST Order Gateway using HTTP Basic credentials, including API key handling and gateway session security.

## Downloads

> [card] OpenAPI Specification
>
> OpenAPI 3.0 specification for the Starbase REST API. Latest version: 2.0
>
> * [Production](https://docs.deribit.com/specifications/starbase_rest_openapi.json)
> * [Testnet](https://docs.deribit.com/specifications/starbase_rest_openapi.json)

Every request to the REST Order Gateway must carry an `Authorization` header. There is no session or token layer. Each request re-authenticates independently.

> [!NOTE]
>
> The REST Order Gateway does not use TLS. Requests are sent over plain HTTP (`http://`). The gateway is reachable only over private, intra-datacenter connectivity (hosted colocation, cross-connect, or AWS Private Link), never the public internet, and omitting TLS removes handshake and encryption overhead from the request path.

## Authorization Header Format

```
Authorization: Basic base64({clientId}:{clientSecret})
```

The header has two parts:

1. The literal prefix `Basic ` (case-sensitive, with a trailing space).
2. Your `clientId` and `clientSecret` joined by a single colon (`:`), then base64-encoded.

### Example

Given these credentials:

| Field | Value |
| - | - |
| Client ID | `atUkltkq` |
| Client Secret | `xn-v4JVKYJxC5v8UgxVvwoBbQ-k_GvkgZFUXJgle3Ow` |

The base64 of `atUkltkq:xn-v4JVKYJxC5v8UgxVvwoBbQ-k_GvkgZFUXJgle3Ow` is `YXRVa2x0a3E6eG4tdjRKVktZSnhDNXY4VWd4VnZ3b0JiUS1rX0d2a2daRlVYSmdsZTNPdw==`, so the header you send is:

```
Authorization: Basic YXRVa2x0a3E6eG4tdjRKVktZSnhDNXY4VWd4VnZ3b0JiUS1rX0d2a2daRlVYSmdsZTNPdw==
```

> [tab] curl
>
> ```bash theme={null}
> curl -X GET "http://195.138.37.137:4410/api/v2/private/cancel_all" \
>   -H "Authorization: Basic $(echo -n 'atUkltkq:xn-v4JVKYJxC5v8UgxVvwoBbQ-k_GvkgZFUXJgle3Ow' | base64)"
> ```

> [tab] Python
>
> ```python theme={null}
> import base64
> import requests
>
> client_id = "atUkltkq"
> client_secret = "xn-v4JVKYJxC5v8UgxVvwoBbQ-k_GvkgZFUXJgle3Ow"
>
> credentials = base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()
> headers = {
>     "Authorization": f"Basic {credentials}"
> }
>
> response = requests.get(
>     "http://195.138.37.137:4410/api/v2/private/cancel_all",
>     headers=headers
> )
> print(response.json())
> ```

> [tab] JavaScript
>
> ```javascript theme={null}
> const clientId = "atUkltkq";
> const clientSecret = "xn-v4JVKYJxC5v8UgxVvwoBbQ-k_GvkgZFUXJgle3Ow";
>
> const credentials = btoa(`${clientId}:${clientSecret}`);
> const response = await fetch("http://195.138.37.137:4410/api/v2/private/cancel_all", {
>   headers: {
>     "Authorization": `Basic ${credentials}`
>   }
> });
> const data = await response.json();
> console.log(data);
> ```

## Error Responses

Any authentication failure returns HTTP `401`. The table below maps each failure cause to its error message:

| Cause | Error message |
| - | - |
| Header missing or not starting with `Basic ` | `Missing or invalid Authorization header` |
| Decoded credential string contains no colon | `Invalid credentials format. Expected clientId:clientSecret` |
| Deribit rejects the credentials | `Authentication failed` |

Treat every `401` as terminal for that request. Retry only after fixing the header or credentials. Do not retry an invalid request blindly.

## Practical Checklist

**1. Use plain HTTP**

The gateway does not terminate TLS. Point clients at `http://` and disable any automatic HTTPS upgrade or certificate verification logic in your HTTP library.

**2. Send the header on every request**

There is no session or token reuse. Every request must include the `Authorization` header.

**3. Base64-encode the credentials**

Concatenate `clientId:clientSecret` with a colon separator, then base64-encode the result. Send that encoded string after `Basic `.

**4. Obtain a Starbase API key**

Any Starbase API key belonging to a direct-access-enabled portfolio can authenticate to the REST Order Gateway. The gateway does not currently enforce API key scopes. A key with any scope can call every REST endpoint, including portfolio management endpoints such as `cancel_all`. Select the **REST** scope when creating the key anyway, as scope enforcement may be introduced in the future. See [Creating a Starbase API Key](https://docs.deribit.com/starbase/creating-api-key.md) for steps.

## Next Steps

> [card] [Creating a Starbase API Key](https://docs.deribit.com/starbase/creating-api-key.md)
>
> Generate credentials for the REST Order Gateway

> [card] [Placing a New Order](https://docs.deribit.com/starbase/placing-new-order.md)
>
> Submit your first order via the REST Order Gateway

> [card] [Rate Limits](https://docs.deribit.com/starbase/api-rate-limits.md)
>
> Per-gateway rate limit rules for REST requests

> [card] [Gateway Connectivity](https://docs.deribit.com/starbase/gateway-connectivity.md)
>
> Gateway addresses, ports, and connection rules


## Related topics

- [Order Management](https://docs.deribit.com/articles/order-management-best-practices.md)
- [Gateway Connectivity](https://docs.deribit.com/starbase/gateway-connectivity.md)
- [Infrastructure, Connectivity & Best Practices](https://docs.deribit.com/starbase/connectivity-best-practices.md)
- [Get Open Orders](https://docs.deribit.com/api-reference/trading/get-open-orders.md)
- [Starbase Connectivity Quickstart](https://docs.deribit.com/starbase/quickstart.md)