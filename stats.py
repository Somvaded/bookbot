def total_words(contents):
	words = contents.split()
	return len(words)
	
def num_stats(contents):
	contents = contents.lower()
	map = {}

	for char in contents:
		if char in map:
			map[char]+=1
		else:
			map[char]=1
	return map

def sort_on(map):
	return map["num"]

def sort_map(contents):
	map = num_stats(contents)
	list = []
	for x in map:
		temp = {"char":x,"num":map[x]}
		list.append(temp)
	list.sort(reverse = True, key = sort_on)
	return list