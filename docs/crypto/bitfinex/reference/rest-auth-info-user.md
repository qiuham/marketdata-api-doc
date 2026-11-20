---
api_type: reference
source_type: llms_txt
version: ''
scope: crypto
asset_class: digital_asset
domain: exchanges
provider: bitfinex
provider_name: Bitfinex
product: api
product_id: bitfinex
source_url: 'https://docs.bitfinex.com/reference/rest-auth-info-user'
updated_at: 2026-11-20
---

# User Info

Retrieve an array of important account data.

#### Response data

<HTMLBlock>{`
<table>
<thead>
<tr>
  <th>Index</th>
  <th>Field</th>
  <th>Type</th>
  <th>Description</th>
</tr>
</thead>
<tbody>
<tr><td>[0]</td><td>ID</td><td>int</td><td>Account ID</td></tr>
<tr><td>[1]</td><td>EMAIL</td><td>string</td><td>Account Email</td></tr>
<tr><td>[2]</td><td>USERNAME</td><td>string</td><td>Account username</td></tr>
<tr><td>[3]</td><td>MTS_ACCOUNT_CREATE</td><td>int</td><td>Millisecond timestamp of account creation</td></tr>
<tr><td>[4]</td><td>VERIFIED</td><td>int</td><td>Indicates if the user has a verified status (KYC) 1 = true, 0 = false</td></tr>
<tr><td>[5]</td><td>VERIFICATION_LEVEL</td><td>int</td><td>Account verification level</td></tr>
<tr><td colspan="4"><div class="placeholders">[ . . . ]</div></td></tr>
<tr><td>[7]</td><td>TIMEZONE</td><td>string</td><td>Account timezone setting</td></tr>
<tr><td>[8]</td><td>LOCALE</td><td>string</td><td>Account locale setting</td></tr>
<tr><td>[9]</td><td>COMPANY</td><td>string</td><td>Shows where the account is registered. Accounts registered at Bitfinex will show 'bitfinex' and accounts registered at eosfinex will show 'eosfinex'</td></tr>
<tr><td>[10]</td><td>EMAIL_VERIFIED</td><td>int</td><td>1 if true</td></tr>
<tr><td colspan="4"><div class="placeholders">[ . . . ]</div></td></tr>
<tr><td>[12]</td><td>SUBACCOUNT_TYPE</td><td>TBD</td><td>TBD</td></tr>
<tr><td colspan="4"><div class="placeholders">[ . . . ]</div></td></tr>
<tr><td>[14]</td><td>MTS_MASTER_ACCOUNT_CREATE</td><td>int</td><td>Millisecond timestamp of master account creation</td></tr>
<tr><td>[15]</td><td>GROUP_ID</td><td>int</td><td>Account group ID</td></tr>
<tr><td>[16]</td><td>MASTER_ACCOUNT_ID</td><td>int</td><td>The ID of the master account, If the account is a sub-account.</td></tr>
<tr><td>[17]</td><td>INHERIT_MASTER_ACCOUNT_VERIFICATION</td><td>int</td><td>1 if account inherits verification from master account</td></tr>
<tr><td>[18]</td><td>IS_GROUP_MASTER</td><td>int</td><td>1 if account is a master account</td></tr>
<tr><td>[19]</td><td>GROUP_WITHDRAW_ENABLED</td><td>int</td><td>1 if enabled</td></tr>
<tr><td colspan="4"><div class="placeholders">[ . . . ]</div></td></tr>
<tr><td>[21]</td><td>PPT_ENABLED</td><td>int</td><td>1 if true (for paper trading accounts)</td></tr>
<tr><td>[22]</td><td>MERCHANT_ENABLED</td><td>int</td><td>1 if true (for merchant accounts)</td></tr>
<tr><td>[23]</td><td>COMPETITION_ENABLED</td><td>int</td><td>1 if true (for competition accounts)</td></tr>
<tr><td colspan="4"><div class="placeholders">[ . . . ]</div></td></tr>
<tr><td>[26]</td><td>2FA_MODES</td><td>array of strings</td><td>Array of enabled 2FA modes ('u2f', 'otp')</td></tr>
<tr><td colspan="4"><div class="placeholders">[ . . . ]</div></td></tr>
<tr><td>[28]</td><td>IS_SECURITIES_MASTER</td><td>int</td><td>Deprecated field</td></tr>
<tr><td>[29]</td><td>SECURITIES_ENABLED</td><td>int</td><td>1 if true (account can trade securities)</td></tr>
<tr><td>[30]</td><td>IS_SECURITIES_INVESTOR_ACCREDITED</td><td>int</td><td>1 if true (when an account is accredited investor verified)</td></tr>
  <tr><td>[31]</td><td>IS_SECURITIES_EL_SALVADOR</td><td>int</td><td>1 if true (if an account is verified for El Salvador securities)</td></tr>
<tr><td>[32]</td><td>IS_SECURITIES_AIFC</td><td>int</td><td>1 if true (if an account is verified for AIFC securities)</td></tr>
<tr><td colspan="4"><div class="placeholders">[ . . . ]</div></td></tr>
<tr><td>[38]</td><td>ALLOW_DISABLE_CTXSWITCH</td><td>int</td><td>Account can disable context switching by master account into this account (1 if true)</td></tr>
<tr><td>[39]</td><td>CTXSWITCH_DISABLED</td><td>int</td><td>Master account cannot context switch into this account (1 if true)</td></tr>
 <tr><td colspan="4"><div class="placeholders">[ . . . ]</div></td></tr>
<tr><td>[42]</td><td>HIGH_NET_WORTH</td><td>int</td><td>1 if true</td></tr>
<tr><td colspan="4"><div class="placeholders">[ . . . ]</div></td></tr>
<tr><td>[44]</td><td>TIME_LAST_LOGIN</td><td>string</td><td>Date and time of last login</td></tr>
<tr><td colspan="4"><div class="placeholders">[ . . . ]</div></td></tr>
<tr><td>[47]</td><td>VERIFICATION_LEVEL_SUBMITTED</td><td>int</td><td>Level of highest verification application submitted from the account</td></tr>
<tr><td colspan="4"><div class="placeholders">[ . . . ]</div></td></tr>
<tr><td>[49]</td><td>COMP_COUNTRIES</td><td>array</td><td>Array of country codes based on your verification data (residence and nationality)</td></tr>
<tr><td>[50]</td><td>COMP_COUNTRIES_RESID</td><td>array</td><td>Array of country codes based on your verification data (residence only)</td></tr>
<tr><td>[51]</td><td>COMPL_ACCOUNT_TYPE</td><td>string</td><td>Type of verification ("individual" or "corporate")</td></tr>
  <tr><td colspan="4"><div class="placeholders">[ . . . ]</div></td></tr>
<tr><td>[53]</td><td>PERMITTED_BENEFICIARY</td><td>int</td><td>1 if true</td></tr>
<tr><td>[54]</td><td>IS_MERCHANT_ENTERPRISE</td><td>int</td><td>1 if true (when account is enterprise merchant)</td></tr>
</tbody>
</table>

<style>
  td:has(div.placeholders) {
    background-color: #ebebeb;
  }

  .placeholders {
    height: 10px;
    text-align: center;
    font-size: 16px;
    line-height: 8px;
  }
</style>
`}</HTMLBlock>

