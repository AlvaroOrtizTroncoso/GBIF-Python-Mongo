import unittest
import os
from subprocess import call

class TestImport(unittest.TestCase):
	"""
	Tests the make script to import GBIF data into MongoDB
	"""
	
	CMD = {
		'import_cmd' : 'make -f tools/import host=%s db=%s collection=%s file=%s',
		'drop_cmd' : 'mongo --host %s %s --eval "db.dropDatabase()"',
		'count_cmd' : 'mongo --host %s %s --eval "db.%s.count()"'
	}
	
	
	def setUp(self):
		self.TEST_HOST = '10.0.2.2' 
		self.TEST_DB = 'test_db'
		self.TEST_COLL = 'test_coll'
		self.TEST_FILE = os.path.join(os.getcwd(), 'test', 'Geraniales_GBIF_Germany.csv' )
	
	
	def testImport(self):
		"""
		Import the test data into a test database
		"""		
		importTestData = TestImport.CMD[ 'import_cmd' ] % ( self.TEST_HOST, self.TEST_DB, self.TEST_COLL, self.TEST_FILE )
		resp = os.system( importTestData )
		# check that import command returned no errors
		self.assertEquals( 0, resp )

		# count entries in file (1 per line minus header)
		numEntriesFile = sum( 1 for line in open( self.TEST_FILE ) ) - 1
		# count entries in db
		countDB = TestImport.CMD[ 'count_cmd' ] % ( self.TEST_HOST, self.TEST_DB, self.TEST_COLL )
		numEntriesDB = int( os.popen( countDB ).readlines()[2] )
		# check that all entries were imported
		self.assertEquals( numEntriesFile, numEntriesDB )


	def tearDown(self):
		"""
		Drop the test database
		"""
		drop = TestImport.CMD[ 'drop_cmd' ] % ( self.TEST_HOST, self.TEST_DB )
		# check that drop command returned no errors
		resp = os.system( drop )
		self.assertEquals( 0, resp )
