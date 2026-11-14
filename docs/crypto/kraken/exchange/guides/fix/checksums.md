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
source_url: 'https://docs.kraken.com/exchange/guides/fix/checksums'
updated_at: 2026-11-13
---

# Book checksum (FIX)

> How to maintain the order book and validate the CRC32 checksum on the FIX Market Data Incremental Refresh

The [Market Data Incremental Refresh](https://docs.kraken.com/exchange/api-reference/unified-fix/mdir.md) message includes a CRC32 checksum (tag `5041`) with each update. Validating it confirms your local book is correctly synchronised with the exchange.

The checksum is always calculated over the **top 10 price levels** regardless of subscription depth. Process all updates in a message before calculating the checksum.

## Book maintenance

Each entry in the [Market Data Incremental Refresh](https://docs.kraken.com/exchange/api-reference/unified-fix/mdir.md) carries an update action:

| Action | Meaning |
| :- | :- |
| New (`279=0`) | A new price level was added |
| Update (`279=1`) | The quantity at a price level changed |
| Delete (`279=2`) | A price level was removed |

## Checksum calculation

Prices and quantities in the FIX feed are sent as floats. To compute the checksum correctly, you must first determine the precision for each instrument from an [Security List Request](https://docs.kraken.com/exchange/api-reference/unified-fix/slr.md).

### Step 1 — get instrument precision

Send a Security List Request for the instrument:

```text theme={null}
8=FIX.4.4|9=90|35=x|34=3|49=CLIENT|52=20231012-09:54:15.316|56=KRAKEN-MD|55=BTC/USD|320=SLS1000002|559=0|10=026|
```

The Security List response includes two precision fields:

```text theme={null}
8=FIX.4.4|9=177|35=y|49=KRAKEN-MD|56=CLIENT|34=3|52=20231012-09:54:15.317|320=SLS1000002|322=1697104455317568799|560=0|146=1|55=BTC/USD|562=0.00000001|5010=8|5011=0.0001|2349=1|5022=0.1|5032=1|10=068|
```

> [!NOTE]
>
> The two fields you need for checksum calculation:
>
> * `2349=1` — price precision is 1 decimal place
> * `5010=8` — quantity precision is 8 decimal places
>
> Store these values. They apply to all subsequent Market Data messages for this instrument.

### Step 2 — subscribe and receive snapshot

Subscribe to Market Data for depth 10:

```text theme={null}
8=FIX.4.4|9=124|35=V|34=6|49=CLIENT|52=20231012-09:54:15.316|56=KRAKEN-MD|146=1|55=BTC/USD|262=0|263=1|264=10|265=1|267=3|269=1|269=0|269=2|10=170|
```

The [Market Data Full Refresh](https://docs.kraken.com/exchange/api-reference/unified-fix/mdsfr.md) response establishes your initial book state. No checksum is provided on the snapshot — only on subsequent incremental updates.

### Step 3 — calculate checksum on each incremental update

**1. Apply the update**

Apply all entries in the [Market Data Incremental Refresh](https://docs.kraken.com/exchange/api-reference/unified-fix/mdir.md) to your local book before calculating the checksum.

**2. Build the asks string**

For each of the top 10 ask price levels, sorted by price **low to high**:

* Format the price using the instrument's price precision → `28013.0` → `"28013.0"`
* Remove `.` → `"280130"`
* Remove leading zeros → `"280130"`
* Format the quantity using the instrument's quantity precision → `0.00096506` → `"0.00096506"`
* Remove `.` → `"000096506"`
* Remove leading zeros → `"96506"`
* Append `price + qty` to the asks string → `"28013096506"`

**3. Build the bids string**

For each of the top 10 bid price levels, sorted by price **high to low**, apply the same formatting and append to the bids string.

**4. Concatenate and hash**

Concatenate **asks + bids** strings, then pass the result to a CRC32 function. Cast the result to an unsigned 32-bit integer and compare to tag `5041` in the message.

### Example

Incremental update received:

```text theme={null}
8=FIX.4.4|9=167|35=X|34=12|49=KRAKEN-MD|52=20231012-09:55:14.934|56=CLIENT|55=BTC/USD|262=0|268=1|279=1|269=1|278=O28013.0|270=28013.0|271=0.00096506|273=09:55:15.071|5041=3341325816|10=090|
```

Asks string (low → high, price precision=1, qty precision=8):

```text theme={null}
28013096506280398100000280665100000280933100000281200100000281467100000281735100000282002100000282270100000282537100000
```

Bids string (high → low):

```text theme={null}
28003010000027999996375279699738604232770013500002757323200002713741000000270913400000267294100000267026100000266759100000
```

Concatenated input to CRC32:

```text theme={null}
2801309650628039810000028066510000028093310000028120010000028146710000028173510000028200210000028227010000028253710000028003010000027999996375279699738604232770013500002757323200002713741000000270913400000267294100000267026100000266759100000
```

Expected result: **`3341325816`**
