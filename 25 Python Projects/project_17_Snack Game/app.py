import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox

# Cube class represents a single part of the snake
class cube(object):
    rows = 20  # Number of rows in the grid
    w = 500  # Width of the game window

    def __init__(self, start, dirnx=1, dirny=0, color=(255, 0, 0)):
        self.pos = start  # Initial position of the cube
        self.dirnx = 1  # Initial movement in x direction
        self.dirny = 0  # Initial movement in y direction
        self.color = color  # Color of the cube

    # Moves the cube in a given direction
    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)

    # Draws the cube on the game screen
    def draw(self, surface, eyes=False):
        dis = self.w // self.rows  # Size of each cube
        i = self.pos[0]  # X position
        j = self.pos[1]  # Y position

        # Draw the cube (snake segment)
        pygame.draw.rect(surface, self.color, (i * dis + 1, j * dis + 1, dis - 2, dis - 2))

        # Draw eyes for the head of the snake
        if eyes:
            centre = dis // 2
            radius = 3
            circleMiddle = (i * dis + centre - radius, j * dis + 8)
            circleMiddle2 = (i * dis + dis - radius * 2, j * dis + 8)
            pygame.draw.circle(surface, (0, 0, 0), circleMiddle, radius)
            pygame.draw.circle(surface, (0, 0, 0), circleMiddle2, radius)

# Snake class controls the movement and body of the snake
class snake(object):
    body = []  # Stores all the cubes of the snake
    turns = {}  # Dictionary to store turning points

    def __init__(self, color, pos):
        self.color = color
        self.head = cube(pos)  # Head of the snake
        self.body.append(self.head)  # Add head to the body list
        self.dirnx = 0  # Initial direction x
        self.dirny = 1  # Initial direction y

    # Handles the movement of the snake
    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # Quit the game if user closes the window

            keys = pygame.key.get_pressed()  # Get pressed keys

            for key in keys:
                if keys[pygame.K_LEFT]:  # Move left
                    self.dirnx = -1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_RIGHT]:  # Move right
                    self.dirnx = 1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_UP]:  # Move up
                    self.dirnx = 0
                    self.dirny = -1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_DOWN]:  # Move down
                    self.dirnx = 0
                    self.dirny = 1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

        # Move each cube in the snake's body
        for i, c in enumerate(self.body):
            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0], turn[1])
                if i == len(self.body) - 1:
                    self.turns.pop(p)  # Remove turn after last cube moves
            else:
                # Handle when the snake moves off the screen (wrap-around effect)
                if c.dirnx == -1 and c.pos[0] <= 0: c.pos = (c.rows - 1, c.pos[1])
                elif c.dirnx == 1 and c.pos[0] >= c.rows - 1: c.pos = (0, c.pos[1])
                elif c.dirny == 1 and c.pos[1] >= c.rows - 1: c.pos = (c.pos[0], 0)
                elif c.dirny == -1 and c.pos[1] <= 0: c.pos = (c.pos[0], c.rows - 1)
                else:
                    c.move(c.dirnx, c.dirny)

    # Resets the snake after losing
    def reset(self, pos):
        self.head = cube(pos)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.dirnx = 0
        self.dirny = 1

    # Adds a new cube when the snake eats food
    def addCube(self):
        tail = self.body[-1]  # Get the last cube
        dx, dy = tail.dirnx, tail.dirny

        # Add new cube at the correct position based on direction
        if dx == 1 and dy == 0:
            self.body.append(cube((tail.pos[0] - 1, tail.pos[1])))
        elif dx == -1 and dy == 0:
            self.body.append(cube((tail.pos[0] + 1, tail.pos[1])))
        elif dx == 0 and dy == 1:
            self.body.append(cube((tail.pos[0], tail.pos[1] - 1)))
        elif dx == 0 and dy == -1:
            self.body.append(cube((tail.pos[0], tail.pos[1] + 1)))

        self.body[-1].dirnx = dx
        self.body[-1].dirny = dy

    # Draws the snake on the screen
    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i == 0:
                c.draw(surface, True)  # Head of the snake with eyes
            else:
                c.draw(surface)

# Draws grid lines on the screen
def drawGrid(w, rows, surface):
    sizeBtwn = w // rows  # Size of each grid cell

    x = 0
    y = 0
    for l in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn

        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, w))
        pygame.draw.line(surface, (255, 255, 255), (0, y), (w, y))

# Updates the game window
def redrawWindow(surface):
    global rows, width, s, snack
    surface.fill((0, 0, 0))  # Fill background with black
    s.draw(surface)  # Draw the snake
    snack.draw(surface)  # Draw the food
    drawGrid(width, rows, surface)  # Draw grid
    pygame.display.update()

# Generates a random position for the snack
def randomSnack(rows, item):
    positions = item.body

    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)
        if len(list(filter(lambda z: z.pos == (x, y), positions))) > 0:
            continue
        else:
            break

    return (x, y)

# Displays a message box when the game is over
def message_box(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass

# Main game loop
def main():
    global width, rows, s, snack
    width = 500
    rows = 20
    win = pygame.display.set_mode((width, width))
    s = snake((255, 0, 0), (10, 10))
    snack = cube(randomSnack(rows, s), color=(0, 255, 0))
    flag = True

    clock = pygame.time.Clock()

    while flag:
        pygame.time.delay(50)
        clock.tick(10)
        s.move()
        
        if s.body[0].pos == snack.pos:
            s.addCube()
            snack = cube(randomSnack(rows, s), color=(0, 255, 0))

        # Check if snake collides with itself
        for x in range(len(s.body)):
            if s.body[x].pos in list(map(lambda z: z.pos, s.body[x + 1:])):
                print("Score: ", len(s.body))
                message_box("You Lost!", "Play again...")
                s.reset((10, 10))
                break

        redrawWindow(win)

main()
