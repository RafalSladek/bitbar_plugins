#!/bin/bash

# <bitbar.title>Kraken.com XBTEUR last price</bitbar.title>
# <bitbar.version>v1.0</bitbar.version>
# <bitbar.author>R.S.</bitbar.author>
# <bitbar.author.github>rafalsladek</bitbar.author.github>
# <bitbar.desc>Gives the last price of bitcoin to euro from Kraken.com</bitbar.desc>
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

bitcoin=$(curl -s "https://api.kraken.com/0/public/Ticker?pair=XBTEUR" | tr -d '{}"[]' | tr ':,' '\n' | grep -A1 "^c$" | tail -1)
ether=$(curl -s "https://api.kraken.com/0/public/Ticker?pair=ETHEUR" | tr -d '{}"[]' | tr ':,' '\n' | grep -A1 "^c$" | tail -1)
xmr=$(curl -s "https://api.kraken.com/0/public/Ticker?pair=XMREUR" | tr -d '{}"[]' | tr ':,' '\n' | grep -A1 "^c$" | tail -1)
zcash=$(curl -s "https://api.kraken.com/0/public/Ticker?pair=ZECEUR" | tr -d '{}"[]' | tr ':,' '\n' | grep -A1 "^c$" | tail -1)

echo "$(printf "𝚵 %.2f €\n" "$ether") | size=13"
echo "$(printf "₿ %.2f €\n" "$bitcoin") | size=13"
echo "$(printf "Ⓜ %.2f €\n" "$xmr") | size=13"
echo "$(printf "ⓩ %.2f €\n" "$zcash") | size=13"
echo "---"
echo "Kraken.com | href=\"https://www.kraken.com/\""
