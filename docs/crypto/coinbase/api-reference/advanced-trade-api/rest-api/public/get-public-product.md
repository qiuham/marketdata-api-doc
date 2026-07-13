---
exchange: coinbase
source_url: https://docs.cdp.coinbase.com/api-reference/advanced-trade-api/rest-api/public/get-public-product
api_type: Market Data
updated_at: 2026-07-13 19:16:16.783840
---

# Get Public Product

**Endpoint:** `GET https://api.coinbase.com/api/v3/brokerage/market/products/{product_id}`


Get information on a single product by product ID.
    
    
    curl --request GET \
      --url https://api.coinbase.com/api/v3/brokerage/market/products/{product_id} \
      --header 'Authorization: Bearer <token>'
    
    
    import requests  
      
    url = "https://api.coinbase.com/api/v3/brokerage/market/products/{product_id}"  
      
    headers = {"Authorization": "Bearer <token>"}  
      
    response = requests.get(url, headers=headers)  
      
    print(response.text)
    
    
    const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};  
      
    fetch('https://api.coinbase.com/api/v3/brokerage/market/products/{product_id}', options)  
      .then(res => res.json())  
      .then(res => console.log(res))  
      .catch(err => console.error(err));
    
    
    <?php  
      
    $curl = curl_init();  
      
    curl_setopt_array($curl, [  
      CURLOPT_URL => "https://api.coinbase.com/api/v3/brokerage/market/products/{product_id}",  
      CURLOPT_RETURNTRANSFER => true,  
      CURLOPT_ENCODING => "",  
      CURLOPT_MAXREDIRS => 10,  
      CURLOPT_TIMEOUT => 30,  
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,  
      CURLOPT_CUSTOMREQUEST => "GET",  
      CURLOPT_HTTPHEADER => [  
        "Authorization: Bearer <token>"  
      ],  
    ]);  
      
    $response = curl_exec($curl);  
    $err = curl_error($curl);  
      
    curl_close($curl);  
      
    if ($err) {  
      echo "cURL Error #:" . $err;  
    } else {  
      echo $response;  
    }
    
    
    package main  
      
    import (  
    	"fmt"  
    	"net/http"  
    	"io"  
    )  
      
    func main() {  
      
    	url := "https://api.coinbase.com/api/v3/brokerage/market/products/{product_id}"  
      
    	req, _ := http.NewRequest("GET", url, nil)  
      
    	req.Header.Add("Authorization", "Bearer <token>")  
      
    	res, _ := http.DefaultClient.Do(req)  
      
    	defer res.Body.Close()  
    	body, _ := io.ReadAll(res.Body)  
      
    	fmt.Println(string(body))  
      
    }
    
    
    HttpResponse<String> response = Unirest.get("https://api.coinbase.com/api/v3/brokerage/market/products/{product_id}")  
      .header("Authorization", "Bearer <token>")  
      .asString();
    
    
    require 'uri'  
    require 'net/http'  
      
    url = URI("https://api.coinbase.com/api/v3/brokerage/market/products/{product_id}")  
      
    http = Net::HTTP.new(url.host, url.port)  
    http.use_ssl = true  
      
    request = Net::HTTP::Get.new(url)  
    request["Authorization"] = 'Bearer <token>'  
      
    response = http.request(request)  
    puts response.read_body
    
    
    {
      "product_id": "BTC-USD",
      "price": "140.21",
      "price_percentage_change_24h": "9.43%",
      "volume_24h": "1908432",
      "volume_percentage_change_24h": "9.43%",
      "base_increment": "0.00000001",
      "quote_increment": "0.00000001",
      "quote_min_size": "0.00000001",
      "quote_max_size": "1000",
      "base_min_size": "0.00000001",
      "base_max_size": "1000",
      "base_name": "Bitcoin",
      "quote_name": "US Dollar",
      "watched": true,
      "is_disabled": false,
      "new": true,
      "status": "<string>",
      "cancel_only": true,
      "limit_only": true,
      "post_only": true,
      "trading_disabled": false,
      "auction_mode": true,
      "base_display_symbol": "BTC",
      "quote_display_symbol": "USD",
      "product_type": "UNKNOWN_PRODUCT_TYPE",
      "quote_currency_id": "USD",
      "base_currency_id": "BTC",
      "fcm_trading_session_details": {
        "is_session_open": true,
        "open_time": "<string>",
        "close_time": "<string>",
        "session_state": "FCM_TRADING_SESSION_STATE_UNDEFINED",
        "after_hours_order_entry_disabled": true,
        "closed_reason": "FCM_TRADING_SESSION_CLOSED_REASON_UNDEFINED",
        "maintenance": {
          "start_time": "<string>",
          "end_time": "<string>"
        }
      },
      "mid_market_price": "140.22",
      "alias": "BTC-USD",
      "alias_to": [
        "BTC-USDC"
      ],
      "view_only": true,
      "price_increment": "0.00000001",
      "display_name": "BTC PERP",
      "product_venue": "neptune",
      "approximate_quote_24h_volume": "1908432",
      "new_at": "2021-07-01T00:00:00.000Z",
      "market_cap": "1500000000000",
      "icon_color": "red",
      "icon_url": "https://metadata.cbhq.net/equity_icons/123456789.png",
      "display_name_overwrite": "Bitcoin Perpetual",
      "is_alpha_testing": false,
      "about_description": "nano Crude Oil Futures is a monthly cash-settled contract that allows participants to manage risk, trade on margin, or speculate on the price of oil.",
      "best_bid_price": "<string>",
      "best_ask_price": "<string>",
      "future_product_details": {
        "venue": "<string>",
        "contract_code": "<string>",
        "contract_expiry": "<string>",
        "contract_size": "<string>",
        "contract_root_unit": "<string>",
        "group_description": "<string>",
        "contract_expiry_timezone": "<string>",
        "group_short_description": "<string>",
        "risk_managed_by": "UNKNOWN_RISK_MANAGEMENT_TYPE",
        "contract_expiry_type": "UNKNOWN_CONTRACT_EXPIRY_TYPE",
        "perpetual_details": {
          "open_interest": "<string>",
          "funding_rate": "<string>",
          "funding_time": "<string>",
          "max_leverage": "<string>",
          "base_asset_uuid": "<string>",
          "underlying_type": "<string>"
        },
        "contract_display_name": "<string>",
        "time_to_expiry_ms": "<string>",
        "non_crypto": true,
        "contract_expiry_name": "<string>",
        "twenty_four_by_seven": true,
        "funding_interval": "<string>",
        "open_interest": "<string>",
        "funding_rate": "<string>",
        "funding_time": "<string>",
        "display_name": "<string>",
        "region_enabled": {},
        "intraday_margin_rate": {
          "long_margin_rate": "0.5",
          "short_margin_rate": "0.5"
        },
        "overnight_margin_rate": {
          "long_margin_rate": "0.5",
          "short_margin_rate": "0.5"
        },
        "settlement_price": "<string>",
        "futures_asset_type": "UNKNOWN_FUTURES_ASSET_TYPE",
        "index_price": "<string>",
        "contract_code_display_name": "<string>",
        "product_group_cbrn": "<string>"
      }
    }
    
    
    {  
      "error": "<string>",  
      "code": 123,  
      "message": "<string>",  
      "details": [  
        {  
          "type_url": "<string>",  
          "value": "aSDinaTvuI8gbWludGxpZnk="  
        }  
      ]  
    }

