---
exchange: coinbase
source_url: https://docs.cdp.coinbase.com/api-reference/advanced-trade-api/rest-api/public/get-public-product-candles
api_type: Market Data
updated_at: 2026-08-26 19:27:23.212196
---

# Get Public Product Candles

**Endpoint:** `GET https://api.coinbase.com/api/v3/brokerage/market/products/{product_id}/candles`


Get rates for a single product by product ID, grouped in buckets.
    
    
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

start

string

required

The UNIX timestamp indicating the start of the time interval.

end

string

required

The UNIX timestamp indicating the end of the time interval.

granularity

enum<string>

default:UNKNOWN_GRANULARITY

required

The timeframe each candle represents.

Available options:

`UNKNOWN_GRANULARITY`,

`ONE_MINUTE`,

`FIVE_MINUTE`,

`FIFTEEN_MINUTE`,

`THIRTY_MINUTE`,

`ONE_HOUR`,

`TWO_HOUR`,

`FOUR_HOUR`,

`SIX_HOUR`,

`ONE_DAY`

limit

integer<int32>

The number of candle buckets to be returned. By default, returns 350 (max 350).

#### Response

A successful response.

candles

object[]