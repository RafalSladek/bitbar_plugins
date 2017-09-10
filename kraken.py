#!/usr/bin/python
# coding: utf8
import locale
import requests
from currency import Currency
from pair import Pair

locale.setlocale(locale.LC_ALL, 'de_DE.UTF-8')

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


def getUrl(parameters):
    return str("https://api.kraken.com/0/public/Ticker?pair=" + parameters)


def getParameters(all_pairs):
    pairs = []
    for (pair) in all_pairs:
        pairs.append(makePair(pair))

    return ','.join(pairs)


def makeResultPair(pair):
    if (pair.crypto.code == 'BCH'):
        return makePair(pair)
    else:
        return str('X' + pair.crypto.code + 'Z' + pair.fiat.code)


def makePair(pair):
    return str(pair.crypto.code + pair.fiat.code)


def getResponse(all_pairs):
    current_url = getUrl(getParameters(all_pairs))
    # print current_url
    data = requests.get(current_url).json()
    result = []
    for (pair) in all_pairs:
       # print data
        symbol = makeResultPair(pair)
        # print symbol
        result.append(formatPrice(
            data['result']['%s' % symbol]['c'][0], pair))
    return result


def formatPrice(unformatted_price, pair):
    price = locale.currency(float(unformatted_price),
                            symbol=False, grouping=True)
    result = [pair.crypto.symbol, price, pair.fiat.symbol]
    return str(" ".join(result))


def formatToBitBar(output):
    return str(output)


def getAllPrices(all_pairs):
    result = getResponse(all_pairs)
    for price in result:
        print formatToBitBar(price)


def run():

    list_of_tuples = []
    eth = Currency('ETH', '𝚵')
    euro = Currency('EUR', '€')
    btc = Currency('XBT', '₿')
    xmr = Currency('XMR', 'Ⓜ')
    zec = Currency('ZEC', 'ⓩ')
    ltc = Currency('LTC', 'Ł')
    bch = Currency('BCH', '฿')

    list_of_tuples.append(Pair(eth, euro))
    list_of_tuples.append(Pair(btc, euro))
    list_of_tuples.append(Pair(xmr, euro))
    list_of_tuples.append(Pair(zec, euro))
    list_of_tuples.append(Pair(ltc, euro))
    list_of_tuples.append(Pair(bch, euro))

    getAllPrices(list_of_tuples)


run()
