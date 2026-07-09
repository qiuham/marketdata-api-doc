---
exchange: coinbase
source_url: https://docs.cdp.coinbase.com/api-reference/advanced-trade-api/rest-api/orders/cancel-order
api_type: Trading
updated_at: 2026-07-09 19:25:35.322931
---

# Cancel Orders

**Endpoint:** `POST https://api.coinbase.com/api/v3/brokerage/orders/batch_cancel`


Initiate cancel requests for one or more orders.
    
    
    curl --request POST \
      --url https://api.coinbase.com/api/v3/brokerage/orders/batch_cancel \
      --header 'Authorization: Bearer <token>' \
      --header 'Content-Type: application/json' \
      --data '
    {
      "order_ids": [
        "0000-00000",
        "1111-11111"
      ]
    }
    '
    
    
    import requests  
      
    url = "https://api.coinbase.com/api/v3/brokerage/orders/batch_cancel"  
      
    payload = { "order_ids": ["0000-00000", "1111-11111"] }  
    headers = {  
        "Authorization": "Bearer <token>",  
        "Content-Type": "application/json"  
    }  
      
    response = requests.post(url, json=payload, headers=headers)  
      
    print(response.text)
    
    
    const options = {  
      method: 'POST',  
      headers: {Authorization: 'Bearer <token>', 'Content-Type': 'application/json'},  
      body: JSON.stringify({order_ids: ['0000-00000', '1111-11111']})  
    };  
      
    fetch('https://api.coinbase.com/api/v3/brokerage/orders/batch_cancel', options)  
      .then(res => res.json())  
      .then(res => console.log(res))  
      .catch(err => console.error(err));
    
    
    <?php  
      
    $curl = curl_init();  
      
    curl_setopt_array($curl, [  
      CURLOPT_URL => "https://api.coinbase.com/api/v3/brokerage/orders/batch_cancel",  
      CURLOPT_RETURNTRANSFER => true,  
      CURLOPT_ENCODING => "",  
      CURLOPT_MAXREDIRS => 10,  
      CURLOPT_TIMEOUT => 30,  
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,  
      CURLOPT_CUSTOMREQUEST => "POST",  
      CURLOPT_POSTFIELDS => json_encode([  
        'order_ids' => [  
            '0000-00000',  
            '1111-11111'  
        ]  
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
      
    	url := "https://api.coinbase.com/api/v3/brokerage/orders/batch_cancel"  
      
    	payload := strings.NewReader("{\n  \"order_ids\": [\n    \"0000-00000\",\n    \"1111-11111\"\n  ]\n}")  
      
    	req, _ := http.NewRequest("POST", url, payload)  
      
    	req.Header.Add("Authorization", "Bearer <token>")  
    	req.Header.Add("Content-Type", "application/json")  
      
    	res, _ := http.DefaultClient.Do(req)  
      
    	defer res.Body.Close()  
    	body, _ := io.ReadAll(res.Body)  
      
    	fmt.Println(string(body))  
      
    }
    
    
    HttpResponse<String> response = Unirest.post("https://api.coinbase.com/api/v3/brokerage/orders/batch_cancel")  
      .header("Authorization", "Bearer <token>")  
      .header("Content-Type", "application/json")  
      .body("{\n  \"order_ids\": [\n    \"0000-00000\",\n    \"1111-11111\"\n  ]\n}")  
      .asString();
    
    
    require 'uri'  
    require 'net/http'  
      
    url = URI("https://api.coinbase.com/api/v3/brokerage/orders/batch_cancel")  
      
    http = Net::HTTP.new(url.host, url.port)  
    http.use_ssl = true  
      
    request = Net::HTTP::Post.new(url)  
    request["Authorization"] = 'Bearer <token>'  
    request["Content-Type"] = 'application/json'  
    request.body = "{\n  \"order_ids\": [\n    \"0000-00000\",\n    \"1111-11111\"\n  ]\n}"  
      
    response = http.request(request)  
    puts response.read_body
    
    
    {
      "results": [
        {
          "success": true,
          "failure_reason": "UNKNOWN_CANCEL_FAILURE_REASON",
          "order_id": "0000-00000"
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

#### Body

application/json

order_ids

string[]

required

The order IDs that cancel requests should be initiated for.

Example:
    
    
    ["0000-00000", "1111-11111"]

#### Response

A successful response.

results

object[]

The result of initiated cancel requests