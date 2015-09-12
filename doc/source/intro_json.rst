.. _json:

**********************
The JSON Format	(stub)
**********************

format described `here <http://json.org/example>`_

..todo::
   show example of GH4GH JSON output

This is from the `ga4gh server example`_

.. _ga4gh server example: http://ga4gh-reference-implementation.readthedocs.org/en/stable/demo.html#demo

To get information from the readgroupsets on a server, create a JSON format request::

    {
      "datasetIds":[], 
      "name":null
    }

.. note::
    What is this actually asking?

To send this to the server, we need to create a HTTP request which tells the server what type of
data to expect (JSON format, in this case)
In our test case, we have a server running at \http://localhost:8000

Since we want to query the readgroupsets, we'll have to make that part of the URL

.. note::
     * How do we know it's v0.5.1?
     * where is the readgroupsets/search part documented or defined?

To create a command line request, we can use `cURL <http://curl.haxx.se/>`_::

    curl --data '{"datasetIds":[], "name":null}' --header 'Content-Type: application/json' http://localhost:8000/v0.5.1/readgroupsets/search

The server returns::

    {
    "nextPageToken": null,
    "readGroupSets": [{
    "readGroups": [{
    "info": {}, 
    "updated": 1432287597662, 
    "predictedInsertSize": null, 
    "description": null, 
    "created": 1432287597662, 
    "programs": [], 
    "sampleId": null, 
    "experiment": null,
    "referenceSetId": null,
    "id":
    "low-coverage:HG00533.mapped.ILLUMINA.bwa.CHS.low_coverage.20120522",
    "datasetId": null,
    "name":
    "low-coverage:HG00533.mapped.ILLUMINA.bwa.CHS.low_coverage.20120522"
    }, 
    {   "info": {},
    "updated": 1432287793946,
    "predictedInsertSize": null,
    "description": null,
    "created": 1432287793946,
    "programs": [],
    "sampleId": null,
    "experiment": null,
    "referenceSetId": null,
    "id":
    "low-coverage:HG00096.mapped.ILLUMINA.bwa.GBR.low_coverage.20120522",
    "datasetId": null,
    "name":
    "low-coverage:HG00096.mapped.ILLUMINA.bwa.GBR.low_coverage.20120522"
    }, 
    {    "info": {},
    "updated": 1432287793946,
    "predictedInsertSize": null,
    "description": null,
    "created": 1432287793946,
    "programs": [],
    "sampleId": null,
    "experiment": null,
    "referenceSetId": null,
    "id":
    "low-coverage:HG00534.mapped.ILLUMINA.bwa.CHS.low_coverage.20120522",
    "datasetId": null,
    "name":
    "low-coverage:HG00534.mapped.ILLUMINA.bwa.CHS.low_coverage.20120522"
    }],
    "id":
    "low-coverage",
    "datasetId": null,
    "name": null
    }
    ]
    }