#### Authorizations

Authorization

string

header

required

A JWT signed using your CDP API Key Secret, encoded in base64. Refer to the [Creating API Keys](/coinbase-app/authentication-authorization/api-key-authentication) section of our Coinbase App Authentication docs for information on how to generate your Bearer Token.

#### Path Parameters

product_id

string

required

The trading pair (e.g. 'BTC-USD').

#### Response

A successful response.

product_id

string

required

The trading pair (e.g. 'BTC-USD').

Example:

`"BTC-USD"`

price

string

required

The current price for the product, in quote currency.

Example:

`"140.21"`

price_percentage_change_24h

string

required

The amount the price of the product has changed, in percent, in the last 24 hours.

Example:

`"9.43%"`

volume_24h

string

required

The trading volume for the product in the last 24 hours.

Example:

`"1908432"`

volume_percentage_change_24h

string

required

The amount the volume of the product has changed, in percent, in the last 24 hours.

Example:

`"9.43%"`

base_increment

string

required

Minimum amount base value can be increased or decreased at once.

Example:

`"0.00000001"`

quote_increment

string

required

Minimum amount quote value can be increased or decreased at once.

Example:

`"0.00000001"`

quote_min_size

string

required

Minimum size that can be represented of quote currency.

Example:

`"0.00000001"`

