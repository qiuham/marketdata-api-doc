---
exchange: coinbase
source_url: https://docs.cdp.coinbase.com/api-reference/advanced-trade-api/rest-api/orders/list-orders
api_type: Trading
updated_at: 2026-07-19 19:04:06.767041
---

# List Orders

**Endpoint:** `GET https://api.coinbase.com/api/v3/brokerage/orders/historical/batch`


Get a list of orders filtered by optional query parameters (`product_id`, `order_status`, etc).
    
    
    curl --request GET \
      --url https://api.coinbase.com/api/v3/brokerage/orders/historical/batch \
      --header 'Authorization: Bearer <token>'
    
    
    import requests  
      
    url = "https://api.coinbase.com/api/v3/brokerage/orders/historical/batch"  
      
    headers = {"Authorization": "Bearer <token>"}  
      
    response = requests.get(url, headers=headers)  
      
    print(response.text)
    
    
    const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};  
      
    fetch('https://api.coinbase.com/api/v3/brokerage/orders/historical/batch', options)  
      .then(res => res.json())  
      .then(res => console.log(res))  
      .catch(err => console.error(err));
    
    
    <?php  
      
    $curl = curl_init();  
      
    curl_setopt_array($curl, [  
      CURLOPT_URL => "https://api.coinbase.com/api/v3/brokerage/orders/historical/batch",  
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
      
    	url := "https://api.coinbase.com/api/v3/brokerage/orders/historical/batch"  
      
    	req, _ := http.NewRequest("GET", url, nil)  
      
    	req.Header.Add("Authorization", "Bearer <token>")  
      
    	res, _ := http.DefaultClient.Do(req)  
      
    	defer res.Body.Close()  
    	body, _ := io.ReadAll(res.Body)  
      
    	fmt.Println(string(body))  
      
    }
    
    
    HttpResponse<String> response = Unirest.get("https://api.coinbase.com/api/v3/brokerage/orders/historical/batch")  
      .header("Authorization", "Bearer <token>")  
      .asString();
    
    
    require 'uri'  
    require 'net/http'  
      
    url = URI("https://api.coinbase.com/api/v3/brokerage/orders/historical/batch")  
      
    http = Net::HTTP.new(url.host, url.port)  
    http.use_ssl = true  
      
    request = Net::HTTP::Get.new(url)  
    request["Authorization"] = 'Bearer <token>'  
      
    response = http.request(request)  
    puts response.read_body
    
    
    {
      "orders": [
        {
          "order_id": "0000-000000-000000",
          "product_id": "BTC-USD",
          "user_id": "2222-000000-000000",
          "order_configuration": {
            "market_market_ioc": {
              "quote_size": "10.00",
              "base_size": "0.001",
              "rfq_disabled": true
            },
            "market_market_fok": {
              "quote_size": "10.00",
              "base_size": "0.001",
              "rfq_disabled": true
            },
            "sor_limit_ioc": {
              "quote_size": "10.00",
              "base_size": "0.001",
              "limit_price": "10000.00",
              "rfq_disabled": true
            },
            "limit_limit_gtc": {
              "quote_size": "10.00",
              "base_size": "0.001",
              "limit_price": "10000.00",
              "post_only": false,
              "rfq_disabled": true
            },
            "limit_limit_gtd": {
              "quote_size": "10.00",
              "base_size": "0.001",
              "limit_price": "10000.00",
              "end_time": "2021-05-31T09:59:59.000Z",
              "post_only": false
            },
            "limit_limit_fok": {
              "quote_size": "10.00",
              "base_size": "0.001",
              "limit_price": "10000.00",
              "rfq_disabled": true
            },
            "twap_limit_gtd": {
              "quote_size": "10.00",
              "base_size": "0.001",
              "start_time": "2021-05-31T07:59:59.000Z",
              "end_time": "2021-05-31T09:59:59.000Z",
              "limit_price": "10000.00",
              "number_buckets": "5",
              "bucket_size": "2.00",
              "bucket_duration": "300s"
            },
            "stop_limit_stop_limit_gtc": {
              "base_size": "0.001",
              "limit_price": "10000.00",
              "stop_price": "20000.00",
              "stop_direction": "20000.00"
            },
            "stop_limit_stop_limit_gtd": {
              "base_size": 0.001,
              "limit_price": "10000.00",
              "stop_price": "20000.00",
              "end_time": "2021-05-31T09:59:59.000Z",
              "stop_direction": "20000.00"
            },
            "trigger_bracket_gtc": {
              "base_size": 0.001,
              "limit_price": "10000.00",
              "stop_trigger_price": "20000.00"
            },
            "trigger_bracket_gtd": {
              "base_size": 0.001,
              "limit_price": "10000.00",
              "stop_trigger_price": "20000.00",
              "end_time": "2021-05-31T09:59:59.000Z"
            },
            "scaled_limit_gtc": {
              "orders": [
                {
                  "quote_size": "10.00",
                  "base_size": "0.001",
                  "limit_price": "10000.00",
                  "post_only": false,
                  "rfq_disabled": true
                }
              ],
              "quote_size": "<string>",
              "base_size": "<string>",
              "num_orders": 123,
              "min_price": "<string>",
              "max_price": "<string>",
              "price_distribution": "FLAT",
              "size_distribution": "UNKNOWN_DISTRIBUTION",
              "size_diff": "<string>",
              "size_ratio": "<string>"
            }
          },
          "side": "",
          "client_order_id": "11111-000000-000000",
          "status": "PENDING",
          "created_time": "2021-05-31T09:59:59.000Z",
          "completion_percentage": "50",
          "average_filled_price": "50",
          "number_of_fills": "2",
          "pending_cancel": true,
          "size_in_quote": false,
          "total_fees": "5.00",
          "size_inclusive_of_fees": false,
          "total_value_after_fees": "<string>",
          "time_in_force": "UNKNOWN_TIME_IN_FORCE",
          "filled_size": "0.001",
          "fee": "<string>",
          "filled_value": "10000",
          "trigger_status": "UNKNOWN_TRIGGER_STATUS",
          "order_type": "UNKNOWN_ORDER_TYPE",
          "reject_reason": "REJECT_REASON_UNSPECIFIED",
          "settled": true,
          "product_type": "UNKNOWN_PRODUCT_TYPE",
          "reject_message": "<string>",
          "cancel_message": "<string>",
          "order_placement_source": "UNKNOWN_PLACEMENT_SOURCE",
          "outstanding_hold_amount": "<string>",
          "is_liquidation": true,
          "last_fill_time": "<string>",
          "edit_history": [
            {
              "price": "19000.00",
              "size": "0.001",
              "replace_accept_timestamp": "<string>"
            }
          ],
          "leverage": "<string>",
          "margin_type": "",
          "retail_portfolio_id": "b87a2d3f-8a1e-49b3-a4ea-402d8c389aca",
          "originating_order_id": "b87a2d3f-8a1e-49b3-a4ea-402d8c389aca",
          "attached_order_id": "b87a2d3f-8a1e-49b3-a4ea-402d8c389aca",
          "attached_order_configuration": {
            "market_market_ioc": {
              "quote_size": "10.00",
              "base_size": "0.001",
              "rfq_disabled": true
            },
            "market_market_fok": {
              "quote_size": "10.00",
              "base_size": "0.001",
              "rfq_disabled": true
            },
            "sor_limit_ioc": {
              "quote_size": "10.00",
              "base_size": "0.001",
              "limit_price": "10000.00",
              "rfq_disabled": true
            },
            "limit_limit_gtc": {
              "quote_size": "10.00",
              "base_size": "0.001",
              "limit_price": "10000.00",
              "post_only": false,
              "rfq_disabled": true
            },
            "limit_limit_gtd": {
              "quote_size": "10.00",
              "base_size": "0.001",
              "limit_price": "10000.00",
              "end_time": "2021-05-31T09:59:59.000Z",
              "post_only": false
            },
            "limit_limit_fok": {
              "quote_size": "10.00",
              "base_size": "0.001",
              "limit_price": "10000.00",
              "rfq_disabled": true
            },
            "twap_limit_gtd": {
              "quote_size": "10.00",
              "base_size": "0.001",
              "start_time": "2021-05-31T07:59:59.000Z",
              "end_time": "2021-05-31T09:59:59.000Z",
              "limit_price": "10000.00",
              "number_buckets": "5",
              "bucket_size": "2.00",
              "bucket_duration": "300s"
            },
            "stop_limit_stop_limit_gtc": {
              "base_size": "0.001",
              "limit_price": "10000.00",
              "stop_price": "20000.00",
              "stop_direction": "20000.00"
            },
            "stop_limit_stop_limit_gtd": {
              "base_size": 0.001,
              "limit_price": "10000.00",
              "stop_price": "20000.00",
              "end_time": "2021-05-31T09:59:59.000Z",
              "stop_direction": "20000.00"
            },
            "trigger_bracket_gtc": {
              "base_size": 0.001,
              "limit_price": "10000.00",
              "stop_trigger_price": "20000.00"
            },
            "trigger_bracket_gtd": {
              "base_size": 0.001,
              "limit_price": "10000.00",
              "stop_trigger_price": "20000.00",
              "end_time": "2021-05-31T09:59:59.000Z"
            },
            "scaled_limit_gtc": {
              "orders": [
                {
                  "quote_size": "10.00",
                  "base_size": "0.001",
                  "limit_price": "10000.00",
                  "post_only": false,
                  "rfq_disabled": true
                }
              ],
              "quote_size": "<string>",
              "base_size": "<string>",
              "num_orders": 123,
              "min_price": "<string>",
              "max_price": "<string>",
              "price_distribution": "FLAT",
              "size_distribution": "UNKNOWN_DISTRIBUTION",
              "size_diff": "<string>",
              "size_ratio": "<string>"
            }
          },
          "current_pending_replace": {
            "price": "19000.00",
            "size": "0.001",
            "replace_accept_timestamp": "<string>"
          },
          "commission_detail_total": {
            "total_commission": "<string>",
            "gst_commission": "<string>",
            "withholding_commission": "<string>",
            "client_commission": "<string>",
            "venue_commission": "<string>",
            "regulatory_commission": "<string>",
            "clearing_commission": "<string>"
          },
          "workable_size": "3",
          "workable_size_completion_pct": "50",
          "product_details": {
            "equity_details": {
              "base_cbrn": "<string>",
              "ticker": "<string>",
              "quote_id": "<string>"
            }
          },
          "cost_basis_method": "COST_BASIS_METHOD_UNSPECIFIED",
          "displayed_order_config": "UNKNOWN_DISPLAYED_ORDER_CONFIG",
          "equity_trading_session": "UNKNOWN_EQUITY_TRADING_SESSION",
          "prediction_side": "PREDICTION_SIDE_UNKNOWN",
          "last_update_time": "<string>"
        }
      ],
      "has_next": true,
      "sequence": "<string>",
      "cursor": "789100",
      "proof_token_required": true
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

#### Query Parameters

order_ids

string[]

ID(s) of order(s).

product_ids

string[]

Optional string of the product ID(s). Defaults to null, or fetch for all products.

product_type

enum<string>

default:UNKNOWN_PRODUCT_TYPE

Returns orders matching this product type. By default, returns all product types.

Available options:

`UNKNOWN_PRODUCT_TYPE`,

`SPOT`,

`FUTURE`

order_status

enum<string>[]

Only returns orders matching the specified order statuses.

Available options:

`PENDING`,

`OPEN`,

`FILLED`,

`CANCELLED`,

`EXPIRED`,

`FAILED`,

`UNKNOWN_ORDER_STATUS`,

`QUEUED`,

`CANCEL_QUEUED`,

`EDIT_QUEUED`

time_in_forces

enum<string>[]

Only orders matching this time in force(s) are returned. Default is to return all time in forces.

Available options:

`UNKNOWN_TIME_IN_FORCE`,

`GOOD_UNTIL_DATE_TIME`,

`GOOD_UNTIL_CANCELLED`,

`IMMEDIATE_OR_CANCEL`,

`FILL_OR_KILL`

order_types

enum<string>[]

Only returns orders matching the specified order types (e.g. MARKET). By default, returns all order types.

Available options:

`UNKNOWN_ORDER_TYPE`,

`MARKET`,

`LIMIT`,

`STOP`,

`STOP_LIMIT`,

`BRACKET`,

`TWAP`,

`ROLL_OPEN`,

`ROLL_CLOSE`,

`LIQUIDATION`,

`SCALED`

order_side

enum<string>

default:""

Only returns the orders matching the specified side (e.g. 'BUY', 'SELL'). By default, returns all sides.

Available options:

`BUY`,

`SELL`

start_date

string<RFC3339 Timestamp>

The start date to fetch orders from (inclusive). If provided, only orders created after this date will be returned.

end_date

string<RFC3339 Timestamp>

The end date to fetch orders from (exclusive). If provided, only orders with creation time before this date will be returned.

order_placement_source

enum<string>

default:RETAIL_ADVANCED

Only returns the orders matching this placement source. By default, returns RETAIL_ADVANCED placement source.

Available options:

`UNKNOWN_PLACEMENT_SOURCE`,

`RETAIL_SIMPLE`,

`RETAIL_ADVANCED`

contract_expiry_type

enum<string>

default:UNKNOWN_CONTRACT_EXPIRY_TYPE

Only returns the orders matching the contract expiry type. Only applicable if product_type is set to FUTURE.

Available options:

`UNKNOWN_CONTRACT_EXPIRY_TYPE`,

`EXPIRING`,

`PERPETUAL`

asset_filters

string[]

Only returns the orders where the quote, base or underlying asset matches the provided asset filter(s) (e.g. 'BTC').

retail_portfolio_id

string

(Deprecated) Only orders matching this retail portfolio id are returned. Only applicable for legacy keys. CDP keys will default to the key's permissioned portfolio.

limit

integer<int32>

The number of orders to display per page (no default amount). If `has_next` is true, additional pages of orders are available to be fetched. Use the `cursor` parameter to start on a specified page.

cursor

string

For paginated responses, returns all responses that come after this value.

sort_by

enum<string>

default:UNKNOWN_SORT_BY

Sort results by a field, results use unstable pagination. Default is to sort by creation time.

Available options:

`UNKNOWN_SORT_BY`,

`LIMIT_PRICE`,

`LAST_FILL_TIME`,

`LAST_UPDATE_TIME`

user_native_currency

string

(Deprecated) Native currency to fetch order with. Default is `USD`.

use_simplified_total_value_calculation

boolean

default:true

Optional boolean to use simplified total value calculation. Default is true.

proof_token

string

Optional proof token for 2FA validation when accessing transaction history (EU SCA compliance).

#### Response

A successful response.

orders

object[]

required

A list of orders matching the query.

has_next

boolean

required

Whether there are additional pages for this query.

Example:

`true`

sequence

string<int64>

(Deprecated) The sequence of the db at which this state was read.

cursor

string

For paginated responses, returns all responses that come after this value.

Example:

`"789100"`

proof_token_required

boolean

Indicates that a valid proof token is required to access this data (EU SCA compliance).

Example:

`true`