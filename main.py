from renderer import LudoRenderer
from engine import LudoEngine
import pygame as pg

def main():
    renderer = LudoRenderer(500,500)
    engine = LudoEngine()
    engine.players[0].pieces[0].position=1
    renderer.render(engine) 

if __name__ == "__main__":
    main()