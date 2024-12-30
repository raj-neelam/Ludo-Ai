from renderer import LudoRenderer
from engine import LudoEngine
import pygame as pg

def main():
    renderer = LudoRenderer(500,500)
    engine = LudoEngine()

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    steps = engine.roll_dice()
                    engine.move_current_player_piece(0, steps)  # Move the first piece of the current player

        renderer.draw_board()
        pg.display.flip()
        renderer.clock.tick(30)

    pg.quit()

if __name__ == "__main__":
    main()