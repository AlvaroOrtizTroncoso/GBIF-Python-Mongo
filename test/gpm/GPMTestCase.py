import unittest
import os

class GPMTestCase(unittest.TestCase):

	CMD = {
		'import_cmd' : 'make -f tools/build import host=%s db=%s collection=%s file=%s',
		'drop_cmd' : 'mongo --host %s %s --eval "db.dropDatabase()"',
		'count_cmd' : 'mongo --host %s %s --eval "db.%s.count()"',
		'cleanup_cmd' : "mongo  --host %s %s  --eval 'db.%s.remove({species:{$eq: null}})'"
	}


	def setUp(self):
		"""
		Import the test data into a test database and cleanup 
		"""
		self.TEST_HOST = '10.0.2.2' 
		self.TEST_DB = 'test_db'
		self.TEST_COLL = 'test_coll'
		self.TEST_FILE = os.path.join(os.getcwd(), 'test', 'Geraniales_GBIF_Germany.csv' )
		self.OUTPUT_FILE = os.path.join(os.getcwd(), 'test', 'diversity.csv' )

		importTestData = GPMTestCase.CMD[ 'import_cmd' ] % ( self.TEST_HOST, self.TEST_DB, self.TEST_COLL, self.TEST_FILE )
		resp = os.system( importTestData )
		self.assertEquals( 0, resp, "Import command failed" )

		cleanupTestData = GPMTestCase.CMD[ 'cleanup_cmd' ] % ( self.TEST_HOST, self.TEST_DB, self.TEST_COLL )
		resp = os.system( cleanupTestData )
		self.assertEquals( 0, resp, "Cleanup command failed" )


	def tearDown(self):
		"""
		Drop the test database
		"""
		drop = GPMTestCase.CMD[ 'drop_cmd' ] % ( self.TEST_HOST, self.TEST_DB )
		# check that drop command returned no errors
		resp = os.system( drop )
		self.assertEquals( 0, resp, "Drop command failed" )
