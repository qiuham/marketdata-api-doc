---
exchange: coinbase
source_url: https://docs.cdp.coinbase.com/api-reference/advanced-trade-api/rest-api/payment-methods/list-payment-methods
api_type: REST
updated_at: 2026-09-13 18:54:19.935065
---

# List Payment Methods

**Endpoint:** `GET https://api.coinbase.com/api/v3/brokerage/payment_methods`

: "10.00",
                "base_size": "0.001",
                "start_time": "2021-05-31T07:59:59Z",
                "end_time": "2021-05-31T09:59:59Z",
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
                "end_time": "2021-05-31T09:59:59Z",
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
                "end_time": "2021-05-31T09:59:59Z"
            },
            "scaled_limit_gtc": {
                "orders": [
                    {
                        "quote_size": "10.00",
                        "base_size": "0.001",
                        "limit_price": "10000.00",
                        "post_only": False
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
        "equity_order_metadata": {
            "equity_trading_session": "UNKNOWN_EQUITY_TRADING_SESSION",
            "displayed_order_config": "UNKNOWN_DISPLAYED_ORDER_CONFIG"
        },
        "prediction_metadata": {
            "prediction_side": "PREDICTION_SIDE_UNKNOWN",
            "preview_order_est_average_filled_price": "<string>",
            "supports_fractional_base_size": True
        },
        "cost_basis_method": "COST_BASIS_METHOD_UNSPECIFIED"
    }
    headers = {
        "Authorization": "Bearer <token>",
        "Content-Type": "application/json"
    }
    
    response = requests.post(url, json=payload, headers=headers)
    
    print(response.text)Payment Methods
    
    # List Payment Methods
    
    Get a list of payment methods for the current user.
    
    
    curl --request GET \
      --url https://api.coinbase.com/api/v3/brokerage/payment_methods \
      --header 'Authorization: Bearer <token>'
    
    
    import requests
    
    url = "https://api.coinbase.com/api/v3/brokerage/payment_methods"
    
    headers = {"Authorization": "Bearer <token>"}
    
    response = requests.get(url, headers=headers)
    
    print(response.text)
    
    
    const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};
    
    fetch('https://api.coinbase.com/api/v3/brokerage/payment_methods', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.coinbase.com/api/v3/brokerage/payment_methods",
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
    
    	url := "https://api.coinbase.com/api/v3/brokerage/payment_methods"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://api.coinbase.com/api/v3/brokerage/payment_methods")
      .header("Authorization", "Bearer <token>")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.coinbase.com/api/v3/brokerage/payment_methods")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Get.new(url)
    request["Authorization"] = 'Bearer <token>'
    
    response = http.request(request)
    puts response.read_body
    
    
    {
      "payment_methods": [
        {
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
      ]
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

#### Response

A successful response.

payment_methods

object[]