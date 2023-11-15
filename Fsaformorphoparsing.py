class PluralizationMachine:
    def __init__(self):
        self.machine = {
            1: {'s': 2, 'x': 3},
            2: {'e': 4, 'y': 5},
            3: {'e': 4},
            4: {'s': 6},
            5: {'s': 6},
            6: {},
        }

    def generate_plural(self, singular):
        state = 1  
        for char in reversed(singular):
            if char in self.machine[state]:
                state = self.machine[state][char]
            else:
                return singular + 's'

        return singular
pluralizer = PluralizationMachine()
nouns = ["cat", "dog", "city", "boy", "box", "bus"]

for noun in nouns:
    plural = pluralizer.generate_plural(noun)
    print(f"Singular: {noun}, Plural: {plural}")
