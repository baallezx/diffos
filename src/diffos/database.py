# project library
import diffparser # this is the parser I will use to break up a given user string and turn that into computer logic.

# standard library
import struct
from os import path

# addons
import json

# TODO: need to come up with a standard for adding new nodes at each level of the tree.
# TODO: need to come up with a language to query the database tree.
# TODO: need to design an actual package managment server
# TODO: need to come up with a binary format to save this tree to.

__author__ = "Alex Balzer <abalzer22@gmail.com>"
__version__ = "0.1.0"

class database(object):
	"""
	the diffos operating system database
	
	os
	|
	|-- architecture -->> all operating system info. os-type, system info, filesystem type
	|
	|-- languages -->> all languages used, and all there correlating info
	|
	|-- processes -->>
	|
	|-- databases -->>
	|
	|-- users -->>
	|
	|-- network -->>
	|
	|-- filesystem -->>
	|
	|-- ... -->> etc...
	
	"""
	# TODO: need to develop means to populate these fields in the database.
	def __init__(self,filelocation="/opt/diffos/fs.db"):
		self.filelocation = filelocation
		if path.isfile(filelocation):
			# TODO: write a method that can check that the flie has not been corrupted or tampered with. meaning you need to keep a log of all the actions this software does. if the file has been modified after this program used it raise an exception an propmt the user for an explanation.
			self.db = self._read_database_file()
		else:
			self.db = {
				"os": {
					"architecture": {},
					#"architecture": {"all":[]},
					"languages": {},
					"processes": {},
					"databases": {},
					"users": {},
					"network": {},
					"filesystem": {},
					"a": { "b": { "c": { "not a good key": {1:[2,3,4,5]}, "d": [ "e", "f" ] } } },
#					"": {},
				},
			}
		self.key = ""

	def _cycle(self,key,element,path_string=""):
		""" depth first search of the database for a key """
		# NOTE: dict keys -->> "a:b:c", list -->> "a:b:c>l"
		if isinstance(element, dict):
			for k,v in element.items():
				if k == key:
					self.key = path_string+":"+key
				self._cycle(key, element[k], path_string+":"+k)
		if isinstance(element, list):
			for i in element:
				if i == key:
					return path_string+">"+key

	def find(self,key):
		"""
		find a key value in the database and return the path to the key.
		"""
		self._cycle(key, self.db)
		return self.key

	# TODO: need to add a function that will pretty print the results of the query.
	def query(self, query_string):
		"""
		query the database for all needed attributes.
		"""
		# NOTE: this is an example and should show the logic behind what is going on
		h = self.db
		for i in query_string.split(':'):
			if isinstance(h, dict):
				#print h[i]
				h = h.get(i,'')
				#print "h =", h
			# print h
		return h

	def update(self,update_string):
		"""
		update the database for specific changes.
		"""
		pass

	def remove(self, remove_string):
		"""
		remove anything from the database that needs to be removed.
		"""
		# TODO: this needs a safety net like not being able to delete certain nodes at certain levels.
		pass

	def _read_database_file(self):
		return open(self.filelocation,"rb").read()

	def _update_database_file(self,curr_db):
		pass

	# TODO: figure out if there is a way to constantly grow the file as opposed to read, destroy rewrite all.
	def _write_database(self,curr_db):
		"""
		write the database to the file
		"""
		pass

	def close(self):
		"""
		close the database and terminate the diffos daemon.
		"""
		pass
		# curr_db = self._read_database_file()
		# self._update_database_file(curr_db)
		# self._write_database(curr_db)

if __name__ == "__main__":
	# TODO: convert this to a unittest file
	this_db = database()
	print "os:architecture = " , this_db.query("os:architecture")
	print "os:languages = " , this_db.query("os:languages")
	print "os:processes = " , this_db.query("os:processes")
	print "os:databases = " , this_db.query("os:databases")
	print "os:users = " , this_db.query("os:users")
	print "os:network = " , this_db.query("os:network")
	print "os:filesystem = " , this_db.query("os:filesystem")
	print "os:filesystem:etc = " , this_db.query("os:filesystem:etc")
	print "os:filesystem:etc:network = " , this_db.query("os:filesystem:etc:network")
	print "find(\"d\") = " , this_db.find("d")
	this_db.close()
