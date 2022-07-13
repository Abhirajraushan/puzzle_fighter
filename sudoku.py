import pygame
import requests
pygame.init()

game_width=550
game_height=550
bg_color=(251,247,245)
element_color = (52,31,151)
buffer = 5

clock= pygame.time.Clock() #clock variable to manipulate speed of execution
screen=pygame.display.set_mode((game_width,game_height)) #setting display 
pygame.display.set_caption("Sudoku") #Setting caption aka title to window
screen.fill(bg_color) #setting backgroung color

difficulty_level=["https://sugoku.herokuapp.com/board?difficulty=easy"] #variable to store link to webpage
response = requests.get(difficulty_level[0]) #Getting results from webpage
grid = response.json()['board'] #making grid aka 2d array from the result
grid_original = [[grid[x][y] for y in range(len(grid[0]))] for x in range(len(grid))] #copy of grid
myfont = pygame.font.SysFont('Comic Sans MS',35) #setting font
for i in range(0,10):
    line_widht=2
    if i%3==0:
        line_widht=4
    pygame.draw.line(screen,(0,0,0),(50+50*i,50),(50+50*i,500),line_widht) #creating vertical lines
    pygame.draw.line(screen,(0,0,0),(50,50+50*i),(500,50+50*i),line_widht) #creating horzontal lines
pygame.display.update() #update the display to show lines

for i in range(0,len(grid[0])):
    for j in range(0,len(grid[0])):
        if 0 < grid[i][j] < 10:
            value = myfont.render(str(grid[i][j]),True,element_color) #getting the value from grid
            screen.blit(value,((j+1)*50 + 15,(i+1)*50)) #displaying the values

pygame.display.update() #Updating the screen 


run=True
mouse_pos =[0,0] 
while run:
    key_pressed = 10
    for event in pygame.event.get(): #getting event in event
        if event.type == pygame.QUIT: #event to quit
            run=False
            exec(open("./module.py").read()) #opening of module
        if event.type == pygame.MOUSEBUTTONUP: #event of mousebuttonup
            mouse_pos =pygame.mouse.get_pos() #pos of mousebuttonup
        if event.type == pygame.KEYUP:
            key_pressed = event.key- 48 #key pressed
    i, j = (mouse_pos[1]//50 )-1,(mouse_pos[0]//50) -1 #getting the index of box clicked
    if 0<= i < 9 and 0<= j < 9: #to check whether the click was inside the grid or not
        if(grid_original[i][j] !=0): #to check wether click was on original no
            mouse_pos=[0,0]
            continue
        if(key_pressed == 0): #if 0 is clicked the draw a rect to hide the no
            grid[i][j] = key_pressed
            pygame.draw.rect(screen,bg_color,((j+1)*50 + buffer, (i+1)*50+ buffer,50 -2*buffer , 50 - 2*buffer)) #draw the rect
            mouse_pos=[0,0]
            pygame.display.update()
        if(0 < key_pressed < 10): #
            pygame.draw.rect(screen,bg_color,((j+1)*50 + buffer, (i+1)*50+ buffer,50 -2*buffer , 50 - 2*buffer))
            value = myfont.render(str(key_pressed),True,(0,0,0))
            screen.blit(value,((j+1)*50 +15,(i+1)*50))
            grid[i][j]= key_pressed
            mouse_pos=[0,0]
            pygame.display.update()
            
    clock.tick(30)
pygame.quit()
