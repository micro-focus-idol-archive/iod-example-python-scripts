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

parser = argparse.ArgumentParser(description='Delete an IOD web connector and its associated text index')
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

# Now delete the index.  Call first to get the confirmation token
response = unirest.get("https://api.idolondemand.com/1/api/sync/deletetextindex/v1", headers={"Accept": "application/json"}, params={"index": name, "apikey": apikey})
reply = json.loads(response.raw_body)
pprint.pprint(reply)
confirm = reply['confirm']

print "DELETING INDEX - CONFIRM"
# Now delete the index.  Second call with the "confirm" token
response = unirest.get("https://api.idolondemand.com/1/api/sync/deletetextindex/v1", headers={"Accept": "application/json"}, params={"index": name, "apikey": apikey, "confirm": confirm})
reply = json.loads(response.raw_body)
pprint.pprint(reply)

print "DELETING CONNECTOR"
response = unirest.get("https://api.idolondemand.com/1/api/sync/deleteconnector/v1", headers={"Accept": "application/json"}, params={"connector": name, "apikey": apikey})
reply = json.loads(response.raw_body)
pprint.pprint(reply)