**Ratelimit**: 90 req/min

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "api-settings",
    "version": "2"
  },
  "servers": [
    {
      "url": "https://api.bitfinex.com/v2"
    }
  ],
  "security": [
    {}
  ],
  "paths": {
    "/auth/r/info/user": {
      "post": {
        "summary": "User Info",
        "description": "Retrieve an of important account data.",
        "operationId": "rest-auth-info-user",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "RAW_BODY": {
                    "type": "string",
                    "default": "{}",
                    "format": "json"
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "200",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "[\n  123456, //ID\n  \"email@email.com\", //EMAIL\n  \"AccountName\", //USERNAME\n  1613492801000, //MTS_ACCOUNT_CREATE\n  1, //VERIFIED\n  3, //VERIFICATION_LEVEL\n  null, //PLACEHOLDER\n  \"Lisbon\", //TIMEZONE\n  \"en\", //LOCALE\n  \"bitfinex\", //COMPANY\n  1, //EMAIL_VERIFIED\n  null, //PLACEHOLDER\n  null, //SUBACCOUNT_TYPE\n  null, //PLACEHOLDER\n  1613492801000, //MTS_MASTER_ACCOUNT_CREATE\n  79, //GROUP_ID\n  123456, //MASTER_ACCOUNT_ID\n  1, //INHERIT_MASTER_ACCOUNT_VERIFICATION\n  1, //IS_GROUP_MASTER\n  1, //GROUP_WITHDRAW_ENABLED\n  null, //PLACEHOLDER\n  null, //PPT_ENABLED\n  0, //MERCHANT_ENABLED\n  null, //COMPETITION_ENABLED\n  null, //PLACEHOLDER\n  null, //PLACEHOLDER\n  [\"u2f\"], //2FA_MODES\n  null, //PLACEHOLDER\n  0, //IS_SECURITIES_MASTER\n  null, //SECURITIES_ENABLED\n  null, //IS_SECURITIES_INVESTOR_ACCREDITED\n  null, //IS_SECURITIES_EL_SALVADOR\n  null, //PLACEHOLDER\n  null, //PLACEHOLDER\n  null, //PLACEHOLDER\n  null, //PLACEHOLDER\n  null, //PLACEHOLDER\n  null, //PLACEHOLDER\n  0, //ALLOW_DISABLE_CTXSWITCH\n  0, //CTXSWITCH_DISABLED\n  null, //PLACEHOLDER\n  null, //PLACEHOLDER\n  null, //PLACEHOLDER\n  null, //PLACEHOLDER\n  \"2022-09-06T12:14:14.600Z\", //TIME_LAST_LOGIN\n  null, //PLACEHOLDER\n  null, //PLACEHOLDER\n  null, //VERIFICATION_LEVEL_SUBMITTED\n  null, //PLACEHOLDER\n  [\"FR\", \"FR_Paris\"], //COMP_COUNTRIES\n  [\"FR\", \"FR_Paris\"], //COMP_COUNTRIES_RESID\n  null, //COMPL_ACCOUNT_TYPE\n  null, //PLACEHOLDER\n  null, //PLACEHOLDER\n  1 //IS_MERCHANT_ENTERPRISE\n]"
                  }
                },
                "schema": {
                  "type": "array"
                }
              }
            }
          },
          "400": {
            "description": "400",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {}
                }
              }
            }
          }
        },
        "deprecated": false
      }
    }
  },
  "x-readme": {
    "headers": [],
    "explorer-enabled": true,
    "proxy-enabled": true
  },
  "x-readme-fauxas": true
}
```
