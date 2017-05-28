import discord
import asyncio
import poloniex
import coindesk
import sys

client = discord.Client()
pairs = poloniex.getCurrencyPairs()

@client.event
async def on_ready():
    print('Satoshi Online!')
    print('---------------')
    # Include logging here    

@client.event
async def on_message(message):
    msg = message.content.lower()
    channel = message.channel
    words = msg.split()

    # Check if a possible command has been submitted
    if msg.startswith('+'):
        response = None
        cmd = words[0][1:]
        if cmd == "coin":
            try:
                pair = words[1].upper()
                exchange = words[2]
            except:
                await client.send_message(channel, "The `+coin` command must be formatted like this: `+coin <currency_pair> <exchange>`.\n\n For example: `+coin BTC_ETH poloniex`")
                return

            response = cmdCoin(pair, exchange)

        if cmd == "bitcoin":
            try:
                currency = words[1].upper()
            except:
                await client.send_message(channel, "The `+bitcoin` command must be formatted like this: `+bitcoin <currency>`.\n\n For example: `+bitcoin GBP`")
                return

            response = cmdBitcoin(currency)

        if cmd == "help":
            response = cmdHelp()

        if response:
            await client.send_message(channel, response)
        else:
            await client.send_message(channel, "`+" + cmd + "` is not a valid command. Type `+help` to get a list of valid commands.")

    # If no command, parse message for currency requests
    else:
        calls = 0
        for word in words:
            if calls >= 3:
                await client.send_message(channel, "You can only request data for up to 3 coins per message.")
                break
            if word.startswith("$"):
                coin = word[1:].upper()
                pair = poloniex.getCurrencyPair(coin)

                if coin == "BTC":
                    ticker = coindesk.getTickerData()
                    tickerMessage = coindesk.getTickerMessage(ticker)
                    await client.send_message(channel, tickerMessage)
                if pair:
                    ticker = poloniex.getTickerData(pair)
                    tickerMessage = poloniex.getTickerMessage(ticker, pair)
                    calls += 1
                    await client.send_message(channel, tickerMessage)                    

# Returns current market data for the specified currency pair and exchange
def cmdCoin(pair, exchange):
    if exchange == 'poloniex':
        ticker = poloniex.getTickerData(pair)
        if ticker:
            return poloniex.getTickerMessage(ticker, pair)
    
    return "The currency pair `" + pair + "` was not found on `" + exchange + "`. Please try again."

# Returns current market data for bitcoin
def cmdBitcoin(currency):
    ticker = coindesk.getTickerData(currency)
    if isinstance(ticker, dict):
        return coindesk.getTickerMessage(ticker)
    else:
        return ticker

# Returns help message
def cmdHelp():
    intro = "Thank you for using Satoshi! This bot provides real time market data for cryptocurrencies on multiple exchanges.\n\n"
    exchanges = "__**Supported Exchanges**__\n\nThe current supported exchanges are: `Poloniex`\n\n"
    commands = "__**Commands**__\n\n"
    cmdCoin = "`+coin <currency pair> <exchange>` - Returns market data for the specified coin/exchange.\nExample: `+coin BTC_LTC Poloniex`\n\n"
    cmdBitcoin = "`+bitcoin <currency>` - Returns current bitcoin price for the specified currency.\nExample: `+bitcoin GBP`\n\n"
    cmdHelp = "`+help` - Returns information about Satoshi\n\n"
    lookup = """You may also retrieve data for up to three coins by simply including `$coin` anywhere in your message. 
If a coin is present on mutiple exchanges, data will be returned from Poloniex. If you wish to specify the exchange, use the `+coin` command. 
Example: `Wow, look at $ETC!`\n\n"""
    github = "__**Github**__\n\nThis project can be found on Github at `https://github.com/cmsart/Satoshi`"

    return intro + exchanges + commands + cmdCoin + cmdBitcoin + cmdHelp + lookup.replace("\t", "") + github

client.run(sys.argv[1])
