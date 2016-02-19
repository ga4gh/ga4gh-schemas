ReadMethods
***********

 .. function:: searchReads(request)

  :param request: SearchReadsRequest: This request maps to the body of `POST /reads/search` as JSON.
  :return type: SearchReadsResponse
  :throws: GAException

Gets a list of `ReadAlignment`s for one or more `ReadGroup`s.

`searchReads` operates over a genomic coordinate space of reference sequence
and position defined by the `Reference`s to which the requested `ReadGroup`s are
aligned.

If a target positional range is specified, search returns all reads whose
alignment to the reference genome *overlap* the range. A query which specifies
only read group IDs yields all reads in those read groups, including unmapped
reads.

All reads returned (including reads on subsequent pages) are ordered by genomic
coordinate (by reference sequence, then position). Reads with equivalent genomic
coordinates are returned in an unspecified order. This order must be consistent
for a given repository, such that two queries for the same content (regardless
of page size) yield reads in the same order across their respective streams of
paginated responses.

`POST /reads/search` must accept a JSON version of `SearchReadsRequest` as
the post body and will return a JSON version of `SearchReadsResponse`.

 .. function:: searchReadGroupSets(request)

  :param request: SearchReadGroupSetsRequest: This request maps to the body of `POST /readgroupsets/search` as JSON.
  :return type: SearchReadGroupSetsResponse
  :throws: GAException

Gets a list of `ReadGroupSet` matching the search criteria.

`POST /readgroupsets/search` must accept a JSON version of
`SearchReadGroupSetsRequest` as the post body and will return a JSON
version of `SearchReadGroupSetsResponse`.

 .. function:: getReadGroupSet(id)

  :param id: string: The ID of the `ReadGroupSet`.
  :return type: org.ga4gh.models.ReadGroupSet
  :throws: GAException

Gets a `org.ga4gh.models.ReadGroupSet` by ID.
`GET /readgroupsets/{id}` will return a JSON version of `ReadGroupSet`.

 .. function:: getReadGroup(id)

  :param id: string: The ID of the `ReadGroup`.
  :return type: org.ga4gh.models.ReadGroup
  :throws: GAException

Gets a `org.ga4gh.models.ReadGroup` by ID.
`GET /readgroups/{id}` will return a JSON version of `ReadGroup`.

.. avro:enum:: Strand

  :symbols: NEG_STRAND|POS_STRAND
  Indicates the DNA strand associate for some data item.
  * `NEG_STRAND`: The negative (-) strand.
  * `POS_STRAND`:  The postive (+) strand.

.. avro:record:: Position

  :field referenceName:
    The name of the `Reference` on which the `Position` is located.
  :type referenceName: string
  :field position:
    The 0-based offset from the start of the forward strand for that `Reference`.
      Genomic positions are non-negative integers less than `Reference` length.
  :type position: long
  :field strand:
    Strand the position is associated with.
  :type strand: Strand

  A `Position` is an unoriented base in some `Reference`. A `Position` is
  represented by a `Reference` name, and a base number on that `Reference`
  (0-based).

.. avro:record:: ExternalIdentifier

  :field database:
    The source of the identifier.
      (e.g. `Ensembl`)
  :type database: string
  :field identifier:
    The ID defined by the external database.
      (e.g. `ENST00000000000`)
  :type identifier: string
  :field version:
    The version of the object or the database
      (e.g. `78`)
  :type version: string

  Identifier from a public database

