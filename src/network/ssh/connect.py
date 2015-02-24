try:
	import paramiko
except ImportError:
	print 'please install `paramiko` so that you can successfully run diffos.'

class SSH_Connection(object):
	"""
	
	"""
	def __init__(self, address, uname, password=''):
		ssh = paramiko.SSHClient()
		try:
			ssh.connect(address, username=uname, password=password)
		except:
			print 'you have an error in your connection please retry with the correct credentials'
		self.address = address
		self.uname = uname
		self.password = password

if __name__ == "__main__":
	ssh = paramiko()
