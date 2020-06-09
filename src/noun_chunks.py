from globals import model

def print_noun_chunks(line):
    doc = model(line)

    for chunk in doc.noun_chunks:
        print(chunk.text)