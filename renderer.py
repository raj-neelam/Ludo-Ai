import pygame as pg

class LudoRenderer:
    def __init__(self, width=400, height=400):
        pg.init()
        self.screen = pg.display.set_mode((width, height), pg.RESIZABLE)
        pg.display.set_caption("Ludo AI")
        self.clock = pg.time.Clock()
        self.board_image = pg.image.load("board.png")  # Ensure you have a board.png file

    def draw_board(self):
        self.screen.fill((255, 255, 255))
        board_rect = self.board_image.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2))
        self.screen.blit(self.board_image, board_rect)

    def render(self):
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                elif event.type == pg.VIDEORESIZE:
                    self.screen = pg.display.set_mode((event.w, event.h), pg.RESIZABLE)

            self.draw_board()
            pg.display.flip()
            self.clock.tick(30)

        pg.quit()