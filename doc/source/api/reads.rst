.. _reads:

*****************
Reads API
*****************

For the Reads schema definitions, see `Reads schema <schemas/reads.html>`_

.. include:: /includes/glossary/short_reads.rst

------------------
The Reads Schema
------------------

While the Reads schema is based on the SAM format, it allows for more versatile interaction with the data. 
Instead of sending whole chromosome or whole genome files, the server can send information on specific
genomic regions instead.

The Reads schema consists of records that each describe part of the data:

=============== ============================================ ==================
Record          | Description                                SAM/BAM equivalent
=============== ============================================ ==================
ReadAlignment   | One alignment for one read                 A single line in a file
ReadGroup       | A group of read alignments                 Complete file
ReadGroupSet    | Collecton of ReadGroups that map to the    Files from one sequencing run
                | same genome
ReadStats       | Counts of aligned and unaligned reads	     Samtools flagstats on a file
                | for a ReadGroup or ReadGroupSet
LinearAlignment | Mapping of a read to a reference           One CIGAR string
Program         | Software version and parameters that were  PN, CL tags in SAM header
                | used to align reads to the genome
Fragment        | *ill defined*
=============== ============================================ ==================

For a complete description of all Reads records, see `Reads schema <schemas/reads.html>`_

Records can contain other records, for instance ReadStats is contained in ReadGroup and ReadGroupSet.
Each record is made up of a number of fields that describe the data.

This is what the ReadGroupSet record looks like::

  record ReadGroupSet {
  /** The UUID of the ReadGroupSet.*/
  string id;

  /** The ID of the Dataset this read group set belongs to. 
  union { null, string } datasetId = null;

  /** The read group set name. 
  union { null, string } name = null;

  /** The ReadStats statistical data on reads in this read group set. 
  union { null, ReadStats } stats = null;

  /** The ReadGroups that make up this read group set. */
  array<ReadGroup> readGroups = [];

  }

`FIXME: Most of these values should not be null`

So this record describes five variables: id, datasetId, name, stats, and readGroups.

  * The ``id`` is unique and can be used in other records.
  * ``dataSetId`` and ``name`` point to the unique IDs of a dataset record and a ReadGroup record, respectively.
  * ``stats`` is a special variable that is itself a whole ``ReadStats`` record.
  * ``readGroups`` is similar to stats but contains multiple ReadGroup records instead of just one.

The image below shows which Reads records contain other records (represented by green triangles), and which contain IDs that can be used to get information from other records (arrows). The arrow points `from` the record that lists the ID `to` the record that can be identified by that ID. Records are represented by blue rectangles; dotted lines indicate records defined in other schemas.

.. image:: _static/reads_schema.png
 
