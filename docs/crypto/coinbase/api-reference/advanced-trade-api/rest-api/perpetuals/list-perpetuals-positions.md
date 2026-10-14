---
exchange: coinbase
source_url: https://docs.cdp.coinbase.com/api-reference/advanced-trade-api/rest-api/perpetuals/list-perpetuals-positions
api_type: REST
updated_at: 2026-10-14 19:08:15.901377
---

# List Perpetuals Positions

**Endpoint:** `GET https://api.coinbase.com/api/v3/brokerage/intx/positions/{portfolio_uuid}`


Get a list of open positions in your Perpetuals portfolio
    
    
    curl --request GET \
      --url https://api.coinbase.com/api/v3/brokerage/intx/positions/{portfolio_uuid} \
      --header 'Authorization: Bearer <token>'
    
    
    import requests
    
    url = "https://api.coinbase.com/api/v3/brokerage/intx/positions/{portfolio_uuid}"
    
    headers = {"Authorization": "Bearer <token>"}
    
    response = requests.get(url, headers=headers)
    
    print(response.text)
    
    
    const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};
    
    fetch('https://api.coinbase.com/api/v3/brokerage/intx/positions/{portfolio_uuid}', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.coinbase.com/api/v3/brokerage/intx/positions/{portfolio_uuid}",
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
    
    	url := "https://api.coinbase.com/api/v3/brokerage/intx/positions/{portfolio_uuid}"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://api.coinbase.com/api/v3/brokerage/intx/positions/{portfolio_uuid}")
      .header("Authorization", "Bearer <token>")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.coinbase.com/api/v3/brokerage/intx/positions/{portfolio_uuid}")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Get.new(url)
    request["Authorization"] = 'Bearer <token>'
    
    response = http.request(request)
    puts response.read_bodyINTX (deprecated)

# List Perpetuals Positions

Get a list of open positions in your Perpetuals portfolio

GET

/

api

/

v3

/

brokerage

/

intx

/

positions

/

{portfolio_uuid}

List Perpetuals Positions
    
    
    curl --request GET \
      --url https://api.coinbase.com/api/v3/brokerage/intx/positions/{portfolio_uuid} \
      --header 'Authorization: Bearer <token>'
    
    
    import requests
    
    url = "https://api.coinbase.com/api/v3/brokerage/intx/positions/{portfolio_uuid}"
    
    headers = {"Authorization": "Bearer <token>"}
    
    response = requests.get(url, headers=headers)
    
    print(response.text)
    
    
    const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};
    
    fetch('https://api.coinbase.com/api/v3/brokerage/intx/positions/{portfolio_uuid}', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.coinbase.com/api/v3/brokerage/intx/positions/{portfolio_uuid}",
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
    
    	url := "https://api.coinbase.com/api/v3/brokerage/intx/positions/{portfolio_uuid}"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    {
      "positions": [
        {
          "product_id": "<string>",
          "product_uuid": "<string>",
          "portfolio_uuid": "<string>",
          "symbol": "<string>",
          "vwap": {
            "value": "<string>",
            "currency": "<string>"
          },
          "entry_vwap": {
            "value": "<string>",
            "currency": "<string>"
          },
          "position_side": "POSITION_SIDE_UNKNOWN",
          "margin_type": "MARGIN_TYPE_UNSPECIFIED",
          "net_size": "<string>",
          "buy_order_size": "<string>",
          "sell_order_size": "<string>",
          "im_contribution": "<string>",
          "unrealized_pnl": {
            "value": "<string>",
            "currency": "<string>"
          },
          "mark_price": {
            "value": "<string>",
            "currency": "<string>"
          },
          "liquidation_price": {
            "value": "<string>",
            "currency": "<string>"
          },
          "leverage": "<string>",
          "im_notional": {
            "value": "<string>",
            "currency": "<string>"
          },
    
    
    HttpResponse<String> response = Unirest.get("https://api.coinbase.com/api/v3/brokerage/intx/positions/{portfolio_uuid}")
      .header("Authorization", "Bearer <token>")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.coinbase.com/api/v3/brokerage/intx/positions/{portfolio_uuid}")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Get.new(url)
    request["Authorization"] = 'Bearer <token>'
    
    response = http.request(request)
    puts response.read_body
    
    
    {
      "positions": [
        {
          "product_id": "<string>",
          "product_uuid": "<string>",
          "portfolio_uuid": "<string>",
          "symbol": "<string>",
          "vwap": {
            "value": "<string>",
            "currency": "<string>"
          },
          "entry_vwap": {
            "value": "<string>",
            "currency": "<string>"
          },
          "position_side": "POSITION_SIDE_UNKNOWN",
          "margin_type": "MARGIN_TYPE_UNSPECIFIED",
          "net_size": "<string>",
          "buy_order_size": "<string>",
          "sell_order_size": "<string>",
          "im_contribution": "<string>",
          "unrealized_pnl": {
            "value": "<string>",
            "currency": "<string>"
          },
          "mark_price": {
            "value": "<string>",
            "currency": "<string>"
          },
          "liquidation_price": {
            "value": "<string>",
            "currency": "<string>"
    
          "mm_notional": {
            "value": "<string>",
            "currency": "<string>"
          },
          "position_notional": {
            "value": "<string>",
            "currency": "<string>"
          },
          "aggregated_pnl": {
            "value": "<string>",
            "currency": "<string>"
          }
        }
      ],
      "summary": {
        "aggregated_pnl": {
          "value": "<string>",
          "currency": "<string>"
        }
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

**Retired.** INTX perpetuals trading through the Advanced Trade API ended on October 1, 2026. International derivatives now trade on the [Deribit-powered derivatives gateway](/coinbase-app/advanced-trade-apis/guides/derivatives/overview). See the [Migration Overview](/coinbase-app/advanced-trade-apis/guides/derivatives/overview).

#### Authorizations

ApiKeyOAuth2ApiKeyOAuth2

Authorization

string

header

required

A bearer token signed using your API Key Secret, see [Creating API Keys](/coinbase-app/authentication-authorization/api-key-authentication) section of our docs for more information. See [Scope & Permissions](/coinbase-app/advanced-trade-apis/rest-scopes) for the permission each endpoint requires.

#### Path Parameters

portfolio_uuid

string

required

The portfolio UUID.

#### Response

A successful response.

}, "leverage": "<string>", "im_notional": { "value": "<string>", "currency": "<string>" }, "mm_notional": { "value": "<string>", "currency": "<string>" }, "position_notional": { "value": "<string>", "currency": "<string>" }, "aggregated_pnl": { "value": "<string>", "currency": "<string>" } } ], "summary": { "aggregated_pnl": { "value": "<string>", "currency": "<string>" } } }`
    
    
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

#### Path Parameters

portfolio_uuid

string

required

The portfolio UUID.

#### Response

A successful response.

positions

object[]

summary

object

INTX (deprecated)

# Opt In or Out of Multi Asset Collateral

Enable or Disable Multi Asset Collateral for a given Portfolio

POST

/

api

/

v3

/

brokerage

/

intx

/

multi_asset_collateral

Opt In or Out of Multi Asset Collateral
    
    
    curl --request POST \
      --url https://api.coinbase.com/api/v3/brokerage/intx/multi_asset_collateral \
      --header 'Authorization: Bearer <token>' \
      --header 'Content-Type: application/json' \
      --data '
    {
      "portfolio_uuid": "<string>",
      "multi_asset_collateral_enabled": true
    }
    '
    
    
    import requests
    
    url = "https://api.coinbase.com/api/v3/brokerage/intx/multi_asset_collateral"
    
    payload = {
        "portfolio_uuid": "<string>",
        "multi_asset_collateral_enabled": True
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
      body: JSON.stringify({portfolio_uuid: '<string>', multi_asset_collateral_enabled: true})
    };
    
    fetch('https://api.coinbase.com/api/v3/brokerage/intx/multi_asset_collateral', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.coinbase.com/api/v3/brokerage/intx/multi_asset_collateral",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "POST",
      CURLOPT_POSTFIELDS => json_encode([
        'portfolio_uuid' => '<string>',
        'multi_asset_collateral_enabled' => true
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
    
    	url := "https://api.coinbase.com/api/v3/brokerage/intx/multi_asset_collateral"
    
    	payload := strings.NewReader("{\n  \"portfolio_uuid\": \"<string>\",\n  \"multi_asset_collateral_enabled\": true\n}")
    
    	req, _ := http.NewRequest("POST", url, payload)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    	req.Header.Add("Content-Type", "application/json")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.post("https://api.coinbase.com/api/v3/brokerage/intx/multi_asset_collateral")
      .header("Authorization", "Bearer <token>")
      .header("Content-Type", "application/json")
      .body("{\n  \"portfolio_uuid\": \"<string>\",\n  \"multi_asset_collateral_enabled\": true\n}")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.coinbase.com/api/v3/brokerage/intx/multi_asset_collateral")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Post.new(url)
    request["Authorization"] = 'Bearer <token>'
    request["Content-Type"] = 'application/json'
    request.body = "{\n  \"portfolio_uuid\": \"<string>\",\n  \"multi_asset_collateral_enabled\": true\n}"
    
    response = http.request(request)
    puts response.read_body
    
    
    {
      "multi_asset_collateral_enabled": true
    }
    
    
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

positionsobject[]Show child attributessummaryobjectShow child attributes