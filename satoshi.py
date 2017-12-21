import discord
import asyncio
import poloniex
import bittrex
import coindesk
import sys
from os.path import expanduser

client = discord.Client()

@client.event
async def on_ready():
    print('Satoshi Online!')
    print('---------------')
    # Include logging here
    file = open(expanduser("~/server_log.txt"), "w") 
    serverCount = 0
    for server in client.servers:
        file.write(server.name + "\n")
        serverCount += 1
    file.write("\nConnected to " + str(serverCount) + " servers.")
    file.close()

@client.event
async def on_message(message):
    msg = message.content.lower()
    channel = message.channel
    words = msg.split()

    # Don't parse message if sent via PM or by the bot itself
    if message.author == client.user or isinstance(message.channel, discord.PrivateChannel):
        return

    # Check if a possible command has been submitted
    if msg.startswith('+'):
        response = None
        cmd = words[0][1:]
        if cmd == "coin":
            try:
                pair = words[1].upper()
                exchange = words[2]
            except:
                err = fmtError("The `+coin` command must be formatted like this: `+coin <currency_pair> <exchange>`\n\n Example: `+coin BTC_ETH poloniex`")
                await client.send_message(channel, embed = err)
                return

            response = cmdCoin(pair, exchange)

        if cmd == "bitcoin":
            try:
                currency = words[1].upper()
            except:
                err = fmtError("The `+bitcoin` command must be formatted like this: `+bitcoin <currency>`.\n\n Example: `+bitcoin GBP`")
                await client.send_message(channel, embed = err)
                return

            response = cmdBitcoin(currency)

        if cmd == "help":
            response = cmdHelp()
            channel = message.author

        if response:
            await client.send_message(channel, embed = response)

    # If no command, parse message for currency requests
    else:
        calls = 0
        for word in words:
            if calls >= 3:
                err = fmtError("You can only request data for up to 3 coins per message.")
                await client.send_message(channel, embed = err)
                break
            if word.startswith("$"):
                coin = word[1:].upper()
                tickerMessage = findCoin(coin)
                if tickerMessage:
                    calls += 1
                    await client.send_message(channel, embed = tickerMessage)                    

# Returns current market data for the specified currency pair and exchange
def cmdCoin(pair, exchange):
    if exchange == 'poloniex':
        ticker = poloniex.getTickerData(pair)
        if ticker:
            return poloniex.getTickerMessage(ticker, pair)
    elif exchange == 'bittrex':
        ticker = bittrex.getTickerData(pair)
        if ticker:
            return bittrex.getTickerMessage(ticker)

    return fmtError("The currency pair `" + pair + "` was not found on the exchange `" + exchange + "`. Please try again.")

# Returns current market data for bitcoin
def cmdBitcoin(currency):
    ticker = coindesk.getTickerData(currency)
    if isinstance(ticker, dict):
        return coindesk.getTickerMessage(ticker)
    else:
        return fmtError("`" + currency + "` is not a valid or supported currency.")

# Returns help message
def cmdHelp():
    intro = "Thank you for using Satoshi! This bot provides real time market data for cryptocurrencies on multiple exchanges.\n\n"
    embed = discord.Embed(title = "Bot Information", description = intro, color = 0xFF9900)

    exchanges = "The currently supported exchanges are: `Poloniex`, `Bittrex`\n\n"
    embed.add_field(name = "Supported Exchanges", value = exchanges)

    cmdCoin = "`+coin <currency pair> <exchange>` - Returns market data for the specified coin/exchange.\n\n\t- Example: `+coin BTC_LTC Poloniex`\n\n"
    cmdBitcoin = "`+bitcoin <currency>` - Returns current bitcoin price for the specified currency.\n\n\t- Example: `+bitcoin GBP`\n\n"
    cmdHelp = "`+help` - Returns information about Satoshi.\n\n"
    embed.add_field(name = "Commands", value = cmdCoin + cmdBitcoin + cmdHelp)

    lookup = """You may also retrieve data for up to three coins by simply including `$coin` anywhere in your message.\n 
If a coin is present on mutiple exchanges, data will be returned from Bittrex. If you wish to specify the exchange, use the `+coin` command.\n 
    - Example: `Wow, look at $ETC`\n\n"""
    embed.add_field(name = "Quick Lookup", value = lookup)

    github = "This project can be found on Github at `https://github.com/cmsart/Satoshi`"
    embed.add_field(name = "Github", value = github)    

    return embed

# Finds coin for $coin command
def findCoin(coin):
    if coin == "BTC":
        ticker = coindesk.getTickerData("USD")
        return coindesk.getTickerMessage(ticker)

    # Default to Bittrex
    pair = "BTC_" + coin
    ticker = bittrex.getTickerData(pair)
    if ticker:
        return bittrex.getTickerMessage(ticker)

    # Check Poloniex if not found
    ticker = poloniex.getTickerData(pair)
    if ticker:
        return poloniex.getTickerMessage(ticker, pair)

    return None

# Formats error messages from string to embed
def fmtError(error):
    embed = discord.Embed(title = "There was an error", description = error, color = 0xFF9900)
    embed.set_footer(text = "For more information about Satoshi, type +help")

    return embed

client.run(sys.argv[1])
