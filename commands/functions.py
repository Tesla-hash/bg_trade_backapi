from bithumb_api.BithumbGlobal import *
import json
import requests


def get_balance():
    user_url = requests.get('http://45.90.34.67:5000/user')
    api_key = user_url.json()[0]
    api_secret = user_url.json()[1]
    bithumb = BithumbGlobalRestAPI(api_key,api_secret)
    balance_btc = round(float(bithumb.balance('BTC')[0]['count']),4)
    balance_btc_frozen = round(float(bithumb.balance('BTC')[0]['frozen']),4)
    balance_eth = round(float(bithumb.balance('ETH')[0]['count']),4)
    balance_eth_frozen = round(float(bithumb.balance('ETH')[0]['frozen']),4)
    balance_usdt = round(float(bithumb.balance('USDT')[0]['count']),4)
    balance_usdt_frozen = round(float(bithumb.balance('USDT')[0]['frozen']),4)
    balance_bip = round(float(bithumb.balance('BIP')[0]['count']),4)
    balance_bip_frozen = round(float(bithumb.balance('BIP')[0]['frozen']),4)

    return (balance_btc, balance_btc_frozen, balance_eth, balance_eth_frozen, balance_usdt, balance_usdt_frozen, balance_bip, balance_bip_frozen)

def get_orders(symbol):
    user_url = requests.get('http://45.90.34.67:5000/user')
    api_key = user_url.json()[0]
    api_secret = user_url.json()[1]
    bithumb = BithumbGlobalRestAPI(api_key,api_secret)
    orders = bithumb.openning_orders(symbol)

    return orders

def get_order_detail(id):
    user_url = requests.get('http://45.90.34.67:5000/user')
    api_key = user_url.json()[0]
    api_secret = user_url.json()[1]
    bithumb = BithumbGlobalRestAPI(api_key,api_secret)
    order_detail = bithumb.query_order('BIP/USDT', id)

    return order_detail


def cancel_order(id):
    user_url = requests.get('http://45.90.34.67:5000/user')
    api_key = user_url.json()[0]
    api_secret = user_url.json()[1]
    bithumb = BithumbGlobalRestAPI(api_key,api_secret)
    bithumb.cancel_order('BIP/USDT',id)

def get_all_orders(symbol):
    orders_list = []
    user_url = requests.get('http://45.90.34.67:5000/user')
    api_key = user_url.json()[0]
    api_secret = user_url.json()[1]
    bithumb = BithumbGlobalRestAPI(api_key,api_secret)
    orders = bithumb.openning_orders(symbol)

    for x in orders:
        order_detail = bithumb.query_order('BIP/USDT', x)
        orders_list.append(order_detail)
    return orders_list


def get_history_orders():
    orders_list = []
    user_url = requests.get('http://45.90.34.67:5000/user')
    api_key = user_url.json()[0]
    api_secret = user_url.json()[1]
    bithumb = BithumbGlobalRestAPI(api_key,api_secret)
    orders = bithumb.orders('buy','BIP-USDT','trading')

    return orders

    #for i in orders:
