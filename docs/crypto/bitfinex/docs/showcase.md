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
source_url: 'https://docs.bitfinex.com/docs/showcase'
updated_at: 2026-11-27
---

# Showcase

<div id="cards-list"> 

<div class="card"> <div class="card-image" style="background-image: url('http://blog.bitfinex.com/wp-content/uploads/2016/12/mobile-app.jpg')"> </div> <div class="card-link"> <a href="https://www.bitfinex.com/app" target="_blank">Bitfinex Mobile app</a> </div> </div>

<div class="card"> <div class="card-image" style="background-image: url('https://i.imgur.com/w7ZNVcL.jpg')"> </div> <div class="card-link"> <a href="https://www.quantconnect.com/brokerages/bitfinex" target="_blank"> QuantConnect</a> </div> </div>

<div class="card"> <div class="card-image" style="background: azure; font-size: 6rem; text-align: center;"> php </div> <div class="card-link"> <a href="https://github.com/mariodian/bitfinex-auto-lend" target="_blank">Bitfinex Autolend Bot</a> </div> </div>

<div class="card"> <div class="card-image" style="background-image: url('https://cdn-std.dprcdn.net/files/acc_572093/D88Zeo')"> </div> <div class="card-link"> <a href="https://cryptolend.net/" target="_blank"> CryptoLend </a> </div> </div>

<div class="card"> <div class="card-image" style="background-image: url('https://cdn-std.dprcdn.net/files/acc_572093/A83wbt')"> </div> <div class="card-link"> <a href="https://coinlend.org/" target="_blank"> CoinLend </a> </div> </div>

<div class="card"> <div class="card-image" style="background-image: url('https://i.imgur.com/ubHKhXy.png')"> </div> <div class="card-link"> <a href="https://bfxmargin.com/" target="_blank"> BFX Margin </a> </div> </div>

<div class="card"> <div class="card-image" style="background-image: url('https://i.imgur.com/KWAMEB1.png')"> </div> <div class="card-link"> <a href="https://www.lendary.net/" target="_blank"> Lendary </a> </div> </div>

<div class="card"> <div class="card-image" style="background-image: url('https://i.imgur.com/JcNdq5D.png')"> </div> <div class="card-link"> <a href="https://github.com/bitfinexcom/bfx-api-excel-demo" target="_blank"> BFX Excel Demo </a> </div> </div>

<div class="card"> <div class="card-image" style="background: grey; font-size: 6rem; text-align: center;"> ... </div> <div class="card-link"> <a href="https://cs.bitfinex.com/" target="_blank">Submit your showcase!</a> </div> </div>
</div>

<strong>Want to add your app here? Contact us at <a href="https://cs.bitfinex.com/"><https://cs.bitfinex.com/></a> to submit your showcase!</strong>

## Special: Import BFX API data into Excel with a Custom Function

> 🚧 Requirement
>
> Please note that the add-in is currently only available in Excel for **Windows**

