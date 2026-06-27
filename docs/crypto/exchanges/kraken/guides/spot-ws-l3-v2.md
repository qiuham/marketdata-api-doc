---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/guides/spot-ws-l3-v2
api_type: WebSocket
updated_at: 2026-05-27 19:59:48.859862
---

# Spot Websockets (v2) Level3 Checksum

This page describes how to maintain the book and generate the checksum for the websockets (v2) [level3](/api/docs/websocket-v2/level3) channel. The feed describes the individual orders at each price level.

The checksum verification is optional. It provides an additional check that the client 
The mechanisms for generating the checksum are very similar between `book` and `level3` feeds. The `level3` feed has an extra level of granularity (i.e. the orders at each price level), the checksum takes this into account and also verifies the sequence of orders in the book (i.e. queue priority).

The checksum is only calculated for the top 10 price levels of the book regardless of the subscription depth.

## Maintaining the `level3` Channel

All orders in a `level3` message should be processed before the checksum is calculated. An update message may contain many updates to either the bids and/or asks.

A price level with no orders or no order quantity should be removed from your book. Note, if a price level is removed from the subscribed levels (i.e. result of trades/cancels) then all the orders at the next available price level will be published to keep the subscription depth at the specified number of levels.

Additionally, after each update, the book should be truncated to your subscribed depth. In other words, if you are subscribed with `"depth": 10` and an insert into the middle of the book results in you having 11 bids, you must remove the 11th worst bid.

## Checksum Calculation

The level3 checksum logic is similar to level2 [book](/api/docs/guides/spot-ws-book-v2) logic. The primary difference, level3 checksum will iterate through the orders in the price levels.

The `limit_price` and `order_qty` fields are pushed onto the wire containing full precision.

tip

To keep the full precision through deserialization and decoding, parse the `level3` message using a decimal (or string decoder) for the prices and quantities.

Example code for decoding message with full precision:
    
    
        async for bytes in websocket:  
            message = json.loads(bytes, parse_float=Decimal)  
            self.on_message(message)  
    

### Checksum Steps with Example

This example data below can be used as input to your l3 book checksum calculator to confirm correct behaviour.

