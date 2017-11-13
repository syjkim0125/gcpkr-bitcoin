# first, you should install python-crontab
# pip install python-crontab
# then, you create this python file
# this code is example for 1 minutes crontask

from crontab import CronTab

my_cron = CronTab(user='Tora')
job = my_cron.new(command='python /home/Tora/MyScripts/for_test.py') # example path
job.minute.every(1)

my_cron.write()
