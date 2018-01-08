import time
import os.path
import datetime
from time import localtime

now = datetime.datetime.now().strftime("%Y%m%d%H") # current day

EXPORT204 = "gsutil -m cp /home/Tora/thread_test/"+now+".csv gs://gcpkr-bitcoin-keras/preprocess" # copy the file to gcs bucket
#EXPORT205 = "mv "+now+".csv 201711_1h"

os.system(EXPORT204) # execute EXPORT204
#os.system(EXPORT205)
