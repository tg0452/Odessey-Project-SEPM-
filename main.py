from tkinter import *
import tkinter as ttk
from tkinter import filedialog
from tkinter import messagebox
import os
import sys
import random
import turtle
from pygame.locals import * 
from PIL import Image, ImageTk
import pygame
from math import *
x=1
def delete1():
  screen1.destroy()

def delete2():
  screen2.destroy()
  welcome()

def delete3():
  screen3.destroy()
  welcome()

def delete():
  screen.destroy()
  
def register():
  global screen1
  screen1 = Toplevel(screen)
  screen1.title("Register")
  screen1.geometry("500x250")
  screen1.resizable(0,0)
  screen1.configure(bg="deep sky blue")
  screen1.title("Register")
  
  l1 =Label(screen1, text="Username:", font=("Arial",15), bg="deep sky blue")
  l1.place(x=10, y=10)
  t1 =Entry(screen1,width=30, bd=5)
  t1.place(x = 200, y=10)

  l2 =Label(screen1, text="Password:", font=("Arial",15), bg="deep sky blue")
  l2.place(x=10, y=60)
  t2 =Entry(screen1, width=30, show="*", bd=5)
  t2.place(x = 200, y=60)

  l3 =Label(screen1, text="Confirm Password:", font=("Arial",15), bg="deep sky blue")
  l3.place(x=10, y=110)
  t3 = Entry(screen1, width=30, show="*", bd=5)
  t3.place(x = 200, y=110)
  def check():
    if t1.get()!="" and t2.get()!="" and t3.get()!="":
        if t2.get()==t3.get():
            with open("credential.txt", "a") as f:
                f.write(t1.get()+","+t2.get()+"\n")
                messagebox.showinfo("Welcome","You are registered successfully!!")
                delete1()
        else:
            messagebox.showinfo("Error","Your password didn't get match!!")
    else:
        messagebox.showinfo("Error", "Please fill the complete field!!")
  b1 = Button(screen1, text="Sign in", font=("Arial",15), bg="#ffc22a", command=check)
  b1.place(x=170, y=150)

def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("800x500")
    load = Image.open("guigp/img1.jpg")
    photo = ImageTk.PhotoImage(load)
    label =Label(screen2, image=photo,bd=0)
    label.image=photo
    label.place(x=0,y=0)
    
    border = LabelFrame(screen2, text='Login', bg='ivory', bd = 10, font=("Arial", 20))
    border.pack(fill="both", expand="yes", padx = 150, pady=150)
    
    L1 =Label(border, text="Username", font=("Arial Bold", 15), bg='ivory')
    L1.place(x=50, y=20)
    T1 = Entry(border, width = 30, bd = 5)
    T1.place(x=180, y=20)
    
    L2 = Label(border, text="Password", font=("Arial Bold", 15), bg='ivory')
    L2.place(x=50, y=80)
    T2 =Entry(border, width = 30, show='*', bd = 5)
    T2.place(x=180, y=80)
    def login_verify():
        try:
            with open("credential.txt", "r") as f:
                info = f.readlines()
                i  = 0
                for e in info:
                    u, p =e.split(",")
                    if u.strip() == T1.get() and p.strip() == T2.get():
                        delete2()
                        i = 1
                        break
                if i==0:
                    messagebox.showinfo("Error", "Please provide correct username and password!!")
        except:
            pass
            #messagebox.showinfo("Error", "Please provide correct username and password!!")
  
    B1 =Button(border, text="Submit", font=("Arial", 15), command=login_verify)
    B1.place(x=320, y=115)
def welcome():
    pygame.quit()
    #sys.exit()
    delete()
    global screen3
    screen3 = Tk()
    #screen3.geometry("1350x900+0+0")
    screen3.state('zoomed')
    screen3.title("ODDESY")
    
    frame=Frame(screen3)
    frame.pack(fill=BOTH, expand=1)
    mycanvas=Canvas(frame)
    mycanvas.pack(side=LEFT, fill=BOTH,expand=1)
    scrollbar =Scrollbar(frame, orient=VERTICAL,command=mycanvas.yview)
    scrollbar.pack(side=RIGHT,fill=Y)
    mycanvas.configure(yscrollcommand=scrollbar.set)
    mycanvas.bind('<Configure>',lambda e:mycanvas.configure(scrollregion=mycanvas.bbox("all")))
    Frame_Slider = Frame(mycanvas)
    mycanvas.create_window((0,0),window=Frame_Slider,anchor="nw")


    img = Image.open('guigp/a.jpg')
    img = img.resize((1350, 2800), Image.ANTIALIAS)
    img=ImageTk.PhotoImage(img)
    img2 = Image.open('guigp/b.jpg')
    img2 = img2.resize((1350, 2800), Image.ANTIALIAS)
    img2=ImageTk.PhotoImage(img2)
    img3 = Image.open('guigp/bg.JPG')
    img3 = img3.resize((1350, 2800), Image.ANTIALIAS)
    img3=ImageTk.PhotoImage(img3)
    img4 = Image.open('guigp/bg3.jpg')
    img4 = img4.resize((1350, 2800), Image.ANTIALIAS)
    img4=ImageTk.PhotoImage(img4)
    
    l=Label(Frame_Slider)
    l.pack()
    
# function to change to next image
    def move():
        global x
        if x == 5:
            x = 1
        if x == 1:
            l.config(image=img)
        elif x == 2:
            l.config(image=img2)
        elif x == 3:
            l.config(image=img3)
        elif x == 4:
            l.config(image=img4)
        x = x+1
        Frame_Slider.after(4000, move)

    # calling the function
    move()

    #snake game outlook
    image1=ImageTk.PhotoImage(file="guigp/sk.JPG")
    Frame_Slider1 = Frame(Frame_Slider)
    Frame_Slider1.place(x=150,y=50,width=425,height=157)
    label1=Label(Frame_Slider1,image=image1,bd=0)
    label1.place(x=0,y=0)
    label = Label(Frame_Slider,text='''Snake:
    The classic game that everyone remembers from their handhelds. 
    Your goal is to move the snake and eat as many “food” blocks as possible. 
    There is only one food block at any given time.''',font=('Helvetica', 10, 'bold'),bd=5,fg="brown").place(x=110,y=210)
    my_button = Button(Frame_Slider, text="Play Game", bg='red',command=sn,bd=5,font=('Helvetica', 10, 'bold'),fg="white")
    my_button.place(x=300,y=300)



    #flappy game outlook
    image2=ImageTk.PhotoImage(file="guigp/fb.JPG")
    Frame_Slider1 = Frame(Frame_Slider)
    Frame_Slider1.place(x=150,y=350,width=425,height=157)
    label1=Label(Frame_Slider1,image=image2,bd=0)
    label1.place(x=0,y=0)
    label = Label(Frame_Slider,text='''Flappy Bird :
The simple game about beating your best friends high score and spending hours in the process.
It's flappy bird with more randomness. 
The goal is to get past the obstacles without getting detracted by everything always changing.''',font=('Helvetica', 10, 'bold'),bd=5,fg="red").place(x=60,y=510)
    my_button = Button(Frame_Slider, text="Play Game", bg='red',command=flap,bd=5,font=('Helvetica', 10, 'bold'),fg="white")
    my_button.place(x=300,y=600)


    #Memory game outlook
    image3=ImageTk.PhotoImage(file="guigp/po.JPG")
    Frame_Slider1 = Frame(Frame_Slider)
    Frame_Slider1.place(x=200,y=660,width=240,height=197)
    label11=Label(Frame_Slider1,image=image3,bd=0)
    label11.place(x=0,y=0)
    label2 = Label(Frame_Slider,text='''Memory Game
The all time classic game to check someone's short term memory based on their visuals.
The objective to this game is simple find the matching pairs in the least amount of tries.''',font=('Helvetica', 10, 'bold'),bd=5,fg="olive").place(x=80,y=860)
    my_button1 = Button(Frame_Slider, text="Play Game", bg='red',command=memo,bd=5,font=('Helvetica', 10, 'bold'),fg="white")
    my_button1.place(x=300,y=930)


    #pong game outlook
    image4=ImageTk.PhotoImage(file="guigp/mem.JPG")
    Frame_Slider1 = Frame(Frame_Slider)
    Frame_Slider1.place(x=200,y=990,width=240,height=197)
    label11=Label(Frame_Slider1,image=image4,bd=0)
    label11.place(x=0,y=0)
    label2 = Label(Frame_Slider,text='''Pong :
One of the first ever video games ever built .One may remember facing their sibling/friends in this.
The object is to hit the ball so that it goes over the net and bounces on the opponent's half of the table,
 in such a way that the opponent cannot reach it or return it correctly.''',font=('Helvetica', 10, 'bold'),bd=5,fg="maroon").place(x=40,y=1200)
    my_button1 = Button(Frame_Slider, text="Play Game", bg='red',command=po,bd=5,font=('Helvetica', 10, 'bold'),fg="white")
    my_button1.place(x=300,y=1290)

    #slide puzzle game outlook
    image6=ImageTk.PhotoImage(file="guigp/slid.JPG")
    Frame_Slider1 = Frame(Frame_Slider)
    Frame_Slider1.place(x=230,y=1350,width=240,height=197)
    label11=Label(Frame_Slider1,image=image6,bd=0)
    label11.place(x=0,y=0)
    label2 = Label(Frame_Slider,text='''Slide Puzzle :
Play the classic Game of 15 tile slide puzzle game. 
Slide your tiles around the game board until you have arranged them in the correct order.
As positions are moved into the correct positions, they will turn green.
Relax while playing the game or get your adrenaline rushing as you compete for a new high score.''',font=('Helvetica', 10, 'bold'),bd=5,fg="teal").place(x=60,y=1550)
    my_button1 = Button(Frame_Slider, text="Play Game", bg='red',command=slide,bd=5,font=('Helvetica', 10, 'bold'),fg="white")
    my_button1.place(x=300,y=1655)

    #sudoku game outlook
    image5=ImageTk.PhotoImage(file="guigp/su.JPG")
    Frame_Slider1 = Frame(Frame_Slider)
    Frame_Slider1.place(x=230,y=1700,width=240,height=197)
    label11=Label(Frame_Slider1,image=image5,bd=0)
    label11.place(x=0,y=0)
    label2 = Label(Frame_Slider,text='''Sudoku :
Sudoku is a logic-based puzzle. It is a type of constraint satisfaction problem, 
where the solver is given a finite number of objects (the numerals 1-9)
By playing Sudoku more often, you can solve the puzzle faster and eventually advance to a harder level.
Exercise your mind and you will become happier and smarter.''',font=('Helvetica', 10, 'bold'),bd=5,fg="purple").place(x=70,y=1900)
    my_button1 = Button(Frame_Slider, text="Play Game", bg='red',command=su,bd=5,font=('Helvetica', 10, 'bold'),fg="white")
    my_button1.place(x=300,y=2000)



    #su game outlook
    image7=ImageTk.PhotoImage(file="guigp/fruit.JPG")
    Frame_Slider1 = Frame(Frame_Slider)
    Frame_Slider1.place(x=100,y=2050,width=575,height=274)
    label11=Label(Frame_Slider1,image=image7,bd=0)
    label11.place(x=0,y=0)
    label2 = Label(Frame_Slider,text='''Fruit Ninja :
The Fruit Ninja game is one of the most popular games.
It is a game where fruits appear on the screen and you have to slice them by tapping them.
Enjoy Fruit Ninja!!!''',font=('Helvetica', 10, 'bold'),bd=5,fg="navy").place(x=100,y=2330)
    my_button1 = Button(Frame_Slider, text="Play Game", bg='red',command=fruit,bd=5,font=('Helvetica', 10, 'bold'),fg="white")
    my_button1.place(x=300,y=2420)




    #ballon shooter game outlook
    image8=ImageTk.PhotoImage(file="guigp/ballo.JPG")
    Frame_Slider1 = Frame(Frame_Slider)
    Frame_Slider1.place(x=230,y=2470,width=240,height=197)
    label11=Label(Frame_Slider1,image=image8,bd=0)
    label11.place(x=0,y=0)
    label2 = Label(Frame_Slider,text='''Ballon Shooter :
This game is a simple shooting game.
Here, the player has to use the mouse to shoot the balloon. 
The game is an interesting game.''',font=('Helvetica', 10, 'bold'),bd=5,fg="chocolate").place(x=140,y=2680)
    my_button1 = Button(Frame_Slider, text="Play Game", bg='red',command=ballon,bd=5,font=('Helvetica', 10, 'bold'),fg="white")
    my_button1.place(x=300,y=2760)


    pygame.mixer.init()
    pygame.mixer.music.load('audio/rw.mp3')
    pygame.mixer.music.play(-1)
    screen3.mainloop()
    
