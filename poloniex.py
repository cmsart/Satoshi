import urllib.request, json

# Returns all Poloniex currency pairs
def getCurrencyPairs():
    btc = ["BTC_BCN", "BTC_BELA", "BTC_BLK", "BTC_BTCD", "BTC_BTM", "BTC_BTS", "BTC_BURST", "BTC_GNT", 
    "BTC_CLAM", "BTC_DASH", "BTC_DGB", "BTC_DOGE", "BTC_EMC2", "BTC_FLDC", "BTC_FLO", "BTC_GAME", "BTC_GRC", 
    "BTC_HUC", "BTC_LTC", "BTC_MAID", "BTC_OMNI", "BTC_NAUT", "BTC_NAV", "BTC_NEOS", "BTC_NMC", "BTC_NOTE", 
    "BTC_NXT", "BTC_PINK", "BTC_POT", "BTC_PPC", "BTC_RIC", "BTC_SJCX", "BTC_STR", "BTC_SYS", "BTC_VIA", 
    "BTC_XVC", "BTC_VRC", "BTC_VTC", "BTC_XBC", "BTC_XCP", "BTC_XEM", "BTC_XMR", "BTC_XPM", "BTC_XRP", "BTC_GNO",
    "BTC_ETH", "BTC_SC", "BTC_BCY", "BTC_EXP", "BTC_FCT", "BTC_RADS", "BTC_AMP", "BTC_DCR", "BTC_LSK", "BTC_LBC", 
    "BTC_STEEM", "BTC_SBD", "BTC_ETC", "BTC_REP", "BTC_ARDR", "BTC_ZEC", "BTC_STRAT", "BTC_NXC", "BTC_PASC"]

    #TODO - Add other currency pairs
    eth = []
    xmr = []
    usdt = []

    return btc + eth + xmr + usdt

# Returns the coin name for the given symbol
def getReadableCoinName(coin):
    names = {"BCN": "Bytecoin", "BELA": "Belacoin", "BLK": "BlackCoin", "BTCD": "BitcoinDark", "BTM": "Bitmark", "BTS": "BitShares", 
    "BURST": "Burst", "GNT": "Golem", "CLAM": "CLAMS", "DASH": "Dash", "DGB": "DigiByte", "DOGE": "Dogecoin", "EMC2": "Einsteinium", 
    "FLDC": "FoldingCoin", "FLO": "Florincoin", "GAME": "GameCredits", "GRC": "Gridcoin Research", "HUC": "Huntercoin", 
    "LTC": "Litecoin", "MAID": "MaidSafeCoin", "OMNI": "Omni", "NAUT": "Nautiluscoin", "NAV": "NAVCoin", "NEOS": "Neoscoin", 
    "NMC": "Namecoin", "NOTE": "DNotes", "NXT": "NXT", "PINK": "Pinkcoin", "POT": "PotCoin", "PPC": "Peercoin", "RIC": "Riecoin", 
    "SJCX": "Storjcoin X", "STR": "Stellar", "SYS": "Syscoin", "VIA": "Viacoin", "XVC": "Vcash", "VRC": "VeriCoin", "VTC": "Vertcoin",
    "XBC": "BitcoinPlus", "XCP": "Counterparty", "XEM": "NEM", "XMR": "Monero", "XPM": "Primecion", "XRP": "Ripple", "GNO": "Gnosis",
    "ETH": "Ethereum", "SC": "Siacoin", "BCY": "BitCrystals", "EXP": "Expanse", "FCT": "Factom", "RADS": "Radium", "AMP": "Synereo AMP",
    "DCR": "Decred", "LSK": "Lisk", "LBC": "LBRY Credits", "STEEM": "STEEM", "SBD": "Steem Dollars", "ETC": "Ethereum Classic",
    "REP": "Augur", "ARDR": "Ardor", "ZEC": "Zcash", "STRAT": "Stratis", "NXC": "Nexium", "PASC": "PascalCoin"}

    return names[coin]

# Returns the currency pair for the given symbol
def getCurrencyPair(coin, coinPair = None):
    if coinPair is None:
        coinPair = "BTC"
    pairs = getCurrencyPairs()
    pair = coinPair + "_" + coin
    if pair in pairs:
        return pair
    else:
        return None

# Returns ticker data from Poloniex for the given currency pair
def getTickerData(pair):
    url = "https://poloniex.com/public?command=returnTicker"
    pairs = getCurrencyPairs()

    if pair in pairs:
        with urllib.request.urlopen(url) as url:
            ticker = json.loads(url.read().decode())
            return ticker[pair]
    else:
        return None

# Returns formatted market data for bot to send
# TODO - Attempt to implement using discord.ext formatter
def getTickerMessage(ticker, pair):
    coin = getReadableCoinName(pair.split("_")[1])
    header = "**" + coin + " (" + pair + ") - Poloniex**\n"
    seperator = "-----------------------\n"
    price = "Current Price: `" + ticker["last"] + "`\n"
    high = "24hr High: `" + ticker["high24hr"] + "`\n"
    low = "24hr Low: `" + ticker["low24hr"] + "`\n"
    volume = "24hr Volume: `" + ticker["baseVolume"] + "`\n"

    changeNum = round((float(ticker["percentChange"]) * 100), 2)
    sign = "+" if changeNum > 0 else ""
    change = "Percent Change: ```diff\n" + sign + str(changeNum) + "%\n```"

    message = header + seperator + price + volume + high + low + change

    return message