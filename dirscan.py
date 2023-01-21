import requests
import argparse
import colorama
import sys
from colorama import Back,Fore,Style
colorama.init()
parser = argparse.ArgumentParser()
parser.add_argument('-u','--url',required=True,help='Enter target url')
parser.add_argument('-w','--wordlist',type=(str),required=True,help='Enter your wordlist')
args = parser.parse_args()
url = args.url
wordlist = args.wordlist
file = open(wordlist,'r')
for i in file.readlines():
        req = requests.get(url+i)
        if (req.status_code == 404):
            print(f"{Fore.BLACK}[{req.status_code}]"+f"{Fore.BLUE}{url+i}")
        if (req.status_code == 403):
            print(f"{Fore.RED}[{req.status_code}]"+f"{Fore.BLUE}{url+i}")
        if (req.status_code == 401):
            print(f"{Fore.RED}[{req.status_code}]"+f"{Fore.BLUE}{url+i}")
        if(req.status_code == 200):
            print(f"{Fore.GREEN}[{req.status_code}]"+f"{Fore.BLUE}{url+i}")
