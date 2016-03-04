BiodataMethods
**************

 .. function:: searchBiosamples(request)

  :param request: SearchBioSamplesRequest: This request maps to the body of `POST /biosamples/search` as JSON.
  :return type: SearchBioSamplesResponse
  :throws: GAException

Gets a list of BioSamples accessible through the API.

`POST /biosamples/search` must accept a JSON version of
`SearchDatasetsRequest` as the post body and will return a JSON version
of `SearchDatasetsResponse`.

 .. function:: getBioSample(id)

  :param id: string: The ID of the `BioSample`.
  :return type: org.ga4gh.models.BioSample
  :throws: GAException

Gets a `BioSample` by ID.
`GET /BioSample/{id}` will return a JSON version of `BioSample`.

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

.. avro:record:: OntologyTerm

  :field id:
    :ref:`Ontology<metadata_ontologies>` source identifier -
      the identifier, a CURIE (preferred) or PURL for an ontology source.
      Example: http://purl.obolibrary.org/obo/hp.obo
      It differs from the standard GA4GH schema's :ref:`id <apidesign_object_ids>`
      in that it is a URI pointing to an information resource outside of the scope
      of the schema or its resource implementation.
  :type id: string
  :field term:
    Ontology term - the representation the id is pointing to.
  :type term: null|string
  :field value:
    Ontology value - In the case of using e.g. UnitOntology, the id/term represent
      a unit of measurement and this would be the measured value.
  :type value: null|string
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

.. avro:error:: GAException

  A general exception type.

.. avro:record:: BioSample

  :field id:
    The BioSample :ref:`id <apidesign_object_ids>`. This is unique in the
       context of the server instance.
  :type id: string
  :field name:
    The BioSample's :ref:`name <apidesign_object_names>`. This is a label or
       symbolic identifier for the biosample.
  :type name: null|string
  :field description:
    The biosample's description. This attribute contains human readable text.
       The "description" attributes should not contain any structured data.
  :type description: null|string
  :field disease:
    Disease annotation of the sample.
  :type disease: null|OntologyTerm
  :field createDateTime:
    The :ref:`ISO 8601<metadata_date_time> time at which this BioSample record
       was created.
  :type createDateTime: string
  :field updateDateTime:
    The :ref:`ISO 8601<metadata_date_time> time at which this BioSample record was updated.
  :type updateDateTime: string
  :field info:
    A map of additional information.
  :type info: map<array<string>>

  A BioSample refers to a unit of biological material from which the substrate
    molecules (e.g. genomic DNA, RNA, proteins) for molecular analyses (e.g.
    sequencing, array hybridisation, mass-spectrometry) are extracted. Examples
    would be a tissue biopsy, a single cell from a culture for single cell genome
    sequencing or a protein fraction from a gradient centrifugation.
    Several instances (e.g. technical replicates) or types of experiments (e.g.
    genomic array as well as RNA-seq experiments) may refer to the same BioSample.
    In the context of the GA4GH metadata schema, BioSample constitutes the central
    reference object.

.. avro:record:: SearchBioSamplesRequest

  :field datasetId:
  :type datasetId: string
  :field name:
  :type name: null|string
  :field pageSize:
  :type pageSize: null|int
  :field pageToken:
  :type pageToken: null|string

  This request maps to the body of `POST /biosamples/search` as JSON.

.. avro:record:: SearchBioSamplesResponse

  :field biosamples:
    The list of biosamples.
  :type biosamples: array<org.ga4gh.models.BioSample>
  :field nextPageToken:
    The continuation token, which is used to page through large result sets.
      Provide this value in a subsequent request to return the next page of
      results. This field will be empty if there aren't any additional results.
  :type nextPageToken: null|string

  This is the response from `POST /biosamples/search` expressed as JSON.

