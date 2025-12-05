import pygame

class InputHandler:
    def __init__(self, game_state):
        self.current_input = ''
        self.game_state = game_state
        self.message = ''

    def handle_event(self, event):
        """
        Processes a pygame event for user input.
        
        args: event (pygame.Event) - keyboard event to handle
        return: tuple (guess or None, message string)
        """
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if len(self.current_input) == 5:
                    guess = self.current_input.upper()
                    self.game_state.add_guess(guess)
                    self.current_input = ''
                    self.message = ''
                    return guess, ''
                else:
                    self.message = 'Guess must be 5 letters'
                    return None, self.message
            elif event.key == pygame.K_BACKSPACE:
                self.current_input = self.current_input[:-1]
            elif event.unicode.isalpha() and len(self.current_input) < 5:
                self.current_input += event.unicode.upper()
        return None, self.message
