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
    msg = message.content
    words = msg.split()
    calls = 0
    for word in words:
        if calls >= 3:
            await client.send_message(message.channel, "You can only request data for up to 3 coins per message")
            break
        if word.startswith("$"):
            coin = word[1:]
            pair = poloniex.getCurrencyPair(coin, "BTC")
            if pair:
                ticker = poloniex.getTickerData(pair)
                tickerMessage = poloniex.getTickerMessage(ticker, coin)
                await client.send_message(message.channel, tickerMessage)
                calls += 1

client.run(sys.argv[1])