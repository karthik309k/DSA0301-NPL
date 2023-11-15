class EarleyParser:
    def __init__(self, grammar):
        self.grammar = grammar

    def parse(self, input_string, start_symbol):
        chart = [set() for _ in range(len(input_string) + 1)]
        self.predict(0, start_symbol, chart)

        for i in range(len(input_string) + 1):
            while True:
                added = False
                for item in chart[i]:
                    if not item.completed() and item.next_symbol() in self.grammar:
                        self.predict(i, item.next_symbol(), chart)
                    elif not item.completed() and item.next_symbol() == input_string[i]:
                        self.scan(i, item, chart)
                    elif item.completed():
                        self.complete(i, item, chart)
                        added = True
                if not added:
                    break

        # Check if the input string can be derived from the start symbol
        final_item = self.find_completed_item(len(input_string), start_symbol, chart)
        return final_item is not None

    def predict(self, position, non_terminal, chart):
        for production in self.grammar[non_terminal]:
            chart_item = ChartItem(non_terminal, production, 0, position)
            chart[position].add(chart_item)

    def scan(self, position, item, chart):
        next_position = position + 1
        next_item = ChartItem(item.non_terminal, item.production, item.dot + 1, item.start_position)
        chart[next_position].add(next_item)

    def complete(self, position, item, chart):
        for completed_item in chart[item.start_position]:
            if not completed_item.completed() and completed_item.next_symbol() == item.non_terminal:
                new_item = ChartItem(completed_item.non_terminal, completed_item.production, completed_item.dot + 1, completed_item.start_position)
                chart[position].add(new_item)

    def find_completed_item(self, position, non_terminal, chart):
        for item in chart[position]:
            if item.non_terminal == non_terminal and item.completed():
                return item
        return None


class ChartItem:
    def __init__(self, non_terminal, production, dot, start_position):
        self.non_terminal = non_terminal
        self.production = production
        self.dot = dot
        self.start_position = start_position

    def completed(self):
        return self.dot == len(self.production)

    def next_symbol(self):
        return self.production[self.dot] if not self.completed() else None


# Example usage
grammar_rules = {
    'S': [['NP', 'VP']],
    'NP': [['Det', 'N'], ['NP', 'PP']],
    'VP': [['V', 'NP'], ['VP', 'PP']],
    'PP': [['P', 'NP']],
    'Det': ['the', 'a'],
    'N': ['cat', 'dog', 'bird'],
    'V': ['chased', 'caught'],
    'P': ['with', 'in']
}

earley_parser = EarleyParser(grammar_rules)
input_string = "the cat chased the bird with the dog"
start_symbol = 'S'
result = earley_parser.parse(input_string.split(), start_symbol)

print(f"Is the input string '{input_string}' derived from the start symbol '{start_symbol}'? {result}")
