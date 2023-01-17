import os 
os.system("pip install requests")
os.system("pip install colorama")
os.system("pip install argparse")


import requests
import argparse

import colorama
from colorama import Back,Fore,Style
colorama.init()


parser = argparse.ArgumentParser()
parser.add_argument('-u','--url',required=True,help='Enter target url')
parser.add_argument('-w','--wordlist',type=(str),required=True,help='Enter your wordlist')
args = parser.parse_args()

# Colors
HEADER = '\033[95m'
BLUE = '\033[94m'
GREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

url = args.url
wordlist = args.wordlist
if(wordlist.__contains__(".txt")):
    file = open(wordlist, mode = 'r', encoding = 'utf-8-sig')
    lines = file.readlines()
    for i in lines:
            req = requests.get(url+i)
            status = req.status_code
            if (status == 404):
                pass
            if (status == 403):
                print(f"{Fore.RED}{status}"+f"{Fore.BLUE}{url+i}")
            if (status == 401):
                print(f"{Fore.RED}{status}"+f"{Fore.BLUE}{url+i}")
            else:
                print(f"{Fore.GREEN}{status}"+f"{Fore.BLUE}{url+i}")


    
else:
    req = requests.get(url+wordlist)
    status = req.status_code
    if (status == 404):
        pass
    if (status == 403):
        print("["+f"{Fore.RED}-"+f"{Fore.WHITE}]",f"{Fore.RED}{status}",f"{Fore.BLUE}{url+wordlist}")
    if (status == 401):
        print("["+f"{Fore.RED}-"+f"{Fore.WHITE}]",f"{Fore.RED}{status}",f"{Fore.BLUE}{url+wordlist}")
    else:
        print("["+f"{Fore.GREEN}+"+f"{Fore.WHITE}]",f"{Fore.GREEN}{status}",f"{Fore.BLUE}{url+wordlist}")
    pass
