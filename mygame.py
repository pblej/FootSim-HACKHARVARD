#import lines
import pygame, sys
from button import Button
import dropdown
from dropdown import DropDown
import time

#initializing
pygame.init()

#setup the display
SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

#load the background
BG = pygame.image.load("fieldbackground.jpg")

# Returns Press-Start-2P in the desired size
def get_font(size):
    return pygame.font.Font("Sportsball.ttf", size)

#player entities




class Sprite(pygame.sprite.Sprite):
    def __init__(self,color,height,width):
        super().__init__()

        self.image = pygame.Surface([width,height])
        self.image.fill("Blue")
        self.image.set_colorkey("Grey")

        pygame.draw.rect(self.image,color,pygame.Rect(0,0,width,height))
        self.rect = self.image.get_rect()



#def playerfunc(x,y):
 #   all_sprites_list = pygame.sprite.Group()
  #  global player
   # player = Sprite("Blue",20,20)
    #player.rect.x = x
#    player.rect.y = y
#
#    all_sprites_list.add(player)
#    all_sprites_list.update()
#    all_sprites_list.draw(SCREEN)



#run left layer
#def run_left(x,y):
#    update_rect = pygame.Rect(500,100,251,541)
#    x = x - 10
#    y = y - 20
#    player(x,y)
#    for event in pygame.event.get():
        
 #       player(x,y)


  #      pygame.display.update(update_rect)
 #   return x,y
    




#play layer
def play():
    while True:
        
        
        update_rect = pygame.Rect(500,100,251,541)
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill((51,135,67))
        

        FIELD_STAGE = pygame.image.load('football field.png').convert()
        SCREEN.blit(FIELD_STAGE, (500,100))

        #player postion
        PLAYERX = 0
        PLAYERY = 0

        #start position
        STARTY = 570
        STARTX = 620
        #player = pygame.image.load('bluebox.jpg')

        
        #SCREEN.blit(player,(STARTX,STARTY))

        CHOICE_TEXT = get_font(40).render("YOUR PLAY:", True, "#b68f40")
        CHOICE_RECT = CHOICE_TEXT.get_rect(center=(1000, 100))
        SCREEN.blit(CHOICE_TEXT,CHOICE_RECT)

        RUN_LEFT = Button(image=None, pos=(1000, 175), 
                text_input="RUN LEFT", font=get_font(20), base_color="White", hovering_color="grey")
        RUN_LEFT.changeColor(PLAY_MOUSE_POS)
        RUN_LEFT.update(SCREEN)

        RUN_MIDDLE = Button(image=None, pos=(1000, 225), 
                text_input="RUN MIDDLE", font=get_font(20), base_color="White", hovering_color="grey")
        RUN_MIDDLE.changeColor(PLAY_MOUSE_POS)
        RUN_MIDDLE.update(SCREEN)

        RUN_RIGHT = Button(image=None, pos=(1000, 275), 
                text_input="RUN RIGHT", font=get_font(20), base_color="White", hovering_color="grey")
        RUN_RIGHT.changeColor(PLAY_MOUSE_POS)
        RUN_RIGHT.update(SCREEN)

        PASS_LEFT = Button(image=None, pos=(1000, 325), 
                text_input="PASS LEFT", font=get_font(20), base_color="White", hovering_color="grey")
        PASS_LEFT.changeColor(PLAY_MOUSE_POS)
        PASS_LEFT.update(SCREEN)

        PASS_MIDDLE = Button(image=None, pos=(1000, 375), 
                text_input="PASS MIDDLE", font=get_font(20), base_color="White", hovering_color="grey")
        PASS_MIDDLE.changeColor(PLAY_MOUSE_POS)
        PASS_MIDDLE.update(SCREEN)

        PASS_RIGHT = Button(image=None, pos=(1000, 425), 
                text_input="PASS RIGHT", font=get_font(20), base_color="White", hovering_color="grey")
        PASS_RIGHT.changeColor(PLAY_MOUSE_POS)
        PASS_RIGHT.update(SCREEN)

        PLAY_BACK = Button(image=None, pos=(100, 700), 
                text_input="BACK", font=get_font(40), base_color="White", hovering_color="grey")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if RUN_LEFT.checkForInput(PLAY_MOUSE_POS):
                    #ynew=STARTY + 10
                    #PLAYERX,PLAYERY = player(STARTX,ynew) #run_left(STARTX,STARTY)
                    STARTX -= 50
                    STARTY -= 50
                    pygame.display.flip()
                    
                   
                    

            pygame.display.update()
    
#options layer
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(45).render("No Options Avaiable", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

#main menu layer
def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("FOOT SIM", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("Play Rect.png"), pos=(640, 250), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("Options Rect.png"), pos=(640, 400), 
                            text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("Quit Rect.png"), pos=(640, 550), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()