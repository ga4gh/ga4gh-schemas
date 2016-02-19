References
**********

Defines types used by the GA4GH References API.

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

.. avro:record:: Reference

  :field id:
    The reference ID. Unique within the repository.
  :type id: string
  :field length:
    The length of this reference's sequence.
  :type length: long
  :field md5checksum:
    The MD5 checksum uniquely representing this `Reference` as a lower-case
      hexadecimal string, calculated as the MD5 of the upper-case sequence
      excluding all whitespace characters (this is equivalent to SQ:M5 in SAM).
  :type md5checksum: string
  :field name:
    The name of this reference. (e.g. '22').
  :type name: string
  :field sourceURI:
    The URI from which the sequence was obtained. Specifies a FASTA format
      file/string with one name, sequence pair. In most cases, clients should call
      the `getReferenceBases()` method to obtain sequence bases for a `Reference`
      instead of attempting to retrieve this URI.
  :type sourceURI: null|string
  :field sourceAccessions:
    All known corresponding accession IDs in INSDC (GenBank/ENA/DDBJ) which must include
      a version number, e.g. `GCF_000001405.26`.
  :type sourceAccessions: array<string>
  :field isDerived:
    A sequence X is said to be derived from source sequence Y, if X and Y
      are of the same length and the per-base sequence divergence at A/C/G/T bases
      is sufficiently small. Two sequences derived from the same official
      sequence share the same coordinates and annotations, and
      can be replaced with the official sequence for certain use cases.
  :type isDerived: boolean
  :field sourceDivergence:
    The `sourceDivergence` is the fraction of non-indel bases that do not match the
      reference this record was derived from.
  :type sourceDivergence: null|float
  :field ncbiTaxonId:
    ID from http://www.ncbi.nlm.nih.gov/taxonomy (e.g. 9606->human).
  :type ncbiTaxonId: null|int

  A `Reference` is a canonical assembled contig, intended to act as a
  reference coordinate space for other genomic annotations. A single
  `Reference` might represent the human chromosome 1, for instance.
  
  `Reference`s are designed to be immutable.

.. avro:record:: ReferenceSet

  :field id:
    The reference set ID. Unique in the repository.
  :type id: string
  :field name:
    The reference set name.
  :type name: null|string
  :field md5checksum:
    Order-independent MD5 checksum which identifies this `ReferenceSet`.
    
      To compute this checksum, make a list of `Reference.md5checksum` for all
      `Reference`s in this set. Then sort that list, and take the MD5 hash of
      all the strings concatenated together. Express the hash as a lower-case
      hexadecimal string.
  :type md5checksum: string
  :field ncbiTaxonId:
    ID from http://www.ncbi.nlm.nih.gov/taxonomy (e.g. 9606->human) indicating
      the species which this assembly is intended to model. Note that contained
      `Reference`s may specify a different `ncbiTaxonId`, as assemblies may
      contain reference sequences which do not belong to the modeled species, e.g.
      EBV in a human reference genome.
  :type ncbiTaxonId: null|int
  :field description:
    Optional free text description of this reference set.
  :type description: null|string
  :field assemblyId:
    Public id of this reference set, such as `GRCh37`.
  :type assemblyId: null|string
  :field sourceURI:
    Specifies a FASTA format file/string.
  :type sourceURI: null|string
  :field sourceAccessions:
    All known corresponding accession IDs in INSDC (GenBank/ENA/DDBJ) ideally
      with a version number, e.g. `NC_000001.11`.
  :type sourceAccessions: array<string>
  :field isDerived:
    A reference set may be derived from a source if it contains
      additional sequences, or some of the sequences within it are derived
      (see the definition of `isDerived` in `Reference`).
  :type isDerived: boolean

  A `ReferenceSet` is a set of `Reference`s which typically comprise a
  reference assembly, such as `GRCh38`. A `ReferenceSet` defines a common
  coordinate space for comparing reference-aligned experimental data.

