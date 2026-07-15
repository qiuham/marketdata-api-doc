---
exchange: coinbase
source_url: https://docs.cdp.coinbase.com/api-reference/advanced-trade-api/rest-api/futures/get-current-margin-window
api_type: REST
updated_at: 2026-07-15 19:07:35.801531
---

# Get Current Margin Window

**Endpoint:** `GET https://api.coinbase.com/api/v3/brokerage/cfm/intraday/current_margin_window`


Get the futures current margin window
    
    
    curl --request GET \
      --url https://api.coinbase.com/api/v3/brokerage/cfm/intraday/current_margin_window \
      --header 'Authorization: Bearer <token>'
    
    
    import requests  
      
    url = "https://api.coinbase.com/api/v3/brokerage/cfm/intraday/current_margin_window"  
      
    headers = {"Authorization": "Bearer <token>"}  
      
    response = requests.get(url, headers=headers)  
      
    print(response.text)
    
    
    const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};  
      
    fetch('https://api.coinbase.com/api/v3/brokerage/cfm/intraday/current_margin_window', options)  
      .then(res => res.json())  
      .then(res => console.log(res))  
      .catch(err => console.error(err));
    
    
    <?php  
      
    $curl = curl_init();  
      
    curl_setopt_array($curl, [  
      CURLOPT_URL => "https://api.coinbase.com/api/v3/brokerage/cfm/intraday/current_margin_window",  
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
      
    	url := "https://api.coinbase.com/api/v3/brokerage/cfm/intraday/current_margin_window"  
      
    	req, _ := http.NewRequest("GET", url, nil)  
      
    	req.Header.Add("Authorization", "Bearer <token>")  
      
    	res, _ := http.DefaultClient.Do(req)  
      
    	defer res.Body.Close()  
    	body, _ := io.ReadAll(res.Body)  
      
    	fmt.Println(string(body))  
      
    }
    
    
    HttpResponse<String> response = Unirest.get("https://api.coinbase.com/api/v3/brokerage/cfm/intraday/current_margin_window")  
      .header("Authorization", "Bearer <token>")  
      .asString();
    
    
    require 'uri'  
    require 'net/http'  
      
    url = URI("https://api.coinbase.com/api/v3/brokerage/cfm/intraday/current_margin_window")  
      
    http = Net::HTTP.new(url.host, url.port)  
    http.use_ssl = true  
      
    request = Net::HTTP::Get.new(url)  
    request["Authorization"] = 'Bearer <token>'  
      
    response = http.request(request)  
    puts response.read_body
    
    
    {
      "margin_window": {
        "margin_window_type": "MARGIN_WINDOW_TYPE_UNSPECIFIED",
        "end_time": "<string>"
      },
      "is_intraday_margin_killswitch_enabled": true,
      "is_intraday_margin_enrollment_killswitch_enabled": true
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

margin_profile_type

enum<string>

default:MARGIN_PROFILE_TYPE_UNSPECIFIED

The margin profile type for your account.

Available options:

`MARGIN_PROFILE_TYPE_UNSPECIFIED`,

`MARGIN_PROFILE_TYPE_RETAIL_REGULAR`,

`MARGIN_PROFILE_TYPE_RETAIL_INTRADAY_MARGIN_1`

#### Response

A successful response.

margin_window

object

is_intraday_margin_killswitch_enabled

boolean

True if intraday margin killswitch is enabled

is_intraday_margin_enrollment_killswitch_enabled

boolean

True if intraday margin enrollment killswitch is enabled