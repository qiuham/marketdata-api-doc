---
exchange: coinbase
source_url: https://docs.cdp.coinbase.com/api-reference/advanced-trade-api/rest-api/public/get-public-product-book
api_type: Market Data
updated_at: 2026-11-13 18:31:35.619086
---

# Get Public Product Book

**Endpoint:** `GET https://api.coinbase.com/api/v3/brokerage/market/product_book`


Get a list of bids/asks for a single product. The amount of detail shown can be customized with the limit parameter.
    
    
    curl --request GET \
      --url https://api.coinbase.com/api/v3/brokerage/market/product_book
    
    
    import requests
    
    url = "https://api.coinbase.com/api/v3/brokerage/market/product_book"
    
    response = requests.get(url)
    
    print(response.text)
    
    
    const options = {method: 'GET'};
    
    fetch('https://api.coinbase.com/api/v3/brokerage/market/product_book', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.coinbase.com/api/v3/brokerage/market/product_book",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "GET",
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
    
    	url := "https://api.coinbase.com/api/v3/brokerage/market/product_book"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://api.coinbase.com/api/v3/brokerage/market/product_book")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.coinbase.com/api/v3/brokerage/market/product_book")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Get.new(url)
    
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

#### Query Parameters

product_id

string

required

The trading pair (e.g. 'BTC-USD').

limit

integer<int32>Public

# Get Public Product Book

Get a list of bids/asks for a single product. The amount of detail shown can be customized with the limit parameter.

GET

/

api

/

v3

/

brokerage

/

market

/

product_book

Get Public Product Book
    
    
    curl --request GET \
      --url https://api.coinbase.com/api/v3/brokerage/market/product_book
    
    
    import requests
    
    url = "https://api.coinbase.com/api/v3/brokerage/market/product_book"
    
    response = requests.get(url)
    
    print(response.text)
    
    
    const options = {method: 'GET'};
    
    fetch('https://api.coinbase.com/api/v3/brokerage/market/product_book', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.coinbase.com/api/v3/brokerage/market/product_book",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "GET",
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
    
    	url := "https://api.coinbase.com/api/v3/brokerage/market/product_book"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://api.coinbase.com/api/v3/brokerage/market/product_book")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.coinbase.com/api/v3/brokerage/market/product_book")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Get.new(url)
    
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

#### Query Parameters

product_id

string

required

The trading pair (e.g. 'BTC-USD').

limit

integer<int32>

The number of bid/asks to be returned.

aggregation_price_increment

string

The minimum price intervals at which buy and sell orders are grouped or combined in the order book.

#### Response

A successful response.

pricebook

object

required

last

string

mid_market

string

spread_bps

string

spread_absolute

string

Public

# Get Public Product Candles

Get rates for a single product by product ID, grouped in buckets.

GET

/

api

/

v3

/

brokerage

/

market

/

products

/

{product_id}

/

candles

Get Public Product Candles
    
    
    curl --request GET \
      --url https://api.coinbase.com/api/v3/brokerage/market/products/{product_id}/candles
    
    
    import requests
    
    url = "https://api.coinbase.com/api/v3/brokerage/market/products/{product_id}/candles"
    
    response = requests.get(url)
    
    print(response.text)
    
    
    const options = {method: 'GET'};
    
    fetch('https://api.coinbase.com/api/v3/brokerage/market/products/{product_id}/candles', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.coinbase.com/api/v3/brokerage/market/products/{product_id}/candles",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "GET",
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
    
    	url := "https://api.coinbase.com/api/v3/brokerage/market/products/{product_id}/candles"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://api.coinbase.com/api/v3/brokerage/market/products/{product_id}/candles")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.coinbase.com/api/v3/brokerage/market/products/{product_id}/candles")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Get.new(url)
    
    response = http.request(request)
    puts response.read_body
    
    
    {
      "candles": [
        {
          "start": "1639508050",
          "low": "140.21",
          "high": "140.21",
          "open": "140.21",
          "close": "140.21",
          "volume": "56437345"
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

#### Path Parameters

product_id

string

required

The trading pair (e.g. 'BTC-USD').

#### Query Parameters

The number of bid/asks to be returned.

aggregation_price_increment

string

The minimum price intervals at which buy and sell orders are grouped or combined in the order book.

#### Response

A successful response.

pricebook

object

required

last

string

mid_market

string

spread_bps

string

spread_absolute

string