import pygame
import time

pygame.init()

game_title = "Dodgy Fly"

display_width = 800
display_height = 600

car_width = 50

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

carImg = pygame.image.load('art/exploderfly.png')

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption(game_title)
clock = pygame.time.Clock()

car_start_x = (display_width * 0.45)
car_speed = 5

x = car_start_x
y = (display_height * 0.8)

####################### Draw commands
def draw():
    draw_background()
    #draw_objects()
    draw_player(x,y)
    #draw_npcs()
    #draw_projectiles()
    #draw_ui()

def draw_player(x, y):
    gameDisplay.blit(carImg, (x,y))

def draw_background():
    gameDisplay.fill(white)

def draw_objects():
    print('No objects yet')
    
def draw_npcs():
    print('No NPCs yet')
    
def draw_projectiles():
    print('No Projectiles yet')
    
def draw_ui():
    print('No UI yet')

def crash():
    message_display('You crashed, boi')
    x = car_start_x

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.SysFont('Verdana', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()

def game_loop():
    x_change = 0
    gameExit = False
    global x

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change += -car_speed
                if event.key == pygame.K_RIGHT:
                    x_change += car_speed

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    x_change += car_speed
                if event.key == pygame.K_RIGHT:
                    x_change += -car_speed

        x += x_change
        draw()

        if x > display_width - car_width or x < 0:
            crash()

        pygame.display.update()
        clock.tick(60)

game_loop()

pygame.quit()
quit()