**Example** : Generating a `level3` snapshot checksum (using json string decoder):
    
    
    {  
       "channel": "level3",  
       "type": "snapshot",  
       "data": [  
          {  
             "symbol": "BTC/USD",  
             "checksum": 1063832831,  
             "bids": [  
                {  
                   "order_id": "OTCFZG-YOE2Q-LQKNM3",  
                   "limit_price": "44939.4",  
                   "order_qty": "0.88968699",  
                   "timestamp": "2024-01-08T12:26:39.526146327Z"  
                },  
                {  
                   "order_id": "OFGP5R-B3E7G-54EZD6",  
                   "limit_price": "44939.4",  
                   "order_qty": "0.45210000",  
                   "timestamp": "2024-01-08T12:26:39.530287934Z"  
                },  
                {  
                   "order_id": "OMPHVY-IZPJ4-KOKA3P",  
                   "limit_price": "44939.4",  
                   "order_qty": "0.10000000",  
                   "timestamp": "2024-01-08T12:26:39.576380340Z"  
                },  
                {  
                   "order_id": "OAI5QZ-AMPLW-NBNO72",  
                   "limit_price": "44939.4",  
                   "order_qty": "0.14296323",  
                   "timestamp": "2024-01-08T12:26:39.602118534Z"  
                },  
                {  
                   "order_id": "O7VFZI-CTFWH-FF6EIR",  
                   "limit_price": "44939.4",  
                   "order_qty": "0.25000000",  
                   "timestamp": "2024-01-08T12:26:41.780601700Z"  
                },  
                {  
                   "order_id": "O472V3-ZG4EZ-OLD66C",  
                   "limit_price": "44939.4",  
                   "order_qty": "0.10292988",  
                   "timestamp": "2024-01-08T12:26:43.087136366Z"  
                },  
                {  
                   "order_id": "OEK26P-BGPUK-LDHMD2",  
                   "limit_price": "44939.4",  
                   "order_qty": "0.33880000",  
                   "timestamp": "2024-01-08T12:26:43.822433365Z"  
                },  
                {  
                   "order_id": "OSMYPE-S5VOC-YSS3WM",  
                   "limit_price": "44939.4",  
                   "order_qty": "1.28140860",  
                   "timestamp": "2024-01-08T12:26:45.066096694Z"  
                },  
                {  
                   "order_id": "OJPMIN-NXZL5-SOWP6V",  
                   "limit_price": "44937.1",  
                   "order_qty": "0.03346877",  
                   "timestamp": "2024-01-08T12:26:39.691304329Z"  
                },  
                {  
                   "order_id": "O6PUGE-SQWYQ-TRJEEE",  
                   "limit_price": "44934.7",  
                   "order_qty": "0.35630000",  
                   "timestamp": "2024-01-08T12:26:44.129718463Z"  
                },  
                {  
                   "order_id": "OPUOGC-Q532V-3OKLPM",  
                   "limit_price": "44930.2",  
                   "order_qty": "0.22734299",  
                   "timestamp": "2024-01-08T12:26:30.769031831Z"  
                },  
                {  
                   "order_id": "OCIU7J-VB3CI-HPULSF",  
                   "limit_price": "44930.2",  
                   "order_qty": "0.01000000",  
                   "timestamp": "2024-01-08T12:26:36.054352106Z"  
                },  
                {  
                   "order_id": "ORWVAF-LJFLY-ZWEHDQ",  
                   "limit_price": "44930.2",  
                   "order_qty": "0.05550000",  
                   "timestamp": "2024-01-08T12:26:36.635882793Z"  
                },  
                {  
                   "order_id": "OYRAHE-PI5AN-7KOQ4E",  
                   "limit_price": "44930.2",  
                   "order_qty": "0.70000000",  
                   "timestamp": "2024-01-08T12:26:37.296554518Z"  
                },  
                {  
                   "order_id": "OGBHYU-UILDD-6DLLYJ",  
                   "limit_price": "44930.2",  
                   "order_qty": "0.15000000",  
                   "timestamp": "2024-01-08T12:26:41.222733191Z"  
                },  
                {  
                   "order_id": "O74ZBU-K2TKC-R76XSW",  
                   "limit_price": "44928.0",  
                   "order_qty": "0.00105240",  
                   "timestamp": "2024-01-08T12:26:23.542563322Z"  
                },  
                {  
                   "order_id": "OQVTQF-Y56MR-BM6LWL",  
                   "limit_price": "44919.6",  
                   "order_qty": "0.33870000",  
                   "timestamp": "2024-01-08T12:26:42.808132842Z"  
                },  
                {  
                   "order_id": "OYEH6U-ZCHA2-3HFR3W",  
                   "limit_price": "44919.5",  
                   "order_qty": "0.07610000",  
                   "timestamp": "2024-01-08T12:26:34.269600037Z"  
                },  
                {  
                   "order_id": "OLGPG7-HVKXU-J6SANK",  
                   "limit_price": "44912.0",  
                   "order_qty": "0.35630000",  
                   "timestamp": "2024-01-08T12:26:34.961292766Z"  
                },  
                {  
                   "order_id": "OHGC3L-FRZQ3-UIVZRU",  
                   "limit_price": "44909.7",  
                   "order_qty": "0.06690000",  
                   "timestamp": "2024-01-08T12:26:31.912880024Z"  
                },  
                {  
                   "order_id": "O73C6Y-VZXYA-H4LDFY",  
                   "limit_price": "44901.9",  
                   "order_qty": "0.00088982",  
                   "timestamp": "2024-01-08T12:26:42.883315043Z"  
                }  
             ],  
             "asks": [  
                {  
                   "order_id": "OFVLAA-HRSSP-BK75KB",  
                   "limit_price": "44939.5",  
                   "order_qty": "4.52308393",  
                   "timestamp": "2024-01-08T12:18:05.770906486Z"  
                },  
                {  
                   "order_id": "OYBAMK-O5DKX-WMPUTM",  
                   "limit_price": "44939.5",  
                   "order_qty": "0.00111261",  
                   "timestamp": "2024-01-08T12:18:12.847426441Z"  
                },  
                {  
                   "order_id": "O3DRCT-J5M2S-KYV526",  
                   "limit_price": "44939.5",  
                   "order_qty": "0.00100000",  
                   "timestamp": "2024-01-08T12:26:42.108176464Z"  
                },  
                {  
                   "order_id": "OF3X3A-72WZY-6EKA5F",  
                   "limit_price": "44939.5",  
                   "order_qty": "0.01000000",  
                   "timestamp": "2024-01-08T12:26:43.955098263Z"  
                },  
                {  
                   "order_id": "OF5UA6-6IIZ2-YGQTSJ",  
                   "limit_price": "44950.0",  
                   "order_qty": "0.10334926",  
                   "timestamp": "2024-01-08T12:25:52.800473795Z"  
                },  
                {  
                   "order_id": "OSDOZX-7UZ6Y-QDNPVI",  
                   "limit_price": "44953.0",  
                   "order_qty": "0.00064537",  
                   "timestamp": "2024-01-08T12:24:58.086806970Z"  
                },  
                {  
                   "order_id": "OV7KTS-A2TWV-3XKRIA",  
                   "limit_price": "44955.0",  
                   "order_qty": "0.00250000",  
                   "timestamp": "2024-01-08T12:21:52.257936228Z"  
                },  
                {  
                   "order_id": "OOF2V5-RYOHC-GLRNPM",  
                   "limit_price": "44959.6",  
                   "order_qty": "0.35630000",  
                   "timestamp": "2024-01-08T12:26:44.202823127Z"  
                },  
                {  
                   "order_id": "OTVOVS-QLST3-3JG7JI",  
                   "limit_price": "44959.6",  
                   "order_qty": "0.35630000",  
                   "timestamp": "2024-01-08T12:26:44.203383999Z"  
                },  
                {  
                   "order_id": "OGZCIU-RDQ77-DAAL3P",  
                   "limit_price": "44960.1",  
                   "order_qty": "0.00338072",  
                   "timestamp": "2024-01-08T12:26:42.724829715Z"  
                },  
                {  
                   "order_id": "OVLG3E-HYBQM-CWNGCY",  
                   "limit_price": "44960.2",  
                   "order_qty": "0.88967575",  
                   "timestamp": "2024-01-08T12:26:12.935924248Z"  
                },  
                {  
                   "order_id": "OWEOFO-HUCJC-T37MVO",  
                   "limit_price": "44967.0",  
                   "order_qty": "3.14392283",  
                   "timestamp": "2024-01-08T12:26:39.474431925Z"  
                },  
                {  
                   "order_id": "OVYTHY-D2N76-5QYREQ",  
                   "limit_price": "44978.5",  
                   "order_qty": "0.06778960",  
                   "timestamp": "2024-01-08T12:26:41.229379178Z"  
                },  
                {  
                   "order_id": "OFO525-PHRVS-236RMN",  
                   "limit_price": "44979.2",  
                   "order_qty": "0.35630000",  
                   "timestamp": "2024-01-08T12:26:20.271584488Z"  
                }  
             ]  
          }  
       ]  
    }  
    

