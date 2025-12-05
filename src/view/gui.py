import pygame

GREEN = (83, 141, 78)
YELLOW = (181, 159, 59)
GRAY = (58, 58, 60)
BG = (255,255,255)
TEXT = (0,0,0)
BOX_BG = (238,238,238)

class GameGUI:
    def __init__(self, screen, game_state, input_handler):
        self.screen = screen
        self.game_state = game_state
        self.input_handler = input_handler
        self.font = pygame.font.SysFont(None, 48)
        self.small = pygame.font.SysFont(None, 24)
        self.cols = 5
        self.cell = 64
        self.margin = 20

    def draw_board(self):
        """
        Draws the game board with current guesses and feedback.
        """
        self.screen.fill(BG)
        # center board
        start_x = (self.screen.get_width() - (self.cell * self.cols)) // 2
        start_y = 40

        # Draw guesses
        for row in range(self.game_state.max_attempts):
            y = start_y + row * (self.cell + 8)
            if row < len(self.game_state.guesses):
                guess = self.game_state.guesses[row]
                feedback = self.game_state.check_guess(guess)
                for col, ch in enumerate(guess):
                    x = start_x + col * self.cell
                    color = GREEN if feedback[col]=='green' else YELLOW if feedback[col]=='yellow' else GRAY
                    pygame.draw.rect(self.screen, color, (x, y, self.cell-4, self.cell-4))
                    text = self.font.render(ch, True, (255,255,255))
                    self.screen.blit(text, (x + self.cell//3, y + self.cell//6))
            elif row == len(self.game_state.guesses):
                # current input row
                cur = self.input_handler.current_input
                for col in range(self.cols):
                    x = start_x + col * self.cell
                    pygame.draw.rect(self.screen, BOX_BG, (x, y, self.cell-4, self.cell-4))
                    if col < len(cur):
                        ch = cur[col]
                        text = self.font.render(ch, True, TEXT)
                        self.screen.blit(text, (x + self.cell//3, y + self.cell//6))

        # message
        if self.input_handler.message:
            msg = self.small.render(self.input_handler.message, True, (200,30,30))
            self.screen.blit(msg, (start_x, start_y + self.game_state.max_attempts * (self.cell+8) + 10))

        # If game over, show result
        if self.game_state.is_game_over():
            if self.game_state.target_word in self.game_state.guesses:
                end_msg = f'You win! Answer: {self.game_state.target_word}'
            else:
                end_msg = f'Game over. Answer: {self.game_state.target_word}'
            em = self.small.render(end_msg, True, TEXT)
            self.screen.blit(em, (start_x, start_y - 30))

        pygame.display.flip()
