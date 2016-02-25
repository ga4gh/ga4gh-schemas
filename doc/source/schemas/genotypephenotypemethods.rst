GenotypePhenotypeMethods
************************

This protocol defines genotype to phenotype association
query system.

Suggested ontologies used in type-based queries include:

Phenotype:
Human Phenotype Ontology (HPO): http://www.ontobee.org/browser/index.php?o=hp
Disease Ontology (DO): http://purl.obolibrary.org/obo/DOID_4

Feature:
Sequence Ontology (SO): http://www.sequenceontology.org/browser/

Evidence:
Evidence Code Ontology (ECO): http://www.ontobee.org/browser/index.php?o=ECO
Ontology for Biomedical Investigations (OBI): http://purl.obofoundry.org/obo/obi/browse

 .. function:: searchPhenotypeAssociationSets(request)

  :param request: SearchPhenotypeAssociationSetsRequest: This request maps to the body of `POST /phenotypeassociationsets/search` as JSON.
  :return type: SearchPhenotypeAssociationSetsResponse
  :throws: GAException

Gets a list of `PhenotypeAssociationSet`s matching the search criteria.

`POST /phenotypeassociationsets/search` must accept a JSON version of
`SearchPhenotypeAssociationSetsRequest` as the post body and will return a JSON version
of `SearchPhenotypeAssociationSetsResponse`.

 .. function:: searchGenotypePhenotype(request)

  :param request: SearchGenotypePhenotypeRequest: This request maps to the body of `POST /genotypepheotype/search` as JSON.
  :return type: SearchGenotypePhenotypeResponse
  :throws: GAException

Gets a list of evidence accessible through the API.

`POST /genotypephenotype/search` must accept a JSON version of
`SearchGenotypePhenotypeRequest` as the post body and will return a JSON version
of `SearchGenotypePhenotypeResponse`.

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

  An experimental preparation of a `Sample`.

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

.. avro:record:: Attributes

  :field vals:
  :type vals: map<array<string|ExternalIdentifier|OntologyTerm>>

  Type defining a collection of attributes associated with various protocol
    records.  Each attribute is a name that maps to an array of one or more
    values.  Values can be strings, external identifiers, or ontology terms.
    Values should be split into the array elements instead of using a separator
    syntax that needs to parsed.

.. avro:record:: Feature

  :field id:
    Id of this annotation node.
  :type id: string
  :field parentId:
    Parent Id of this node. Set to empty string if node has no parent.
  :type parentId: string
  :field childIds:
    Ordered array of Child Ids of this node.
        Since not all child nodes are ordered by genomic coordinates,
        this can't always be reconstructed from parentId's of the children alone.
  :type childIds: array<string>
  :field featureSetId:
    Identifier for the containing feature set.
  :type featureSetId: string
  :field referenceName:
    The reference on which this feature occurs.
        (e.g. `chr20` or `X`)
  :type referenceName: string
  :field start:
    The start position at which this feature occurs (0-based).
        This corresponds to the first base of the string of reference bases.
        Genomic positions are non-negative integers less than reference length.
        Features spanning the join of circular genomes are represented as
        two features one on each side of the join (position 0).
  :type start: long
  :field end:
    The end position (exclusive), resulting in [start, end) closed-open interval.
        This is typically calculated by `start + referenceBases.length`.
  :type end: long
  :field strand:
    The strand on which the feature is present.
  :type strand: Strand
  :field featureType:
    Feature that is annotated by this region.  Normally, this will be a term in
        the Sequence Ontology.
  :type featureType: OntologyTerm
  :field attributes:
    Name/value attributes of the annotation.  Attribute names follow the GFF3
        naming convention of reserved names starting with an upper cases
        character, and user-define names start with lower-case.  Most GFF3
        pre-defined attributes apply, the exceptions are ID and Parent, which are
        defined as fields. Additional, the following attributes are added:
        * Score - the GFF3 score column
        * Phase - the GFF3 phase column for CDS features.
  :type attributes: Attributes

  Node in the annotation graph that annotates a contiguous region of a
    sequence.

.. avro:record:: FeatureSet

  :field id:
    The ID of this annotation set.
  :type id: string
  :field datasetId:
    The ID of the dataset this annotation set belongs to.
  :type datasetId: null|string
  :field referenceSetId:
    The ID of the reference set which defines the coordinate-space for this
        set of annotations.
  :type referenceSetId: null|string
  :field name:
    The display name for this annotation set.
  :type name: null|string
  :field sourceURI:
    The source URI describing the file from which this annotation set was
        generated, if any.
  :type sourceURI: null|string
  :field info:
    Remaining structured metadata key-value pairs.
  :type info: map<array<string>>

