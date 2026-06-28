---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/guides/spot-ws-book-v1
api_type: WebSocket
updated_at: 2026-05-27 19:59:27.689480
---

# Spot Websockets (v1) Book Checksum

This page describes how to maintain the book using the websockets v1 [book](/api/docs/websocket-v1/book) channel.

## Book Updates

Each book update message will have a checksum value appended. The checksum is a CRC32 value based on the top 10 bids and 10 asks, and you can use it to verify that your data is correct and up to date by calculating the checksum independently and comparing it against the value provided.

Checksums will not be sent in book snapshot messages, but rather only in book update messages. In the following sample book update messages, note the checksum field appears in the last bid or ask map structure in the message.

### Example `book` update with asks, bids and checksum
    
    
    [  
        0,  
        {  
            "a": [  
                ["0.05120", "0.00000500", "1582905486.493008"],  
                ["0.05275", "0.00000500", "1582905486.493034"]  
            ]  
        },  
        {  
            "b": [  
                ["0.04765", "0.00000500", "1582905486.493008"],  
                ["0.04940", "0.00000500", "1582905486.493034"]  
            ],  
            "c": "974947235" <-- CRC32 checksum is here.  
        },  
        "book-1000",  
        "BTC/USD"  
    ]  
    

## Book Checksum Calculation

The checksum is computed by concatenating the top 10 bids and asks in the current book and then taking the CRC32 checksum of that string. The price and volume values should be treated as a string and formatted and concatenated as follows.

caution

Processing order is important, the price levels will be received in the correct sequence from the exchange. The last entries in array are the most recent. Do not sort by timestamp, as there can be multiple of price level updates in a microsecond period.

### Example

Consider you are subscribed at depth = 100 on the `book` channel and you receive the following book update message:
    
    
    [ "0.05000", "0.00000304", "1582905487.439814" ]  
    

This update should be processed as follows:

  1. Apply the update to your local 
  2. For each of the top ten ask price levels, sorted by price from low to high:  
a. Remove the decimal character, '.', from the price, i.e. "0.05000" -> "005000".  
b. Remove all leading zero characters from the price. i.e. "005000" -> "5000".  
c. Add the formatted price string to the concatenation.  
d. Repeat steps a-c above but for the volume.

> For example, the price level corresponding to the sample update above would be formatted as "5000304". Note the timestamp values are not used in this calculation.

  3. Repeat the above steps for the top ten bids, sorted by price from high to low.

  4. Feed the concatenated string as input to a CRC32 checksum function, storing the result.

  5. Cast the result (comprising 32 bits) as an unsigned 32-bit integer. This value can now be compared to the checksum received to ensure your local book is accurate. For example, given the following book state:

    
    
    {  
    "as": [  
        [ "0.05005", "0.00000500", "1582905487.684110" ],  
        [ "0.05010", "0.00000500", "1582905486.187983" ],  
        [ "0.05015", "0.00000500", "1582905484.480241" ],  
        [ "0.05020", "0.00000500", "1582905486.645658" ],  
        [ "0.05025", "0.00000500", "1582905486.859009" ],  
        [ "0.05030", "0.00000500", "1582905488.601486" ],  
        [ "0.05035", "0.00000500", "1582905488.357312" ],  
        [ "0.05040", "0.00000500", "1582905488.785484" ],  
        [ "0.05045", "0.00000500", "1582905485.302661" ],  
        [ "0.05050", "0.00000500", "1582905486.157467" ] ],  
    "bs": [  
        [ "0.05000", "0.00000500", "1582905487.439814" ],  
        [ "0.04995", "0.00000500", "1582905485.119396" ],  
        [ "0.04990", "0.00000500", "1582905486.432052" ],  
        [ "0.04980", "0.00000500", "1582905480.609351" ],  
        [ "0.04975", "0.00000500", "1582905476.793880" ],  
        [ "0.04970", "0.00000500", "1582905486.767461" ],  
        [ "0.04965", "0.00000500", "1582905481.767528" ],  
        [ "0.04960", "0.00000500", "1582905487.378907" ],  
        [ "0.04955", "0.00000500", "1582905483.626664" ],  
        [ "0.04950", "0.00000500", "1582905488.509872" ] ]  
    }  
    

The checksum input should be as follows (newlines appear here for convenience only and should not be included):
    
    
    50055005010500501550050205005025500  
    50305005035500504050050455005050500  
    50005004995500499050049805004975500  
    49705004965500496050049555004950500  
    

The final unsigned CRC32 checksum value will then be "974947235".

  * Book Updates
* Example `book` update with asks, bids and checksum
  * Book Checksum Calculation
* Example