def sn():
    #pygame.mixer.music.stop()

    pygame.mixer.init()

    pygame.init()



    # Colors
    white = (255, 255, 255)
    red = (255, 4, 29)
    black = (0, 0, 0)
    brown = (121, 25, 30)
    tomato = (255, 99, 71)
    green = (124, 252, 0)
    light_blue = (30, 144, 255)
    orang = (255, 69 ,0)
    yellow = (255, 215, 0)
    pink = (255, 20, 100)



    # Creating window
    screen_width = 900
    screen_height = 600
    gameWindow = pygame.display.set_mode((screen_width, screen_height))

    #Background Image
    bgimg = pygame.image.load("graphics/bgimg.JPG")
    bgimg = pygame.transform.scale(bgimg, (screen_width, screen_height)).convert_alpha()
    #welcome iamge
    fgimg = pygame.image.load("graphics/fgimg.JPG")
    fgimg = pygame.transform.scale(fgimg, (screen_width, screen_height)).convert_alpha()

    goimg = pygame.image.load("graphics/goimg.JPG")
    goimg = pygame.transform.scale(goimg, (screen_width, screen_height)).convert_alpha()


    #fruit image
    apple = pygame.image.load("graphics/apple.png").convert_alpha()
    mango = pygame.image.load("graphics/mango.png").convert_alpha()
    orange = pygame.image.load("graphics/oranges.png").convert_alpha()
    straw = pygame.image.load("graphics/straw.png").convert_alpha()
    grapes = pygame.image.load("graphics/grapes.png").convert_alpha()
    banana = pygame.image.load("graphics/banana.png").convert_alpha()
    water = pygame.image.load("graphics/water.png").convert_alpha()
    head = pygame.image.load("graphics/snake_head.png").convert_alpha()


    # Game Title
    pygame.display.set_caption("Odyssey")
    pygame.display.update()
    clock = pygame.time.Clock()
    font = pygame.font.SysFont('Ariel', 55)



    def text_screen(text, color, x, y):
        screen_text = font.render(text, True, color)
        gameWindow.blit(screen_text, [x, y])


    def plot_snake(gameWindow, color, snk_list):
        for x, y in snk_list:
            pygame.draw.ellipse(gameWindow, color, [x, y, 25, 25])

    def welcome():
        exit_game = False
        x_pos = 350
        text_x = 350
        color = 'white'
        color2 = light_blue
        flag = False
        while not exit_game:
            gameWindow.fill((233,210,229))
            gameWindow.blit(fgimg, (0, 0))
            frame = pygame.Surface((460, 100))
            frame.fill(color2)
            gameWindow.blit(frame, (x_pos, 460))

            text_screen("Welcome to Fruity Snake", color, text_x, 470)
            text_screen("Press Space Bar To Play", color, text_x, 520)

            if(flag == True):
                text_x -= 1.5
                x_pos -= 1.5
            else:
                x_pos += 1.5
                text_x += 1.5
            if x_pos + 460 == screen_width:
                flag = True
                color = 'white'
                color2 = tomato
            elif x_pos <= 0:
                flag = False
                color = 'white'
                color2 = light_blue
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        pygame.mixer.music.load('audio/Nagin Dhun.mp3')
                        pygame.mixer.music.play(-1)
                        gameloop()

            pygame.display.update()
            clock.tick(60)


    # Game Loop
    def gameloop():
        # Game specific variables
        exit_game = False
        game_over = False
        snake_x = 45
        snake_y = 55
        velocity_x = 0
        velocity_y = 0
        snk_list = []
        snk_length = 1
        # Check if hiscore file exists
        if(not os.path.exists("hiscore.txt")):
            with open("hiscore.txt", "w") as f:
                f.write("0")

        with open("hiscore.txt", "r") as f:
            hiscore = f.read()

        food_x = random.randint(20, screen_width - 100)
        food_y = random.randint(20, screen_height - 100)
        score = 0
        init_velocity = 3
        snake_size = 20
        fps = 60
        food = 1
        while not exit_game:
            if game_over:
                with open("hiscore.txt", "w") as f:
                    f.write(str(hiscore))
                gameWindow.fill(white)
                gameWindow.blit(goimg, (0, 0))
                text_screen("Press Enter To Continue", white, 250, 250)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        #sys.exit()

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            exit_game = True
                            welcome()

            else:

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit_game = True

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RIGHT:
                            velocity_x = init_velocity
                            velocity_y = 0

                        if event.key == pygame.K_LEFT:
                            velocity_x = - init_velocity
                            velocity_y = 0

                        if event.key == pygame.K_UP:
                            velocity_y = - init_velocity
                            velocity_x = 0

                        if event.key == pygame.K_DOWN:
                            velocity_y = init_velocity
                            velocity_x = 0
                        if event.key == pygame.K_z:
                            score += 10

                snake_x = snake_x + velocity_x
                snake_y = snake_y + velocity_y

                if abs(snake_x - food_x) < 30 and abs(snake_y - food_y) < 30:
                    score += 10
                    if food == 1:
                        food = 2
                    elif food == 2:
                        food = 3
                    elif food == 3:
                        food = 4
                    elif food == 4:
                        food = 5
                    elif food == 5:
                        food = 6
                    elif food == 6:
                        food = 7
                    elif food == 7:
                        food = 1
                    if score == 80 or score == 400:
                        pygame.mixer.music.load('audio/Dj Nagin.mp3')
                        pygame.mixer.music.play(-1)
                    elif score == 160:
                        pygame.mixer.music.load('audio/nagin.mp3')
                        pygame.mixer.music.play(-1)
                    elif score == 240:
                        pygame.mixer.music.load('audio/Nagin1.mp3')
                        pygame.mixer.music.play(-1)
                    elif score == 320:
                        pygame.mixer.music.load('audio/Twist Nagin.mp3')
                        pygame.mixer.music.play(-1)




                    if score % 50 == 0:
                        init_velocity += 0.5



                    food_x = random.randint(20, screen_width-100)
                    food_y = random.randint(20, screen_height-100)
                    snk_length += 5
                    if score > int(hiscore):
                        hiscore = score

                gameWindow.fill(white)
                gameWindow.blit(bgimg, (0, 0))
                text_screen("Score: " + str(score) + "  HighScore: "+str(hiscore), white, 5, 5)
                #food rectangle
                if food == 1:
                    f_surface = pygame.Rect(food_x, food_y, 40, 40)
                    gameWindow.blit(apple, f_surface)
                    color = green
                elif food == 2:
                    f_surface = pygame.Rect(food_x, food_y, 40, 40)
                    gameWindow.blit(mango, f_surface)
                    color = red
                elif food == 3:
                    f_surface = pygame.Rect(food_x, food_y, 40, 40)
                    gameWindow.blit(orange, f_surface)
                    color = yellow
                elif food == 4:
                    f_surface = pygame.Rect(food_x, food_y, 80, 80)
                    gameWindow.blit(straw, f_surface)
                    color = orang
                elif food == 5:
                    f_surface = pygame.Rect(food_x, food_y, 60, 60)
                    gameWindow.blit(grapes, f_surface)
                    color = pink
                elif food == 6:
                    f_surface = pygame.Rect(food_x, food_y, 40, 40)
                    gameWindow.blit(banana, f_surface)
                    color = brown
                elif food == 7:
                    f_surface = pygame.Rect(food_x, food_y, 80, 80)
                    gameWindow.blit(water, f_surface)
                    color = white




                head = []
                head.append(snake_x)
                head.append(snake_y)
                snk_list.append(head)


                if len(snk_list)>snk_length:
                    del snk_list[0]

                if head in snk_list[:-1]:
                    game_over = True
                    pygame.mixer.music.load('audio/sfx-defeat3.mp3')
                    pygame.mixer.music.play()

                if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                    game_over = True
                    pygame.mixer.music.load('audio/sfx-defeat3.mp3')
                    pygame.mixer.music.play()
                plot_snake(gameWindow, color, snk_list)
            pygame.display.update()
            clock.tick(fps)

        pygame.quit()
        quit()
    welcome()
  
