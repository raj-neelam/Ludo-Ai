from renderer import LudoRenderer
from engine import LudoEngine
import pygame as pg

def main():
    renderer = LudoRenderer(500,500)
    engine = LudoEngine()

    renderer.render() 

if __name__ == "__main__":
    main()