quote_max_size

string

required

Maximum size that can be represented of quote currency.

Example:

`"1000"`

base_min_size

string

required

Minimum size that can be represented of base currency.

Example:

`"0.00000001"`

base_max_size

string

required

Maximum size that can be represented of base currency.

Example:

`"1000"`

base_name

string

required

Name of the base currency.

Example:

`"Bitcoin"`

quote_name

string

required

Name of the quote currency.

Example:

`"US Dollar"`

watched

boolean

required

Whether or not the product is on the user's watchlist.

Example:

`true`

is_disabled

boolean

required

Whether or not the product is disabled for trading.

Example:

`false`

new

boolean

required

Whether or not the product is 'new'.

Example:

`true`

status

string

required

Status of the product.

cancel_only

boolean

required

Whether or not orders of the product can only be cancelled, not placed or edited.

Example:

`true`

limit_only

boolean

required

Whether or not orders of the product can only be limit orders, not market orders.

Example:

`true`

post_only

boolean

required

Whether or not orders of the product can only be posted, not cancelled.

Example:

`true`

trading_disabled

boolean

required

Whether or not the product is disabled for trading for all market participants.

Example:

`false`

auction_mode

boolean

required

Whether or not the product is in auction mode.

Example:

`true`

base_display_symbol

string

required

Symbol of the base display currency.

Example:

`"BTC"`

quote_display_symbol

string

required

Symbol of the quote display currency.

Example:

`"USD"`

product_type

enum<string>

default:UNKNOWN_PRODUCT_TYPE

Type of the product.

Available options:

`UNKNOWN_PRODUCT_TYPE`,

`SPOT`,

`FUTURE`

quote_currency_id

string

Symbol of the quote currency.

Example:

`"USD"`

base_currency_id

string

Symbol of the base currency.

Example:

`"BTC"`

fcm_trading_session_details

object

mid_market_price

string

The current midpoint of the bid-ask spread, in quote currency.

Example:

`"140.22"`

alias

string

Product id for the corresponding unified book.

Example:

`"BTC-USD"`

alias_to

string[]

Product ids that this product serves as an alias for.

Example:
    
    
    ["BTC-USDC"]

view_only

boolean

Reflects whether an FCM product has expired. For SPOT, set get_tradability_status to get a return value here. Defaulted to false for all other product types.

Example:

`true`

price_increment

string

Minimum amount price can be increased or decreased at once.

Example:

`"0.00000001"`

display_name

string

Display name for the product e.g. BTC-PERP-INTX => BTC PERP

Example:

`"BTC PERP"`

product_venue

enum<string>

default:UNKNOWN_VENUE_TYPE

The sole venue id for the product. Defaults to CBE if the product is not specific to a single venue

Available options:

`UNKNOWN_VENUE_TYPE`,

`CBE`,

`FCM`,

`INTX`

Example:

`"neptune"`

approximate_quote_24h_volume

string

The approximate trading volume for the product in the last 24 hours based on the current quote.

Example:

`"1908432"`

new_at

string<RFC3339 Timestamp>

The timestamp when the product was listed. This is only populated if product has new tag.

Example:

`"2021-07-01T00:00:00.000Z"`

market_cap

string

The market capitalization of the product's base asset.

Example:

`"1500000000000"`

icon_color

string

color for icon display

Example:

`"red"`

icon_url

string

A URL to the icon image.

Example:

`"https://metadata.cbhq.net/equity_icons/123456789.png"`

display_name_overwrite

string

An alternative name to display for the product.

Example:

`"Bitcoin Perpetual"`

is_alpha_testing

boolean

flag for alpha user testing

Example:

`false`

about_description

string

description used in about section for an asset

Example:

`"nano Crude Oil Futures is a monthly cash-settled contract that allows participants to manage risk, trade on margin, or speculate on the price of oil."`

best_bid_price

string

best_ask_price

string

future_product_details

object