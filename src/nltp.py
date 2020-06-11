from model import model
import parser

class nltp:

    def __init__(self):
        self.nlp = model

    def compile(self, line):
        doc = self.nlp(line)
        parse = parser.rdp(doc)
        parse.parse_doc()


