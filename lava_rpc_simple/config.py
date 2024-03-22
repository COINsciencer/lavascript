import configparser
import json

RPC = configparser.ConfigParser()
RPC.read("conf/lava.ini")

with open("conf/address_pool.txt", "r") as file:
    AddressSet = [row.strip() for row in file]
    print("加载地址池成功，地址池中共有 {} 个地址".format(len(AddressSet)))
