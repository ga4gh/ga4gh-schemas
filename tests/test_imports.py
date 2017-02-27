"""
Tests for schemas
"""
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import unittest

# similar to dev_glue.py
import ga4gh

ga4gh.__path__.insert(0, 'python/ga4gh')

import ga4gh.schemas._protocol_version as version  # NOQA

import ga4gh.schemas.ga4gh.common_pb2 as common_pb2  # NOQA
import ga4gh.schemas.ga4gh.metadata_pb2 as metadata_pb2  # NOQA
import ga4gh.schemas.ga4gh.metadata_service_pb2 as metadata_service_pb2  # NOQA
import ga4gh.schemas.ga4gh.read_service_pb2 as read_service_pb2  # NOQA
import ga4gh.schemas.ga4gh.reads_pb2 as reads_pb2  # NOQA
import ga4gh.schemas.ga4gh.reference_service_pb2 as reference_service_pb2  # NOQA
import ga4gh.schemas.ga4gh.references_pb2 as references_pb2  # NOQA
import ga4gh.schemas.ga4gh.variant_service_pb2 as variant_service_pb2  # NOQA
import ga4gh.schemas.ga4gh.variants_pb2 as variants_pb2  # NOQA
import ga4gh.schemas.ga4gh.allele_annotations_pb2 as allele_annotations_pb2  # NOQA
import ga4gh.schemas.ga4gh.allele_annotation_service_pb2 as allele_annotation_service_pb2  # NOQA
import ga4gh.schemas.ga4gh.sequence_annotations_pb2 as sequence_annotations_pb2  # NOQA
import ga4gh.schemas.ga4gh.sequence_annotation_service_pb2 as sequence_annotation_service_pb2  # NOQA
import ga4gh.schemas.ga4gh.bio_metadata_pb2 as bio_metadata_pb2  # NOQA
import ga4gh.schemas.ga4gh.bio_metadata_service_pb2 as bio_metadata_service_pb2  # NOQA
import ga4gh.schemas.ga4gh.genotype_phenotype_pb2 as genotype_phenotype_pb2  # NOQA
import ga4gh.schemas.ga4gh.genotype_phenotype_service_pb2 as genotype_phenotype_service_pb2  # NOQA
import ga4gh.schemas.ga4gh.rna_quantification_pb2 as rna_quantification_pb2  # NOQA
import ga4gh.schemas.ga4gh.rna_quantification_service_pb2 as rna_quantification_service_pb2  # NOQA

import ga4gh.schemas.google.api.annotations_pb2 as annotations_pb2  # NOQA
import ga4gh.schemas.google.api.http_pb2 as http_pb2  # NOQA
import ga4gh.schemas.pb as pb  # NOQA


class TestPb(unittest.TestCase):
    def testString(self):
        self.assertEqual(pb.DEFAULT_STRING, pb.string(None))
        self.assertEqual('A', pb.string('A'))

    def testInt(self):
        self.assertEqual(pb.DEFAULT_INT, pb.int(None))
        self.assertEqual(1, pb.int(1))


class TestSchemas(unittest.TestCase):
    def testVersion(self):
        version.version.split('.')
        self.assertIsNotNone(version.version)

    def testGa4ghImports(self):
        self.assertIsNotNone(common_pb2.DESCRIPTOR)
        self.assertIsNotNone(metadata_pb2.DESCRIPTOR)
        self.assertIsNotNone(metadata_service_pb2.DESCRIPTOR)
        self.assertIsNotNone(read_service_pb2.DESCRIPTOR)
        self.assertIsNotNone(reads_pb2.DESCRIPTOR)
        self.assertIsNotNone(reference_service_pb2.DESCRIPTOR)
        self.assertIsNotNone(references_pb2.DESCRIPTOR)
        self.assertIsNotNone(variant_service_pb2.DESCRIPTOR)
        self.assertIsNotNone(variants_pb2.DESCRIPTOR)
        self.assertIsNotNone(allele_annotations_pb2.DESCRIPTOR)
        self.assertIsNotNone(allele_annotation_service_pb2 .DESCRIPTOR)
        self.assertIsNotNone(sequence_annotations_pb2.DESCRIPTOR)
        self.assertIsNotNone(sequence_annotation_service_pb2.DESCRIPTOR)
        self.assertIsNotNone(bio_metadata_pb2.DESCRIPTOR)
        self.assertIsNotNone(bio_metadata_service_pb2.DESCRIPTOR)
        self.assertIsNotNone(genotype_phenotype_pb2.DESCRIPTOR)
        self.assertIsNotNone(genotype_phenotype_service_pb2.DESCRIPTOR)
        self.assertIsNotNone(rna_quantification_pb2.DESCRIPTOR)
        self.assertIsNotNone(rna_quantification_service_pb2.DESCRIPTOR)

    def testGoogleImports(self):
        self.assertIsNotNone(annotations_pb2.DESCRIPTOR)

    def testDatasetAttributes(self):
        """
        Demonstrates the usage of the Attribute's field on a dataset message.
        This field is available on many other messages as well.
        """
        key = "numbers_and_strings"
        string_value = "hello"
        int32_value = 5
        double_value = 3.14159
        attributes = {key: [string_value, int32_value, double_value]}
        dataset = metadata_pb2.Dataset()
        myattribute = dataset.attributes.attr[key].values

        myattribute.add().string_value = string_value
        myattribute.add().int32_value = int32_value
        myattribute.add().double_value = double_value

        self.assertEqual(
            dataset.attributes.attr[key].values[0].string_value,
            attributes[key][0])

        self.assertEqual(
            dataset.attributes.attr[key].values[1].int32_value,
            attributes[key][1])

        self.assertEqual(
            dataset.attributes.attr[key].values[2].double_value,
            attributes[key][2])

    def testNestedAttributes(self):
        """
        Demonstrates how nested attributes can be used to interchange
        arbitrary unstructured, typed data.
        """
        dataset = metadata_pb2.Dataset()
        key1 = "key1"
        key2 = "key2"
        string_value = "hello"
        int32_value = 32
        attributes = {key1: [{key2: [string_value]}, int32_value]}
        myAttribute = dataset.attributes.attr[key1].values
        nestedAttribute = myAttribute.add().attributes.attr[key2].values
        nestedAttribute.add().string_value = string_value
        myAttribute.add().int32_value = int32_value

        mynested = dataset.attributes.attr[key1]. \
            values[0].attributes.attr[key2]

        self.assertEqual(
            mynested.values[0].string_value,
            attributes[key1][0][key2][0])

        self.assertEqual(dataset.attributes.attr[key1].
                         values[1].int32_value, attributes[key1][1])

    def testTypedAttributes(self):
        """
        Demonstrates how to use other types defined in common to create an
        attribute message.
        """
        dataset = metadata_pb2.Dataset()
        ontologyTerm = common_pb2.OntologyTerm()
        ontologyTerm.term_id = "test"
        ontologyKey = "my_ontology_term"

        dataset.attributes.attr[ontologyKey] \
            .values.add().ontology_term.MergeFrom(ontologyTerm)
        term = dataset.attributes.attr[ontologyKey]
        self.assertEqual(
            term.values[0].ontology_term.term_id,
            ontologyTerm.term_id)

        experiment = common_pb2.Experiment()
        experiment.id = "test"
        key = "my_experiment"

        dataset.attributes.attr[key] \
            .values.add().experiment.MergeFrom(experiment)
        self.assertEqual(
            dataset.attributes.attr[key].values[0].experiment.id,
            experiment.id)

    def testGoogle(self):
        self.assertIsNotNone(http_pb2.DESCRIPTOR)
