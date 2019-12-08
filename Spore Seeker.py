import pygame
from pygame.locals import *
from os import path
import random

working_dir = path.dirname(__file__)

### CLASSES ###

#Used for the player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((96,96))
        self.rect = self.surf.get_rect()
        self.image = pygame.transform.scale(pygame.image.load(path.join(working_dir,"Sprites/Icon-Player.png")),(96,96))

    def update(self, pressed_keys):
        #Movement keys (arrows/wasd)
        if pressed_keys[K_UP] or pressed_keys[K_w]:
            screen.blit(player.surf,player.rect)
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN] or pressed_keys[K_s]:
            screen.blit(player.surf,player.rect)
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT] or pressed_keys[K_a]:
            screen.blit(player.surf,player.rect)
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT] or pressed_keys[K_d]:
            screen.blit(player.surf,player.rect)
            self.rect.move_ip(5, 0)

        #Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > width:
            self.rect.right = width
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= height:
            self.rect.bottom = height



#Enemies
class Enemy:
    def __init__(self,hp,damage,move,dist,img):
        self.hp = hp
        self.damage = damage
        self.move = move
        self.dist = dist
        self.img = img

    def load(self):
        pygame.transform.scale(pygame.image.load(path.join(working_dir,self.img)),(64,64))

    def health(self,health):
        alive = True

        if health <= 0:
            alive = False



class Question:
    def __init__(self,quest,ans):
        self.quest = quest
        self.ans = ans

    def load():
        pass



class Level:
    def __init__(self,lvl,type):
        self.lvl = lvl
        self.type = type

    def level_gen(self,points):
        rand_num = random.randint(0,7)
        if self.type == "enemy":
            print("enemy")
            #self.load()
            enemy_img = enemies[rand_num].img
            img(64,64,400,400,enemy_img)
        else:
            print("question")
            question = questions[rand_num].quest
            answer = questions[rand_num].ans

            img(280,110,220,500,"Button-True.png")
            img(280,110,700,500,"Button-False.png")

        return rand_num



class Weapons:
    pass



### Called Modules ###
#When escape or the exit button is pressed, quit the game
def quit_game():
    clock = pygame.time.Clock()

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
                pygame.display.quit()
        elif event.type == QUIT:
            running = False
            pygame.display.quit()

    clock.tick(250)



#Changing the background
def background():
    background_img = pygame.image.load(path.join(working_dir,"Sprites/Background.png"))
    screen.blit(background_img,(0,0))



#Loads and displays an image
def img(w,h,x,y,file):
    image = pygame.transform.scale(pygame.image.load(path.join(working_dir,"Sprites/"+file)),(w,h))
    screen.blit(image,(x,y))
    pygame.display.flip()





### OBJECTS ###
## LEVELS ##
levels = []

#Enemies
levels.append(Level(0,"enemy"))
levels.append(Level(1,"enemy"))
levels.append(Level(2,"enemy"))
levels.append(Level(3,"enemy"))

#Questions
levels.append(Level(0,"question"))
levels.append(Level(1,"question"))
levels.append(Level(2,"question"))
levels.append(Level(3,"question"))



## ENEMIES ##
enemies = []

#Horizontal enemies
enemies.append(Enemy(50,5,"h",2,"Enemy-H1.png"))
enemies.append(Enemy(75,5,"h",2,"Enemy-H2.png"))
enemies.append(Enemy(100,20,"h",7,"Enemy-H3.png"))
enemies.append(Enemy(125,30,"h",9,"Enemy-H4.png"))

#Vertical Enemies
enemies.append(Enemy(50,10,"v",2,"Enemy-V1.png"))
enemies.append(Enemy(75,10,"v",3,"Enemy-V2.png"))
enemies.append(Enemy(100,25,"v",8,"Enemy-V3.png"))
enemies.append(Enemy(125,35,"v",10,"Enemy-V4.png"))



## QUESTIONS ##
questions = []

#True answers
questions.append(Question("",True))
questions.append(Question("",True))
questions.append(Question("",True))
questions.append(Question("",True))

#False answers
questions.append(Question("",False))
questions.append(Question("",False))
questions.append(Question("",False))
questions.append(Question("",False))





