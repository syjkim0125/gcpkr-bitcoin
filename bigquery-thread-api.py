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


def stream_data(dataset_id, table_id, time_stamp, open_p, high_p, low_p, closed_p):

    bigquery_client = bigquery.Client()
    dataset_ref = bigquery_client.dataset(dataset_id)
    table_ref = dataset_ref.table(table_id)

    # Get the table from the API so that the schema is available.
    table = bigquery_client.get_table(table_ref)

    rows = [{'traded_at' : time_stamp, 'open' : open_p, 'high' : high_p, 'low' : low_p, 'close' : closed_p}]
    errors = bigquery_client.create_rows(table, rows)

    if not errors:
        print('Loaded 1 row into {}:{}'.format(dataset_id, table_id))
    else:
        print('Errors:')
        pprint(errors)


def main():

        print("### STARTING... ###")
        time()
        checkCoin('https://api.bithumb.com/public/ticker/BTC')

def time():
        global timestamp
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        print(timestamp)
        threading.Timer(3, time).start()

def checkCoin(url):
        threading.Timer(3, checkCoin, [url]).start()

        data = urllib.urlopen(url).read(2000) # number of chars that should catch the announcement

        print("########### http data ############")
        j = json.loads(data) # data fetch
        open_p = j['data']['opening_price']
        high_p = j['data']['max_price']
        low_p = j['data']['min_price']
        closed_p = j['data']['closing_price']

        stream_data("test_de", "thread_test", timestamp, open_p, high_p, low_p, closed_p)

main()
