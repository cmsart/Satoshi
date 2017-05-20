import discord
import asyncio
import poloniex
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
        cmd = words[0][1:]
        if cmd == "coin":
            try:
                pair = words[1].upper()
                exchange = words[2]
            except:
                await client.send_message(channel, "The `$coin` command must be formatted like this: `$coin <currency_pair> <exchange>`.\n\n For example: `$coin BTC_ETH poloniex`.")
                return

            response = cmdCoin(pair, exchange)

        if response:
            await client.send_message(channel, response)

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

client.run(sys.argv[1])