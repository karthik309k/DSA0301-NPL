class SimpleParser:
    def __init__(self, grammar):
        self.grammar = grammar
        self.tokens = []
        self.current_token = 0

    def parse(self, input_string):
        self.tokens = input_string.split()
        self.current_token = 0

        try:
            self.parse_sentence()
            print("Parsing successful!")
        except Exception as e:
            print(f"Parsing error: {e}")

    def match(self, expected_token):
        if self.current_token < len(self.tokens) and self.tokens[self.current_token] == expected_token:
            self.current_token += 1
        else:
            raise Exception(f"Expected '{expected_token}' but found '{self.tokens[self.current_token]}'")

    def parse_sentence(self):
        self.parse_subject()
        self.match('VERB')
        self.parse_object()

    def parse_subject(self):
        self.match('NOUN')

    def parse_object(self):
        self.match('NOUN')

# Example usage
grammar_rules = {
    'sentence': [('subject', 'VERB', 'object')],
    'subject': [('NOUN',)],
    'object': [('NOUN',)],
}

parser = SimpleParser(grammar_rules)
input_string = "cat VERB dog"
parser.parse(input_string)
