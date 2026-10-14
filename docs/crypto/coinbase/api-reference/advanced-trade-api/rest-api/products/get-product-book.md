---
exchange: coinbase
source_url: https://docs.cdp.coinbase.com/api-reference/advanced-trade-api/rest-api/products/get-product-book
api_type: Market Data
updated_at: 2026-10-14 19:08:16.898742
---

# Get Product Book

**Endpoint:** `GET https://api.coinbase.com/api/v3/brokerage/product_book`

ProductsGet Product BookGet a list of bids/asks for a single product. The amount of detail shown can be customized with the limit parameter.GET/api/v3/brokerage/product_bookGet Product Book
    
    
    curl --request GET \
      --url https://api.coinbase.com/api/v3/brokerage/product_book \
      --header 'Authorization: Bearer <token>'
    
    
    import requests
    
    url = "https://api.coinbase.com/api/v3/brokerage/product_book"
    
    headers = {"Authorization": "Bearer <token>"}
    
    response = requests.get(url, headers=headers)
    
    print(response.text)
    
    
    const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};
    
    fetch('https://api.coinbase.com/api/v3/brokerage/product_book', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.coinbase.com/api/v3/brokerage/product_book",
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
    
    	url := "https://api.coinbase.com/api/v3/brokerage/product_book"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://api.coinbase.com/api/v3/brokerage/product_book")
      .header("Authorization", "Bearer <token>")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.coinbase.com/api/v3/brokerage/product_book")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Get.new(url)
    request["Authorization"] = 'Bearer <token>'
    
    response = http.request(request)
    puts response.read_body
    
    
    {
      "pricebook": {
        "product_id": "BTC-USD",
        "bids": [
          {
            "price": "<string>",
            "size": "<string>"
          }
        ],
        "asks": [
          {
            "price": "<string>",
            "size": "<string>"
          }
        ],
        "time": "<string>"
      },
      "last": "<string>",
      "mid_market": "<string>",
      "spread_bps": "<string>",
      "spread_absolute": "<string>"
    }
    
    
    {
      "error": "<string>",
      "code": 123,
      "message": "<string>",
      "details": [
        {}
      ]
    }

AuthorizationsApiKeyOAuth2ApiKeyOAuth2AuthorizationstringheaderrequiredA bearer token signed using your API Key Secret, see [Creating API Keys](/coinbase-app/authentication-authorization/api-key-authentication) section of our docs for more information. See [Scope & Permissions](/coinbase-app/advanced-trade-apis/rest-scopes) for the permission each endpoint requires.Query Parametersproduct_idstringrequiredThe trading pair (e.g. 'BTC-USD').limitinteger<int32>The number of bid/asks to be returned.aggregation_price_incrementstringThe minimum price intervals at which buy and sell orders are grouped or combined in the order book.ResponseA successful response.pricebookobjectrequiredShow child attributeslaststringmid_marketstringspread_bpsstringspread_absolutestring