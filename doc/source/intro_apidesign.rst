.. _apidesign:

****************************
GA4GH API Design (empty)
****************************

The GA4GH schema defines common attributes and value types/ranges, as well as object relations, and how to query data in a consistent way throughout GA4GH compatible resources.

The underlying schema mostly serves those purposes but does not imply that local implementations have to mirror this object model exactly e.g. in their databaseimplementations. A typical example would be the separate definition of "Biosample" and "Individual" records in the GA4GH schema definitions, wherease a denormalized data structure with both "Biosample" and "individual" attribute::value pairs could be API compatible.
