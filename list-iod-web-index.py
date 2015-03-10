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

parser = argparse.ArgumentParser(description='List IOD connectors associated with the API key')
parser.add_argument('--apikey', default=IODAPIKEY)
args = parser.parse_args()

apikey = args.apikey
if apikey:
    logging.info("Using apikey: %s" % apikey)
else:
    logging.critical("No apikey supplied. Exiting.")
    exit(1)

print "CALLING LISTRESOURCES FOR WEB_CLOUD CONNECTORS"
response = unirest.post("https://api.idolondemand.com/1/api/sync/listresources/v1", headers={"Accept": "application/json"}, params={"apikey": apikey, "type": "connector", "flavor": "web_cloud"})
reply = json.loads(response.raw_body)
pprint.pprint(reply)

print "CALLING LISTRESOURCES FOR FILESYSTEM_ONSITE CONNECTORS"
response = unirest.post("https://api.idolondemand.com/1/api/sync/listresources/v1", headers={"Accept": "application/json"}, params={"apikey": apikey, "type": "connector", "flavor": "filesystem_onsite"})
reply = json.loads(response.raw_body)
pprint.pprint(reply)

