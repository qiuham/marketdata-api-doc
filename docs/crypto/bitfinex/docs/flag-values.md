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
source_url: 'https://docs.bitfinex.com/docs/flag-values'
updated_at: 2026-11-26
---

# Flag Values

Orders and Offers can use Flags to indicate different functionalities. Here we list the details of the possible flags values that can be seen or used depending on the interaction.

> 📘 Multiple Flags
>
> You may sum flag values to pass multiple flags. For example passing 4160 (64 + 4096) means hidden post only.\
> Default value is 0.

Order Flags

| Flag         | Type | Value  | Description                                                                                                                                                                                                                  |
| :----------- | :--- | :----- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Hidden       | int  | 64     | The hidden order option ensures an order does not appear in the order book; thus does not influence other market participants.   \n  \nTo toggle 'visible on hit', add a meta object to your order with `{make_visible: 1}`. |
| Close        | int  | 512    | Close position if position present.                                                                                                                                                                                          |
| Reduce Only  | int  | 1024   | Ensures that the executed order does not flip the opened position.                                                                                                                                                           |
| Post Only    | int  | 4096   | The post-only limit order option ensures the limit order will be added to the order book and not match with a pre-existing order unless the pre-existing order is a hidden order.                                            |
| OCO          | int  | 16384  | The one cancels other order option allows you to place a pair of orders stipulating that if one order is executed fully or partially, then the other is automatically canceled.                                              |
| No Var Rates | int  | 524288 | Excludes variable rate funding offers from matching against this order, if on margin                                                                                                                                         |

Offer Flags

| Flag   | Type | Value | Description                                                                                                                    |
| :----- | :--- | :---- | :----------------------------------------------------------------------------------------------------------------------------- |
| Hidden | int  | 64    | The hidden offer option ensures an offer does not appear in the offer book; thus does not influence other market participants. |
