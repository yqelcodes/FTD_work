from razdel import sentenize
import pprint
import json

with open("a12_prep.json") as data:
    initial_data = json.load(data)

_data = [] # store all texts

for text in initial_data:
    _data.append(text["Text"])

pre_calc = [] # stores all razdel calculated substrings

for text in _data:
    pre_calc.append(list(sentenize(text)))

calc = [] # stores all lengths of substrings

for text in pre_calc:
    for sentence in text:
        calc.append(getattr(sentence, 'stop') - getattr(sentence, 'start'))

final = sum(calc)/len(calc)

print(round(final, 2))