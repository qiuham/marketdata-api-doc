---
exchange: coinbase
source_url: https://docs.cdp.coinbase.com/api-reference/advanced-trade-api/rest-api/portfolios/get-portfolio-breakdown
api_type: Account
updated_at: 2026-07-14 19:08:04.051003
---

# Get Portfolio Breakdown

**Endpoint:** `GET https://api.coinbase.com/api/v3/brokerage/portfolios/{portfolio_uuid}`


Get the breakdown of a portfolio.
    
    
    curl --request GET \
      --url https://api.coinbase.com/api/v3/brokerage/portfolios/{portfolio_uuid} \
      --header 'Authorization: Bearer <token>'
    
    
    import requests  
      
    url = "https://api.coinbase.com/api/v3/brokerage/portfolios/{portfolio_uuid}"  
      
    headers = {"Authorization": "Bearer <token>"}  
      
    response = requests.get(url, headers=headers)  
      
    print(response.text)
    
    
    const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};  
      
    fetch('https://api.coinbase.com/api/v3/brokerage/portfolios/{portfolio_uuid}', options)  
      .then(res => res.json())  
      .then(res => console.log(res))  
      .catch(err => console.error(err));
    
    
    <?php  
      
    $curl = curl_init();  
      
    curl_setopt_array($curl, [  
      CURLOPT_URL => "https://api.coinbase.com/api/v3/brokerage/portfolios/{portfolio_uuid}",  
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
      
    	url := "https://api.coinbase.com/api/v3/brokerage/portfolios/{portfolio_uuid}"  
      
    	req, _ := http.NewRequest("GET", url, nil)  
      
    	req.Header.Add("Authorization", "Bearer <token>")  
      
    	res, _ := http.DefaultClient.Do(req)  
      
    	defer res.Body.Close()  
    	body, _ := io.ReadAll(res.Body)  
      
    	fmt.Println(string(body))  
      
    }
    
    
    HttpResponse<String> response = Unirest.get("https://api.coinbase.com/api/v3/brokerage/portfolios/{portfolio_uuid}")  
      .header("Authorization", "Bearer <token>")  
      .asString();
    
    
    require 'uri'  
    require 'net/http'  
      
    url = URI("https://api.coinbase.com/api/v3/brokerage/portfolios/{portfolio_uuid}")  
      
    http = Net::HTTP.new(url.host, url.port)  
    http.use_ssl = true  
      
    request = Net::HTTP::Get.new(url)  
    request["Authorization"] = 'Bearer <token>'  
      
    response = http.request(request)  
    puts response.read_body
    
    
    {
      "breakdown": {
        "portfolio": {
          "name": "<string>",
          "uuid": "<string>",
          "type": "UNDEFINED",
          "deleted": true
        },
        "portfolio_balances": {
          "total_balance": {
            "value": "<string>",
            "currency": "<string>"
          },
          "total_futures_balance": {
            "value": "<string>",
            "currency": "<string>"
          },
          "total_cash_equivalent_balance": {
            "value": "<string>",
            "currency": "<string>"
          },
          "total_crypto_balance": {
            "value": "<string>",
            "currency": "<string>"
          },
          "futures_unrealized_pnl": {
            "value": "<string>",
            "currency": "<string>"
          },
          "perp_unrealized_pnl": {
            "value": "<string>",
            "currency": "<string>"
          },
          "total_equities_balance": {
            "value": "<string>",
            "currency": "<string>"
          }
        },
        "spot_positions": [
          {
            "asset": "<string>",
            "account_uuid": "<string>",
            "total_balance_fiat": 123,
            "total_balance_crypto": 123,
            "available_to_trade_fiat": 123,
            "allocation": 123,
            "cost_basis": {
              "value": "<string>",
              "currency": "<string>"
            },
            "asset_img_url": "<string>",
            "is_cash": true,
            "average_entry_price": {
              "value": "<string>",
              "currency": "<string>"
            },
            "asset_uuid": "<string>",
            "available_to_trade_crypto": 123,
            "unrealized_pnl": 123,
            "available_to_transfer_fiat": 123,
            "available_to_transfer_crypto": 123,
            "asset_color": "<string>",
            "account_type": "ACCOUNT_TYPE_UNKNOWN_UNSPECIFIED",
            "funding_pnl": 123,
            "available_to_send_fiat": 123,
            "available_to_send_crypto": 123
          }
        ],
        "perp_positions": [
          {
            "product_id": "<string>",
            "product_uuid": "<string>",
            "symbol": "<string>",
            "asset_image_url": "<string>",
            "vwap": {
              "userNativeCurrency": {
                "value": "<string>",
                "currency": "<string>"
              },
              "rawCurrency": {
                "value": "<string>",
                "currency": "<string>"
              }
            },
            "position_side": "FUTURES_POSITION_SIDE_UNSPECIFIED",
            "net_size": "<string>",
            "buy_order_size": "<string>",
            "sell_order_size": "<string>",
            "im_contribution": "<string>",
            "unrealized_pnl": {
              "userNativeCurrency": {
                "value": "<string>",
                "currency": "<string>"
              },
              "rawCurrency": {
                "value": "<string>",
                "currency": "<string>"
              }
            },
            "mark_price": {
              "userNativeCurrency": {
                "value": "<string>",
                "currency": "<string>"
              },
              "rawCurrency": {
                "value": "<string>",
                "currency": "<string>"
              }
            },
            "liquidation_price": {
              "userNativeCurrency": {
                "value": "<string>",
                "currency": "<string>"
              },
              "rawCurrency": {
                "value": "<string>",
                "currency": "<string>"
              }
            },
            "leverage": "<string>",
            "im_notional": {
              "userNativeCurrency": {
                "value": "<string>",
                "currency": "<string>"
              },
              "rawCurrency": {
                "value": "<string>",
                "currency": "<string>"
              }
            },
            "mm_notional": {
              "userNativeCurrency": {
                "value": "<string>",
                "currency": "<string>"
              },
              "rawCurrency": {
                "value": "<string>",
                "currency": "<string>"
              }
            },
            "position_notional": {
              "userNativeCurrency": {
                "value": "<string>",
                "currency": "<string>"
              },
              "rawCurrency": {
                "value": "<string>",
                "currency": "<string>"
              }
            },
            "margin_type": "MARGIN_TYPE_UNSPECIFIED",
            "liquidation_buffer": "<string>",
            "liquidation_percentage": "<string>",
            "asset_color": "<string>"
          }
        ],
        "futures_positions": [
          {
            "product_id": "<string>",
            "contract_size": "<string>",
            "side": "FUTURES_POSITION_SIDE_UNSPECIFIED",
            "amount": "<string>",
            "avg_entry_price": "<string>",
            "current_price": "<string>",
            "unrealized_pnl": "<string>",
            "expiry": "<string>",
            "underlying_asset": "<string>",
            "asset_img_url": "<string>",
            "product_name": "<string>",
            "venue": "<string>",
            "notional_value": "<string>",
            "asset_color": "<string>",
            "last_traded_at": "<string>",
            "roll_date": "<string>",
            "price_increment": "<string>",
            "price_precision": 123
          }
        ],
        "prediction_markets_positions": [
          {
            "product_type": "PRODUCT_TYPE_UNSPECIFIED",
            "cbrn": "<string>",
            "prediction_markets": {
              "side": "PREDICTION_MARKETS_POSITION_SIDE_UNSPECIFIED",
              "last_traded_at": "<string>",
              "average_entry_price": {
                "value": "<string>",
                "currency": "<string>"
              },
              "current_price": {
                "value": "<string>",
                "currency": "<string>"
              },
              "unrealized_pnl": {
                "value": "<string>",
                "currency": "<string>"
              },
              "notional_value": {
                "value": "<string>",
                "currency": "<string>"
              },
              "cost_basis": {
                "value": "<string>",
                "currency": "<string>"
              },
              "contracts_owned": "<string>",
              "quote_cbrn": "<string>"
            }
          }
        ],
        "equity_positions": [
          {
            "cbrn": "<string>",
            "account_uuid": "<string>",
            "total_balance_fiat": {
              "value": "<string>",
              "currency": "<string>"
            },
            "total_balance_equity": {
              "value": "<string>",
              "currency": "<string>"
            },
            "available_to_trade_equity": {
              "value": "<string>",
              "currency": "<string>"
            },
            "available_to_trade_fiat": {
              "value": "<string>",
              "currency": "<string>"
            },
            "account_type": "ACCOUNT_TYPE_UNKNOWN_UNSPECIFIED",
            "allocation": 123,
            "cost_basis": {
              "value": "<string>",
              "currency": "<string>"
            },
            "average_entry_price": {
              "value": "<string>",
              "currency": "<string>"
            },
            "unrealized_pnl": {
              "value": "<string>",
              "currency": "<string>"
            }
          }
        ]
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

#### Path Parameters

portfolio_uuid

string

required

The portfolio UUID.

#### Query Parameters

currency

string

The currency symbol (e.g. USD).

#### Response

A successful response.

breakdown

object

PortfolioBreakdown is a breakdown of a portfolio, all balances, and all positions within the portfolio.