.. avro:record:: PhenotypeAssociationSet

  :field id:
    The phenotype association set ID.
  :type id: string
  :field name:
    The phenotype association set name.
  :type name: null|string
  :field datasetId:
    The ID of the dataset this phenotype association set belongs to.
  :type datasetId: string
  :field info:
    Optional additional information for this phenotype association set.
  :type info: map<array<string>>

  A PhenotypeAssociationSet is a collection of phenotype association results. 
  Such results are grouped by data source and possibly release version or analysis 
  type.

.. avro:record:: EnvironmentalContext

  :field id:
    The Environment ID.
  :type id: null|string
  :field environmentType:
    Examples of some environment types could be drawn from:
      Ontology for Biomedical Investigations (OBI): http://purl.obofoundry.org/obo/obi/browse
      Chemical Entities of Interest (ChEBI): http://www.ontobee.org/browser/index.php?o=chebi
      Environment Ontology (ENVO):  http://www.ontobee.org/browser/index.php?o=ENVO
      Anatomy (Uberon): http://www.ontobee.org/browser/index.php?o=uberon
  :type environmentType: OntologyTerm
  :field description:
    A textual description of the environment. This is used to complement 
    	the structured description in the environmentType field
  :type description: null|string

  The context in which a genotype gives rise to a phenotype.
  This is fairly open-ended; as a stub we have a simple ontology term.
  For example, a controlled term for a drug, or perhaps an instance of a 
  complex environment including temperature and air quality, or perhaps
  the anatomical environment (gut vs tissue type vs whole organism).

.. avro:record:: PhenotypeInstance

  :field id:
    The Phenotype ID.
  :type id: null|string
  :field type:
    HPO is recommended
  :type type: OntologyTerm
  :field qualifier:
    PATO is recommended.  Often this qualifier might be for abnormal/normal, 
      or severity.
      For example, severe: http://purl.obolibrary.org/obo/PATO_0000396 
      or abnormal: http://purl.obolibrary.org/obo/PATO_0000460
  :type qualifier: null|array<OntologyTerm>
  :field ageOfOnset:
    HPO is recommended, for example, subclasses of
      http://purl.obolibrary.org/obo/HP_0011007
  :type ageOfOnset: null|OntologyTerm
  :field description:
    A textual description of the phenotype. This is used to complement the 
      structured phenotype description in the type field.
  :type description: null|string

  An association to a phenotype and related information.
  This record is intended primarily to be used in conjunction with variants, but 
  the record can also be composed with other kinds of entities such as diseases

.. avro:record:: Evidence

  :field evidenceType:
    ECO or OBI is recommended
  :type evidenceType: OntologyTerm
  :field description:
    A textual description of the evidence. This is used to complement the 
    	structured description in the evidenceType field
  :type description: null|string

  Evidence for the phenotype association.
  This is also a stub for further expansion.  We should consider moving this into 
  it's own schema.

.. avro:record:: FeaturePhenotypeAssociation

  :field id:
  :type id: string
  :field phenotypeAssociationId:
    The ID of the PhenotypeAssociationSet this FeaturePhenotypeAssociation
      belongs to.
  :type phenotypeAssociationId: string
  :field features:
    The set of features of the organism that bears the phenotype.
        This could be as complete as a full complement of variants,
        or as minimal as the confirmed variants that are known causation
        for the annotated phenotype.  
        Examples of features could be variations at the nucleotide level, 
        large rearrangements at the chromosome level, or relevant epigenetic
        markers.  Relevant genomic feature types are suggested to be 
        those typed in the Sequence Ontology (SO).
    
        The feature set can have only one item, and must not be null.
  :type features: array<Feature>
  :field evidence:
    The evidence for this specific instance of association between the
        features and the phenotype.
  :type evidence: array<Evidence>
  :field phenotype:
    The phenotypic component of this association.
        Note that we delegate this to a separate record to allow us the flexibility 
    	to composition of phenotype associations with records that are not 
    	variant sets - for example, diseases.
  :type phenotype: PhenotypeInstance
  :field description:
    A textual description of the association.
  :type description: null|string
  :field environmentalContexts:
    The context in which the phenotype arises.
      Multiple contexts can be specified - these are assumed to all hold together
  :type environmentalContexts: array<EnvironmentalContext>

  An association between one or more genomic features and a phenotype.
  The instance of association allows us to link a feature to a phenotype,
  multiple times, each bearing potentially different levels of confidence,
  such as resulting from alternative experiments and analysis.

.. avro:error:: GAException

  A general exception type.

