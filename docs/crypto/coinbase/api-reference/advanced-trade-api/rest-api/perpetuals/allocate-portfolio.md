---
exchange: coinbase
source_url: https://docs.cdp.coinbase.com/api-reference/advanced-trade-api/rest-api/perpetuals/allocate-portfolio
api_type: Account
updated_at: 2026-11-21 18:56:58.347197
---

# Allocate Portfolio

**Endpoint:** `POST https://api.coinbase.com/api/v3/brokerage/intx/allocate`

,\n      \"end_time\": \"2021-05-31T09:59:59Z\",\n      \"limit_price\": \"10000.00\",\n      \"number_buckets\": \"5\",\n      \"bucket_size\": \"2.00\",\n      \"bucket_duration\": \"300s\"\n    },\n    \"stop_limit_stop_limit_gtc\": {\n      \"base_size\": \"0.001\",\n      \"limit_price\": \"10000.00\",\n      \"stop_price\": \"20000.00\",\n      \"stop_direction\": \"20000.00\"\n    },\n    \"stop_limit_stop_limit_gtd\": {\n      \"base_size\": 0.001,\n      \"limit_price\": \"10000.00\",\n      \"stop_price\": \"20000.00\",\n      \"end_time\": \"2021-05-31T09:59:59Z\",\n      \"stop_direction\": \"20000.00\"\n    },\n    \"trigger_bracket_gtc\": {\n      \"base_size\": 0.001,\n      \"limit_price\": \"10000.00\",\n      \"stop_trigger_price\": \"20000.00\"\n    },\n    \"trigger_bracket_gtd\": {\n      \"base_size\": 0.001,\n      \"limit_price\": \"10000.00\",\n      \"stop_trigger_price\": \"20000.00\",\n      \"end_time\": \"2021-05-31T09:59:59Z\"\n    },\n    \"scaled_limit_gtc\": {\n      \"orders\": [\n        {\n          \"quote_size\": \"10.00\",\n          \"base_size\": \"0.001\",\n          \"limit_price\": \"10000.00\",\n          \"post_only\": false\n        }\n      ],\n      \"quote_size\": \"<string>\",\n      \"base_size\": \"<string>\",\n      \"num_orders\": 123,\n      \"min_price\": \"<string>\",\n      \"max_price\": \"<string>\",\n      \"price_distribution\": \"FLAT\",\n      \"size_distribution\": \"UNKNOWN_DISTRIBUTION\",\n      \"size_diff\": \"<string>\",\n      \"size_ratio\": \"<string>\"\n    }\n  },\n  \"leverage\": \"2.0\",\n  \"margin_type\": \"\",\n  \"retail_portfolio_id\": \"11111111-1111-1111-1111-111111111111\",\n  \"attached_order_configuration\": {\n    \"market_market_ioc\": {\n      \"quote_size\": \"10.00\",\n      \"base_size\": \"0.001\"\n    },\n    \"market_market_fok\": {\n      \"quote_size\": \"10.00\",\n      \"base_size\": \"0.001\"\n    },\n    \"sor_limit_ioc\": {\n      \"quote_size\": \"10.00\",\n      \"base_size\": \"0.001\",\n      \"limit_price\": \"10000.00\"\n    },\n    \"limit_limit_gtc\": {\n      \"quote_size\": \"10.00\",\n      \"base_size\": \"0.001\",\n      \"limit_price\": \"10000.00\",\n      \"post_only\": false\n    },\n    \"limit_limit_gtd\": {\n      \"quote_size\": \"10.00\",\n      \"base_size\": \"0.001\",\n      \"limit_price\": \"10000.00\",\n      \"end_time\": \"2021-05-31T09:59:59Z\",\n      \"post_only\": false\n    },\n    \"limit_limit_fok\": {\n      \"quote_size\": \"10.00\",\n      \"base_size\": \"0.001\",\n      \"limit_price\": \"10000.00\"\n    },\n    \"twap_limit_gtd\": {\n      \"quote_size\": \"10.00\",\n      \"base_size\": \"0.001\",\n      \"start_time\": \"2021-05-31T07:59:59Z\",\n      \"end_time\": \"2021-05-31T09:59:59Z\",\n      \"limit_price\": \"10000.00\",\n      \"number_buckets\": \"5\",\n      \"bucket_size\": \"2.00\",\n      \"bucket_duration\": \"300s\"\n    },\n    \"stop_limit_stop_limit_gtc\": {\n      \"base_size\": \"0.001\",\n      \"limit_price\": \"10000.00\",\n      \"stop_price\": \"20000.00\",\n      \"stop_direction\": \"20000.00\"\n    },\n    \"stop_limit_stop_limit_gtd\": {\n      \"base_size\": 0.001,\n      \"limit_price\": \"10000.00\",\n      \"stop_price\": \"20000.00\",\n      \"end_time\": \"2021-05-31T09:59:59Z\",\n      \"stop_direction\": \"20000.00\"\n    },\n    \"trigger_bracket_gtc\": {\n      \"base_size\": 0.001,\n      \"limit_price\": \"10000.00\",\n      \"stop_trigger_price\": \"20000.00\"\n    },\n    \"trigger_bracket_gtd\": {\n      \"base_size\": 0.001,\n      \"limit_price\": \"10000.00\",\n      \"stop_trigger_price\": \"20000.00\",\n      \"end_time\": \"2021-05-31T09:59:59Z\"\n    },\n    \"scaled_limit_gtc\": {\n      \"orders\": [\n        {\n          \"quote_size\": \"10.00\",\n          \"base_size\": \"0.001\",\n          \"limit_price\": \"10000.00\",\n          \"post_only\": false\n        }\n      ],\n      \"quote_size\": \"<string>\",\n      \"base_size\": \"<string>\",\n      \"num_orders\": 123,\n      \"min_price\": \"<string>\",\n      \"max_price\": \"<string>\",\n      \"price_distribution\": \"FLAT\",\n      \"size_distribution\": \"UNKNOWN_DISTRIBUTION\",\n      \"size_diff\": \"<string>\",\n      \"size_ratio\": \"<string>\"\n    }\n  },\n  \"equity_order_metadata\": {\n    \"equity_trading_session\": \"UNKNOWN_EQUITY_TRADING_SESSION\",\n    \"displayed_order_config\": \"UNKNOWN_DISPLAYED_ORDER_CONFIG\"\n  },\n  \"prediction_metadata\": {\n    \"prediction_side\": \"PREDICTION_SIDE_UNKNOWN\",\n    \"preview_order_est_average_filled_price\": \"<string>\",\n    \"supports_fractional_base_size\": true\n  },\n  \"cost_basis_method\": \"COST_BASIS_METHOD_UNSPECIFIED\"\n}")
    
    	req, _ := http.NewRequest("POST", url, payload)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    	req.Header.Add("Content-Type", "application/json")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }INTX (deprecated)
    
    # Allocate Portfolio
    
    Allocate portfolio funds to a sub-portfolio on Intx Portfolio
    
    
    curl --request POST \
      --url https://api.coinbase.com/api/v3/brokerage/intx/allocate \
      --header 'Authorization: Bearer <token>' \
      --header 'Content-Type: application/json' \
      --data '
    {
      "portfolio_uuid": "<string>",
      "symbol": "<string>",
      "amount": "<string>",
      "currency": "<string>"
    }
    '
    
    
    import requests
    
    url = "https://api.coinbase.com/api/v3/brokerage/intx/allocate"
    
    payload = {
        "portfolio_uuid": "<string>",
        "symbol": "<string>",
        "amount": "<string>",
        "currency": "<string>"
    }
    headers = {
        "Authorization": "Bearer <token>",
        "Content-Type": "application/json"
    }
    
    response = requests.post(url, json=payload, headers=headers)
    
    print(response.text)
    
    
    const options = {
      method: 'POST',
      headers: {Authorization: 'Bearer <token>', 'Content-Type': 'application/json'},
      body: JSON.stringify({
        portfolio_uuid: '<string>',
        symbol: '<string>',
        amount: '<string>',
        currency: '<string>'
      })
    };
    
    fetch('https://api.coinbase.com/api/v3/brokerage/intx/allocate', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.coinbase.com/api/v3/brokerage/intx/allocate",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "POST",
      CURLOPT_POSTFIELDS => json_encode([
        'portfolio_uuid' => '<string>',
        'symbol' => '<string>',
        'amount' => '<string>',
        'currency' => '<string>'
      ]),
      CURLOPT_HTTPHEADER => [
        "Authorization: Bearer <token>",
        "Content-Type: application/json"
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
    	"strings"
    	"net/http"
    	"io"
    )
    
    func main() {
    
    	url := "https://api.coinbase.com/api/v3/brokerage/intx/allocate"
    
    	payload := strings.NewReader("{\n  \"portfolio_uuid\": \"<string>\",\n  \"symbol\": \"<string>\",\n  \"amount\": \"<string>\",\n  \"currency\": \"<string>\"\n}")
    
    	req, _ := http.NewRequest("POST", url, payload)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    	req.Header.Add("Content-Type", "application/json")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.post("https://api.coinbase.com/api/v3/brokerage/intx/allocate")
      .header("Authorization", "Bearer <token>")
      .header("Content-Type", "application/json")
      .body("{\n  \"portfolio_uuid\": \"<string>\",\n  \"symbol\": \"<string>\",\n  \"amount\": \"<string>\",\n  \"currency\": \"<string>\"\n}")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.coinbase.com/api/v3/brokerage/intx/allocate")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Post.new(url)
    request["Authorization"] = 'Bearer <token>'
    request["Content-Type"] = 'application/json'
    request.body = "{\n  \"portfolio_uuid\": \"<string>\",\n  \"symbol\": \"<string>\",\n  \"amount\": \"<string>\",\n  \"currency\": \"<string>\"\n}"
    
    response = http.request(request)
    puts response.read_body
    
    
    {}
    
    
    {
      "error": "<string>",
      "code": 123,
      "message": "<string>",
      "details": [
        {}
      ]
    }

**Retired.** INTX perpetuals trading through the Advanced Trade API ended on October 1, 2026. International derivatives now trade on the [Deribit-powered derivatives gateway](/coinbase-app/advanced-trade-apis/guides/derivatives/overview). See the [Migration Overview](/coinbase-app/advanced-trade-apis/guides/derivatives/overview).

#### Authorizations

ApiKeyOAuth2ApiKeyOAuth2

Authorization

string

header

required

A bearer token signed using your API Key Secret, see [Creating API Keys](/coinbase-app/authentication-authorization/api-key-authentication) section of our docs for more information. See [Scope & Permissions](/coinbase-app/advanced-trade-apis/rest-scopes) for the permission each endpoint requires.

#### Scopes

transfer

ApiKey

wallet:transactions:transfer

OAuth2

Transfer funds between accounts.

#### Body

application/json

portfolio_uuid

string

The portfolio UUID.

symbol

string

The trading pair (e.g. 'BTC-PERP-INTX').

amount

string

The amount to be allocated for the specified isolated position.

currency

string

The currency to be allocated for the specific isolated position (e.g. USD, BTC, etc).

#### Response

A successful response.

The response is of type `object`.