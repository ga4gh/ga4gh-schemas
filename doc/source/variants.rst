.. _variants:

***************
Variants
***************

Genetic variants are changes in the genome from one individual to the next. Such variants can be more or less common and may have effects on gene regulation
or protein sequences. 

There are three types of variants:

#. Single Nucleotide Polymorphisms (SNPs), which include small insertions and deletions 
#. Copy number variations, which happen when the number of copies of a particular gene or DNA segment varies from one individual to the next.
#. Structural variants, affecting larger genomic regions. This last group is (currently) outside the scope of GA4GH.

To study genetic variants, individual genome sequences are usually compared to a single reference genome, for example `GRCh37`_ in humans.

An individual genome will have many differences with respect to the reference. They might be displayed like so::

    CHROM  POS     REF  ALT  
    20     14370   G      A 
    20     17330   T      A
    20     18302   T      .


Here, the reference sequence has a T at position 18302 in the genome, but the individual has a one nucleotide deletion, 
represented as a period.
These variant versions (G or A, T or .) are also known as alleles.

Many variants are common enough to have a SNP id, a number starting with 'rs' (for Reference SNP). See `dbSNP`_ for details.

Humans are diploid, meaning they have two copies of each chromosome (except X and Y). It is therefore possible to have one copy each of the reference and
alternative alleles in a single individual.

The `Variant Call Format (VCF)`_ is a way of representing allele data for individuals. It includes a coordinate system as shown above, SNP rsIDs if available, 
and one data column per individual that shows the alleles for each variant.
The Variant schema is based on this file format.

.. _GRCh37: http://www.ncbi.nlm.nih.gov/assembly/GCF_000001405.13
.. _dbSNP: http://www.ncbi.nlm.nih.gov/SNP
.. _Variant Call Format (VCF): http://www.1000genomes.org/wiki/analysis/variant%20call%20format/vcf-variant-call-format-version-41


------------------
The Variant Schema
------------------

While the Variant schema is based on VCF, it allows for more versatile interaction with the data. 
Instead of sending whole chromosome or whole genome VCF files, the server can send information on specific
genomic regions instead. And instead of getting all data for an experiment, it is possible to just get details for a single individual.
`EXPLAIN: Will it also be possible to query on e.g. rsID?`

The Variant schema consists of records that each describe part of the data:

========== ================================================== ==============
Record     | Description                                      VCF equivalent
========== ================================================== ==============
Variant    | Position of genetic difference with respect to   Single line without genotype fields
           | a reference genome 
Allele     | A contiguous piece of sequence that is           **REF** and **ALT** fields
           | present or absent in a sample. 
AlleleCall | Allele call(s) for one variant in one individual First subfield in genotype field
Call	   | Information on AlleleCall			      Remaining subfields in genotype field
CallSet	   | All Variant calls for a single individual        Genotype column
VariantSet | A collection of variants                         VCF file
Metadata   | Information on the flags used                    VCF header
========== ================================================== ==============


`EXPLAIN: Where do the Qual, Info, Filter, and Format fields go?`

This is what the Allele record looks like::

  record Allele {
  /**
  The ID of this Allele.
  */
  string id;

  /** The ID of the variant set this allele belongs to. */
  string variantSetId;

  /**
  The ordered and oriented Segments of DNA that this Allele represents.
  */
  Path path;
  }

So this record describes three variables: id, variantSetId, and path.

The ``id`` is unique and can be used in other records. For instance, the Variant record has a variable named ``alleleIds``, which can be used to look up allele records.

``variantSetId`` points to the unique ID of a variantSet record.

``path`` is a special variable that is itself a whole record. This nesting of records is very common: For instance, if you request a VariantSet (for instance by its ``id``), one of its fields contains a list of VariantSetMetadata, which are described in a separate record.
Path is used by records in other schemas, and is therefore described in the Common schema.

Below is an image of which records contain other records (such as ``path``), and which contain IDs that can be used to get information from other records (such as ``variantSetId``). The arrow points `from` the record that lists the ID `to` the record that can be identified by that ID.

.. image:: _static/variant_schema.png
 
`NOTE from your friendly neighborhood doc author: To be honest, this maze of arrows makes little sense to me.  
Why is there an arrow from Call to Variant?  
Why do both AlleleCall and Variant contain Allele IDs?`
