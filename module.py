from platform import python_compiler
import pygame
from subprocess import call
pygame.init()

FPS = 30
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (40, 40, 40)
RED = (255, 0, 0)
CRIMSON = (220, 20, 60)
ORANGE = (255, 127, 0)
GREEN = (45, 194, 31)

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Puzzle Fighter')

font_title = pygame.font.Font('Hello Avocado.ttf', 120)
font_content = pygame.font.Font('Hello Avocado.ttf', 60)

bg = pygame.image.load("module_photo.png").convert_alpha()
bg_rect = bg.get_rect()
bg_rect.topleft = (0,0)

title = font_title.render("Puzzle Fighter", True, RED)
title_rect = title.get_rect(center = (640,120))

minesweeper = font_content.render("Minesweeper", True, RED)
minesweeper_rect = minesweeper.get_rect(center = (640,250))

puzzle = font_content.render("Puzzle", True, RED)
puzzle_rect = puzzle.get_rect(center = (640,350))

suduko = font_content.render("Suduko", True, RED)
suduko_rect = suduko.get_rect(center = (640,450))

flipping_tile = font_content.render("Flipping Tile", True, RED)
flipping_tile_rect = flipping_tile.get_rect(center = (640,550))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.MOUSEBUTTONUP:
            if minesweeper_rect.collidepoint(event.pos):
                f=open("Minesweeper.py")
                exec(f.read())
                f.close()
            if puzzle_rect.collidepoint(event.pos):
                f=open("puzzle.py")
                exec(f.read())
                f.close()
            if suduko_rect.collidepoint(event.pos):
                f=open("sudoku.py")
                exec(f.read())
                f.close()
            if flipping_tile_rect.collidepoint(event.pos):
                f=open("flipping tiles.py")
                exec(f.read())
                f.close()
        
    screen.blit(bg,bg_rect)
    mouse_pos = pygame.mouse.get_pos()
    if minesweeper_rect.collidepoint(mouse_pos):
        pygame.draw.rect(screen,ORANGE,pygame.Rect(minesweeper_rect.left-5,minesweeper_rect.top,300,minesweeper_rect.bottom-minesweeper_rect.top),0,7)
    else:
        pygame.draw.rect(screen,GREY,pygame.Rect(minesweeper_rect.left-5,minesweeper_rect.top,300,minesweeper_rect.bottom-minesweeper_rect.top),0,7)
        
    if puzzle_rect.collidepoint(mouse_pos):
        pygame.draw.rect(screen,ORANGE,pygame.Rect(minesweeper_rect.left-5,puzzle_rect.top,300,minesweeper_rect.bottom-minesweeper_rect.top),0,7)
    else:
        pygame.draw.rect(screen,GREY,pygame.Rect(minesweeper_rect.left-5,puzzle_rect.top,300,minesweeper_rect.bottom-minesweeper_rect.top),0,7)

    if suduko_rect.collidepoint(mouse_pos):
        pygame.draw.rect(screen,ORANGE,pygame.Rect(minesweeper_rect.left-5,suduko_rect.top,300,minesweeper_rect.bottom-minesweeper_rect.top),0,7)
    else:
        pygame.draw.rect(screen,GREY,pygame.Rect(minesweeper_rect.left-5,suduko_rect.top,300,minesweeper_rect.bottom-minesweeper_rect.top),0,7)

    if flipping_tile_rect.collidepoint(mouse_pos):
        pygame.draw.rect(screen,ORANGE,pygame.Rect(minesweeper_rect.left-5,flipping_tile_rect.top,300,minesweeper_rect.bottom-minesweeper_rect.top),0,7)
    else:
        pygame.draw.rect(screen,GREY,pygame.Rect(minesweeper_rect.left-5,flipping_tile_rect.top,300,minesweeper_rect.bottom-minesweeper_rect.top),0,7)

    screen.blit(title,title_rect)
    screen.blit(minesweeper, minesweeper_rect)
    screen.blit(puzzle, puzzle_rect)
    screen.blit(suduko,suduko_rect)
    screen.blit(flipping_tile,flipping_tile_rect)

    
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
