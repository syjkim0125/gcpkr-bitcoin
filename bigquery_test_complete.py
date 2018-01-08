import threading
import time
import os.path
import io
import urllib
import json
import csv
import datetime
from time import localtime
from pprint import pprint
from google.cloud import bigquery

count = 1

def stream_data(dataset_id, table_id, time_stamp, open_p, high_p, low_p, closed_p):

    global timestamp, count

    bigquery_client = bigquery.Client()
    dataset_ref = bigquery_client.dataset(dataset_id)
    table_ref = dataset_ref.table(table_id)

    # Get the table from the API so that the schema is available.
    table = bigquery_client.get_table(table_ref)
    while True:
        try:
            rows = [{'traded_at' : time_stamp.strftime("%Y%m%d%H%M%S"), 'open' : open_p, 'high' : high_p, 'low' : low_p, 'close' : closed_p}]
        except:
            continue
        break

    timestamp = timestamp + datetime.timedelta(seconds=3)
    errors = bigquery_client.create_rows(table, rows)

    if not errors:
        print('Loaded 1 row into {}:{}'.format(dataset_id, table_id))
        print(count)
        count+=1
    else:
        print('Errors:')
        pprint(errors)


def main():
        print("### STARTING... ###")
        time()
        checkCoin('https://api.bithumb.com/public/ticker/BTC')

def time():
        global timestamp
        timestamp = datetime.datetime.now()
        timestamp = timestamp.replace(second = 1)

def checkCoin(url):
        threading.Timer(3, checkCoin, [url]).start()

        try:
                data = urllib.urlopen(url).read(2000) # number of chars that should catch the announcement

                j = json.loads(data) # data fetch

                open_p = j['data']['opening_price']
                high_p = j['data']['max_price']
                low_p = j['data']['min_price']
                closed_p = j['data']['closing_price']

                stream_data("test_de", "thread_forced", timestamp, open_p, high_p, low_p, closed_p)
        except:
                while True:
                        try:
                                stream_data("test_de", "thread_forced", timestamp, open_p, high_p, low_p, closed_p)
                        except:
                                continue
                        break

main()
