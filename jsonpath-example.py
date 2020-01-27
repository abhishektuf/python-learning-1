import json
from jsonpath_ng import jsonpath,parse

with open("cloud.json", 'r') as json_file:
    json_data = json.load(json_file)
'''
print(json_data)
'''

jsonpath_expression=parse('$.ListBucketResult.Contents[*].Key')

for match in jsonpath_expression.find(json_data):
    print(f'Template name: {match.value}')