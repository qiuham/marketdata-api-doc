---
exchange: coinbase
source_url: https://docs.cdp.coinbase.com/api-reference/advanced-trade-api/rest-api/futures/cancel-pending-futures-sweep
api_type: REST
updated_at: 2026-07-21 19:14:35.987378
---

# Cancel Pending US Derivatives Sweep

**Endpoint:** `DELETE https://api.coinbase.com/api/v3/brokerage/cfm/sweeps`


Cancel the pending sweep of funds from FCM wallet to USD Spot wallet
    
    
    curl --request DELETE \
      --url https://api.coinbase.com/api/v3/brokerage/cfm/sweeps \
      --header 'Authorization: Bearer <token>'
    
    
    import requests  
      
    url = "https://api.coinbase.com/api/v3/brokerage/cfm/sweeps"  
      
    headers = {"Authorization": "Bearer <token>"}  
      
    response = requests.delete(url, headers=headers)  
      
    print(response.text)
    
    
    const options = {method: 'DELETE', headers: {Authorization: 'Bearer <token>'}};  
      
    fetch('https://api.coinbase.com/api/v3/brokerage/cfm/sweeps', options)  
      .then(res => res.json())  
      .then(res => console.log(res))  
      .catch(err => console.error(err));
    
    
    <?php  
      
    $curl = curl_init();  
      
    curl_setopt_array($curl, [  
      CURLOPT_URL => "https://api.coinbase.com/api/v3/brokerage/cfm/sweeps",  
      CURLOPT_RETURNTRANSFER => true,  
      CURLOPT_ENCODING => "",  
      CURLOPT_MAXREDIRS => 10,  
      CURLOPT_TIMEOUT => 30,  
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,  
      CURLOPT_CUSTOMREQUEST => "DELETE",  
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
      
    	url := "https://api.coinbase.com/api/v3/brokerage/cfm/sweeps"  
      
    	req, _ := http.NewRequest("DELETE", url, nil)  
      
    	req.Header.Add("Authorization", "Bearer <token>")  
      
    	res, _ := http.DefaultClient.Do(req)  
      
    	defer res.Body.Close()  
    	body, _ := io.ReadAll(res.Body)  
      
    	fmt.Println(string(body))  
      
    }
    
    
    HttpResponse<String> response = Unirest.delete("https://api.coinbase.com/api/v3/brokerage/cfm/sweeps")  
      .header("Authorization", "Bearer <token>")  
      .asString();
    
    
    require 'uri'  
    require 'net/http'  
      
    url = URI("https://api.coinbase.com/api/v3/brokerage/cfm/sweeps")  
      
    http = Net::HTTP.new(url.host, url.port)  
    http.use_ssl = true  
      
    request = Net::HTTP::Delete.new(url)  
    request["Authorization"] = 'Bearer <token>'  
      
    response = http.request(request)  
    puts response.read_body
    
    
    {
      "success": true
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

#### Response

A successful response.

success

boolean