.. avro:record:: SearchPhenotypeAssociationSetsRequest

  :field datasetId:
    The `Dataset` to search.
  :type datasetId: string
  :field pageSize:
    Specifies the maximum number of results to return in a single page.
      If unspecified, a system default will be used.
  :type pageSize: null|int
  :field pageToken:
    The continuation token, which is used to page through large result sets.
      To get the next page of results, set this parameter to the value of
      `nextPageToken` from the previous response.
  :type pageToken: null|string

  This request maps to the body of `POST /phenotypeassociationsets/search` as JSON.

.. avro:record:: SearchPhenotypeAssociationSetsResponse

  :field phenotypeAssociationSets:
    The list of matching phenotype association sets.
  :type phenotypeAssociationSets: array<org.ga4gh.models.PhenotypeAssociationSet>
  :field nextPageToken:
    The continuation token, which is used to page through large result sets.
      Provide this value in a subsequent request to return the next page of
      results. This field will be empty if there aren't any additional results.
  :type nextPageToken: null|string

  This is the response from `POST /phenotypeassociationsets/search` expressed as JSON.

.. avro:record:: EvidenceQuery

  :field evidenceType:
    ECO or OBI is recommended
  :type evidenceType: array<org.ga4gh.models.OntologyTerm>

  Evidence for the phenotype association.

.. avro:record:: GenomicFeatureQuery

  :field features:
  :type features: array<org.ga4gh.models.Feature>

  The feature collection to search for.  One or more features (variants,
  genes, etc) can be specified.  The idea here is that if a
  query is for a gene, then any alleles to that gene for which
  there are annotation records would be returned.

.. avro:record:: PhenotypeQuery

  :field phenotypes:
  :type phenotypes: array<org.ga4gh.models.PhenotypeInstance>

  One or more phenotypes can be queried together.

.. avro:record:: OntologyTermQuery

  :field terms:
  :type terms: array<org.ga4gh.models.OntologyTerm>

  One or more ontology terms can be queried together.

.. avro:record:: ExternalIdentifierQuery

  :field ids:
  :type ids: array<org.ga4gh.models.ExternalIdentifier>

  One or more ids can be queried together.  Generally used for instances
  of a particular class of object (e.g. a specific gene or SNP).

.. avro:record:: SearchGenotypePhenotypeRequest

  :field phenotypeAssociationSetId:
    The `PhenotypeAssociationSet` to search.
  :type phenotypeAssociationSetId: string
  :field feature:
  :type feature: null|string|ExternalIdentifierQuery|OntologyTermQuery|GenomicFeatureQuery
  :field phenotype:
  :type phenotype: null|string|ExternalIdentifierQuery|OntologyTermQuery|PhenotypeQuery
  :field evidence:
  :type evidence: null|string|ExternalIdentifierQuery|OntologyTermQuery|EvidenceQuery
  :field pageSize:
    Specifies the maximum number of results to return in a single page.
      If unspecified, a system default will be used.
  :type pageSize: null|int
  :field pageToken:
    The continuation token, which is used to page through large result sets.
      To get the next page of results, set this parameter to the value of
      `nextPageToken` from the previous response.
  :type pageToken: null|string

  This request maps to the body of `POST /genotypephenotype/search` as JSON.
  
  The goal here is to allow users to query using one or more of
  Genotype, Phenotype, Environment, and Evidence.
  
  A query using one of the above items is to mean, by default,
  that the remainder of the query is as a "wildcard", such
  that all matches to just that query term would come back.
  Combinations of the above are to act like AND rather than OR.
  
  The "genotype" part of the query methods can be one or more
  genomic features.  Associations can be made at many
  levels of granularity (from whole genotypes down to individual
  SNVs), but users may use these methods with partial or
  inexact information.  Therefore, the query methods must be
  able to support query of some or all of the associated features.
  Furthermore, use of the relationships between genomic features
  means that when querying for a gene, any variants to that
  gene are also returned.  For example, a query with
  BRCA2 would mean that in addition to any direct associations
  to the BRCA2, all associations to sequence variants of BRCA2 would also
  be returned.  Similarly, queries with OntologyTerms should perform
  the subclass closure.
  
  Each query can be made against a string, an array of external
  identifers (such as for gene or SNP ids), ontology term ids, or
  full feature/phenotype/evidence objects.

.. avro:record:: SearchGenotypePhenotypeResponse

  :field associations:
    The list of matching FeaturePhenotypeAssociation.
  :type associations: array<org.ga4gh.models.FeaturePhenotypeAssociation>
  :field nextPageToken:
    The continuation token, which is used to page through large result sets.
      Provide this value in a subsequent request to return the next page of
      results. This field will be empty if there aren't any additional results.
  :type nextPageToken: null|string

  This is the response from `POST /genotypephenotype/search` expressed as JSON.

