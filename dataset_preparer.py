import csv
import json
import pandas as pd
# with open("new_representative_all.csv","rt") as source:
#     rdr = csv.reader(source)
#     with open("new_topics_all_topics.csv","wt") as result:
#         wtr = csv.writer(result)
#         for r in rdr:
#             wtr.writerow((r[0], r[1], r[2], r[3]))
"""
legacy code up there
"""

with open('new_topics_a12_all.csv') as infile:
    reader = csv.DictReader(infile)
    out = [{"Text": row['Text']} for row in reader if row["Dominant_Topic"] == '30.0']

with open('a12_prep.json', 'w', encoding='utf-8') as outfile:
    json.dump(out, outfile, ensure_ascii=False, indent=4)

# df = pd.read_csv('new_topics_a1_all.csv')
# if df['Dominant_topic' == 17.0]:
    