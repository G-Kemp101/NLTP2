from model import model
import parser

class nltp:

    def __init__(self):
        self.nlp = model

    def compile(self, line):
        self.doc = self.nlp(line)
        self.print_doc()
        parse = parser.rdp(self.doc)
        parse.parse_doc()

    def print_doc(self):

        for token in self.doc:
            print(token.text, token.tag_)

