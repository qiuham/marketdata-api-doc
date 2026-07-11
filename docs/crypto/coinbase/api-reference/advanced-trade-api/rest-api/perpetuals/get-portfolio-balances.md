---
exchange: coinbase
source_url: https://docs.cdp.coinbase.com/api-reference/advanced-trade-api/rest-api/perpetuals/get-portfolio-balances
api_type: Account
updated_at: 2026-07-11 19:01:27.995059
---

# Get Portfolios Balances

**Endpoint:** `GET https://api.coinbase.com/api/v3/brokerage/intx/balances/{portfolio_uuid}`


Get a list of asset balances on Intx for a given Portfolio
    
    
    curl --request GET \
      --url https://api.coinbase.com/api/v3/brokerage/intx/balances/{portfolio_uuid} \
      --header 'Authorization: Bearer <token>'
    
    
    import requests  
      
    url = "https://api.coinbase.com/api/v3/brokerage/intx/balances/{portfolio_uuid}"  
      
    headers = {"Authorization": "Bearer <token>"}  
      
    response = requests.get(url, headers=headers)  
      
    print(response.text)
    
    
    const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};  
      
    fetch('https://api.coinbase.com/api/v3/brokerage/intx/balances/{portfolio_uuid}', options)  
      .then(res => res.json())  
      .then(res => console.log(res))  
      .catch(err => console.error(err));
    
    
    <?php  
      
    $curl = curl_init();  
      
    curl_setopt_array($curl, [  
      CURLOPT_URL => "https://api.coinbase.com/api/v3/brokerage/intx/balances/{portfolio_uuid}",  
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
      
    	url := "https://api.coinbase.com/api/v3/brokerage/intx/balances/{portfolio_uuid}"  
      
    	req, _ := http.NewRequest("GET", url, nil)  
      
    	req.Header.Add("Authorization", "Bearer <token>")  
      
    	res, _ := http.DefaultClient.Do(req)  
      
    	defer res.Body.Close()  
    	body, _ := io.ReadAll(res.Body)  
      
    	fmt.Println(string(body))  
      
    }
    
    
    HttpResponse<String> response = Unirest.get("https://api.coinbase.com/api/v3/brokerage/intx/balances/{portfolio_uuid}")  
      .header("Authorization", "Bearer <token>")  
      .asString();
    
    
    require 'uri'  
    require 'net/http'  
      
    url = URI("https://api.coinbase.com/api/v3/brokerage/intx/balances/{portfolio_uuid}")  
      
    http = Net::HTTP.new(url.host, url.port)  
    http.use_ssl = true  
      
    request = Net::HTTP::Get.new(url)  
    request["Authorization"] = 'Bearer <token>'  
      
    response = http.request(request)  
    puts response.read_body
    
    
    {
      "portfolio_balances": [
        {
          "portfolio_uuid": "<string>",
          "balances": [
            {
              "asset": {
                "asset_id": "<string>",
                "asset_uuid": "<string>",
                "asset_name": "<string>",
                "status": "<string>",
                "collateral_weight": "<string>",
                "account_collateral_limit": "<string>",
                "ecosystem_collateral_limit_breached": true,
                "asset_icon_url": "<string>",
                "supported_networks_enabled": true
              },
              "quantity": "<string>",
              "hold": "<string>",
              "transfer_hold": "<string>",
              "collateral_value": "<string>",
              "collateral_weight": "<string>",
              "max_withdraw_amount": "<string>",
              "loan": "<string>",
              "loan_collateral_requirement_usd": "<string>",
              "pledged_quantity": "<string>",
              "max_portfolio_transfer_amount": "<string>"
            }
          ],
          "is_margin_limit_reached": true
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

#### Response

A successful response.

portfolio_balances

object[]