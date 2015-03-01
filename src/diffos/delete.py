def cycle(key,element,path_string=""):
	if isinstance(element, dict):
		for k,v in element.items():
			if k == key:
				print "\n\n\n\t\tFOUND\n\n\n" , path_string+":"+key
				return path_string+":"+key
			else:
				path_string = path_string+":"+k
				cycle(key, element[k], path_string)
	if isinstance(element, list):
		for i in element:
			if i == key:
				return path_string+">"+key
	if isinstance(element, set):
		pass
	if isinstance(element, tuple):
		pass
	# return path_string

path = ""
def cyclone(key,element,path_str=""):
	print path_str
	if isinstance(element,dict):
		for k,v in element.items():
			if k == key:
				print "\n\nFOUND\n\n"
				return path_str + ":" + key
			cyclone(key, element[k], path_str+":"+k)

def cycle(key,element,path_string=""):
	if isinstance(element,dict):
		c = element.get(key, None)
		if c == None:
			pass

if __name__ == "__main__":
	db = {
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
		},
	}
	print cyclone("d",db,"")
