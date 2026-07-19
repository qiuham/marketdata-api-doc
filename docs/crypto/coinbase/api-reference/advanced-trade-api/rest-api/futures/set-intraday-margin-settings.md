---
exchange: coinbase
source_url: https://docs.cdp.coinbase.com/api-reference/advanced-trade-api/rest-api/futures/set-intraday-margin-settings
api_type: REST
updated_at: 2026-07-19 19:04:05.915585
---

# Set Intraday Margin Setting

**Endpoint:** `POST https://api.coinbase.com/api/v3/brokerage/cfm/intraday/margin_setting`


Set the futures intraday margin setting
    
    
    curl --request POST \
      --url https://api.coinbase.com/api/v3/brokerage/cfm/intraday/margin_setting \
      --header 'Authorization: Bearer <token>' \
      --header 'Content-Type: application/json' \
      --data '
    {
      "setting": "INTRADAY_MARGIN_SETTING_UNSPECIFIED"
    }
    '
    
    
    import requests  
      
    url = "https://api.coinbase.com/api/v3/brokerage/cfm/intraday/margin_setting"  
      
    payload = { "setting": "INTRADAY_MARGIN_SETTING_UNSPECIFIED" }  
    headers = {  
        "Authorization": "Bearer <token>",  
        "Content-Type": "application/json"  
    }  
      
    response = requests.post(url, json=payload, headers=headers)  
      
    print(response.text)
    
    
    const options = {  
      method: 'POST',  
      headers: {Authorization: 'Bearer <token>', 'Content-Type': 'application/json'},  
      body: JSON.stringify({setting: 'INTRADAY_MARGIN_SETTING_UNSPECIFIED'})  
    };  
      
    fetch('https://api.coinbase.com/api/v3/brokerage/cfm/intraday/margin_setting', options)  
      .then(res => res.json())  
      .then(res => console.log(res))  
      .catch(err => console.error(err));
    
    
    <?php  
      
    $curl = curl_init();  
      
    curl_setopt_array($curl, [  
      CURLOPT_URL => "https://api.coinbase.com/api/v3/brokerage/cfm/intraday/margin_setting",  
      CURLOPT_RETURNTRANSFER => true,  
      CURLOPT_ENCODING => "",  
      CURLOPT_MAXREDIRS => 10,  
      CURLOPT_TIMEOUT => 30,  
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,  
      CURLOPT_CUSTOMREQUEST => "POST",  
      CURLOPT_POSTFIELDS => json_encode([  
        'setting' => 'INTRADAY_MARGIN_SETTING_UNSPECIFIED'  
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
      
    	url := "https://api.coinbase.com/api/v3/brokerage/cfm/intraday/margin_setting"  
      
    	payload := strings.NewReader("{\n  \"setting\": \"INTRADAY_MARGIN_SETTING_UNSPECIFIED\"\n}")  
      
    	req, _ := http.NewRequest("POST", url, payload)  
      
    	req.Header.Add("Authorization", "Bearer <token>")  
    	req.Header.Add("Content-Type", "application/json")  
      
    	res, _ := http.DefaultClient.Do(req)  
      
    	defer res.Body.Close()  
    	body, _ := io.ReadAll(res.Body)  
      
    	fmt.Println(string(body))  
      
    }
    
    
    HttpResponse<String> response = Unirest.post("https://api.coinbase.com/api/v3/brokerage/cfm/intraday/margin_setting")  
      .header("Authorization", "Bearer <token>")  
      .header("Content-Type", "application/json")  
      .body("{\n  \"setting\": \"INTRADAY_MARGIN_SETTING_UNSPECIFIED\"\n}")  
      .asString();
    
    
    require 'uri'  
    require 'net/http'  
      
    url = URI("https://api.coinbase.com/api/v3/brokerage/cfm/intraday/margin_setting")  
      
    http = Net::HTTP.new(url.host, url.port)  
    http.use_ssl = true  
      
    request = Net::HTTP::Post.new(url)  
    request["Authorization"] = 'Bearer <token>'  
    request["Content-Type"] = 'application/json'  
    request.body = "{\n  \"setting\": \"INTRADAY_MARGIN_SETTING_UNSPECIFIED\"\n}"  
      
    response = http.request(request)  
    puts response.read_body
    
    
    {}
    
    
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

setting

enum<string>

default:INTRADAY_MARGIN_SETTING_UNSPECIFIED

The margin setting for the account. Describes whether the account is opted in to receive increased leverage during weekdays (8am-4pm ET), excluding [market holidays](https://www.coinbase.com/derivatives/market-notices).

Available options:

`INTRADAY_MARGIN_SETTING_UNSPECIFIED`,

`INTRADAY_MARGIN_SETTING_STANDARD`,

`INTRADAY_MARGIN_SETTING_INTRADAY`

#### Response

A successful response.

The response is of type `SetIntradayMarginSettingResponse · object`.