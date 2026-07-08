---
exchange: coinbase
source_url: https://docs.cdp.coinbase.com/api-reference/advanced-trade-api/rest-api/orders/edit-order
api_type: Trading
updated_at: 2026-07-08 19:16:23.042212
---

# Edit Order

**Endpoint:** `POST https://api.coinbase.com/api/v3/brokerage/orders/edit`


Edit an order with a specified new `size`, or new `price`.
    
    
    curl --request POST \
      --url https://api.coinbase.com/api/v3/brokerage/orders/edit \
      --header 'Authorization: Bearer <token>' \
      --header 'Content-Type: application/json' \
      --data '
    {
      "order_id": "<string>",
      "price": "19000.00",
      "size": "0.001",
      "attached_order_configuration": {
        "market_market_ioc": {
          "quote_size": "10.00",
          "base_size": "0.001",
          "rfq_disabled": true
        },
        "market_market_fok": {
          "quote_size": "10.00",
          "base_size": "0.001",
          "rfq_disabled": true
        },
        "sor_limit_ioc": {
          "quote_size": "10.00",
          "base_size": "0.001",
          "limit_price": "10000.00",
          "rfq_disabled": true
        },
        "limit_limit_gtc": {
          "quote_size": "10.00",
          "base_size": "0.001",
          "limit_price": "10000.00",
          "post_only": false,
          "rfq_disabled": true
        },
        "limit_limit_gtd": {
          "quote_size": "10.00",
          "base_size": "0.001",
          "limit_price": "10000.00",
          "end_time": "2021-05-31T09:59:59.000Z",
          "post_only": false
        },
        "limit_limit_fok": {
          "quote_size": "10.00",
          "base_size": "0.001",
          "limit_price": "10000.00",
          "rfq_disabled": true
        },
        "twap_limit_gtd": {
          "quote_size": "10.00",
          "base_size": "0.001",
          "start_time": "2021-05-31T07:59:59.000Z",
          "end_time": "2021-05-31T09:59:59.000Z",
          "limit_price": "10000.00",
          "number_buckets": "5",
          "bucket_size": "2.00",
          "bucket_duration": "300s"
        },
        "stop_limit_stop_limit_gtc": {
          "base_size": "0.001",
          "limit_price": "10000.00",
          "stop_price": "20000.00",
          "stop_direction": "20000.00"
        },
        "stop_limit_stop_limit_gtd": {
          "base_size": 0.001,
          "limit_price": "10000.00",
          "stop_price": "20000.00",
          "end_time": "2021-05-31T09:59:59.000Z",
          "stop_direction": "20000.00"
        },
        "trigger_bracket_gtc": {
          "base_size": 0.001,
          "limit_price": "10000.00",
          "stop_trigger_price": "20000.00"
        },
        "trigger_bracket_gtd": {
          "base_size": 0.001,
          "limit_price": "10000.00",
          "stop_trigger_price": "20000.00",
          "end_time": "2021-05-31T09:59:59.000Z"
        },
        "scaled_limit_gtc": {
          "orders": [
            {
              "quote_size": "10.00",
              "base_size": "0.001",
              "limit_price": "10000.00",
              "post_only": false,
              "rfq_disabled": true
            }
          ],
          "quote_size": "<string>",
          "base_size": "<string>",
          "num_orders": 123,
          "min_price": "<string>",
          "max_price": "<string>",
          "price_distribution": "FLAT",
          "size_distribution": "UNKNOWN_DISTRIBUTION",
          "size_diff": "<string>",
          "size_ratio": "<string>"
        }
      },
      "cancel_attached_order": "true",
      "stop_price": "17000.00",
      "average_entry_price": "18000.00"
    }
    '
    
    
    import requests  
      
    url = "https://api.coinbase.com/api/v3/brokerage/orders/edit"  
      
    payload = {  
        "order_id": "<string>",  
        "price": "19000.00",  
        "size": "0.001",  
        "attached_order_configuration": {  
            "market_market_ioc": {  
                "quote_size": "10.00",  
                "base_size": "0.001",  
                "rfq_disabled": True  
            },  
            "market_market_fok": {  
                "quote_size": "10.00",  
                "base_size": "0.001",  
                "rfq_disabled": True  
            },  
            "sor_limit_ioc": {  
                "quote_size": "10.00",  
                "base_size": "0.001",  
                "limit_price": "10000.00",  
                "rfq_disabled": True  
            },  
            "limit_limit_gtc": {  
                "quote_size": "10.00",  
                "base_size": "0.001",  
                "limit_price": "10000.00",  
                "post_only": False,  
                "rfq_disabled": True  
            },  
            "limit_limit_gtd": {  
                "quote_size": "10.00",  
                "base_size": "0.001",  
                "limit_price": "10000.00",  
                "end_time": "2021-05-31T09:59:59.000Z",  
                "post_only": False  
            },  
            "limit_limit_fok": {  
                "quote_size": "10.00",  
                "base_size": "0.001",  
                "limit_price": "10000.00",  
                "rfq_disabled": True  
            },  
            "twap_limit_gtd": {  
                "quote_size": "10.00",  
                "base_size": "0.001",  
                "start_time": "2021-05-31T07:59:59.000Z",  
                "end_time": "2021-05-31T09:59:59.000Z",  
                "limit_price": "10000.00",  
                "number_buckets": "5",  
                "bucket_size": "2.00",  
                "bucket_duration": "300s"  
            },  
            "stop_limit_stop_limit_gtc": {  
                "base_size": "0.001",  
                "limit_price": "10000.00",  
                "stop_price": "20000.00",  
                "stop_direction": "20000.00"  
            },  
            "stop_limit_stop_limit_gtd": {  
                "base_size": 0.001,  
                "limit_price": "10000.00",  
                "stop_price": "20000.00",  
                "end_time": "2021-05-31T09:59:59.000Z",  
                "stop_direction": "20000.00"  
            },  
            "trigger_bracket_gtc": {  
                "base_size": 0.001,  
                "limit_price": "10000.00",  
                "stop_trigger_price": "20000.00"  
            },  
            "trigger_bracket_gtd": {  
                "base_size": 0.001,  
                "limit_price": "10000.00",  
                "stop_trigger_price": "20000.00",  
                "end_time": "2021-05-31T09:59:59.000Z"  
            },  
            "scaled_limit_gtc": {  
                "orders": [  
                    {  
                        "quote_size": "10.00",  
                        "base_size": "0.001",  
                        "limit_price": "10000.00",  
                        "post_only": False,  
                        "rfq_disabled": True  
                    }  
                ],  
                "quote_size": "<string>",  
                "base_size": "<string>",  
                "num_orders": 123,  
                "min_price": "<string>",  
                "max_price": "<string>",  
                "price_distribution": "FLAT",  
                "size_distribution": "UNKNOWN_DISTRIBUTION",  
                "size_diff": "<string>",  
                "size_ratio": "<string>"  
            }  
        },  
        "cancel_attached_order": "true",  
        "stop_price": "17000.00",  
        "average_entry_price": "18000.00"  
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
        order_id: '<string>',  
        price: '19000.00',  
        size: '0.001',  
        attached_order_configuration: {  
          market_market_ioc: {quote_size: '10.00', base_size: '0.001', rfq_disabled: true},  
          market_market_fok: {quote_size: '10.00', base_size: '0.001', rfq_disabled: true},  
          sor_limit_ioc: {  
            quote_size: '10.00',  
            base_size: '0.001',  
            limit_price: '10000.00',  
            rfq_disabled: true  
          },  
          limit_limit_gtc: {  
            quote_size: '10.00',  
            base_size: '0.001',  
            limit_price: '10000.00',  
            post_only: false,  
            rfq_disabled: true  
          },  
          limit_limit_gtd: {  
            quote_size: '10.00',  
            base_size: '0.001',  
            limit_price: '10000.00',  
            end_time: '2021-05-31T09:59:59.000Z',  
            post_only: false  
          },  
          limit_limit_fok: {  
            quote_size: '10.00',  
            base_size: '0.001',  
            limit_price: '10000.00',  
            rfq_disabled: true  
          },  
          twap_limit_gtd: {  
            quote_size: '10.00',  
            base_size: '0.001',  
            start_time: '2021-05-31T07:59:59.000Z',  
            end_time: '2021-05-31T09:59:59.000Z',  
            limit_price: '10000.00',  
            number_buckets: '5',  
            bucket_size: '2.00',  
            bucket_duration: '300s'  
          },  
          stop_limit_stop_limit_gtc: {  
            base_size: '0.001',  
            limit_price: '10000.00',  
            stop_price: '20000.00',  
            stop_direction: '20000.00'  
          },  
          stop_limit_stop_limit_gtd: {  
            base_size: 0.001,  
            limit_price: '10000.00',  
            stop_price: '20000.00',  
            end_time: '2021-05-31T09:59:59.000Z',  
            stop_direction: '20000.00'  
          },  
          trigger_bracket_gtc: {base_size: 0.001, limit_price: '10000.00', stop_trigger_price: '20000.00'},  
          trigger_bracket_gtd: {  
            base_size: 0.001,  
            limit_price: '10000.00',  
            stop_trigger_price: '20000.00',  
            end_time: '2021-05-31T09:59:59.000Z'  
          },  
          scaled_limit_gtc: {  
            orders: [  
              {  
                quote_size: '10.00',  
                base_size: '0.001',  
                limit_price: '10000.00',  
                post_only: false,  
                rfq_disabled: true  
              }  
            ],  
            quote_size: '<string>',  
            base_size: '<string>',  
            num_orders: 123,  
            min_price: '<string>',  
            max_price: '<string>',  
            price_distribution: 'FLAT',  
            size_distribution: 'UNKNOWN_DISTRIBUTION',  
            size_diff: '<string>',  
            size_ratio: '<string>'  
          }  
        },  
        cancel_attached_order: 'true',  
        stop_price: '17000.00',  
        average_entry_price: '18000.00'  
      })  
    };  
      
    fetch('https://api.coinbase.com/api/v3/brokerage/orders/edit', options)  
      .then(res => res.json())  
      .then(res => console.log(res))  
      .catch(err => console.error(err));
    
    
    <?php  
      
    $curl = curl_init();  
      
    curl_setopt_array($curl, [  
      CURLOPT_URL => "https://api.coinbase.com/api/v3/brokerage/orders/edit",  
      CURLOPT_RETURNTRANSFER => true,  
      CURLOPT_ENCODING => "",  
      CURLOPT_MAXREDIRS => 10,  
      CURLOPT_TIMEOUT => 30,  
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,  
      CURLOPT_CUSTOMREQUEST => "POST",  
      CURLOPT_POSTFIELDS => json_encode([  
        'order_id' => '<string>',  
        'price' => '19000.00',  
        'size' => '0.001',  
        'attached_order_configuration' => [  
            'market_market_ioc' => [  
                    'quote_size' => '10.00',  
                    'base_size' => '0.001',  
                    'rfq_disabled' => true  
            ],  
            'market_market_fok' => [  
                    'quote_size' => '10.00',  
                    'base_size' => '0.001',  
                    'rfq_disabled' => true  
            ],  
            'sor_limit_ioc' => [  
                    'quote_size' => '10.00',  
                    'base_size' => '0.001',  
                    'limit_price' => '10000.00',  
                    'rfq_disabled' => true  
            ],  
            'limit_limit_gtc' => [  
                    'quote_size' => '10.00',  
                    'base_size' => '0.001',  
                    'limit_price' => '10000.00',  
                    'post_only' => false,  
                    'rfq_disabled' => true  
            ],  
            'limit_limit_gtd' => [  
                    'quote_size' => '10.00',  
                    'base_size' => '0.001',  
                    'limit_price' => '10000.00',  
                    'end_time' => '2021-05-31T09:59:59.000Z',  
                    'post_only' => false  
            ],  
            'limit_limit_fok' => [  
                    'quote_size' => '10.00',  
                    'base_size' => '0.001',  
                    'limit_price' => '10000.00',  
                    'rfq_disabled' => true  
            ],  
            'twap_limit_gtd' => [  
                    'quote_size' => '10.00',  
                    'base_size' => '0.001',  
                    'start_time' => '2021-05-31T07:59:59.000Z',  
                    'end_time' => '2021-05-31T09:59:59.000Z',  
                    'limit_price' => '10000.00',  
                    'number_buckets' => '5',  
                    'bucket_size' => '2.00',  
                    'bucket_duration' => '300s'  
            ],  
            'stop_limit_stop_limit_gtc' => [  
                    'base_size' => '0.001',  
                    'limit_price' => '10000.00',  
                    'stop_price' => '20000.00',  
                    'stop_direction' => '20000.00'  
            ],  
            'stop_limit_stop_limit_gtd' => [  
                    'base_size' => 0.001,  
                    'limit_price' => '10000.00',  
                    'stop_price' => '20000.00',  
                    'end_time' => '2021-05-31T09:59:59.000Z',  
                    'stop_direction' => '20000.00'  
            ],  
            'trigger_bracket_gtc' => [  
                    'base_size' => 0.001,  
                    'limit_price' => '10000.00',  
                    'stop_trigger_price' => '20000.00'  
            ],  
            'trigger_bracket_gtd' => [  
                    'base_size' => 0.001,  
                    'limit_price' => '10000.00',  
                    'stop_trigger_price' => '20000.00',  
                    'end_time' => '2021-05-31T09:59:59.000Z'  
            ],  
            'scaled_limit_gtc' => [  
                    'orders' => [  
                                    [  
                                                                    'quote_size' => '10.00',  
                                                                    'base_size' => '0.001',  
                                                                    'limit_price' => '10000.00',  
                                                                    'post_only' => false,  
                                                                    'rfq_disabled' => true  
                                    ]  
                    ],  
                    'quote_size' => '<string>',  
                    'base_size' => '<string>',  
                    'num_orders' => 123,  
                    'min_price' => '<string>',  
                    'max_price' => '<string>',  
                    'price_distribution' => 'FLAT',  
                    'size_distribution' => 'UNKNOWN_DISTRIBUTION',  
                    'size_diff' => '<string>',  
                    'size_ratio' => '<string>'  
            ]  
        ],  
        'cancel_attached_order' => 'true',  
        'stop_price' => '17000.00',  
        'average_entry_price' => '18000.00'  
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
      
    	url := "https://api.coinbase.com/api/v3/brokerage/orders/edit"  
      
    	payload := strings.NewReader("{\n  \"order_id\": \"<string>\",\n  \"price\": \"19000.00\",\n  \"size\": \"0.001\",\n  \"attached_order_configuration\": {\n    \"market_market_ioc\": {\n      \"quote_size\": \"10.00\",\n      \"base_size\": \"0.001\",\n      \"rfq_disabled\": true\n    },\n    \"market_market_fok\": {\n      \"quote_size\": \"10.00\",\n      \"base_size\": \"0.001\",\n      \"rfq_disabled\": true\n    },\n    \"sor_limit_ioc\": {\n      \"quote_size\": \"10.00\",\n      \"base_size\": \"0.001\",\n      \"limit_price\": \"10000.00\",\n      \"rfq_disabled\": true\n    },\n    \"limit_limit_gtc\": {\n      \"quote_size\": \"10.00\",\n      \"base_size\": \"0.001\",\n      \"limit_price\": \"10000.00\",\n      \"post_only\": false,\n      \"rfq_disabled\": true\n    },\n    \"limit_limit_gtd\": {\n      \"quote_size\": \"10.00\",\n      \"base_size\": \"0.001\",\n      \"limit_price\": \"10000.00\",\n      \"end_time\": \"2021-05-31T09:59:59.000Z\",\n      \"post_only\": false\n    },\n    \"limit_limit_fok\": {\n      \"quote_size\": \"10.00\",\n      \"base_size\": \"0.001\",\n      \"limit_price\": \"10000.00\",\n      \"rfq_disabled\": true\n    },\n    \"twap_limit_gtd\": {\n      \"quote_size\": \"10.00\",\n      \"base_size\": \"0.001\",\n      \"start_time\": \"2021-05-31T07:59:59.000Z\",\n      \"end_time\": \"2021-05-31T09:59:59.000Z\",\n      \"limit_price\": \"10000.00\",\n      \"number_buckets\": \"5\",\n      \"bucket_size\": \"2.00\",\n      \"bucket_duration\": \"300s\"\n    },\n    \"stop_limit_stop_limit_gtc\": {\n      \"base_size\": \"0.001\",\n      \"limit_price\": \"10000.00\",\n      \"stop_price\": \"20000.00\",\n      \"stop_direction\": \"20000.00\"\n    },\n    \"stop_limit_stop_limit_gtd\": {\n      \"base_size\": 0.001,\n      \"limit_price\": \"10000.00\",\n      \"stop_price\": \"20000.00\",\n      \"end_time\": \"2021-05-31T09:59:59.000Z\",\n      \"stop_direction\": \"20000.00\"\n    },\n    \"trigger_bracket_gtc\": {\n      \"base_size\": 0.001,\n      \"limit_price\": \"10000.00\",\n      \"stop_trigger_price\": \"20000.00\"\n    },\n    \"trigger_bracket_gtd\": {\n      \"base_size\": 0.001,\n      \"limit_price\": \"10000.00\",\n      \"stop_trigger_price\": \"20000.00\",\n      \"end_time\": \"2021-05-31T09:59:59.000Z\"\n    },\n    \"scaled_limit_gtc\": {\n      \"orders\": [\n        {\n          \"quote_size\": \"10.00\",\n          \"base_size\": \"0.001\",\n          \"limit_price\": \"10000.00\",\n          \"post_only\": false,\n          \"rfq_disabled\": true\n        }\n      ],\n      \"quote_size\": \"<string>\",\n      \"base_size\": \"<string>\",\n      \"num_orders\": 123,\n      \"min_price\": \"<string>\",\n      \"max_price\": \"<string>\",\n      \"price_distribution\": \"FLAT\",\n      \"size_distribution\": \"UNKNOWN_DISTRIBUTION\",\n      \"size_diff\": \"<string>\",\n      \"size_ratio\": \"<string>\"\n    }\n  },\n  \"cancel_attached_order\": \"true\",\n  \"stop_price\": \"17000.00\",\n  \"average_entry_price\": \"18000.00\"\n}")  
      
    	req, _ := http.NewRequest("POST", url, payload)  
      
    	req.Header.Add("Authorization", "Bearer <token>")  
    	req.Header.Add("Content-Type", "application/json")  
      
    	res, _ := http.DefaultClient.Do(req)  
      
    	defer res.Body.Close()  
    	body, _ := io.ReadAll(res.Body)  
      
    	fmt.Println(string(body))  
      
    }
    
    
    HttpResponse<String> response = Unirest.post("https://api.coinbase.com/api/v3/brokerage/orders/edit")  
      .header("Authorization", "Bearer <token>")  
      .header("Content-Type", "application/json")  
      .body("{\n  \"order_id\": \"<string>\",\n  \"price\": \"19000.00\",\n  \"size\": \"0.001\",\n  \"attached_order_configuration\": {\n    \"market_market_ioc\": {\n      \"quote_size\": \"10.00\",\n      \"base_size\": \"0.001\",\n      \"rfq_disabled\": true\n    },\n    \"market_market_fok\": {\n      \"quote_size\": \"10.00\",\n      \"base_size\": \"0.001\",\n      \"rfq_disabled\": true\n    },\n    \"sor_limit_ioc\": {\n      \"quote_size\": \"10.00\",\n      \"base_size\": \"0.001\",\n      \"limit_price\": \"10000.00\",\n      \"rfq_disabled\": true\n    },\n    \"limit_limit_gtc\": {\n      \"quote_size\": \"10.00\",\n      \"base_size\": \"0.001\",\n      \"limit_price\": \"10000.00\",\n      \"post_only\": false,\n      \"rfq_disabled\": true\n    },\n    \"limit_limit_gtd\": {\n      \"quote_size\": \"10.00\",\n      \"base_size\": \"0.001\",\n      \"limit_price\": \"10000.00\",\n      \"end_time\": \"2021-05-31T09:59:59.000Z\",\n      \"post_only\": false\n    },\n    \"limit_limit_fok\": {\n      \"quote_size\": \"10.00\",\n      \"base_size\": \"0.001\",\n      \"limit_price\": \"10000.00\",\n      \"rfq_disabled\": true\n    },\n    \"twap_limit_gtd\": {\n      \"quote_size\": \"10.00\",\n      \"base_size\": \"0.001\",\n      \"start_time\": \"2021-05-31T07:59:59.000Z\",\n      \"end_time\": \"2021-05-31T09:59:59.000Z\",\n      \"limit_price\": \"10000.00\",\n      \"number_buckets\": \"5\",\n      \"bucket_size\": \"2.00\",\n      \"bucket_duration\": \"300s\"\n    },\n    \"stop_limit_stop_limit_gtc\": {\n      \"base_size\": \"0.001\",\n      \"limit_price\": \"10000.00\",\n      \"stop_price\": \"20000.00\",\n      \"stop_direction\": \"20000.00\"\n    },\n    \"stop_limit_stop_limit_gtd\": {\n      \"base_size\": 0.001,\n      \"limit_price\": \"10000.00\",\n      \"stop_price\": \"20000.00\",\n      \"end_time\": \"2021-05-31T09:59:59.000Z\",\n      \"stop_direction\": \"20000.00\"\n    },\n    \"trigger_bracket_gtc\": {\n      \"base_size\": 0.001,\n      \"limit_price\": \"10000.00\",\n      \"stop_trigger_price\": \"20000.00\"\n    },\n    \"trigger_bracket_gtd\": {\n      \"base_size\": 0.001,\n      \"limit_price\": \"10000.00\",\n      \"stop_trigger_price\": \"20000.00\",\n      \"end_time\": \"2021-05-31T09:59:59.000Z\"\n    },\n    \"scaled_limit_gtc\": {\n      \"orders\": [\n        {\n          \"quote_size\": \"10.00\",\n          \"base_size\": \"0.001\",\n          \"limit_price\": \"10000.00\",\n          \"post_only\": false,\n          \"rfq_disabled\": true\n        }\n      ],\n      \"quote_size\": \"<string>\",\n      \"base_size\": \"<string>\",\n      \"num_orders\": 123,\n      \"min_price\": \"<string>\",\n      \"max_price\": \"<string>\",\n      \"price_distribution\": \"FLAT\",\n      \"size_distribution\": \"UNKNOWN_DISTRIBUTION\",\n      \"size_diff\": \"<string>\",\n      \"size_ratio\": \"<string>\"\n    }\n  },\n  \"cancel_attached_order\": \"true\",\n  \"stop_price\": \"17000.00\",\n  \"average_entry_price\": \"18000.00\"\n}")  
      .asString();
    
    
    require 'uri'  
    require 'net/http'  
      
    url = URI("https://api.coinbase.com/api/v3/brokerage/orders/edit")  
      
    http = Net::HTTP.new(url.host, url.port)  
    http.use_ssl = true  
      
    request = Net::HTTP::Post.new(url)  
    request["Authorization"] = 'Bearer <token>'  
    request["Content-Type"] = 'application/json'  
    request.body = "{\n  \"order_id\": \"<string>\",\n  \"price\": \"19000.00\",\n  \"size\": \"0.001\",\n  \"attached_order_configuration\": {\n    \"market_market_ioc\": {\n      \"quote_size\": \"10.00\",\n      \"base_size\": \"0.001\",\n      \"rfq_disabled\": true\n    },\n    \"market_market_fok\": {\n      \"quote_size\": \"10.00\",\n      \"base_size\": \"0.001\",\n      \"rfq_disabled\": true\n    },\n    \"sor_limit_ioc\": {\n      \"quote_size\": \"10.00\",\n      \"base_size\": \"0.001\",\n      \"limit_price\": \"10000.00\",\n      \"rfq_disabled\": true\n    },\n    \"limit_limit_gtc\": {\n      \"quote_size\": \"10.00\",\n      \"base_size\": \"0.001\",\n      \"limit_price\": \"10000.00\",\n      \"post_only\": false,\n      \"rfq_disabled\": true\n    },\n    \"limit_limit_gtd\": {\n      \"quote_size\": \"10.00\",\n      \"base_size\": \"0.001\",\n      \"limit_price\": \"10000.00\",\n      \"end_time\": \"2021-05-31T09:59:59.000Z\",\n      \"post_only\": false\n    },\n    \"limit_limit_fok\": {\n      \"quote_size\": \"10.00\",\n      \"base_size\": \"0.001\",\n      \"limit_price\": \"10000.00\",\n      \"rfq_disabled\": true\n    },\n    \"twap_limit_gtd\": {\n      \"quote_size\": \"10.00\",\n      \"base_size\": \"0.001\",\n      \"start_time\": \"2021-05-31T07:59:59.000Z\",\n      \"end_time\": \"2021-05-31T09:59:59.000Z\",\n      \"limit_price\": \"10000.00\",\n      \"number_buckets\": \"5\",\n      \"bucket_size\": \"2.00\",\n      \"bucket_duration\": \"300s\"\n    },\n    \"stop_limit_stop_limit_gtc\": {\n      \"base_size\": \"0.001\",\n      \"limit_price\": \"10000.00\",\n      \"stop_price\": \"20000.00\",\n      \"stop_direction\": \"20000.00\"\n    },\n    \"stop_limit_stop_limit_gtd\": {\n      \"base_size\": 0.001,\n      \"limit_price\": \"10000.00\",\n      \"stop_price\": \"20000.00\",\n      \"end_time\": \"2021-05-31T09:59:59.000Z\",\n      \"stop_direction\": \"20000.00\"\n    },\n    \"trigger_bracket_gtc\": {\n      \"base_size\": 0.001,\n      \"limit_price\": \"10000.00\",\n      \"stop_trigger_price\": \"20000.00\"\n    },\n    \"trigger_bracket_gtd\": {\n      \"base_size\": 0.001,\n      \"limit_price\": \"10000.00\",\n      \"stop_trigger_price\": \"20000.00\",\n      \"end_time\": \"2021-05-31T09:59:59.000Z\"\n    },\n    \"scaled_limit_gtc\": {\n      \"orders\": [\n        {\n          \"quote_size\": \"10.00\",\n          \"base_size\": \"0.001\",\n          \"limit_price\": \"10000.00\",\n          \"post_only\": false,\n          \"rfq_disabled\": true\n        }\n      ],\n      \"quote_size\": \"<string>\",\n      \"base_size\": \"<string>\",\n      \"num_orders\": 123,\n      \"min_price\": \"<string>\",\n      \"max_price\": \"<string>\",\n      \"price_distribution\": \"FLAT\",\n      \"size_distribution\": \"UNKNOWN_DISTRIBUTION\",\n      \"size_diff\": \"<string>\",\n      \"size_ratio\": \"<string>\"\n    }\n  },\n  \"cancel_attached_order\": \"true\",\n  \"stop_price\": \"17000.00\",\n  \"average_entry_price\": \"18000.00\"\n}"  
      
    response = http.request(request)  
    puts response.read_body
    
    
    {
      "success": true,
      "errors": [
        {
          "edit_failure_reason": "UNKNOWN_EDIT_ORDER_FAILURE_REASON",
          "preview_failure_reason": "UNKNOWN_PREVIEW_FAILURE_REASON"
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

order_id

string

required

The ID of the order.

price

string

required

The update price of the order.

Example:

`"19000.00"`

size

string

required

The updated size of the order.

Example:

`"0.001"`

attached_order_configuration

object

The configuration of the attached order. Only TriggerBracketGtc, LimitLimitGtc or StopLimitStopLimitGtc are eligible.

cancel_attached_order

boolean

Drops both the legs of TP/SL, order becomes a simple limit order.

Example:

`"true"`

stop_price

string

The updated stop price of the order. Only applicable for editing TP/SL or SL orders.

Example:

`"17000.00"`

average_entry_price

string

The average entry price of the position. Used for estimated PnL

Example:

`"18000.00"`

#### Response

A successful response.

success

boolean

required

Whether the order edit request was placed.

Example:

`true`

errors

object[]