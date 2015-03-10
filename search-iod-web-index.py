#!/usr/bin/env python

import os
import unirest
import time
import json
import pprint
import logging
import argparse

unirest.timeout(120)

IODAPIKEY = os.environ.get('IODAPIKEY')

parser = argparse.ArgumentParser(description='Check the status of an IOD web connector and its associated text index')
parser.add_argument('--apikey', default=IODAPIKEY)
parser.add_argument('--name', default='')
parser.add_argument('text')
args = parser.parse_args()

apikey = args.apikey
if apikey:
    logging.info("Using apikey: %s" % apikey)
else:
    logging.critical("No apikey supplied. Exiting.")
    exit(1)

name = args.name
if name:
    logging.info("Deleting index/connector: %s" % name)
else:
    logging.critical("No name supplied. Exiting.")
    exit(1)

text = args.text
if text:
    logging.info("Searching for: %s" % text)
else:
    logging.critical("No search text supplied. Exiting.")
    exit(1)

print "CALLING QUERYTEXTINDEX"
response = unirest.post("https://api.idolondemand.com/1/api/sync/querytextindex/v1", headers={"Accept": "application/json"}, params={"apikey": apikey, "indexes": name, "text": text})
reply = json.loads(response.raw_body)
pprint.pprint(reply)
