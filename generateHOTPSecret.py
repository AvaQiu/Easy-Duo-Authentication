#!/usr/bin/env python3

import requests
import base64
import json
import sys

DuoURL = sys.argv[1]
host = 'api' + DuoURL[DuoURL.find('-') : DuoURL.find('com')+3]
key = DuoURL[DuoURL.rindex('/')+1 : ]

URL = 'https://' + host + '/push/v2/activation/' + key + '?customer_protocol=1'
response = json.loads(requests.post(URL).text)

try:
    HOTPSecret = response['response']['hotp_secret']
    print('This is your HOTP Secret: ' + HOTPSecret)
    print('Please copy it to the Chrome extension.')
except KeyError:
    print('Something went wrong. Maybe the link has been used.')
