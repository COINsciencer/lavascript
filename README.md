

更多最新项目免费脚本关注 

币圈科学家旺仔

youtube
https://www.youtube.com/channel/UCX3J_A7EG437G8X857fBZfQ

twitter
https://twitter.com/howbuybtc

LAVA刷RPC教程
注册lava：https://points.lavanet.xyz/profile
注册地址： https://points.lavanet.xyz/register?code=1WHAW
注册码：1WHAW
安装Python3环境
Windows系统：python安装教程（Windows系统，python3.10.1版本为例，适用所有python3.X版本）_python3.10.1下载-CSDN博客
Linux系统：在Linux上安装Python 3 — The Hitchhiker’s Guide to Python
Mac系统：在Mac OS X上安装Python 3 — The Hitchhiker’s Guide to Python
下载LAVA-RPC脚本代码到本地
将lava_rpc包放置在一个文件夹下，如果你是windows，可以直接放在D盘下，后续操作会用到。
进入该文件夹，安装程序执行所需环境
Windows系统：运行powershell，依次执行以下指令
PowerShell
复制代码
1
2
3
4
# 1. 通过power_shell进入到lava_rpc文件夹：
cd d:\lava_rpc_simple
# 2. 安装脚本需要的环境
pip3 install -r requirement.txt
Linux系统
Shell
复制代码
1
2
3
4
# 1. 进入目录
cd ${you_lava_rpc_path}
# 2. 安装包
pip3 install -r requirement.txt
Mac系统
Shell
复制代码
1
2
3
4
# 1. 进入目录
cd ${you_lava_rpc_path}
# 2. 安装包
pip3 install -r requirement.txt
利用脚本编辑更改文件conf/lava.ini，将URL更改为你自己的lava-RPC链接
Properties
复制代码
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
[ETH]
Mainnet = https://eth1.lava.build/lava-referer-6661cbc8-1e41-49d6-8748-7ddaf8f640df/

[NEAR]
Mainnet = https://near.lava.build/lava-referer-6661cbc8-1e41-49d6-8748-7ddaf8f640df/
Testnet = https://near-testnet.lava.build/lava-referer-6661cbc8-1e41-49d6-8748-7ddaf8f640df/

[STRK]
Mainnet = https://rpc.starknet.lava.build/lava-referer-6661cbc8-1e41-49d6-8748-7ddaf8f640df/
Testnet = https://rpc.starknet-testnet.lava.build/lava-referer-6661cbc8-1e41-49d6-8748-7ddaf8f640df/

[AXELAR]
Mainnet = https://tm.axelar.lava.build/lava-referer-6661cbc8-1e41-49d6-8748-7ddaf8f640df/
Testnet = https://tm.axelar-testnet.lava.build/lava-referer-6661cbc8-1e41-49d6-8748-7ddaf8f640df/
MainnetLCD = https://rest.axelar.lava.build/lava-referer-6661cbc8-1e41-49d6-8748-7ddaf8f640df/
TestnetLCD = https://rest.axelar-testnet.lava.build/lava-referer-6661cbc8-1e41-49d6-8748-7ddaf8f640df/


运行脚本
window:  基于powershell，在lava_rpc_simple根目录下，运行python3 main.py
linux/mac：在lava_rpc_simple根目录下，运行python3 main.py

