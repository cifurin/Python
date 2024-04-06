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
from random import randrange

# Initializing Pygame
pygame.init()
clock = pygame.time.Clock()

# Initializing surface
surface = pygame.display.set_mode((800, 800))

# Initializing Color
color = (255, 0, 0)

# grid = [[0 for column in range(8)] for row in range(8)]

# puzzle = [3, 0, 10], [2, 5, 5], [2, 6, 10], [1, 6, 2], [7, 3, 2]

# puzzle = [3, 0, 11], [2, 2, 12], [1, 6, 10], [7, 3, 8]

# puzzle = [6, 0, 3, 10], [2, 2, 1, 6], [7, 4, 2, 8], [4, 6, 11, 5]
# puzzle = [6, 0, [10]], [2, 2, [1, 6]], [7, 4, [8]], [4, 6, [11, 5]]

# puzzle = [0, 0, [11]], [3, 2, [1, 6]], [3, 5, [7, 12]], [7, 6, [8]]

# puzzle = [7, 0, [10]], [2, 4, [2, 8]], [6, 5, [5, 11]], [7, 7, [8]]

# puzzle = [6, 0, [12]], [4, 4, [2, 8]], [4, 6, [1, 6]], [7, 7, [8]]

# puzzle = [2, 0, [10]], [7, 7, [8]]

puzzle = [1, 0, [11]], [7, 0, [8]], [5, 3, [7, 12]], [7, 7, [3, 10]]

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

RowTracks = [3, 4, 1, 2, 7, 6, 7, 3]
colTracks = [3, 5, 7, 5, 3, 2, 4, 4]

rt = [0, 0, 0, 0, 0, 0, 0, 0]
ct = [0, 0, 0, 0, 0, 0, 0, 0]

prt = [0, 0, 0, 0, 0, 0, 0, 0]
pct = [0, 0, 0, 0, 0, 0, 0, 0]

g = [0] * 64

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
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.initialState = defaultState[x][y]
        self.solved = False
        self.hasTrack = False

    def removeB(self):
        pass


def containsR(trackList):
    # determine if the tracklist contains any tracks that touch the RIGHT face
    # these are the track types that touch face R
    rightFace = [1, 4, 5, 6, 9, 11]
    return any(item in rightFace for item in trackList)


def containsL(trackList):
    # determine if the tracklist contains any tracks that touch the LEFT face
    # these are the track types that touch face L
    leftFace = [3, 5, 7, 10, 11, 12]
    return any(item in leftFace for item in trackList)


def containsB(trackList):
    # these are the track types that touch face B
    bottomFace = [2, 4, 7, 8, 9, 12]
    return any(item in bottomFace for item in trackList)


def containsT(trackList):
    # these are the track types that touch face T
    topFace = [1, 2, 3, 6, 8, 10]
    return any(item in topFace for item in trackList)


def applyRowConstraints(a, b):
    #
    if a.solved and not (b.solved):
        if containsR(a.initialState):
            # remove all tracks EXCEPT left face
            b.initialState = list(set(b.initialState) - {1, 2, 4, 6, 8, 9})
            b.hasTrack = True
        else:
            # remove all the left face tracks
            b.initialState = list(set(b.initialState) - {3, 5, 7, 10, 11, 12})

    if b.solved and not (a.solved):
        if containsL(b.initialState):
            # remove all tracks EXCEPT right face
            a.initialState = list(set(a.initialState) - {2, 3, 7, 8, 10, 12})
            a.hasTrack = True
        else:
            # remove all right face tracks
            a.initialState = list(set(a.initialState) - {1, 4, 5, 6, 9, 11})

    if not a.solved and not b.solved:
        if not containsR(a.initialState):
            b.initialState = list(set(b.initialState) - {3, 5, 7, 10, 11, 12})
        if not containsL(b.initialState):
            a.initialState = list(set(a.initialState) - {1, 4, 5, 6, 9, 11})
        # check if the 2 squares are in the same group, remove connecting options CANNOT BE CONNECTED as would create a loop
        if g[a.x * 8 + a.y] == g[b.x * 8 + b.y] and g[a.x * 8 + a.y] > 0:
            # pass
            # print(g)
            print(a.x * 8 + a.y, b.x * 8 + b.y)
            # remove all right face tracks
            a.initialState = list(set(a.initialState) - {1, 4, 5, 6, 9, 11})
            # remove all the left face tracks
            b.initialState = list(set(b.initialState) - {3, 5, 7, 10, 11, 12})


