# This is a sample Python script.
from datetime import datetime

import keyboard # wymagany jest root na linuxie
import requests
import threading
import time
import sys
import os
from tinydb import TinyDB, Query
import json
import uuid

import zlib
db = TinyDB('db.json')

sys.path.append(os.path.abspath('./src/page'))
import page

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

### Listowanie documentow
table = db.table('page_request')

print("Wprowadź URL do wykonywania requestów metodą GET:")

#Utworzenie obiektu page
page = page.Page(
    input("Podaj pełną ścieżkę z http/https:\n"),
    int(input("Podaj liczbę wątków:\n"))
)

f = open("log.txt", "a")

def doRequest():
    while True:
        r = requests.get(page.get_url())
        f.write(page.get_url() + " " + str(datetime.now().strftime("%H:%M:%S")) + ": " + str(r.status_code) + "\n")
        f.write(r.text)
        f.write("\n")
        print(page.get_url() + ": " + str(r.status_code) + "\n")

        #switch table

        table = db.table('page_request')

        table.insert({
            'uuid': str(uuid.uuid4()),
            'url': page.get_url(),
            'status_code': r.status_code,
            'date': datetime.now().isoformat(),
            'date_string': str(datetime.now().strftime("%H:%M:%S")),
            'compressed_response': r.text,
            'headers': json.dumps(dict(r.headers))
        })

        if r.status_code != 200:
            print(r.text)

threads = []

if __name__ == '__main__':
    for i in range(page.get_threads_cnt()):
        t = threading.Thread(target=doRequest, daemon=True)
        t.setDaemon(True)
        threads.append(t)

        print(t)

    for i in range(page.get_threads_cnt()):
        threads[i].start()
        print(threads[i].name)

    for i in range(page.get_threads_cnt()):
        threads[i].join()

f.close()