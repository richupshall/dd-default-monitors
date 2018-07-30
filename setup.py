#!/usr/bin/env python
import os
import requests

API_KEY=''
APPLICATION_KEY=''

url='https://app.datadoghq.com/api/v1/monitor?api_key=%s&application_key=%s' % (API_KEY,APPLICATION_KEY)

for subdir, dirs, files in os.walk('.'):
    for file in files:
		print file
		if file.endswith(".json"): 
			with open(subdir + os.sep + file) as f:
				read_data = f.read().replace('\n', ' ').replace('\r', '')
				payload=read_data
				headers={'Content-type': 'application/json'}
				res=requests.post(url, data=payload, headers=headers)
				print res