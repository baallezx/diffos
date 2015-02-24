import json
import yaml

# TODO: create a method to pass in a stack that can basically represent a rodmap to a dictionary query.
# -------------------------------------------------------------
# Ex. ["id","name","s5"]
#	{
#		id:{
#			code:{
#				number: 89237346234,
#				securty-pin: 3328,
#				access: "restricted"
#			},
#			name:{
#				s1: 0x3452
#				s3: 0x7221
#				s5: 0x8911
#			}
#		}
#	}
# will return the value 0x8911
# -------------------------------------------------------------

def search(d,key):
	"""
	finds and returns a specific value from the nested hash.
	d = nested dictionary
	key = search parameter... (this should be able to be converted betweeen string, int, etc to make finding things easier. I dont know if there are rules on values in json.)
	"""
	return dfs(d,key)

def search_stack(d, keys=[]):
	"""
	depth-first search of the nested hash for a consecutive graph traversal.
	"""
	if isinstance(keys, list):
		pass
	else:
		# TODO: raise a custom exception here for a bad parameter...
		raise Exception

def dfs(jsn,key):
	"""
	depth-first search of the nested hash
	"""
	if isinstance(jsn, dict):
		for k,v in jsn.items():
			dfs(jsn[k], key)
	elif isinstance(jsn, list):
		for i in jsn:
			dfs(jsn[i],key)
	# TODO: make the below statement be a `elif` that contains all the acceptable data types for a dictionary key/value
	else:
		if jsn == key:
			# TODO: this should not return true but should return excatly where the instance is located at. ie. a pointer of some sort.
			return True

if __name__ == "__main__":
	r = open('facebook.json','r').read()
	j = json.loads(r)
	dfs(j,"id")
