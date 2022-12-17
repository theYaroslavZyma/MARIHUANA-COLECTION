import pygame
import random
# init pygame 
pygame.init()

#creating of screen
width = 1000
height = 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("weed colection")
##############################################################################################################
###############   
#                                  MAIN SETTINGS
#colors
white = (255, 255, 255)
black = (0,0,0)
red = (255, 0 , 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

#color of background

screen.fill(white)

# count variables
count1 = 0
count2 = 0
#font
font = pygame.font.SysFont("corbel", 33)


#text

main_text = font.render("first player moves by 'AWSD', second by 'arrows'(COLLECT MARIHUANA!!!)", True, white, black)
main_text_rect = main_text.get_rect()
main_text_rect.topleft = (0,0)

menu_text = font.render("PRESS SPACE TO START", True, white, black)
menu_text_rect = menu_text.get_rect()
menu_text_rect.center = (width//2,height//2)

win_text_1 = font.render("PLAYER 1 WIN", True, white, black)
win_text_1_rect = win_text_1.get_rect()
win_text_1_rect.center = (width//2,height//2)

win_text_2 = font.render("'PLAYER 2' WIN", True, white, black)
win_text_2_rect = win_text_2.get_rect()
win_text_2_rect.center = (width//2,height//2)


#sounds
#bg song
pygame.mixer.music.load("SOUNDS/background_song.mp3")
pygame.mixer.music.play(-1, 0.0)

win_sound = pygame.mixer.Sound("SOUNDS/win.mp3")

#img loading
first_player_img = pygame.image.load("IMGES/runner.png")
first_player_ract = first_player_img.get_rect()
first_player_ract.center = (random.randint(128, 1000-128), random.randint(128, 500-128))


second_player_img = pygame.image.load("IMGES/runner.png")
second_player_ract = first_player_img.get_rect()
second_player_ract.center = (random.randint(128, 1000-128), random.randint(128, 500-128))


marihuana_img = pygame.image.load("IMGES/marihuana.png")
marihuana_ract = marihuana_img.get_rect()
marihuana_ract.center = (random.randint(128, 1000-128), random.randint(128, 500-128))

#main distance

distance = 10

# menu variable
menu = "menu"
#fps


fps = 30
clock = pygame.time.Clock()


#                                          MENU LOOP
if menu == "menu":
    width = 1000
    height = 500
    screen_menu = pygame.display.set_mode((width, height))
    pygame.display.set_caption("weed colection")
    screen_menu.fill(white)
    
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
            keys = pygame.key.get_pressed()

            
            if (keys[pygame.K_SPACE]):
                menu = "game"
                
                run = False

            
        pygame.display.update()
        screen_menu.blit(menu_text, menu_text_rect)
run = True

#                                                GAME LOOP
if menu == "game":
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


        
        #geting all keys
        keys = pygame.key.get_pressed()

        #navigation
        #first player
        if (keys[pygame.K_w]) and first_player_ract.top >= 36:
            first_player_ract.y -= distance
        
        elif (keys[pygame.K_s]) and first_player_ract.bottom <= height:
            first_player_ract.y += distance

        elif (keys[pygame.K_d]) and first_player_ract.right <= width:
            first_player_ract.x += distance

        elif (keys[pygame.K_a]) and first_player_ract.left >= 0:
            first_player_ract.x -= distance

        # second player
        if (keys[pygame.K_UP]) and second_player_ract.top >= 36:
            second_player_ract.y -= distance
        
        elif (keys[pygame.K_DOWN]) and second_player_ract.bottom <= height:
            second_player_ract.y += distance

        elif (keys[pygame.K_RIGHT]) and second_player_ract.right <= width:
            second_player_ract.x += distance

        elif (keys[pygame.K_LEFT]) and second_player_ract.left >= 0:
            second_player_ract.x -= distance

        #colidirect
        #first player
        if first_player_ract.colliderect(marihuana_ract):
            marihuana_ract.centery = random.randint(36+64,500-64)
            marihuana_ract.centerx = random.randint(64,1000-64)
            count1 += 1
            print(f"first player score:{count1}")
        #second player
        if second_player_ract.colliderect(marihuana_ract):
            marihuana_ract.centery = random.randint(36+64,500-64)
            marihuana_ract.centerx = random.randint(64,1000-64)
            count2 += 1
            print(f"second player score:{count2 }")

        #win condition
        if count1 == 15:
            menu = "win_1"
            run = False
            win_sound.play()
        elif count2 == 15:
            menu = "win_2"
            run = False
            win_sound.play()
        screen.fill(white)




        #blitting
        screen.blit(first_player_img, first_player_ract)
        screen.blit(second_player_img, second_player_ract)
        screen.blit(main_text, main_text_rect)
        screen.blit(marihuana_img, marihuana_ract)

        #updtae of screen
        pygame.display.update()

        #fps maining

        clock.tick(fps)


#                                             PLAYER 1 WIN LOOP
if menu == "win_1":
    width = 1000
    height = 500
    screen_win_1 = pygame.display.set_mode((width, height))
    pygame.display.set_caption("weed colection")
    screen_win_1.fill(white)
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
 
        pygame.display.update()
        screen_menu.blit(win_text_1, win_text_1_rect)


#          print                                  PLAYER 2 WIN LOOP
if menu == "win_2":
    width = 1000
    height = 500
    screen_win_2 = pygame.display.set_mode((width, height))
    pygame.display.set_caption("run thomas")

    
    screen_win_2.fill(white)
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
            

            
            

            
        pygame.display.update()
        screen_menu.blit(win_text_2, win_text_2_rect)




#end of program
pygame.quit()

