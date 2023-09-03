import json

json_file = open('all_sections.json', 'r')
json_hash = json.load(json_file)
json_file.close()

print(json_hash)

