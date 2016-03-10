Variants
********

This file defines the objects used to represent variant calls, most importantly
VariantSet, Variant, and Call.
See {TODO: LINK TO VARIANTS OVERVIEW} for more information.

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

.. avro:record:: VariantSetMetadata

  :field key:
    The top-level key.
  :type key: string
  :field value:
    The value field for simple metadata.
  :type value: string
  :field id:
    User-provided ID field, not enforced by this API.
      Two or more pieces of structured metadata with identical
      id and key fields are considered equivalent.
      `FIXME: If it's not enforced, then why can't it be null?`
  :type id: string
  :field type:
    The type of data.
  :type type: string
  :field number:
    The number of values that can be included in a field described by this
      metadata.
  :type number: string
  :field description:
    A textual description of this metadata.
  :type description: string
  :field info:
    Remaining structured metadata key-value pairs.
  :type info: map<array<string>>

  Optional metadata associated with a variant set.

.. avro:record:: VariantSet

  :field id:
    The variant set ID.
  :type id: string
  :field name:
    The variant set name.
  :type name: null|string
  :field datasetId:
    The ID of the dataset this variant set belongs to.
  :type datasetId: string
  :field referenceSetId:
    The ID of the reference set that describes the sequences used by the variants in this set.
  :type referenceSetId: string
  :field metadata:
    Optional metadata associated with this variant set.
      This array can be used to store information about the variant set, such as information found
      in VCF header fields, that isn't already available in first class fields such as "name".
  :type metadata: array<VariantSetMetadata>

  A VariantSet is a collection of variants and variant calls intended to be analyzed together.

.. avro:record:: CallSet

  :field id:
    The call set ID.
  :type id: string
  :field name:
    The call set name.
  :type name: null|string
  :field sampleId:
    The sample this call set's data was generated from.
      Note: the current API does not have a rigorous definition of sample. Therefore, this
      field actually contains an arbitrary string, typically corresponding to the sampleId
      field in the read groups used to generate this call set.
  :type sampleId: null|string
  :field variantSetIds:
    The IDs of the variant sets this call set has calls in.
  :type variantSetIds: array<string>
  :field created:
    The date this call set was created in milliseconds from the epoch.
  :type created: null|long
  :field updated:
    The time at which this call set was last updated in
      milliseconds from the epoch.
  :type updated: null|long
  :field info:
    A map of additional call set information.
  :type info: map<array<string>>

  A CallSet is a collection of calls that were generated by the same analysis of the same sample.

.. avro:record:: Call

  :field callSetName:
    The name of the call set this variant call belongs to.
      If this field is not present, the ordering of the call sets from a
      `SearchCallSetsRequest` over this `VariantSet` is guaranteed to match
      the ordering of the calls on this `Variant`.
      The number of results will also be the same.
  :type callSetName: null|string
  :field callSetId:
    The ID of the call set this variant call belongs to.
    
      If this field is not present, the ordering of the call sets from a
      `SearchCallSetsRequest` over this `VariantSet` is guaranteed to match
      the ordering of the calls on this `Variant`.
      The number of results will also be the same.
  :type callSetId: null|string
  :field genotype:
    The genotype of this variant call.
    
      A 0 value represents the reference allele of the associated `Variant`. Any
      other value is a 1-based index into the alternate alleles of the associated
      `Variant`.
    
      If a variant had a referenceBases field of "T", an alternateBases
      value of ["A", "C"], and the genotype was [2, 1], that would mean the call
      represented the heterozygous value "CA" for this variant. If the genotype
      was instead [0, 1] the represented value would be "TA". Ordering of the
      genotype values is important if the phaseset field is present.
  :type genotype: array<int>
  :field phaseset:
    If this field is not null, this variant call's genotype ordering implies
      the phase of the bases and is consistent with any other variant calls on
      the same contig which have the same phaseset string.
  :type phaseset: null|string
  :field genotypeLikelihood:
    The genotype likelihoods for this variant call. Each array entry
      represents how likely a specific genotype is for this call as
      log10(P(data | genotype)), analogous to the GL tag in the VCF spec. The
      value ordering is defined by the GL tag in the VCF spec.
  :type genotypeLikelihood: array<double>
  :field info:
    A map of additional variant call information.
  :type info: map<array<string>>

  A `Call` represents the determination of genotype with respect to a
  particular `Variant`.
  
  It may include associated information such as quality
  and phasing. For example, a call might assign a probability of 0.32 to
  the occurrence of a SNP named rs1234 in a call set with the name NA12345.

.. avro:record:: Variant

  :field id:
    The variant ID.
  :type id: string
  :field variantSetId:
    The ID of the `VariantSet` this variant belongs to. This transitively defines
      the `ReferenceSet` against which the `Variant` is to be interpreted.
  :type variantSetId: string
  :field names:
    Names for the variant, for example a RefSNP ID.
  :type names: array<string>
  :field created:
    The date this variant was created in milliseconds from the epoch.
  :type created: null|long
  :field updated:
    The time at which this variant was last updated in
      milliseconds from the epoch.
  :type updated: null|long
  :field referenceName:
    The reference on which this variant occurs.
      (e.g. `chr20` or `X`)
  :type referenceName: string
  :field start:
    The start position at which this variant occurs (0-based).
      This corresponds to the first base of the string of reference bases.
      Genomic positions are non-negative integers less than reference length.
      Variants spanning the join of circular genomes are represented as
      two variants one on each side of the join (position 0).
  :type start: long
  :field end:
    The end position (exclusive), resulting in [start, end) closed-open interval.
      This is typically calculated by `start + referenceBases.length`.
  :type end: long
  :field referenceBases:
    The reference bases for this variant. They start at the given start position.
  :type referenceBases: string
  :field alternateBases:
    The bases that appear instead of the reference bases. Multiple alternate
      alleles are possible.
  :type alternateBases: array<string>
  :field info:
    A map of additional variant information.
  :type info: map<array<string>>
  :field calls:
    The variant calls for this particular variant. Each one represents the
      determination of genotype with respect to this variant. `Call`s in this array
      are implicitly associated with this `Variant`.
  :type calls: array<Call>

  A `Variant` represents a change in DNA sequence relative to some reference.
  For example, a variant could represent a SNP or an insertion.
  Variants belong to a `VariantSet`.
  This is equivalent to a row in VCF.

