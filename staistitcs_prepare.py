from collections import Counter
import json
import pandas as pd

with open("a1_raw_prep_stat.json", 'r', encoding='utf-8') as f:
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
                
cnt = Counter(parts_of_speech).most_common()
print(parts_of_speech)
print(cnt)

dframe = pd.DataFrame(cnt, columns=['Part_of_speech', 'Count']) 
dframe.to_csv('a1_statistics_prepared.csv') 