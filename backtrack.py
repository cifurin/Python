# The Traintracks puzzle comprises a 8x8 grid of squares where each square may/may not have a track.
# The start and end of the traintrack is provided as well as one or more intermediary tracks.
# The rows and columns of the grid are given numbers that represent the number of squares that have tracks.
# The objective of the puzzle is to build a single and complete path from start to finish that satisfies all row/column track constraints.
#
# A track can be placed in a square in a number of different orientations.
# The track will start in the centre of one of the 4 faces, move to the centre and then exit via the centre of one of the remaining 3 faces.
# The total number of variations are therefore 12 and each possibility can be represented using the 4 faces of each square as LEFT, RIGHT, TOP and BOTTOM (L,R, T and B) as input/output.
# 1(T-R),2(T-B),3(T-L),4(R-B),5(R-L),6(R-T),7(B-L),8(B-T),9(B-R),10(L-T),11(L-R),12(L-B) where the 1st face is the input and the second face is the output.
# The start and end squares will contain a track where the start/finish is on the outside of the grid.
#
# Puzzle is defined as a list of squares (row,col) and the track type (1-12)
# E.g. (3,1,4)
#
# Default state of board: matrix/grid defining possible track types for each location independent of given puzzle
# The initial state = default state + puzzle
# (4,9),(4,5,7,9,11,12),(4,5,7,9,11,12),(4,5,7,9,11,12),(4,5,7,9,11,12),(4,5,7,9,11,12),(4,5,7,9,11,12),(7,12)
# (1,2,4,6,8,9),....,(2,3,7,8,10,12)
# ..
# (1,6),(1,3,5,6,10,11),(1,3,5,6,10,11),(1,3,5,6,10,11),(1,3,5,6,10,11),(1,3,5,6,10,11),(1,3,5,6,10,11),(3,10)


import pygame
import pygame_gui
import csv
import tkinter.filedialog
from random import randrange
from functools import reduce

# Initializing Pygame
pygame.init()
clock = pygame.time.Clock()

# Initializing surface
surface = pygame.display.set_mode((800, 800))

manager = pygame_gui.UIManager((800, 600))

hello_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((100, 100), (100, 50)), text="Say Hello", manager=manager
)

# Initializing Color
color = (255, 0, 0)

puzzle = []

RowTracks = [0] * 8
colTracks = [0] * 8

# grid = [[0 for column in range(8)] for row in range(8)]

# puzzle = [3, 0, 10], [2, 5, 5], [2, 6, 10], [1, 6, 2], [7, 3, 2]

# puzzle = [3, 0, 11], [2, 2, 12], [1, 6, 10], [7, 3, 8]

# puzzle = [6, 0, 3, 10], [2, 2, 1, 6], [7, 4, 2, 8], [4, 6, 11, 5]
# puzzle = [6, 0, [10]], [2, 2, [1, 6]], [7, 4, [8]], [4, 6, [11, 5]]

# puzzle = [0, 0, [11]], [3, 2, [1, 6]], [3, 5, [7, 12]], [7, 6, [8]]

# puzzle = [7, 0, [10]], [2, 4, [2, 8]], [6, 5, [5, 11]], [7, 7, [8]]

# puzzle = [6, 0, [12]], [4, 4, [2, 8]], [4, 6, [1, 6]], [7, 7, [8]]

# puzzle = [2, 0, [10]], [7, 7, [8]]

# puzzle = [1, 0, [11]], [7, 0, [8]], [5, 3, [7, 12]], [7, 7, [3, 10]]

# RowTracks = [2, 4, 8, 4, 4, 2, 1, 1]
# colTracks = [2, 1, 1, 5, 4, 3, 5, 5]

# RowTracks = [8, 7, 3, 6, 4, 2, 1, 1]
# colTracks = [3, 4, 6, 6, 2, 4, 3, 4]

# RowTracks = [4, 5, 6, 6, 7, 4, 3, 1]
# colTracks = [3, 1, 5, 3, 7, 7, 5, 5]

# RowTracks = [4, 3, 4, 4, 4, 4, 2, 1]
# colTracks = [1, 1, 3, 4, 5, 5, 4, 3]

