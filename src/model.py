import spacy
import random

model = spacy.load("en_core_web_sm")
# merge_ncs = model.create_pipe("merge_noun_chunks")
# model.add_pipe(merge_ncs)

TRAIN_DATA = [
    ("multiply value by orange", {"tags": ["VB", "NN", "IN", "NN"]})
]

def train_model(n_iter=5):

    global model

    disabled = model.disable_pipes("parser", "ner")
    optimizer = model.begin_training()
    for i in range(n_iter):
        random.shuffle(TRAIN_DATA)
        for text, annotations in TRAIN_DATA:
            model.update([text], [annotations], sgd=optimizer)
    
    disabled.restore()

    merge_ncs = model.create_pipe("merge_noun_chunks")
    model.add_pipe(merge_ncs)
    model.to_disk("./model")

def test_model():

    nlp = spacy.load("model")
    doc = nlp("divide the orange monkey by 9")

    for token in doc:
        print(token.tag_)

train_model()
test_model()