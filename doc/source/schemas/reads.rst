Reads
*****

This file defines the objects used to represent a hierarchy of reads and
alignments:

ReadGroupSet >--< ReadGroup --< fragment --< read --< alignment --<
linear alignment

-  A ReadGroupSet is a logical collection of ReadGroup's.
-  A ReadGroup is all the data that's processed the same way by the
   sequencer. There are typically 1-10 ReadGroup's in a ReadGroupSet.
-  A *fragment* is a single stretch of a DNA molecule. There are
   typically millions of fragments in a ReadGroup. A fragment has a name
   (QNAME in BAM spec), a length (TLEN in BAM spec), and an array of
   reads.
-  A *read* is a contiguous sequence of bases. There are typically only
   one or two reads in a fragment. If there are two reads, they're known
   as a mate pair. A read has an array of base values, an array of base
   qualities, and alignment information.
-  An *alignment* is the way alignment software maps a read to a
   reference. There's one primary alignment, and can be one or more
   secondary alignments. Secondary alignments represent alternate
   possible mappings.
-  A *linear alignment* maps a string of bases to a reference using a
   single CIGAR string. There's one representative alignment, and can be
   one or more supplementary alignments. Supplementary alignments
   represent linear alignments that are subsets of a chimeric alignment.
-  A ReadAlignment object is a flattened representation of the bottom
   layers of this hierarchy. There's exactly one such object per *linear
   alignment*. The object contains alignment info, plus fragment and
   read info for easy access.


.. avro:enum:: Strand

  :symbols: NEG_STRAND|POS_STRAND
  Indicates the DNA strand associate for some data item. \*
  ``NEG_STRAND``: The negative (-) strand. \* ``POS_STRAND``: The postive
  (+) strand.
  

.. avro:record:: Position

  :field referenceName:
    The name of the ``Reference`` on which the ``Position`` is located.
    
  :type referenceName: string
  :field position:
    The 0-based offset from the start of the forward strand for that
    ``Reference``. Genomic positions are non-negative integers less than
    ``Reference`` length.
    
  :type position: long
  :field strand:
    Strand the position is associated with.
    
  :type strand: Strand

  A ``Position`` is an unoriented base in some ``Reference``. A
  ``Position`` is represented by a ``Reference`` name, and a base number
  on that ``Reference`` (0-based).
  

.. avro:record:: ExternalIdentifier

  :field database:
    The source of the identifier. (e.g. ``Ensembl``)
    
  :type database: string
  :field identifier:
    The ID defined by the external database. (e.g. ``ENST00000000000``)
    
  :type identifier: string
  :field version:
    The version of the object or the database (e.g. ``78``)
    
  :type version: string

  Identifier from a public database
  

.. avro:enum:: CigarOperation

  :symbols: ALIGNMENT_MATCH|INSERT|DELETE|SKIP|CLIP_SOFT|CLIP_HARD|PAD|SEQUENCE_MATCH|SEQUENCE_MISMATCH
  An enum for the different types of CIGAR alignment operations that
  exist. Used wherever CIGAR alignments are used. The different enumerated
  values have the following usage:
  
  -  ``ALIGNMENT_MATCH``: An alignment match indicates that a sequence can
     be aligned to the reference without evidence of an INDEL. Unlike the
     ``SEQUENCE_MATCH`` and ``SEQUENCE_MISMATCH`` operators, the
     ``ALIGNMENT_MATCH`` operator does not indicate whether the reference
     and read sequences are an exact match. This operator is equivalent to
     SAM's ``M``.
  -  ``INSERT``: The insert operator indicates that the read contains
     evidence of bases being inserted into the reference. This operator is
     equivalent to SAM's ``I``.
  -  ``DELETE``: The delete operator indicates that the read contains
     evidence of bases being deleted from the reference. This operator is
     equivalent to SAM's ``D``.
  -  ``SKIP``: The skip operator indicates that this read skips a long
     segment of the reference, but the bases have not been deleted. This
     operator is commonly used when working with RNA-seq data, where reads
     may skip long segments of the reference between exons. This operator
     is equivalent to SAM's 'N'.
  -  ``CLIP_SOFT``: The soft clip operator indicates that bases at the
     start/end of a read have not been considered during alignment. This
     may occur if the majority of a read maps, except for low quality
     bases at the start/end of a read. This operator is equivalent to
     SAM's 'S'. Bases that are soft clipped will still be stored in the
     read.
  -  ``CLIP_HARD``: The hard clip operator indicates that bases at the
     start/end of a read have been omitted from this alignment. This may
     occur if this linear alignment is part of a chimeric alignment, or if
     the read has been trimmed (e.g., during error correction, or to trim
     poly-A tails for RNA-seq). This operator is equivalent to SAM's 'H'.
  -  ``PAD``: The pad operator indicates that there is padding in an
     alignment. This operator is equivalent to SAM's 'P'.
  -  ``SEQUENCE_MATCH``: This operator indicates that this portion of the
     aligned sequence exactly matches the reference (e.g., all bases are
     equal to the reference bases). This operator is equivalent to SAM's
     '='.
  -  ``SEQUENCE_MISMATCH``: This operator indicates that this portion of
     the aligned sequence is an alignment match to the reference, but a
     sequence mismatch (e.g., the bases are not equal to the reference).
     This can indicate a SNP or a read error. This operator is equivalent
     to SAM's 'X'.
  

