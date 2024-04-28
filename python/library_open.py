#! /usr/bin/env python3
import requests, json

url = 'https://www.library-archives.pref.fukui.lg.jp/tosyo/assets/json/calendar/eventcalendar.fukuilib.tosyo.json'
res = requests.get(url)
if res.status_code == 200:
    json_data = json.dumps(res.json())
    opening_durations = json.dumps(res)
    print(json_data)
else:
    print("Error",response.status_code)