.. avro:enum:: CigarOperation

  :symbols: ALIGNMENT_MATCH|INSERT|DELETE|SKIP|CLIP_SOFT|CLIP_HARD|PAD|SEQUENCE_MATCH|SEQUENCE_MISMATCH
  An enum for the different types of CIGAR alignment operations that exist.
  Used wherever CIGAR alignments are used. The different enumerated values
  have the following usage:
  
  * `ALIGNMENT_MATCH`: An alignment match indicates that a sequence can be
    aligned to the reference without evidence of an INDEL. Unlike the
    `SEQUENCE_MATCH` and `SEQUENCE_MISMATCH` operators, the `ALIGNMENT_MATCH`
    operator does not indicate whether the reference and read sequences are an
    exact match. This operator is equivalent to SAM's `M`.
  * `INSERT`: The insert operator indicates that the read contains evidence of
    bases being inserted into the reference. This operator is equivalent to
    SAM's `I`.
  * `DELETE`: The delete operator indicates that the read contains evidence of
    bases being deleted from the reference. This operator is equivalent to
    SAM's `D`.
  * `SKIP`: The skip operator indicates that this read skips a long segment of
    the reference, but the bases have not been deleted. This operator is
    commonly used when working with RNA-seq data, where reads may skip long
    segments of the reference between exons. This operator is equivalent to
    SAM's 'N'.
  * `CLIP_SOFT`: The soft clip operator indicates that bases at the start/end
    of a read have not been considered during alignment. This may occur if the
    majority of a read maps, except for low quality bases at the start/end of
    a read. This operator is equivalent to SAM's 'S'. Bases that are soft clipped
    will still be stored in the read.
  * `CLIP_HARD`: The hard clip operator indicates that bases at the start/end of
    a read have been omitted from this alignment. This may occur if this linear
    alignment is part of a chimeric alignment, or if the read has been trimmed
    (e.g., during error correction, or to trim poly-A tails for RNA-seq). This
    operator is equivalent to SAM's 'H'.
  * `PAD`: The pad operator indicates that there is padding in an alignment.
    This operator is equivalent to SAM's 'P'.
  * `SEQUENCE_MATCH`: This operator indicates that this portion of the aligned
    sequence exactly matches the reference (e.g., all bases are equal to the
    reference bases). This operator is equivalent to SAM's '='.
  * `SEQUENCE_MISMATCH`: This operator indicates that this portion of the
    aligned sequence is an alignment match to the reference, but a sequence
    mismatch (e.g., the bases are not equal to the reference). This can
    indicate a SNP or a read error. This operator is equivalent to SAM's 'X'.

.. avro:record:: CigarUnit

  :field operation:
    The operation type.
  :type operation: CigarOperation
  :field operationLength:
    The number of bases that the operation runs for.
  :type operationLength: long
  :field referenceSequence:
    `referenceSequence` is only used at mismatches (`SEQUENCE_MISMATCH`)
      and deletions (`DELETE`). Filling this field replaces the MD tag.
      If the relevant information is not available, leave this field as `null`.
  :type referenceSequence: null|string

  A structure for an instance of a CIGAR operation.
  `FIXME: This belongs under Reads (only readAlignment refers to this)`

.. avro:error:: GAException

  A general exception type.

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
    The time at which this record was created. 
      Format: ISO 8601, YYYY-MM-DDTHH:MM:SS.SSS (e.g. 2015-02-10T00:03:42.123Z)
  :type recordCreateTime: string
  :field recordUpdateTime:
    The time at which this record was last updated.
      Format: ISO 8601, YYYY-MM-DDTHH:MM:SS.SSS (e.g. 2015-02-10T00:03:42.123Z)
  :type recordUpdateTime: string
  :field runTime:
    The time at which this experiment was performed.
      Granularity here is variable (e.g. date only).
      Format: ISO 8601, YYYY-MM-DDTHH:MM:SS (e.g. 2015-02-10T00:03:42)
  :type runTime: null|string
  :field molecule:
    The molecule examined in this experiment. (e.g. genomics DNA, total RNA)
  :type molecule: null|string
  :field strategy:
    The experiment technique or strategy applied to the sample.
      (e.g. whole genome sequencing, RNA-seq, RIP-seq)
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
    The instrument model used as part of this experiment.
        This maps to sequencing technology in BAM.
  :type instrumentModel: null|string
  :field instrumentDataFile:
    The data file generated by the instrument.
      TODO: This isn't actually a file is it?
      Should this be `instrumentData` instead?
  :type instrumentDataFile: null|string
  :field sequencingCenter:
    The sequencing center used as part of this experiment.
  :type sequencingCenter: null|string
  :field platformUnit:
    The platform unit used as part of this experiment. This is a flowcell-barcode
      or slide unique identifier.
  :type platformUnit: null|string
  :field info:
    A map of additional experiment information.
  :type info: map<array<string>>

  An experimental preparation of a sample.

.. avro:record:: Dataset

  :field id:
    The dataset's id, locally unique to the server instance.
  :type id: string
  :field name:
    The name of the dataset.
  :type name: null|string
  :field description:
    Additional, human-readable information on the dataset.
  :type description: null|string

  A Dataset is a collection of related data of multiple types.
  Data providers decide how to group data into datasets.
  See [Metadata API](../api/metadata.html) for a more detailed discussion.

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

  Program can be used to track the provenance of how read data was generated.

