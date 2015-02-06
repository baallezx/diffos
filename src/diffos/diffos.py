"""
this is the actual implementation of the diffos which gives users the abilitiy to query different nodes for os information
"""
import sys

__author__ = "alexander balzer <abalzer22@gmail.com>"
__version__ = "0.1.0"

def helper(help_f=None): #*args, **kwargs):
	help_methods = {
		'diff'	:	'returns a diff object between the 2 machines',
		'check'	:	'checks a specified number of machines specific features/processes',
		'dump'	:	'write a json file of the specified machine'
	}
	spc = ' '*4
	if help_f in help_methods:
		print spc,help_f , '\t' , help_methods[help_f]
	elif help_f == None:
		print '\nHelp Commands:\n'
		for k,v in help_methods.items():
			print spc,k,'\t',v
	print '\n',
	

# TODO: come up with a grammar file for how diffos argument parsing works and how it applies to the command line and the functions within this library
if __name__ == "__main__":
	import optparse
	l = sys.argv[1:]
	# parse l with optparse
	if l[0] == 'help':
		helper()
