import time
from datetime import datetime as dt
websites=['www.facebook.com','facebook.com','www.instagram.com','instagram.com']
local_ip='127.0.0.1'
hosts_path="/etc/hosts"

while True:
    #if dt.now() > dt(2016,5,5,4)
    if  dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        print("working hours....")
    else:
       print("fun hours...")

    time.sleep(5)
