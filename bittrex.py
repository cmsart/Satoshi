import urllib.request, json

def getCurrencyPairs():
    url = "https://bittrex.com/api/v1.1/public/getmarkets"
    pairs = []

    with urllib.request.urlopen(url) as url:
        data = json.loads(url.read().decode())
        coins = data["result"]
        for coin in coins:
            pairs.append(coin["BaseCurrency"] + "-" + coin["MarketCurrency"])

    return pairs        

def getReadableCoinName(coin):
    url = "https://bittrex.com/api/v1.1/public/getcurrencies"
    name = None

    with urllib.request.urlopen(url) as url:
        data = json.loads(url.read().decode())
        coins = data["result"]
        for trexCoin in coins:
            if trexCoin["Currency"] == coin:
                name = trexCoin["CurrencyLong"]

    return name

# Returns the currency pair for the given symbol
def getCurrencyPair(coin, coinPair = "BTC"):
    pairs = getCurrencyPairs()
    pair = coinPair + "-" + coin
    if pair in pairs:
        return pair
    else:
        return None

# Returns ticker data from Poloniex for the given currency pair
def getTickerData(pair):
    pair = pair.replace("_", "-")
    url = "https://bittrex.com/api/v1.1/public/getmarketsummary?market=" + pair
    pairs = getCurrencyPairs()

    if pair in pairs:
        with urllib.request.urlopen(url) as url:
            ticker = json.loads(url.read().decode())
            return ticker["result"]
    else:
        return None

def getTickerMessage(ticker):
    ticker = ticker[0]
    pair = ticker["MarketName"]
    coin = getReadableCoinName(pair.split("-")[1])
    header = "**" + coin + " (" + pair.replace("-", "_") + ") - Bittrex**\n"
    seperator = "-----------------------\n"
    price = "Current Price: `" + "{:.8f}".format(ticker["Last"]) + "`\n"
    high = "24hr High: `" + "{:.8f}".format(ticker["High"]) + "`\n"
    low = "24hr Low: `" + "{:.8f}".format(ticker["Low"]) + "`\n"
    volume = "24hr Volume: `" + "{:.8f}".format(ticker["BaseVolume"]) + "`\n"

    changeNum = round(((ticker["Last"] - ticker["PrevDay"]) / ticker["PrevDay"]) * 100, 2)
    sign = "+" if changeNum > 0 else ""
    change = "Percent Change: ```diff\n" + sign + str(changeNum) + "%\n```"

    message = header + seperator + price + volume + high + low + change

    return message