.. avro:record:: ReadStats

  :field alignedReadCount:
    The number of aligned reads.
  :type alignedReadCount: null|long
  :field unalignedReadCount:
    The number of unaligned reads.
  :type unalignedReadCount: null|long
  :field baseCount:
    The total number of bases.
      This is equivalent to the sum of `alignedSequence.length` for all reads.
  :type baseCount: null|long

  ReadStats can be used to provide summary statistics about read data.

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
      Note: the current API does not have a rigorous definition of sample. Therefore, this
      field actually contains an arbitrary string, typically corresponding to the SM tag in a
      BAM file.
  :type sampleId: null|string
  :field experiment:
    The experiment used to generate this read group.
  :type experiment: null|Experiment
  :field predictedInsertSize:
    The predicted insert size of this read group.
  :type predictedInsertSize: null|int
  :field created:
    The time at which this read group was created in milliseconds from the epoch.
  :type created: null|long
  :field updated:
    The time at which this read group was last updated in milliseconds
      from the epoch.
  :type updated: null|long
  :field stats:
    Statistical data on reads in this read group.
  :type stats: null|ReadStats
  :field programs:
    The programs used to generate this read group.
  :type programs: array<Program>
  :field referenceSetId:
    The ID of the reference set to which the reads in this read group are aligned.
      Required if there are any read alignments.
  :type referenceSetId: null|string
  :field info:
    A map of additional read group information.
  :type info: map<array<string>>

  A ReadGroup is a set of reads derived from one physical sequencing process.

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

  A ReadGroupSet is a logical collection of ReadGroups. Typically one ReadGroupSet
  represents all the reads from one experimental sample.

.. avro:record:: LinearAlignment

  :field position:
    The position of this alignment.
  :type position: Position
  :field mappingQuality:
    The mapping quality of this alignment, meaning the likelihood that the read
      maps to this position.
    
      Specifically, this is -10 log10 Pr(mapping position is wrong), rounded to the
      nearest integer.
  :type mappingQuality: null|int
  :field cigar:
    Represents the local alignment of this sequence (alignment matches, indels, etc)
      versus the reference.
  :type cigar: array<CigarUnit>

  A linear alignment describes the alignment of a read to a Reference, using a
  position and CIGAR array.

.. avro:record:: ReadAlignment

  :field id:
    The read alignment ID. This ID is unique within the read group this
      alignment belongs to.
    
      For performance reasons, this field may be omitted by a backend.
      If provided, its intended use is to make caching and UI display easier for
      genome browsers and other lightweight clients.
  :type id: null|string
  :field readGroupId:
    The ID of the read group this read belongs to.
      (Every read must belong to exactly one read group.)
  :type readGroupId: string
  :field fragmentName:
    The fragment name. Equivalent to QNAME (query template name) in SAM.
  :type fragmentName: string
  :field properPlacement:
    The orientation and the distance between reads from the fragment are
      consistent with the sequencing protocol (equivalent to SAM flag 0x2)
  :type properPlacement: null|boolean
  :field duplicateFragment:
    The fragment is a PCR or optical duplicate (SAM flag 0x400).
  :type duplicateFragment: null|boolean
  :field numberReads:
    The number of reads in the fragment (extension to SAM flag 0x1)
  :type numberReads: null|int
  :field fragmentLength:
    The observed length of the fragment, equivalent to TLEN in SAM.
  :type fragmentLength: null|int
  :field readNumber:
    The read ordinal in the fragment, 0-based and less than numberReads. This
      field replaces SAM flag 0x40 and 0x80 and is intended to more cleanly
      represent multiple reads per fragment.
  :type readNumber: null|int
  :field failedVendorQualityChecks:
    The read fails platform or vendor quality checks (SAM flag 0x200).
  :type failedVendorQualityChecks: null|boolean
  :field alignment:
    The alignment for this alignment record. This field will be null if the read
      is unmapped.
  :type alignment: null|LinearAlignment
  :field secondaryAlignment:
    Whether this alignment is secondary. Equivalent to SAM flag 0x100.
      A secondary alignment represents an alternative to the primary alignment
      for this read. Aligners may return secondary alignments if a read can map
      ambiguously to multiple coordinates in the genome.
    
      By convention, each read has one and only one alignment where both
      secondaryAlignment and supplementaryAlignment are false.
  :type secondaryAlignment: null|boolean
  :field supplementaryAlignment:
    Whether this alignment is supplementary. Equivalent to SAM flag 0x800.
      Supplementary alignments are used in the representation of a chimeric
      alignment. In a chimeric alignment, a read is split into multiple
      linear alignments that map to different reference contigs. The first
      linear alignment in the read will be designated as the representative alignment;
      the remaining linear alignments will be designated as supplementary alignments.
      These alignments may have different mapping quality scores.
    
      In each linear alignment in a chimeric alignment, the read will be hard clipped.
      The `alignedSequence` and `alignedQuality` fields in the alignment record will
      only represent the bases for its respective linear alignment.
  :type supplementaryAlignment: null|boolean
  :field alignedSequence:
    The bases of the read sequence contained in this alignment record (equivalent
      to SEQ in SAM).
    
      `alignedSequence` and `alignedQuality` may be shorter than the full read sequence
      and quality. This will occur if the alignment is part of a chimeric alignment,
      or if the read was trimmed. When this occurs, the CIGAR for this read will
      begin/end with a hard clip operator that will indicate the length of the
      excised sequence.
  :type alignedSequence: null|string
  :field alignedQuality:
    The quality of the read sequence contained in this alignment record
      (equivalent to QUAL in SAM).
    
      `alignedSequence` and `alignedQuality` may be shorter than the full read sequence
      and quality. This will occur if the alignment is part of a chimeric alignment,
      or if the read was trimmed. When this occurs, the CIGAR for this read will
      begin/end with a hard clip operator that will indicate the length of the excised sequence.
  :type alignedQuality: array<int>
  :field nextMatePosition:
    The mapping of the primary alignment of the `(readNumber+1)%numberReads`
      read in the fragment. It replaces mate position and mate strand in SAM.
  :type nextMatePosition: null|Position
  :field info:
    A map of additional read alignment information.
  :type info: map<array<string>>

  Each read alignment describes an alignment with additional information
  about the fragment and the read. A read alignment object is equivalent to a
  line in a SAM file.

