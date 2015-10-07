import json
import sys
from metaphone import doublemetaphone


def levenshteinDistance(s1,s2):
	if len(s1) > len(s2):
		s1,s2 = s2,s1
	distances = range(len(s1) + 1)
	for index2,char2 in enumerate(s2):
		newDistances = [index2+1]
		for index1,char1 in enumerate(s1):
			if char1 == char2:
				newDistances.append(distances[index1])
			else:
				newDistances.append(1 + min((distances[index1], distances[index1+1], newDistances[-1])))
		distances = newDistances
	return distances[-1]

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print "Usage: %s <last name>" % sys.argv[0]
		sys.exit(1)
	lastname = sys.argv[1].upper()

	data_file = open("name_file.json", "r")
	data = json.loads(data_file.readlines()[0])
	
	dmeta = doublemetaphone(lastname)[0]


	temp_data = {}
	if dmeta not in data:
		print "No data exists"
	else:
		for lname in data[dmeta]:
			temp_data[lname] = levenshteinDistance(lastname, lname)

	print sorted(temp_data.items(), key=lambda x: x[1])


