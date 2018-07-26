import time
from datetime import datetime as dt
websites=['www.facebook.com','facebook.com','www.instagram.com','instagram.com']
local_ip='127.0.0.1'
hosts_path="/etc/hosts"
hosts_temp="hosts"

while True:
    #if dt.now() > dt(2016,5,5,4)
    if  dt(dt.now().year,dt.now().month,dt.now().day,0) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,8):
        with open(hosts_temp ,'r+') as file:
            data=file.read()
            for website in websites:
                if website in data:
                    pass
                else:
                    file.write(local_ip+" "+website+"\n")
                    #print("data written")
    else:
        with open(hosts_temp,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in websites):
                    file.write(line)
            file.truncate()


    time.sleep(5)
