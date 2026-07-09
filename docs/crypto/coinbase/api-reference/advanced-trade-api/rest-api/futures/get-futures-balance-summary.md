---
exchange: coinbase
source_url: https://docs.cdp.coinbase.com/api-reference/advanced-trade-api/rest-api/futures/get-futures-balance-summary
api_type: REST
updated_at: 2026-07-09 19:25:33.589279
---

# Get US Derivatives Balance Summary

**Endpoint:** `GET https://api.coinbase.com/api/v3/brokerage/cfm/balance_summary`


Get a summary of balances for CFM trading
    
    
    curl --request GET \
      --url https://api.coinbase.com/api/v3/brokerage/cfm/balance_summary \
      --header 'Authorization: Bearer <token>'
    
    
    import requests
    
    url = "https://api.coinbase.com/api/v3/brokerage/cfm/balance_summary"
    
    headers = {"Authorization": "Bearer <token>"}
    
    response = requests.get(url, headers=headers)
    
    print(response.text)
    
    
    const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};
    
    fetch('https://api.coinbase.com/api/v3/brokerage/cfm/balance_summary', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.coinbase.com/api/v3/brokerage/cfm/balance_summary",
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
    
    	url := "https://api.coinbase.com/api/v3/brokerage/cfm/balance_summary"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://api.coinbase.com/api/v3/brokerage/cfm/balance_summary")
      .header("Authorization", "Bearer <token>")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.coinbase.com/api/v3/brokerage/cfm/balance_summary")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Get.new(url)
    request["Authorization"] = 'Bearer <token>'
    
    response = http.request(request)
    puts response.read_body
    
    
    {
      "balance_summary": {
        "futures_buying_power": {
          "value": "<string>",
          "currency": "<string>",
          "cbrn": "<string>"
        },
        "total_usd_balance": {
          "value": "<string>",
          "currency": "<string>",
          "cbrn": "<string>"
        },
        "cbi_usd_balance": {
          "value": "<string>",
          "currency": "<string>",
          "cbrn": "<string>"
        },
        "cfm_usd_balance": {
          "value": "<string>",
          "currency": "<string>",
          "cbrn": "<string>"
        },
        "total_open_orders_hold_amount": {
          "value": "<string>",
          "currency": "<string>",
          "cbrn": "<string>"
        },
        "unrealized_pnl": {
          "value": "<string>",
          "currency": "<string>",
          "cbrn": "<string>"
        },
        "daily_realized_pnl": {
          "value": "<string>",
          "currency": "<string>",
          "cbrn": "<string>"
        },
        "initial_margin": {
          "value": "<string>",
          "currency": "<string>",
          "cbrn": "<string>"
        },
        "available_margin": {
          "value": "<string>",
          "currency": "<string>",
          "cbrn": "<string>"
        },
        "liquidation_threshold": {
          "value": "<string>",
          "currency": "<string>",
          "cbrn": "<string>"
        },
        "liquidation_buffer_amount": {
          "value": "<string>",
          "currency": "<string>",
          "cbrn": "<string>"
        },
        "liquidation_buffer_percentage": "<string>",
        "intraday_margin_window_measure": {
          "margin_window_type": "FCM_MARGIN_WINDOW_TYPE_UNSPECIFIED",
          "margin_level": "MARGIN_LEVEL_TYPE_UNSPECIFIED",
          "initial_margin": "<string>",
          "maintenance_margin": "<string>",
          "liquidation_buffer": "<string>",
          "total_hold": "<string>",
          "futures_buying_power": "<string>"
        },
        "overnight_margin_window_measure": {
          "margin_window_type": "FCM_MARGIN_WINDOW_TYPE_UNSPECIFIED",
          "margin_level": "MARGIN_LEVEL_TYPE_UNSPECIFIED",
          "initial_margin": "<string>",
          "maintenance_margin": "<string>",
          "liquidation_buffer": "<string>",
          "total_hold": "<string>",
          "futures_buying_power": "<string>"
        },
        "total_pending_transfers_amount": {
          "value": "<string>",
          "currency": "<string>",
          "cbrn": "<string>"
        },
        "funding_pnl": {
          "value": "<string>",
          "currency": "<string>",
          "cbrn": "<string>"
        }
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

#### Response

A successful response.

balance_summary

object