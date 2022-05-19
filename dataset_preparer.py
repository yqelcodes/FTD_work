import csv
with open("new_representative_all.csv","rt") as source:
    rdr = csv.reader(source)
    with open("new_topics_all_topics.csv","wt") as result:
        wtr = csv.writer(result)
        for r in rdr:
            wtr.writerow((r[0], r[1], r[2], r[3]))