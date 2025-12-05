class GameState:
    def __init__(self, target_word):
        self.target_word = target_word.upper()
        self.guesses = []
        self.max_attempts = 6

    def add_guess(self, guess):
        self.guesses.append(guess.upper())

    def check_guess(self, guess):
        guess = guess.upper()
        result = []
        # Use simple frequency accounting for better Wordle logic
        target = list(self.target_word)
        # First pass for greens
        feedback = [''] * len(guess)
        for i, ch in enumerate(guess):
            if i < len(target) and ch == target[i]:
                feedback[i] = 'green'
                target[i] = None
        # Second pass for yellows and grays
        for i, ch in enumerate(guess):
            if feedback[i] == 'green':
                continue
            if ch in target:
                feedback[i] = 'yellow'
                target[target.index(ch)] = None
            else:
                feedback[i] = 'gray'
        return feedback

    def is_game_over(self):
        return len(self.guesses) >= self.max_attempts or self.target_word in self.guesses
