import pygame
import random
from sys import exit
pygame.init()

bg_color = (192, 192, 192)
grid_color = (128, 128, 128)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (40, 40, 40)
RED = (255, 0, 0)
CRIMSON = (220, 20, 60)
ORANGE = (255, 127, 0)
GREEN = (45, 194, 31)


grid_size = 32  # Size of grid (WARNING: macke sure to change the images dimension as well)
border = 16  # Top border
top_border = 100  # Left, Right, Bottom border
timer = pygame.time.Clock()  # Create timer
pygame.display.set_caption("Minesweeper")  # S Set the caption of window

# Import files
emptyGrid = pygame.image.load("minesweeper_icon/empty.png")
flag = pygame.image.load("minesweeper_icon/flag.png")
gridn0 = pygame.image.load("minesweeper_icon/Grid.png")
gridn01 = pygame.image.load("minesweeper_icon/grid1.png")
gridn02 = pygame.image.load("minesweeper_icon/grid2.png")
gridn03 = pygame.image.load("minesweeper_icon/grid3.png")
gridn04 = pygame.image.load("minesweeper_icon/grid4.png")
gridn05 = pygame.image.load("minesweeper_icon/grid5.png")
gridn06 = pygame.image.load("minesweeper_icon/grid6.png")
gridn07 = pygame.image.load("minesweeper_icon/grid7.png")
gridn08 = pygame.image.load("minesweeper_icon/grid8.png")
gridn07 = pygame.image.load("minesweeper_icon/grid7.png")
mine_img = pygame.image.load("minesweeper_icon/mine.png")
mine_imgClicked = pygame.image.load("minesweeper_icon/mineClicked.png")
mine_imgFalse = pygame.image.load("minesweeper_icon/mineFalse.png")

font_title = pygame.font.Font('Hello Avocado.ttf', 40)
font_content = pygame.font.Font('Hello Avocado.ttf', 25)


