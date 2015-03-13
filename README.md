# iod-example-python-scripts

A set of sample Python Scripts for using various [IDOL OnDemand](http://www.idolondemand.com) [APIs](https://www.idolondemand.com/developer/apis).  

In particular these demonstrate the creation, administration, querying and deletion of a standard flavor unstructured text index populated with a connector that indexes content from a website.

See [connector documentation](https://www.idolondemand.com/developer/apis/createconnector#overview) and [unstructured index documentation](https://www.idolondemand.com/developer/apis/createtextindex#overview)

## Dependencies

You will need to install the [unirest](http://unirest.io/) [python module](http://unirest.io/python.html)

> sudo pip install unirest

If you don't have pip then it's simple to install:

Ubuntu / Debian based systems:

> sudo apt-get install python-pip

Read Hat / CentOS based systems:

> sudo yum install python-pip

## Usage

You will need to signup for an account and obtain your [IDOL OnDemand](http://www.idolondemand.com) API key.  The scripts below can either read the [IDOL OnDemand](http://www.idolondemand.com) API Key from the IODAPIKEY environment variable or you can supply it on the command line using the --apikey option.

> export IODAPIKEY=&lt;YOUR-IOD-API-KEY-HERE&gt;

Create an IOD unstructured index and a web connector
> ./create-iod-web-index.py --name &lt;indexname&gt; --url &lt;enter URL here&gt;

Check the status of the connector and unstructued index
> ./check-iod-web-index.py --name &lt;indexname&gt;

List connectors created on this account
> ./list-iod-connectors.py 

Search an unstructured index
> ./search-iod-web-index.py --name &lt;indexname&gt; &lt;search text&gt;

Search an unstructured index and the connector we used to populate it
> ./delete-iod-web-index.py --name &lt;indexname&gt;

IODAPIKEY can either be set as an environment variable or supplied using the --apikey option.

## License
Copyright 2015 Hewlett-Packard Development Company, L.P.

Licensed under the MIT License (the "License"); you may not use this project except in compliance with the License.


