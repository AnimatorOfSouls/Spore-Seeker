import pygame
from pygame.locals import *
from os import path
import random
import sqlite3

working_dir = path.dirname(__file__)

### CLASSES ###
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((78,96))
        self.rect = self.surf.get_rect()
        self.image = pygame.transform.scale(pygame.image.load(path.join(working_dir,"Sprites/Player-Red.png")),(78,96))

    def changeImage(self,image):
        self.image = pygame.transform.scale(pygame.image.load(path.join(working_dir,"Sprites/"+image)),(78,96))



class Question:
    def __init__(self,question,answer,truefalse,difficulty):
        self.question = question
        self.answer = answer
        self.truefalse = truefalse
        self.difficulty = difficulty

    #Loads the screen
    def load(self):
        #displays the question
        text_loader(100,"Question Time!",64)
        text_loader(300,self.question,32)

        #Display True and False buttons
        img(280,110,220,500,"Button-True.png")
        img(280,110,700,500,"Button-False.png")
        img(78,96,561,500,sprite)

    #Check if player gets the right answer
    def check_ans(self,points,player_ans):
        #Checking of the player's answer is correct and changing the score accordingly
        if player_ans == self.truefalse:
            points += (self.difficulty * 10)
            text_loader(400,"Correct",32)
        else:
            points -= (self.difficulty * 5)
            text_loader(400,"Incorrect",32)
            text_loader(450,self.answer,24)

        pygame.time.wait(1500)
        return points



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



#loads text aligned to the center of the screen
def text_loader(pos,text,size):
    #loading a font to be used. Parameters:(font name, font size)
    font = pygame.font.Font('freesansbold.ttf', size)

    #defining the colour of the text, and the displayed text
    text_colour = (91,0,14)

    #Creating a rect surface for text and drawing the text on to the surface
    text = font.render(text, True, text_colour)
    textRect = text.get_rect()

    #setting the central location of the rect
    textRect.center = (600, pos)

    #displaying the text
    screen.blit(text, textRect)
    pygame.display.flip()



#loads text anywhere on the screen
def text_loader_pos(posx,posy,text,size):
    #loading a font to be used. Parameters:(font name, font size)
    font = pygame.font.Font('freesansbold.ttf', size)

    #defining the colour of the text, and the displayed text
    text_colour = (91,0,14)

    #Creating a rect surface for text and drawing the text on to the surface
    text = font.render(text, True, text_colour)
    textRect = text.get_rect()

    #setting the central location of the rect
    textRect.center = (posx, posy)

    #displaying the text
    screen.blit(text, textRect)
    pygame.display.flip()



#displays the number of points
def disp_points(points):
    img(32,32,1050,20,"GUI-Point.png")
    points = str(points)

    text_loader_pos(1125,36,points,32)



#Insertion sort
def insert_sort():
    global highscores

    tempstore = 0
    listpoint = 0

    #Looping through the scores
    for i in range (len(highscores)):
        #Initiating temporary variables
        listpoint = i
        tempstore = highscores[listpoint]


        #Sorting the list
        while listpoint > 0 and highscores[listpoint][1] < highscores[listpoint-1][1]:
            highscores[listpoint] = highscores[listpoint-1]
            listpoint = listpoint-1
            highscores[listpoint] = tempstore

    #Reversing the table to be from highest to lowest
    highscores = highscores[::-1]



#Read database into array
def sql_linker():
    global highscores
    global username
    global points

    conn = sqlite3.connect("Highscores.db")
    cursor = conn.cursor()


    #Creating the table
    conn.execute("CREATE TABLE IF NOT EXISTS highscores(id INTEGER PRIMARY KEY AUTOINCREMENT,username VARCHAR(15),score INT)")


    #Inserting the username and score into the database after a game
    if username != "":
        sql = "INSERT INTO highscores (username,score) VALUES (?,?)"  #The SQL command to run
        val = (username,points)
        cursor.execute(sql,val)  #Inserting the data
        conn.commit()       #Saving the entry


    #Importing database into the array
    cursor.execute("SELECT * FROM highscores")
    myresult = cursor.fetchall()
    for row in myresult:
        highscores.append(row[1:3])


    #Sorting the database
    insert_sort()

    #Closing the connections
    cursor.close()
    conn.close()



#Clearing previously stored data
def clear_data():
    global points
    global username
    global highscores

    points = 100
    username = ""
    highscores = []




### OBJECTS ###
## QUESTIONS ##
questions = []

