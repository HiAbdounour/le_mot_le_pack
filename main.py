from noormiextracts import *
from menu import print_menu, choice_level
from game import build_level,play

# Init graphic window
init_graphic(500,500,"Le Mot")

# status booleans
running = True
in_menu = True
in_game = False

while running:
    if in_menu:
        clear_window(PYGAME_GRAY)
        BUTTONS_MENU_LIST = print_menu()
        chosen_word = ""
        click_pos = wait_clic()
        lvl = choice_level(BUTTONS_MENU_LIST,click_pos)
        if lvl!=-1:
            in_menu = False
            in_game = True
            chosen_word = build_level(lvl)

    if in_game:
        play(chosen_word)
        in_game = False
        in_menu = True

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False

            pygame.quit()
