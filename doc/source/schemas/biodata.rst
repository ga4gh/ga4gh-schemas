Biodata
*******

This protocol defines the "biodata" objects, which can be considered data
representations of biological correlates.

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

.. avro:record:: Disease

  :field disease:
    The diagnosis, defined through an OntologyTerm.
  :type disease: OntologyTerm
  :field stageAtDiagnosis:
    The stage of the disease at diagnosis. This is not updated to reflect
        progression of the disease, which is recorded in the clinical data.
        e.g. OntologyTerm representation for stage T2N1M0.
  :type stageAtDiagnosis: null|OntologyTerm
  :field ageOfOnset:
    Age of onset of the disease in ISO 8601 duration PnYnMnDTnHnMnS
        in a suitable approximation
        Example: P47Y08M (47 years, 8 months)
  :type ageOfOnset: null|string
  :field dateTimeDiagnosis:
    Date the diagnosis was made/assigned. This is NOT when the record was
        created.
        Format: ISO 8601 (cf. documentation on time formats)
  :type dateTimeDiagnosis: null|string

  Representation of a disease. The object should in minimal version report the
    kind of the disease and a temporal parameter.
  
    The "Disease" object is not intended to represent extended clinical records,
    but as a basic representation of the most relevant attributes in the context
    of the study at hand.
  
    GA4GH metadata does not attempt to encode detailed phenotypes of the disease
    or longitudinal concepts. Association of diseases and disease phenotypes
    (e.g Li-Fraumeni syndrome and resulting malignancies) is complex and left to
    external processes utilizing GA4GH type records in combination with medical
    information systems.
  
    TODO:
      - need to link to clinical data. Reference to clinical working group
      - need keyword/value table, also human notes

.. avro:record:: Phenotype

  :field phenotype:
    The phenotype, defined through an OntologyTerm.
  :type phenotype: OntologyTerm
  :field ageOfOnset:
    Age of onset of the phenotype.
        TODO: need to define format (see Disease)
  :type ageOfOnset: null|string
  :field dateTimeIdentified:
    Date the phenotype was identified/assigned.
        Format: ISO 8601 (cf. documentation on time formats)
  :type dateTimeIdentified: null|string

  Record of phenotypes observed in an individual, which maybe independent of a
    disease diagnosis.
    Phenotype-disease links are complex and as this is a process
    performed by clinicians, presentations can be atypical and phenotypes
    unrelated to an individual diagnosis may be present.
    We also want to record phenotypes in the absences of a diagnosis.
  
    TODO:
      - need to link to clinical data. Reference to clinical working group
      - need keyword/value table, also human notes

.. avro:record:: Observation

  :field id:
    The id of the observation. This is facultative and allows the use of
        "relationship objects" to assign e.g. evidence levels between an observation
        and e.g. a phenotype object.
        Format: UUIDv4 recommended
  :type id: null|string
  :field observation:
    The type of the observation.
  :type observation: OntologyTerm
  :field value:
    The value of the observation.
  :type value: OntologyTerm
  :field unit:
    The unit of the observation; e.g. for numeric values.
  :type unit: null|string
  :field dateTimeObserved:
    Date the observation was made/assigned (e.g. date of diagnosis, observation
        of phenotype...). Suitable e.g. for health related purposes, epidemiology,
        experimental setups (time series)...
        Format: ISO 8601 (cf. documentation on time formats)
  :type dateTimeObserved: null|string
  :field ageAtObservation:
    Age at time of the observation.
        This is highly relevant in the human context and usually the primary
        available time related parameter available, as date of birth might not
        be available.
  :type ageAtObservation: null|string

  Observations are single measurements, which can be described through their
    type, value and unit, as well as an associated dateTime value. This could be
    numerical values with a unit, or observations defined through ontologies.
  
    Examples would be body height, body weight, BMI...
  
    TODO:
      - need keyword/value table, also human notes

.. avro:record:: Intervention

  :field id:
    The id of the intervention. This is facultative and allows the association
        of an intervention to e.g. a phenotype object, through a relationship.
  :type id: null|string
  :field intervention:
    The type of the intervention.
  :type intervention: null|OntologyTerm
  :field description:
    A description of the intervention.
  :type description: null|string
  :field dateTimeIntervention:
    Date the the invervention started.
        Format: ISO 8601 (cf. documentation on time formats)
  :type dateTimeIntervention: null|string

  Interventions are e.g. medical treatments.  This is a summary of the clinical
    information intended to be used in basic analysis when clinical information
    may not be avalable. This could be e.g. OntologyTerm based representations of
  
      medical procedure, SIO_001024
      cognitive behavior, NBO_0000607
      drug, CHEBI_23888