def applyColConstraints(a, b):
    #
    if a.solved and not (b.solved):
        if containsB(a.initialState):
            # remove all tracks EXCEPT top face
            b.initialState = list(set(b.initialState) - {4, 5, 7, 9, 11, 12})
            b.hasTrack = True
        else:
            # remove all the top face tracks
            b.initialState = list(set(b.initialState) - {1, 2, 3, 6, 8, 10})

    if b.solved and not (a.solved):
        if containsT(b.initialState):
            # remove all tracks EXCEPT bottom face
            a.initialState = list(set(a.initialState) - {1, 3, 5, 6, 10, 11})
            a.hasTrack = True
        else:
            # remove all bottom face tracks
            a.initialState = list(set(a.initialState) - {2, 4, 7, 8, 9, 12})

    if not (a.solved) and not (b.solved):
        if not (containsB(a.initialState)):
            b.initialState = list(set(b.initialState) - {1, 2, 3, 6, 8, 10})
        if not (containsT(b.initialState)):
            a.initialState = list(set(a.initialState) - {2, 4, 7, 8, 9, 12})
        if g[a.x * 8 + a.y] == g[b.x * 8 + b.y] and g[a.x * 8 + a.y] > 0:
            # pass
            # print(g)
            print(a.x * 8 + a.y, b.x * 8 + b.y)
            # remove all bottom face tracks
            a.initialState = list(set(a.initialState) - {2, 4, 7, 8, 9, 12})
            # remove all the top face tracks
            b.initialState = list(set(b.initialState) - {1, 2, 3, 6, 8, 10})


def rowConstraints():
    for row in range(0, 8):
        for col in range(0, 7):
            square_index = row * 8 + col
            # 0-1, 1-2 ...
            applyRowConstraints(squares[square_index], squares[square_index + 1])


def colConstraints():
    for row in range(0, 7):
        for col in range(0, 8):
            square_index = row * 8 + col
            # 0-8, 1-9, 2-10 ...
            applyColConstraints(squares[square_index], squares[square_index + 8])


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


def checkColConstraint():
    # check if constraint satisfied and then remove all track options from other squares
    updateColHastracks()
    for col in range(0, 8):
        if ct[col] == colTracks[col]:
            for row in range(0, 8):
                if not squares[row * 8 + col].hasTrack:
                    squares[row * 8 + col].initialState.clear()
                    squares[row * 8 + col].solved = True


def checkRowConstraint():
    # check if constraint satisfied and then remove all track options from other squares in row
    updateRowHastracks()
    for row in range(0, 8):
        if rt[row] == RowTracks[row]:
            for col in range(0, 8):
                if not squares[row * 8 + col].hasTrack:
                    squares[row * 8 + col].initialState.clear()
                    squares[row * 8 + col].solved = True


def forceAddRow():
    # find cases where the number of remaining squares must have tracks
    for row in range(0, 8):
        p = 0
        for col in range(0, 8):
            index = row * 8 + col
            if (
                not squares[index].solved
                and not squares[index].hasTrack
                # and len(squares[index].initialState) > 0
            ):
                p = p + 1
        prt[row] = p

        updateRowHastracks()

        if prt[row] == RowTracks[row] - rt[row]:
            for col in range(0, 8):
                index = row * 8 + col
                if (
                    not squares[index].solved
                    and not squares[index].hasTrack
                    # and len(squares[index].initialState) > 0
                ):
                    squares[index].hasTrack = True


