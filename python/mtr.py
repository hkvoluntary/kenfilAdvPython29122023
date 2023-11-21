
# Real-time MTR train information
# https://data.gov.hk/en-data/dataset/mtr-data2-nexttrain-data

#
# https://rt.data.gov.hk/v1/transport/mtr/getSchedule.php?line=EAL&sta=EXC
# East Rail Line (EAL)
# Exhibition Centre (EXC)

import urllib.request
import json
import time
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def getData(url):
    response = urllib.request.urlopen(url, context=ctx)
    if(response.getcode()==200):
        data = response.read()
        jsonData = json.loads(data)
    else:
        print("Error occured", response.getcode())
    return jsonData

url = "https://rt.data.gov.hk/v1/transport/mtr/getSchedule.php?line=EAL&sta=EXC"
data = getData(url)

#print(data)
#print(data['sys_time'])

coming_train = []

for i in data["data"]['EAL-EXC']['UP']:
    print(type(i))
    for key, value in i.items():
      print(key, '->', value)
      if (key == 'dest'):
        coming_train.append(value)
      if (key == 'time'):
        coming_train.append(value)

print("List of the next 4 trains: ", end="")
print(coming_train)
