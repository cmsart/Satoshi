import urllib.request, json
import discord

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
    "REP": "Augur", "ARDR": "Ardor", "ZEC": "Zcash", "STRAT": "Stratis", "NXC": "Nexium", "PASC": "PascalCoin", "ZRX": "0x", "CVC": "Civic",
    "BCH": "Bitcoin Cash", "OMG": "OmiseGO", "GAS": "Gas", "STORJ": "Storj", "BTC": "Bitcoin"}

    return names[coin]

# Returns ticker data from Poloniex for the given currency pair
def getTickerData(pair):
    url = "https://poloniex.com/public?command=returnTicker"

    with urllib.request.urlopen(url) as url:
        ticker = json.loads(url.read().decode())
        if pair in ticker:
            return ticker[pair]

    return None

# Returns formatted market data for the bot to send
def getTickerMessage(ticker, pair):
    coin = getReadableCoinName(pair.split("_")[1])
    header = coin + " (" + pair + ") - Poloniex"
    price = "Current Price: `" + ticker["last"] + "`\n"
    high = "24hr High: `" + ticker["high24hr"] + "`\n"
    low = "24hr Low: `" + ticker["low24hr"] + "`\n"
    volume = "24hr Volume: `" + ticker["baseVolume"] + "`\n"

    changeNum = round((float(ticker["percentChange"]) * 100), 2)
    sign = "+" if changeNum > 0 else ""
    change = "Percent Change: ```diff\n" + sign + str(changeNum) + "%```"

    data = price + volume + high + low + change

    embed = discord.Embed(title = header, description = data, color = 0xFF9900)
    embed.set_footer(text = "For more information about Satoshi, type +help")

    return embed