def forcedAddCol():
    for col in range(0, 8):
        p = 0
        for row in range(0, 8):
            index = row * 8 + col
            #
            if (
                not squares[index].solved
                and not squares[index].hasTrack
                # and len(squares[index].initialState) >= 0
            ):
                p = p + 1
        pct[col] = p

        updateColHastracks()

        if pct[col] == colTracks[col] - ct[col]:
            for row in range(0, 8):
                index = row * 8 + col
                if (
                    not squares[index].solved
                    and not squares[index].hasTrack
                    # and len(squares[index].initialState) >= 0
                ):
                    squares[index].hasTrack = True


def checkForSolved():
    for square in squares:
        # print(square.x, square.y, square.initialState, square.solved, square.hasTrack)
        if not square.solved and not square.hasTrack and len(square.initialState) == 0:
            square.solved = True
        if not square.solved and square.hasTrack:
            if len(square.initialState) == 1:
                square.solved = True
            if len(square.initialState) == 2:
                # check if the options are the same but reversed
                # 1,6 2,8 3,10 4,9 5,11 7,7,12
                for s in [[1, 6], [2, 8], [3, 10], [4, 9], [5, 11], [7, 12]]:
                    # print(s)
                    if set(square.initialState) == set(s):
                        square.solved = True


def drawBoard():
    width = 60
    height = 60
    for row in range(8):
        for col in range(8):
            if squares[row * 8 + col].solved:
                color = (0, 0, 255)
            elif squares[row * 8 + col].hasTrack:
                color = (0, 255, 0)
            else:
                color = (255, 0, 0)
            # color = (0, 0, 255)
            pygame.draw.rect(
                surface,
                color,
                pygame.Rect(160 + col * 60, 160 + row * 60, width, height),
                0,
            )


