import sys
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

def sentences_segmentation(file_name = None):
    if file_name == None:
        raw_text = open("../data/seed/Adipose Tissue.txt", "r").read()
    else:
        raw_text = open("../data/seed/" + file_name, "r").read()

    sent_tokenizer=nltk.data.load('tokenizers/punkt/english.pickle')
    return sent_tokenizer.tokenize(raw_text)


def pos_tag(text):
    tokens = word_tokenize(text)
    pos = nltk.pos_tag(tokens)
    #print(pos)
    return [i[1] for i in pos]

def is_candidate(sentence):
    candidate = False
    for i in sentence:
        if "V" in i:
            candidate = True
            break
    return candidate

file_name = None
if len(sys.argv) > 1:
    file_name = sys.argv[1]

print("Segmenting sentences")
sentences = sentences_segmentation(file_name)
candidate_sentences = []

print("pos tagging")
for sentence in sentences:
    pos = pos_tag(sentence)
    if is_candidate(pos):
        candidate_sentences.append(sentence)

print("writing")
s = open("../data/seed/" + file_name + "_sentencas_candidatas.txt", "w")
for i in candidate_sentences:
    s.write(i + "\n")

s.close()