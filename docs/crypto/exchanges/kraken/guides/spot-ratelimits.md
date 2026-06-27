---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/guides/spot-ratelimits
api_type: Guide
updated_at: 2026-05-27 19:58:44.883597
---

# Spot Trading Limits

The engine has two categories of limits:

  * Rate of transactions.
  * Open order count.

The limits are agnostic of the API used, i.e. there is a shared limit across REST, Websockets and FIX.

## Transaction Rate Limits

Each client has a rate counter **per pair** , the count starts at 0 and the count is incremented on each transaction by a given amount depending on the transaction type. The count is decremented over time by a decay rate based on client tier.

When the rate counter threshold is reached, the engine will generate `EOrder:Rate limit exceeded` rejection message.

Note, most clients will never reach the trading rate threshold and the restriction is designed to protect the market / platform when clients trading at higher frequencies with a larger quantity of orders.

### Incrementing the rate counter

The table below shows the increase in the rate counter for different transactions:

  * **Fixed count** : this is always applied on receipt of the transaction (even if the transaction fails validation).
  * **Decaying count** : this is an additional count depending on the resting time of the order. The size of the count depends on the number of seconds since the order was created or amended.

Transaction| Fixed| < 5s| < 10s| < 15s| < 45s| < 90s| < 300s  
---|---|---|---|---|---|---|---  
Add Order| +1| -| -| -| -| -| -  
Amend Order| +1| +3| +2| +1| -| -| -  
Edit Order| +1| +6| +5| +4| +2| +1| -  
Cancel Order| -| +8| +6| +5| +4| +2| +1  
Batch Add| +(n/2)| -| -| -| -| -| -  
Batch Cancel| -| +(8*n)| +(6*n)| +(5*n)| +(4*n)| +(2*n)| (1*n)  
  
Note, for batch orders:

  * `n` represents the number of orders in a batch.
  * If the rate counter in the batch exceeds maximum for a batch cancel, the requests in batch are still accepted.

#### Example: rate counter increase over short order lifetime

Scenario: a client sends a new order and amends the price after 7 seconds. After a further 36 seconds, the client cancels the order from the book, what would be the increase to the rate counter?

Description| Rate Count Change| Rate Count Total  
---|---|---  
Add order - fixed| +1| 1  
Amend order - fixed| +1| 2  
Amend order - decay < 15s| +2| 4  
Cancel order - decay < 45s| +4| 8  
  
The client will have accumulated a total rate counter value of **8** for this specific pair.

This simple example shows the _increase_ in rate counter only. In practise the rate counter is also decrementing over time, this will be covered in the next section.

### Decrementing the rate counter

The rate counter is decreased by a **decay rate every second** , the decay rate varies by client tier.

| Starter Tier| Intermediate Tier| Pro Tier  
---|---|---|---  
Rate counter decay rate| -1| -2.34| -3.75  
  
#### Example: rate counter decrease over 10 seconds

Scenario: a intermediate tier client has entered a burst of 50 orders and waited 10 seconds, what would be the new rate counter value at the end of the period?
    
    
    rate counter = (50 orders * add order) - (10 seconds * intermediate decay rate) = (50 * 1) - (10 * 2.34) = 26.6  
    

### Exceeding rate counter threshold

When the rate counter exceeds the threshold for the client tier, further transactions will be restricted with `EOrder:Rate limit exceeded` rejection until the rate counter has decayed below the threshold.

| Starter Tier| Intermediate Tier| Pro Tier  
---|---|---|---  
Rate counter threshold| 60| 125| 180  
  
### Additional rate counter information

  * The rate counter values can be monitored in the websockets feeds [openOrders (v1)](/api/docs/websocket-v1/openorders) or [executions (v2)](/api/docs/websocket-v2/executions).
  * A [rate counter calculator](https://support.kraken.com/hc/en-us/articles/360061656951-Trading-rate-limit-calculator) is available in the support pages.

## Open Order Limits

The open order limit is the maximum number of open orders **per pair**. When the open order threshold is reached, the engine will generate `EOrder:Orders limit exceeded` rejection message.

The maximum open order limit varies per client tier.

| Starter Tier| Intermediate Tier| Pro Tier  
---|---|---|---  
Max open orders per pair| 60| 80| 225  
* Transaction Rate Limits
* Incrementing the rate counter
* Decrementing the rate counter
* Exceeding rate counter threshold
* Additional rate counter information
  * Open Order Limits