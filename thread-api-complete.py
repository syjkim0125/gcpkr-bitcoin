import threading
import time
import os.path
import io
import urllib
import json
import csv
import datetime
from time import localtime, strftime, strptime

now = '0'
timestamp = datetime.datetime.now()
def main():

        print("### STARTING... ###")
        #time()
        checkCoin('https://api.bithumb.com/public/ticker/BTC')
'''
def time():
        global timestamp

        timestamp = timestamp.replace(second = 1)
        print(timestamp)
        #threading.Timer(3, time).start()
'''
def checkCoin(url):
        threading.Timer(3, checkCoin, [url]).start()

        global writer, timestamp

        now = datetime.datetime.now().strftime("%Y%m%d%H") # current day

        file_exists = os.path.isfile(now+'.csv') # file_name exists check

        with open(now+'.csv', 'a') as f:
                fieldnames = ['traded_at', 'open', 'high', 'low', 'close'] # column name

                timestamp = timestamp + datetime.timedelta(seconds=3)

                writer = csv.DictWriter(f, fieldnames = fieldnames)
                if not file_exists: # file doesn't exists, write header and data if the file already exists,(header exists) do not write again
                        writer.writeheader()
                        timestamp = timestamp.replace(second = 1)
                print(timestamp)
                try:
                        trigger = 0
                        data = urllib.urlopen(url).read(2000) # number of chars that should catch the announcement

                        print("########### http data ############")
                        j = json.loads(data) # data fetch

                        open_p = j['data']['opening_price']
                        high_p = j['data']['max_price']
                        low_p = j['data']['min_price']
                        closed_p = j['data']['closing_price']
                        writer.writerow({'traded_at' : timestamp.strftime("%Y%m%d%H%M%S"), 'open' : open_p, 'high' : high_p, 'low' : low_p, 'close' : closed_p}) # write data (append)

                except:
                        while True:
                                try:
                                        writer.writerow({'traded_at' : timestamp.strftime("%Y%m%d%H%M%S"), 'open' : open_p, 'high' : high_p, 'low' : low_p, 'close' : closed_p}) # write data (append)
                                except:
                                        continue
                                break

main()
'''
EXPORT204 = "gsutil -m cp /home/Tora/"+now+".csv gs://gcpkr-bitcoin-keras/preprocess" # copy the file to gcs bucket
EXPORT205 = "mv "+now+".csv 201711_1h"

os.system(EXPORT204) # execute EXPORT204
os.system(EXPORT205)
'''
