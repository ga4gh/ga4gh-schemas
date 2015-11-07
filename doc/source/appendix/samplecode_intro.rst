.. _samplecode:

*******************
Code samples (stub)
*******************

Useful tips from an online `article`_ about API development:

.. _article: https://msdn.microsoft.com/en-us/magazine/gg309172.aspx

    * Relevant information should be grouped together.
    * Clarity is more important than efficiency or robustness.
    * Simplicity is more important than a good-looking UI.

Notes on sample code: 
    * *DO* use hard-coded values to make the code easy to understand
    * Variable, class, member and function names should be clear, feel free to use long names
    * Forego exception handling, instead put in a comment indicating what kind of exceptions to handle in production code.

There is a long, useful section on sample code in the article listed above.

Notes on web APIs:
    * There should be code samples in several languages 
    * Create Sample HTTP calls and JSON/ProtoBuf files

Samples should be followed by tables that describe each element as well as its data format. 
For example, it may not be enough to describe a parameter as a string. 
Are there special characters it can't handle? 
Are there limitations on its length? 
If an XML element is a date, you should specify the format of the date. 
If it's a time, then you need to specify its time zone.

Also, you'll need to explain how errors are handled. 
This may vary for the different formats that your API supports. 
If your API uses HTTP response codes to flag errors, these should be documented. 
Error documentation should explain why an error occurs and how to fix the problem.

Authentication is often required for Web APIs, and this needs to be documented in detail as well. 
If developers need API keys, be sure to give them step-by-step instructions on how to obtain these. 
Also, don't forget that Web APIs are built on top of HTTP, which is an incredibly rich protocol. 
You may have HTTP-related information that requires documentation, such as caching, content type and status codes.
