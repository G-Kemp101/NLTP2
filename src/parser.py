# A recursive descent parser for a simple grammar to split up
# imperative verb phrases

class rdp:

    def __init__(self, doc):
        self.doc = doc
        self.pos = 0
        self.current_token = doc[self.pos]
    
    def get_next_token(self):
        self.pos += 1
        if self.pos >= len(self.doc):
            self.current_token = "EOF"
        else:
            self.current_token = self.doc[self.pos]
    
    def parse_nn(self):
        if self.current_token.tag_ == "NN" or self.current_token.tag_ == "SYM" or self.current_token.like_num:
            print(self.current_token.text)
            self.get_next_token()
            return
        else:
            print("ERR")
       
    def parse_verb(self):
        if self.current_token.tag_ != "VB":
            print("ERR")
        else:
            print(self.current_token.text)
            self.get_next_token()
            return
    
    def parse_expr(self):
        if self.current_token.tag_ == "IN":
            print(self.current_token.text)
            self.get_next_token()
            self.parse_nn()
            self.parse_nn()
            return
        else:
            self.parse_nn()
            if self.current_token.tag_ == "IN" or self.current_token.tag_ == "TO":
                print(self.current_token.text)
                self.get_next_token()
                self.parse_nn()
            return

    def parse_doc(self):
        self.parse_verb()
        self.parse_expr()