#True answers
questions.append(Question("In Pokemon, there is a virus called Pokerus that Pokemon can contract.","This is true",True,5))
questions.append(Question("In Super Mario 64, there are 120 stars to collect.","This is true",True,3))
questions.append(Question("In Overwatch, Tracer has exactly 40 bullets in her pistols.","This is true",True,2))
questions.append(Question("In Stardew Valley, there are 30 bundles in the Community Centre.","This is true",True,5))
questions.append(Question("The highest competitive rank in CSGO is Global Elite.","This is true",True,1))
questions.append(Question("In ARK Survival Evolved, the biggest dinosaur is called 'Titanosaur'.","This is true",True,3))
questions.append(Question("In Destiny 2, the three classes are Warlock, Hunter, and Titan.","This is true",True,4))
questions.append(Question("In No Mans Sky, the galaxy you start in is called Euclid.","This is true",True,3))

#False answers
questions.append(Question("The original Legend of Zelda game was released in 1989.","It was released in February 1986.",False,5))
questions.append(Question("In Minecraft, there are 15 colours of wool.","There are 16 colours of wool.",False,2))
questions.append(Question("In Apex Legends, Caustic can set up poison traps and electric fences.","Caustic can set up poison traps and throw a smoke grenade",False,3))
questions.append(Question("League of Legends was published by Riot Entertainment.","League of Legends was published by Riot Games.",False,3))
questions.append(Question("In Rainbow 6 Siege, the operator 'Jager' is an attacker.","Jager is a defender.",False,4))
questions.append(Question("In Breath of the Wild, Hyrule Field was the first area to be made.","The Great Plateau was the first area to be made.",False,5))
questions.append(Question("In Pac-Man, the cyan ghost is called Clyde.","The cyan ghost is called Inky, and the orange ghost is called Clyde.",False,4))
questions.append(Question("The game of the year 2019 was Resident Evil 2.","The game of the year was Sekiro: Shadows Die Twice.",False,4))





### Screens ###
#The start screen with buttons leading to different "pages"
def start_screen():
    background()

    clear_data()

    #Loading icon
    img(512,512,194,144,"Game-Icon-Text.png")

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
            clear_data()
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
            pygame.quit()
            quit()



#The customisation screen with buttons which can be clicked to change the colour of the player's mushroom
def custom_screen():
    background()

    global sprite

    text_loader(100,"Customisation",64)
    text_loader(200,"Pick A Colour",38)
    text_loader(250,"You:",32)

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
    img(195,240,503,280,sprite)
    pygame.display.flip()

    #Prevents accidentally clicking a colour after clicking the button
    pygame.time.wait(50)



    # Running #
    while True:
        quit_game()

        #Displaying the currently selected sprite
        img(195,240,503,280,sprite)

        #Checking if a button is pressed, and then running what the button should do
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        #Back button
        if 460+280>mouse[0]>460 and 600+110>mouse[1]>600 and click[0]==1:
            player.changeImage(sprite)
            start_screen()


        #Red
        if 200+128>mouse[0]>200 and 145+128>mouse[1]>145 and click[0]==1:
            sprite = "Player-Red.png"
        #Pink
        if 200+128>mouse[0]>200 and 400+128>mouse[1]>400 and click[0]==1:
            sprite = "Player-Pink.png"
        #Green
        if 872+128>mouse[0]>872 and 145+128>mouse[1]>145 and click[0]==1:
            sprite = "Player-Green.png"
        #Orange
        if 872+128>mouse[0]>872 and 400+128>mouse[1]>400 and click[0]==1:
            sprite = "Player-Orange.png"



