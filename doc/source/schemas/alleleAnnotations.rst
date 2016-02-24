AlleleAnnotations
*****************

This protocol defines types used by the GA4GH Allele Annotation API.

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
    The experiment UUID. This is globally unique.
  :type id: string
  :field name:
    The name of the experiment.
  :type name: null|string
  :field description:
    A description of the experiment.
  :type description: null|string
  :field createDateTime:
    The time at which this record was created. 
      Format: :ref:`ISO 8601 <metadata_date_time>`
  :type createDateTime: string
  :field updateDateTime:
    The time at which this record was last updated.
      Format: :ref:`ISO 8601 <metadata_date_time>`
  :type updateDateTime: string
  :field runTime:
    The time at which this experiment was performed.
      Granularity here is variable (e.g. date only).
      Format: :ref:`ISO 8601 <metadata_date_time>`
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

.. avro:record:: Analysis

  :field id:
    Formats of id | name | description | accessions are described in the
      documentation on general attributes and formats.
  :type id: string
  :field name:
  :type name: null|string
  :field description:
  :type description: null|string
  :field createDateTime:
    The time at which this record was created. 
      Format: :ref:`ISO 8601 <metadata_date_time>`
  :type createDateTime: null|string
  :field updateDateTime:
    The time at which this record was last updated.
      Format: :ref:`ISO 8601 <metadata_date_time>`
  :type updateDateTime: string
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

.. avro:record:: AnalysisResult

  :field analysisId:
    The ID of the analysis record for this result
  :type analysisId: string
  :field result:
    The text-based result for this analysis
  :type result: null|string
  :field score:
    The numeric score for this analysis
  :type score: null|int

  An AnalysisResult record holds the output of a prediction package such
  as SIFT on a specific allele.

.. avro:record:: AlleleLocation

  :field start:
    Relative start position of the allele in this coordinate system
  :type start: int
  :field end:
    Relative end position of the allele in this coordinate system
  :type end: null|int
  :field referenceSequence:
    Reference sequence in feature (this should be the codon at CDS level)
  :type referenceSequence: null|string
  :field alternateSequence:
    Alternate sequence in feature (this should be the codon at CDS level)
  :type alternateSequence: null|string

  An allele location record holds the location of an allele relative to a
  non-genomic coordinate system such as a CDS or protein and holds the
  reference and alternate sequence where appropriate

.. avro:record:: VariantAnnotationSet

  :field id:
    The ID of the variant annotation set record
  :type id: string
  :field variantSetId:
    The ID of the variant set to which this annotation set belongs
  :type variantSetId: string
  :field name:
    The variant annotation set name.
  :type name: null|string
  :field analysis:
    Analysis details. It is essential to supply versions for all software and
      reference data used.
  :type analysis: Analysis

  A VariantAnnotationSet record groups VariantAnnotation records. It is derived
  from a VariantSet and holds information describing the software and reference
  data used in the annotation.

.. avro:record:: HGVSAnnotation

  :field genomic:
  :type genomic: null|string
  :field transcript:
  :type transcript: null|string
  :field protein:
  :type protein: null|string

  A HGVSAnnotation record holds Human Genome Variation Society descriptions
  of the sequence change with respect to genomic, transcript and protein
  sequences. See: http://www.hgvs.org/mutnomen/recs.html.
  Descriptions should be provided at genomic level. Descriptions at transcript
  level should be provided when the allele lies within a transcript. Descriptions
  at protein level should be provided when the allele lies within the translated
  sequence or stop codon.

.. avro:record:: TranscriptEffect

  :field id:
    The ID of the transcript effect record
  :type id: string
  :field featureId:
    The id of the transcript feature the annotation is relative to
  :type featureId: string
  :field alternateBases:
    Alternate allele - a variant may have more than one alternate allele,
      each of which will have distinct annotation.
  :type alternateBases: null|string
  :field effects:
    Effect of variant on this feature
  :type effects: array<OntologyTerm>
  :field hgvsAnnotation:
    Human Genome Variation Society variant descriptions
  :type hgvsAnnotation: HGVSAnnotation
  :field cDNALocation:
    Change relative to cDNA
  :type cDNALocation: null|AlleleLocation
  :field CDSLocation:
  :type CDSLocation: null|AlleleLocation
  :field proteinLocation:
    Change relative to protein
  :type proteinLocation: null|AlleleLocation
  :field analysisResults:
    Output from prediction packages such as SIFT
  :type analysisResults: array<AnalysisResult>

  A transcript effect record is a set of information describing the
  effect of an allele on a transcript

.. avro:record:: VariantAnnotation

  :field id:
    The ID of this VariantAnnotation.
  :type id: string
  :field variantId:
    The variant ID.
  :type variantId: string
  :field variantAnnotationSetId:
    The ID of the variant annotation set this record belongs to.
  :type variantAnnotationSetId: string
  :field createDateTime:
    The :ref:`ISO 8601 <metadata_date_time>` time at which this record was created.
  :type createDateTime: null|string
  :field transcriptEffects:
    The transcript effect annotation for the alleles of this variant. Each one
      represents the effect of a single allele on a single transcript.
  :type transcriptEffects: array<TranscriptEffect>
  :field info:
    Additional annotation data in key-value pairs.
  :type info: map<array<string>>

  A `VariantAnnotation` record represents the result of comparing a variant
  to a set of reference data.