# RowTracks = [3, 3, 3, 3, 3, 3, 8, 8]
# colTracks = [2, 2, 2, 2, 7, 8, 7, 4]

# RowTracks = [2, 4, 3, 4, 3, 3, 5, 5]
# colTracks = [2, 2, 2, 3, 6, 4, 3, 7]

# RowTracks = [4, 4, 2, 1, 3, 5, 5, 3]
# colTracks = [2, 2, 4, 8, 3, 2, 2, 4]

# RowTracks = [3, 4, 1, 2, 7, 6, 7, 3]
# colTracks = [3, 5, 7, 5, 3, 2, 4, 4]

rt = [0, 0, 0, 0, 0, 0, 0, 0]
ct = [0, 0, 0, 0, 0, 0, 0, 0]

prt = [0, 0, 0, 0, 0, 0, 0, 0]
pct = [0, 0, 0, 0, 0, 0, 0, 0]

paused = False

defaultState = (
    [
        [4, 9],
        [4, 5, 7, 9, 11, 12],
        [4, 5, 7, 9, 11, 12],
        [4, 5, 7, 9, 11, 12],
        [4, 5, 7, 9, 11, 12],
        [4, 5, 7, 9, 11, 12],
        [4, 5, 7, 9, 11, 12],
        [7, 12],
    ],
    [
        [1, 2, 4, 6, 8, 9],
        [i for i in range(1, 12 + 1)],
        [i for i in range(1, 12 + 1)],
        [i for i in range(1, 12 + 1)],
        [i for i in range(1, 12 + 1)],
        [i for i in range(1, 12 + 1)],
        [i for i in range(1, 12 + 1)],
        [2, 3, 7, 8, 10, 12],
    ],
    [
        [1, 2, 4, 6, 8, 9],
        [i for i in range(1, 12 + 1)],
        [i for i in range(1, 12 + 1)],
        [i for i in range(1, 12 + 1)],
        [i for i in range(1, 12 + 1)],
        [i for i in range(1, 12 + 1)],
        [i for i in range(1, 12 + 1)],
        [2, 3, 7, 8, 10, 12],
    ],
    [
        [1, 2, 4, 6, 8, 9],
        [i for i in range(1, 12 + 1)],
        [i for i in range(1, 12 + 1)],
        [i for i in range(1, 12 + 1)],
        [i for i in range(1, 12 + 1)],
        [i for i in range(1, 12 + 1)],
        [i for i in range(1, 12 + 1)],
        [2, 3, 7, 8, 10, 12],
    ],
    [
        [1, 2, 4, 6, 8, 9],
        [i for i in range(1, 12 + 1)],
        [i for i in range(1, 12 + 1)],
        [i for i in range(1, 12 + 1)],
        [i for i in range(1, 12 + 1)],
        [i for i in range(1, 12 + 1)],
        [i for i in range(1, 12 + 1)],
        [2, 3, 7, 8, 10, 12],
    ],
    [
        [1, 2, 4, 6, 8, 9],
        [i for i in range(1, 12 + 1)],
        [i for i in range(1, 12 + 1)],
        [i for i in range(1, 12 + 1)],
        [i for i in range(1, 12 + 1)],
        [i for i in range(1, 12 + 1)],
        [i for i in range(1, 12 + 1)],
        [2, 3, 7, 8, 10, 12],
    ],
    [
        [1, 2, 4, 6, 8, 9],
        [i for i in range(1, 12 + 1)],
        [i for i in range(1, 12 + 1)],
        [i for i in range(1, 12 + 1)],
        [i for i in range(1, 12 + 1)],
        [i for i in range(1, 12 + 1)],
        [i for i in range(1, 12 + 1)],
        [2, 3, 7, 8, 10, 12],
    ],
    [
        [1, 6],
        [1, 3, 5, 6, 10, 11],
        [1, 3, 5, 6, 10, 11],
        [1, 3, 5, 6, 10, 11],
        [1, 3, 5, 6, 10, 11],
        [1, 3, 5, 6, 10, 11],
        [1, 3, 5, 6, 10, 11],
        [3, 10],
    ],
)


