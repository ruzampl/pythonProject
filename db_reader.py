import sys
import os
from tinydb import TinyDB, Query
db = TinyDB('db.json')

sys.path.append(os.path.abspath('./src/page'))
import page
### Listowanie documentow
table = db.table('page_request')

PageData = Query()
table.all()

for page_data in table.all():
  print(f"UUID: {page_data['uuid']}")
  print(f"Status CODE: {page_data['status_code']}")
  print(f"Data: {page_data['date_string']}")
  print(f"Adres url: {page_data['url']}")

