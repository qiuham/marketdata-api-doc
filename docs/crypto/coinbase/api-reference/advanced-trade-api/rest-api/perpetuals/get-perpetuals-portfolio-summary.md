---
exchange: coinbase
source_url: https://docs.cdp.coinbase.com/api-reference/advanced-trade-api/rest-api/perpetuals/get-perpetuals-portfolio-summary
api_type: Account
updated_at: 2026-07-12 19:04:36.763944
---

# Get Perpetuals Portfolio Summary

**Endpoint:** `GET https://api.coinbase.com/api/v3/brokerage/intx/portfolio/{portfolio_uuid}`


Get a summary of your Perpetuals portfolio
    
    
    curl --request GET \
      --url https://api.coinbase.com/api/v3/brokerage/intx/portfolio/{portfolio_uuid} \
      --header 'Authorization: Bearer <token>'
    
    
    import requests  
      
    url = "https://api.coinbase.com/api/v3/brokerage/intx/portfolio/{portfolio_uuid}"  
      
    headers = {"Authorization": "Bearer <token>"}  
      
    response = requests.get(url, headers=headers)  
      
    print(response.text)
    
    
    const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};  
      
    fetch('https://api.coinbase.com/api/v3/brokerage/intx/portfolio/{portfolio_uuid}', options)  
      .then(res => res.json())  
      .then(res => console.log(res))  
      .catch(err => console.error(err));
    
    
    <?php  
      
    $curl = curl_init();  
      
    curl_setopt_array($curl, [  
      CURLOPT_URL => "https://api.coinbase.com/api/v3/brokerage/intx/portfolio/{portfolio_uuid}",  
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
      
    	url := "https://api.coinbase.com/api/v3/brokerage/intx/portfolio/{portfolio_uuid}"  
      
    	req, _ := http.NewRequest("GET", url, nil)  
      
    	req.Header.Add("Authorization", "Bearer <token>")  
      
    	res, _ := http.DefaultClient.Do(req)  
      
    	defer res.Body.Close()  
    	body, _ := io.ReadAll(res.Body)  
      
    	fmt.Println(string(body))  
      
    }
    
    
    HttpResponse<String> response = Unirest.get("https://api.coinbase.com/api/v3/brokerage/intx/portfolio/{portfolio_uuid}")  
      .header("Authorization", "Bearer <token>")  
      .asString();
    
    
    require 'uri'  
    require 'net/http'  
      
    url = URI("https://api.coinbase.com/api/v3/brokerage/intx/portfolio/{portfolio_uuid}")  
      
    http = Net::HTTP.new(url.host, url.port)  
    http.use_ssl = true  
      
    request = Net::HTTP::Get.new(url)  
    request["Authorization"] = 'Bearer <token>'  
      
    response = http.request(request)  
    puts response.read_body
    
    
    {
      "portfolios": [
        {
          "portfolio_uuid": "<string>",
          "collateral": "<string>",
          "position_notional": "<string>",
          "open_position_notional": "<string>",
          "pending_fees": "<string>",
          "borrow": "<string>",
          "accrued_interest": "<string>",
          "rolling_debt": "<string>",
          "portfolio_initial_margin": "<string>",
          "portfolio_im_notional": {
            "value": "<string>",
            "currency": "<string>"
          },
          "portfolio_maintenance_margin": "<string>",
          "portfolio_mm_notional": {
            "value": "<string>",
            "currency": "<string>"
          },
          "liquidation_percentage": "<string>",
          "liquidation_buffer": "<string>",
          "margin_type": "MARGIN_TYPE_UNSPECIFIED",
          "margin_flags": "PORTFOLIO_MARGIN_FLAGS_UNSPECIFIED",
          "liquidation_status": "PORTFOLIO_LIQUIDATION_STATUS_UNSPECIFIED",
          "unrealized_pnl": {
            "value": "<string>",
            "currency": "<string>"
          },
          "total_balance": {
            "value": "<string>",
            "currency": "<string>"
          }
        }
      ],
      "summary": {
        "unrealized_pnl": {
          "value": "<string>",
          "currency": "<string>"
        },
        "buying_power": {
          "value": "<string>",
          "currency": "<string>"
        },
        "total_balance": {
          "value": "<string>",
          "currency": "<string>"
        },
        "max_withdrawal_amount": {
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
        {  
          "type_url": "<string>",  
          "value": "aSDinaTvuI8gbWludGxpZnk="  
        }  
      ]  
    }

**Deprecated — retires September 9, 2026.** This INTX perpetuals endpoint is being replaced by the [Deribit-powered derivatives gateway](/coinbase-app/advanced-trade-apis/guides/derivatives/overview). Migrate before the cutover — see the [Migration Overview](/coinbase-app/advanced-trade-apis/guides/derivatives/overview).

#### Authorizations

Authorization

string

header

required

A JWT signed using your CDP API Key Secret, encoded in base64. Refer to the [Creating API Keys](/coinbase-app/authentication-authorization/api-key-authentication) section of our Coinbase App Authentication docs for information on how to generate your Bearer Token.

#### Path Parameters

portfolio_uuid

string

required

The portfolio UUID.

#### Response

A successful response.

portfolios

object[]

summary

object