def flap():
    #delete3()
    pygame.init() 
    pygame.mixer.music.stop()


    FPS = 32
    SCREENWIDTH = 289
    SCREENHEIGHT = 511
    SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
    GROUNDY = SCREENHEIGHT * 0.8
    GROUND2Y = SCREENHEIGHT * 0.7
    GAME_SPRITES = {}
    GAME_SOUNDS = {}
    PLAYER = 'gallery/sprites/bird.png'
    PLAYER2 = 'gallery/sprites/bird2.png' 
    BACKGROUND = 'gallery/sprites/background.png'
    PIPE = 'gallery/sprites/pipe.png'
    font = pygame.font.SysFont(None, 55)
    white = (255, 255, 255)


    def text_screen(text, color, x, y):
        screen_text = font.render(text, True, color)
        SCREEN.blit(screen_text, [x, y])

    def welcomeScreen():
        player2x = int(SCREENWIDTH/3)
        player2y = int((SCREENHEIGHT - GAME_SPRITES['player2'].get_height())/2)
        riverx = 0
        while True:
            for event in pygame.event.get():
        
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    welcome()

                    
                elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                    return
                else:
                    SCREEN.blit(GAME_SPRITES['bg'], (0,1))
                    SCREEN.blit(GAME_SPRITES['player2'], (player2x,player2y))
                    SCREEN.blit(GAME_SPRITES['river'], (riverx,GROUND2Y))
                    text_screen("Flappy Bird", (102, 51, 0), 40,360)
                    text_screen("<TAP TAP>", (255, 51, 0), 50, 450)
                    pygame.display.update()
                    FPSCLOCK.tick(FPS)

    def mainGame():
        score = 0
        playerx = int(SCREENWIDTH/5)
        playery = int(SCREENWIDTH/2)
        basex = 0

        # Create 2 pipes for blitting on the screen
        newPipe1 = getRandomPipe()
        newPipe2 = getRandomPipe()

        # my List of upper pipes
        upperPipes = [
            {'x': SCREENWIDTH+200, 'y':newPipe1[0]['y']},
            {'x': SCREENWIDTH+200+(SCREENWIDTH/2), 'y':newPipe2[0]['y']},
        ]
        # my List of lower pipes
        lowerPipes = [
            {'x': SCREENWIDTH+200, 'y':newPipe1[1]['y']},
            {'x': SCREENWIDTH+200+(SCREENWIDTH/2), 'y':newPipe2[1]['y']},
        ]

        pipeVelX = -4

        playerVelY = -9
        playerMaxVelY = 10
        playerMinVelY = -8
        playerAccY = 1

        playerFlapAccv = -8 # velocity while flapping
        playerFlapped = False # It is true only when the bird is flapping

        

        while True:
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    welcome()
                if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                    if playery > 0:
                        playerVelY = playerFlapAccv
                        playerFlapped = True
                        GAME_SOUNDS['wing'].play()


            crashTest = isCollide(playerx, playery, upperPipes, lowerPipes) # This function will return true if the player is crashed
            if crashTest:
                return 
            

            #check for score
            playerMidPos = playerx + GAME_SPRITES['player'].get_width()/2
            for pipe in upperPipes:
                pipeMidPos = pipe['x'] + GAME_SPRITES['pipe'][0].get_width()/2
                if pipeMidPos<= playerMidPos < pipeMidPos +4:
                    score +=1
                    GAME_SOUNDS['point'].play()


            if playerVelY <playerMaxVelY and not playerFlapped:
                playerVelY += playerAccY

            if playerFlapped:
                playerFlapped = False            
            playerHeight = GAME_SPRITES['player'].get_height()
            playery = playery + min(playerVelY, GROUNDY - playery - playerHeight)

            # move pipes to the left
            for upperPipe , lowerPipe in zip(upperPipes, lowerPipes):
                upperPipe['x'] += pipeVelX
                lowerPipe['x'] += pipeVelX

            # Add a new pipe when the first is about to cross the leftmost part of the screen
            if 0<upperPipes[0]['x']<5:
                newpipe = getRandomPipe()
                upperPipes.append(newpipe[0])
                lowerPipes.append(newpipe[1])

            # if the pipe is out of the screen, remove it
            if upperPipes[0]['x'] < -GAME_SPRITES['pipe'][0].get_width():
                upperPipes.pop(0)
                lowerPipes.pop(0)
            
            # Lets blit our sprites now
            SCREEN.blit(GAME_SPRITES['background'], (0, 0))
            for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
                SCREEN.blit(GAME_SPRITES['pipe'][0], (upperPipe['x'], upperPipe['y']))
                SCREEN.blit(GAME_SPRITES['pipe'][1], (lowerPipe['x'], lowerPipe['y']))

            SCREEN.blit(GAME_SPRITES['base'], (basex, GROUNDY))
            SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))
            myDigits = [int(x) for x in list(str(score))]
            width = 0
            for digit in myDigits:
                width += GAME_SPRITES['numbers'][digit].get_width()
            Xoffset = (SCREENWIDTH - width)/2

            for digit in myDigits:
                SCREEN.blit(GAME_SPRITES['numbers'][digit], (Xoffset, SCREENHEIGHT*0.12))
                Xoffset += GAME_SPRITES['numbers'][digit].get_width()
            pygame.display.update()
            FPSCLOCK.tick(FPS)

    def isCollide(playerx, playery, upperPipes, lowerPipes):
        if playery> GROUNDY - 25  or playery<0:
            GAME_SOUNDS['hit'].play()
            return True
        
        for pipe in upperPipes:
            pipeHeight = GAME_SPRITES['pipe'][0].get_height()
            if(playery < pipeHeight + pipe['y'] and abs(playerx - pipe['x']) < GAME_SPRITES['pipe'][0].get_width()):
                GAME_SOUNDS['hit'].play()
                return True

        for pipe in lowerPipes:
            if (playery + GAME_SPRITES['player'].get_height() > pipe['y']) and abs(playerx - pipe['x']) < GAME_SPRITES['pipe'][0].get_width():
                GAME_SOUNDS['hit'].play()
                return True

        return False

    def getRandomPipe():
        """
        Generate positions of two pipes(one bottom straight and one top rotated ) for blitting on the screen
        """
        pipeHeight = GAME_SPRITES['pipe'][0].get_height()
        offset = SCREENHEIGHT/3
        y2 = offset + random.randrange(0, int(SCREENHEIGHT - GAME_SPRITES['base'].get_height()  - 1.2 *offset))
        pipeX = SCREENWIDTH + 10
        y1 = pipeHeight - y2 + offset
        pipe = [
            {'x': pipeX, 'y': -y1}, #upper Pipe
            {'x': pipeX, 'y': y2} #lower Pipe
        ]
        return pipe



    def gameover(): 
        SCREEN.fill(white)
        goimg = pygame.image.load("gallery/sprites/goimg.png")
        goimg = pygame.transform.scale(goimg, (SCREENWIDTH, SCREENHEIGHT)).convert_alpha()
        SCREEN.blit(goimg, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                        welcome()

            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                            welcomeScreen()


    if __name__ == "__main__":
        # This will be the main point from where our game will start
        FPSCLOCK = pygame.time.Clock()
        pygame.display.set_caption('Flappy Bird')
        GAME_SPRITES['numbers'] = ( 
            pygame.image.load('gallery/sprites/0.png').convert_alpha(),
            pygame.image.load('gallery/sprites/1.png').convert_alpha(),
            pygame.image.load('gallery/sprites/2.png').convert_alpha(),
            pygame.image.load('gallery/sprites/3.png').convert_alpha(),
            pygame.image.load('gallery/sprites/4.png').convert_alpha(),
            pygame.image.load('gallery/sprites/5.png').convert_alpha(),
            pygame.image.load('gallery/sprites/6.png').convert_alpha(),
            pygame.image.load('gallery/sprites/7.png').convert_alpha(),
            pygame.image.load('gallery/sprites/8.png').convert_alpha(),
            pygame.image.load('gallery/sprites/9.png').convert_alpha(),
        )

        # GAME_SPRITES['message'] =pygame.image.load('gallery/sprites/message.png').convert_alpha()
        GAME_SPRITES['river'] =pygame.image.load('gallery/sprites/river.png').convert_alpha()
        GAME_SPRITES['bg'] =pygame.image.load('gallery/sprites/bg.png').convert_alpha()
        GAME_SPRITES['base'] =pygame.image.load('gallery/sprites/base.png').convert_alpha()
        GAME_SPRITES['pipe'] =(pygame.transform.rotate(pygame.image.load( PIPE).convert_alpha(), 180), 
        pygame.image.load(PIPE).convert_alpha()
        )

        # Game sounds
        GAME_SOUNDS['die'] = pygame.mixer.Sound('gallery/audio/die.wav')
        GAME_SOUNDS['hit'] = pygame.mixer.Sound('gallery/audio/hit.wav')
        GAME_SOUNDS['point'] = pygame.mixer.Sound('gallery/audio/point.wav')
        GAME_SOUNDS['swoosh'] = pygame.mixer.Sound('gallery/audio/swoosh.wav')
        GAME_SOUNDS['wing'] = pygame.mixer.Sound('gallery/audio/wing.wav')

        GAME_SPRITES['background'] = pygame.image.load(BACKGROUND).convert()
        GAME_SPRITES['player'] = pygame.image.load(PLAYER).convert_alpha()
        GAME_SPRITES['player2'] = pygame.image.load(PLAYER2).convert_alpha()

        while True:
            welcomeScreen() # Shows welcome screen to the user until he presses a button
            mainGame() # This is the main game function 
            gameover() 

def memo():
    PuzzleWindow=Tk()
    pygame.mixer.music.stop()


 
    PuzzleWindow.title('Memory Puzzle Game By DataFlair')
    
    tabs = ttk.Notebook(PuzzleWindow) 
    easy= ttk.Frame(tabs)

    def draw(a,l,m):
        global base1
        if a=='A':
            d=base1.create_rectangle(100*l+20,m*100+20,100*l+100-20,100*m+100-20,fill='red')
        elif a=='B':
            d=base1.create_rectangle(100*l+20,m*100+20,100*l+100-20,100*m+100-20,fill='yellow')
        elif a=='C':
            d=base1.create_rectangle(100*l+20,m*100+20,100*l+100-20,100*m+100-20,fill='blue')
        elif a=='D':
            d=base1.create_oval(100*l+20,m*100+20,100*l+100-20,100*m+100-20,fill='red')
        elif a=='E':
            d=base1.create_oval(100*l+20,m*100+20,100*l+100-20,100*m+100-20,fill='yellow')
        elif a=='F':
            d=base1.create_oval(100*l+20,m*100+20,100*l+100-20,100*m+100-20,fill='blue')
        elif a=='G':
            d=base1.create_polygon(100*l+50,m*100+20,100*l+20,100*m+100-20,100*l+100-20,100*m+100-20,fill='red')
        elif a=='H':
            d=base1.create_polygon(100*l+50,m*100+20,100*l+20,100*m+100-20,100*l+100-20,100*m+100-20,fill='green')
        
    def quizboard():
        global base1,ans1,board1,moves1
        count=0
        for i in range(4):
            for j in range(4):
                rec=base1.create_rectangle(100*i,j*100,100*i+100,100*j+100,fill="white")
                if(board1[i][j]!='.'):
                    draw(board1[i][j],i,j)
                    count+=1
        if count==16:
            base1.create_text(200,450,text="No. of moves: "+str(moves1),font=('arial',20))
                
    
    def call(event):
        global base1,ans1,board1,moves1,prev1
        i=event.x//100
        j=event.y//100
        if board1[i][j]!='.':
            return
        moves1+=1
        #print(moves)
        if(prev1[0]>4):
            prev1[0]=i
            prev1[1]=j
            board1[i][j]=ans1[i][j]
            quizboard()
        else:
            board1[i][j]=ans1[i][j]
            quizboard()
            if(ans1[i][j]==board1[prev1[0]][prev1[1]]):
                print("matched")
                prev1=[100,100]
                quizboard()
                return
            else:
                board1[prev1[0]][prev1[1]]='.'
                quizboard()
                prev1=[i,j]
                return
    
    base1=Canvas(easy,width=500,height=500)
    base1.pack()
    
    ans1 = list('AABBCCDDEEFFGGHH')
    random.shuffle(ans1)
    ans1 = [ans1[:4],
        ans1[4:8],
        ans1[8:12],
        ans1[12:]]
    
    base1.bind("<Button-1>", call)
    
    moves1=IntVar()
    moves1=0
    
    prev1=[100,100]
    
    board1=[list('.'*4) for count in range(4)]
    quizboard()
    window2= ttk.Frame(tabs)
    
    def draw1(a,l,m):
        global base2
        if a=='A':
            d=base2.create_rectangle(100*l+20,m*100+20,100*l+100-20,100*m+100-20,fill='red')
        elif a=='B':
            d=base2.create_rectangle(100*l+20,m*100+20,100*l+100-20,100*m+100-20,fill='yellow')
        elif a=='C':
            d=base2.create_rectangle(100*l+20,m*100+20,100*l+100-20,100*m+100-20,fill='blue')
        elif a=='D':
            d=base2.create_oval(100*l+20,m*100+20,100*l+100-20,100*m+100-20,fill='red')
        elif a=='E':
            d=base2.create_oval(100*l+20,m*100+20,100*l+100-20,100*m+100-20,fill='yellow')
        elif a=='F':
            d=base2.create_oval(100*l+20,m*100+20,100*l+100-20,100*m+100-20,fill='blue')
        elif a=='G':
            d=base2.create_polygon(100*l+50,m*100+20,100*l+20,100*m+100-20,100*l+100-20,100*m+100-20,fill='red')
        elif a=='H':
            d=base2.create_polygon(100*l+50,m*100+20,100*l+20,100*m+100-20,100*l+100-20,100*m+100-20,fill='green')
        elif a=='I':
            d=base2.create_polygon(100*l+50,m*100+20,100*l+20,100*m+100-20,100*l+100-20,100*m+100-20,fill='yellow')
        elif a=='J':
            d=base2.create_polygon(100*l+50,m*100+20,100*l+20,100*m+100-20,100*l+100-20,100*m+100-20,fill='blue')
        elif a=='K':
            d=base2.create_polygon(100*l+50,m*100+20,100*l+20,100*m+100-20,100*l+100-20,100*m+100-20,fill='black')
        elif a=='L':
            d=base2.create_polygon(100*l+50,m*100+20,100*l+20,100*m+100-20,100*l+100-20,100*m+100-20,fill='orange')
        elif a=='M':
            d=base2.create_rectangle(100*l+20,m*100+20,100*l+100-20,100*m+100-20,fill='black')
        elif a=='N':
            d=base2.create_rectangle(100*l+20,m*100+20,100*l+100-20,100*m+100-20,fill='orange')
        elif a=='O':
            d=base2.create_rectangle(100*l+20,m*100+20,100*l+100-20,100*m+100-20,fill='green')
        elif a=='P':
            d=base2.create_oval(100*l+20,m*100+20,100*l+100-20,100*m+100-20,fill='black')
        elif a=='Q':
            d=base2.create_oval(100*l+20,m*100+20,100*l+100-20,100*m+100-20,fill='orange')
        elif a=='R':
            d=base2.create_oval(100*l+20,m*100+20,100*l+100-20,100*m+100-20,fill='green')
        
        
    def puzzleboard2():
        global base2,ans2,board2,moves2
        count=0
        for i in range(6):
            for j in range(6):
                rec=base2.create_rectangle(100*i,j*100,100*i+100,100*j+100,fill="white")
                if(board2[i][j]!='.'):
                    draw1(board2[i][j],i,j)
                    count+=1
        if count>=36:
            base2.create_text(300,650,text="No. of moves: "+str(moves2),font=('arial',20))
                
    def call2(event):
        global base2,ans2,board2,moves2,prev2
        i=event.x//100
        j=event.y//100
        if board2[i][j]!='.':
            return
        moves2+=1
        if(prev2[0]>6):
            prev2[0]=i
            prev2[1]=j
            board2[i][j]=ans2[i][j]
            puzzleboard2()
        else:
            board2[i][j]=ans2[i][j]
            puzzleboard2()
            if(ans2[i][j]==board2[prev2[0]][prev2[1]]):
                prev2=[100,100]
                puzzleboard2()
                return
            else:
                board2[prev2[0]][prev2[1]]='.'
                puzzleboard2()
                prev2=[i,j]
                return
    base2=Canvas(window2,width=1000,height=1000)
    base2.pack()
    ans2 = list('AABBCCDDEEFFGGHHIIJJKKLLMMNNOOPPQQRR')
    random.shuffle(ans2)
    ans2 = [ans2[:6],
        ans2[6:12],
        ans2[12:18],
        ans2[18:24],
        ans2[24:30],
        ans2[30:]
        ]
    base2.bind("<Button-1>", call2)
    moves2=IntVar()
    moves2=0
    prev2=[100,100]
    board2=[list('.'*6) for count in range(6)]
    puzzleboard2()

    window3= ttk.Frame(tabs)
    tabs.add(easy, text ='Easy') 
    tabs.add(window2, text ='medium') 
    tabs.add(window3, text ='Hard') 
    tabs.pack(expand = 1, fill ="both") 
    
    def draw2(a,l,m):
        global base3
        if a=='A':
            d=base3.create_rectangle(80*l+20,m*80+20,80*l+80-20,80*m+80-20,fill='red')
        elif a=='B':
            d=base3.create_rectangle(80*l+20,m*80+20,80*l+80-20,80*m+80-20,fill='yellow')
        elif a=='C':
            d=base3.create_rectangle(80*l+20,m*80+20,80*l+80-20,80*m+80-20,fill='blue')
        elif a=='D':
            d=base3.create_oval(80*l+20,m*80+20,80*l+80-20,80*m+80-20,fill='red')
        elif a=='E':
            d=base3.create_oval(80*l+20,m*80+20,80*l+80-20,80*m+80-20,fill='yellow')
        elif a=='F':
            d=base3.create_oval(80*l+20,m*80+20,80*l+80-20,80*m+80-20,fill='blue')
        elif a=='G':
            d=base3.create_polygon(80*l+50,m*80+20,80*l+20,80*m+80-20,80*l+80-20,80*m+80-20,fill='red')
        elif a=='H':
            d=base3.create_polygon(80*l+50,m*80+20,80*l+20,80*m+80-20,80*l+80-20,80*m+80-20,fill='green')
        elif a=='I':
            d=base3.create_polygon(80*l+50,m*80+20,80*l+20,80*m+80-20,80*l+80-20,80*m+80-20,fill='yellow')
        elif a=='J':
            d=base3.create_polygon(80*l+50,m*80+20,80*l+20,80*m+80-20,80*l+80-20,80*m+80-20,fill='blue')
        elif a=='K':
            d=base3.create_polygon(80*l+50,m*80+20,80*l+20,80*m+80-20,80*l+80-20,80*m+80-20,fill='black')
        elif a=='L':
            d=base3.create_polygon(80*l+50,m*80+20,80*l+20,80*m+80-20,80*l+80-20,80*m+80-20,fill='orange')
        elif a=='M':
            d=base3.create_rectangle(80*l+20,m*80+20,80*l+80-20,80*m+80-20,fill='black')
        elif a=='N':
            d=base3.create_rectangle(80*l+20,m*80+20,80*l+80-20,80*m+80-20,fill='orange')
        elif a=='O':
            d=base3.create_rectangle(80*l+20,m*80+20,80*l+80-20,80*m+80-20,fill='green')
        elif a=='P':
            d=base3.create_oval(80*l+20,m*80+20,80*l+80-20,80*m+80-20,fill='pink')
        elif a=='Q':
            d=base3.create_oval(80*l+20,m*80+20,80*l+80-20,80*m+80-20,fill='green')
        elif a=='R':
            d=base3.create_rectangle(80*l+20,m*80+20,80*l+80-20,80*m+80-20,fill='pink')
        elif a=='S':
            d=base3.create_rectangle(80*l+20,m*80+20,80*l+80-20,80*m+80-20,fill='purple')
        elif a=='T':
            d=base3.create_oval(80*l+20,m*80+20,80*l+80-20,80*m+80-20,fill='purple')
        elif a=='U':
            d=base3.create_polygon(80*l+50,m*80+20,80*l+20,80*m+80-20,80*l+80-20,80*m+80-20,fill='purple')
        elif a=='V':
            d=base3.create_polygon(80*l+50,m*80+20,80*l+20,80*m+80-20,80*l+80-20,80*m+80-20,fill='pink')
        elif a=='W':
            d=base3.create_polygon(80*l+50,m*80+20,80*l+20,80*m+80-20,80*l+80-20,80*m+80-20,fill='maroon')
        elif a=='X':
            d=base3.create_rectangle(80*l+20,m*80+20,80*l+80-20,80*m+80-20,fill='maroon')
        elif a=='Y':
            d=base3.create_oval(80*l+20,m*80+20,80*l+80-20,80*m+80-20,fill='maroon')
        elif a=='Z':
            d=base3.create_polygon(80*l+50,m*80+20,80*l+20,80*m+80-20,80*l+80-20,80*m+80-20,fill='brown')
        elif a=='a':
            d=base3.create_oval(80*l+20,m*80+20,80*l+80-20,80*m+80-20,fill='brown')
        elif a=='b':
            d=base3.create_rectangle(80*l+20,m*80+20,80*l+80-20,80*m+80-20,fill='brown')
        elif a=='c':
            d=base3.create_polygon(80*l+50,m*80+20,80*l+20,80*m+80-20,80*l+80-20,80*m+80-20,fill='aqua')
        elif a=='d':
            d=base3.create_rectangle(80*l+20,m*80+20,80*l+80-20,80*m+80-20,fill='aqua')
        elif a=='e':
            d=base3.create_oval(80*l+20,m*80+20,80*l+80-20,80*m+80-20,fill='aqua')
        elif a=='f':
            d=base3.create_polygon(80*l+50,m*80+20,80*l+20,80*m+80-20,80*l+80-20,80*m+80-20,fill='magenta')
        elif a=='g':
            d=base3.create_oval(80*l+20,m*80+20,80*l+80-20,80*m+80-20,fill='magenta')
    
    def quizboard3():
        global base3,ans3,board3,moves3
        count=0
        for i in range(8):
            for j in range(8):
                e=base3.create_rectangle(80*i,j*80,80*i+80,80*j+80,fill="white")
                if(board3[i][j]!='.'):
                    draw2(board3[i][j],i,j)
                    count+=1
        if count>=64:
            base3.create_text(300,650,text="No. of moves: "+str(moves3),font=('arial',20))
    
                
    
    def call3(event):
        global base3,ans3,board3,moves3,prev3
        i=event.x//80
        j=event.y//80
        if board3[i][j]!='.':
            return
        moves3+=1
        if(prev3[0]>8):
            prev3[0]=i
            prev3[1]=j
            board3[i][j]=ans3[i][j]
            quizboard3()
        else:
            board3[i][j]=ans3[i][j]
            quizboard3()
            if(ans3[i][j]==board3[prev3[0]][prev3[1]]):
                print("matched")
                prev3=[100,100]
                quizboard3()
                return
            else:
                board3[prev3[0]][prev3[1]]='.'
                quizboard3()
                prev3=[i,j]
                return
    
    base3=Canvas(window3,width=1000,height=1000)
    base3.pack()
    
    ans3 = list('AABBCCDDEEFFGGHHIIJJKKLLMMNNOOPPQQRRSSTTUUWWXXYYZZaabbccddeeffgg')
    random.shuffle(ans3)
    ans3 = [ans3[:8],
        ans3[8:16],
        ans3[16:24],
        ans3[24:32],
        ans3[32:40],
        ans3[40:48],
        ans3[48:56],
        ans3[56:]
        ]
    
    base3.bind("<Button-1>", call3)
    
    moves3=IntVar()
    moves3=0
    
    prev3=[80,80]
    
    board3=[list('.'*8) for count in range(8)]
    quizboard3()
    mainloop()

def po():
    #pygame.mixer.music.stop()


    score_a = 0
    score_b = 0
    screen = turtle.Screen()
    screen.title("Pong odessy")
    screen.bgcolor("black")
    screen.setup(width=800, height=600)
    screen.tracer(0)
    paddle_a = turtle.Turtle()
    paddle_a.speed(0)
    paddle_a.shape("square")
    paddle_a.color("white")
    paddle_a.shapesize(stretch_wid=5, stretch_len=1)
    paddle_a.penup()
    paddle_a.goto(-350, 0)
    paddle_b = turtle.Turtle()
    paddle_b.speed(0)
    paddle_b.shape("square")
    paddle_b.color("white")
    paddle_b.shapesize(stretch_wid=5, stretch_len=1)
    paddle_b.penup()
    paddle_b.goto(350, 0)
    ball = turtle.Turtle()
    ball.speed(0)
    ball.shape("circle")
    ball.color("white")
    ball.penup()
    ball.goto(0, 0)
    ball.dx = 0.3
    ball.dy = -0.3
    pen = turtle.Turtle()
    pen.speed(0)
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 20, "normal"))
    def paddle_a_up():
        y = paddle_a.ycor()
        y += 30
        paddle_a.sety(y)
    def paddle_a_down():
        y = paddle_a.ycor()
        y -= 30
        paddle_a.sety(y)
    def paddle_b_up():
        y = paddle_b.ycor()
        y += 30
        paddle_b.sety(y)
    def paddle_b_down():
        y = paddle_b.ycor()
        y -= 30
        paddle_b.sety(y)
    screen.listen()
    screen.onkeypress(paddle_a_up, "w")
    screen.onkeypress(paddle_a_down, "s")
    screen.onkeypress(paddle_b_up, "Up")
    screen.onkeypress(paddle_b_down, "Down")
    while True:
        screen.update()

        # move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # border checking
        if ball.ycor() > 280:
            ball.sety(280)
            ball.dy *= -1

        if ball.ycor() < -280:
            ball.sety(-280)
            ball.dy *= -1

        #left and right
        if (ball.xcor() < -340 and ball.xcor() > -350) and (paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50):
            score_a += 1
            pen.clear()
            pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 20, "normal"))
        if ball.xcor() > 380:
            score_a = 0
            pen.clear()
            pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 20, "normal"))
            ball.goto(0, 0)
            ball.dx *= -1


        if (ball.xcor() > 340 and ball.xcor() < 350) and (paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50):
            score_b += 1
            pen.clear()
            pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 20, "normal"))
        if ball.xcor() < -380:
            score_b = 0
            pen.clear()
            pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 20, "normal"))
            ball.goto(0, 0)
            ball.dx *= -1


        # paddle and ball collisions
        if (ball.xcor() > 340 and ball.xcor() < 350) and (paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50):
            ball.setx(340)
            ball.dx *= -1

        if (ball.xcor() < -340 and ball.xcor() > -350) and (paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50):
            ball.setx(-340)
            ball.dx *= -1

