from graphics import Canvas
import random
import pygame
import time

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
SIZE = 20
DELAY = 100 #ms

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    canvas._canvas.master.title("Basilisk Run")
    player = canvas.create_rectangle(0, 0, SIZE, SIZE, "skyblue", "black")
    goal_x = 360
    goal_y = 360
    goal = canvas.create_rectangle(goal_x, goal_y, goal_x+SIZE, goal_y+SIZE, "salmon", "red")

    max_index = (CANVAS_WIDTH // SIZE) - 1

    move = 'Right'

    delay = DELAY
    score = 0
    game_start = False
    game_over = False
    game_over_text1 = None
    game_over_text2 = None

    score_display = canvas.create_text(CANVAS_WIDTH // 2, 10, f"Points: {score}", font='Arial', font_size=15, color='black', anchor='n')
    start_text = canvas.create_text(CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2, text="Press Enter to Start", font="Arial", font_size=20, color="black", anchor="center")


    # sound
    pygame.mixer.init()
    eating = pygame.mixer.Sound("sounds/Crunch.wav")
    out = pygame.mixer.Sound("sounds/gameover.wav")
    background = pygame.mixer.Sound("sounds/background.wav")

    def reset_game():
        nonlocal move, delay, score, game_over, game_over_text1, game_over_text2, score_display
        canvas.moveto(player, 0, 0)
        new_x = random.randint(0, max_index) * SIZE
        new_y = random.randint(0, max_index) * SIZE
        canvas.moveto(goal, new_x, new_y)
        delay = DELAY
        score = 0
        move = 'Right'
        game_over = False
        if game_over_text1 is not None:
            canvas.delete(game_over_text1)
            game_over_text1 = None
        if game_over_text2 is not None:
            canvas.delete(game_over_text2)
            game_over_text2 = None

        canvas.delete(score_display)
        score_display = canvas.create_text(CANVAS_WIDTH // 2, 10, f"Points: {score}", font='Arial', font_size=15, color='black', anchor='n')

    #-------------------------

    def countdown(seconds):          # 24 june added countdown
        nonlocal start_text
        if seconds == 0: 
            canvas.delete(start_text) # will first delete countdown start_text canvas
            background.play(loops=-1) # then play background song for infinity loop=-1
            game_loop()         # then call the game loop
        else:
            canvas.change_text(start_text, str(seconds))   # change_text will change the existing object start_text to show new text, and making vising by str(seconds)
            canvas._canvas.after(1000, next_countdown, seconds-1)  # using after function, each 1000 millisecond/1 second (n -1). 

   
    def next_countdown(seconds):  # next_countdown will call itself until countdown is 0
        countdown(seconds)



    def on_key(event):
        nonlocal move, game_over, game_start

        if not game_start and event.keysym == 'Return':
            game_start = True           
            countdown(3)         # 3 seconds passed

        if not game_over:
            if event.keysym in ['Left', 'Right', 'Up', 'Down']:
                move = event.keysym
                
        else:
            if event.keysym == 'Return': #restart
                reset_game()
                game_loop()
                background.play(loops=-1)

    canvas._canvas.bind("<Key>", on_key)
    canvas._canvas.focus_set()



    #--------------
    def game_loop():
        nonlocal move, delay, score, score_display, game_over, game_over_text1, game_over_text2

        if game_over:
            return  # stop movement after game over

        if move == 'Left':
            canvas.move(player, -SIZE, 0)
        elif move == 'Right':
            canvas.move(player, SIZE, 0)
        elif move == 'Up':
            canvas.move(player, 0, -SIZE)
        elif move == 'Down':
            canvas.move(player, 0, SIZE)

        x = canvas.get_left_x(player)
        y = canvas.get_top_y(player)

        # boundary
        if x < 0 or x >= CANVAS_WIDTH or y < 0 or y >= CANVAS_HEIGHT:
            out.play()
            background.stop()
            game_over_text1 = canvas.create_text( CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2, text="Game Over!", font="Arial", font_size=30, color="Red", anchor='center')
            game_over_text2 = canvas.create_text( CANVAS_WIDTH // 2, CANVAS_HEIGHT //2 +30, text="Press Enter to Restart", font="Arial", font_size=15, color="black", anchor="center")
            
            game_over = True
            return

        goal_x = canvas.get_left_x(goal)
        goal_y = canvas.get_top_y(goal)

        # if snake eats
        if x == goal_x and y == goal_y:
            score += 1
            eating.play()
            new_x = random.randint(0, max_index) * SIZE
            new_y = random.randint(0, max_index) * SIZE
            canvas.moveto(goal, new_x, new_y)
            canvas.delete(score_display)
            score_display = canvas.create_text(CANVAS_WIDTH // 2, 10, f"Points: {score}", font='Arial', font_size=15, color='black', anchor='n')


            if score % 3 == 0:
                delay = int(delay * 0.9)

        canvas._canvas.after(delay, game_loop)

    
    canvas.run()



if __name__ == '__main__':
    main()