### Screens ###
#The start screen with buttons leading to different "pages"
def start_screen():
    running = True
    background()

    #Loading buttons - y+150 space between each button
    img(280,110,880,40,"Button-Start.png")     #Start button
    img(280,110,880,190,"Button-Custom.png")    #Customisation menu
    img(280,110,880,340,"Button-Scores.png")    #Highscores table


    while running:
        quit_game()

        #Checking if a button is pressed, and then running what the button should do
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        #Start game
        if 880+280>mouse[0]>880 and 40+110>mouse[1]>40 and click[0]==1:
            game()
        #Customisation menu
        wearing = "Hat-Blank.png"   #Removing hats
        if 880+280>mouse[0]>880 and 190+110>mouse[1]>190 and click[0]==1:
            custom_screen(wearing)
        #Highscores table
        if 880+280>mouse[0]>880 and 340+110>mouse[1]>340 and click[0]==1:
            highscores_screen()



#The customisation screen with buttons which can be clicked to change the hat the user is wearing
def custom_screen(wearing):
    running = True

    #Loading images and background
    background()

    #Variables to input: width, height, x position, y position, file name (in Sprites folder)
    img(280,110,460,600,"Button-Back.png")
    img(128,128,200,145,"GUI-Custom.png")
    img(128,128,200,400,"GUI-Custom.png")
    img(128,128,872,145,"GUI-Custom.png")
    img(128,128,872,400,"GUI-Custom.png")
    img(64,64,232,177,"Hat-Tophat.png")
    img(64,64,232,432,"Hat-Fez.png")
    img(64,64,904,177,"Hat-Cowboy.png")
    img(64,64,904,432,"Hat-Party.png")
    pygame.display.flip()


    # Running #
    while running:
        quit_game()

        #Checking if a button is pressed, and then running what the button should do
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        #Back button
        if 460+280>mouse[0]>460 and 600+110>mouse[1]>600 and click[0]==1:
            start_screen()

        #Hat 1
        if 200+128>mouse[0]>200 and 145+128>mouse[1]>145 and click[0]==1:
            wearing = "Hat-Tophat.png"
        #Hat 2
        if 200+128>mouse[0]>200 and 400+128>mouse[1]>400 and click[0]==1:
            wearing = "Hat-Fez.png"
        #Hat 3
        if 872+128>mouse[0]>872 and 145+128>mouse[1]>145 and click[0]==1:
            wearing = "Hat-Cowboy.png"
        #Hat 4
        if 872+128>mouse[0]>872 and 400+128>mouse[1]>400 and click[0]==1:
            wearing = "Hat-Party.png"



#The highscores screen with a highscores table and a button to return to the start screen
def highscores_screen():
    running = True
    background()

    #Loading back button
    img(280,110,460,600,"Button-Back.png")


    while running:
        quit_game()

        #Checking if a button is pressed, and then running what the button should do
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        #Back button
        if 460+280>mouse[0]>460 and 600+110>mouse[1]>600 and click[0]==1:
            start_screen()



#The main game
def game():
    screen.fill((239,228,176))

    running = True
    points = 100                #Player starts with 100 points

    rand_num = random.randint(0,7)
    question_num = levels[rand_num].level_gen(points)


    while running:
        quit_game()

        #Checking if a button is pressed, and then running what the button should do
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()


        #Checking if the current level has an enemy or a question
        #If enemy, run the fight
        if levels[rand_num].type == "enemy":
            pressed_keys = pygame.key.get_pressed()

            player.update(pressed_keys)

            screen.blit(player.image, player.rect)
            pygame.display.flip()

        #If question, check if player gets the right answer
        else:
            #Setting variables to be used
            player_ans = bool
            answer = questions[question_num].ans

            #True button
            if 220+280>mouse[0]>220 and 500+110>mouse[1]>500 and click[0]==1:
                player_ans = True
                break

            #False button
            if 700+280>mouse[0]>700 and 500+110>mouse[1]>500 and click[0]==1:
                player_ans = False
                break

    #Checking of the player's answer is correct and changing the score accordingly
    if levels[rand_num].type == "question":
        if player_ans == answer:
            points += 25
            print("correct")
        else:
            points -= 10
            print("wrong")



### Called Game Modules ###
def weapons():
    pass





### Main Program ###
#Installing from library
pygame.init()

#Loading and adding the icon of the tab
game_icon = pygame.image.load(path.join(working_dir,"Sprites/Game-Icon.png"))
pygame.display.set_icon(game_icon)

#Setting width and height as variables so that they can be easily modified
width = 1200
height = 800

#Defining the size of the screen and the tab name
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Dungeon Game")

#Setting variables to reference the classes
player = Player()
weapons = Weapons()



## Running the game
start_screen()
#game()
#custom_screen(wearing)
#highscores_screen()
