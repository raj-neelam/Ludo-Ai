import pygame as pg
import numpy as np

class LudoRenderer:
    def __init__(self, width=400, height=400):
        pg.init()
        self.colors = ["red", "blue", "yellow", "green"]
        self.screen = pg.display.set_mode((width, height), pg.RESIZABLE)
        pg.display.set_caption("Ludo AI")
        self.clock = pg.time.Clock()
        self.board_image = pg.image.load("board.png")  # Ensure you have a board.png file
        self.center_of_board = (0,0)
        self.font = pg.font.Font(None, 36)
        self.inc=0
    
    def write(self, text, color, pos):
        text = self.font.render(str(text), True, color)
        text_rect = text.get_rect(center=pos)
        self.screen.blit(text, text_rect)

    def draw_board(self):
        self.inc+=0.05
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
        self.center_of_board = np.array(board_rect.center)

        # setting the length
        self.length = board_rect.width*0.3

    def draw_player(self, engine):
        for player in engine.players:
            self.draw_player_pice(player)

    def draw_player_pice(self, player):
        for pice in player.pieces:
            self.draw_pice(player.player_number, pice)
    
    def draw_pice(self, color, pice):
        pos = np.array([0,1])

        pos = self.offset_pos(pos, pice)
        
        # rotate_pos
        rotate_ang = (3.1415/2) * color
        pos = np.array([pos[0]*np.cos(rotate_ang)-pos[1]*np.sin(rotate_ang),
                        pos[0]*np.sin(rotate_ang)+pos[1]*np.cos(rotate_ang)])

        # translating
        pos = ((pos*self.length) + self.center_of_board) 
        # drawing
        circle_size = 15
        pg.draw.circle(self.screen, "white", pos, circle_size)
        pg.draw.circle(self.screen, self.colors[color], pos, circle_size, 5)
        pg.draw.circle(self.screen, "black", pos, circle_size, 1)
        self.write(pice.Pid, "black", pos)
        
    def offset_pos(self, pos, pice):
        if pice.position==0:
            if pice.Pid==0:return pos+np.array([-1.17, -0.25])
            elif pice.Pid==1:return pos+np.array([-1.17, 0.19])
            elif pice.Pid==2:return pos+np.array([-0.75, 0.19])
            elif pice.Pid==3:return pos+np.array([-0.75, -0.25])
        elif pice.position==1:return pos+np.array([-0.21, 0.3])
        return pos
    def render(self, engine):
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                elif event.type == pg.VIDEORESIZE:
                    self.screen = pg.display.set_mode((event.w, event.h), pg.RESIZABLE)

            self.draw_board()
            self.draw_player(engine)
            pg.display.flip()
            self.clock.tick(30)

        pg.quit()