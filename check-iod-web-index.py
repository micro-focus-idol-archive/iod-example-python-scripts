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

print "CALLING INDEXSTATUS"
response = unirest.post("https://api.idolondemand.com/1/api/sync/indexstatus/v1", headers={"Accept": "application/json"}, params={"apikey": apikey, "index": name})
reply = json.loads(response.raw_body)
pprint.pprint(reply)
total_documents = reply['total_documents']
logging.info("Index has %d docs." % total_documents)

print "CALLING CONNECTORSTATUS"
response = unirest.post("https://api.idolondemand.com/1/api/sync/connectorstatus/v1", headers={"Accept": "application/json"}, params={ "apikey": apikey, "connector": name})
reply = json.loads(response.raw_body)
pprint.pprint(reply)