def su():
    pygame.font.init()
    Window = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("SUDOKU ODESSY")
    x = 0
    z = 0
    diff = 500 / 9
    value= 0
    defaultgrid =[
            [0, 0, 4, 0, 6, 0, 0, 0, 5],
            [7, 8, 0, 4, 0, 0, 0, 2, 0],
            [0, 0, 2, 6, 0, 1, 0, 7, 8],
            [6, 1, 0, 0, 7, 5, 0, 0, 9],
            [0, 0, 7, 5, 4, 0, 0, 6, 1],
            [0, 0, 1, 7, 5, 0, 9, 3, 0],
            [0, 7, 0, 3, 0, 0, 0, 1, 0],
            [0, 4, 0, 2, 0, 6, 0, 0, 7],
            [0, 2, 0, 0, 0, 7, 4, 0, 0],
        ]
    

    font = pygame.font.SysFont("comicsans", 30)
    font1 = pygame.font.SysFont("comicsans", 15)
    def cord(pos):
        global x
        x = pos[0]//diff
        global z
        z = pos[1]//diff

    def highlightbox():
        for k in range(2):
            pygame.draw.line(Window, (0, 0, 0), (x * diff-3, (z + k)*diff), (x * diff + diff + 3, (z + k)*diff), 7)
            pygame.draw.line(Window, (0, 0, 0), ( (x + k)* diff, z * diff ), ((x + k) * diff, z * diff + diff), 7)  
        
    def drawlines():
        for i in range (9):
            for j in range (9):
                if defaultgrid[i][j]!= 0:
                    pygame.draw.rect(Window, (255, 255, 0), (i * diff, j * diff, diff + 1, diff + 1))
                    text1 = font.render(str(defaultgrid[i][j]), 1, (0, 0, 0))
                    Window.blit(text1, (i * diff + 15, j * diff + 15))         
        for l in range(10):
            if l % 3 == 0 :
                thick = 7
            else:
                thick = 1
            pygame.draw.line(Window, (0, 0, 0), (0, l * diff), (500, l * diff), thick)
            pygame.draw.line(Window, (0, 0, 0), (l * diff, 0), (l * diff, 500), thick)     
    
        
    def fillvalue(value):
        text1 = font.render(str(value), 1, (0, 0, 0))
        Window.blit(text1, (x * diff + 15, z * diff + 15))   
    

    def raiseerror():
        text1 = font.render("wrong!", 1, (0, 0, 0))
        Window.blit(text1, (20, 570)) 
    def raiseerror1():
        text1 = font.render("wrong ! enter a valid key for the game", 1, (0, 0, 0))
        Window.blit(text1, (20, 570)) 
    
    def validvalue(m, k, l, value):
        for it in range(9):
            if m[k][it]== value:
                return False
            if m[it][l]== value:
                return False
        it = k//3
        jt = l//3
        for k in range(it * 3, it * 3 + 3):
            for l in range (jt * 3, jt * 3 + 3):
                if m[k][l]== value:
                    return False
        return True
    def solvegame(defaultgrid, i, j):
        
        while defaultgrid[i][j]!= 0:
            if i<8:
                i+= 1
            elif i == 8 and j<8:
                i = 0
                j+= 1
            elif i == 8 and j == 8:
                return True
        pygame.event.pump()   
        for it in range(1, 10):
            if validvalue(defaultgrid, i, j, it)== True:
                defaultgrid[i][j]= it
                global x, z
                x = i
                z = j
                Window.fill((255, 255, 255))
                drawlines()
                highlightbox()
                pygame.display.update()
                pygame.time.delay(20)
                if solvegame(defaultgrid, i, j)== 1:
                    return True
                else:
                    defaultgrid[i][j]= 0
                Window.fill((0,0,0))
            
                drawlines()
                highlightbox()
                pygame.display.update()
                pygame.time.delay(50)   
        return False 
    def gameresult():
        text1 = font.render("game finished", 1, (0, 0, 0))
        Window.blit(text1, (20, 570)) 
    flag=True  
    flag1 = 0
    flag2 = 0
    rs = 0
    error = 0
    while flag:
        Window.fill((255,182,193))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag = False   
            if event.type == pygame.MOUSEBUTTONDOWN:
                flag1 = 1
                pos = pygame.mouse.get_pos()
                cord(pos)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x-= 1
                    flag1 = 1
                if event.key == pygame.K_RIGHT:
                    x+= 1
                    flag1 = 1
                if event.key == pygame.K_UP:
                    y-= 1
                    flag1 = 1
                if event.key == pygame.K_DOWN:
                    y+= 1
                    flag1 = 1   
                if event.key == pygame.K_1:
                    value = 1
                if event.key == pygame.K_2:
                    value = 2   
                if event.key == pygame.K_3:
                    value = 3
                if event.key == pygame.K_4:
                    value = 4
                if event.key == pygame.K_5:
                    value = 5
                if event.key == pygame.K_6:
                    value = 6
                if event.key == pygame.K_7:
                    value = 7
                if event.key == pygame.K_8:
                    value = 8
                if event.key == pygame.K_9:
                    value = 9 
                if event.key == pygame.K_RETURN:
                    flag2 = 1  
                if event.key == pygame.K_r:
                    rs = 0
                    error = 0
                    flag2 = 0
                    defaultgrid=[
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0]
                    ]
                if event.key == pygame.K_d:
                    rs = 0
                    error = 0
                    flag2 = 0
                    defaultgrid  =[
                        [0, 0, 4, 0, 6, 0, 0, 0, 5],
                        [7, 8, 0, 4, 0, 0, 0, 2, 0],
                        [0, 0, 2, 6, 0, 1, 0, 7, 8],
                        [6, 1, 0, 0, 7, 5, 0, 0, 9],
                        [0, 0, 7, 5, 4, 0, 0, 6, 1],
                        [0, 0, 1, 7, 5, 0, 9, 3, 0],
                        [0, 7, 0, 3, 0, 0, 0, 1, 0],
                        [0, 4, 0, 2, 0, 6, 0, 0, 7],
                        [0, 2, 0, 0, 0, 7, 4, 0, 0],
                    ]
        if flag2 == 1:
            if solvegame(defaultgrid , 0, 0)== False:
                error = 1
            else:
                rs = 1
            flag2 = 0   
        if value != 0:           
            fillvalue(value)
            if validvalue(defaultgrid , int(x), int(z), value)== True:
                defaultgrid[int(x)][int(z)]= value
                flag1 = 0
            else:
                defaultgrid[int(x)][int(z)]= 0
                raiseerror1()  
            value = 0   
        
        if error == 1:
            raiseerror() 
        if rs == 1:
            gameresult()       
        drawlines() 
        if flag1 == 1:
            highlightbox()      
        pygame.display.update() 
    
    pygame.quit()

