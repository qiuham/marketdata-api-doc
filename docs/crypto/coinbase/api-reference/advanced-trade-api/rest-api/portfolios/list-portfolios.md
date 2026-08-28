---
exchange: coinbase
source_url: https://docs.cdp.coinbase.com/api-reference/advanced-trade-api/rest-api/portfolios/list-portfolios
api_type: Account
updated_at: 2026-08-28 21:58:49.224671
---

# List Portfolios

**Endpoint:** `GET https://api.coinbase.com/api/v3/brokerage/portfolios`


Get all portfolios of a user.
    
    
    curl --request GET \
      --url https://api.coinbase.com/api/v3/brokerage/portfolios \
      --header 'Authorization: Bearer <token>'
    
    
    import requests
    
    url = "https://api.coinbase.com/api/v3/brokerage/portfolios"
    
    headers = {"Authorization": "Bearer <token>"}
    
    response = requests.get(url, headers=headers)
    
    print(response.text)
    
    
    const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};
    
    fetch('https://api.coinbase.com/api/v3/brokerage/portfolios', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.coinbase.com/api/v3/brokerage/portfolios",
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
    
    	url := "https://api.coinbase.com/api/v3/brokerage/portfolios"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://api.coinbase.com/api/v3/brokerage/portfolios")
      .header("Authorization", "Bearer <token>")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.coinbase.com/api/v3/brokerage/portfolios")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Get.new(url)
    request["Authorization"] = 'Bearer <token>'
    
    response = http.request(request)
    puts response.read_body
    
    
    {
      "portfolios": [
        {
          "name": "<string>",
          "uuid": "<string>",
          "type": "UNDEFINED",
          "deleted": true
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

#### Query Parameters

portfolio_type

enum<string>

default:UNDEFINED

Only returns portfolios matching this portfolio type.

Available options:

`UNDEFINED`,

`DEFAULT`,

`CONSUMER`,

`INTX`

#### Response

A successful response.

portfolios

object[]