import json
from metaphone import doublemetaphone
from .name_file import names


def levenshtein_distance(s1, s2):
    """
    Performs Levenshtein distance on two strings
    :param s1: String 1
    :param s2: String 2
    :return: L-Distance between two s1 and s2
    """
    if len(s1) > len(s2):
        s1, s2 = s2, s1
    distances = range(len(s1) + 1)
    for index2, char2 in enumerate(s2):
        new_distances = [index2 + 1]
        for index1, char1 in enumerate(s1):
            if char1 == char2:
                new_distances.append(distances[index1])
            else:
                new_distances.append(1 + min((distances[index1],
                                              distances[index1 + 1],
                                              new_distances[-1])))
        distances = new_distances
    return distances[-1]


def suggest_name(name):
    """
    Suggest names based on a name
    :param name: The name to generate matches on
    :return:
    """
    name = name.upper()
    data = names
    dmeta = doublemetaphone(name)[0]

    temp_data = {}
    if dmeta not in data:
        return [()]
    else:
        for lname in data[dmeta]:
            temp_data[lname] = levenshtein_distance(name, lname)
    return sorted(temp_data.items(), key=lambda x: x[1])
