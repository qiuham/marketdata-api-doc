---
exchange: coinbase
source_url: https://docs.cdp.coinbase.com/api-reference/advanced-trade-api/rest-api/fees/get-transaction-summary
api_type: REST
updated_at: 2026-07-12 19:04:35.602080
---

# Get Transaction Summary

**Endpoint:** `GET https://api.coinbase.com/api/v3/brokerage/transaction_summary`


Get a summary of transactions with fee tiers, total volume, and fees.
    
    
    curl --request GET \
      --url https://api.coinbase.com/api/v3/brokerage/transaction_summary \
      --header 'Authorization: Bearer <token>'
    
    
    import requests  
      
    url = "https://api.coinbase.com/api/v3/brokerage/transaction_summary"  
      
    headers = {"Authorization": "Bearer <token>"}  
      
    response = requests.get(url, headers=headers)  
      
    print(response.text)
    
    
    const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};  
      
    fetch('https://api.coinbase.com/api/v3/brokerage/transaction_summary', options)  
      .then(res => res.json())  
      .then(res => console.log(res))  
      .catch(err => console.error(err));
    
    
    <?php  
      
    $curl = curl_init();  
      
    curl_setopt_array($curl, [  
      CURLOPT_URL => "https://api.coinbase.com/api/v3/brokerage/transaction_summary",  
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
      
    	url := "https://api.coinbase.com/api/v3/brokerage/transaction_summary"  
      
    	req, _ := http.NewRequest("GET", url, nil)  
      
    	req.Header.Add("Authorization", "Bearer <token>")  
      
    	res, _ := http.DefaultClient.Do(req)  
      
    	defer res.Body.Close()  
    	body, _ := io.ReadAll(res.Body)  
      
    	fmt.Println(string(body))  
      
    }
    
    
    HttpResponse<String> response = Unirest.get("https://api.coinbase.com/api/v3/brokerage/transaction_summary")  
      .header("Authorization", "Bearer <token>")  
      .asString();
    
    
    require 'uri'  
    require 'net/http'  
      
    url = URI("https://api.coinbase.com/api/v3/brokerage/transaction_summary")  
      
    http = Net::HTTP.new(url.host, url.port)  
    http.use_ssl = true  
      
    request = Net::HTTP::Get.new(url)  
    request["Authorization"] = 'Bearer <token>'  
      
    response = http.request(request)  
    puts response.read_body
    
    
    {
      "total_fees": 25,
      "fee_tier": {
        "pricing_tier": "<$10k",
        "taker_fee_rate": "0.0010",
        "maker_fee_rate": "0.0020",
        "aop_from": "0",
        "aop_to": "10000",
        "volume_types_and_range": [
          {
            "volume_types": [
              "VOLUME_TYPE_SPOT",
              "VOLUME_TYPE_US_DERIVATIVES"
            ],
            "vol_from": "0",
            "vol_to": "50000"
          }
        ]
      },
      "margin_rate": 0.5,
      "goods_and_services_tax": {
        "rate": "<string>",
        "type": "INCLUSIVE"
      },
      "advanced_trade_only_volume": 1000,
      "advanced_trade_only_fees": 25,
      "coinbase_pro_volume": 1000,
      "coinbase_pro_fees": 25,
      "total_balance": "1000",
      "volume_breakdown": [
        {
          "volume_type": "VOLUME_TYPE_SPOT",
          "volume": 1000
        }
      ],
      "has_cost_plus_commission": false
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

#### Query Parameters

product_type

enum<string>

default:UNKNOWN_PRODUCT_TYPE

Only returns the orders matching this product type. By default, returns all product types.

Available options:

`UNKNOWN_PRODUCT_TYPE`,

`SPOT`,

`FUTURE`

contract_expiry_type

enum<string>

default:UNKNOWN_CONTRACT_EXPIRY_TYPE

Only returns the orders matching this contract expiry type. Only applicable if product_type is set to FUTURE.

Available options:

`UNKNOWN_CONTRACT_EXPIRY_TYPE`,

`EXPIRING`,

`PERPETUAL`

product_venue

enum<string>

default:UNKNOWN_VENUE_TYPE

Venue for product

Available options:

`UNKNOWN_VENUE_TYPE`,

`CBE`,

`FCM`,

`INTX`

#### Response

A successful response.

total_fees

number<double>

required

Total fees across assets, denoted in USD.

Example:

`25`

fee_tier

object

required

Description of maker and taker rates across all applicable fee tiers.

margin_rate

object

Margin rate, only applicable to product_type `FUTURE`.

Example:

`0.5`

goods_and_services_tax

object

advanced_trade_only_volume

number<double>

Advanced Trade volume (non-inclusive of Pro) across assets, denoted in USD.

Example:

`1000`

advanced_trade_only_fees

number<double>

Advanced Trade fees (non-inclusive of Pro) across assets, denoted in USD.

Example:

`25`

coinbase_pro_volume

number<double>

Coinbase Pro volume across assets, denoted in USD.

Example:

`1000`

coinbase_pro_fees

number<double>

Coinbase Pro fees across assets, denoted in USD.

Example:

`25`

total_balance

string

Total balance across assets and products, which is comprised of the sum of spot, intx, and fcm, and denoted in USD.

Example:

`"1000"`

volume_breakdown

object[]

Breakdown of volumes that contributed to the fee tier calculation.

Example:
    
    
    [  
      {  
        "volume_type": "VOLUME_TYPE_SPOT",  
        "volume": 1000  
      }  
    ]

has_cost_plus_commission

boolean

Indicates whether the user uses cost plus commission pricing model.

Example:

`false`