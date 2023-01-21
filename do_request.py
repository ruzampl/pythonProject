# This is a sample Python script.
from datetime import datetime
from dataclasses import dataclass
import keyboard # wymagany jest root na linuxie
import requests
import threading
import sys
import os
from tinydb import TinyDB, Query
import json
import uuid

sys.path.append(os.path.abspath('./src/page'))
import page

@dataclass()
class DoRequest:
    def prepare_db(self):
        import zlib
        db = TinyDB('db.json')
        ### Listowanie documentow
        table = db.table('page_request')
        return table

    def prepare_log(self):
        f = open("log.txt", "a")
        return f

    def doRequest(self, page, f, table, windowOutput, window):
        while True:
            dateString = str(datetime.now().strftime("%H:%M:%S"))
            r = requests.get(page.get_url())
            f.write(page.get_url() + " " + str(datetime.now().strftime("%H:%M:%S")) + ": " + str(r.status_code) + "\n")
            f.write(r.text)
            f.write("\n")
            print(page.get_url() + ": " + str(r.status_code) + "\n")
            windowOutput.update(dateString + " " + str(page.get_url() + ": " + str(r.status_code)))
            window.refresh()

            table.insert({
                'uuid': str(uuid.uuid4()),
                'url': page.get_url(),
                'status_code': r.status_code,
                'date': datetime.now().isoformat(),
                'date_string': dateString,
                'compressed_response': r.text,
                'headers': json.dumps(dict(r.headers))
            })

            if r.status_code != 200:
                print(r.text)

    def run_threads(self, page, output, window):
        threads = []
        f = self.prepare_log()
        table = self.prepare_db()

        for i in range(page.get_threads_cnt()):
            t = threading.Thread(target=self.doRequest(page, f, table, output, window), daemon=True)
            t.setDaemon(True)
            threads.append(t)

            print(t)

        for i in range(page.get_threads_cnt()):
            threads[i].start()
            print(threads[i].name)

        for i in range(page.get_threads_cnt()):
            threads[i].join()

        f.close()