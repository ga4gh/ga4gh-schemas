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

import ga4gh.schemas.pb as pb  # NOQA
import ga4gh.schemas._protocol_version as version  # NOQA

import ga4gh.schemas.ga4gh.common_pb2 as common_pb2  # NOQA
import ga4gh.schemas.ga4gh.assay_metadata_pb2 as assay_metadata_pb2  # NOQA
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
        self.assertIsNotNone(assay_metadata_pb2.DESCRIPTOR)
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
        self.assertIsNotNone(http_pb2.DESCRIPTOR)
