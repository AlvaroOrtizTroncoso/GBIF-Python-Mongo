import unittest
import os
from test.gpm.GPMTestCase import GPMTestCase

class TestImport(GPMTestCase):
	"""
	Tests the make script to import GBIF data into MongoDB
	"""
	
	def testImport(self):
		# count entries in db
		countDB = GPMTestCase.CMD[ 'count_cmd' ] % ( self.TEST_HOST, self.TEST_DB, self.TEST_COLL )
		numEntriesDB = int( os.popen( countDB ).readlines()[2] )
		# check that all entries were imported
		self.assertEquals( 1476, numEntriesDB )


