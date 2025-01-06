import pygame as pg

class LudoRenderer:
    def __init__(self, width=400, height=400):
        pg.init()
        self.screen = pg.display.set_mode((width, height), pg.RESIZABLE)
        pg.display.set_caption("Ludo AI")
        self.clock = pg.time.Clock()
        self.board_image = pg.image.load("board.png")  # Ensure you have a board.png file
        self.center_of_board = (0,0)

    def draw_board(self):
        self.screen.fill("black")
        screen_width, screen_height = self.screen.get_size()
        image_width, image_height = self.board_image.get_size()
        
        # Calculate the aspect ratio
        aspect_ratio = image_width / image_height
        
        # Determine new dimensions while maintaining aspect ratio
        if screen_width / screen_height > aspect_ratio:
            new_height = screen_height
            new_width = int(new_height * aspect_ratio)
        else:
            new_width = screen_width
            new_height = int(new_width / aspect_ratio)
        
        # Scale the image to the new dimensions
        scaled_board_image = pg.transform.scale(self.board_image, (new_width, new_height))
        board_rect = scaled_board_image.get_rect(center=(screen_width // 2, screen_height // 2))
        
        # Blit the scaled image onto the screen
        self.screen.blit(scaled_board_image, board_rect)
        
        # setting the center of the board
        self.center_of_board = board_rect.center

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