---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/guides/spot-errors
api_type: Guide
updated_at: 2026-05-27 19:58:23.431750
---

# Spot Error Messages

The following error messages may be thrown for private data requests.

### Some Common Examples

Error| Additional Info  
---|---  
EGeneral:Invalid arguments| The request payload is malformed, incorrect or ambiguous  
EGeneral:Invalid arguments:Index unavailable| Index pricing is unavailable for stop/profit orders on this pair  
EGeneral:Temporary lockout| Too many sequential EAPI:Invalid key errors  
EService:Unavailable| The matching engine or API is offline  
EService:Market in cancel_only mode| Request can't be made at this time (See `SystemStatus` endpoint)  
EService:Market in post_only mode| Request can't be made at this time (See `SystemStatus` endpoint)  
EService:Deadline elapsed| The request timed out according to the default or specified `deadline`  
EAPI:Invalid key| An invalid `API-Key` header was supplied (see Authentication section)  
EAPI:Invalid signature| An invalid `API-Sign` header was supplied (see Authentication section)  
EAPI:Invalid nonce| An invalid `nonce` was supplied (see Authentication section)  
EGeneral:Permission denied| API key doesn't have permission to make this request  
EGeneral:Internal error[:<code>]| Internal Support. Please contact support.  
EOrder:Cannot open opposing position| User/tier is ineligible for margin trading  
EOrder:Cannot open position| User/tier is ineligible for margin trading  
EOrder:Margin allowance exceeded| User has exceeded their margin allowance  
EOrder:Margin level too low| Client has insufficient equity or collateral  
EOrder:Margin position size exceeded| Client would exceed the maximum position size for this pair  
EOrder:Insufficient margin| Exchange does not have available funds for this margin trade  
EOrder:Insufficient funds| Client does not have the necessary funds  
EOrder:Order minimum not met| Order size does not meet `ordermin` (See `AssetPairs` endpoint)  
EOrder:Cost minimum not met| Cost (price * volume) does not meet `costmin` (See `AssetPairs` endpoint)  
EOrder:Tick size check failed| Price submitted is not a valid multiple of the pair's tick_size (See `AssetPairs` endpoint)  
EOrder:Orders limit exceeded| See [Rate Limits](/api/docs/guides/spot-rest-ratelimits) section  
EOrder:Rate limit exceeded| See [Rate Limits](/api/docs/guides/spot-rest-ratelimits) section  
EOrder:Invalid price|   
EOrder:Domain rate limit exceeded| See [Rate Limits](/api/docs/guides/spot-rest-ratelimits) section  
EOrder:Positions limit exceeded|   
EOrder:Reduce only:Non-PC|   
EOrder:Reduce only:No position exists| When trying to submit a reduce-only order (new or via trigger) for a market that has no open positions  
EOrder:Reduce only:Position is closed| When submitting a reduce-only order that would flip a position, order will match as much as possible and cancel back the rest with this error  
EOrder:Scheduled orders limit exceeded|   
EOrder:Unknown position|   
EAccount:Invalid permissions|   
EAuth:Account temporary disabled|   
EAuth:Account unconfirmed|   
EAuth:Rate limit exceeded|   
EAuth:Too many requests|   
ETrade:Invalid request|   
EBM:limit exceeded:CAL| Exceeded [Canadian Acquisition Limits (CAL)](https://support.kraken.com/hc/en-us/articles/15568473780628-CAD-net-purchase-limits-for-certain-cryptocurrencies-in-Canada)  
EFunding:Max fee exceeded| Processed fee exceeds `max_fee` set in `Withdraw` request  
* Some Common Examples