def slide():

    # Create the constants (go ahead and experiment with different values)
    BOARDWIDTH = 4  # number of columns in the board
    BOARDHEIGHT = 4 # number of rows in the board
    TILESIZE = 80
    WINDOWWIDTH = 640
    WINDOWHEIGHT = 480
    FPS = 30
    BLANK = None

    #                 R    G    B
    BLACK =         (  0,   0,   0)
    WHITE =         (255, 255, 255)
    BRIGHTBLUE =    (  0,  50, 255)
    DARKTURQUOISE = (  3,  54,  73)
    GREEN =         (  0, 204,   0)

    BGCOLOR = DARKTURQUOISE
    TILECOLOR = GREEN
    TEXTCOLOR = WHITE
    BORDERCOLOR = BRIGHTBLUE
    BASICFONTSIZE = 20

    BUTTONCOLOR = WHITE
    BUTTONTEXTCOLOR = BLACK
    MESSAGECOLOR = WHITE

    XMARGIN = int((WINDOWWIDTH - (TILESIZE * BOARDWIDTH + (BOARDWIDTH - 1))) / 2)
    YMARGIN = int((WINDOWHEIGHT - (TILESIZE * BOARDHEIGHT + (BOARDHEIGHT - 1))) / 2)

    UP = 'up'
    DOWN = 'down'
    LEFT = 'left'
    RIGHT = 'right'

    def main():
        global FPSCLOCK, DISPLAYSURF, BASICFONT, RESET_SURF, RESET_RECT, NEW_SURF, NEW_RECT, SOLVE_SURF, SOLVE_RECT

        pygame.init()
        FPSCLOCK = pygame.time.Clock()
        DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
        pygame.display.set_caption('Slide Puzzle')
        BASICFONT = pygame.font.Font('freesansbold.ttf', BASICFONTSIZE)

        # Store the option buttons and their rectangles in OPTIONS.
        RESET_SURF, RESET_RECT = makeText('Reset',    TEXTCOLOR, TILECOLOR, WINDOWWIDTH - 120, WINDOWHEIGHT - 90)
        NEW_SURF,   NEW_RECT   = makeText('New Game', TEXTCOLOR, TILECOLOR, WINDOWWIDTH - 120, WINDOWHEIGHT - 60)
        SOLVE_SURF, SOLVE_RECT = makeText('Solve',    TEXTCOLOR, TILECOLOR, WINDOWWIDTH - 120, WINDOWHEIGHT - 30)

        mainBoard, solutionSeq = generateNewPuzzle(80)
        SOLVEDBOARD = getStartingBoard() # a solved board is the same as the board in a start state.
        allMoves = [] # list of moves made from the solved configuration

        while True: # main game loop
            slideTo = None # the direction, if any, a tile should slide
            msg = 'Click tile or press arrow keys to slide.' # contains the message to show in the upper left corner.
            if mainBoard == SOLVEDBOARD:
                msg = 'Solved!'

            drawBoard(mainBoard, msg)

            checkForQuit()
            for event in pygame.event.get(): # event handling loop
                if event.type == MOUSEBUTTONUP:
                    spotx, spoty = getSpotClicked(mainBoard, event.pos[0], event.pos[1])

                    if (spotx, spoty) == (None, None):
                        # check if the user clicked on an option button
                        if RESET_RECT.collidepoint(event.pos):
                            resetAnimation(mainBoard, allMoves) # clicked on Reset button
                            allMoves = []
                        elif NEW_RECT.collidepoint(event.pos):
                            mainBoard, solutionSeq = generateNewPuzzle(80) # clicked on New Game button
                            allMoves = []
                        elif SOLVE_RECT.collidepoint(event.pos):
                            resetAnimation(mainBoard, solutionSeq + allMoves) # clicked on Solve button
                            allMoves = []
                    else:
                        # check if the clicked tile was next to the blank spot

                        blankx, blanky = getBlankPosition(mainBoard)
                        if spotx == blankx + 1 and spoty == blanky:
                            slideTo = LEFT
                        elif spotx == blankx - 1 and spoty == blanky:
                            slideTo = RIGHT
                        elif spotx == blankx and spoty == blanky + 1:
                            slideTo = UP
                        elif spotx == blankx and spoty == blanky - 1:
                            slideTo = DOWN

                elif event.type == KEYUP:
                    # check if the user pressed a key to slide a tile
                    if event.key in (K_LEFT, K_a) and isValidMove(mainBoard, LEFT):
                        slideTo = LEFT
                    elif event.key in (K_RIGHT, K_d) and isValidMove(mainBoard, RIGHT):
                        slideTo = RIGHT
                    elif event.key in (K_UP, K_w) and isValidMove(mainBoard, UP):
                        slideTo = UP
                    elif event.key in (K_DOWN, K_s) and isValidMove(mainBoard, DOWN):
                        slideTo = DOWN

            if slideTo:
                slideAnimation(mainBoard, slideTo, 'Click tile or press arrow keys to slide.', 8) # show slide on screen
                makeMove(mainBoard, slideTo)
                allMoves.append(slideTo) # record the slide
            pygame.display.update()
            FPSCLOCK.tick(FPS)


    def terminate():
        welcome()


    def checkForQuit():
        for event in pygame.event.get(QUIT): # get all the QUIT events
            terminate() # terminate if any QUIT events are present
        for event in pygame.event.get(KEYUP): # get all the KEYUP events
            if event.key == K_ESCAPE:
                terminate() # terminate if the KEYUP event was for the Esc key
            pygame.event.post(event) # put the other KEYUP event objects back


    def getStartingBoard():
        # Return a board data structure with tiles in the solved state.
        # For example, if BOARDWIDTH and BOARDHEIGHT are both 3, this function
        # returns [[1, 4, 7], [2, 5, 8], [3, 6, BLANK]]
        counter = 1
        board = []
        for x in range(BOARDWIDTH):
            column = []
            for y in range(BOARDHEIGHT):
                column.append(counter)
                counter += BOARDWIDTH
            board.append(column)
            counter -= BOARDWIDTH * (BOARDHEIGHT - 1) + BOARDWIDTH - 1

        board[BOARDWIDTH-1][BOARDHEIGHT-1] = BLANK
        return board


    def getBlankPosition(board):
        # Return the x and y of board coordinates of the blank space.
        for x in range(BOARDWIDTH):
            for y in range(BOARDHEIGHT):
                if board[x][y] == BLANK:
                    return (x, y)


    def makeMove(board, move):
        # This function does not check if the move is valid.
        blankx, blanky = getBlankPosition(board)

        if move == UP:
            board[blankx][blanky], board[blankx][blanky + 1] = board[blankx][blanky + 1], board[blankx][blanky]
        elif move == DOWN:
            board[blankx][blanky], board[blankx][blanky - 1] = board[blankx][blanky - 1], board[blankx][blanky]
        elif move == LEFT:
            board[blankx][blanky], board[blankx + 1][blanky] = board[blankx + 1][blanky], board[blankx][blanky]
        elif move == RIGHT:
            board[blankx][blanky], board[blankx - 1][blanky] = board[blankx - 1][blanky], board[blankx][blanky]


    def isValidMove(board, move):
        blankx, blanky = getBlankPosition(board)
        return (move == UP and blanky != len(board[0]) - 1) or \
            (move == DOWN and blanky != 0) or \
            (move == LEFT and blankx != len(board) - 1) or \
            (move == RIGHT and blankx != 0)


    def getRandomMove(board, lastMove=None):
        # start with a full list of all four moves
        validMoves = [UP, DOWN, LEFT, RIGHT]

        # remove moves from the list as they are disqualified
        if lastMove == UP or not isValidMove(board, DOWN):
            validMoves.remove(DOWN)
        if lastMove == DOWN or not isValidMove(board, UP):
            validMoves.remove(UP)
        if lastMove == LEFT or not isValidMove(board, RIGHT):
            validMoves.remove(RIGHT)
        if lastMove == RIGHT or not isValidMove(board, LEFT):
            validMoves.remove(LEFT)

        # return a random move from the list of remaining moves
        return random.choice(validMoves)


    def getLeftTopOfTile(tileX, tileY):
        left = XMARGIN + (tileX * TILESIZE) + (tileX - 1)
        top = YMARGIN + (tileY * TILESIZE) + (tileY - 1)
        return (left, top)


    def getSpotClicked(board, x, y):
        # from the x & y pixel coordinates, get the x & y board coordinates
        for tileX in range(len(board)):
            for tileY in range(len(board[0])):
                left, top = getLeftTopOfTile(tileX, tileY)
                tileRect = pygame.Rect(left, top, TILESIZE, TILESIZE)
                if tileRect.collidepoint(x, y):
                    return (tileX, tileY)
        return (None, None)


    def drawTile(tilex, tiley, number, adjx=0, adjy=0):
        # draw a tile at board coordinates tilex and tiley, optionally a few
        # pixels over (determined by adjx and adjy)
        left, top = getLeftTopOfTile(tilex, tiley)
        pygame.draw.rect(DISPLAYSURF, TILECOLOR, (left + adjx, top + adjy, TILESIZE, TILESIZE))
        textSurf = BASICFONT.render(str(number), True, TEXTCOLOR)
        textRect = textSurf.get_rect()
        textRect.center = left + int(TILESIZE / 2) + adjx, top + int(TILESIZE / 2) + adjy
        DISPLAYSURF.blit(textSurf, textRect)


    def makeText(text, color, bgcolor, top, left):
        # create the Surface and Rect objects for some text.
        textSurf = BASICFONT.render(text, True, color, bgcolor)
        textRect = textSurf.get_rect()
        textRect.topleft = (top, left)
        return (textSurf, textRect)


    def drawBoard(board, message):
        DISPLAYSURF.fill(BGCOLOR)
        if message:
            textSurf, textRect = makeText(message, MESSAGECOLOR, BGCOLOR, 5, 5)
            DISPLAYSURF.blit(textSurf, textRect)

        for tilex in range(len(board)):
            for tiley in range(len(board[0])):
                if board[tilex][tiley]:
                    drawTile(tilex, tiley, board[tilex][tiley])

        left, top = getLeftTopOfTile(0, 0)
        width = BOARDWIDTH * TILESIZE
        height = BOARDHEIGHT * TILESIZE
        pygame.draw.rect(DISPLAYSURF, BORDERCOLOR, (left - 5, top - 5, width + 11, height + 11), 4)

        DISPLAYSURF.blit(RESET_SURF, RESET_RECT)
        DISPLAYSURF.blit(NEW_SURF, NEW_RECT)
        DISPLAYSURF.blit(SOLVE_SURF, SOLVE_RECT)


    def slideAnimation(board, direction, message, animationSpeed):
        # Note: This function does not check if the move is valid.

        blankx, blanky = getBlankPosition(board)
        if direction == UP:
            movex = blankx
            movey = blanky + 1
        elif direction == DOWN:
            movex = blankx
            movey = blanky - 1
        elif direction == LEFT:
            movex = blankx + 1
            movey = blanky
        elif direction == RIGHT:
            movex = blankx - 1
            movey = blanky

        # prepare the base surface
        drawBoard(board, message)
        baseSurf = DISPLAYSURF.copy()
        # draw a blank space over the moving tile on the baseSurf Surface.
        moveLeft, moveTop = getLeftTopOfTile(movex, movey)
        pygame.draw.rect(baseSurf, BGCOLOR, (moveLeft, moveTop, TILESIZE, TILESIZE))

        for i in range(0, TILESIZE, animationSpeed):
            # animate the tile sliding over
            checkForQuit()
            DISPLAYSURF.blit(baseSurf, (0, 0))
            if direction == UP:
                drawTile(movex, movey, board[movex][movey], 0, -i)
            if direction == DOWN:
                drawTile(movex, movey, board[movex][movey], 0, i)
            if direction == LEFT:
                drawTile(movex, movey, board[movex][movey], -i, 0)
            if direction == RIGHT:
                drawTile(movex, movey, board[movex][movey], i, 0)

            pygame.display.update()
            FPSCLOCK.tick(FPS)


    def generateNewPuzzle(numSlides):
        # From a starting configuration, make numSlides number of moves (and
        # animate these moves).
        sequence = []
        board = getStartingBoard()
        drawBoard(board, '')
        pygame.display.update()
        pygame.time.wait(500) # pause 500 milliseconds for effect
        lastMove = None
        for i in range(numSlides):
            move = getRandomMove(board, lastMove)
            slideAnimation(board, move, 'Generating new puzzle...', animationSpeed=int(TILESIZE / 3))
            makeMove(board, move)
            sequence.append(move)
            lastMove = move
        return (board, sequence)


    def resetAnimation(board, allMoves):
        # make all of the moves in allMoves in reverse.
        revAllMoves = allMoves[:] # gets a copy of the list
        revAllMoves.reverse()

        for move in revAllMoves:
            if move == UP:
                oppositeMove = DOWN
            elif move == DOWN:
                oppositeMove = UP
            elif move == RIGHT:
                oppositeMove = LEFT
            elif move == LEFT:
                oppositeMove = RIGHT
            slideAnimation(board, oppositeMove, '', animationSpeed=int(TILESIZE / 2))
            makeMove(board, oppositeMove)


    if __name__ == '__main__':
        main()

