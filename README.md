# About Satoshi

Satoshi is a [Discord](discord.gg) chat bot that returns cryptocurrency market data requests for coins on a variety of exchanges. Currently, the bot supports [Poloniex](https://poloniex.com), [Bittrex](https://bittrex.com), and the [CoinDesk BPI](https://www.coindesk.com/price/). There are plans to add more exchanges in the future. 

Satoshi is written in Python and uses the [discord.py](https://github.com/Rapptz/discord.py) library.

# Add Satoshi to Your Server

To add Satoshi to your Discord server, simply [click here](https://discordapp.com/oauth2/authorize?client_id=315215494896680972&scope=bot&permissions=0). You can then grant the bot access to any server you have admin privileges in. 

# Usage

The most commonly used command is the quick lookup using the '$' prefix. To do this, simply type `$[coin ticker]` in a server that Satoshi is a member of, and it will return current market data for that coin. Up to three coins can be included anywhere in your message. Some examples: `$ETH`, `Wow, look at the price of $ETH`, `$ETH and $LTC have really been catching up to $BTC lately`. 

If a coin is on both Poloniex and Bittrex, data will be returned from Poloniex. There are other commands that will allow you to specify parameters such as coin pair and exchange. For a complete list of commands, type `+help` in any server Satoshi is present in.

# Running Locally

Satoshi is written in Python 3, and will not work with any verisons of Python 2. To run your own instance of Satoshi, clone this repository and install [discord.py](https://github.com/Rapptz/discord.py) (instructions for this are in the discord.py readme). To run the bot, you will need a Discord bot application linked to your account. You can create one [here](https://discordapp.com/developers/applications/me). Once you have a bot user created, you can use its token to run the bot. The token is currently taken in as a command line argument when starting the application. To start the bot, navigate to the project's root directory and run `python3 satoshi.py [your bot's token]` (without the brackets). 
