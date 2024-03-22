import time

from config import *
from rpc import *
import random

QPS = 10


def query_balance_eth(eth_rpc, address):
    balance = eth_get_balance(eth_rpc, address)
    if balance is not None:
        print("币圈科学家旺仔出品")
        print("通过lava-RPC {} \n 查询账户{} 余额为 {} eth".format(eth_rpc, address, balance))
    else:
        print("调用lava-RPC {} 失败，请确认你的RPC地址".format(eth_rpc))


def main():
    if "ETH" not in RPC or "Mainnet" not in RPC["ETH"]:
        print("缺少lava的ETH-RPC-Endpoint，请先配置你的地址")
        exit(1)
    print("======开始运行lava-rpc脚本======")
    print("币圈科学家旺仔出品")
    print("微信btc9767")
    while True:
        r = random.randint(0, len(AddressSet)-1) % len(AddressSet)
        address = AddressSet[r]
        query_balance_eth(RPC["ETH"]["Mainnet"], address)
        time.sleep(1 / QPS)


if __name__ == '__main__':
    main()