.. avro:record:: Evidence

  :field evidenceType:
    ECO or OBI is recommended
  :type evidenceType: OntologyTerm
  :field description:
    A textual description of the evidence. This is used to complement the
        structured description in the evidenceType field
  :type description: null|string

  NOTE: Copied from genotypephenotype.avdl
    Evidence for the phenotype association.
    This is also a stub for further expansion. We should consider moving this into
    its own schema.
    TODO: Move Evidence from genotypephenotype.avdl to metadata.avdl?

.. avro:record:: Association

  :field ids:
    A list of exactly two object ids.
        This is the minimum object glue; e.g. for association of the intervention
        (applied to an individual) with a sample.
  :type ids: array<string>
  :field description:
    A textual description of the association.
  :type description: null|string
  :field evidence:
    The evidence for this specific instance of association between the
        different objects.
  :type evidence: array<Evidence>

  Associations allow to "glue" two objects together, in lieu of forced nesting.
    The concept borrows from the G2P definitions.
    TODO: Move Association from genotypephenotype.avdl?

.. avro:record:: GeographicLocation

  :field latitude:
    signed decimal degrees (North, relative to Equator)
  :type latitude: null|float
  :field longitude:
    signed decimal degrees (East, relative to IERS Reference Meridian)
  :type longitude: null|float
  :field elevation:
    meters above/below (standard) sea level
  :type elevation: null|float
  :field description:
    A verbose description of the location, for processing into latitude,
        longitude, elevation attributes.
        Preferably used standard "administrative boundaries" terms.
  :type description: null|string

  A geographic location object.
    This implementation supports a single "point" location
    and an additional/fallback description (e.g. address style) attribute.
  
    Using multiple GeographicLocation objects in an ordered list could allow for
    encoding of polygon-style locations (e.g. representation of administrative
    boundaries).
  
    The geographic point object uses the default units from the DCMI point scheme
    http://dublincore.org/documents/dcmi-point/
    and avoids optional representation in non-standard units.
  
    TODO:
    - Include extended attributes, capture standardized address parameters?

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
    The times at which this record was created / updated.
        Format: ISO 8601 (cf. documentation on time formats)
  :type created: string
  :field updated:
  :type updated: string
  :field bioSampleId:
  :type bioSampleId: null|string
  :field runTime:
    The time at which this experiment was performed.
        Granularity here is variabel (e.g. date only).
        Format: ISO 8601, YYYY-MM-DDTHH:MM:SS (e.g. 2015-02-10T00:03:42)
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

