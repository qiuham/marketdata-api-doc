---
exchange: coinbase
source_url: https://docs.cdp.coinbase.com/api-reference/advanced-trade-api/rest-api/payment-methods/get-payment-method
api_type: REST
updated_at: 2026-09-26 18:58:29.787877
---

# Get Payment Method

**Endpoint:** `GET https://api.coinbase.com/api/v3/brokerage/payment_methods/{payment_method_id}`

": \"10.00\",\n      \"base_size\": \"0.001\"\n    },\n    \"market_market_fok\": {\n      \"quote_size\": \"10.00\",\n      \"base_size\": \"0.001\"\n    },\n    \"sor_limit_ioc\": {\n      \"quote_size\": \"10.00\",\n      \"base_size\": \"0.001\",\n      \"limit_price\": \"10000.00\"\n    },\n    \"limit_limit_gtc\": {\n      \"quote_size\": \"10.00\",\n      \"base_size\": \"0.001\",\n      \"limit_price\": \"10000.00\",\n      \"post_only\": false\n    },\n    \"limit_limit_gtd\": {\n      \"quote_size\": \"10.00\",\n      \"base_size\": \"0.001\",\n      \"limit_price\": \"10000.00\",\n      \"end_time\": \"2021-05-31T09:59:59Z\",\n      \"post_only\": false\n    },\n    \"limit_limit_fok\": {\n      \"quote_size\": \"10.00\",\n      \"base_size\": \"0.001\",\n      \"limit_price\": \"10000.00\"\n    },\n    \"twap_limit_gtd\": {\n      \"quote_size\": \"10.00\",\n      \"base_size\": \"0.001\",\n      \"start_time\": \"2021-05-31T07:59:59Z\",\n      \"end_time\": \"2021-05-31T09:59:59Z\",\n      \"limit_price\": \"10000.00\",\n      \"number_buckets\": \"5\",\n      \"bucket_size\": \"2.00\",\n      \"bucket_duration\": \"300s\"\n    },\n    \"stop_limit_stop_limit_gtc\": {\n      \"base_size\": \"0.001\",\n      \"limit_price\": \"10000.00\",\n      \"stop_price\": \"20000.00\",\n      \"stop_direction\": \"20000.00\"\n    },\n    \"stop_limit_stop_limit_gtd\": {\n      \"base_size\": 0.001,\n      \"limit_price\": \"10000.00\",\n      \"stop_price\": \"20000.00\",\n      \"end_time\": \"2021-05-31T09:59:59Z\",\n      \"stop_direction\": \"20000.00\"\n    },\n    \"trigger_bracket_gtc\": {\n      \"base_size\": 0.001,\n      \"limit_price\": \"10000.00\",\n      \"stop_trigger_price\": \"20000.00\"\n    },\n    \"trigger_bracket_gtd\": {\n      \"base_size\": 0.001,\n      \"limit_price\": \"10000.00\",\n      \"stop_trigger_price\": \"20000.00\",\n      \"end_time\": \"2021-05-31T09:59:59Z\"\n    },\n    \"scaled_limit_gtc\": {\n      \"orders\": [\n        {\n          \"quote_size\": \"10.00\",\n          \"base_size\": \"0.001\",\n          \"limit_price\": \"10000.00\",\n          \"post_only\": false\n        }\n      ],\n      \"quote_size\": \"<string>\",\n      \"base_size\": \"<string>\",\n      \"num_orders\": 123,\n      \"min_price\": \"<string>\",\n      \"max_price\": \"<string>\",\n      \"price_distribution\": \"FLAT\",\n      \"size_distribution\": \"UNKNOWN_DISTRIBUTION\",\n      \"size_diff\": \"<string>\",\n      \"size_ratio\": \"<string>\"\n    }\n  },\n  \"leverage\": \"2.0\",\n  \"margin_type\": \"\",\n  \"retail_portfolio_id\": \"11111111-1111-1111-1111-111111111111\",\n  \"attached_order_configuration\": {\n    \"market_market_ioc\": {\n      \"quote_size\": \"10.00\",\n      \"base_size\": \"0.001\"\n    },\n    \"market_market_fok\": {\n      \"quote_size\": \"10.00\",\n      \"base_size\": \"0.001\"\n    },\n    \"sor_limit_ioc\": {\n      \"quote_size\": \"10.00\",\n      \"base_size\": \"0.001\",\n      \"limit_price\": \"10000.00\"\n    },\n    \"limit_limit_gtc\": {\n      \"quote_size\": \"10.00\",\n      \"base_size\": \"0.001\",\n      \"limit_price\": \"10000.00\",\n      \"post_only\": false\n    },\n    \"limit_limit_gtd\": {\n      \"quote_size\": \"10.00\",\n      \"base_size\": \"0.001\",\n      \"limit_price\": \"10000.00\",\n      \"end_time\": \"2021-05-31T09:59:59Z\",\n      \"post_only\": false\n    },\n    \"limit_limit_fok\": {\n      \"quote_size\": \"10.00\",\n      \"base_size\": \"0.001\",\n      \"limit_price\": \"10000.00\"\n    },\n    \"twap_limit_gtd\": {\n      \"quote_size\": \"10.00\",\n      \"base_size\": \"0.001\",\n      \"start_time\": \"2021-05-31T07:59:59Z\",\n      \"end_time\": \"2021-05-31T09:59:59Z\",\n      \"limit_price\": \"10000.00\",\n      \"number_buckets\": \"5\",\n      \"bucket_size\": \"2.00\",\n      \"bucket_duration\": \"300s\"\n    },\n    \"stop_limit_stop_limit_gtc\": {\n      \"base_size\": \"0.001\",\n      \"limit_price\": \"10000.00\",\n      \"stop_price\": \"20000.00\",\n      \"stop_direction\": \"20000.00\"\n    },\n    \"stop_limit_stop_limit_gtd\": {\n      \"base_size\": 0.001,\n      \"limit_price\": \"10000.00\",\n      \"stop_price\": \"20000.00\",\n      \"end_time\": \"2021-05-31T09:59:59Z\",\n      \"stop_direction\": \"20000.00\"\n    },\n    \"trigger_bracket_gtc\": {\n      \"base_size\": 0.001,\n      \"limit_price\": \"10000.00\",\n      \"stop_trigger_price\": \"20000.00\"\n    },\n    \"trigger_bracket_gtd\": {\n      \"base_size\": 0.001,\n      \"limit_price\": \"10000.00\",\n      \"stop_trigger_price\": \"20000.00\",\n      \"end_time\": \"2021-05-31T09:59:59Z\"\n    },\n    \"scaled_limit_gtc\": {\n      \"orders\": [\n        {\n          \"quote_size\": \"10.00\",\n          \"base_size\": \"0.001\",\n          \"limit_price\": \"10000.00\",\n          \"post_only\": false\n        }\n      ],\n      \"quote_size\": \"<string>\",\n      \"base_size\": \"<string>\",\n      \"num_orders\": 123,\n      \"min_price\": \"<string>\",\n      \"max_price\": \"<string>\",\n      \"price_distribution\": \"FLAT\",\n      \"size_distribution\": \"UNKNOWN_DISTRIBUTION\",\n      \"size_diff\": \"<string>\",\n      \"size_ratio\": \"<string>\"\n    }\n  },\n  \"equity_order_metadata\": {\n    \"equity_trading_session\": \"UNKNOWN_EQUITY_TRADING_SESSION\",\n    \"displayed_order_config\": \"UNKNOWN_DISPLAYED_ORDER_CONFIG\"\n  },\n  \"prediction_metadata\": {\n    \"prediction_side\": \"PREDICTION_SIDE_UNKNOWN\",\n    \"preview_order_est_average_filled_price\": \"<string>\",\n    \"supports_fractional_base_size\": true\n  },\n  \"cost_basis_method\": \"COST_BASIS_METHOD_UNSPECIFIED\"\n}")
      .asString();Payment Methods
    
    # Get Payment Method
    
    Get information about a payment method for the current user.
    
    
    curl --request GET \
      --url https://api.coinbase.com/api/v3/brokerage/payment_methods/{payment_method_id} \
      --header 'Authorization: Bearer <token>'
    
    
    import requests
    
    url = "https://api.coinbase.com/api/v3/brokerage/payment_methods/{payment_method_id}"
    
    headers = {"Authorization": "Bearer <token>"}
    
    response = requests.get(url, headers=headers)
    
    print(response.text)
    
    
    const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};
    
    fetch('https://api.coinbase.com/api/v3/brokerage/payment_methods/{payment_method_id}', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.coinbase.com/api/v3/brokerage/payment_methods/{payment_method_id}",
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
    
    	url := "https://api.coinbase.com/api/v3/brokerage/payment_methods/{payment_method_id}"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://api.coinbase.com/api/v3/brokerage/payment_methods/{payment_method_id}")
      .header("Authorization", "Bearer <token>")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.coinbase.com/api/v3/brokerage/payment_methods/{payment_method_id}")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Get.new(url)
    request["Authorization"] = 'Bearer <token>'
    
    response = http.request(request)
    puts response.read_body
    
    
    {
      "payment_method": {
        "id": "8bfc20d7-f7c6-4422-bf07-8243ca4169fe",
        "type": "ACH",
        "name": "ALLY BANK ******1234",
        "currency": "USD",
        "verified": true,
        "allow_buy": true,
        "allow_sell": true,
        "allow_deposit": true,
        "allow_withdraw": true,
        "created_at": "2021-05-31T09:59:59Z",
        "updated_at": "2021-05-31T09:59:59Z"
      }
    }
    
    
    {
      "error": "<string>",
      "code": 123,
      "message": "<string>",
      "details": [
        {}
      ]
    }

#### Authorizations

ApiKeyOAuth2ApiKeyOAuth2

Authorization

string

header

required

A bearer token signed using your API Key Secret, see [Creating API Keys](/coinbase-app/authentication-authorization/api-key-authentication) section of our docs for more information. See [Scope & Permissions](/coinbase-app/advanced-trade-apis/rest-scopes) for the permission each endpoint requires.

#### Path Parameters

payment_method_id

string

required

The ID of the payment method. Refer to [List Payment Methods](https://docs.cdp.coinbase.com/advanced-trade/reference/retailbrokerageapi_getpaymentmethods/) for the list of all available payment methods and their corresponding IDs.

#### Response

A successful response.

payment_method

object