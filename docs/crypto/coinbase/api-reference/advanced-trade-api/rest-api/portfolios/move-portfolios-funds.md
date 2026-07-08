---
exchange: coinbase
source_url: https://docs.cdp.coinbase.com/api-reference/advanced-trade-api/rest-api/portfolios/move-portfolios-funds
api_type: Account
updated_at: 2026-07-08 19:16:23.977187
---

# Move Portfolio Funds

**Endpoint:** `POST https://api.coinbase.com/api/v3/brokerage/portfolios/move_funds`


Move funds between portfolios.
    
    
    curl --request POST \
      --url https://api.coinbase.com/api/v3/brokerage/portfolios/move_funds \
      --header 'Authorization: Bearer <token>' \
      --header 'Content-Type: application/json' \
      --data '
    {
      "funds": {
        "value": "<string>",
        "currency": "<string>"
      },
      "source_portfolio_uuid": "8bfc20d7-f7c6-4422-bf07-8243ca4169fe",
      "target_portfolio_uuid": "8bfc20d7-f7c6-4422-bf07-8243ca4169fe"
    }
    '
    
    
    import requests  
      
    url = "https://api.coinbase.com/api/v3/brokerage/portfolios/move_funds"  
      
    payload = {  
        "funds": {  
            "value": "<string>",  
            "currency": "<string>"  
        },  
        "source_portfolio_uuid": "8bfc20d7-f7c6-4422-bf07-8243ca4169fe",  
        "target_portfolio_uuid": "8bfc20d7-f7c6-4422-bf07-8243ca4169fe"  
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
      body: JSON.stringify({  
        funds: {value: '<string>', currency: '<string>'},  
        source_portfolio_uuid: '8bfc20d7-f7c6-4422-bf07-8243ca4169fe',  
        target_portfolio_uuid: '8bfc20d7-f7c6-4422-bf07-8243ca4169fe'  
      })  
    };  
      
    fetch('https://api.coinbase.com/api/v3/brokerage/portfolios/move_funds', options)  
      .then(res => res.json())  
      .then(res => console.log(res))  
      .catch(err => console.error(err));
    
    
    <?php  
      
    $curl = curl_init();  
      
    curl_setopt_array($curl, [  
      CURLOPT_URL => "https://api.coinbase.com/api/v3/brokerage/portfolios/move_funds",  
      CURLOPT_RETURNTRANSFER => true,  
      CURLOPT_ENCODING => "",  
      CURLOPT_MAXREDIRS => 10,  
      CURLOPT_TIMEOUT => 30,  
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,  
      CURLOPT_CUSTOMREQUEST => "POST",  
      CURLOPT_POSTFIELDS => json_encode([  
        'funds' => [  
            'value' => '<string>',  
            'currency' => '<string>'  
        ],  
        'source_portfolio_uuid' => '8bfc20d7-f7c6-4422-bf07-8243ca4169fe',  
        'target_portfolio_uuid' => '8bfc20d7-f7c6-4422-bf07-8243ca4169fe'  
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
      
    	url := "https://api.coinbase.com/api/v3/brokerage/portfolios/move_funds"  
      
    	payload := strings.NewReader("{\n  \"funds\": {\n    \"value\": \"<string>\",\n    \"currency\": \"<string>\"\n  },\n  \"source_portfolio_uuid\": \"8bfc20d7-f7c6-4422-bf07-8243ca4169fe\",\n  \"target_portfolio_uuid\": \"8bfc20d7-f7c6-4422-bf07-8243ca4169fe\"\n}")  
      
    	req, _ := http.NewRequest("POST", url, payload)  
      
    	req.Header.Add("Authorization", "Bearer <token>")  
    	req.Header.Add("Content-Type", "application/json")  
      
    	res, _ := http.DefaultClient.Do(req)  
      
    	defer res.Body.Close()  
    	body, _ := io.ReadAll(res.Body)  
      
    	fmt.Println(string(body))  
      
    }
    
    
    HttpResponse<String> response = Unirest.post("https://api.coinbase.com/api/v3/brokerage/portfolios/move_funds")  
      .header("Authorization", "Bearer <token>")  
      .header("Content-Type", "application/json")  
      .body("{\n  \"funds\": {\n    \"value\": \"<string>\",\n    \"currency\": \"<string>\"\n  },\n  \"source_portfolio_uuid\": \"8bfc20d7-f7c6-4422-bf07-8243ca4169fe\",\n  \"target_portfolio_uuid\": \"8bfc20d7-f7c6-4422-bf07-8243ca4169fe\"\n}")  
      .asString();
    
    
    require 'uri'  
    require 'net/http'  
      
    url = URI("https://api.coinbase.com/api/v3/brokerage/portfolios/move_funds")  
      
    http = Net::HTTP.new(url.host, url.port)  
    http.use_ssl = true  
      
    request = Net::HTTP::Post.new(url)  
    request["Authorization"] = 'Bearer <token>'  
    request["Content-Type"] = 'application/json'  
    request.body = "{\n  \"funds\": {\n    \"value\": \"<string>\",\n    \"currency\": \"<string>\"\n  },\n  \"source_portfolio_uuid\": \"8bfc20d7-f7c6-4422-bf07-8243ca4169fe\",\n  \"target_portfolio_uuid\": \"8bfc20d7-f7c6-4422-bf07-8243ca4169fe\"\n}"  
      
    response = http.request(request)  
    puts response.read_body
    
    
    {
      "source_portfolio_uuid": "8bfc20d7-f7c6-4422-bf07-8243ca4169fe",
      "target_portfolio_uuid": "8bfc20d7-f7c6-4422-bf07-8243ca4169fe"
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

funds

object

The amount to be moved to the specified portfolio.

source_portfolio_uuid

string

The UUID of the portfolio to send funds from.

Example:

`"8bfc20d7-f7c6-4422-bf07-8243ca4169fe"`

target_portfolio_uuid

string

The UUID of the portfolio to send funds to.

Example:

`"8bfc20d7-f7c6-4422-bf07-8243ca4169fe"`

#### Response

A successful response.

source_portfolio_uuid

string

The UUID of the portfolio to send funds from.

Example:

`"8bfc20d7-f7c6-4422-bf07-8243ca4169fe"`

target_portfolio_uuid

string

The UUID of the portfolio to send funds to.

Example:

`"8bfc20d7-f7c6-4422-bf07-8243ca4169fe"`