---
exchange: coinbase
source_url: https://docs.cdp.coinbase.com/api-reference/advanced-trade-api/rest-api/perpetuals/opt-in-or-out
api_type: REST
updated_at: 2026-07-13 19:16:14.559659
---

# Opt In or Out of Multi Asset Collateral

**Endpoint:** `POST https://api.coinbase.com/api/v3/brokerage/intx/multi_asset_collateral`


Enable or Disable Multi Asset Collateral for a given Portfolio
    
    
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

#### Body

application/json

portfolio_uuid

string

The portfolio UUID.

multi_asset_collateral_enabled

boolean

Enable or disable Multi Asset Collateral.

#### Response

A successful response.

multi_asset_collateral_enabled

boolean