The Bitfinex REST API offers users access to a variety of data generated on the Bitfinex Platform. In this special, we will show how public API data can easily be imported directly into an Excel spreadsheet through the use of VBA scripts. As a proof of concept, these scripts have been bundled into a handy add-in, which is available on [Github](https://github.com/bitfinexcom/bfx-api-excel-demo). Below, we will first provide instructions on the installation and usage of the add-in. Following that, we will go through a simplified version of the script in order to show how it can be easily recreated or customized for your specific needs.

### Requirements

The Excel add-in uses a custom function to directly load API data into your Excel spreadsheets. The script depends on several references that need to be enabled in the Visual Basic Editor. Since these references are only available in the Windows version of Excel, the add-in can only be used in Excel for Windows.

### Installing the add-in

1. Download the files from our [GitHub](https://github.com/bitfinexcom/bfx-api-excel-demo).
2. Extract the Zip file to a folder that you can easily find again.
3. Navigate to the BFX Function 1.0.xlam -> right click -> properties
4. At the bottom of the file properties, check the "Unblock" option to allow Excel to load the file. (note: depending on your security settings, this may not be a required step. On some devices, the unblock option will not be available. If that is the case for you, continue to the next step.)

![](https://files.readme.io/c2b4984-image_11.png "image (11).png")

5. In Excel, go to "File" -> "Options" -> "Add-ins".
6. At the bottom of the window that opened, select "Manage: Excel Add-ins" and click on "Go".
7. Click on "Browse" and navigate to the BFX Function 1.0.xlam file to add it to your Excel Add-ins.
8. Next, check the BFX Function 1.0 in the list of "Add-ins available" and press OK. (If the add-in does not appear, close down Excel, restart, and navigate back to this menu (see step 5).
9. The Add-in should now be available and load automatically when you start up Excel. If this is not the case, try following the steps again and make sure that the file is not blocked (step 4)

<Image align="center" className="border" width="smart" border={true} src="https://files.readme.io/f9c0af4-Addin_Activate.PNG" />

### Using the BFX() function

> 🚧 Formula separator
>
> The examples in this tutorial use a comma (",") as the separator between arguments in a function. Depending on your localized Excel settings, you may need to use a semicolon (";").
>
> Example: "=BFX("SYMBOL"; "Bid")

Using the custom function works similarly to any other function available in Excel. Simply select a cell into which you would like the data to load, start by typing "=BFX(" and fill out the arguments required for the field you wish to retrieve using the following syntax:

\=BFX(“SYMBOL”, “FIELD”, “TIMESTAMP”, “TIMEFRAME”, “PERIOD”, “SECOND\_SYMBOL”, “SECOND\_TIMESTAMP”)

Each argument for the function will need to be entered as a string, which means that you will need to place quotes ("") on either side of the information entered. Do note that it is not required to fill in all arguments for each call. If you do not use an argument at the end of the list, it can simply be left out. For example, to retrieve the best bid from the Tickers endpoint, only the "SYMBOL" and "FIELD" arguments need to be provided. As such, the call to use would be:

\=BFX(“SYMBOL”, “Bid”)

When skipping an argument in the middle of the list of arguments, be sure to still place a comma for the argument that you skip. For example, to skip the "TIMESTAMP" argument, the syntax would look like this:

\=BFX(“SYMBOL”, “FIELD”,,”TIMEFRAME”)

### Creating tables

Getting data into Excel through a custom function can be a very powerful tool. For example, by creating a column with different symbols and having a cell which designates the field which you wish to retrieve, you can easily create a custom table. Simply use the BFX function with the first argument referencing the cell that holds the first symbol of your table and the second argument as a fixed reference ($Collumn$Row) to the cell holding the name of the field to retrieve. Once the first row of your table is populated with data, simply drag down from the cell you just entered to populate the rest of the table.

After creating the table, it is also very easy to retrieve different information. Editing the cell used to designate the field that you are retrieving will automatically cause populated cells to update with the data related to the new field. Similarly, the symbols can be updated to retrieve data for different pairs or funding currencies.

![](https://files.readme.io/613a75c-AddinBFX.gif "AddinBFX.gif")

### Available fields

> 🚧 Arguments are case-sensitive
>
> Please note that arguments case-sensitive. This means that "Bid" will return data, whereas "BID" will return an "invalid field" error. Similarly, "BTCUSD" will return data, but "btcusd" will return an error.

The BFX() custom function can retrieve many different data points from the API. On the add-in's [GitHub page ](https://github.com/bitfinexcom/bfx-api-excel-demo), a CheatSheet file can be found with a full overview of all possible fields and the syntax required to retrieve them.

The following public endpoints are currently included in the function:

* [Tickers](https://docs.bitfinex.com/reference#rest-public-tickers)
* [Trades](https://docs.bitfinex.com/reference#rest-public-trades)(for historical prices)
* [Platform Status](https://docs.bitfinex.com/reference#rest-public-platform-status)
* [Stats](https://docs.bitfinex.com/reference#rest-public-stats1)
* [Candles](https://docs.bitfinex.com/reference#rest-public-candles)
* [Status](https://docs.bitfinex.com/reference#rest-public-status)

The BFX() function also includes calculation fields based on these endpoints. These fields will use one or multiple data points to calculate things like: price change, relative price change, volume for a specified period, the high or low within a specified period, the ratio of longs versus shorts, and many other useful figures and metrics. Check the CheatSheet file for on GitHub for all available fields.

### Limitations

The BFX() function relies on our REST API to retrieve data. This means that the function is also subject to the same limitations as our REST API. When data is retrieved through the function, each cell that needs to be populated requires a separate call to the API. When creating larger tables, the number of calls that need to be made can quickly add up, which may cause your IP address to be rate limited. When that happens, data will not be filled into your cells. If you have been rate limited, wait for 60 second and reduce the number of simultaneous calls made before trying again.

## BFX() Function - Technical Rundown

> 🚧 Enabling the VBA Editor
>
> If you wish to edit the VBA code for this add-in, you will need the VBA editor. You can open the editor from the developer tab in Excel. By default, the developer tab may not be enabled in your Excel ribbon. If that is the case, please find instructions on how to enable it [here](https://support.microsoft.com/en-us/office/show-the-developer-tab-e1192344-5e56-4d45-931b-e5fd9bea2d45).

Loading API data into Excel using VBA can be very powerful and is relatively easy to achieve. In this section, we will go through the add-in step by step to see how it functions. For instruction purposes, the examples here will use a simplified and much shorter version of the custom function which can only return two different fields: Bid (using the tickers endpoint) and Last\_Price\_Hist (using the trades endpoint).

### Setup

To return the best bid based on the ticker, only two arguments are required in the function: the symbol and the name of the field (“Bid”). To return the Last\_Price\_Hist, an additional Timestamp argument is necessary. This means that, for the purpose of retrieving these fields, the function would look as follows:

```text
Function BFX(Optional Symbol As String, Optional Field As String, Optional Timestamp As String)
```

Next, we declare the different variables that the function will use:

```text
Dim URL As String
Dim ApiData As String
Dim Pair As String
Dim Endpoint As String
Dim Query_Parameters As String
Dim Path_Parameters As String
```

### Defining variables

Following this, the first variable that will be defined is the “Pair”. The API requires trading pairs to be prepended by a ‘t’ and funding currencies to be prepended by an ‘f’. For example, BTCUSD will become “tBTCUSD” and USD will become “fUSD” when used for an API call. The following snippet of code uses the length of the entered symbol argument to automatically discern trading pairs from funding currencies and converts them to symbols which the Bitfinex API can recognize:

```text
If Len(Symbol) < 5 Then
	Pair = "f" + Symbol
Else
	Pair = "t" + Symbol
End If
```

Other variables will be assigned and used based on the requested field. First, the script will choose which endpoint and which parameters to use based on the arguments entered in the function. Here is an example of what the selection of the endpoint and parameters based on the “Field” argument looks like in VBA:

```text
If Field = "Bid" Then
    
    Endpoint = "tickers"
    Query_Parameters = "symbols=" + Pair
    URL = BuildURL(Endpoint, , Query_Parameters)
    ApiData = SendRequest(URL)

    BFX = ReturnField(ApiData, Field, Timeframe)
    
ElseIf Field = "Last_Price_Hist" Then
    
    Endpoint = "trades"
    Path_Parameters = Pair + "/hist"
    Query_Parameters = "end=" + Timestamp + "&limit=1"
    URL = BuildURL(Endpoint, Path_Parameters, Query_Parameters)
    ApiData = SendRequest(URL)

    BFX = ReturnField(ApiData, Field)

End If
```

The code checks the value of the “Field” argument. If it is equal to “Bid”, the script moves on to define the “Endpoint” variable as “tickers”. The documentation for this endpoint can be found here: <https://docs.bitfinex.com/reference#rest-public-tickers>

The tickers endpoint does not use any path parameters, so these do not need to be defined for this call. To retrieve a specific ticker, the endpoint uses the “symbols=” query parameter. In this case, we wish to retrieve the best bid for whichever pair or currency was entered as the “Symbol” argument. For a call that retrieves the best bid for BTCUSD, the query parameter will be defined as “symbols=tBTCUSD”.

### Adding more fields

The more fields added to the logical checks in the BFX() function (and in the ReturnField() function which will be explained later) along with the required parameters, the more fields the BFX() function is able to return. If you wish to add additional functionality to the BFX() function, you would start by adding an additional ElseIf block here or, if the data you are after can be retrieved from an endpoint that you are already using, by adding additional checks to the If/ElseIf statement. For example, the following If statement can be used to enable the function to return all of the separate elements returned by the tickers endpoint:

```text
If Field = "Bid" Or Field = "Bid_Size" Or Field = "Ask" Or Field = "Ask_Size" Or Field = "Daily_Change" Or Field = "Daily_Change_Relative" Or Field = "Last_Price" Or Field = "Volume" Or Field = "High" Or Field = "Low" Then
```

Certain endpoints may require additional parameters to be used. If you require user input for these parameters, additional (optional) arguments need to be added to the BFX() function.

Further steps to take in order to expand the functionality of the add-in can be found under the "Adding more fields (continued)" header further down the page.

### Building the URL

After defining the endpoint and parameters, the BFX() function calls the BuildURL(). The BuildURL() function takes three arguments: “Endpoint”, “Path\_Parameters”, and “Query\_Parameters”. The BuildURL() function works like this:

```text
Function BuildURL(Endpoint As String, Optional Path_Parameters As String, Optional Query_Parameters As String)

  Dim BaseURL As String
  BaseURL = "https://api-pub.bitfinex.com/v2/"

  BuildURL = BaseURL + Endpoint + "/" + Path_Parameters + "?" + Query_Parameters

End Function
```

The function takes the BaseURL, which is “<https://api-pub.bitfinex.com/v2/”> and combines it with the “Endpoint”, “Path\_Parameters”, and “Query\_Parameters” variables. In this case, the endpoint is “tickers”, there are no path parameters, and the query parameters are “symbols=tBTCUSD”. This means that the finished URL will be: <https://api-pub.bitfinex.com/v2/tickers/?symbols=tBTCUSD>. Opening this URL in your browser will show that this returns the ticker data for BTCUSD.

### Retrieving the data

After the URL has been contructed, the BFX() function now defines “ApiData” as the data returned by calling the SendRequest() function with the URL as its only argument. The SendRequest() function looks like this:

```text
Function SendRequest(URL As String)

Dim req As WinHttpRequest
Dim Response As String

Set req = New WinHttpRequest

req.Open "GET", URL
req.Send

Response = req.ResponseText

SendRequest = Response
End Function
```

The SendRequest() function requires “Microsoft WinHTTP Services” to be enabled in the VBA editor references. In the code above, “req” is declared and defined as a WinHttpRequest object. The object has several methods available for which more information can be found in [Microsoft's documentation pages](https://docs.microsoft.com/en-us/windows/win32/winhttp/winhttprequest). In this case, the script uses the “.Open” and “.Send” methods to open a connection and send the request. The “Response” variable is then defined as the “ResponseText” property of the “req” object. Finally, the “Response” is returned to the BFX() function.

### Parsing and returning specific data from the response array

Following this, the BFX() function will return the response of a call to the ReturnField() function. The ReturnField() function accepts three arguments: “ApiData” (the “ResponseText” returned by the SendRequest() function), the “Field” (“Bid”, in our example), and “TimeFrame” (not used for this particular call). The ReturnField() function (shortened for this example) looks like this:

```text
Function ReturnField(ApiData As String, Field As String, Optional Timeframe As String)

Dim ResponseObject As Object
Set ResponseObject = JsonConverter.ParseJson(ApiData)

If Field = "Bid" Then
	ReturnField = ResponseObject(1)(2)
ElseIf Field = "Last_Price_Hist" Then
	ReturnField = ResponseObject(1)(4)
Else
	ReturnField = “Error, Unknown Field”
End If
```

The ReturnField() function declares a ResponseObject variable as an object. It then uses a publicly available JSON converter library to parse the JSON ApiData so that the value of individual elements from the API response array can be returned. The library is included in the add-in as a separate module, but can also be found on [GitHub](https://github.com/VBA-tools/VBA-JSON).

As an example, let's return to the API call which we created earlier: <https://api-pub.bitfinex.com/v2/tickers?symbols=tBTCUSD>

Calling the API with this URL returns the ticker data for BTCUSD. An example of such data is:

\[\["tBTCUSD",13136,52.935694080000005,13137,50.68218988,296,0.0231,13137,2184.69922612,13178,12803]]

The response is an array within an array and can be mapped as follows:

\[\[SYMBOL, BID, BID\_SIZE, ASK, ASK\_SIZE, DAILY\_CHANGE, DAILY\_CHANGE\_RELATIVE, LAST\_PRICE, VOLUME, HIGH, LOW]\[SYMBOL, BID, BID\_SIZE, ASK, ASK\_SIZE, DAILY\_CHANGE, DAILY\_CHANGE\_RELATIVE, LAST\_PRICE, VOLUME, HIGH, LOW]]

The ReturnField() function checks the “Field” argument used to determine which element of the response array should be returned by the function. By default, the array uses a base 1 index, which means that the first element of the array will have the index 1. To have the function return the “Bid” element, the script will need to return the 2nd element of the 1st inner array. To do this, the script returns ResponseObject(1)(2). Should the requested “Field” have been “Last\_Price\_Hist”, then the script would have returned ResponseObject(1)(4). If the “Field” argument entered is not present in the ReturnField() function, the script will print an error in the cell from which the BFX() function was called.

### Adding more fields (continued)

If you wish to expand on the add-in, this is, after changing the If/ElseIf statements in the BFX() function, the second place that you need to edit. For example, the tickers endpoint also returns the best “Ask”. To enable to function to return this field, you would add the following ElseIf statement after the “If Field = ‘Bid’ Then” block:

```text
ElseIf Field = "Ask" Then
	ReturnField = ResponseObject(1)(3)
```

#### Calculation Fields

The function is not limited to returning only values which are directly available from the API. It is also possible to edit the script to make calculations based on data returned by one or more calls to the API. For example, you could return (an approximation) of the trading volume on a specific pair between two timestamps with the following code block:

```text
ElseIf Field = "Custom_Volume" Then

  Dim AggregateVolume As Double

  If ResponseObject.Count < 10000 Then   
    For Each Entry In ResponseObject
    	AggregateVolume = AggregateVolume + Entry(6)
    Next
    	ReturnField = AggregateVolume
  Else
  	ReturnField = "Candle limit exceeded. Increase candle size or reduce the spread between the first and second timestamp"
    
End If
```

In this example, the BFX() function called the Candles endpoint using start and end timestamps as well as a candle size argument provided by the user. The ReturnField() function then checks if the number of candles returned is lower than the maximum number of candles that can be returned in a single call to the candles endpoint. If the number of candles is equal to or greater than the maximum, the function returns an error. If the number of candles returned falls within the limit, the script loops through all the candles in the response and aggregates the volume of all of the candles in the “AggregateVolume” variable. The value of this variable is then returned by the function.

#### Recursive Use

For some calculation fields, rather than using the BFX() function to set up all parameters and then calling the ReturnField() function for data, the BFX() function can also call itself. For example, the BFX() function can return the total position size of all short positions on a particular currency. The function also offers a field to calculate the difference in the size of all short positions between two timestamps. To do this, the field "Short\_Size\_Change"  calls the BFX() function with the field "Pos\_Size\_Short" for two different timestamps and then returns the difference. With this method, if you wish to make certain calculations more quickly, it is very easy to add custom fields to the BFX() function. Here is how it would look in code:

```text
ElseIf Field = "Short_Size_Change" Then
    
    Data1 = BFX(Symbol, "Pos_Size_Short", Timestamp)
    Data2 = BFX(Symbol, "Pos_Size_Short", Second_Timestamp)

    BFX = Data2 - Data1
             
End If
```

### Conclusion

And that is all there is to it! We hope you enjoyed this look into the possibilities of using VBA to load our API data into Excel and we hope that you can use this knowledge to your advantage. We welcome everyone to use this code as they see fit or to fork the GitHub repository to edit and expand the existing script to their own specifications. Happy trading!
