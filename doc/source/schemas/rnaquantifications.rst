RnaQuantifications
******************

This protocol defines feature expression counts on GA4GH reads.

.. proto3:enum:: ExpressionUnits

  :symbols: EXPRESSION_UNIT_UNSPECIFIED|FPKM|TPM
  Units for expression level.
  FPKM - number of Fragments Per Kilobase of feature length per Million reads
  FPKM is calculated by dividing the fragment count per feature by the total number of reads in millions (FPM - Fragments Per Million).  FPM is then divided by feature length in kilobases to obtain FPKM.
  
  TPM - Transcripts per kilobase Per Million reads
  TPM is calculated by first dividing the fragment/read count by feature length in kilobases (RPK - Reads Per Kilobase).  The count of all RPKs in the sample are then divided by a million to generate a 'per million' scaling value.  For each feature RPK divided by the 'per million' scaling factor generated TPM.

.. proto3:message:: RnaQuantificationSet

  :field id:
    The RNA quantification set ID.
  :type id: string
  :field dataset_id:
    The ID of the dataset this RNA Quantification set belongs to.
  :type dataset_id: string
  :field name:
    The RNA quantification set name.
  :type name: string

  A collection of associated RNAQuantifications.  Typically this will be all
  the Quantifications of samples from an experiment.

.. proto3:message:: RnaQuantification

  :field id:
    The unique ID assigned to the results of running the described programs on the
    specified reads and assignment to the listed annotation.
  :type id: string
  :field name:
    Name
  :type name: string
  :field description:
    Description
  :type description: string
  :field read_group_ids:
    ID(s) of the ReadGroup(s) providing the reads for the analysis.
  :type read_group_ids: repeated string
  :field programs:
    Programs can be used to track the provenance of how read data was quantified.
  :type programs: repeated Program
  :field feature_set_ids:
    List of annotation sets used.
  :type feauture_set_ids: repeated string

  Top level identifying information

.. proto3:message:: FeatureGroup

  :field id:
    feature group ID
  :type id: string
  :field feature_ids:
    The associated features.
  :type feature_ids: repeated string
  :field name:
    User assigned short name for the collection
  :type name: string
  :field description:
    Description
  :type description: string

  Identifying information for a group of features.

.. proto3:message:: ExpressionLevel

  :field id:
    Expression ID
  :type id: string
  :field name:
    Name
  :type name: string
  :field rna_quantification_id:
    The associated RnaQuantification
  :type rna_quantification_id: string
  :field raw_read_count:
    The number of reads mapped to this feature.
  :type raw_read_count: float
  :field expression:
    Numerical expression value.
  :type expression: float
  :field is_normalized:
    True if the expression value is a normalized value.
  :type is_normalized: bool
  :field units:
    The units of the expression value if one is given.
  :type units: ExpressionUnit
  :field score:
    Weighted score for the expression value.
  :type score: float
  :field conf_interval_low:
    Lower bound of the confidence interval on the expression value.
  :type conf_interval_low: float
  :field conf_interval_high:
    Upper bound of the confidence interval on the expression value.
  :type conf_interval_high: float
  :field feature_group_ids:
    Associated feature groups
  :type feature_group_ids: repeated string

  The actual numerical quantification for each feature.

