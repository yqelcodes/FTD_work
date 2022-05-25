from corpy.udpipe import Model
import json
import re


model = Model('russian-taiga-ud-2.5-191206.udpipe')

with open("a12_prep.json", 'r', encoding='utf-8') as f:
    text = json.load(f)

clear_text = []
for elem in text:
    antilink = elem['Text']
    data = re.sub(r'[https:\/\/youtu.be\/]+\w+', ' ', antilink)
    data = re.sub(r'[^\w\s]', '', data)
    clear_text.append(data)


with open('a12_raw_prep_stat.json', 'w', encoding='utf-8') as f:
    for i in clear_text:
        sents = model.process(i)

        mylst = []
        for sent in sents:
            sentlist = []
            for word in sent.words:
                sentlist.append({'form': word.form,
                                 'LEMMA': word.lemma,
                                 'POS': word.upostag,
                                 'GRAM_INF': word.feats,
                                 'DEP': word.deprel
                                 })
            mylst.append(sentlist)

    json.dump(mylst, f, ensure_ascii=False, indent=4)