.. avro:record:: CigarUnit

  :field operation:
    The operation type.
    
  :type operation: CigarOperation
  :field operationLength:
    The number of bases that the operation runs for.
    
  :type operationLength: long
  :field referenceSequence:
    ``referenceSequence`` is only used at mismatches (``SEQUENCE_MISMATCH``)
    and deletions (``DELETE``). Filling this field replaces the MD tag. If
    the relevant information is not available, leave this field as ``null``.
    
  :type referenceSequence: null|string

  A structure for an instance of a CIGAR operation.
  

.. avro:record:: Experiment

  :field id:
    The experiment UUID. This is globally unique.
    
  :type id: string
  :field name:
    The name of the experiment.
    
  :type name: null|string
  :field description:
    A description of the experiment.
    
  :type description: null|string
  :field recordCreateTime:
    The time at which this record was created. Format: ISO 8601,
    YYYY-MM-DDTHH:MM:SS.SSS (e.g. 2015-02-10T00:03:42.123Z)
    
  :type recordCreateTime: string
  :field recordUpdateTime:
    The time at which this record was last updated. Format: ISO 8601,
    YYYY-MM-DDTHH:MM:SS.SSS (e.g. 2015-02-10T00:03:42.123Z)
    
  :type recordUpdateTime: string
  :field runTime:
    The time at which this experiment was performed. Granularity here is
    variabel (e.g. date only). Format: ISO 8601, YYYY-MM-DDTHH:MM:SS (e.g.
    2015-02-10T00:03:42)
    
  :type runTime: null|string
  :field molecule:
    The molecule examined in this experiment. (e.g. genomics DNA, total RNA)
    
  :type molecule: null|string
  :field strategy:
    The experiment technique or strategy applied to the sample. (e.g. whole
    genome sequencing, RNA-seq, RIP-seq)
    
  :type strategy: null|string
  :field selection:
    The method used to enrich the target. (e.g. immunoprecipitation, size
    fractionation, MNase digestion)
    
  :type selection: null|string
  :field library:
    The name of the library used as part of this experiment.
    
  :type library: null|string
  :field libraryLayout:
    The configuration of sequenced reads. (e.g. Single or Paired)
    
  :type libraryLayout: null|string
  :field instrumentModel:
    The instrument model used as part of this experiment. This maps to
    sequencing technology in BAM.
    
  :type instrumentModel: null|string
  :field instrumentDataFile:
    The data file generated by the instrument. TODO: This isn't actually a
    file is it? Should this be ``instrumentData`` instead?
    
  :type instrumentDataFile: null|string
  :field sequencingCenter:
    The sequencing center used as part of this experiment.
    
  :type sequencingCenter: null|string
  :field platformUnit:
    The platform unit used as part of this experiment. This is a
    flowcell-barcode or slide unique identifier.
    
  :type platformUnit: null|string
  :field info:
    A map of additional experiment information.
    
  :type info: map<array<string>>

  An experimental preparation of a ``Sample``.
  