def applyConstraints():
    # covers both squares with and without tracks (unsolved)
    for index, square in enumerate(squares):
        if not square.solved and not (len(square.initialState) == 0):
            print(index, square.initialState)
            for track in square.initialState:
                match track:
                    case 1 | 6:  # T -> R or R -> T
                        r1, c1, r2, c2 = square.x - 1, square.y, square.x, square.y + 1
                        first = squares[index - 8].hasTrack
                        second = squares[index + 1].hasTrack

                        if square.hasTrack:
                            if first and not second:
                                if not (
                                    rt[r2] < RowTracks[r2] and ct[c2] < colTracks[c2]
                                ):
                                    square.initialState.remove(track)
                            if not first and second:
                                if not (
                                    rt[r1] < RowTracks[r1] and ct[c1] < colTracks[c1]
                                ):
                                    square.initialState.remove(track)
                            if not first and not second:
                                if not (
                                    rt[r1] < RowTracks[r1]
                                    and ct[c1] < colTracks[c1]
                                    and rt[r2] < RowTracks[r2]
                                    and ct[c2] < colTracks[c2]
                                ):
                                    square.initialState.remove(track)
                        else:
                            if first and not second:
                                if not (
                                    rt[r2] < RowTracks[r2] - 1
                                    and ct[c1] < colTracks[c1]
                                    and ct[c2] < colTracks[c2]
                                ):
                                    square.initialState.remove(track)
                            if not first and second:
                                if not (
                                    rt[r1] < RowTracks[r1]
                                    and rt[r2] < RowTracks[r2]
                                    and ct[c1] < colTracks[c1] - 1
                                ):
                                    square.initialState.remove(track)
                            if not first and not second:
                                if not (
                                    rt[r1] < RowTracks[r1]
                                    and ct[c1] < colTracks[c1] - 1
                                    and rt[r2] < RowTracks[r2] - 1
                                    and ct[c2] < colTracks[c2]
                                ):
                                    square.initialState.remove(track)

                    case 2 | 8:  # T -> B or B -> T
                        r, r1, c1, r2, c2 = (
                            square.x,
                            square.x - 1,
                            square.y,
                            square.x + 1,
                            square.y,
                        )
                        first = squares[index - 8].hasTrack
                        second = squares[index + 8].hasTrack

                        if square.hasTrack:
                            if first and not (second):
                                if not (
                                    rt[r2] < RowTracks[r2] and ct[c2] < colTracks[c2]
                                ):
                                    square.initialState.remove(track)
                            if not (first) and second:
                                if not (
                                    rt[r1] < RowTracks[r1] and ct[c1] < colTracks[c1]
                                ):
                                    square.initialState.remove(track)
                            if not (first) and not (second):
                                if not (
                                    rt[r1] < RowTracks[r1]
                                    and ct[c1] < colTracks[c1] - 1
                                    and rt[r2] < RowTracks[r2]
                                ):
                                    square.initialState.remove(track)
                        else:
                            if first and not (second):
                                if not (
                                    rt[r2] < RowTracks[r2]
                                    and rt[r] < RowTracks[r]
                                    and ct[c2] < colTracks[c2] - 1
                                ):
                                    square.initialState.remove(track)
                            if not (first) and second:
                                if not (
                                    rt[r1] < RowTracks[r1]
                                    and rt[r] < RowTracks[r2]
                                    and ct[c1] < colTracks[c1] - 1
                                ):
                                    square.initialState.remove(track)
                            if not (first) and not (second):
                                if not (
                                    rt[r] < RowTracks[r]
                                    and rt[r1] < RowTracks[r1]
                                    and ct[c1] < colTracks[c1] - 2
                                    and rt[r2] < RowTracks[r2]
                                ):
                                    square.initialState.remove(track)

                    case 3 | 10:  # T -> L or L -> T
                        r1, c1, r2, c2 = square.x - 1, square.y, square.x, square.y - 1
                        first = squares[index - 8].hasTrack
                        second = squares[index - 1].hasTrack

                        if square.hasTrack:
                            if first and not (second):
                                if not (
                                    rt[r2] < RowTracks[r2] and ct[c2] < colTracks[c2]
                                ):
                                    square.initialState.remove(track)
                            if not (first) and second:
                                if not (
                                    rt[r1] < RowTracks[r1] and ct[c1] < colTracks[c1]
                                ):
                                    square.initialState.remove(track)
                            if not (first) and not (second):
                                if not (
                                    rt[r1] < RowTracks[r1]
                                    and ct[c1] < colTracks[c1]
                                    and rt[r2] < RowTracks[r2]
                                    and ct[c2] < colTracks[c2]
                                ):
                                    square.initialState.remove(track)
                        else:
                            if first and not (second):
                                if not (
                                    rt[r2] < RowTracks[r2] - 1
                                    and ct[c1] < colTracks[c1]
                                    and ct[c2] < colTracks[c2]
                                ):
                                    square.initialState.remove(track)
                            if not (first) and second:
                                if not (
                                    rt[r1] < RowTracks[r1]
                                    and rt[r2] < RowTracks[r2]
                                    and ct[c1] < colTracks[c1] - 1
                                ):
                                    square.initialState.remove(track)
                            if not (first) and not (second):
                                if not (
                                    rt[r1] < RowTracks[r1]
                                    and ct[c1] < colTracks[c1] - 1
                                    and rt[r2] < RowTracks[r2] - 1
                                    and ct[c2] < colTracks[c2]
                                ):
                                    square.initialState.remove(track)

                    case 4 | 9:  # R -> B or B -> R
                        r1, c1, r2, c2 = square.x, square.y + 1, square.x + 1, square.y
                        first = squares[index + 1].hasTrack
                        second = squares[index + 8].hasTrack

                        if square.hasTrack:
                            if first and not (second):
                                if not (
                                    rt[r2] < RowTracks[r2] and ct[c2] < colTracks[c2]
                                ):
                                    square.initialState.remove(track)
                            if not first and second:
                                if not (
                                    rt[r1] < RowTracks[r1] and ct[c1] < colTracks[c1]
                                ):
                                    square.initialState.remove(track)
                            if not (first) and not (second):
                                if not (
                                    rt[r1] < RowTracks[r1]
                                    and ct[c1] < colTracks[c1]
                                    and rt[r2] < RowTracks[r2]
                                    and ct[c2] < colTracks[c2]
                                ):
                                    square.initialState.remove(track)
                        else:
                            if first and not second:
                                if not (
                                    rt[r1] < RowTracks[r1]
                                    and rt[r2] < RowTracks[r2]
                                    and ct[c2] < colTracks[c2] - 1
                                ):
                                    square.initialState.remove(track)
                            if not (first) and second:
                                if not (
                                    rt[r1] < RowTracks[r1] - 1
                                    and ct[c1] < colTracks[c1]
                                    and ct[c2] < colTracks[c2]
                                ):
                                    square.initialState.remove(track)
                            if not (first) and not (second):
                                if not (
                                    rt[r1] < RowTracks[r1] - 1
                                    and ct[c1] < colTracks[c1]
                                    and rt[r2] < RowTracks[r2]
                                    and ct[c2] < colTracks[c2] - 1
                                ):
                                    square.initialState.remove(track)

                    case 5 | 11:  # R -> L or L -> R
                        c, r1, c1, r2, c2 = (
                            square.y,
                            square.x,
                            square.y + 1,
                            square.x,
                            square.y - 1,
                        )
                        first = squares[index + 1].hasTrack
                        second = squares[index - 1].hasTrack

                        if square.hasTrack:
                            if first and not (second):
                                if not (
                                    rt[r2] < RowTracks[r2] and ct[c2] < colTracks[c2]
                                ):
                                    square.initialState.remove(track)
                            if not (first) and second:
                                if not (
                                    rt[r1] < RowTracks[r1] and ct[c1] < colTracks[c1]
                                ):
                                    square.initialState.remove(track)
                            if not (first) and not (second):
                                if not (
                                    rt[r1] < RowTracks[r1] - 1
                                    and ct[c1] < colTracks[c1]
                                    and ct[c2] < colTracks[c2]
                                ):
                                    square.initialState.remove(track)
                        else:
                            if first and not (second):
                                if not (
                                    ct[c] < colTracks[c]
                                    and rt[r2] < RowTracks[r2] - 1
                                    and ct[c2] < colTracks[c2]
                                ):
                                    square.initialState.remove(track)
                            if not (first) and second:
                                if not (
                                    rt[r1] < RowTracks[r1] - 1
                                    and ct[c] < colTracks[c]
                                    and ct[c1] < colTracks[c1]
                                ):
                                    square.initialState.remove(track)
                            if not (first) and not (second):
                                if not (
                                    rt[r1] < RowTracks[r1] - 2
                                    and ct[c] < colTracks[c]
                                    and ct[c1] < colTracks[c1]
                                    and ct[c2] < colTracks[c2]
                                ):
                                    square.initialState.remove(track)

                    case 7 | 12:  # B-> L or L -> B
                        r1, c1, r2, c2 = square.x + 1, square.y, square.x, square.y - 1
                        first = squares[index + 8].hasTrack
                        second = squares[index - 1].hasTrack

                        if square.hasTrack:
                            if first and not (second):
                                if not (
                                    rt[r2] < RowTracks[r2] and ct[c2] < colTracks[c2]
                                ):
                                    square.initialState.remove(track)
                            if not (first) and second:
                                if not (
                                    rt[r1] < RowTracks[r1] and ct[c1] < colTracks[c1]
                                ):
                                    square.initialState.remove(track)
                            if not (first) and not (second):
                                if not (
                                    rt[r1] < RowTracks[r1]
                                    and ct[c1] < colTracks[c1]
                                    and rt[r2] < RowTracks[r2]
                                    and ct[c2] < colTracks[c2]
                                ):
                                    square.initialState.remove(track)
                        else:
                            if first and not second:
                                if not (
                                    ct[c1] < colTracks[c1]
                                    and rt[r2] < RowTracks[r2] - 1
                                    and ct[c2] < colTracks[c2]
                                ):
                                    square.initialState.remove(track)
                            if not first and second:
                                if not (
                                    rt[r2] < RowTracks[r2]
                                    and rt[r1] < RowTracks[r1]
                                    and ct[c1] < colTracks[c1] - 1
                                ):
                                    square.initialState.remove(track)
                            if not first and not second:
                                if not (
                                    rt[r1] < RowTracks[r1]
                                    and ct[c1] < colTracks[c1] - 1
                                    and rt[r2] < RowTracks[r2] - 1
                                    and ct[c2] < colTracks[c2]
                                ):
                                    square.initialState.remove(track)


