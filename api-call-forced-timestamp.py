import time
import os.path
import io
import urllib
import json
import csv
import datetime
from time import localtime

window = 3
now = datetime.datetime.now().strftime("%Y%m%d%H") # current day
file_exists = os.path.isfile(now+'.csv') # file_name exists check
#timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S") # current timestamp
timestamp = datetime.datetime.now()
timestamp = timestamp.replace(second = 1)

with open(now+'.csv', 'a') as f:
        fieldnames = ['traded_at', 'open', 'high', 'low', 'close'] # column name
        writer = csv.DictWriter(f, fieldnames = fieldnames, delimiter = ',', lineterminator='\n')
        if not file_exists: # file doesn't exists, write header and data if the file already exists,(header exists) do not write again
                writer.writeheader()
        for i in range(3600, 0, -3):
                start_time = time.time()
                url = 'https://api.bithumb.com/public/ticker/BTC' # api url

                request_url = url

                u = urllib.urlopen(request_url)
                data = u.read()

                j = json.loads(data) # data fetch

                open_p = j['data']['opening_price']
                high_p = j['data']['max_price']
                low_p = j['data']['min_price']
                closed_p = j['data']['closing_price']

                writer.writerow({'traded_at' : timestamp.strftime("%Y%m%d%H%M%S"), 'open' : open_p, 'high' : high_p, 'low' : low_p, 'close' : closed_p}) # write data (append)
                end_time = time.time()
                elapsed_time = end_time - start_time
                timestamp = timestamp + datetime.timedelta(seconds=3)
                if elapsed_time < window:
                        time.sleep(window-elapsed_time)

EXPORT204 = "gsutil -m cp /home/Tora/"+now+".csv gs://gcpkr-bitcoin-keras/preprocess" # copy the file to gcs bucket
EXPORT205 = "mv "+now+".csv 201711_1h"

os.system(EXPORT204) # execute EXPORT204
os.system(EXPORT205)
