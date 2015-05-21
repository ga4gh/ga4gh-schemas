.. _schemadetails:

****************
API Reference
****************


.. ATTENTION::
    The below is mostly copied verbatim from `Google's API documentation <https://cloud.google.com/genomics/what-is-google-genomics>`_

This API reference is organized by resource type as described in the Introduction. 
Each resource type has one or more data representations. 

--------------
Resource types
--------------

   * beacon
   * common
   * metadata
   * metadatamethods
   * methods
   * ontologies
   * readmethods
   * reads
   * referencemethods
   * references
   * sequenceAnnotationmethods
   * sequenceAnnotations
   * variantmethods
   * variants

++++++++++
Variants
++++++++++

A variant represents a change in DNA sequence relative to a reference sequence. 
For example, a variant could represent a SNP or an insertion. Variants belong to a variant set. 
Each of the calls on a variant represent a determination of genotype with respect to that variant. 
For example, a call might assign probability of 0.32 to the occurrence of a SNP named rs1234 in a sample named NA12345.
A call belongs to a call set, which contains related calls typically from one sample. 

(current variants.avdl text:)
A Variant represents a change in DNA sequence relative to some reference.
For example, a variant could represent a SNP or an insertion.
Variants belong to a `VariantSet`.
This is equivalent to a row in VCF.

Schema definition::

  record Variant {
    string id;
    string variantSetId;
    array<string> names = [];
    union { null, long } created = null;
    union { null, long } updated = null;
    union { null, string } referenceName = null;
    union { null, long } start = null;
    union { null, long } end = null;
    union { null, string } referenceBases = null;
    union { null, array<string> } alternateBases = null;
    union { null, array<string> } alleleIds;
    map<array<string>> info = {};
    union { null, array<Call> } calls = null;
  }

+----------------+---------+---------------------------------------------------------------------------------+
| Variable       | Type    | Description                                                                     |
+================+=========+=================================================================================+
| id             | string  | The variant ID                                                                  |
+----------------+---------+---------------------------------------------------------------------------------+
| variantSetId   | string  | The ID of the variant set this variant belongs to                               |
+----------------+---------+---------------------------------------------------------------------------------+
| names          | list    | Names for the variant, for example a RefSNP ID.                                 |
+----------------+---------+---------------------------------------------------------------------------------+
| created        | integer | The date this variant was created in milliseconds from the epoch                |
+----------------+---------+---------------------------------------------------------------------------------+
| updated        | integer | The time at which this variant was last updated in milliseconds from the        |
|                |         | epoch                                                                           |
+----------------+---------+---------------------------------------------------------------------------------+
| referenceName  | string  | The reference on which this variant occurs (e.g. chr20 or X)                    |
+----------------+---------+---------------------------------------------------------------------------------+
| start          | integer | The start position at which this variant occurs (0-based)                       |
+----------------+---------+---------------------------------------------------------------------------------+
| end            | integer | The end position (exclusive), resulting in [start, end) closed-open interval    |
+----------------+---------+---------------------------------------------------------------------------------+
| referenceBases | string  | The reference bases for this variant                                            |
+----------------+---------+---------------------------------------------------------------------------------+
| alternateBases | list    | The bases that appear instead of the reference bases                            |
+----------------+---------+---------------------------------------------------------------------------------+
| alleleIds      | list    | The IDs of the reference and alternate Alleles for this Variant                 |
+----------------+---------+---------------------------------------------------------------------------------+
| info           | map     | Additional variant information                                                  |
+----------------+---------+---------------------------------------------------------------------------------+
| calls          | list    | The variant calls for this particular variant.                                  |
+----------------+---------+---------------------------------------------------------------------------------+

Table with line breaks

============= ======= ===========
Variable      Type    Description
============= ======= ===========
id            string  | The variant ID
variantSetId  string  | The ID of the variant set this variant belongs to
names         list    | Names for the variant, for example a RefSNP ID
created       integer | The date this variant was created in milliseconds from 
                      | the epoch
updated       integer | The time at which this variant was last updated in 
                      | milliseconds from the epoch
referenceName string  | The reference on which this variant occurs (e.g. chr20 or X)
start         integer | The start position at which this variant occurs (0-based)
                      | This corresponds to the first base of the string of 
                      | reference bases. Genomic positions are non-negative 
                      | integers less than reference length. Variants spanning 
                      | the join of circular genomes are represented as two 
                      | variants one on each side of the join (position 0).
end           integer | The end position (exclusive), resulting in [start, end) 
                      | closed-open interval. This is typically calculated by 
                      | start + referenceBases.length
============= ======= ===========
