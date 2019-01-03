from bs4 import BeautifulSoup 
from bs4.element import Tag
import nltk

# Read data file and parse the XML
with open("../seed/usefull/umbilical_cord.xml", "r") as infile:
    soup = BeautifulSoup(infile, 'html.parser')

docs = []
for elem in soup.find_all("sentence"):
    texts = []
   
    for c in elem:
        if type(c) == Tag:
            # part of a named entity
            for j in c.text.split(" "):
                if len(j) > 0:
                    texts.append((j, "N")) 
        else:
            # irrelevant word
            for j in c.replace(",", "").replace("\"", "").split(" "):
                if len(j) > 0:
                    texts.append((j, "I")) 
        
            

    docs.append(texts)

data = []
for i, doc in enumerate(docs):

    # Obtain the list of tokens in the document
    tokens = [t for t, label in doc]

    # Perform POS tagging
    tagged = nltk.pos_tag(tokens)

    # Take the word, POS tag, and its label
    data.append([(w, pos, label) for (w, label), (word, pos) in zip(doc, tagged)])


output = open("CRF_umbilical_cord.txt", "w")
for i in data:
    output.write('\n'.join("%s, %s, %s" % x for x in i))

output.close()