.. avro:record:: Dataset

  :field id:
    The dataset's id, (at least) locally unique.
    
  :type id: string
  :field name:
    The name of the dataset.
    
  :type name: null|string
  :field description:
    Additional, human-readable information on the dataset.
    
  :type description: null|string

  A Dataset is a data-provider-specified collection of related data of
  multiple types. Logically, it's akin to a folder -- it's up to the
  provider what goes into the folder.
  
  For server implementors, they're a useful level of granularity for
  implementing administrative features such as access control (e.g.
  Dataset X is public; Dataset Y is only available to lab Z's
  collaborators) and billing (e.g. the costs of hosting Dataset Y should
  be charged to lab Z).
  
  For data curators, they're 'the simplest thing that could possibly work'
  for grouping data (e.g. Dataset X has all the reads, variants, and
  expression levels for a particular research project; Dataset Y has all
  the work product from a particular grant).
  
  For data accessors, they're a simple way to scope exploration and
  analysis (e.g. are there any supporting examples in 1000genomes? what's
  the distribution of that result in the data from our project?)
  

.. avro:record:: Program

  :field commandLine:
    The command line used to run this program.
    
  :type commandLine: null|string
  :field id:
    The user specified ID of the program.
    
  :type id: null|string
  :field name:
    The name of the program.
    
  :type name: null|string
  :field prevProgramId:
    The ID of the program run before this one.
    
  :type prevProgramId: null|string
  :field version:
    The version of the program run.
    
  :type version: null|string

.. avro:record:: ReadStats

  :field alignedReadCount:
    The number of aligned reads.
    
  :type alignedReadCount: null|long
  :field unalignedReadCount:
    The number of unaligned reads.
    
  :type unalignedReadCount: null|long
  :field baseCount:
    The total number of bases. This is equivalent to the sum of
    ``alignedSequence.length`` for all reads.
    
  :type baseCount: null|long

.. avro:record:: ReadGroup

  :field id:
    The read group ID.
    
  :type id: string
  :field datasetId:
    The ID of the dataset this read group belongs to.
    
  :type datasetId: null|string
  :field name:
    The read group name.
    
  :type name: null|string
  :field description:
    The read group description.
    
  :type description: null|string
  :field sampleId:
    The sample this read group's data was generated from.
    
  :type sampleId: null|string
  :field experiment:
    The experiment used to generate this read group.
    
  :type experiment: null|Experiment
  :field predictedInsertSize:
    The predicted insert size of this read group.
    
  :type predictedInsertSize: null|int
  :field created:
    The time at which this read group was created in milliseconds from the
    epoch.
    
  :type created: null|long
  :field updated:
    The time at which this read group was last updated in milliseconds from
    the epoch.
    
  :type updated: null|long
  :field stats:
    Statistical data on reads in this read group.
    
  :type stats: null|ReadStats
  :field programs:
    The programs used to generate this read group.
    
  :type programs: array<Program>
  :field referenceSetId:
    The reference set the reads in this read group are aligned to. Required
    if there are any read alignments.
    
  :type referenceSetId: null|string
  :field info:
    A map of additional read group information.
    
  :type info: map<array<string>>

.. avro:record:: ReadGroupSet

  :field id:
    The read group set ID.
    
  :type id: string
  :field datasetId:
    The ID of the dataset this read group set belongs to.
    
  :type datasetId: null|string
  :field name:
    The read group set name.
    
  :type name: null|string
  :field stats:
    Statistical data on reads in this read group set.
    
  :type stats: null|ReadStats
  :field readGroups:
    The read groups in this set.
    
  :type readGroups: array<ReadGroup>

.. avro:record:: LinearAlignment

  :field position:
    The position of this alignment.
    
  :type position: Position
  :field mappingQuality:
    The mapping quality of this alignment. Represents how likely the read
    maps to this position as opposed to other locations.
    
  :type mappingQuality: null|int
  :field cigar:
    Represents the local alignment of this sequence (alignment matches,
    indels, etc) versus the reference.
    
  :type cigar: array<CigarUnit>

  A linear alignment can be represented by one CIGAR string.
  

.. avro:record:: Fragment

  :field id:
    The fragment ID.
    
  :type id: string

  A fragment represents a contiguous stretch of a DNA or RNA molecule.
  Reads can be associated with a fragment to specify they derive from the
  same molecule.
  