def fruit():
    player_lives = 3                                                #keep track of lives
    score = 0                                                       #keeps track of score
    fruits = ['melon', 'orange', 'pomegranate', 'guava', 'bomb']    #entities in the game

    # initialize pygame and create window
    WIDTH = 800
    HEIGHT = 500
    FPS = 12                                                 #controls how often the gameDisplay should refresh. In our case, it will refresh every 1/12th second
    pygame.init()
    pygame.display.set_caption('Fruit-Ninja Game')
    gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))   #setting game display size
    clock = pygame.time.Clock()

    # Define colors
    WHITE = (255,255,255)
    BLACK = (0,0,0)
    RED = (255,0,0)
    GREEN = (0,255,0)
    BLUE = (0,0,255)

    background = pygame.image.load('graphics/back.jpg')                                  #game background
    font = pygame.font.SysFont(None, 55)
    score_text = font.render('Score : ' + str(score), True, (255, 255, 255))    #score display
    lives_icon = pygame.image.load('graphics/white_lives.png')                    #images that shows remaining lives

    # Generalized structure of the fruit Dictionary
    def generate_random_fruits(fruit):
        fruit_path = "graphics/" + fruit + ".png"
        data[fruit] = {
            'img': pygame.image.load(fruit_path),
            'x' : random.randint(100,500),          #where the fruit should be positioned on x-coordinate
            'y' : 800,
            'speed_x': random.randint(-5,5),      #how fast the fruit should move in x direction. Controls the diagonal movement of fruits
            'speed_y': random.randint(-80, -60),    #control the speed of fruits in y-directionn ( UP )
            'throw': False,                         #determines if the generated coordinate of the fruits is outside the gameDisplay or not. If outside, then it will be discarded
            't': 0,                                 #manages the
            'hit': False,
        }

        if random.random() >= 0.75:     #Return the next random floating point number in the range [0.0, 1.0) to keep the fruits inside the gameDisplay
            data[fruit]['throw'] = True
        else:
            data[fruit]['throw'] = False

    # Dictionary to hold the data the random fruit generation
    data = {}
    for fruit in fruits:
        generate_random_fruits(fruit)

    def hide_cross_lives(x, y):
        gameDisplay.blit(pygame.image.load("graphics/red_lives.png"), (x, y))

    # Generic method to draw fonts on the screen
    font_name = pygame.font.match_font('comic.ttf')
    def draw_text(display, text, size, x, y):
        font = pygame.font.Font(font_name, size)
        text_surface = font.render(text, True, WHITE)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        gameDisplay.blit(text_surface, text_rect)

    # draw players lives
    def draw_lives(display, x, y, lives, image) :
        for i in range(lives) :
            img = pygame.image.load(image)
            img_rect = img.get_rect()       #gets the (x,y) coordinates of the cross icons (lives on the the top rightmost side)
            img_rect.x = int(x + 35 * i)    #sets the next cross icon 35pixels awt from the previous one
            img_rect.y = y                  #takes care of how many pixels the cross icon should be positioned from top of the screen
            display.blit(img, img_rect)

    # show game over display & front display
    def show_gameover_screen():
        gameDisplay.blit(background, (0,0))
        draw_text(gameDisplay, "FRUIT NINJA!", 90, WIDTH / 2, HEIGHT / 4)
        if not game_over :
            draw_text(gameDisplay,"Score : " + str(score), 50, WIDTH / 2, HEIGHT /2)

        draw_text(gameDisplay, "Press a key to begin!", 64, WIDTH / 2, HEIGHT * 3 / 4)
        pygame.display.flip()
        waiting = True
        while waiting:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    welcome()
                if event.type == pygame.KEYUP:
                    waiting = False

    # Game Loop
    first_round = True
    game_over = True        #terminates the game While loop if more than 3-Bombs are cut
    game_running = True     #used to manage the game loop
    while game_running :
        if game_over :
            if first_round :
                show_gameover_screen()
                first_round = False
            game_over = False
            player_lives = 3
            draw_lives(gameDisplay, 690, 5, player_lives, 'graphics/red_lives.png')
            score = 0

        for event in pygame.event.get():
            # checking for closing window
            if event.type == pygame.QUIT:
                game_running = False

        gameDisplay.blit(background, (0, 0))
        gameDisplay.blit(score_text, (0, 0))
        draw_lives(gameDisplay, 690, 5, player_lives, 'graphics/red_lives.png')

        for key, value in data.items():
            if value['throw']:
                value['x'] += value['speed_x']          #moving the fruits in x-coordinates
                value['y'] += value['speed_y']          #moving the fruits in y-coordinate
                value['speed_y'] += (1 * value['t'])    #increasing y-corrdinate
                value['t'] += 1                         #increasing speed_y for next loop

                if value['y'] <= 800:
                    gameDisplay.blit(value['img'], (value['x'], value['y']))    #displaying the fruit inside screen dynamically
                else:
                    generate_random_fruits(key)

                current_position = pygame.mouse.get_pos()   #gets the current coordinate (x, y) in pixels of the mouse

                if not value['hit'] and current_position[0] > value['x'] and current_position[0] < value['x']+60 \
                        and current_position[1] > value['y'] and current_position[1] < value['y']+60:
                    if key == 'bomb':
                        player_lives -= 1
                        if player_lives == 0:
                            
                            hide_cross_lives(690, 15)
                        elif player_lives == 1 :
                            hide_cross_lives(725, 15)
                        elif player_lives == 2 :
                            hide_cross_lives(760, 15)
                        #if the user clicks bombs for three time, GAME OVER message should be displayed and the window should be reset
                        if player_lives < 0 :
                            show_gameover_screen()
                            game_over = True

                        half_fruit_path = "graphics/explosion.png"
                    else:
                        half_fruit_path = "graphics/" + "half_" + key + ".png"

                    value['img'] = pygame.image.load(half_fruit_path)
                    value['speed_x'] += 5
                    if key != 'bomb' :
                        score += 1
                    score_text = font.render('Score : ' + str(score), True, (255, 255, 255))
                    value['hit'] = True
            else:
                generate_random_fruits(key)

        pygame.display.update()
        clock.tick(FPS)      # keep loop running at the right speed (manages the frame/second. The loop should update afer every 1/12th pf the sec
                            

    pygame.quit()
