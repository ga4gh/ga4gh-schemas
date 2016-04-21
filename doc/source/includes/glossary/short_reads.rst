-------------------
Short Reads and BAM
-------------------

High throughput genome and transcriptome sequencing produces millions of short (50-200 nucleotide) sequences.
These sequences are usually referred to as reads. Reads can be produced from:

#. Complete genomes. These reads can be used to piece together the full genome of an individual.
#. Exomes. These reads are derived from just the gene regions in the genome (in humans this is a reduction of >97%)
#. Transcriptomes. Here, the RNA that gets transcribed from the genomic DNA is sequenced, representing only the genes that are active in the tissue that was sampled. Transcriptomes differ from tissue to tissue and can be used to determine differences between tumors and their surrounding tissues.

Reads are usually mapped to a reference genome, for example `GRCh37`_ in humans.

These alignments can be displayed like so::

    ID      CHROM  POS    CIGAR   SEQUENCE  
    read1   chr1   234    10M     GACAGTCCCA  
    read2   chr14  1456   10M     AAAGATTGAC  
    read3   chrX   2837   7M2I1M  TGGGACTCTA  


In this format, the CIGAR string shows how well the read matches the genome: read1 is identical to the genome sequence over all its
10 bases: 10M. The first seven bases of read3 match the genome (7M), but then it has a 2 base insertion (2I), followed by another 1 base match (1M).

The `SAM/BAM Format`_ is a way of representing read data. It includes the fields shown above as well as information on read orientation, sequence quality, and optional fields. The format also allows for reads that do not align to the genome, by leaving the reference sequence ID, position, and cigar fields empty.

SAM is a human readable format, BAM is a condensed binary format. The formats can be readily converted to each other.

.. _SAM/BAM Format: https://samtools.github.io/hts-specs/SAMv1.pdf

.. _GRCh37: http://www.ncbi.nlm.nih.gov/assembly/GCF_000001405.13
