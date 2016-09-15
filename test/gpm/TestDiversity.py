import os
import unittest
from test.gpm.GPMTestCase import GPMTestCase
from src.gpm.Diversity import Diversity

class TestDiversity(GPMTestCase):
	"""
	Tests the python class to compute species richness from GBIF data stored in a Mongo database 
	"""

	def setUp(self):
		GPMTestCase.setUp(self)
		self.diversity = Diversity( self.TEST_HOST, self.TEST_DB, self.TEST_COLL )
		

	def testCounts(self):
		self.assertEquals( 1, self.diversity.countPhyla() )
		self.assertEquals( 1, self.diversity.countClasses() )
		self.assertEquals( 1, self.diversity.countOrders() )
		self.assertEquals( 1, self.diversity.countFamilies() )
		self.assertEquals( 3, self.diversity.countGenera() )
		self.assertEquals( 26, self.diversity.countSpecies() )

	def testList(self):
		self.assertEquals( 1, len( self.diversity.listPhyla() ) )
		self.assertEquals( 1, len( self.diversity.listClasses() ) )
		self.assertEquals( 1, len( self.diversity.listOrders() ) )
		self.assertEquals( 1, len( self.diversity.listFamilies() ) )
		self.assertEquals( 3, len( self.diversity.listGenera() ) )
		self.assertEquals( 26, len( self.diversity.listSpecies() ) )

	#def testOutput(self):
		#countPhylum = GPMTestCase.CMD[ 'count_py' ] % ( self.TEST_HOST, self.TEST_DB, self.TEST_COLL )
		#count = int( os.popen( countPhylum ).readlines()[1] )
		#self.assertEquals( 1, count )


