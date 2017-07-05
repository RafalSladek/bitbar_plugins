#!/bin/bash

# <bitbar.title>Kraken.com ETHEUR last price</bitbar.title>
# <bitbar.version>v1.0</bitbar.version>
# <bitbar.author>G.G.</bitbar.author>
# <bitbar.author.github>ggrelet</bitbar.author.github>
# <bitbar.desc>Gives the last price of ether to euro from Kraken.com</bitbar.desc>
# <bitbar.image>https://i.imgur.com/iGX2yjR.png</bitbar.image>
# <bitbar.dependencies>bash</bitbar.dependencies>

# <pair_name> = pair name
# a = ask array(<price>, <whole lot volume>, <lot volume>),
# b = bid array(<price>, <whole lot volume>, <lot volume>),
# c = last trade closed array(<price>, <lot volume>),
# v = volume array(<today>, <last 24 hours>),
# p = volume weighted average price array(<today>, <last 24 hours>),
# t = number of trades array(<today>, <last 24 hours>),
# l = low array(<today>, <last 24 hours>),
# h = high array(<today>, <last 24 hours>),
# o = today's opening price

ether=$(curl -s "https://api.kraken.com/0/public/Ticker?pair=ETHEUR" | tr -d '{}"[]' | tr ':,' '\n' | grep -A1 "^c$" | tail -1)

echo "$(printf "𝚵 %.3f \n" "$ether") | size=13"
echo "---"
echo "Kraken.com | href=\"https://www.kraken.com/\""
