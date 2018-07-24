#!/usr/bin/python

import json

data = json.load(open('ip-ranges.json'))
for y in data["prefixes"]:
	print y["ip_prefix"]
