import pygame
from sys import exit
from random import randint

def display_score():
    current_time =int(pygame.time.get_ticks() / 1000)-start_time
    score_surface = test_font.render(f'Score: {current_time}',False,(64,64,64))
    Score_surface = pygame.transform.scale(score_surface,(90,90))
    score_Rect = Score_surface.get_rect(center = (900,50))
    screen.blit(Score_surface,score_Rect)
    return current_time

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -=5
            if obstacle_rect.bottom ==543:
                screen.blit(monster_surface,obstacle_rect)
            else:
                screen.blit(flys_surface,obstacle_rect)
        
        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x> 100]
        return obstacle_list
    else:
        return[]

def collisions(player,obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):
                return False
    return True

pygame.init()   #initialise a pygame
screen = pygame.display.set_mode((1000,730))      #creating a screen on which the game will be set on.
pygame.display.set_caption('Runner')             #naming the game
Clock = pygame.time.Clock()                      #works for maintaining the frame rate
test_font = pygame.font.Font(None,100)
game_active=False
start_time = 0

back_surface = pygame.image.load('python1/back.webp').convert()        #importing a image from my computer and dont forget the type of file like png,webp etc
ground_surface = pygame.image.load('python1/ground.png').convert_alpha()

text_font = test_font.render('Das Mario',False,'#000000')
text_rect = text_font.get_rect(center =(500,50))


mon_surface = pygame.image.load('python1/mon1.png')
monster_surface = pygame.transform.scale(mon_surface,(50,50)).convert_alpha()        #resizing a imported image 
mon_Rect = monster_surface.get_rect(bottomleft= (1050,543))

fly_surface = pygame.image.load('python1/mon2.png')
flys_surface = pygame.transform.scale(fly_surface,(50,50))
#Fly_surface = pygame.transform.rotate(fly_surface,180).convert_alpha()


obstacle_rect_list=[]


player_surface = pygame.image.load('python1/player.png')
Player_Surf = pygame.transform.scale(player_surface,(110,110)).convert_alpha()
player_Rect = Player_Surf.get_rect(midbottom=(100,550))
player_gravity = 0
score =0
player_Stand = pygame.image.load('python1/player.png').convert_alpha()
player_Stand_rect = player_Stand.get_rect(center=(500,365))
starting_point = test_font.render('Tap Space to Start',False,(64,64,64))
starting_point_rect = starting_point.get_rect(center = (500,650))
game_name = test_font.render('Pixel Runner',False,(64,64,64))
game_name_rect = game_name.get_rect(center = (500,120))

obstacle_time = pygame.USEREVENT +1
pygame.time.set_timer(obstacle_time,1400)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_Rect.bottom>=545:
                    player_gravity= -25
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active=True
                #mon_Rect.left=900
                start_time =int(pygame.time.get_ticks()/1000)
        if event.type == obstacle_time and game_active :
            if randint(0,2):
                obstacle_rect_list.append(monster_surface.get_rect(bottomleft= (randint(1100,1200),543)))
            else:
                obstacle_rect_list.append(flys_surface.get_rect(bottomleft= (randint(1100,1200),360)))
            
                
            
    if game_active:
        screen.blit(back_surface,(0,0))              # this helps in placing 1 surface on top of another surface like we placed test_surface on top of screen by using (blit)
        screen.blit(ground_surface,(0,520))
        #pygame.draw.rect(screen,'#000000',text_rect,6)
        #pygame.draw.rect(screen,'#000000',text_rect)    
        #pygame.draw.line(screen,'Gold',(0,0),(1000,730),10)
        screen.blit(text_font,text_rect)
        
        score =display_score()
        
        """ #mon_Rect.x -=4
        #if mon_Rect.right<=0:
        #    mon_Rect.left=1000
        #screen.blit(monster_surface,mon_Rect) """
        
        player_gravity +=1
        player_Rect.y += player_gravity
        if player_Rect.bottom >=545:
            player_Rect.bottom = 545
        screen.blit(Player_Surf,player_Rect)
        
        obstacle_rect_list=obstacle_movement(obstacle_rect_list)
        
        game_active = collisions(player_Rect,obstacle_rect_list)
    else:
        screen.fill((94,129,162))
        screen.blit(player_Stand,player_Stand_rect)
        score_display=test_font.render(f'Your score :{score}',False,(64,64,64))
        score_display_rect = score_display.get_rect(center=(500,650))
        screen.blit(game_name,game_name_rect)
        obstacle_rect_list.clear()
        player_Rect.midbottom = (100,545)
        player_gravity=0
        
        if score ==0:
            screen.blit(starting_point,starting_point_rect)
        else:
            screen.blit(score_display,score_display_rect)
        
    
    pygame.display.update()
    Clock.tick(60)                               #Should not run faster than 60fps 