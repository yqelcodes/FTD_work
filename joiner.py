import json

files = ['a1.json', 'a11.json', 'a12.json']



def merge_JsonFiles(filename):
    result = list()
    for f1 in filename:
        with open(f1, 'r') as infile:
            result.extend(json.load(infile))

    with open('full_data.json', 'w') as output_file:
        json.dump(result, output_file)

merge_JsonFiles(files)