from renderer import LudoRenderer
from engine import LudoEngine
import pygame as pg
import time

def main():
    renderer = LudoRenderer(500,500)
    engine = LudoEngine()
    
    game_end = False
    print("game started")
    t1 = time.time()
    while not game_end:
        game_end = engine.step()
        renderer.update(engine)
    pg.quit()
    print("game ended")
    print("time took :", time.time()-t1 )

if __name__ == "__main__":
    main()