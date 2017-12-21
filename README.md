# About Satoshi

Satoshi is a [Discord](discord.gg) chat bot that returns cryptocurrency market data requests for coins on a variety of exchanges. Currently, the bot supports [Poloniex](https://poloniex.com), [Bittrex](https://bittrex.com), [Binance](https://www.binance.com/?ref=15552990) and the [CoinDesk BPI](https://www.coindesk.com/price/).

Satoshi is written in Python and uses the [discord.py](https://github.com/Rapptz/discord.py) library.

![sample](https://i.imgur.com/OeLKuHH.png)

# Add Satoshi to Your Server

To add Satoshi to your Discord server, simply [click here](https://discordapp.com/oauth2/authorize?client_id=315215494896680972&scope=bot&permissions=0). You can then grant the bot access to any server you have admin privileges in. 

# Usage

The most commonly used command is the quick lookup using the '$' prefix. To do this, simply type `$[coin ticker]` in a server that Satoshi is a member of, and it will return current market data for that coin. Up to three coins can be included anywhere in your message. Some examples: `$ETH`, `Wow, look at the price of $ETH`, `$ETH and $LTC have really been catching up to $BTC lately`. 

If a coin is on multiple exchanges, data will be returned from Bittrex. There are other commands that will allow you to specify parameters such as coin pair and exchange. For a complete list of commands, type `+help` in any server Satoshi is present in.