#The leaderboard screen with a highscores table and a button to return to the start screen
def leaderboard_screen():
    background()
    global highscores

    #Clearing highscores to prevent multiple views of leaderboard from adding to the same array
    highscores = []

    text_loader(100,"Leaderboard",64)

    #Loading back button
    img(280,110,460,600,"Button-Back.png")

    #Importing the sorted table
    sql_linker()

    #Displaying the headers for each column
    text_loader_pos(300,150,"Rank",36)
    text_loader_pos(600,150,"Username",36)
    text_loader_pos(900,150,"Spores",36)

    #If there are less than 10 scores saved, the number of scores available will be displayed
    if len(highscores) < 10:
        score_range = len(highscores)
    else:
        score_range = 10

    #Displaying the sorted table using text_loader_pos(posx,posy,text,size)
    text_pos = 200
    for i in range(score_range):
        text_loader_pos(300,text_pos,str(i+1)+")",32)
        text_loader_pos(600,text_pos,highscores[i][0],32)
        text_loader_pos(900,text_pos,str(highscores[i][1]),32)
        text_pos += 40



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
    text_loader(100,"Controls",64)
    text_loader(300,"Click: Left Mouse Button",32)
    text_loader(340,"Type Username: Keyboard Buttons",32)
    text_loader(380,"Type Capitalised Username: Hold Down Shift",32)
    text_loader(420,"Exit Game: Esc Button",32)

    img(280,110,460,600,"Button-Back.png") #Loading back button

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
    text_loader(100,"About the Game",64)
    text_loader(180,"In Spore Seeker, the aim of the game is to collect as",32)
    text_loader(220,"many spores (points) as possible by answering quiz questions.",32)
    text_loader(300,"The game ends after you answer 10 questions.",32)
    text_loader(340,"Each level will present you with game related",32)
    text_loader(380,"true-or-false quiz questions. The top 10 scores will be",32)
    text_loader(420,"displayed on the leaderboard, so only the most knowledgeable",32)
    text_loader(460,"players will be able to reach the top.",32)
    text_loader(540,"GL HF!",32)

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
    global points

    chosen = [] #Making any empty array for previously used rand_num to be appended to

    for repeat in range(10):
        background()
        disp_points(points)

        counter = 0

        rand_num = random.randint(0,len(questions)-1)   #Generating a random number between 0 and the last position in the array of objects

        #Checking if the rand_num has been used before - if it has then a new rand_num will be made.
        while counter < len(chosen) and len(chosen)>0:
            if rand_num == chosen[counter]:                     #Checking if the rand_num has been previously chosen
                counter = 0                                     #Restarting the search from the beginning
                rand_num = random.randint(0,len(questions)-1)   #Rerolling the rand_num
            else:
                counter += 1        #Increaing the counter to look at the next item in the array

        questions[rand_num].load()  #Loading the question
        chosen.append(rand_num)     #Adding the rand_num to the array of previously used rand_num

        while True:
            quit_game()

            #Checking if a button is pressed, and then running what the button should do
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            #True button
            if 220+280>mouse[0]>220 and 500+110>mouse[1]>500 and click[0]==1:
                player_ans = True
                break

            #False button
            if 700+280>mouse[0]>700 and 500+110>mouse[1]>500 and click[0]==1:
                player_ans = False
                break

        points = questions[rand_num].check_ans(points,player_ans)

    game_over()



#Game over screen display number of points and asks for username
def game_over():
    background()
    global points
    global username

    text_loader(200,"Game Over!",64)
    text_loader(300,"Spores Collected: "+str(points),32)
    text_loader(360,"Username:",32)
    text_loader(700,"Press Enter to Continue",32)

    #Defining the font + colour
    font = pygame.font.Font('freesansbold.ttf', 64)
    colour = (171, 62, 153)



    #Recieving username
    while True:
        event = pygame.event.poll()
        keys = pygame.key.get_pressed()

        if event.type == pygame.KEYDOWN:
            key = pygame.key.name(event.key)  #Returns the id of the pressed key

            if len(key) == 1:  #If the key is a letter/number not on numpad...
                if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]: #If shift is being pressed, set the letter to a capital letter
                    username += key.upper()
                else:
                    username += key


            if key == "backspace":
                username = username[:len(username) - 1]
            elif event.key == pygame.K_RETURN:  #If the enter key is pressed, run a check and enter the username
                if len(username) > 15:
                    text_loader(600,"Your username is too long! (max 15 characters)",32)
                    pygame.time.wait(2000)
                elif len(username) <= 0:
                    text_loader(600,"You must enter a username!",32)
                    pygame.time.wait(2000)
                else:
                    leaderboard_screen()



            background()
            text_loader(200,"Game Over!",64)
            text_loader(300,"Spores Collected: "+str(points),32)
            text_loader(360,"Username:",32)
            text_loader(700,"Press Enter to Continue",32)

            text = font.render(username, True, colour)
            text_rect = text.get_rect()
            text_rect.center = (600,450)
            screen.blit(text, text_rect)
            pygame.display.update()





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

#Setting the default sprite colour
sprite = "Player-Red.png"

clear_data()


## Running the game
start_screen()
#game()
#custom_screen()
#leaderboard_screen()
#about_screen()
#game_over()
