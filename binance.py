import requests
import discord

# Returns ticker data from Binance for the given currency pair
def getTickerData(pair):
    pairsplit = pair.split("_")
    pair = pairsplit[1] + pairsplit[0]
    url = "https://api.binance.com/api/v1/ticker/24hr?symbol=" + pair

    ticker = requests.get(url)
    if ticker.status_code == 200:
        return ticker.json()

    return None

# Returns formatted market data for the bot to send
def getTickerMessage(ticker, pair):
    header = "(" + pair + ") - Binance"
    price = "Current Price: `" + ticker["lastPrice"] + "`\n"
    high = "24hr High: `" + ticker["highPrice"] + "`\n"
    low = "24hr Low: `" + ticker["lowPrice"] + "`\n"
    volume = "24hr Volume: `" + ticker["quoteVolume"] + "`\n"

    changeNum = float(ticker["priceChangePercent"])
    sign = "+" if changeNum > 0 else ""
    change = "Percent Change: ```diff\n" + sign + "{:.2f}".format(changeNum) + "%```"

    data = price + volume + high + low + change

    embed = discord.Embed(title = header, description = data, color = 0xFF9900)
    embed.set_footer(text = "For more information about Satoshi, type +help")

    return embed