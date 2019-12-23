import pygame
from pygame.locals import *
from os import path
import random

working_dir = path.dirname(__file__)

### CLASSES ###
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((78,96))
        self.rect = self.surf.get_rect()
        self.image = pygame.transform.scale(pygame.image.load(path.join(working_dir,"Sprites/Player-Blue.png")),(78,96))

    def update(self, pressed_keys):
        #Movement keys (arrows/wasd)
        if pressed_keys[K_UP] or pressed_keys[K_w]:
            screen.blit(player.surf,player.rect)
            self.surf.fill((239,228,176))
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN] or pressed_keys[K_s]:
            screen.blit(player.surf,player.rect)
            self.surf.fill((239,228,176))
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT] or pressed_keys[K_a]:
            screen.blit(player.surf,player.rect)
            self.surf.fill((239,228,176))
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT] or pressed_keys[K_d]:
            screen.blit(player.surf,player.rect)
            self.surf.fill((239,228,176))
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

    def changeImage(self,image):
        self.image = pygame.transform.scale(pygame.image.load(path.join(working_dir,"Sprites/"+image)),(78,96))



class Enemy:
    def __init__(self,hp,damage,move,dist,img):
        self.hp = hp
        self.damage = damage
        self.move = move
        self.dist = dist
        self.img = img

    def load(self):
        pygame.transform.scale(pygame.image.load(path.join(working_dir,self.img)),(62,58))

    def health(self,health):
        alive = True

        if health <= 0:
            alive = False

    def move(self):
        pass



class Question:
    def __init__(self,quest,ans):
        self.quest = quest
        self.ans = ans

    def load(self):
        text_loader(100,300,"Question Time!",self.quest)



class Level:
    def __init__(self,lvl,type):
        self.lvl = lvl
        self.type = type

    def levelGen(self,points):
        rand_num = random.randint(0,7)
        if self.type == "enemy":
            print("enemy")
            enemy_img = enemies[rand_num].img
            img(64,64,400,400,enemy_img)
        else:
            print("question")
            question = questions[rand_num].quest
            ##print(question)
            questions[rand_num].load()
            answer = questions[rand_num].ans

            img(280,110,220,500,"Button-True.png")
            img(280,110,700,500,"Button-False.png")

        return rand_num



class Weapons:
    pass





### Other Modules ###
#When escape or the exit button is pressed, quit the game
def quit_game():
    clock = pygame.time.Clock()

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                quit()
        elif event.type == QUIT:
            pygame.quit()
            quit()

    clock.tick(250)



#Loads and displays an image
def img(w,h,x,y,file):
    image = pygame.transform.scale(pygame.image.load(path.join(working_dir,"Sprites/"+file)),(w,h))
    screen.blit(image,(x,y))
    pygame.display.flip()



#Changing the background
def background():
    img(1200,800,0,0,"Background.png")



#loads a header and the text
def text_loader(h_pos,m_pos,h_text,m_text):
    #loading a font to be used. Parameters:(font name, font size)
    font_big = pygame.font.Font('freesansbold.ttf', 64)
    font_small = pygame.font.Font('freesansbold.ttf', 32)

    #defining the colour of the text, and the displayed text
    text_colour = (91,0,14)

    #Creating a rect surface for text and drawing the text on to the surface
    ##Header
    header_text = font_big.render(h_text, True, text_colour)
    headerTextRect = header_text.get_rect()
    ##Main Text
    main_text = font_small.render(m_text, True, text_colour)
    mainTextRect = main_text.get_rect()

    #setting the central location fo the rect
    headerTextRect.center = (600, h_pos)
    mainTextRect.center = (600, m_pos)

    #displaying the text
    screen.blit(header_text, headerTextRect)
    screen.blit(main_text, mainTextRect)
    pygame.display.flip()



#displays the number of points
def disp_points(points):
    img(32,32,1050,20,"GUI-Point.png")
    points = str(points)

    #loading a font to be used. Parameters:(font name, font size)
    font = pygame.font.Font('freesansbold.ttf', 32)

    #defining the colour of the text, and the displayed text
    text_colour = (91,0,14)

    #Creating a rect surface for text and drawing the text on to the surface
    text = font.render(points, True, text_colour)
    textRect = text.get_rect()

    #setting the central location fo the rect
    textRect.center = (1125, 36)

    #displaying the text
    screen.blit(text, textRect)
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
questions.append(Question("In Pokemon, there is a virus called Pokerus that Pokemon can contract.",True))
questions.append(Question("In Super Mario 64, there are 120 stars to collect.",True))
questions.append(Question("In Overwatch, Tracer has exactly 40 bullets in her pistols.",True))
questions.append(Question("In Stardew Valley, there are 30 bundles in the Community Centre",True))

#False answers
questions.append(Question("The original Legend of Zelda game was released in 1989.",False))
questions.append(Question("In Minecraft, there are 15 colours of wool",False))
questions.append(Question("In Apex Legends, Caustic can set up poison traps and electric fences.",False))
questions.append(Question("League of Legends was published by Riot Entertainment",False))





