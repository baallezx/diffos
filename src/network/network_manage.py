"""
This is the library that will handle of the networking features of diffos.
It should handle making a connection to a machine through a specific protocol
make sure there is a proper handshake. make a conneciton with the machine.
"""

class address(object):
	"""  """
	def __init__(self,addr):
		self.addr, self.addr_type = self.find_address_type(addr)

	def find_address_type(self,addr):
		""" returns the type of address given to help network manage with the actual connection """
		import re
		# TODO: check using regular expressions as to what type of address you ahve been given
		
		return this_addr, this_addr_type

class network_manage(object):
	"""
	handles the connection of each diffnode
	"""
	def __init__(self):
		pass