.. avro:record:: Individual

  :field id:
    The Individual's :ref:`id <apidesign_object_ids>`. This is unique in the
        context of the server instance.
  :type id: string
  :field name:
    The Individual's :ref:`name <apidesign_object_names>`. This is a label or
        symbolic identifier for the individual.
  :type name: null|string
  :field description:
    The Individual's description. This attribute contains human readable text.
        The "description" attributes should not contain any structured data.
  :type description: null|string
  :field created:
    The :ref:`ISO 8601<metadata_date_time> time at which this Individual record
        was created.
  :type created: string
  :field updated:
    The :ref:`ISO 8601<metadata_date_time> time at which this Individual object
        was updated.
  :type updated: string
  :field species:
    For a representation of an NCBI Taxon ID as an OntologyTerm, see
        NCBITaxon Ontology
          http://www.obofoundry.org/wiki/index.php/NCBITaxon:Main_Page
        For example, 'Homo sapiens' has the ID 9606. The NCBITaxon ontology ID for
        this is NCBITaxon:9606, which has the URI
        http://purl.obolibrary.org/obo/NCBITaxon_9606
  :type species: null|OntologyTerm
  :field sex:
    The genetic sex of this individual.
        Use `null` when unknown or not applicable.
        Recommended: PATO http://purl.obolibrary.org/obo/PATO_0020001; PATO_0020002
  :type sex: null|OntologyTerm
  :field developmentalStage:
    The developmental stage of this individual. This not age of onset of a
        disease.
        Using Uberon is recommended.
        For example http://purl.obolibrary.org/obo/UBERON_0007023 => adult organism
        TODO: need to clarify how to deal with this as a temporal series
  :type developmentalStage: null|OntologyTerm
  :field dateOfBirth:
    The date of birth of this individual. Usually would be
        coded to the day; however, finer (e.g. animal model system) or more
        approximate (e.g. year for clinical applications) granularity is possible.
        :ref:`ISO 8601<metadata_date_time>
  :type dateOfBirth: null|string
  :field strain:
    The strain of this individual, for non-humans.
  :type strain: null|OntologyTerm
  :field ethnicity:
    Ethnicity of individual, if applicable.
        Recommended by the NHGRI GWAS Catalog 0 ontology
        http://purl.bioontology.org/ontology/ANCESTRO
  :type ethnicity: null|OntologyTerm
  :field geographicLocation:
    Geographic coordinates from which the individual was obtained.
  :type geographicLocation: null|GeographicLocation
  :field diseases:
    Diseases with which the individual has been diagnosed.
  :type diseases: array<Disease>
  :field phenotypes:
    Phenotypes for this individual.
  :type phenotypes: array<Phenotype>
  :field interventions:
    A description of the clinical treatments/interventions.
  :type interventions: array<Intervention>
  :field observations:
    Observations and measurements related to the individual.
  :type observations: array<Observation>
  :field info:
    A map of additional information.
  :type info: map<array<string>>

  An individual (or subject) typically corresponds to an individual
    human or other organism.

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
  :field created:
    The :ref:`ISO 8601<metadata_date_time> time at which this BioSample record
        was created.
  :type created: string
  :field updated:
    The :ref:`ISO 8601<metadata_date_time> time at which this BioSample object was updated.
  :type updated: string
  :field collected:
    The :ref:`ISO 8601<metadata_date_time> time at which the corresponding
        BioSample was collected.  Granularity here is variable (e.g. only date would be common for
        biopsies, minutes for in vitro time series).
  :type collected: null|string
  :field individualId:
    The id of the individual this biosample was derived from.
  :type individualId: null|string
  :field ageAtcollection:
    The age of the individual (not of the biosample) at time of
        biosample's collection.
        This parameter is both more prevalent in clinical records than the
        combination of sampling date and DOB, and also more relevant for
        clinical/experimental purposes than either of those alone.
        This field may be approximate.
        Format: :ref:`ISO 8601<metadata_date_time> duration PnYnMnDTnHnMnS in a suitable approximation
        Example: P12Y3M
  :type ageAtcollection: null|string
  :field interventions:
    A description of the interventions applied to the biosample
        (e.g. in vitro drug testing).
  :type interventions: array<Intervention>
  :field observations:
    Observations and measurements related to the biosample.
  :type observations: array<Observation>
  :field cellType:
    The cell types of this biosample.
        Using the [Cell Ontology](http://cellontology.org/) (CL) is recommended.
  :type cellType: null|OntologyTerm
  :field organismPart:
    The anatomical part (body part, organ, tissue, body or excretory fluid) of
        the individual from which this biosample derives.
        Using Uberon (http://uberon.org) is recommended.
  :type organismPart: null|OntologyTerm
  :field cellLine:
    This biosample could be derived from a cell line, which still
        could be from an indivdual.
        Using the Cell Line Ontology (https://code.google.com/p/clo-ontology/)
        is a possibility.
        TODO: discuss further. Other possibilities: Cellosaurus (nextprot),
        BRENDA/BTO, EFO (EBI)
        TODO: need to have derivation record from other biosample for
        cell lines.
  :type cellLine: null|OntologyTerm
  :field geographicLocation:
    Geographic coordinates from which the biosample was obtained.
        This is either related to a field collection, or the corresponding
        individual's place of residencde or treatment.
        TODO: May need replacement with multiple locations.
  :type geographicLocation: null|GeographicLocation
  :field specimenType:
    A typing of the specimen under study. Use the OBI terms under child of
        specimen. e.g. "cloacal swab".
  :type specimenType: null|OntologyTerm
  :field preservationMethod:
    Preservation method of sample.
        http://bioportal.bioontology.org/ontologies/OBI/ - use children of specimen
        with known storage state e.g. "frozen specimen"
  :type preservationMethod: null|OntologyTerm
  :field info:
    A map of additional information.
  :type info: map<array<string>>

  A BioSammple refers to a unit of biological material from which the substrate
     molecules (e.g. genomic DNA, RNA, proteins) for molecular analyses (e.g.
     sequencing, array hybridisation, mass-spectrometry) are extracted. Examples
     would be a tissue biopsy, a single cell from a culture for single cell genome
     sequencing or a protein fraction from a gradient centrifugation.
     Several instances (e.g. technical replicates) or types of experiments (e.g.
     genomic array as well as RNA-seq experiments) may refer to the same BioSample.
     In the context of the GA4GH metadata schema, BioSample constitutes the central
     reference object.

