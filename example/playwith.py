import requests
import xml.etree.ElementTree as ET
import time

current_position = None

def get_state():
    full_url = "http://192.168.86.114/zrap/chscan/ch1"
    device_info_response = requests.get(full_url)
    root = ET.fromstring(device_info_response.text)
    return str(root[0][0].text)

def count_time_till_stop():
    start = time.time()
    time.sleep(float(0.5))
    while(get_state() != '0'):
        time.sleep(float(0.2))
    end = time.time()
    print(end - start)

def go_to_position(postion):
    sleep_time = None
    global current_position
    if  current_position is None:
        payload = "cmd=close"
        full_url = "http://192.168.86.114/zrap/chctrl/ch1"
        requests.post(full_url, data=payload)
        time.sleep(float(0.2))
        while(get_state() != '0'):
            time.sleep(float(0.2))
        payload = "cmd=open"
        full_url = "http://192.168.86.114/zrap/chctrl/ch1"
        requests.post(full_url, data=payload)
        sleep_time = float(55.3/100*postion)
    elif postion < current_position:
        payload = "cmd=open"
        full_url = "http://192.168.86.114/zrap/chctrl/ch1"
        requests.post(full_url, data=payload)
        sleep_time = float(53.7/100*(current_position-postion))
    elif postion > current_position:
        payload = "cmd=close"
        full_url = "http://192.168.86.114/zrap/chctrl/ch1"
        requests.post(full_url, data=payload)
        sleep_time = float(55.3/100*(postion-current_position))
    
    time.sleep(sleep_time)
    payload = "cmd=stop"
    full_url = "http://192.168.86.114/zrap/chctrl/ch1"
    requests.post(full_url, data=payload)
    current_position = postion

device_info_response = requests.get("http://192.168.86.114/zrap/chdes")

#payload = "cmd=open"
#full_url = "http://192.168.86.114/zrap/chctrl/ch1"
#device_info_response = requests.post(full_url, data=payload)
#print(device_info_response)

go_to_position(50)
time.sleep(float(2))
go_to_position(20)
time.sleep(float(2))
go_to_position(90)
time.sleep(float(2))
go_to_position(100)
time.sleep(float(2))
go_to_position(10)
time.sleep(float(2))
go_to_position(0)

