---
exchange: coinbase
source_url: https://docs.cdp.coinbase.com/api-reference/advanced-trade-api/rest-api/accounts/get-account
api_type: Account
updated_at: 2026-10-13 19:08:45.160791
---

# Get Account

**Endpoint:** `GET https://api.coinbase.com/api/v3/brokerage/accounts/{account_uuid}`


Get a list of information about an account, given an account UUID.
    
    
    curl --request GET \
      --url https://api.coinbase.com/api/v3/brokerage/accounts/{account_uuid} \
      --header 'Authorization: Bearer <token>'
    
    
    import requests
    
    url = "https://api.coinbase.com/api/v3/brokerage/accounts/{account_uuid}"
    
    headers = {"Authorization": "Bearer <token>"}
    
    response = requests.get(url, headers=headers)
    
    print(response.text)
    
    
    const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};
    
    fetch('https://api.coinbase.com/api/v3/brokerage/accounts/{account_uuid}', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.coinbase.com/api/v3/brokerage/accounts/{account_uuid}",
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
    
    	url := "https://api.coinbase.com/api/v3/brokerage/accounts/{account_uuid}"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://api.coinbase.com/api/v3/brokerage/accounts/{account_uuid}")
      .header("Authorization", "Bearer <token>")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.coinbase.com/api/v3/brokerage/accounts/{account_uuid}")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Get.new(url)
    request["Authorization"] = 'Bearer <token>'
    
    response = http.request(request)
    puts response.read_body
    
    
    {
      "account": {
        "uuid": "8bfc20d7-f7c6-4422-bf07-8243ca4169fe",
        "name": "BTC Wallet",
        "currency": "BTC",
        "available_balance": {
          "value": "1.23",
          "currency": "BTC"
        },
        "default": false,
        "active": true,
        "created_at": "2021-05-31T09:59:59Z",
        "updated_at": "2021-05-31T09:59:59Z",
        "deleted_at": "2021-05-31T09:59:59Z",
        "type": "FIAT",
        "ready": true,
        "hold": {
          "value": "1.23",
          "currency": "BTC"
        },
        "retail_portfolio_id": "b87a2d3f-8a1e-49b3-a4ea-402d8c389aca",
        "platform": "ACCOUNT_PLATFORM_CONSUMER"
      }
    }
    
    
    {
      "error": "<string>",
      "code": 123,
      "message": "<string>",
      "details": [
        {}
      ]
    }

#### Authorizations

ApiKeyOAuth2ApiKeyOAuth2

Authorization

string

header

required

A bearer token signed using your API Key Secret, see [Creating API Keys](/coinbase-app/authentication-authorization/api-key-authentication) section of our docs for more information. See [Scope & Permissions](/coinbase-app/advanced-trade-apis/rest-scopes) for the permission each endpoint requires.

#### Path Parameters

account_uuid

string

required

The account's UUID.

#### Response

A successful response.

account

object

: "<string>" } }, "hot_wallet": { "network": "<string>", "address": "<string>" }, "nova_account": { "network": "<string>", "nova_account_id": "<string>", "pool_name": "<string>", "account_idempotency_key": "<string>" }, "magic_spend_blockchain_address": { "address": "<string>", "destination_tag": "<string>" }, "transfer_pointer": { "idem": "<string>" }, "eft": { "account": { "account_name": "<string>", "account_phone_number": "<string>", "account_email": "<string>", "institution_number": "<string>", "transit_number": "<string>", "account_number": "<string>", "provider_id": "<string>", "provider_name": "<string>", "trustly_account_token_status": "TRUSTLY_TOKEN_STATUS_UNSPECIFIED", "account_type": "<string>" } }, "wallace_account": { "wallace_account_id": "<string>", "pool_name": "<string>" }, "manual": { "settlement_bank_name": "<string>", "settlement_account_number": "<string>", "reference": "<string>" }, "argentine_bank_account": { "tax_id": "<string>", "cbu": "<string>" }, "representment": { "currency": "<string>" }, "banking_circle_now": { "iban": "<string>", "currency": "<string>", "customer_payment_name": "<string>" }, "trustly": { "country": "<string>", "iban": "<string>", "account_holder": "<string>", "bank_code": "<string>", "account_number": "<string>", "partial_account_number": "<string>", "bank_name": "<string>", "email": "<string>" }, "blik": { "email": "<string>", "country": "<string>", "account_holder": "<string>" }, "mb_way": { "account_holder": "<string>", "country": "<string>", "phone_number": "<string>" }, "pix": { "account_number": "<string>", "account_type": "<string>", "bank_code": "<string>", "bank_name": "<string>", "branch_number": "<string>", "customer_payment_name": "<string>", "sender_document": "<string>", "pix_key": "<string>", "pix_account_type": "ACCOUNT_TYPE_UNSPECIFIED", "branch_code": "<string>" }, "magic_wallet": { "user_uuid": "<string>", "network_name": "<string>", "wallet_name": "<string>" }, "samsung_pay": { "samsung_pay": { "nonce": "<string>", "correlation_id": "<string>", "version": "<string>" }, "user_id": "<string>", "postal_code": "<string>", "customer_name": "<string>", "address": { "address1": "<string>", "address2": "<string>", "city": "<string>", "state": "<string>", "postal_code": "<string>", "country": "<string>", "uuid": "<string>", "id": "<string>" }, "six_digit_bin": "<string>", "last_four": "<string>", "issuing_country": "<string>", "issuing_bank": "<string>", "product_id": "<string>", "customer_dob": "<string>", "currency": "<string>", "billing_address_id": "<string>", "scheme": "UNKNOWN", "prepaid": "UNCERTAIN", "debit": "UNCERTAIN" }, "cad_wire": { "account_number": "<string>", "customer_payment_name": "<string>", "account_address": "<string>", "institution_number": "<string>", "transit_number": "<string>", "bank_address1": "<string>", "institution_name": "<string>" }, "wab_intra_bank": { "account_id": "<string>", "customer_name": "<string>" }, "india_bank_account": { "account_number": "<string>", "ifsc_code": "<string>", "bank_name": "<string>", "customer_first_name": "<string>", "customer_last_name": "<string>", "email": "<string>", "phone_number": "<string>", "pan_number": "<string>", "customer_payment_name": "<string>" }, "jpmorgan_kinexys": { "account_number": "<string>", "bic": "<string>" }, "sic": { "legal_name": "<string>", "iban": "<string>", "swift": "<string>", "customer_payment_address1": "<string>", "customer_payment_address2": "<string>", "customer_payment_address3": "<string>", "bank_name": "<string>", "bank_address1": "<string>", "bank_address2": "<string>", "bank_address3": "<string>", "bank_country_code": "<string>" }, "spei": { "account_number": "<string>", "customer_name": "<string>" } }, "target": { "type": "INVALID", "network": "<string>", "payment_method_id": "<string>", "payment_method_uuid": "<string>", "payment_method_type_string": "<string>", "blockchain_address": { "address": "<string>", "destination_tag": "<string>" }, "coinbase_account": { "account_id": "<string>" }, "blockchain_transaction": { "hsh": "<string>", "height": 123, "normalized_hash": "<string>" }, "fedwire": { "routing_number": "<string>", "account_holder": { "legal_name": "<string>", "account_number": "<string>", "address": { "lines": [ "<string>" ], "country_code": "<string>", "city": "<string>", "state": "<string>", "postal_code": "<string>" } }, "bank": { "name": "<string>", "address": { "lines": [ "<string>" ], "country_code": "<string>", "city": "<string>", "state": "<string>", "postal_code": "<string>" }, "identifier": "<string>", "type": "CHIPS_IDENTIFIER", "identifier_code": "<string>" }, "intermediary_bank": { "name": "<string>", "address": { "lines": [ "<string>" ], "country_code": "<string>", "city": "<string>", "state": "<string>", "postal_code": "<string>" }, "identifier": "<string>", "type": "CHIPS_IDENTIFIER", "identifier_code": "<string>" }, "currency": "<string>", "fiat_id": "<string>", "rejection_count_v2": 123 }, "swift": { "account_holder": { "legal_name": "<string>", "iban": "<string>", "bban": "<string>", "domestic_account_id": "<string>", "customer_payment_address1": "<string>", "customer_payment_address2": "<string>", "customer_payment_address3": "<string>", "customer_payment_country_code": "<string>", "iban_generated": true }, "institution": { "bic": "<string>", "name": "<string>", "bank_address1": "<string>", "bank_address2": "<string>", "bank_address3": "<string>", "bank_country_code": "<string>", "domestic_bank_id": "<string>", "international_bank_id": "<string>" }, "intermediary": { "bic": "<string>", "name": "<string>", "bank_address1": "<string>", "bank_address2": "<string>", "bank_address3": "<string>", "bank_country_code": "<string>", "domestic_bank_id": "<string>", "international_bank_id": "<string>" }, "currency": "<string>", "rejection_count": 123 }, "card": { "first_data_token": { "value": "<string>", "store_id": "<string>", "id": "<string>" }, "merchant": { "mid": "<string>" }, "vault_token": { "value": "<string>", "vault_id": "<string>", "attempted_at": "<string>", "encrypted_data": "<string>", "encrypted_cvv": "<string>" }, "worldpay_params": { "token_value": "<string>", "token_event": "<string>", "uses_merchant_token": true, "accept_header": "<string>", "user_agent_header": "<string>", "shopper_ip": "<string>", "shopper_session_id": "<string>" }, "checkout_token": { "source_id": "<string>" }, "stripe_params": { "stripe_id": "<string>", "radar_session_id": "<string>", "address_line1_check": "STRIPE_CARD_CHECK_STATUS_UNKNOWN", "address_postal_code_check": "STRIPE_CARD_CHECK_STATUS_UNKNOWN", "cvc_check": "STRIPE_CARD_CHECK_STATUS_UNKNOWN" }, "six_digit_bin": "<string>", "last_four": "<string>", "eight_digit_bin": "<string>", "card_sub_brand": "<string>", "card_brand": "<string>", "obfuscated_pan": "<string>", "bin_info": { "match_found": true, "type": "UNKNOWN", "issuer": "<string>", "issuer_country_code": "<string>", "prepaid": true, "corporate": true, "consumer": true, "visa": { "oct_supported": true, "fast_funds_supported": true }, "mastercard": { "fast_funds_supported": true }, "use_3ds": true }, "scheme": "UNKNOWN", "issuer": "<string>", "issuer_country_code": "<string>", "address": { "address1": "<string>", "address2": "<string>", "city": "<string>", "state": "<string>", "postal_code": "<string>", "country": "<string>", "uuid": "<string>", "id": "<string>" }, "phone_number": "<string>", "user_id": "<string>", "postal_code": "<string>", "customer_info": { "full_name": "<string>", "first_name": "<string>", "last_name": "<string>", "dob": { "month": "<string>", "day": "<string>", "year": "<string>" }, "nationality": "<string>", "email": "<string>" }, "expiry_date": { "month": "<string>", "year": "<string>" }, "cdv_method": "<string>", "cdv_amount_1": { "amount": "<string>", "currency": "<string>" }, "cdv_amount_2": { "amount": "<string>", "currency": "<string>" }, "worldpay_card_cdv_status": { "cdv_required": true, "cdv_failed": true }, "previous_scheme_tx_id": "<string>", "initial_scheme_tx_id": "<string>", "rejected": true, "rejected_at": "<string>", "rejection_count": 123, "rejected_via_purchase": true, "account_updater_updated_at