.. avro:record:: SearchReadsRequest

  :field readGroupIds:
    The ReadGroups to search. At least one id must be specified.
  :type readGroupIds: array<string>
  :field referenceId:
    The reference to query. Leaving blank returns results from all
      references, including unmapped reads - this could be very large.
  :type referenceId: null|string
  :field start:
    The start position (0-based) of this query.
      If a reference is specified, this defaults to 0.
      Genomic positions are non-negative integers less than reference length.
      Requests spanning the join of circular genomes are represented as
      two requests one on each side of the join (position 0).
  :type start: null|long
  :field end:
    The end position (0-based, exclusive) of this query.
      If a reference is specified, this defaults to the
      reference's length.
  :type end: null|long
  :field pageSize:
    Specifies the maximum number of results to return in a single page.
      If unspecified, a system default will be used.
  :type pageSize: null|int
  :field pageToken:
    The continuation token, which is used to page through large result sets.
      To get the next page of results, set this parameter to the value of
      `nextPageToken` from the previous response.
  :type pageToken: null|string

  This request maps to the body of `POST /reads/search` as JSON.
  
  If a reference is specified, all queried `ReadGroup`s must be aligned
  to `ReferenceSet`s containing that same `Reference`. If no reference is
  specified, all queried `ReadGroup`s must be aligned to the same `ReferenceSet`.

.. avro:record:: SearchReadsResponse

  :field alignments:
    The list of matching alignment records, sorted by position.
      Unmapped reads, which have no position, are returned last.
  :type alignments: array<org.ga4gh.models.ReadAlignment>
  :field nextPageToken:
    The continuation token, which is used to page through large result sets.
      Provide this value in a subsequent request to return the next page of
      results. This field will be empty if there aren't any additional results.
  :type nextPageToken: null|string

  This is the response from `POST /reads/search` expressed as JSON.

.. avro:record:: SearchReadGroupSetsRequest

  :field datasetId:
    The dataset to search.
  :type datasetId: string
  :field name:
    Only return read group sets with this name (case-sensitive, exact match).
  :type name: null|string
  :field pageSize:
    Specifies the maximum number of results to return in a single page.
      If unspecified, a system default will be used.
  :type pageSize: null|int
  :field pageToken:
    The continuation token, which is used to page through large result sets.
      To get the next page of results, set this parameter to the value of
      `nextPageToken` from the previous response.
  :type pageToken: null|string

  This request maps to the body of `POST /readgroupsets/search` as JSON.
  
  TODO: Factor this out to a common API patterns section.
  - If searching by a resource ID, and that resource is not found, the method
  will return a `404` HTTP status code (`NOT_FOUND`).
  - If searching by other attributes, e.g. `name`, and no matches are found, the
  method will return a `200` HTTP status code (`OK`) with an empty result list.

.. avro:record:: SearchReadGroupSetsResponse

  :field readGroupSets:
    The list of matching read group sets.
  :type readGroupSets: array<org.ga4gh.models.ReadGroupSet>
  :field nextPageToken:
    The continuation token, which is used to page through large result sets.
      Provide this value in a subsequent request to return the next page of
      results. This field will be empty if there aren't any additional results.
  :type nextPageToken: null|string

  This is the response from `POST /readgroupsets/search` expressed as JSON.

