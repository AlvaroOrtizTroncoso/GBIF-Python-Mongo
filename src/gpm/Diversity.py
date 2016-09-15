import sys
from pymongo import MongoClient

class Diversity:
	"""
	Compute species diversity per taxon grade fom GBIF data stored in a Mongo database
	"""
	
	def __init__(self, host, db, coll):
		"""
		@param host - String IP of the mongo server
		@param db - String name of the mongo database
		@param coll - String name of the mongo collaction
		"""
		client = MongoClient("mongodb://%s:27017" % host)
		self.db = client[db]
		self.coll = self.db[coll]


	def compute(self):
		pass


	def countPhyla(self):
		return len( self.listPhyla() )


	def countClasses(self):
		return len( self.listClasses() )
	
	
	def countOrders(self):
		return len( self.listOrders() )
	
	
	def countFamilies(self):
		return len( self.listFamilies() )
	
	
	def countGenera(self):
		return len( self.listGenera() )
	
	
	def countSpecies(self):
		return len( self.listSpecies() )


	def listPhyla(self):
		return self.coll.distinct( "phylum" )


	def listClasses(self):
		return self.coll.distinct( "class" )
	
	
	def listOrders(self):
		return self.coll.distinct( "order" )
	
	
	def listFamilies(self):
		return self.coll.distinct( "family" )
	
	
	def listGenera(self):
		return self.coll.distinct( "genus" )

	
	def listSpecies(self):
		return self.coll.distinct( "species" )

if __name__ == "__main__":
	try:
		if len( sys.argv ) != 4: raise Exception( "Wrong argument count" )
		host = sys.argv[ 1 ]
		db = sys.argv[ 2 ]
		coll = sys.argv[ 3 ]
		diversity = Diversity( host, db, coll )
		
	except Exception as e:
		print( e )