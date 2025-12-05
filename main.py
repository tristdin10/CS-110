import pygame, sys, os
from model.wordbank import WordBank
from model.gamestate import GameState
from controller.input_handler import InputHandler
from view.gui import GameGUI

def main():
    pygame.init()
    screen = pygame.display.set_mode((420, 600))
    pygame.display.set_caption('Wordle MVC - Pygame')
    clock = pygame.time.Clock()

    proj_dir = os.path.dirname(os.path.abspath(__file__))
    word_bank = WordBank(os.path.join(proj_dir, 'data', 'words.json'))
    target_word = word_bank.get_random_word()
    game_state = GameState(target_word)
    input_handler = InputHandler(game_state)
    gui = GameGUI(screen, game_state, input_handler)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            guess, _ = input_handler.handle_event(event)
        gui.draw_board()

        if game_state.is_game_over():
            # pause briefly to show final board
            pygame.time.wait(1500)
            running = False

        clock.tick(30)

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
