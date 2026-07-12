---
exchange: coinbase
source_url: https://docs.cdp.coinbase.com/api-reference/advanced-trade-api/rest-api/public/get-public-product-candles
api_type: Market Data
updated_at: 2026-07-12 19:04:37.574214
---

# Get Public Product Candles

**Endpoint:** `GET https://api.coinbase.com/api/v3/brokerage/market/products/{product_id}/candles`


Get rates for a single product by product ID, grouped in buckets.
    
    
    curl --request GET \
      --url https://api.coinbase.com/api/v3/brokerage/market/products/{product_id}/candles \
      --header 'Authorization: Bearer <token>'
    
    
    import requests  
      
    url = "https://api.coinbase.com/api/v3/brokerage/market/products/{product_id}/candles"  
      
    headers = {"Authorization": "Bearer <token>"}  
      
    response = requests.get(url, headers=headers)  
      
    print(response.text)
    
    
    const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};  
      
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
      
    	url := "https://api.coinbase.com/api/v3/brokerage/market/products/{product_id}/candles"  
      
    	req, _ := http.NewRequest("GET", url, nil)  
      
    	req.Header.Add("Authorization", "Bearer <token>")  
      
    	res, _ := http.DefaultClient.Do(req)  
      
    	defer res.Body.Close()  
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
      --url https://api.coinbase.com/api/v3/brokerage/market/products/{product_id}/candles \
      --header 'Authorization: Bearer <token>'
    
    
    import requests  
      
    url = "https://api.coinbase.com/api/v3/brokerage/market/products/{product_id}/candles"  
      
    headers = {"Authorization": "Bearer <token>"}  
      
    response = requests.get(url, headers=headers)  
      
    print(response.text)
    
    
    const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};  
      
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
      
    	url := "https://api.coinbase.com/api/v3/brokerage/market/products/{product_id}/candles"  
      
    	req, _ := http.NewRequest("GET", url, nil)  
      
    	req.Header.Add("Authorization", "Bearer <token>")  
      
    	res, _ := http.DefaultClient.Do(req)  
      
    	defer res.Body.Close()  
    	body, _	body, _ := io.ReadAll(res.Body)  
      
    	fmt.Println(string(body))  
      
    }
    
    
    HttpResponse<String> response = Unirest.get("https://api.coinbase.com/api/v3/brokerage/market/products/{product_id}/candles")  
      .header("Authorization", "Bearer <token>")  
      .asString();
    
    
    require 'uri'  
    require 'net/http'  
      
    url = URI("https://api.coinbase.com/api/v3/brokerage/market/products/{product_id}/candles")  
      
    http = Net::HTTP.new(url.host, url.port)  
    http.use_ssl = true  
      
    request = Net::HTTP::Get.new(url)  
    request["Authorization"] = 'Bearer <token>'  
      
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