score = 0
def ballon():

    pygame.init()

    width = 500
    height = 500

    display = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Balloon Shooter")
    clock = pygame.time.Clock()

    margin = 100
    lowerBound = 100


    # Colors
    white = (230, 230, 230)
    lightBlue = (174, 214, 241)
    red = (231, 76, 60)
    lightGreen = (25, 111, 61)
    darkGray = (40, 55, 71)
    darkBlue = (21, 67, 96)
    green = (35, 155, 86)
    yellow = (244, 208, 63)
    blue = (46, 134, 193)
    purple = (155, 89, 182)
    orange = (243, 156, 18)

    font = pygame.font.SysFont("Snap ITC", 25)

    # Balloon Class
    class Balloon:
        def __init__(self, speed):
            self.a = random.randint(30, 40)
            self.b = self.a + random.randint(0, 10)
            self.x = random.randrange(margin, width - self.a - margin)
            self.y = height - lowerBound
            self.angle = 90
            self.speed = -speed
            self.probPool = [-1, -1, -1, 0, 0, 0, 0, 1, 1, 1]
            self.length = random.randint(50, 100)
            self.color = random.choice([red, green, purple, orange, yellow, blue])

        # Move balloon around the Screen
        def move(self):
            direct = random.choice(self.probPool)

            if direct == -1:
                self.angle += -10
            elif direct == 0:
                self.angle += 0
            else:
                self.angle += 10

            self.y += self.speed*sin(radians(self.angle))
            self.x += self.speed*cos(radians(self.angle))

            if (self.x + self.a > width) or (self.x < 0):
                if self.y > height/5:
                    self.x -= self.speed*cos(radians(self.angle)) 
                else:
                    self.reset()
            if self.y + self.b < 0 or self.y > height + 30:
                self.reset()

        # Show/Draw the balloon  
        def show(self):
            pygame.draw.line(display, darkBlue, (self.x + self.a/2, self.y + self.b), (self.x + self.a/2, self.y + self.b + self.length))
            pygame.draw.ellipse(display, self.color, (self.x, self.y, self.a, self.b))
            pygame.draw.ellipse(display, self.color, (self.x + self.a/2 - 5, self.y + self.b - 3, 10, 10))

        # Check if Balloon is bursted
        def burst(self):
            global score
            pos = pygame.mouse.get_pos()

            if onBalloon(self.x, self.y, self.a, self.b, pos):
                score += 1
                self.reset()

        # Reset the Balloon
        def reset(self):
            self.a = random.randint(30, 40)
            self.b = self.a + random.randint(0, 10)
            self.x = random.randrange(margin, width - self.a - margin)
            self.y = height - lowerBound 
            self.angle = 90
            self.speed -= 0.002
            self.probPool = [-1, -1, -1, 0, 0, 0, 0, 1, 1, 1]
            self.length = random.randint(50, 100)
            self.color = random.choice([red, green, purple, orange, yellow, blue])

    balloons = []
    noBalloon = 10
    for i in range(noBalloon):
        obj = Balloon(random.choice([1, 1, 2, 2, 2, 2, 3, 3, 3, 4]))
        balloons.append(obj)

    def onBalloon(x, y, a, b, pos):
        if (x < pos[0] < x + a) and (y < pos[1] < y + b):
            return True
        else:
            return False

    # show the location of Mouse
    def pointer():
        pos = pygame.mouse.get_pos()
        r = 25
        l = 20
        color = lightGreen
        for i in range(noBalloon):
            if onBalloon(balloons[i].x, balloons[i].y, balloons[i].a, balloons[i].b, pos):
                color = red
        pygame.draw.ellipse(display, color, (pos[0] - r/2, pos[1] - r/2, r, r), 4)
        pygame.draw.line(display, color, (pos[0], pos[1] - l/2), (pos[0], pos[1] - l), 4)
        pygame.draw.line(display, color, (pos[0] + l/2, pos[1]), (pos[0] + l, pos[1]), 4)
        pygame.draw.line(display, color, (pos[0], pos[1] + l/2), (pos[0], pos[1] + l), 4)
        pygame.draw.line(display, color, (pos[0] - l/2, pos[1]), (pos[0] - l, pos[1]), 4)

    def lowerPlatform():
        pygame.draw.rect(display, darkGray, (0, height - lowerBound, width, lowerBound))

    def showScore():
        scoreText = font.render("Balloons Bursted : " + str(score), True, white)
        display.blit(scoreText, (150, height - lowerBound + 50))


    def close():
        welcome()

    def game():
        global score
        loop = True

        while loop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    close()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        close()
                    if event.key == pygame.K_r:
                        score = 0
                        game()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i in range(noBalloon):
                        balloons[i].burst()

            display.fill(lightBlue)
            
            for i in range(noBalloon):
                balloons[i].show()

            pointer()
            
            for i in range(noBalloon):
                balloons[i].move()

            
            lowerPlatform()
            showScore()
            pygame.display.update()
            clock.tick(60)


    game()

def main_screen():
  global screen
  screen = Tk()
  screen.geometry("300x250")
  screen.title("Main Screen")
  Label(text = "Welcome!", bg = "grey", width = "300", height = "2", font = ("Calibri", 13)).pack()
  Label(text = "").pack()
  Button(text = "Login", height = "2", width = "30", command = login).pack()
  Label(text = "").pack()
  Button(text = "Register",height = "2", width = "30", command = register).pack()

  screen.mainloop()
main_screen()