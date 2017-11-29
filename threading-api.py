import threading
import time
import os.path
import io
import urllib
import json
import csv
import datetime
from time import localtime, strftime, strptime

now = datetime.datetime.now().strftime("%Y%m%d%H") # current day
file_exists = os.path.isfile(now+'.csv') # file_name exists check

window = 3

def main():

        print("### STARTING... ###")

        with open(now+'.csv', 'a') as f:
                fieldnames = ['traded_at', 'open', 'high', 'low', 'close'] # column name
                writer = csv.DictWriter(f, fieldnames = fieldnames)
                if not file_exists: # file doesn't exists, write header and data if the file already exists,(header exists) do not write again
                        writer.writeheader()
        checkCoin('https://api.bithumb.com/public/ticker/BTC')

def checkCoin(url):
        start_time = time.time()
        threading.Timer(3, checkCoin, [url]).start()
        data = urllib.urlopen(url).read(2000) # number of chars that should catch the announcement

        print("########### http data ############")
#print(data)
        j = json.loads(data) # data fetch
        timestamp = j['data']['date'] # current timestamp
        open_p = j['data']['opening_price']
        high_p = j['data']['max_price']
        low_p = j['data']['min_price']
        closed_p = j['data']['closing_price']
        timestamp = datetime.datetime.fromtimestamp(int(timestamp)/1000).strftime('%Y%m%d%H%M%S')

        main().writer.writerow({'traded_at' : timestamp, 'open' : open_p, 'high' : high_p, 'low' : low_p, 'close' : closed_p}) # write data (append)

        end_time = time.time()
        sleep_time = end_time - start_time
        if sleep_time < window:
                time.sleep(window-sleep_time)

main()
