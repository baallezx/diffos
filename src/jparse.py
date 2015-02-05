import json

# TODO: get this fully implemented because it is important for diffos

def g():
	pass

def dfs(d):
	if isinstance(d,dict):
		k = d.iterkeys()
		for i in k:
			print i
			if isinstance(i,str):
				print '< ',i,',',d[i],' >'
			dfs(d[i])
	elif isinstance(d,list):
		for i in d:
			print i
			if not isinstance(i,str):
				dfs(i)

if __name__ == "__main__":
	r = open('animals.json','r').read()
	j = json.loads(r)
	dfs(j)
