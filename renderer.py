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
        elif pice.position==2:return pos+np.array([-0.21, 0.07])
        elif pice.position==3:return pos+np.array([-0.21, -0.15])
        elif pice.position==4:return pos+np.array([-0.21, -0.35])
        elif pice.position==5:return pos+np.array([-0.21, -0.55])


        elif pice.position==6:return pos+np.array([-0.41, -0.76])
        elif pice.position==7:return pos+np.array([-0.62, -0.76])
        elif pice.position==8:return pos+np.array([-0.83, -0.76])
        elif pice.position==9:return pos+np.array([-1.04, -0.76])
        elif pice.position==10:return pos+np.array([-1.26, -0.76])

        elif pice.position==11:return pos+np.array([-1.48, -0.76])
        elif pice.position==12:return pos+np.array([-1.48, -0.98])
        elif pice.position==13:return pos+np.array([-1.48, -1.21])

        elif pice.position==14:return pos+np.array([-1.26, -1.21])
        elif pice.position==15:return pos+np.array([-1.04, -1.21])
        elif pice.position==16:return pos+np.array([-0.83, -1.21])
        elif pice.position==17:return pos+np.array([-0.62, -1.21])
        elif pice.position==18:return pos+np.array([-0.41, -1.21])


        elif pice.position==19:return pos+np.array([-0.21, -1.43])
        elif pice.position==20:return pos+np.array([-0.21, -1.64])
        elif pice.position==21:return pos+np.array([-0.21, -1.85])
        elif pice.position==22:return pos+np.array([-0.21, -2.06])
        elif pice.position==23:return pos+np.array([-0.21, -2.27])

        elif pice.position==24:return pos+np.array([-0.21, -2.48])
        elif pice.position==25:return pos+np.array([-0, -2.48])
        elif pice.position==26:return pos+np.array([0.21, -2.48])

        elif pice.position==27:return pos+np.array([0.21, -2.27])
        elif pice.position==28:return pos+np.array([0.21, -2.06])
        elif pice.position==29:return pos+np.array([0.21, -1.85])
        elif pice.position==30:return pos+np.array([0.21, -1.64])
        elif pice.position==31:return pos+np.array([0.21, -1.43])


        elif pice.position==32:return pos+np.array([0.42, -1.21])
        elif pice.position==33:return pos+np.array([0.63, -1.21])
        elif pice.position==34:return pos+np.array([0.84, -1.21])
        elif pice.position==35:return pos+np.array([1.05, -1.21])
        elif pice.position==36:return pos+np.array([1.27, -1.21])

        elif pice.position==37:return pos+np.array([1.48, -1.21])
        elif pice.position==38:return pos+np.array([1.48, -0.98])
        elif pice.position==39:return pos+np.array([1.48, -0.76])

        elif pice.position==40:return pos+np.array([1.27, -0.76])
        elif pice.position==41:return pos+np.array([1.05, -0.76])
        elif pice.position==42:return pos+np.array([0.84, -0.76])
        elif pice.position==43:return pos+np.array([0.63, -0.76])
        elif pice.position==44:return pos+np.array([0.42, -0.76])


        elif pice.position==45:return pos+np.array([0.22, -0.55])
        elif pice.position==46:return pos+np.array([0.22, -0.35])
        elif pice.position==47:return pos+np.array([0.22, -0.15])
        elif pice.position==48:return pos+np.array([0.22, 0.07])
        elif pice.position==49:return pos+np.array([0.22, 0.3])

        elif pice.position==50:return pos+np.array([0.22, 0.5])
        elif pice.position==51:return pos+np.array([0, 0.5])

        elif pice.position==52:return pos+np.array([0, 0.3])
        elif pice.position==53:return pos+np.array([0, 0.07])
        elif pice.position==54:return pos+np.array([0, -0.15])
        elif pice.position==55:return pos+np.array([0, -0.35])
        elif pice.position==56:return pos+np.array([0, -0.55])

        elif pice.position==57:return pos+np.array([0, -0.79])

        else:
            print("error Position :",  pice.position)
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
    
    def update(self, engine):
        for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                elif event.type == pg.VIDEORESIZE:
                    self.screen = pg.display.set_mode((event.w, event.h), pg.RESIZABLE)
        self.draw_board()
        self.draw_player(engine)
        pg.display.flip()
        self.clock.tick(30)