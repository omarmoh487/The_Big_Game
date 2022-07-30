from tkinter import *
import random
#from T_BG import big_GUI

# Game Settings

GAME_WIDTH = 1000
GAME_HEIGHT = 450
SPEED = 120             # Snake speed: (The lower the number the faster the snake)
SPACE_SIZE = 50         # to change snake and food size
BODY_PARTS = 5
SNAKE_COLOR = "#FF0000"
FOOD_COLOR = "#00FF00"
BACKGROUND_COLOR = "#FFFF00"   # Background color for the canvas
canvas = 0
label = 0
window = 0
score = 0
direction = 'right'


class Snake:
    def __init__(self):  # Constructor
        global canvas

        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):   # list for coordinates
            self.coordinates.append([0, 0])  # [0, 0] for making the snake appear at the top left corner
        for x, y in self.coordinates:   # List of lists for making the body of the snake
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)  # to make the snake bigger


class Food:

    # This method will construct a new food object
    def __init__(self):
        global canvas

        x = random.randint(0, (GAME_WIDTH / SPACE_SIZE)-1) * SPACE_SIZE   # spawning the food on x-axis
        y = random.randint(0, (GAME_HEIGHT / SPACE_SIZE)-1) * SPACE_SIZE  # spawning the food on y-axis

        self.coordinates = [x, y]  # putting these coordinates in a list to be used as ordered pairs

        # Draw food object in canvas
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")


def next_turn(snake, food):
    global canvas, window, label, direction

    x, y = snake.coordinates[0]  # Head of the snake

    if direction == "up":
        y -= SPACE_SIZE   # Moving 1 space up

    elif direction == "down":
        y += SPACE_SIZE   # Moving 1 space down

    elif direction == "left":
        x -= SPACE_SIZE   # Moving 1 space left

    elif direction == "right":
        x += SPACE_SIZE   # Moving 1 space right

    snake.coordinates.insert(0, (x, y))  # updating the coordinates for the head of the snake

    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)  # new graphic for the head

    snake.squares.insert(0, square)  # updating the list of snake's squares (it's body)

    if x == food.coordinates[0] and y == food.coordinates[1]:  # for making the snake eat the food
        global score
        score += 1

        label.config(text="Score:{}".format(score))  # for changing the score

        canvas.delete("food")  # for deleting the food

        food = Food()  # for making a new food

    else:
        del snake.coordinates[-1]  # deleting the tail of the snake

        canvas.delete(snake.squares[-1])  # Updating canvas

        del snake.squares[-1]  # then deleting for the next move

    if check_collisions(snake):  # checking if the head of the snake collided with anything
        game_over()

    else:
        window.after(SPEED, next_turn, snake, food)  # updating the snake


def change_direction(new_direction):
    global direction  # to accessing the direction
    if new_direction == 'left':  # to prevent it from going in it's reversed direction same goes for the rest
        if direction != 'right':
            direction = new_direction

    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction

    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction

    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction


def check_collisions(snake):

    x, y = snake.coordinates[0]  # unpacking the head of the snake

    if x < 0 or x >= GAME_WIDTH:  # Checking if the snake crossed the width borders of the game
        return True
    elif y < 0 or y >= GAME_HEIGHT:  # Checking if the snake crossed the height borders of the game
        return True

    for body_part in snake.coordinates[1:]:  # for checking if the snake touches it's body
        if x == body_part[0] and y == body_part[1]:

            return True  # collision happened
    return False  # means no collision


def game_over():  # for showing GAME OVER on losing
    global canvas
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
                       font=('consolas', 70), text="GAME OVER", fill="black", tag="gameover")


#############################################################################################################


#                                                (Creating GUI Window)
def snake_GUI():
    def back():
        window.destroy()
        from T_BG import big_GUI
        big_GUI()

    global canvas, window, label, score, direction
    window = Tk()
    score = 0
    direction = 'right'
    window.title("Snake game")
    window.resizable(False, False)  # Method to make Window (non-resizable)

    # Creating a score label

    label = Label(window, text="Score:{}".format(score), font=('consolas', 40))
    label.pack()
    # GameBoard view
    canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
    canvas.pack()

    # Center Window on Screen

    window.update()
    # These 4 Lines are for getting the user Resolution
    window_width = window.winfo_width()   # for getting window width of the game
    window_height = window.winfo_height()   # for getting window height of the game
    screen_width = window.winfo_screenwidth()   # for getting the screen width of the PC
    screen_height = window.winfo_screenheight()  # for getting the screen height of the PC

    # adjust the position of the window

    x = int((screen_width/2) - (window_width/2))
    y = int((screen_height/2) - (window_height/2))

    # Set the Geometry
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Binding some keys to Let User Control Snake:

    window.bind('<Left>', lambda event: change_direction('left'))
    window.bind('<Right>', lambda event: change_direction('right'))
    window.bind('<Up>', lambda event: change_direction('up'))
    window.bind('<Down>', lambda event: change_direction('down'))

    back_button = Button(window, text="← Back", font=('Areal Bold', 13), command=back).place(x=0, y=13)
    start_button = Button(window, text="Start", font=('Areal Bold', 13), command=start).place(x=900, y=13)
    window.mainloop()


def start():  # To start the game a (snake and food) object must be created
    global canvas
    global score
    canvas.delete(ALL)
    score = 0
    snake = Snake()  # calling snake constructor
    food = Food()    # Calling food constructor
    next_turn(snake, food)  # to make the snake move
