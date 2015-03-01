try:
	import paramiko
except ImportError:
	print 'please install `paramiko` so that you can successfully run diffos.'

# TODO: need to come up with a default ssh user that all client nodes use within diffos. also need to look into the security vulnerabilities of doing such a thing.
# TODO: need to come up with an initiation procedure on a linux client node when diffos is first installed on the machine. 
# Ex. (
#	`mkdir /var/lib/diffos/`,
# 	`scp diffos_daemon from central diffos server`,
# 	`install diffos inside of /var/lib/diffos`,
# 	`create user diffos`,
# 	`create keys for diffos and log them to central server and to workstation node`
# )
class SSH_Connection(object):
	"""
	make a connection to a client node through ssh protocol.
	"""
	def __init__(self, address, uname=None, password=None,port=None):
		ssh = paramiko.SSHClient()
		try:
			if port == None:
				ssh.connect(address, username=uname, password=password)
			else:
				ssh.connect(address,port=port)
		except:
			print 'you have an error in your connection please retry with the correct credentials'
		self.address = address
		self.uname = uname
		self.password = password

if __name__ == "__main__":
	ssh = paramiko()
