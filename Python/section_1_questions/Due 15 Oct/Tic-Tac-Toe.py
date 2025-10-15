# Tic-Tac-Toe
# by David Kosbie

# This implements a basic game of TicTacToe.

# This version does not save or load the game (that is left for you to do!)

from cmu_graphics import *
import math
import json

def saveGame(app):
    game_data = {
        'board': app.board,
        'turn': app.turn,
        'message': app.message,
        'turnCount': app.turnCount,
        'gameOver': app.gameOver,
        'winningCells': app.winningCells
    }
    with open('tic_tac_toe_save.json', 'w') as f:
        json.dump(game_data, f)
    print('Game saved!')

def loadGame(app):
    try:
        with open('tic_tac_toe_save.json', 'r') as f:
            game_data = json.load(f)
        app.board = game_data['board']
        app.turn = game_data['turn']
        app.message = game_data['message']
        app.turnCount = game_data['turnCount']
        app.gameOver = game_data['gameOver']
        app.winningCells = game_data['winningCells']
        print('Game loaded!')
    except FileNotFoundError:
        print('No saved game found.')
    except Exception as e:
        print(f'Error loading game: {e}')


def onAppStart(app):
    # Set the model values (in the app object) that never change.
    app.rows = 3
    app.cols = 3
    app.boardBounds = (50, 75, 350, 375) # left, top, right, bottom
    app.cellBorderWidth = 2
    resetApp(app)

def resetApp(app):
    app.selection = None
    app.board = [[None]*app.cols for row in range(app.rows)]
    app.turn = 'X'
    app.message = "X's turn"
    app.turnCount = 0
    app.gameOver = False
    app.winningCells = None

def onKeyPress(app, key):
    if key == 's':
        saveGame(app)
    elif key == 'l':
        loadGame(app)
    elif (app.gameOver) and (key == 'r'):
        resetApp(app)

def onMousePress(app, mouseX, mouseY):
    # Always clear the selection on any mouse press.
    app.selection = None
    # Then, make the move, but only if the game is not over, and the move is legal
    # (that is, it's in an empty cell).
    if not app.gameOver:
        cell = getCell(app, mouseX, mouseY)
        if cell != None:
            row, col = cell
            if app.board[row][col] == None:
                makeMove(app, row, col)

def onMouseMove(app, mouseX, mouseY):
    if app.gameOver:
        return
    # Set the cell selection as the mouse is moved, but only
    # if there is a selected cell, and that cell on the board is empty.
    # Otherwise, clear the cell selection.
    selectedCell = getCell(app, mouseX, mouseY)
    if selectedCell == None:
        app.selection = None
    else:
        row, col = selectedCell
        if app.board[row][col] == None:
            app.selection = selectedCell
        else:
            app.selection = None

def makeMove(app, row, col):
    # We already know that this is a legal move, so set the board
    # to the current player, add one to the turn count, check if the
    # game is over, and if not, change turns.
    app.board[row][col] = app.turn
    app.turnCount += 1
    checkForGameOver(app)
    if not app.gameOver:
        changeTurns(app)

def checkForGameOver(app):
    # Check if the game is over (tie or win), and if so, set app.gameOver to
    # True and set the app.message as appropriate.
    # First check for a tie game.  If it is, set 
    if app.turnCount == app.rows * app.cols:
        app.gameOver = True
        app.message = 'Tie game!'
    # It's not a tie game, so check if there are 3 in a row on the board,
    # in a search that is similar to wordSearch:
    else:
        directions = [ (0, 1), # right
                       (1, 0), # down
                       (1, 1), # right-down diagonal
                       (1, -1) # right-up diagonal
                     ]
        for startRow in range(app.rows):
            for startCol in range(app.cols):
                for drow,dcol in directions:
                    winner = checkForWin(app, startRow, startCol, drow, dcol)
                    if winner != None:
                        app.gameOver = True
                        app.message = f'{winner} wins!'
                        return

