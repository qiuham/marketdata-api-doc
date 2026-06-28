---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/guides/futures-websockets
api_type: WebSocket
updated_at: 2026-05-27 19:57:54.812807
---

# Futures Websockets

## Sign challenge

The subscribe and unsubscribe requests to WebSocket private feeds require a signed challenge message with the user `api_secret`.

The challenge is obtained as is shown in Section WebSocket API Public (using the `api_key`).

Authenticated requests must include both the original challenge message (`original_challenge`) and the signed (`signed_challenge`) in JSON format.

### Challenge

> Challenge example
    
    
    c100b894-1729-464d-ace1-52dbce11db42  
    

The challenge is a [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier) string.

The steps to sign the challenge are the same as the steps to generate an authenticated HTTP request except for step 1 which now is just the `challenge` string:

  1. Hash the challenge with the [SHA-256 algorithm](https://en.wikipedia.org/wiki/SHA-2)
  2. [Base64-decode](https://en.wikipedia.org/wiki/Base64) your `api_secret`
  3. Use the result of step 2 to hash the result of step 1 with the [HMAC-SHA-512 algorithm](https://en.wikipedia.org/wiki/Hash-based_message_authentication_code)
  4. [Base64-encode](https://en.wikipedia.org/wiki/Base64) the result of step 3

The result of the step 4 is the signed challenge which will be included in the subscribe request.

The table below shows the expected output from example inputs:

Name| Value  
---|---  
`challenge`| `c100b894-1729-464d-ace1-52dbce11db42`  
`api_secret`| `7zxMEF5p/Z8l2p2U7Ghv6x14Af+Fx+92tPgUdVQ748FOIrEoT9bgT+bTRfXc5pz8na+hL/QdrCVG7bh9KpT0eMTm`  
signed output| `4JEpF3ix66GA2B+ooK128Ift4XQVtc137N9yeg4Kqsn9PI0Kpzbysl9M1IeCEdjg0zl00wkVqcsnG4bmnlMb3A==`  
  
## Subscriptions

Subscriptions requests are sent through a web socket connection.

To subscribe to a feed, a web socket connection is required to establish a connection using the following URL:

`wss://futures.kraken.com/ws/v1`

### Keeping the connection alive

In order to keep the websocket connection alive, you will need to make a ping request at least every 60 seconds. You can see this in our [sample implementation](https://github.com/CryptoFacilities/WebSocket-v1-Python/blob/master/cfWebSocketApiV1.py#L138).

## Snapshots and updates

For ease of use, most web socket feeds first send a snapshot of the history or current state and subsequently send real-time updates.

### Authentication

In order to subscription to a private feed, clients must pass a challenge which involves signing a message (see Section Sign Challenge) with the private API key. First, a message must be sent to request the challenge. Second, the solved challenge has to be passed in every subscribe and unsubscribe message that is sent.

  * Sign challenge
* Challenge
  * Subscriptions
* Keeping the connection alive
  * Snapshots and updates
* Authentication