#### Generate Checksum String

The checksum is generated by iterating through the top 10 price levels in each side of book to generate a string representation, then passing this string to a CRC32 checksum function. The final checksum is a integer value.

1, Generate formatted string for each price level in the **asks** (sorted by price from low to high), then iterating through each order in a price level:

  * Remove the decimal character, '.', from the `limit_price`, i.e. "44939.5" -> "449395".
  * Remove all leading zero characters from the `limit_price`. i.e. "449395" -> "449395".
  * Remove the decimal character, '.', from the `order_qty`, i.e. "4.52308393" -> "452308393".
  * Remove all leading zero characters from the `order_qty`. i.e. "452308393" -> "452308393".
  * Add the `limit_price` \+ `order_qty` (`449395452308393`) string to the **asks** concatenation.
  * Repeat for the remaining 9 price levels.

    
    
    44939545230839344939511126144939510000044939510000004495001033492644953064537449550250000449596356300004495963563000044960133807244960288967575449670314392283449785677896044979235630000  
    

2, Generate formatted string for each price level in the **bids** (sorted by price from high to low), then iterating through each order in a price level:

  * Remove the decimal character, '.', from the `limit_price`, i.e. "44939.4" -> "449394".
  * Remove all leading zero characters from the `limit_price`. i.e. "449394" -> "449394".
  * Remove the decimal character, '.', from the `order_qty`, i.e. "0.88968699" -> "088968699".
  * Remove all leading zero characters from the `order_qty`. i.e. "088968699" -> "88968699".
  * Add the `limit_price` \+ `order_qty` (`44939488968699`) string to the **bids** concatenation.
  * Repeat for the remaining 9 price levels.

    
    
    449394889686994493944521000044939410000000449394142963234493942500000044939410292988449394338800004493941281408604493713346877449347356300004493022273429944930210000004493025550000449302700000004493021500000044928010524044919633870000449195761000044912035630000449097669000044901988982  
    

#### Generate Integer Value from Checksum String

3, Concatenate the generated **asks** \+ **bids** strings.
    
    
    44939545230839344939511126144939510000044939510000004495001033492644953064537449550250000449596356300004495963563000044960133807244960288967575449670314392283449785677896044979235630000449394889686994493944521000044939410000000449394142963234493942500000044939410292988449394338800004493941281408604493713346877449347356300004493022273429944930210000004493025550000449302700000004493021500000044928010524044919633870000449195761000044912035630000449097669000044901988982  
    

4, Feed the concatenated string as input to a CRC32 checksum function.
    
    
    1063832831  
    

This value can now be compared to the checksum received to ensure your local book is accurate.

Optionally, depending on the CRC32 checksum function, the result may need to be cast to unsigned 32-bit integer.

  * Maintaining the `level3` Channel
  * Checksum Calculation
* Checksum Steps with Example