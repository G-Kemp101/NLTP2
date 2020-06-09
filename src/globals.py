import spacy

model = spacy.load("en_core_web_sm")
merge_ncs = model.create_pipe("merge_noun_chunks")
model.add_pipe(merge_ncs)