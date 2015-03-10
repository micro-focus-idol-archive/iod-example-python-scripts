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

parser = argparse.ArgumentParser(description='Create an IOD web connector and its associated text index')
parser.add_argument('--apikey', default=IODAPIKEY)
parser.add_argument('--name', default='')
parser.add_argument('--url', default='')
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

url = args.url
if url:
    logging.info("Creating index/connector for url: %s" % url)
else:
    logging.critical("No url supplied. Exiting.")
    exit(1)

# Create the index
print "CALLING CREATTEXTINDEX"
response = unirest.post("https://api.idolondemand.com/1/api/sync/createtextindex/v1", headers={"Accept": "application/json"}, params={"apikey": apikey, "index": name, "flavor": "explorer"})
reply = json.loads(response.raw_body)
pprint.pprint(reply)
#print response.code # The HTTP status code
#print response.headers # The HTTP headers
#print response.body # The parsed response
#print response.raw_body

time.sleep(5)

# Check that the index was created and that it has finished initialising
print "CALLING INDEXSTATUS"
response = unirest.post("https://api.idolondemand.com/1/api/sync/indexstatus/v1", headers={"Accept": "application/json"}, params={"apikey": apikey, "index": name})
reply = json.loads(response.raw_body)
pprint.pprint(reply)
total_documents = reply['total_documents']
logging.info("Index has %d docs." % total_documents)

#Now we can create the connector
print "CALLING CREATECONNECTOR"
response = unirest.post("https://api.idolondemand.com/1/api/sync/createconnector/v1", headers={"Accept": "application/json"}, 
    params={
        "apikey" : apikey, 
        "connector" : name,
	"flavor" : "web_cloud",
	"config": json.dumps({"url" : url, "duration": 3600, "follow_robot_protocol": "true", "max_page_size": 9638400, "follow_redirect": "false", "page_timeout": 120}),
	"destination": json.dumps({"action" : "addtotextindex", "index" : name})
    }	
)
reply = json.loads(response.raw_body)
pprint.pprint(reply)

time.sleep(5)

print "CALLING CONNECTORSTATUS"
response = unirest.post("https://api.idolondemand.com/1/api/sync/connectorstatus/v1", headers={"Accept": "application/json"}, params={ "apikey": apikey, "connector": name})
reply = json.loads(response.raw_body)
pprint.pprint(reply)

print "CALLING STARTCONNECTOR"
response = unirest.post("https://api.idolondemand.com/1/api/sync/startconnector/v1", headers={"Accept": "application/json"}, params={ "apikey": apikey, "connector": name})
reply = json.loads(response.raw_body)
pprint.pprint(reply)

# Should now be started
print "CALLING CONNECTORSTATUS"
response = unirest.post("https://api.idolondemand.com/1/api/sync/connectorstatus/v1", headers={"Accept": "application/json"}, params={ "apikey": apikey, "connector": name})
reply = json.loads(response.raw_body)
pprint.pprint(reply)





