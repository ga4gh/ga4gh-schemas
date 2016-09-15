.. _assaymetadata:

.. image:: /_static/assaymetadata_schema.png
   :scale: 50 %
   :align: right

.. _assaymetadata_experiment:

**********************************
AssayMetadata: *Experiment* Object
**********************************

Experiment in the GA4GH Schema
------------------------------


Experiment attributes
=====================

===================== ==========================================================
Attribute             Notes
===================== ==========================================================
*id*                  * the Experiment's id
-                     * unique in the context of the server
-                     * used for referencing this Experiment
*name*                * a human readable object label/identifier
-                     * not to be used for referencing
*description*         * additional, unstructured information about this Experiment
*created*             * the time the record was created, in ISO8601
*updated*             * the time the record was updated, in ISO8601
*info*                * additional, structured information
===================== ==========================================================

.. _assaymetadata_analysis:

********************************
AssayMetadata: *Analysis* Object
********************************

Analysis in the GA4GH Schema
------------------------------



Analysis attributes
=====================

Attribute             Notes
===================== ==========================================================
*id*                  * the Analysis's id
-                     * unique in the context of the server
-                     * used for referencing this Analysis
*name*                * a human readable object label/identifier
-                     * not to be used for referencing
*description*         * additional, unstructured information about this Analysis
*created*             * the time the record was created, in ISO8601
*updated*             * the time the record was updated, in ISO8601
*info*                * additional, structured information
===================== ==========================================================
