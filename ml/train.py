#!/usr/bin/env python
# coding: utf-8

# In[1]:


import generate

data = generate.generate_train_data()
#
# for obj in tqdm(data):
#     text = obj[0] + '\n'
#     labels = obj[1]['entities']
#     doc = nlp.make_doc(text)
#     ents = []
#     for start, end, label in labels:
#         span = doc.char_span(start, end, label=label, alignment_mode="expand")
#         if span is None:
#             print("Skipping entity ({}-{}) in {}".format(start, end, text))
#         else:
#             ents.append(span)
#     filtered_ents = filter_spans(ents)
#     doc.ents = filtered_ents
#     doc_bin.add(doc)
# 
# doc_bin.to_disk("training_data.spacy")  # save the docbin object


# In[3]:


# use the training data to train the ner model
import spacy
import random
import warnings
from spacy.training import Example
from spacy.util import minibatch, compounding
from tqdm import tqdm

# spacy.require_gpu()
# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

# Create a blank NER model and add it to the pipeline
ner = nlp.get_pipe("ner")

# Add your custom entity labels here
labels = [ent[2] for d in data for ent in d[1]['entities']]

# Add the labels to the NER model
for label in labels:
    ner.add_label(label)

# In[4]:

print(len(data))

other_pipes = [pipe for pipe in nlp.pipe_names if pipe != "ner"]
with nlp.select_pipes(enable=["ner"]), warnings.catch_warnings():
    # Show warnings for misaligned entity spans once
    warnings.filterwarnings("once", category=UserWarning, module='spacy')

    # Reset and initialize the weights randomly – but only if we're
    # training a new model
    # optimizer = nlp.begin_training()
    for itn in tqdm(range(100)):
        random.shuffle(data)
        losses = {}
        # Batch up the examples using spaCy's minibatch
        batches = minibatch(data, size=compounding(4.0, 32.0, 1.01))
        for batch in batches:
            texts, annotations = zip(*batch)
            example = []
            # Update the example format to match spaCy v3
            for i in range(len(texts)):
                doc = nlp.make_doc(texts[i])
                example.append(Example.from_dict(doc, annotations[i]))

            # Update the model with the examples
            nlp.update(example, drop=0.2, losses=losses)
        print("Losses", losses)

# In[ ]:


# test the trained model
text = """
alpha2,English
aa,Afar
ab,Abkhazian
ae,Avestan
af,Afrikaans
ak,Akan
am,Amharic
an,Aragonese
ar,Arabic
as,Assamese
av,Avaric
ay,Aymara
az,Azerbaijani
ba,Bashkir
be,Belarusian
bg,Bulgarian
bh,Bihari languages
bi,Bislama
bm,Bambara
bn,Bengali
bo,Tibetan
br,Breton
bs,Bosnian
ca,Catalan; Valencian
ce,Chechen
ch,Chamorro
co,Corsican
cr,Cree
cs,Czech
cu,Church Slavic; Old Slavonic; Church Slavonic; Old Bulgarian; Old Church Slavonic
cv,Chuvash
cy,Welsh
da,Danish
de,German
dv,Divehi; Dhivehi; Maldivian
dz,Dzongkha
ee,Ewe
el,"Greek, Modern (1453-)"
en,English
eo,Esperanto
es,Spanish; Castilian
et,Estonian
eu,Basque
fa,Persian
ff,Fulah
fi,Finnish
fj,Fijian
fo,Faroese
fr,French
fy,Western Frisian
ga,Irish
gd,Gaelic; Scottish Gaelic
gl,Galician
gn,Guarani
gu,Gujarati
gv,Manx
ha,Hausa
he,Hebrew
hi,Hindi
ho,Hiri Motu
hr,Croatian
ht,Haitian; Haitian Creole
hu,Hungarian
hy,Armenian
hz,Herero
ia,Interlingua (International Auxiliary Language Association)
id,Indonesian
ie,Interlingue; Occidental
ig,Igbo
ii,Sichuan Yi; Nuosu
ik,Inupiaq
io,Ido
is,Icelandic
it,Italian
iu,Inuktitut
ja,Japanese
jv,Javanese
ka,Georgian
kg,Kongo
ki,Kikuyu; Gikuyu
kj,Kuanyama; Kwanyama
kk,Kazakh
kl,Kalaallisut; Greenlandic
km,Central Khmer
kn,Kannada
ko,Korean
kr,Kanuri
ks,Kashmiri
ku,Kurdish
kv,Komi
kw,Cornish
ky,Kirghiz; Kyrgyz
la,Latin
lb,Luxembourgish; Letzeburgesch
lg,Ganda
li,Limburgan; Limburger; Limburgish
ln,Lingala
lo,Lao
lt,Lithuanian
lu,Luba-Katanga
lv,Latvian
mg,Malagasy
mh,Marshallese
mi,Maori
mk,Macedonian
ml,Malayalam
mn,Mongolian
mr,Marathi
ms,Malay
mt,Maltese
my,Burmese
na,Nauru
nb,"Bokmål, Norwegian; Norwegian Bokmål"
nd,"Ndebele, North; North Ndebele"
ne,Nepali
ng,Ndonga
nl,Dutch; Flemish
nn,"Norwegian Nynorsk; Nynorsk, Norwegian"
no,Norwegian
nr,"Ndebele, South; South Ndebele"
nv,Navajo; Navaho
ny,Chichewa; Chewa; Nyanja
oc,Occitan (post 1500)
oj,Ojibwa
om,Oromo
or,Oriya
os,Ossetian; Ossetic
pa,Panjabi; Punjabi
pi,Pali
pl,Polish
ps,Pushto; Pashto
pt,Portuguese
qu,Quechua
rm,Romansh
rn,Rundi
ro,Romanian; Moldavian; Moldovan
ru,Russian
rw,Kinyarwanda
sa,Sanskrit
sc,Sardinian
sd,Sindhi
se,Northern Sami
sg,Sango
si,Sinhala; Sinhalese
sk,Slovak
sl,Slovenian
sm,Samoan
sn,Shona
so,Somali
sq,Albanian
sr,Serbian
ss,Swati
st,"Sotho, Southern"
su,Sundanese
sv,Swedish
sw,Swahili
ta,Tamil
te,Telugu
tg,Tajik
th,Thai
ti,Tigrinya
tk,Turkmen
tl,Tagalog
tn,Tswana
to,Tonga (Tonga Islands)
tr,Turkish
ts,Tsonga
tt,Tatar
tw,Twi
ty,Tahitian
ug,Uighur; Uyghur
uk,Ukrainian
ur,Urdu
uz,Uzbek
ve,Venda
vi,Vietnamese
vo,Volapük
wa,Walloon
wo,Wolof
xh,Xhosa
yi,Yiddish
yo,Yoruba
za,Zhuang; Chuang
zh,Chinese
zu,Zulu
"""
nlp2 = spacy.load("en_core_web_sm")
doc = nlp(text)
print("Entities", [(ent.text, ent.label_) for ent in doc.ents])
doc = nlp2(text)
print("Entities", [(ent.text, ent.label_) for ent in doc.ents])
