from graph.files import read_data_from_file

friends = read_data_from_file()

universities = dict()

for friend in friends:
    del friend['friends']
    del friend['id']

for friend in friends:
    if 'university_name' in friend.keys() and not friend['university'] == 0:
        if friend['university_name'] in universities:
            universities[friend['university_name']] += 1
        else:
            universities[friend['university_name']] = 1

print(universities)