def ImportPuzzle(csv_file):
    with open(csv_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for r, row in enumerate(csv_reader):
            if r == 0:
                for index, item in enumerate(row):
                    RowTracks[index] = int(item)
            if r == 1:
                for index, item in enumerate(row):
                    colTracks[index] = int(item)
            if r > 1:
                a = [int(item) for index, item in enumerate(row) if index < 2]
                b = [int(item) for index, item in enumerate(row) if index > 1]
                a.append(b)
                puzzle.append(a)


class Square:
    # Design
    # A class that represents a square
    # Location (x,y) of the square in the Grid
    # Initial State: This allows the puzzle board to be reset
    # (a) list of the possible track options for the specific square
    # (b) if the track is given then there will only be one
    #
    # Current state:
    #
    def __init__(self, x, y, s):
        self.x = x
        self.y = y
        self.state = defaultState[x][y]
        self.solution = s
        self.solved = False
        self.hasTrack = False
        self.saved_state = []

    def checkIfSolved(self):
        if not self.solved and not self.hasTrack and len(self.state) == 0:
            print("length = 0 solved")
            self.solved = True
        if not self.solved and self.hasTrack:
            if len(self.state) == 1:
                print("length = 1 solved")
                self.solved = True
            if len(self.state) == 2:
                print("length = 2 solved")
                # check if the options are the same but reversed
                # 1,6 2,8 3,10 4,9 5,11 7,7,12
                for s in [[1, 6], [2, 8], [3, 10], [4, 9], [5, 11], [7, 12]]:
                    # print(s)
                    if set(self.state) == set(s):
                        self.solved = True

    def set_solution(self, option):
        self.solution = option

    def remove_options(self, option):
        self.state = [x for x in self.state if x == option]

    def save_state(self):
        self.saved_state = [x for x in self.state]

    def restore_state(self):
        self.state = self.saved_state

    def removeTrack(self, track):
        self.state.remove(track)
        self.checkIfSolved()

    def containsR(self):
        # determine if the tracklist contains any tracks that touch the RIGHT face
        # these are the track types that touch face R
        rightFace = [1, 4, 5, 6, 9, 11]
        return any(item in rightFace for item in self.state)

    def containsL(self):
        # determine if the tracklist contains any tracks that touch the LEFT face
        # these are the track types that touch face L
        leftFace = [3, 5, 7, 10, 11, 12]
        return any(item in leftFace for item in self.state)

    def containsB(self):
        # these are the track types that touch face B
        bottomFace = [2, 4, 7, 8, 9, 12]
        return any(item in bottomFace for item in self.state)

    def containsT(self):
        # these are the track types that touch face T
        topFace = [1, 2, 3, 6, 8, 10]
        return any(item in topFace for item in self.state)

    def leaveL(self):
        # remove all tracks EXCEPT left face
        self.state = list(set(self.state) - {1, 2, 4, 6, 8, 9})

    def removeL(self):
        # remove all LEFT face tracks
        self.state = list(set(self.state) - {3, 5, 7, 10, 11, 12})
        # self.checkIfSolved()

    def leaveR(self):
        # remove all tracks EXCEPT right face
        self.state = list(set(self.state) - {2, 3, 7, 8, 10, 12})

    def removeR(self):
        # remove all right face tracks
        self.state = list(set(self.state) - {1, 4, 5, 6, 9, 11})
        # self.checkIfSolved()

    def removeB(self):
        # remove all bottom face tracks
        self.state = list(set(self.state) - {2, 4, 7, 8, 9, 12})
        # self.checkIfSolved()

    def leaveB(self):
        # remove all tracks EXCEPT bottom face
        self.state = list(set(self.state) - {1, 3, 5, 6, 10, 11})

    def removeT(self):
        # remove all the top face tracks
        self.state = list(set(self.state) - {1, 2, 3, 6, 8, 10})
        # self.checkIfSolved()

    def leaveT(self):
        # remove all tracks EXCEPT top face
        self.state = list(set(self.state) - {4, 5, 7, 9, 11, 12})


def updateColHastracks():
    # calculate the current number of squares that a track passes through in each column
    for col in range(0, 8):
        sum = 0
        for row in range(0, 8):
            index = row * 8 + col
            if squares[index].hasTrack:
                sum = sum + 1
        ct[col] = sum


def updateRowHastracks():
    # calculate the current number of squares that a track passes through in each row
    for row in range(0, 8):
        sum = 0
        for col in range(0, 8):
            index = row * 8 + col
            if squares[index].hasTrack:
                sum = sum + 1
        rt[row] = sum

    [
        rt[row]
        for row in range(0, 8)
        for col in range(0, 8)
        if squares[row * 8 + col].hasTrack
    ]


def checkForSolved():
    for square in squares:
        # print(square.x, square.y, square.state, square.solved, square.hasTrack)
        square.checkIfSolved()


def drawBoard():
    width = 60
    height = 60
    for row in range(8):
        for col in range(8):
            color = (255, 0, 0)
            # color = (0, 0, 255)
            pygame.draw.rect(
                surface,
                color,
                pygame.Rect(160 + col * 60, 160 + row * 60, width, height),
                0,
            )


def drawtrack(row, col, trackType):
    # 1(T-R),2(T-B),3(T-L),4(R-B),5(R-L),6(R-T),7(B-L),8(B-T),9(B-R),10(L-T),11(L-R),12(L-B)

    x = 160 + col * 60
    y = 160 + row * 60

    ct = (x + 30, y)
    cr = (x + 60, y + 30)
    cb = (x + 30, y + 60)
    cl = (x, y + 30)
    c = (x + 30, y + 30)

    match trackType:
        case 0:
            return
        case 1 | 6:
            start = ct
            end = cr
        case 2 | 8:
            start = ct
            end = cb
        case 3 | 10:
            start = ct
            end = cl
        case 4 | 9:
            start = cr
            end = cb
        case 5 | 11:
            start = cr
            end = cl
        case 7 | 12:
            start = cl
            end = cb

    pygame.draw.line(surface, pygame.Color("yellow"), start, c, 1)
    pygame.draw.line(surface, pygame.Color("yellow"), c, end, 1)


squares = []

for row in range(8):
    for col in range(8):
        # print(row, col)
        squares.append(Square(row, col, 0))

# read in puzzle from file
# csv_file = tkinter.filedialog.askopenfilename()

csv_file = "C:/Users/NCSISS/Python/traintrack_puzzles/puzzle1.txt"

print(csv_file)

ImportPuzzle(csv_file)

print(puzzle)
print(RowTracks)
print(colTracks)

for item in puzzle:
    index = item[0] * 8 + item[1]
    squares[index].state = item[2]
    squares[index].solved = True
    # squares[index].hasTrack = True

squares[24].hasTrack = True
# squares[59].hasTrack = True

path = []


def constraintsSatisfied(i, track):
    # check if move to new square doesn't violate the row and column constraints

    updateColHastracks()
    updateRowHastracks()

    match track:
        # MOVE RIGHT
        case 1 | 9 | 11:
            row = squares[i].x
            col = squares[i].y + 1
            if rt[row] < RowTracks[row] and ct[col] < colTracks[col]:
                return True
        # MOVE LEFT
        case 3 | 5 | 7:
            row = squares[i].x
            col = squares[i].y - 1
            if rt[row] < RowTracks[row] and ct[col] < colTracks[col]:
                return True

        # MOVE UP
        case 6 | 8 | 10:
            row = squares[i].x - 1
            col = squares[i].y
            if rt[row] < RowTracks[row] and ct[col] < colTracks[col]:
                return True

        # MOVE DOWN
        case 2 | 4 | 12:
            row = squares[i].x + 1
            col = squares[i].y
            if rt[row] < RowTracks[row] and ct[col] < colTracks[col]:
                return True


def findGroups(index, count):
    count = count - 1
    # print(index, squares[index].solution, count)
    # path.append((index, squares[index].solution))

    if index == 59 and squares[21].solution > 0 or count == 0:
        squares[59].solution = squares[59].state[0]
        path.append((59, 2))
        # print(index, squares[index].state, count)
        print("teminating")
        return True

    # do we need to check that we havn't already included this square in solution?
    for trackType in squares[index].state:
        print(index, trackType, count)
        path.append((index, trackType))
        squares[index].solution = trackType
        match trackType:
            # MOVE RIGHT
            case 1 | 9 | 11:
                # check if valid
                if (
                    squares[index + 1].containsL()
                    and not squares[index + 1].solution
                    and constraintsSatisfied(index, trackType)
                ):
                    # save the other options in case we need to backtrack
                    squares[index + 1].save_state()
                    # set state to this option
                    squares[index + 1].leaveL()

                    # set the hasTrack state to True for drawing purposes, IS THIS NEEDED??
                    squares[index + 1].hasTrack = True

                    # squares[index].solution = trackType

                    if findGroups(index + 1, count):
                        return True

                    # need to backtrack
                    print("backtracking")
                    print(index, trackType, count)
                    path.append((index, trackType))
                    squares[index + 1].restore_state()
                    squares[index + 1].hasTrack = False

            # MOVE LEFT
            case 3 | 5 | 7:
                if (
                    squares[index - 1].containsR()
                    and not squares[index - 1].solution
                    and constraintsSatisfied(index, trackType)
                ):
                    squares[index - 1].save_state()
                    squares[index - 1].leaveR()
                    squares[index - 1].hasTrack = True
                    # squares[index - 1].solution = trackType
                    if findGroups(index - 1, count):
                        return True
                    print("backtracking")
                    print(index, trackType, count)
                    path.append((index, trackType))
                    squares[index - 1].restore_state()
                    squares[index - 1].hasTrack = False

            # MOVE UP
            case 6 | 8 | 10:
                if (
                    squares[index - 8].containsB()
                    and not squares[index - 8].solution
                    and constraintsSatisfied(index, trackType)
                ):
                    squares[index - 8].save_state()
                    squares[index - 8].leaveB()
                    squares[index - 8].hasTrack = True
                    # squares[index - 8].solution = trackType
                    if findGroups(index - 8, count):
                        return True
                    print("backtracking")
                    print(index, trackType, count)
                    path.append((index, trackType))
                    squares[index - 8].restore_state()
                    squares[index - 8].hasTrack = False
            # MOVE DOWN
            case 2 | 4 | 12:
                if (
                    squares[index + 8].containsT()
                    and not squares[index + 8].solution
                    and constraintsSatisfied(index, trackType)
                ):
                    squares[index + 8].save_state()
                    # squares[index + 8].remove_options(trackType)
                    squares[index + 8].leaveT()
                    squares[index + 8].hasTrack = True
                    # squares[index + 8].solution = trackType
                    if findGroups(index + 8, count):
                        return True
                    print("backtracking")
                    print(index, trackType, count)
                    path.append((index, trackType))
                    squares[index + 8].restore_state()
                    squares[index + 8].hasTrack = False

        squares[index].solution = 0

    return False


findGroups(24, 100)

print(path)

n = 1
b = 0

while True:
    # iterate over the list of Event objects
    # that was returned by pygame.event.get() method.

    clock.tick(60)
    time_delta = clock.tick(30) / 1000.0

    surface.fill((0, 0, 0))

    drawBoard()

    # check if backtracking
    if n > 0 and path[n] in path[: n - 1]:
        b = n - path.index(path[n])

    for sol in path[: n + 1]:

        row, col = squares[sol[0]].x, squares[sol[0]].y

        pygame.draw.rect(
            surface,
            color,
            pygame.Rect(160 + col * 60, 160 + row * 60, 60, 60),
            0,
        )

        drawtrack(row, col, sol[1])

    if n < len(path) - 1:
        if b == 0:
            n = n + 1
        else:
            n = n - 1
            b = b - 1
            path.remove(path[n])

    for event in pygame.event.get():
        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        if event.type == pygame.QUIT:
            # deactivates the pygame library
            pygame.quit()

            # quit the program.
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                pass
            elif event.key == pygame.K_LEFT:
                pass
            elif event.key == pygame.K_UP:
                pass
            elif event.key == pygame.K_p:
                paused = not paused

        manager.process_events(event)

    manager.update(time_delta)

    manager.draw_ui(surface)

    pygame.display.update()

    # check that only Group 1 is present i.e. nothing greater than 1 and hence list will be empty
    # if not [x for x in g if x > 1]:
    #     print(" Puzzle Solved")
