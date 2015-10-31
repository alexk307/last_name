from metaphone import doublemetaphone
from collections import defaultdict
import json


if __name__ == '__main__':
	data = {}
	name_file = open("census_names.csv", "r")
	out_file = open("name_file.json", "w")
	for line in name_file:
		name = line.split(",")[0]
		data[name] = doublemetaphone(name)[0]


	sorted_data = defaultdict(list)
	for res in sorted(data.items(), key=lambda x: x[1]):
		sorted_data[res[1]].append(res[0])
	
	out_file.write(str(json.dumps(dict(sorted_data))))


