# Case Study #3: Dots App

# This code will not run in Google Colab.
# Instead, see the replit repl we provided.

# Level 1 (Core)
# Watch the accompanying video carefully. Then write the
# Dots app so it matches that video.

# Level 2+ (Not Core)
# For an additional challenge beyond Level 1 / Core,
# for Level 2 (Not Core), the accompanying video
# only shows the desired behavior.  It does not
# derive the solution for this level.  Edit the
# Dots app so it matches the Level 2+ video.

# Good luck!

from cmu_graphics import *
import random

def onAppStart(app):
    app.board = Board(50, 120, 300, 250)
    app.modes = [ Mode('Standard Blue Dot', 'blue', Dot),
                  Mode('Big Slow Red Dot', 'red', BigSlowRedDot),
                ]
    app.modeIndex = 0

def onStep(app):
    app.board.moveDots()

def redrawAll(app):
    drawLabel('Dot Classes App', app.width/2, 20, size=16, bold=True)
    drawLabel('Click to place a new dot', app.width/2, 40, size=14)
    drawLabel('Press m to change dot mode', app.width/2, 60, size=14)
    drawLabel('Press c to clear all dots', app.width/2, 80, size=14)
    mode = app.modes[app.modeIndex]
    drawLabel(f'Current mode: {mode.name}', app.width/2,
              100, size=14, fill=mode.color)
    app.board.draw(app)

def onKeyPress(app, key):
    if key == 'm':
        app.modeIndex = (app.modeIndex + 1) % len(app.modes)
    elif key == 'c':
        app.board.clearDots()

def onMousePress(app, mouseX, mouseY):
    if app.board.contains(mouseX, mouseY):
       mode = app.modes[app.modeIndex]
       dot = mode.ModeClass(mouseX, mouseY, app.board)

class Dot: 
    def __init__(self, x, y, board):
        self.x = x
        self.y = y
        self.r = 5
        self.color = "blue"
        self.board = board
        #set dx and dy
        while True:
            self.dx = random.randrange(-3, 3)
            self.dy = random.randrange(-3, 3)
            if (self.dx != 0) or (self.dy != 0):
                break
        board.dots.append(self)
    
    def move(self):
        self.x += self.dx
        self.y += self.dy

        xmin = self.board.left + self.r
        ymin = self.board.top + self.r
        xmax = self.board.left + self.board.width - self.r
        ymax = self.board.top + self.board.height - self.r

        if self.x < xmin:
            self.x = xmin
            self.dx = -self.dx
        if self.y < ymin:
            self.y = ymin
            self.dy = -self.dy
        if self.x > xmax:
            self.x = xmax
            self.dx = -self.dx
        if self.y > ymax:
            self.y = ymax
            self.dy = -self.dy


    def draw(self, app):
        drawCircle(self.x, self.y, self.r, fill=self.color)

class BigSlowRedDot(Dot):
    def __init__(self, x, y, board):
        super().__init__(x, y, board)
        self.r = 20
        self.color = "red"

class Mode:
    def __init__(self, name, color, ModeClass):
        self.name = name
        self.color = color
        self.ModeClass = ModeClass

class Board:
    def __init__(self, left, top, width, height):
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.dots = [ ]

    def clearDots(self):
        self.dots.clear()

    def moveDots(self):
        for dot in self.dots:
            dot.move()

    def contains(self, x, y):
        return ((self.left <= x <= self.left + self.width) and
                (self.top <= y <= self.top + self.height))
    
    def draw(self, app):
        drawRect(self.left, self.top, self.width, self.height,
                 fill=None, border='black', borderWidth=4)
        for dot in self.dots:
            dot.draw(app)

def main():
    runApp()

main()