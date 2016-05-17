Metadata
********

TODO:
  - id discussion
  - How to represent trios, twins, etc. See PGP data to drive this.
  - Explicit temporal sample relationships or samplingDate sufficient?
  - standardize name/description/notes/key-value data types
  - VERY IMPORTANT data/time of record goes to the issue of what are the
    objects and what is the data model. Is it containment or relational.
    Are we building a data model or a exchange format without knowing
    the data model.
  - should every field be prefixed by `ontology*'

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

.. avro:record:: OntologyTerm

  :field id:
    Ontology source identifier - the identifier, a CURIE (preferred) or
      PURL for an ontology source e.g. http://purl.obolibrary.org/obo/hp.obo
      It differs from the standard GA4GH schema's :ref:`id <apidesign_object_ids>`
      in that it is a URI pointing to an information resource outside of the scope
      of the schema or its resource implementation.
  :type id: string
  :field term:
    Ontology term - the representation the id is pointing to.
  :type term: null|string
  :field sourceName:
    Ontology source name - the name of ontology from which the term is obtained
      e.g. 'Human Phenotype Ontology'
  :type sourceName: null|string
  :field sourceVersion:
    Ontology source version - the version of the ontology from which the
      OntologyTerm is obtained; e.g. 2.6.1.
      There is no standard for ontology versioning and some frequently
      released ontologies may use a datestamp, or build number.
  :type sourceVersion: null|string

  An ontology term describing an attribute. (e.g. the phenotype attribute
    'polydactyly' from HPO)

.. avro:record:: Experiment

  :field id:
    The experiment id. This is at least locally unique.
  :type id: string
  :field name:
    The name of the experiment.
  :type name: null|string
  :field description:
    A description of the experiment.
  :type description: null|string
  :field created:
    The time at which this record was created.
      Format: :ref:`ISO 8601 <metadata_date_time>`
  :type created: string
  :field updated:
    The time at which this record was last updated.
      Format: :ref:`ISO 8601 <metadata_date_time>`
  :type updated: string
  :field runTime:
    The time at which this experiment was performed.
      Granularity here is variable (e.g. date only).
      Format: :ref:`ISO 8601 <metadata_date_time>`
  :type runTime: null|string
  :field molecule:
    The molecule examined in this experiment. (e.g. genomic DNA, total RNA)
  :type molecule: null|string
  :field strategy:
    The general experiment technique or strategy applied to the sample.
        (e.g. whole genome sequencing, RNA-seq, RIP-seq, SNP array)
  :type strategy: null|string
  :field platformName:
    A descriptive name of the technology platform.
        Example: Illumina HiSeq
  :type platformName: null|string
  :field platformId:
    A platform identifier which corresponds to a locally controlled vocabulary.
        Example: "GPL6801" in the context of GEO
  :type platformId: null|string
  :field selection:
    The method used to enrich the target. (e.g. immunoprecipitation, size
        fractionation, MNase digestion)
  :type selection: null|string
  :field preparationId:
    The ID of the library or other labeled preparation used in this experiment.
  :type preparationId: null|string
  :field instrumentModel:
    The instrument model used for this experiment.
        FIXIT: Does this map to sequencing technology in BAM?
  :type instrumentModel: null|string
  :field instrumentDataFile:
    The data file generated by the instrument.
        FIXIT: Should probably be a pointer to an object ID; storage as file should
        not be coded in.
  :type instrumentDataFile: null|string
  :field processingFacility:
    The facility where this experiment was performed.
        FIXIT: Systematic way to identify facilities?
  :type processingFacility: null|string
  :field info:
    A map of additional information.
  :type info: map<array<string>>

  A technical procedure performed on (pre-processed, labeled ...) material
    (DNA, RNA, protein extraction) derived from a single or a mix of BioSamples.
    FIXIT:
    - Would Assay be a better name?

.. avro:record:: Dataset

  :field id:
    Formats of id | name | description | accessions are described in the
        documentation on general attributes and formats.
  :type id: string
  :field name:
  :type name: null|string
  :field description:
  :type description: null|string
  :field accessions:
  :type accessions: array<string>

  A Dataset is a collection of related data of multiple types.
    Data providers decide how to group data into datasets.
    See [Metadata API](../api/metadata.html) for a more detailed discussion.

.. avro:record:: IndividualGroup

  :field id:
    Formats of id | name | description | accessions are described in the
        documentation on general attributes and formats.
  :type id: string
  :field name:
  :type name: null|string
  :field description:
  :type description: null|string
  :field accessions:
  :type accessions: array<string>
  :field created:
    The times at which this record was created / updated.
        Format: ISO 8601 (cf. documentation on time formats)
  :type created: string
  :field updated:
  :type updated: string
  :field memberIds:
    Group member ids.
  :type memberIds: array<string>
  :field type:
    The type of individual group.
  :type type: null|string
  :field info:
    A map of additional information.
  :type info: map<array<string>>

  Represents a group of individuals. (e.g. a trio)
    TODO: review, this clearly define how this works.  Need an list of
    individuals.  Needs typed.
    TODO: how does matchmaker group them?
    https://github.com/MatchmakerExchange/mme-apis/blob/master/search-api.md

.. avro:record:: Analysis

  :field id:
    Formats of id | name | description | accessions are described in the
        documentation on general attributes and formats.
  :type id: string
  :field name:
  :type name: null|string
  :field description:
  :type description: null|string
  :field accessions:
  :type accessions: array<string>
  :field created:
    The times at which this record was created / updated.
        Format: ISO 8601 (cf. documentation on time formats)
  :type created: string
  :field updated:
  :type updated: string
  :field type:
    The type of analysis.
  :type type: null|string
  :field bioSampleIds:
  :type bioSampleIds: array<string>
  :field experimentIds:
  :type experimentIds: array<string>
  :field software:
    The software run to generate this analysis.
  :type software: array<string>
  :field info:
    A map of additional information.
  :type info: map<array<string>>

  An analysis contains an interpretation of one or several experiments.
    (e.g. SNVs, copy number variations, methylation status) together with
    information about the methodology used.
    TODO: review

.. avro:record:: Analysis

  :field id:
    Formats of id | name | description | accessions are described in the
      documentation on general attributes and formats.
  :type id: string
  :field name:
  :type name: null|string
  :field description:
  :type description: null|string
  :field created:
    The time at which this record was created.
      Format: :ref:`ISO 8601 <metadata_date_time>`
  :type created: null|string
  :field updated:
    The time at which this record was last updated.
      Format: :ref:`ISO 8601 <metadata_date_time>`
  :type updated: string
  :field type:
    The type of analysis.
  :type type: null|string
  :field software:
    The software run to generate this analysis.
  :type software: array<string>
  :field info:
    A map of additional analysis information.
  :type info: map<array<string>>

  An analysis contains an interpretation of one or several experiments.
  (e.g. SNVs, copy number variations, methylation status) together with
  information about the methodology used.