gameState = "Start"
# Create global values
grid = []  # The main grid
mines = []  # Pos of the mines
def selectScreen():
    global gameState
    global game_width 
    global game_height 
    global numMine 
    global display_width
    global display_height
    global gameDisplay
    game_width = 10  # Change this to increase size
    game_height = 10 
    numMine= 10
    display_width = grid_size * game_width + border * 2  # Display width
    display_height = grid_size * game_height + border + top_border  # Display height
    gameDisplay = pygame.display.set_mode((display_width, display_height))  # Create display
    while gameState != "Exit":
        # Reset screen
        # mineLeft = numMine  # Number of mine left
        gameDisplay.fill(bg_color)

        # User inputs
        for event in pygame.event.get():
            # Check if player close window
            if event.type == pygame.QUIT or gameState == "Exit":
                gameState = "Exit"
                exec(open("module.py").read())
                exit()
            # Check if play restart
            if gameState == "Game Over" or gameState == "Win":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        gameState = "Exit"
                        game_width = 10  # Change this to increase size
                        game_height = 10 
                        numMine= 10
                        display_width = grid_size * game_width + border * 2  # Display width
                        display_height = grid_size * game_height + border + top_border  # Display height
                        gameDisplay = pygame.display.set_mode((display_width, display_height))  # Create display
                        gameLoop(numMine, game_width, game_height)
            elif gameState == "Start":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_b:
                        gameState = "Playing"
                        game_width = 10  # Change this to increase size
                        game_height = 10 
                        numMine= 10
                        display_width = grid_size * game_width + border * 2  # Display width
                        display_height = grid_size * game_height + border + top_border  # Display height
                        gameDisplay = pygame.display.set_mode((display_width, display_height))  # Create display
                        gameLoop(numMine, game_width, game_height)
                    if event.key == pygame.K_i:
                        gameState = "Playing"
                        game_width = 16  # Change this to increase size
                        game_height = 16 
                        numMine= 40
                        display_width = grid_size * game_width + border * 2  # Display width
                        display_height = grid_size * game_height + border + top_border  # Display height
                        gameDisplay = pygame.display.set_mode((display_width, display_height))  # Create display
                        gameLoop(numMine, game_width, game_height)
                    if event.key == pygame.K_e:
                        gameState = "Playing"
                        game_width = 30  # Change this to increase size
                        game_height = 16 
                        numMine= 99
                        display_width = grid_size * game_width + border * 2  # Display width
                        display_height = grid_size * game_height + border + top_border  # Display height
                        gameDisplay = pygame.display.set_mode((display_width, display_height))  # Create display
                        gameLoop(numMine, game_width, game_height)

        # Check if won
        if gameState == "Start":
            title_text = font_title.render('Puzzle Game', True, BLACK)
            title_rect = title_text.get_rect()
            title_rect.center = (display_width // 2, display_height // 2 - 80)

            choose_text = font_content.render('Choose your difficulty', True, BLACK)
            choose_rect = choose_text.get_rect()
            choose_rect.center = (display_width // 2, display_height // 2 - 20)

            easy_text = font_content.render("Press 'B' - Basic (10x10)", True, BLACK)
            easy_rect = easy_text.get_rect()
            easy_rect.center = (display_width // 2, display_height // 2 + 40)

            medium_text = font_content.render("Press 'I' - Intermediate (16x16)", True, BLACK)
            medium_rect = medium_text.get_rect()
            medium_rect.center = (display_width // 2, display_height // 2 + 90)

            hard_text = font_content.render("Press 'E' - Expert (30x16)", True, BLACK)
            hard_rect = hard_text.get_rect()
            hard_rect.center = (display_width // 2, display_height // 2 + 140)
            gameDisplay.blit(title_text, title_rect)
            gameDisplay.blit(choose_text, choose_rect)
            gameDisplay.blit(easy_text, easy_rect)
            gameDisplay.blit(medium_text, medium_rect)
            gameDisplay.blit(hard_text, hard_rect)
        
        pygame.display.update()  # Update screen
        timer.tick(40)  # Tick fps
    # mineLeft = numMine  # Number of mine left

# Create funtion to draw texts
def drawText(txt, s, yOff=0):
    screen_text = pygame.font.SysFont("Calibri", s, True).render(txt, True, (0, 0, 0))
    rect = screen_text.get_rect()
    rect.center = (game_width * grid_size / 2 + border, game_height * grid_size / 2 + top_border + yOff)
    gameDisplay.blit(screen_text, rect)


# Create class grid
class Grid:
    def __init__(self, xGrid, yGrid, type):
        self.xGrid = xGrid  # X pos of grid
        self.yGrid = yGrid  # Y pos of grid
        self.clicked = False  # Boolean var to check if the grid has been clicked
        self.mineClicked = False  # Bool var to check if the grid is clicked and its a mine
        self.mineFalse = False  # Bool var to check if the player flagged the wrong grid
        self.flag = False  # Bool var to check if player flagged the grid
        # Create rectObject to handle drawing and collisions
        self.rect = pygame.Rect(border + self.xGrid * grid_size, top_border + self.yGrid * grid_size, grid_size, grid_size)
        self.val = type  # Value of the grid, -1 is mine

    def drawGrid(self):
        # Draw the grid according to bool variables and value of grid
        if self.mineFalse:
            gameDisplay.blit(mine_imgFalse, self.rect)
        else:
            if self.clicked:
                if self.val == -1:
                    if self.mineClicked:
                        gameDisplay.blit(mine_imgClicked, self.rect)
                    else:
                        gameDisplay.blit(mine_img, self.rect)
                else:
                    if self.val == 0:
                        gameDisplay.blit(emptyGrid, self.rect)
                    elif self.val == 1:
                        gameDisplay.blit(gridn01, self.rect)
                    elif self.val == 2:
                        gameDisplay.blit(gridn02, self.rect)
                    elif self.val == 3:
                        gameDisplay.blit(gridn03, self.rect)
                    elif self.val == 4:
                        gameDisplay.blit(gridn04, self.rect)
                    elif self.val == 5:
                        gameDisplay.blit(gridn05, self.rect)
                    elif self.val == 6:
                        gameDisplay.blit(gridn06, self.rect)
                    elif self.val == 7:
                        gameDisplay.blit(gridn07, self.rect)
                    elif self.val == 8:
                        gameDisplay.blit(gridn08, self.rect)

            else:
                if self.flag:
                    gameDisplay.blit(flag, self.rect)
                else:
                    gameDisplay.blit(gridn0, self.rect)

    def revealGrid(self):
        self.clicked = True
        # Auto reveal if it's a 0
        if self.val == 0:
            for x in range(-1, 2):
                if self.xGrid + x >= 0 and self.xGrid + x < game_width:
                    for y in range(-1, 2):
                        if self.yGrid + y >= 0 and self.yGrid + y < game_height:
                            if not grid[self.yGrid + y][self.xGrid + x].clicked:
                                grid[self.yGrid + y][self.xGrid + x].revealGrid()
        elif self.val == -1:
            # Auto reveal all mines if it's a mine
            for m in mines:
                if not grid[m[1]][m[0]].clicked:
                    grid[m[1]][m[0]].revealGrid()

    def updateValue(self):
        # Update the value when all grid is generated
        if self.val != -1:
            for x in range(-1, 2):
                if self.xGrid + x >= 0 and self.xGrid + x < game_width:
                    for y in range(-1, 2):
                        if self.yGrid + y >= 0 and self.yGrid + y < game_height:
                            if grid[self.yGrid + y][self.xGrid + x].val == -1:
                                self.val += 1


def gameLoop(numMine, game_width, game_height):
    global gameState
    mineLeft = numMine  # Number of mine left
    global grid  # Access global var
    grid = []
    global mines
    t = 0  # Set time to 0

    # Generating mines
    mines = [[random.randrange(0, game_width),
              random.randrange(0, game_height)]]

    for c in range(numMine - 1):
        pos = [random.randrange(0, game_width),
               random.randrange(0, game_height)]
        same = True
        while same:
            for i in range(len(mines)):
                if pos == mines[i]:
                    pos = [random.randrange(0, game_width), random.randrange(0, game_height)]
                    break
                if i == len(mines) - 1:
                    same = False
        mines.append(pos)

    # Generating entire grid
    for j in range(game_height):
        line = []
        for i in range(game_width):
            if [i, j] in mines:
                line.append(Grid(i, j, -1))
            else:
                line.append(Grid(i, j, 0))
        grid.append(line)

    # Update of the grid
    for i in grid:
        for j in i:
            j.updateValue()

    # Main Loop
    while gameState != "Exit":
        # Reset screen
        gameDisplay.fill(bg_color)

        # User inputs
        for event in pygame.event.get():
            # Check if player close window
            if event.type == pygame.QUIT:
                gameState = "Exit"
                exec(open("module.py").read())
                exit()
            # Check if play restart
            if gameState == "Game Over" or gameState == "Win":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        gameState = "Start"
                        selectScreen()
            else:
                if event.type == pygame.MOUSEBUTTONUP:
                    for i in grid:
                        for j in i:
                            if j.rect.collidepoint(event.pos):
                                if event.button == 1:
                                    # If player left clicked of the grid
                                    j.revealGrid()
                                    # Toggle flag off
                                    if j.flag:
                                        mineLeft += 1
                                        j.falg = False
                                    # If it's a mine
                                    if j.val == -1:
                                        gameState = "Game Over"
                                        j.mineClicked = True
                                elif event.button == 3:
                                    # If the player right clicked
                                    if not j.clicked:
                                        if j.flag:
                                            j.flag = False
                                            mineLeft += 1
                                        else:
                                            j.flag = True
                                            mineLeft -= 1

        # Check if won
        w = True
        for i in grid:
            for j in i:
                j.drawGrid()
                if j.val != -1 and not j.clicked:
                    w = False
        if w and gameState != "Exit":
            gameState = "Win"

        # Draw Texts
        if gameState != "Game Over" and gameState != "Win":
            t += 1
        elif gameState == "Game Over":
            drawText("Game Over!", 50)
            drawText("R to restart", 35, 50)
            for i in grid:
                for j in i:
                    if j.flag and j.val != -1:
                        j.mineFalse = True
        else:
            drawText("You WON!", 50)
            drawText("R to restart", 35, 50)
        # Draw time
        s = str(t // 30)
        screen_text = pygame.font.SysFont("Calibri", 50).render(s, True, (0, 0, 0))
        gameDisplay.blit(screen_text, (border, border))
        # Draw mine left
        screen_text = pygame.font.SysFont("Calibri", 50).render(mineLeft.__str__(), True, (0, 0, 0))
        gameDisplay.blit(screen_text, (display_width - border - 50, border))

        pygame.display.update()  # Update screen

        timer.tick(30)  # Tick fps


selectScreen()
pygame.quit()

