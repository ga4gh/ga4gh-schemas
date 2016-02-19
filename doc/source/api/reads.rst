.. _reads:


Reads API
!!!!!!!!!

See `Reads schema <../schemas/reads.html>`_ for a detailed reference.


Reads Data Model
@@@@@@@@@@@@@@@@

The Reads data model,although based on the SAM format, allows for more
versatile interaction with the data.  Instead of sending whole
chromosome or whole genome files, the server can send information on
specific genomic regions instead.

The model has the following data types:

============================== ============================================ ==================
Record                         | Description                                SAM/BAM rough equivalent
============================== ============================================ ==================
:avro:record:`ReadAlignment`   | One alignment for one read                 A single line in a file
:avro:record:`ReadGroup`       | A group of read alignments                 A single RG tag
:avro:record:`ReadGroupSet`    | Collecton of ReadGroups that map to the    Single SAM/BAM file
                               | same genome
:avro:record:`Program`         | Software version and parameters that were  PN, CL tags in SAM header
                               | used to align reads to the genome
:avro:record:`ReadStats`       | Counts of aligned and unaligned reads      Samtools flagstats on a file
                               | for a ReadGroup or ReadGroupSet
============================== ============================================ ==================

The relationships are mostly one to many (e.g. each
:avro:record:`ReadAlignment` is part of exactly one
:avro:record:`ReadGroup`), with the exception that a
:avro:record:`ReadGroup` is allowed to be part of more than one
:avro:record:`ReadGroupSet`.

:avro:record:`Dataset` --< :avro:record:`ReadGroupSet` >--< :avro:record:`ReadGroup` --< :avro:record:`ReadAlignment`

* A :avro:record:`Dataset` is a general-purpose container, defined in
  metadata.avdl.
* A :avro:record:`ReadGroupSet` is a logical collection of ReadGroups,
  as determined by the data owner.  Typically one
  :avro:record:`ReadGroupSet` represents all the Reads from one
  experimental sample, which traditionally would be stored in a single
  BAM file.
* A :avro:record:`ReadGroup` is all the data that's processed the same
  way by the sequencer.  There are typically 1-10 ReadGroups in a
  :avro:record:`ReadGroupSet`.
* A :avro:record:`ReadAlignment` object is a flattened representation
  of several layers of bioinformatics hierarchy, including fragments,
  reads, and alignments, stored in one object for easy access.


ReadAlignment: detailed discussion
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

One :avro:record:`ReadAlignment` object represents the following
logical hierarchy. See the field definitions in the
:avro:record:`ReadAlignment` object for more details.

.. image:: /_static/read_alignment_diagrams.png

* A *fragment* is a single stretch of a DNA molecule.  There are
  typically at least millions of fragments in a ReadGroup.  A fragment
  has a name (QNAME in BAM spec), a length (TLEN in BAM spec), and one
  or more reads.
* A *read* is a contiguous sequence of bases. There are typically only
  one or two reads in a fragment. If there are two reads, they're
  known as a mate pair.  A read has an array of base values, an array
  of base qualities, and optional alignment information.
* An *alignment* is the way alignment software maps a read to a
  reference.  There's one primary alignment, and can be one or more
  secondary alignments.  Secondary alignments represent alternate
  possible mappings.
* A *linear alignment* maps a string of bases to a reference using a
  single CIGAR string. There's one representative alignment, and can
  be one or more supplementary alignments. Supplementary alignments
  represent linear alignments that are subsets of a chimeric
  alignment.

The image below shows which Reads records contain other records
(represented by green triangles), and which contain IDs that can be
used to get information from other records (arrows). The arrow points
*from* the record that lists the ID *to* the record that can be
identified by that ID. Records are represented by blue rectangles;
dotted lines indicate records defined in other schemas.

.. image:: /_static/reads_schema.png
 
