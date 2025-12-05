import json, random, os

class WordBank:
    def __init__(self, filepath):
        filepath = os.path.abspath(filepath)
        with open(filepath, 'r') as f:
            self.words = [w.strip() for w in json.load(f) if w.strip()]
    def get_random_word(self):
        # return uppercase 5-letter word
        return random.choice(self.words).upper()
