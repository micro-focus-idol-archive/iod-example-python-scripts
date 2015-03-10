# iod-example-python-scripts

A set of sample Python Scripts for using various [IDOL OnDemand](http://www.idolondemand.com) APIs.  

In particular these demonstrate the creation, admin, query and deletion of a standard flavor unstructured text index populated with a web connector.

## Usage

Create an IOD unstructured index and a web connector
> ./create-iod-web-index.py --name &lt;indexname&gt; --url <enter URL here>

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


