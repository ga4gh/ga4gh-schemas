"""
Tests the schema compilation
"""
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import fnmatch
import os
import tempfile
import unittest

# similar to dev_glue.py
import ga4gh
ga4gh.__path__.insert(0, 'python/ga4gh')

import ga4gh.common.utils as utils  # NOQA
import ga4gh.schemas._version as version  # NOQA


class TestCompile(unittest.TestCase):

    def _getPb2Files(self, sourceDir):
        """
        Return file paths of all pb2 files found in the sourceDir tree
        """
        pb2Files = []
        for root, dirs, files in os.walk(sourceDir):
            pb2Files.extend([
                os.path.join(root, filename)
                for filename in fnmatch.filter(files, "*_pb2.py")])
        pb2Files.sort()
        return pb2Files

    def _getDirAndFilenameOfPath(self, path):
        """
        Returns the last two segments of a file path
        """
        return os.path.join(
            os.path.basename(os.path.dirname(path)),
            os.path.basename(path))

    @unittest.skip
    def testCompile(self):
        """
        Compiles the schemas to a temporary directory and then checks
        that the pb2 files in the temporary direcory are the same as the
        pb2 files that are checked in.

        This test prevents inadvertent mismatches between proto files and
        pb2 files from being checked in.
        """
        # compile the schemas to a temporary directory
        scriptPath = 'scripts/process_schemas.py'
        schemaVersion = '.'.join(version.version.split('.')[0:3])
        schemaPath = 'src/main/proto/'
        schemaDest = tempfile.mkdtemp()
        cmd = "python {} {} {} -d {}".format(
            scriptPath, schemaVersion, schemaPath, schemaDest)
        utils.runCommand(cmd, silent=True)

        # get the file paths of the checked in pb2 files
        # (we do it in two calls to avoid the build/ tree, etc.
        # in the python directory which may contain pb2 files)
        checkedInDirGa4gh = 'python/ga4gh'
        checkedInDirGoogle = 'python/google'
        checkedInFilePathsGa4gh = self._getPb2Files(checkedInDirGa4gh)
        checkedInFilePathsGoogle = self._getPb2Files(checkedInDirGoogle)
        checkedInFilePaths = sorted(
            checkedInFilePathsGa4gh + checkedInFilePathsGoogle)

        # check to see that the contents of the directories are the same
        tempFilePaths = self._getPb2Files(schemaDest)
        self.assertEqual(len(checkedInFilePaths), len(tempFilePaths))
        for checkedInFilePath, tempFilePath in utils.zipLists(
                checkedInFilePaths, tempFilePaths):
            checkedInFileShortPath = self._getDirAndFilenameOfPath(
                checkedInFilePath)
            tempFileShortPath = self._getDirAndFilenameOfPath(tempFilePath)
            self.assertEqual(checkedInFileShortPath, tempFileShortPath)
            with open(checkedInFilePath) as checkedInFile, \
                    open(tempFilePath) as tempFile:
                for checkedInLine, tempLine in zip(checkedInFile, tempFile):
                    self.assertEqual(checkedInLine, tempLine)