.. avro:record:: ReadAlignment

  :field id:
    The read alignment ID. This ID is unique within the read group this
    alignment belongs to. This field may not be provided by all backends.
    Its intended use is to make caching and UI display easier for genome
    browsers and other light weight clients.
    
  :type id: null|string
  :field readGroupId:
    The ID of the read group this read belongs to. (Every read must belong
    to exactly one read group.)
    
  :type readGroupId: string
  :field fragmentId:
    The fragment ID that this ReadAlignment belongs to.
    
  :type fragmentId: string
  :field fragmentName:
    The fragment name. Equivalent to QNAME (query template name) in SAM.
    
  :type fragmentName: string
  :field properPlacement:
    The orientation and the distance between reads from the fragment are
    consistent with the sequencing protocol (equivalent to SAM flag 0x2)
    
  :type properPlacement: null|boolean
  :field duplicateFragment:
    The fragment is a PCR or optical duplicate (SAM flag 0x400)
    
  :type duplicateFragment: null|boolean
  :field numberReads:
    The number of reads in the fragment (extension to SAM flag 0x1)
    
  :type numberReads: null|int
  :field fragmentLength:
    The observed length of the fragment, equivalent to TLEN in SAM.
    
  :type fragmentLength: null|int
  :field readNumber:
    The read number in sequencing. 0-based and less than numberReads. This
    field replaces SAM flag 0x40 and 0x80.
    
  :type readNumber: null|int
  :field failedVendorQualityChecks:
    SAM flag 0x200
    
  :type failedVendorQualityChecks: null|boolean
  :field alignment:
    The alignment for this alignment record. This field will be null if the
    read is unmapped.
    
  :type alignment: null|LinearAlignment
  :field secondaryAlignment:
    Whether this alignment is secondary. Equivalent to SAM flag 0x100. A
    secondary alignment represents an alternative to the primary alignment
    for this read. Aligners may return secondary alignments if a read can
    map ambiguously to multiple coordinates in the genome.
    
    By convention, each read has one and only one alignment where both
    secondaryAlignment and supplementaryAlignment are false.
    
  :type secondaryAlignment: null|boolean
  :field supplementaryAlignment:
    Whether this alignment is supplementary. Equivalent to SAM flag 0x800.
    Supplementary alignments are used in the representation of a chimeric
    alignment. In a chimeric alignment, a read is split into multiple linear
    alignments that map to different reference contigs. The first linear
    alignment in the read will be designated as the representative
    alignment; the remaining linear alignments will be designated as
    supplementary alignments. These alignments may have different mapping
    quality scores.
    
    In each linear alignment in a chimeric alignment, the read will be hard
    clipped. The ``alignedSequence`` and ``alignedQuality`` fields in the
    alignment record will only represent the bases for its respective linear
    alignment.
    
  :type supplementaryAlignment: null|boolean
  :field alignedSequence:
    The bases of the read sequence contained in this alignment record.
    ``alignedSequence`` and ``alignedQuality`` may be shorter than the full
    read sequence and quality. This will occur if the alignment is part of a
    chimeric alignment, or if the read was trimmed. When this occurs, the
    CIGAR for this read will begin/end with a hard clip operator that will
    indicate the length of the excised sequence.
    
  :type alignedSequence: null|string
  :field alignedQuality:
    The quality of the read sequence contained in this alignment record.
    ``alignedSequence`` and ``alignedQuality`` may be shorter than the full
    read sequence and quality. This will occur if the alignment is part of a
    chimeric alignment, or if the read was trimmed. When this occurs, the
    CIGAR for this read will begin/end with a hard clip operator that will
    indicate the length of the excised sequence.
    
  :type alignedQuality: array<int>
  :field nextMatePosition:
    The mapping of the primary alignment of the
    ``(readNumber+1)%numberReads`` read in the fragment. It replaces mate
    position and mate strand in SAM.
    
  :type nextMatePosition: null|Position
  :field info:
    A map of additional read alignment information.
    
  :type info: map<array<string>>

  Each read alignment describes an alignment with additional information
  about the fragment and the read. A read alignment object is equivalent
  to a line in a SAM file.
  

