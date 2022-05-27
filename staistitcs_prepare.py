from collections import Counter
import json
import pandas as pd

with open("a12_raw_prep_stat.json", 'r', encoding='utf-8') as f:
    data = json.load(f)

parts_of_speech = {}

for text in data:
    for sent in text:
    
        #counter = 0
        for k, v in sent.items():
            if k == 'POS':
                #print(k, v)
                if v in parts_of_speech:
                    parts_of_speech[v] = parts_of_speech[v] +1
                else:
                    parts_of_speech[v] = 0
gram_info = {}
for text in data:
    for sent in text:

        # counter = 0
        for k, v in sent.items():
            if k == 'GRAM_INF':
                # print(k, v)
                if v in gram_info:
                    gram_info[v] = gram_info[v] + 1
                else:
                    gram_info[v] = 0

dependencies = {}
for text in data:
    for sent in text:

        # counter = 0
        for k, v in sent.items():
            if k == 'DEP':

                if v in dependencies:
                    dependencies[v] = dependencies[v] + 1
                else:
                    dependencies[v] = 0

cnt = Counter(parts_of_speech).most_common()
cnt2 = Counter(gram_info).most_common()
cnt3 = Counter(dependencies).most_common()

dframe = pd.DataFrame(cnt, columns=['Part_of_speech', 'Count'])
dframe.to_csv('a12_statistics_prepared.csv')
dframe2 = pd.DataFrame(cnt2, columns=["Grammatical_info", 'Count'])
dframe2.to_csv('a12_statistics_grammatical_info.csv')
dframe3 = pd.DataFrame(cnt3, columns=["Dependencies", 'Count'])
dframe3.to_csv('a12_statistics_dependencies.csv')