def checkForWin(app, startRow, startCol, drow, dcol):
    # Check for a winner (3 in a row) starting from (startRow, startCol) and
    # heading in the direction (drow, dcol).  Return the winner if there
    # is one, otherwise None.  Also, so that we can draw the line through
    # the winning 3-in-a-row run, store the winning cells in the order
    # they appear in app.winningCells.
    player = app.board[startRow][startCol]
    if player == None:
        return None
    winLength = 3
    winningCells = [ ]
    for i in range(winLength):
        row = startRow + i * drow
        col = startCol + i * dcol
        if ((row < 0) or (row >= app.rows) or
            (col < 0) or (col >= app.cols)):
            # we went off the board
            return None
        if app.board[row][col] != player:
            return None
        winningCells.append((row, col))
    app.winningCells = winningCells
    return player

def changeTurns(app):
    # Change the turn from 'X' to 'O' or 'O' to 'X',
    # and set the app.message as appropriate.
    app.turn = 'O' if (app.turn == 'X') else 'X'
    app.message = f"{app.turn}'s turn"

def redrawAll(app):
    drawLabel('Tic-Tac-Toe', 200, 20, size=16, bold=True)
    drawLabel('Press s to save game, l to load game', 200, 40, size=14)
    drawAppMessage(app)
    drawBoard(app)
    drawWinningLine(app)

def drawAppMessage(app):
    # Draw the app.message, and if the game is over, make the message red
    # and add a note to press r to restart.
    if app.gameOver:
        message = app.message + ' (press r to restart)'
        color = 'red'
    else:
        message = app.message
        color = 'black'
    drawLabel(message, 200, 60, size=14, fill=color)

def drawBoard(app):
    # first draw each cell (with single-thickness):
    for row in range(app.rows):
        for col in range(app.cols):
            drawCell(app, row, col)
    # then draw the board outline (with double-thickness):
    x0, y0, x1, y1 = app.boardBounds
    drawRect(x0, y0, x1-x0, y1-y0,
             fill=None, border='black',
             borderWidth=2*app.cellBorderWidth)

def drawCell(app, row, col):
    x0, y0, x1, y1 = getCellBounds(app, row, col)
    color = 'cyan' if (row, col) == app.selection else None
    drawRect(x0, y0, x1-x0, y1-y0,
             fill=color, border='black', borderWidth=app.cellBorderWidth)
    label = app.board[row][col]
    if label != None:
        cx = x0 + (x1 - x0)/2
        cy = y0 + (y1 - y0)/2
        drawLabel(label, cx, cy, size=24, bold=True)

def drawWinningLine(app):
    # If there is a winner, then app.winningCells will contain the
    # cells in order, so draw a line from the center of the first cell
    # to the center of the last cell.
    if app.winningCells != None:
        cx0, cy0 = getCellCenter(app, app.winningCells[0])
        cx1, cy1 = getCellCenter(app, app.winningCells[-1])
        drawLine(cx0, cy0, cx1, cy1)

def getCellCenter(app, cell):
    # Return the center of the given cell, a (row, col) tuple.
    row, col = cell
    x0, y0, x1, y1 = getCellBounds(app, row, col)
    cx = (x0 + x1) / 2
    cy = (y0 + y1) / 2
    return cx, cy

def getCellBounds(app, row, col):
    boardX0, boardY0, boardX1, boardY1 = app.boardBounds
    cellWidth, cellHeight = getCellSize(app)
    x0 = boardX0 + col * cellWidth
    y0 = boardY0 + row * cellHeight
    x1 = x0 + cellWidth
    y1 = y0 + cellHeight
    return (x0, y0, x1, y1)

def getCellSize(app):
    boardX0, boardY0, boardX1, boardY1 = app.boardBounds
    boardWidth = boardX1 - boardX0
    boardHeight = boardY1 - boardY0
    cellWidth = boardWidth / app.cols
    cellHeight = boardHeight / app.rows
    return (cellWidth, cellHeight)

def getCell(app, x, y):
    boardX0, boardY0, boardX1, boardY1 = app.boardBounds
    dx = x - boardX0
    dy = y - boardY0
    cellWidth, cellHeight = getCellSize(app)
    row = math.floor(dy / cellHeight)
    col = math.floor(dx / cellWidth)
    if (0 <= row < app.rows) and (0 <= col < app.cols):
        return (row, col)
    else:
        return None

def main():
    runApp()

main()