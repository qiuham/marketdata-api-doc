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
source_url: 'https://docs.kraken.com/institutional/api-reference/prime-fix/ocrej'
updated_at: 2026-11-13
---

# Order Cancel Reject

> Response message used to reject invalid order cancel or cancel/replace requests.

The OrderCancelReject message is used to reject invalid cancel or cancel/replace requests.

> [tab] FIX Specification
>
> **header** *required*
>
> MsgType `9`
>
> **11 - ClOrdID** `string` *required*
>
> ClOrdID(11) which could not be canceled/replaced.
>
> **41 - OrigClOrdID** `string` *required*
>
> ClOrdID of the previous accepted order.
>
> **37 - OrderID** `string` *required*
>
> Unique identifier of most recent order as assigned by Customer. If CxlRejReason="Unknown order", then will be "NONE".
>
> **60 - TransactTime** `string`
>
> Business timestamp for this reject. Format: YYYYMMDD-HH:MM:SS.uuu
>
> **39 - OrdStatus** `integer` *required*
>
> Identifies current status of order.
>
> <ul>
>   \*\*Possible values: \*\*
>   <li>`0` : New</li>
>   <li>`1` : Partially filled</li>
>   <li>`2` : Filled</li>
>   <li>`4` : Canceled</li>
>   <li>`6` : Pending Cancel (i.e. result of Order Cancel Request)</li>
>   <li>`8` : Rejected</li>
>   <li>`A` : Pending New</li>
>   <li>`E` : Pending Replace (i.e. result of Order Cancel/Replace Request)</li>
> </ul>
>
> **434 - CxlRejResponseTo** `integer` *required*
>
> Identifies the type of request that a Cancel Reject is in response to.
>
> <ul>
>   \*\*Possible values: \*\*
>   <li>`1` : Order cancel request</li>
>   <li>`2` : Order cancel/replace request</li>
> </ul>
>
> **102 - CxlRejReason** `integer`
>
> Code to identify reason for cancel rejection.
>
> <ul>
>   \*\*Possible values: \*\*
>   <li>`0` : Too late to cancel</li>
>   <li>`1` : Unknown order</li>
>   <li>`2` : Broker / Exchange Option</li>
>   <li>`3` : Order already in Pending Cancel or Pending Replace status</li>
> </ul>
>
> **58 - Text** `string`
>
> Free-format text string.
>
> **trailer** *required*
