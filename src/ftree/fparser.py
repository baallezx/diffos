"""
parses a file system and returns a data structure of the results in-memory
"""

# TODO: need to come up woth a solution to handle common cases where file-system is larger than given memory. 

class ftree(object):
	"""
	a basic n-dimensional tree that is representative of the file system
	"""
	node_map = [] # used to get a map of the location of the file
	def __init__(self,root):
		self.root = root

	def walk(self,cnode):
		""" walk the tree in depth-first fashion """
		pass

	def to_json(self):
		""" return a json string of the filesystem """
		pass

	def to_yaml(self):
		""" return a yaml string of the filesystem """
		pass

class node(object):
	"""
	an abstract node type that all system nodes inherit from
	"""
	def __init__(self,val,children=[],parent=None,siblings=None):
		self.val = val
		self.children = children
		self.parent = parent
		self.siblings = siblings

	def to_json(self):
		""" returns the json version of itself """
		# XXX: this method might be unneccesary given pythons object structure
		d = self.__dict__()

class file_node(node):
	""" a file node representing a file """
	# TODO: add special attributes that can search and query specific types of file_node(s)
	def __init__(self,filename,contents="",extension="",size=0,parent=None,path=""):
		self.filename = filename
		self.contents = contents
		self.extension = extension
		self.size = size
		self.parent = parent
		self.path = path

	def load_contents(self,as_string=False):
		try:
			if as_string:
				self.contents = open(self.path + self.filename, "r").read()
			else:
				self.contents = open(self.path + self.filename, "r").readlines()
		except:
			# TODO: add a handler here
			pass

class dir_node(node):
	""" a directory node representing a directory """
	def __init__(self):
		pass
