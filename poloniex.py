import urllib.request, json

def getCurrencyPairs():
    return ["BTC_BCN", "BTC_BELA", "BTC_BLK", "BTC_BTCD", "BTC_BTM", "BTC_BTS", "BTC_BURST", "BTC_GNT", 
    "BTC_CLAM", "BTC_DASH", "BTC_DGB", "BTC_DOGE", "BTC_EMC2", "BTC_FLDC", "BTC_FLO", "BTC_GAME", "BTC_GRC", 
    "BTC_HUC", "BTC_LTC", "BTC_MAID", "BTC_OMNI", "BTC_NAUT", "BTC_NAV", "BTC_NEOS", "BTC_NMC", "BTC_NOTE", 
    "BTC_NXT", "BTC_PINK", "BTC_POT", "BTC_PPC", "BTC_RIC", "BTC_SJCX", "BTC_STR", "BTC_SYS", "BTC_VIA", 
    "BTC_XVC", "BTC_VRC", "BTC_VTC", "BTC_XBC", "BTC_XCP", "BTC_XEM", "BTC_XMR", "BTC_XPM", "BTC_XRP", "BTC_GNO",
    "BTC_ETH", "BTC_SC", "BTC_BCY", "BTC_EXP", "BTC_FCT", "BTC_RADS", "BTC_AMP", "BTC_DCR", "BTC_LSK", "BTC_LBC", 
    "BTC_STEEM", "BTC_SBD", "BTC_ETC", "BTC_REP", "BTC_ARDR", "BTC_ZEC", "BTC_STRAT", "BTC_NXC", "BTC_PASC"]

def getCurrencyPair(coin, coinPair):
    pairs = getCurrencyPairs()
    pair = coinPair + "_" + coin
    if pair in pairs:
        return pair

    return None

def getTickerData(pair):
    url = "https://poloniex.com/public?command=returnTicker"
    with urllib.request.urlopen(url) as url:
        ticker = json.loads(url.read().decode())
        return ticker[pair]

def getTickerMessage(ticker, coin):
    coin = "**COIN NAME (" + coin + ")**\n"
    seperator = "-----------------------\n"
    price = "Current Price: `" + ticker["last"] + "`\n"
    high = "24hr High: `" + ticker["high24hr"] + "`\n"
    low = "24hr Low: `" + ticker["low24hr"] + "`\n"
    volume = "24hr Volume: `" + ticker["baseVolume"] + "`\n"

    changeNum = round((float(ticker["percentChange"]) * 100), 2)
    sign = "+" if changeNum > 0 else ""
    change = "Percent Change: ```diff\n" + sign + str(changeNum) + "%\n```"

    message = coin + seperator + price + volume + high + low + change

    return message