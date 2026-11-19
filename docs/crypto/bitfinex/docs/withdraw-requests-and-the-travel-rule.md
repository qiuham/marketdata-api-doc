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
source_url: 'https://docs.bitfinex.com/docs/withdraw-requests-and-the-travel-rule'
updated_at: 2026-11-19
---

# Withdraw requests and the "Travel Rule"

As required by compliance regulation, when making a withdrawal from Bitfinex of $1,000 or more in value, specific information is sent to one or more Third-Party Services that provide Travel Rule compliance solutions, and, who make it available to VASPs, as required by the Travel Rule.

Travel Rule compliance is mandatory for withdraw requests originating from the frontend website or app.\
More details can be found here: <https://support.bitfinex.com/hc/en-us/articles/25285206917529-Understanding-the-Travel-Rule-on-Bitfinex>

**Important Notice**

**From 19th February 2025, Travel Rule will be required for withdraw requests originating from the API**, this applies to both the [V1](https://docs.bitfinex.com/v1/reference/rest-auth-withdrawal) and [V2](https://docs.bitfinex.com/reference/rest-auth-withdraw) Withdraw APIs.

If you consume these API endpoints, then please review this document, and your implementation, and make any required changes in order to avoid any disruption in service.

If non-compliant withdraw requests are received from the initiation date, the requests will be rejected.

**Withdraw API changes & Travel Rule**

The withdraw endpoint has the following additional fields:

`travel_rule_tos`: true,\
`vasp_did`: "did:ethr:0x36c12a3d41698534463a6dcda1c549b8f178249b",\
`vasp_name`: "Strawb Exchange Ltd",\
`beneficiary_self`: true,\
`dest_firstname`: "John",\
`dest_lastname`: "Doe",\
`dest_corp_name`: "Yotsuba Ltd"

`travel_rule_tos`\
If the request will supply Travel Rule data, then this flag needs to be set to `true`

`vasp_did`\
This identifies the recipient VASP (Virtual Service Asset Provider)\
A list of VASP IDs for all major exchanges can be obtained from this endpoint: [api.bitfinex.com/v2/ext/vasps](https://api.bitfinex.com/v2/ext/vasps)

`vasp_name`\
If a VASP id cannot be found, then this field can be used instead (e.g. use `vasp_did` OR `vasp_name`)\
data type is a string containing the name of the VASP

`dest_firstname`\
This field contains the beneficiaries first name; this can be a third-party, or yourself.

`dest_lastname`\
This field contains the beneficiaries last name; this can be a third-party, or yourself.\
If `dest_firstname`is supplied, then also supplying `dest_lastname`becomes mandatory, and vice-versa

`dest_corp_name`\
This field contains the beneficiary corporation, and would be used if you are withdrawing funds to a wallet or VASP account owned by a company. This could be your own company, or a third-party company.

`beneficiary_self`\
This flag indicates that the account requesting the withdraw will also be the beneficiary.\
This means that, for example, if you're withdrawing to your own account on a different exchange, you can set this flag to `true` as an alternative to providing `dest_firstname`, `dest_lastname`, `dest_corp_name`\
When this flag is true, the destination name will be extracted from your KYC data automatically.

**Example payloads**

**Travel Rule data required: Withdrawing to your personal account on another exchange:**

![](https://files.readme.io/63f0930a89055214cdbccd7f99f036b0889493286c9d71773268b28a95c16a77-image.png)

**Amount being withdrawn does not meet the Travel Rule threshold:**

![](https://files.readme.io/8ada7d912e95d9351b229616c7ec8660cf67ea70bba8dfba7a951bcdc651056c-image.png)

**Travel Rule data required: Withdrawing to your personal cold storage.**

![](https://files.readme.io/757a8cecbc17854fda926004888a91f16434357580d385a71d9b4a59323b223a-image.png)

**Travel Rule data required: Withdrawing to your personal account on another exchange (VASP identified by name)**

![](https://files.readme.io/a0f49ee2352b4fbe33ec5f109b91acdf6bce1400feaf7806305999f2e11ab762-image.png)

**Travel Rule data required: Withdrawing to a third-party persons cold wallet:**

![](https://files.readme.io/3752956fe4a34e36ce1160d95b6f325298aec2fdeec10c4d1edbd39bee7a7b28-image.png)

**Travel Rule required: Withdrawing to a third-party corporations cold wallet:**

![](https://files.readme.io/7c2020b6460ccd25269d8776689dbd20063124634d63a6bcb081b86a7e197219-image.png)

**Travel Rule required: Withdrawing to a third-party persons exchange account:**

![](https://files.readme.io/41273f8ccaa74d8667668c1f553a9c455c5108e4a44e7050a799ba1e5097aed3-image.png)
