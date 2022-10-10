import time
import datetime
import logging
import sys
import os


### [INFO] 2022/09/17 23:13:58 "GET / HTTP/1.1" 200 "address: https://www.baidu.com" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
### [WARNING] 2022/09/17 23:13:60 "GET / HTTP/1.1" 404 "address: https://www.google.com" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
def log(type="INFO"):
    addr_1 = "https://www.baidu.com"
    addr_2 = "https://www.google.com"
    content = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"

    addr = addr_1 if type == "INFO" else addr_2
    status = 200 if type == "INFO" else 404

    curTime = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')

    return f"[{type}] {curTime} \"GET / HTTP/1.1\" {status} \"address: {addr}\" \"{content}\"\n"


N = 30
interval = 5

filename = "log"
for i in range(N):
    with open(filename, 'a+') as file:
        file.write(log("INFO" if i % 5 != 0 else "WARNING"))
        time.sleep(interval)
        file.close()