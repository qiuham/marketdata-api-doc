---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/asset/portfolio-margin
api_type: REST
updated_at: 2026-11-13 19:21:46.922396
---

# Get Portfolio Margin Info

Query portfolio margin account balance and asset P&L range information. The data returned by this endpoint is consistent with what is displayed on the [web page](https://www.bybit.com/trade/usdc/pm/umpm).

### HTTP Request

GET`/v5/asset/portfolio-margin`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
baseCoin| false| string| Base coin, e.g. `BTC`, `ETH`. Returns all if not passed  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
wallet| object| Wallet info  
> equity| string| Equity  
> cashBalance| string| Cash balance  
> marginBalance| string| Margin balance  
> availableBalance| string| Available balance  
> accountIM| string| Account initial margin  
> accountMM| string| Account maintenance margin  
> accountMMRate| string| Account maintenance margin rate  
> accountIMRate| string| Account initial margin rate  
assetPnlRange| array| Asset P&L range list  
> baseCoin| string| Base coin, e.g. `BTC`  
> totalPnlRanges| object| Aggregated P&L ranges by contract type  
>> ALL| object| Combined P&L range across all contract types  
>> PERPETUAL| object| P&L range for perpetual positions  
>> OPTION| object| P&L range for option positions  
>>> pnlRanges| array| P&L range data points  
>>>> priceScale| string| Price change scale, e.g. `-0.1` means -10%  
>>>> pnls| array| P&L values at this price scale  
> perpPositionPnlRanges| array| P&L ranges per perpetual position  
>> symbolName| string| Symbol name  
>> position| string| Position size  
>> pnlRanges| array| P&L range data points (same structure as above)  
>> sessionAvgPrice| string| Session average price  
>> markPrice| string| Mark price  
>> orderSize| string| Open order size  
>> contractType| integer| Contract type  
>> settleCoin| string| Settlement coin  
>> symbolAlias| string| Symbol alias  
> optionExpiryDatePnlRanges| array| P&L ranges grouped by option expiry date  
>> expiryDateRepresentation| string| Expiry date, e.g. `25SEP26`  
>> pnlRanges| array| P&L range data points. Each `pnls` array contains values for multiple IV shock scenarios  
>> optionPositionPnlRanges| array| P&L ranges per option position  
>>> symbolName| string| Option symbol name  
>>> position| string| Position size  
>>> pnlRanges| array| P&L range data points  
>>> sessionAvgPrice| string| Session average price  
>>> markPrice| string| Mark price  
>>> orderSize| string| Open order size  
>>> contractType| integer| Contract type  
>>> settleCoin| string| Settlement coin  
> contingency| object| Contingency margin info  
>> optionContingency| string| Option contingency  
>> futureDeltaContingency| string| Future delta contingency  
>> optionVegaContingency| string| Option vega contingency  
>> contingencyComponents| string| Total contingency components  
>> usdtUsdcContingency| string| USDT/USDC contingency  
>> futureContingency| string| Future contingency  
> asset| object| Asset margin info  
>> coin| string| Coin  
>> assetIM| string| Asset initial margin  
>> assetMM| string| Asset maintenance margin  
> maxLossPriceMove| string| Max loss price move scenario  
> maxLossIvShock| string| Max loss IV shock scenario  
> totalClosePzFee| string| Total close position fee  
> spotHedgeInfo| object| Spot hedge info  
>> hedgeSpotSize| string| Hedge spot size  
>> walletBalance| string| Spot wallet balance  
>> usdIndexPrice| string| USD index price  
>> pnlRanges| array| P&L range data points for spot hedge  
> maxLossIvShockList| array| IV shock values corresponding to each price scale scenario  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/asset/portfolio-margin?baseCoin=BTC HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1773230920000  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
      
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "Success",  
        "result": {  
            "wallet": {  
                "equity": "52197.86892104",  
                "cashBalance": "45391.74423708",  
                "marginBalance": "52145.70917115",  
                "availableBalance": "50893.36062347",  
                "accountIM": "1304.50829757",  
                "accountMM": "1069.93399838",  
                "accountMMRate": "0.0204",  
                "accountIMRate": "0.0249"  
            },  
            "assetPnlRange": [  
                {  
                    "baseCoin": "BTC",  
                    "totalPnlRanges": {  
                        "ALL": {  
                            "pnlRanges": [  
                                {"priceScale": "-0.1", "pnls": ["-1004.74710000"]},  
                                {"priceScale": "-0.08", "pnls": ["-807.88000000"]},  
                                {"priceScale": "-0.06", "pnls": ["-610.19020000"]},  
                                {"priceScale": "-0.04", "pnls": ["-411.59200000"]},  
                                {"priceScale": "-0.02", "pnls": ["-212.00760000"]},  
                                {"priceScale": "0.0", "pnls": ["-11.36910000"]},  
                                {"priceScale": "0.02", "pnls": ["191.78950000"]},  
                                {"priceScale": "0.04", "pnls": ["396.10080000"]},  
                                {"priceScale": "0.06", "pnls": ["601.59360000"]},  
                                {"priceScale": "0.08", "pnls": ["808.28220000"]},  
                                {"priceScale": "0.1", "pnls": ["1016.16720000"]}  
                            ]  
                        },  
                        "PERPETUAL": {  
                            "pnlRanges": [  
                                {"priceScale": "-0.1", "pnls": ["-972.14482880"]},  
                                {"priceScale": "-0.08", "pnls": ["-777.71586304"]},  
                                {"priceScale": "-0.06", "pnls": ["-583.28689728"]},  
                                {"priceScale": "-0.04", "pnls": ["-388.85793152"]},  
                                {"priceScale": "-0.02", "pnls": ["-194.42896576"]},  
                                {"priceScale": "0.0", "pnls": ["0.00000000"]},  
                                {"priceScale": "0.02", "pnls": ["194.42896576"]},  
                                {"priceScale": "0.04", "pnls": ["388.85793152"]},  
                                {"priceScale": "0.06", "pnls": ["583.28689728"]},  
                                {"priceScale": "0.08", "pnls": ["777.71586304"]},  
                                {"priceScale": "0.1", "pnls": ["972.14482880"]}  
                            ]  
                        },  
                        "OPTION": {  
                            "pnlRanges": [  
                                {"priceScale": "-0.1", "pnls": ["-39.65273684"]},  
                                {"priceScale": "-0.08", "pnls": ["-35.80450518"]},  
                                {"priceScale": "-0.06", "pnls": ["-31.13352117"]},  
                                {"priceScale": "-0.04", "pnls": ["-25.55420042"]},  
                                {"priceScale": "-0.02", "pnls": ["-18.98866670"]},  
                                {"priceScale": "0.0", "pnls": ["-11.36906857"]},  
                                {"priceScale": "0.02", "pnls": ["-2.63944748"]},  
                                {"priceScale": "0.04", "pnls": ["7.24291762"]},  
                                {"priceScale": "0.06", "pnls": ["18.30672359"]},  
                                {"priceScale": "0.08", "pnls": ["30.56641060"]},  
                                {"priceScale": "0.1", "pnls": ["44.02244694"]}  
                            ]  
                        }  
                    },  
                    "perpPositionPnlRanges": [  
                        {  
                            "symbolName": "BTCUSDT",  
                            "position": "0.038",  
                            "pnlRanges": [  
                                {"priceScale": "-0.1", "pnls": ["-972.14482880"]},  
                                {"priceScale": "-0.08", "pnls": ["-777.71586304"]},  
                                {"priceScale": "-0.06", "pnls": ["-583.28689728"]},  
                                {"priceScale": "-0.04", "pnls": ["-388.85793152"]},  
                                {"priceScale": "-0.02", "pnls": ["-194.42896576"]},  
                                {"priceScale": "0.0", "pnls": ["0.00000000"]},  
                                {"priceScale": "0.02", "pnls": ["194.42896576"]},  
                                {"priceScale": "0.04", "pnls": ["388.85793152"]},  
                                {"priceScale": "0.06", "pnls": ["583.28689728"]},  
                                {"priceScale": "0.08", "pnls": ["777.71586304"]},  
                                {"priceScale": "0.1", "pnls": ["972.14482880"]}  
                            ],  
                            "sessionAvgPrice": "75995.4295",  
                            "markPrice": "255902.31000000",  
                            "orderSize": "0.0",  
                            "contractType": 2,  
                            "settleCoin": "USDT",  
                            "symbolAlias": "BTCUSDT"  
                        }  
                    ],  
                    "optionExpiryDatePnlRanges": [  
                        {  
                            "expiryDateRepresentation": "25SEP26",  
                            "pnlRanges": [  
                                {"priceScale": "-0.1", "pnls": ["-24.06747339", "-33.15841013", "-39.65273684"]},  
                                {"priceScale": "-0.08", "pnls": ["-18.12509537", "-28.31048642", "-35.80450518"]},  
                                {"priceScale": "-0.06", "pnls": ["-11.36193138", "-22.62748031", "-31.13352117"]},  
                                {"priceScale": "-0.04", "pnls": ["-3.73852526", "-16.04846592", "-25.55420042"]},  
                                {"priceScale": "-0.02", "pnls": ["4.77766694", "-8.52041879", "-18.98866670"]},  
                                {"priceScale": "0.0", "pnls": ["14.21190294", "0.00067229", "-11.36906857"]},  
                                {"priceScale": "0.02", "pnls": ["24.58198339", "9.54902598", "-2.63944748"]},  
                                {"priceScale": "0.04", "pnls": ["35.89827143", "20.14862960", "7.24291762"]},  
                                {"priceScale": "0.06", "pnls": ["48.16388381", "31.81313064", "18.30672359"]},  
                                {"priceScale": "0.08", "pnls": ["61.37503018", "44.54603289", "30.56641060"]},  
                                {"priceScale": "0.1", "pnls": ["75.52147477", "58.34116026", "44.02244694"]}  
                            ],  
                            "optionPositionPnlRanges": [  
                                {  
                                    "symbolName": "BTC-25SEP26-80000-C-USDT",  
                                    "position": "0.02",  
                                    "pnlRanges": [  
                                        {"priceScale": "-0.1", "pnls": ["-24.06747339", "-33.15841013", "-39.65273684"]},  
                                        {"priceScale": "-0.08", "pnls": ["-18.12509537", "-28.31048642", "-35.80450518"]},  
                                        {"priceScale": "-0.06", "pnls": ["-11.36193138", "-22.62748031", "-31.13352117"]},  
                                        {"priceScale": "-0.04", "pnls": ["-3.73852526", "-16.04846592", "-25.55420042"]},  
                                        {"priceScale": "-0.02", "pnls": ["4.77766694", "-8.52041879", "-18.98866670"]},  
                                        {"priceScale": "0.0", "pnls": ["14.21190294", "0.00067229", "-11.36906857"]},  
                                        {"priceScale": "0.02", "pnls": ["24.58198339", "9.54902598", "-2.63944748"]},  
                                        {"priceScale": "0.04", "pnls": ["35.89827143", "20.14862960", "7.24291762"]},  
                                        {"priceScale": "0.06", "pnls": ["48.16388381", "31.81313064", "18.30672359"]},  
                                        {"priceScale": "0.08", "pnls": ["61.37503018", "44.54603289", "30.56641060"]},  
                                        {"priceScale": "0.1", "pnls": ["75.52147477", "58.34116026", "44.02244694"]}  
                                    ],  
                                    "sessionAvgPrice": "0",  
                                    "markPrice": "2608.56395729",  
                                    "orderSize": "0.0",  
                                    "contractType": 5,  
                                    "settleCoin": "USDT"  
                                }  
                            ]  
                        }  
                    ],  
                    "contingency": {  
                        "optionContingency": "0.00000000",  
                        "futureDeltaContingency": "56.89174177",  
                        "optionVegaContingency": "0.00000000",  
                        "contingencyComponents": "57.69544638",  
                        "usdtUsdcContingency": "0.00000000",  
                        "futureContingency": "0.80370460"  
                    },  
                    "asset": {  
                        "coin": "BTC",  
                        "assetIM": "1274.8190514137673",  
                        "assetMM": "1062.3492095114727"  
                    },  
                    "maxLossPriceMove": "-0.1",  
                    "maxLossIvShock": "-0.2",  
                    "totalClosePzFee": "-0.2",  
                    "spotHedgeInfo": {  
                        "hedgeSpotSize": "-0.00100006",  
                        "walletBalance": "-0.00000007",  
                        "usdIndexPrice": "0",  
                        "pnlRanges": [  
                            {"priceScale": "-0.1", "pnls": ["7.05047869"]},  
                            {"priceScale": "-0.08", "pnls": ["5.64038295"]},  
                            {"priceScale": "-0.06", "pnls": ["4.23028721"]},  
                            {"priceScale": "-0.04", "pnls": ["2.82019147"]},  
                            {"priceScale": "-0.02", "pnls": ["1.41009574"]},  
                            {"priceScale": "0.0", "pnls": ["0"]},  
                            {"priceScale": "0.02", "pnls": ["0"]},  
                            {"priceScale": "0.04", "pnls": ["0"]},  
                            {"priceScale": "0.06", "pnls": ["0"]},  
                            {"priceScale": "0.08", "pnls": ["0"]},  
                            {"priceScale": "0.1", "pnls": ["0"]}  
                        ]  
                    },  
                    "maxLossIvShockList": ["-0.2", "-0.2", "-0.2", "-0.2", "-0.2", "-0.2", "-0.2", "-0.2", "-0.2", "-0.2", "-0.2"]  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1774319290506  
    }

---

# 查詢組合保證金信息

查詢組合保證金帳戶的資產餘額及資產盈虧範圍信息。該接口返回的內容與 [網頁端](https://www.bybit.com/trade/usdc/pm/umpm) 顯示的數據一致。

### HTTP 請求

GET`/v5/asset/portfolio-margin`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
baseCoin| false| string| 基礎幣種，如 `BTC`、`ETH`。不傳則返回全部  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
wallet| object| 錢包信息  
> equity| string| 權益  
> cashBalance| string| 現金餘額  
> marginBalance| string| 保證金餘額  
> availableBalance| string| 可用餘額  
> accountIM| string| 賬戶初始保證金  
> accountMM| string| 賬戶維持保證金  
> accountMMRate| string| 賬戶維持保證金率  
> accountIMRate| string| 賬戶初始保證金率  
assetPnlRange| array| 資產盈虧範圍列表  
> baseCoin| string| 基礎幣種，如 `BTC`  
> totalPnlRanges| object| 按合約類型彙總的盈虧範圍  
>> ALL| object| 所有合約類型的合計盈虧範圍  
>> PERPETUAL| object| 永續合約倉位盈虧範圍  
>> OPTION| object| 期權倉位盈虧範圍  
>>> pnlRanges| array| 盈虧範圍數據點  
>>>> priceScale| string| 價格變動幅度，如 `-0.1` 表示 -10%  
>>>> pnls| array| 該價格幅度下的盈虧值  
> perpPositionPnlRanges| array| 各永續倉位盈虧範圍  
>> symbolName| string| 交易對名稱  
>> position| string| 倉位大小  
>> pnlRanges| array| 盈虧範圍數據點（結構同上）  
>> sessionAvgPrice| string| 本次會話平均價格  
>> markPrice| string| 標記價格  
>> orderSize| string| 掛單數量  
>> contractType| integer| 合約類型  
>> settleCoin| string| 結算幣種  
>> symbolAlias| string| 交易對別名  
> optionExpiryDatePnlRanges| array| 按期權到期日分組的盈虧範圍  
>> expiryDateRepresentation| string| 到期日，如 `25SEP26`  
>> pnlRanges| array| 盈虧範圍數據點，`pnls` 數組包含多個IV衝擊情景下的值  
>> optionPositionPnlRanges| array| 各期權倉位盈虧範圍  
>>> symbolName| string| 期權合約名稱  
>>> position| string| 倉位大小  
>>> pnlRanges| array| 盈虧範圍數據點  
>>> sessionAvgPrice| string| 本次會話平均價格  
>>> markPrice| string| 標記價格  
>>> orderSize| string| 掛單數量  
>>> contractType| integer| 合約類型  
>>> settleCoin| string| 結算幣種  
> contingency| object| 應急保證金信息  
>> optionContingency| string| 期權應急保證金  
>> futureDeltaContingency| string| 期貨Delta應急保證金  
>> optionVegaContingency| string| 期權Vega應急保證金  
>> contingencyComponents| string| 應急保證金合計  
>> usdtUsdcContingency| string| USDT/USDC應急保證金  
>> futureContingency| string| 期貨應急保證金  
> asset| object| 資產保證金信息  
>> coin| string| 幣種  
>> assetIM| string| 資產初始保證金  
>> assetMM| string| 資產維持保證金  
> maxLossPriceMove| string| 最大虧損對應的價格變動情景  
> maxLossIvShock| string| 最大虧損對應的IV衝擊情景  
> totalClosePzFee| string| 平倉手續費合計  
> spotHedgeInfo| object| 現貨對沖信息  
>> hedgeSpotSize| string| 對沖現貨數量  
>> walletBalance| string| 現貨錢包餘額  
>> usdIndexPrice| string| USD指數價格  
>> pnlRanges| array| 現貨對沖盈虧範圍數據點  
> maxLossIvShockList| array| 各價格情景對應的IV衝擊值列表  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/asset/portfolio-margin?baseCoin=BTC HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1773230920000  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
      
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "Success",  
        "result": {  
            "wallet": {  
                "equity": "52197.86892104",  
                "cashBalance": "45391.74423708",  
                "marginBalance": "52145.70917115",  
                "availableBalance": "50893.36062347",  
                "accountIM": "1304.50829757",  
                "accountMM": "1069.93399838",  
                "accountMMRate": "0.0204",  
                "accountIMRate": "0.0249"  
            },  
            "assetPnlRange": [  
                {  
                    "baseCoin": "BTC",  
                    "totalPnlRanges": {  
                        "ALL": {  
                            "pnlRanges": [  
                                {"priceScale": "-0.1", "pnls": ["-1004.74710000"]},  
                                {"priceScale": "-0.08", "pnls": ["-807.88000000"]},  
                                {"priceScale": "-0.06", "pnls": ["-610.19020000"]},  
                                {"priceScale": "-0.04", "pnls": ["-411.59200000"]},  
                                {"priceScale": "-0.02", "pnls": ["-212.00760000"]},  
                                {"priceScale": "0.0", "pnls": ["-11.36910000"]},  
                                {"priceScale": "0.02", "pnls": ["191.78950000"]},  
                                {"priceScale": "0.04", "pnls": ["396.10080000"]},  
                                {"priceScale": "0.06", "pnls": ["601.59360000"]},  
                                {"priceScale": "0.08", "pnls": ["808.28220000"]},  
                                {"priceScale": "0.1", "pnls": ["1016.16720000"]}  
                            ]  
                        },  
                        "PERPETUAL": {  
                            "pnlRanges": [  
                                {"priceScale": "-0.1", "pnls": ["-972.14482880"]},  
                                {"priceScale": "-0.08", "pnls": ["-777.71586304"]},  
                                {"priceScale": "-0.06", "pnls": ["-583.28689728"]},  
                                {"priceScale": "-0.04", "pnls": ["-388.85793152"]},  
                                {"priceScale": "-0.02", "pnls": ["-194.42896576"]},  
                                {"priceScale": "0.0", "pnls": ["0.00000000"]},  
                                {"priceScale": "0.02", "pnls": ["194.42896576"]},  
                                {"priceScale": "0.04", "pnls": ["388.85793152"]},  
                                {"priceScale": "0.06", "pnls": ["583.28689728"]},  
                                {"priceScale": "0.08", "pnls": ["777.71586304"]},  
                                {"priceScale": "0.1", "pnls": ["972.14482880"]}  
                            ]  
                        },  
                        "OPTION": {  
                            "pnlRanges": [  
                                {"priceScale": "-0.1", "pnls": ["-39.65273684"]},  
                                {"priceScale": "-0.08", "pnls": ["-35.80450518"]},  
                                {"priceScale": "-0.06", "pnls": ["-31.13352117"]},  
                                {"priceScale": "-0.04", "pnls": ["-25.55420042"]},  
                                {"priceScale": "-0.02", "pnls": ["-18.98866670"]},  
                                {"priceScale": "0.0", "pnls": ["-11.36906857"]},  
                                {"priceScale": "0.02", "pnls": ["-2.63944748"]},  
                                {"priceScale": "0.04", "pnls": ["7.24291762"]},  
                                {"priceScale": "0.06", "pnls": ["18.30672359"]},  
                                {"priceScale": "0.08", "pnls": ["30.56641060"]},  
                                {"priceScale": "0.1", "pnls": ["44.02244694"]}  
                            ]  
                        }  
                    },  
                    "perpPositionPnlRanges": [  
                        {  
                            "symbolName": "BTCUSDT",  
                            "position": "0.038",  
                            "pnlRanges": [  
                                {"priceScale": "-0.1", "pnls": ["-972.14482880"]},  
                                {"priceScale": "-0.08", "pnls": ["-777.71586304"]},  
                                {"priceScale": "-0.06", "pnls": ["-583.28689728"]},  
                                {"priceScale": "-0.04", "pnls": ["-388.85793152"]},  
                                {"priceScale": "-0.02", "pnls": ["-194.42896576"]},  
                                {"priceScale": "0.0", "pnls": ["0.00000000"]},  
                                {"priceScale": "0.02", "pnls": ["194.42896576"]},  
                                {"priceScale": "0.04", "pnls": ["388.85793152"]},  
                                {"priceScale": "0.06", "pnls": ["583.28689728"]},  
                                {"priceScale": "0.08", "pnls": ["777.71586304"]},  
                                {"priceScale": "0.1", "pnls": ["972.14482880"]}  
                            ],  
                            "sessionAvgPrice": "75995.4295",  
                            "markPrice": "255902.31000000",  
                            "orderSize": "0.0",  
                            "contractType": 2,  
                            "settleCoin": "USDT",  
                            "symbolAlias": "BTCUSDT"  
                        }  
                    ],  
                    "optionExpiryDatePnlRanges": [  
                        {  
                            "expiryDateRepresentation": "25SEP26",  
                            "pnlRanges": [  
                                {"priceScale": "-0.1", "pnls": ["-24.06747339", "-33.15841013", "-39.65273684"]},  
                                {"priceScale": "-0.08", "pnls": ["-18.12509537", "-28.31048642", "-35.80450518"]},  
                                {"priceScale": "-0.06", "pnls": ["-11.36193138", "-22.62748031", "-31.13352117"]},  
                                {"priceScale": "-0.04", "pnls": ["-3.73852526", "-16.04846592", "-25.55420042"]},  
                                {"priceScale": "-0.02", "pnls": ["4.77766694", "-8.52041879", "-18.98866670"]},  
                                {"priceScale": "0.0", "pnls": ["14.21190294", "0.00067229", "-11.36906857"]},  
                                {"priceScale": "0.02", "pnls": ["24.58198339", "9.54902598", "-2.63944748"]},  
                                {"priceScale": "0.04", "pnls": ["35.89827143", "20.14862960", "7.24291762"]},  
                                {"priceScale": "0.06", "pnls": ["48.16388381", "31.81313064", "18.30672359"]},  
                                {"priceScale": "0.08", "pnls": ["61.37503018", "44.54603289", "30.56641060"]},  
                                {"priceScale": "0.1", "pnls": ["75.52147477", "58.34116026", "44.02244694"]}  
                            ],  
                            "optionPositionPnlRanges": [  
                                {  
                                    "symbolName": "BTC-25SEP26-80000-C-USDT",  
                                    "position": "0.02",  
                                    "pnlRanges": [  
                                        {"priceScale": "-0.1", "pnls": ["-24.06747339", "-33.15841013", "-39.65273684"]},  
                                        {"priceScale": "-0.08", "pnls": ["-18.12509537", "-28.31048642", "-35.80450518"]},  
                                        {"priceScale": "-0.06", "pnls": ["-11.36193138", "-22.62748031", "-31.13352117"]},  
                                        {"priceScale": "-0.04", "pnls": ["-3.73852526", "-16.04846592", "-25.55420042"]},  
                                        {"priceScale": "-0.02", "pnls": ["4.77766694", "-8.52041879", "-18.98866670"]},  
                                        {"priceScale": "0.0", "pnls": ["14.21190294", "0.00067229", "-11.36906857"]},  
                                        {"priceScale": "0.02", "pnls": ["24.58198339", "9.54902598", "-2.63944748"]},  
                                        {"priceScale": "0.04", "pnls": ["35.89827143", "20.14862960", "7.24291762"]},  
                                        {"priceScale": "0.06", "pnls": ["48.16388381", "31.81313064", "18.30672359"]},  
                                        {"priceScale": "0.08", "pnls": ["61.37503018", "44.54603289", "30.56641060"]},  
                                        {"priceScale": "0.1", "pnls": ["75.52147477", "58.34116026", "44.02244694"]}  
                                    ],  
                                    "sessionAvgPrice": "0",  
                                    "markPrice": "2608.56395729",  
                                    "orderSize": "0.0",  
                                    "contractType": 5,  
                                    "settleCoin": "USDT"  
                                }  
                            ]  
                        }  
                    ],  
                    "contingency": {  
                        "optionContingency": "0.00000000",  
                        "futureDeltaContingency": "56.89174177",  
                        "optionVegaContingency": "0.00000000",  
                        "contingencyComponents": "57.69544638",  
                        "usdtUsdcContingency": "0.00000000",  
                        "futureContingency": "0.80370460"  
                    },  
                    "asset": {  
                        "coin": "BTC",  
                        "assetIM": "1274.8190514137673",  
                        "assetMM": "1062.3492095114727"  
                    },  
                    "maxLossPriceMove": "-0.1",  
                    "maxLossIvShock": "-0.2",  
                    "totalClosePzFee": "-0.2",  
                    "spotHedgeInfo": {  
                        "hedgeSpotSize": "-0.00100006",  
                        "walletBalance": "-0.00000007",  
                        "usdIndexPrice": "0",  
                        "pnlRanges": [  
                            {"priceScale": "-0.1", "pnls": ["7.05047869"]},  
                            {"priceScale": "-0.08", "pnls": ["5.64038295"]},  
                            {"priceScale": "-0.06", "pnls": ["4.23028721"]},  
                            {"priceScale": "-0.04", "pnls": ["2.82019147"]},  
                            {"priceScale": "-0.02", "pnls": ["1.41009574"]},  
                            {"priceScale": "0.0", "pnls": ["0"]},  
                            {"priceScale": "0.02", "pnls": ["0"]},  
                            {"priceScale": "0.04", "pnls": ["0"]},  
                            {"priceScale": "0.06", "pnls": ["0"]},  
                            {"priceScale": "0.08", "pnls": ["0"]},  
                            {"priceScale": "0.1", "pnls": ["0"]}  
                        ]  
                    },  
                    "maxLossIvShockList": ["-0.2", "-0.2", "-0.2", "-0.2", "-0.2", "-0.2", "-0.2", "-0.2", "-0.2", "-0.2", "-0.2"]  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1774319290506  
    }