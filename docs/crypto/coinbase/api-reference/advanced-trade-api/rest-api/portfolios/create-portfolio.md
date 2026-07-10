---
exchange: coinbase
source_url: https://docs.cdp.coinbase.com/api-reference/advanced-trade-api/rest-api/portfolios/create-portfolio
api_type: Account
updated_at: 2026-07-10 19:19:31.207308
---

# Create Portfolio

**Endpoint:** `POST https://api.coinbase.com/api/v3/brokerage/portfolios`


Create a portfolio.
    
    
    curl --request POST \
      --url https://api.coinbase.com/api/v3/brokerage/portfolios \
      --header 'Authorization: Bearer <token>' \
      --header 'Content-Type: application/json' \
      --data '
    {
      "name": "<string>"
    }
    '
    
    
    import requests  
      
    url = "https://api.coinbase.com/api/v3/brokerage/portfolios"  
      
    payload = { "name": "<string>" }  
    headers = {  
        "Authorization": "Bearer <token>",  
        "Content-Type": "application/json"  
    }  
      
    response = requests.post(url, json=payload, headers=headers)  
      
    print(response.text)
    
    
    const options = {  
      method: 'POST',  
      headers: {Authorization: 'Bearer <token>', 'Content-Type': 'application/json'},  
      body: JSON.stringify({name: '<string>'})  
    };  
      
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
      CURLOPT_CUSTOMREQUEST => "POST",  
      CURLOPT_POSTFIELDS => json_encode([  
        'name' => '<string>'  
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
      
    	url := "https://api.coinbase.com/api/v3/brokerage/portfolios"  
      
    	payload := strings.NewReader("{\n  \"name\": \"<string>\"\n}")  
      
    	req, _ := http.NewRequest("POST", url, payload)  
      
    	req.Header.Add("Authorization", "Bearer <token>")  
    	req.Header.Add("Content-Type", "application/json")  
      
    	res, _ := http.DefaultClient.Do(req)  
      
    	defer res.Body.Close()  
    	body, _ := io.ReadAll(res.Body)  
      
    	fmt.Println(string(body))  
      
    }
    
    
    HttpResponse<String> response = Unirest.post("https://api.coinbase.com/api/v3/brokerage/portfolios")  
      .header("Authorization", "Bearer <token>")  
      .header("Content-Type", "application/json")  
      .body("{\n  \"name\": \"<string>\"\n}")  
      .asString();
    
    
    require 'uri'  
    require 'net/http'  
      
    url = URI("https://api.coinbase.com/api/v3/brokerage/portfolios")  
      
    http = Net::HTTP.new(url.host, url.port)  
    http.use_ssl = true  
      
    request = Net::HTTP::Post.new(url)  
    request["Authorization"] = 'Bearer <token>'  
    request["Content-Type"] = 'application/json'  
    request.body = "{\n  \"name\": \"<string>\"\n}"  
      
    response = http.request(request)  
    puts response.read_body
    
    
    {
      "portfolio": {
        "name": "<string>",
        "uuid": "<string>",
        "type": "UNDEFINED",
        "deleted": true
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

#### Authorizations

Authorization

string

header

required

A JWT signed using your CDP API Key Secret, encoded in base64. Refer to the [Creating API Keys](/coinbase-app/authentication-authorization/api-key-authentication) section of our Coinbase App Authentication docs for information on how to generate your Bearer Token.

#### Body

application/json

name

string

The name of the portfolio.

#### Response

A successful response.

portfolio

object

Portfolio is the identifying information for a portfolio.