### Screens ###
#The start screen with buttons leading to different "pages"
def start_screen():
    background()

    #Loading icon
    img(512,512,180,140,"Game-Icon-Text.png")

    #Loading buttons - 20y space between each button
    img(280,110,900,20,"Button-Start.png")      #Start button
    img(280,110,900,150,"Button-Custom.png")    #Customisation menu
    img(280,110,900,280,"Button-Scores.png")    #Leaderboard
    img(280,110,900,410,"Button-Control.png")   #Controls
    img(280,110,900,540,"Button-About.png")     #About the game
    img(280,110,900,670,"Button-Exit.png")      #Exit the game


    while True:
        quit_game()

        #Checking if a button is pressed, and then running what the button should do
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        #Start game
        if 900+280>mouse[0]>900 and 20+110>mouse[1]>20 and click[0]==1:
            game()
        #Customisation menu
        if 900+280>mouse[0]>900 and 150+110>mouse[1]>150 and click[0]==1:
            custom_screen()
        #Leaderboard
        if 900+280>mouse[0]>900 and 280+110>mouse[1]>280 and click[0]==1:
            leaderboard_screen()
        #Controls
        if 900+280>mouse[0]>900 and 410+110>mouse[1]>410 and click[0]==1:
            controls_screen()
        #About the game
        if 900+280>mouse[0]>900 and 540+110>mouse[1]>540 and click[0]==1:
            about_screen()
        #Exit the game
        if 900+280>mouse[0]>900 and 670+110>mouse[1]>670 and click[0]==1:
            running = False
            pygame.display.quit()



#The customisation screen with buttons which can be clicked to change the colour of the player's mushroom
def custom_screen():
    background()

    #Loading buttons
    #Variables to input: width, height, x position, y position, file name (in Sprites folder)
    img(280,110,460,600,"Button-Back.png")
    img(128,128,200,145,"GUI-Custom.png")
    img(128,128,200,400,"GUI-Custom.png")
    img(128,128,872,145,"GUI-Custom.png")
    img(128,128,872,400,"GUI-Custom.png")
    img(78,96,225,161,"Player-Red.png")
    img(78,96,225,416,"Player-Pink.png")
    img(78,96,897,161,"Player-Green.png")
    img(78,96,897,416,"Player-Orange.png")
    pygame.display.flip()

    sprite = "Player-Red.png"


    # Running #
    while True:
        quit_game()

        #Checking if a button is pressed, and then running what the button should do
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        #Back button
        if 460+280>mouse[0]>460 and 600+110>mouse[1]>600 and click[0]==1:
            player.changeImage(sprite)
            start_screen()

        #Hat 1
        if 200+128>mouse[0]>200 and 145+128>mouse[1]>145 and click[0]==1:
            sprite = "Player-Red.png"
        #Hat 2
        if 200+128>mouse[0]>200 and 400+128>mouse[1]>400 and click[0]==1:
            sprite = "Player-Pink.png"
        #Hat 3
        if 872+128>mouse[0]>872 and 145+128>mouse[1]>145 and click[0]==1:
            sprite = "Player-Green.png"
        #Hat 4
        if 872+128>mouse[0]>872 and 400+128>mouse[1]>400 and click[0]==1:
            sprite = "Player-Orange.png"



#The leaderboard screen with a highscores table and a button to return to the start screen
def leaderboard_screen():
    background()
    text_loader(100,250,"Leaderboard","scores")

    #Loading back button
    img(280,110,460,600,"Button-Back.png")

    while True:
        quit_game()

        #Checking if a button is pressed, and then running what the button should do
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        #Back button
        if 460+280>mouse[0]>460 and 600+110>mouse[1]>600 and click[0]==1:
            start_screen()



#Shows all the controls
def controls_screen():
    background()
    text_loader(100,250,"Controls","press buttons")

    #Loading back button
    img(280,110,460,600,"Button-Back.png")

    while True:
        quit_game()

        #Checking if a button is pressed, and then running what the button should do
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        #Back button
        if 460+280>mouse[0]>460 and 600+110>mouse[1]>600 and click[0]==1:
            start_screen()



#A screen showing information about the game
def about_screen():
    background()
    text_loader(100,250,"About the Game","owo/t")

    #Loading back button
    img(280,110,460,600,"Button-Back.png")

    while True:
        quit_game()

        #Checking if a button is pressed, and then running what the button should do
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        #Back button
        if 460+280>mouse[0]>460 and 600+110>mouse[1]>600 and click[0]==1:
            start_screen()



#The main game
def game():
    points = 100                #Player starts with 100 points

    for repeat in range(10):
        background()
        disp_points(points)
        print("Rep num: "+str(repeat))

        rand_num = random.randint(0,7)
        question_num = levels[rand_num].levelGen(points)


        while True:
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
                points -= 15
                print("wrong")

        pygame.time.wait(50)





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
pygame.display.set_caption("Spore Seeker")

#Setting variables to reference the classes
player = Player()
weapons = Weapons()



## Running the game
start_screen()
#game()
#custom_screen()
#leaderboard_screen()
#about_screen()