# x = 30 + col * 60
# y = 30 + row * 60

# Centre Top        (x + 30, y)
# Centre Right      (x + 60, y + 30)
# Centre Bottom     (x + 30, y + 30)
# Centre Left       (x, y + 30)
# Centre            (x + 30, y + 30)


def drawtrack(row, col, trackType):
    # 1(T-R),2(T-B),3(T-L),4(R-B),5(R-L),6(R-T),7(B-L),8(B-T),9(B-R),10(L-T),11(L-R),12(L-B)
    # 1,6   (ct,c,cr)
    # 2,8   (ct,c,cb)
    # 3,10  (ct,c,cl)
    # 4,9   (cr,c,cb)
    # 5,11  (cr,c,cl)
    # 7,12  (cl,c,cb)

    x = 160 + col * 60
    y = 160 + row * 60

    ct = (x + 30, y)
    cr = (x + 60, y + 30)
    cb = (x + 30, y + 60)
    cl = (x, y + 30)
    c = (x + 30, y + 30)

    match trackType:
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
        squares.append(Square(row, col))

for item in puzzle:
    index = item[0] * 8 + item[1]
    squares[index].initialState = item[2]
    squares[index].solved = True
    squares[index].hasTrack = True


def findGroups(index):
    if squares[index].solved and squares[index].hasTrack and g[index] == 0:
        g[index] = group
        # print(index, squares[index].initialState, group)
        for trackType in squares[index].initialState:
            match trackType:
                # MOVE RIGHT
                case 1 | 9 | 11:
                    findGroups(index + 1)
                # MOVE LEFT
                case 3 | 5 | 7:
                    findGroups(index - 1)
                # MOVE UP
                case 6 | 8 | 10:
                    findGroups(index - 8)
                # MOVE DOWN
                case 2 | 4 | 12:
                    findGroups(index + 8)
    else:
        # include squares at the ends; even though they are not solved, they will still be part of this group
        if squares[index].hasTrack and g[index] == 0:
            # print(index, squares[index].initialState, group)
            g[index] = group
            # pass


while True:
    # iterate over the list of Event objects
    # that was returned by pygame.event.get() method.

    surface.fill((0, 0, 0))

    drawBoard()

    for row in range(8):
        for col in range(8):
            for trk in squares[row * 8 + col].initialState:
                drawtrack(row, col, trk)

    for n in range(0, 5):
        checkColConstraint()
        checkRowConstraint()
        rowConstraints()
        colConstraints()
        checkForSolved()
        forceAddRow()
        forcedAddCol()

    applyConstraints()

    g = [0] * 64
    group = 1

    for index, square in enumerate(squares):
        if squares[index].solved and squares[index].hasTrack and g[index] == 0:
            findGroups(index)
            # print(g)
            group = group + 1

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
                forcedAddCol()
            elif event.key == pygame.K_LEFT:
                forceAddRow()
            elif event.key == pygame.K_UP:
                applyConstraints()

    # Draws the surface object to the screen.
    pygame.display.update()
    # pygame.display.flip()

    clock.tick(1)
