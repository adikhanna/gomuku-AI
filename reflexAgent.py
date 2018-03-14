import numpy
import math
import itertools
import scipy, scipy.ndimage
import copy
from itertools import groupby
from operator import itemgetter

# board is a dictionary, where the keys are positions and values are spaces, B or R
# board[(1, 2)] = "B"


# arg passed in is current board condition, where board is as described above

def move_one(arg, color):

        if (color == 'B'):
            dict = arg
            agent_stones = []

            # for i, row in enumerate(arg):
            #     for j, col in enumerate(row):
            #         if col == "B":
            #             agent_stones.append((i, j))
            #
            # if len(agent_stones) != 4:
            #     print "Move_One: four agent stones are not on the board!"
            #     return None

            agent_stones = chain_four(arg, 'B')

            if len(agent_stones) != 0:
                agent_stones = agent_stones[0]

            else:
                #print "No chain found.."
                return None

            if (horiz_test(agent_stones)):
                #print "Move_1"
                return find_horizontal_move(agent_stones, dict)

            elif (vert_test(agent_stones)):
                #print "Move_1"
                return find_vertical_move(agent_stones, dict)

            elif (diag_test(agent_stones)):
                #print "Move_1"
                return find_diagonal_move(agent_stones, dict)

            else:
                #print "Move_One: no unbroken agent chain of length 4 found!"
                return None

        else:
            dict = arg
            agent_stones = []

            # for i, row in enumerate(arg):
            #     for j, col in enumerate(row):
            #         if col == "R":
            #             agent_stones.append((i, j))
            #
            # if len(agent_stones) != 4:
            #     print "Move_One: four agent stones are not on the board!"
            #     return None

            agent_stones = chain_four(arg, 'R')

            if len(agent_stones) != 0:
                agent_stones = agent_stones[0]
            else:
                #print "No chain found.."
                return None

            if (horiz_test(agent_stones)):
                #print "Move_1"
                return find_horizontal_move(agent_stones, dict)

            elif (vert_test(agent_stones)):
                #print "Move_1"
                return find_vertical_move(agent_stones, dict)

            elif (diag_test(agent_stones)):
                #print "Move_1"
                return find_diagonal_move(agent_stones, dict)

            else:
                #print "Move_One: no unbroken agent chain of length 4 found!"
                return None


# arg passed in is current board condition

def move_two(arg, color):

    if (color == 'B'):
        dict = arg
        opp_stones = []

        # for i, row in enumerate(arg):
        #     for j, col in enumerate(row):
        #         if col == "R":
        #             opp_stones.append((i, j))
        #
        # if len(opp_stones) != 4:
        #     print "Move_Two: four opponent stones are not on the board!"
        #     return None

        opp_stones = chain_four(arg, 'R')

        if len(opp_stones) != 0:
            opp_stones = opp_stones[0]
        else:
            #print "No chain found.."
            return None

        if (horiz_test(opp_stones)):
            #print "Move_2"
            return find_horizontal_move(opp_stones, dict)

        elif (vert_test(opp_stones)):
            #print "Move_2"
            return find_vertical_move(opp_stones, dict)

        elif (diag_test(opp_stones)):
            #print "Move_2"
            return find_diagonal_move(opp_stones, dict)

        else:
            #print "Move_Two: no unbroken opponent chain of length 4 found!"
            return None

    else:
        dict = arg
        opp_stones = []

        # for i, row in enumerate(arg):
        #     for j, col in enumerate(row):
        #         if col == "B":
        #             opp_stones.append((i, j))
        #
        # if len(opp_stones) != 4:
        #     print "Move_Two: four opponent stones are not on the board!"
        #     return None

        opp_stones = chain_four(arg, 'B')

        if len(opp_stones) != 0:
            opp_stones = opp_stones[0]
        else:
            #print "No chain found.."
            return None

        if (horiz_test(opp_stones)):
            #print "Move_2"
            return find_horizontal_move(opp_stones, dict)

        elif (vert_test(opp_stones)):
            #print "Move_2"
            return find_vertical_move(opp_stones, dict)

        elif (diag_test(opp_stones)):
            #print "Move_2"
            return find_diagonal_move(opp_stones, dict)

        else:
            #print "Move_Two: no unbroken opponent chain of length 4 found!"
            return None


# arg passed in is current board condition

def move_three(arg, color):

    if color == 'B':
        dict = arg
        opp_stones = []

        # for i, row in enumerate(arg):
        #     for j, col in enumerate(row):
        #         if col == "R":
        #             opp_stones.append((i, j))
        #
        # if len(opp_stones) != 3:
        #     print "Move_Three: three opponent stones are not on the board!"
        #     return None

        opp_stones = chain_three(arg, 'R')

        if len(opp_stones) != 0:
            opp_stones = opp_stones[0]
        else:
            #print "No chain found.."
            return None

        if (horiz_test(opp_stones)):
            #print "Move_3"
            return find_horizontal_move(opp_stones, dict)

        elif (vert_test(opp_stones)):
            #print "Move_3"
            return find_vertical_move(opp_stones, dict)

        elif (diag_test(opp_stones)):
            #print "Move_3"
            return find_diagonal_move(opp_stones, dict)

        else:
            #print "Move_Three: no unbroken opponent chain of length 3 found!"
            return None

    else:
        dict = arg
        opp_stones = []

        # for i, row in enumerate(arg):
        #     for j, col in enumerate(row):
        #         if col == "B":
        #             opp_stones.append((i, j))
        #
        # if len(opp_stones) != 3:
        #     print "Move_Three: three opponent stones are not on the board!"
        #     return None

        opp_stones = chain_three(arg, 'B')

        if len(opp_stones) != 0:
            opp_stones = opp_stones[0]
        else:
            #print "No chain found.."
            return None

        if (horiz_test(opp_stones)):
            #print "Move_3"
            return find_horizontal_move(opp_stones, dict)

        elif (vert_test(opp_stones)):
            #print "Move_3"
            return find_vertical_move(opp_stones, dict)

        elif (diag_test(opp_stones)):
            #print "Move_3"
            return find_diagonal_move(opp_stones, dict)

        else:
            #print "Move_Three: no unbroken opponent chain of length 3 found!"
            return None

def tie_breaker(arg):
    # type: (object) -> object
    x_dict = {}

    for i in arg:
        x_dict[i] = i[1]

    left_vals = []
    min_value = float("inf")

    for k, v in x_dict.items():
        if v == min_value:
            left_vals.append(k)
        if v < min_value:
            min_value = v
            left_vals = []
            left_vals.append(k)

    if len(left_vals) == 1:
        return left_vals[0]
    else:
        return min(left_vals, key=lambda t: t[0])

    return None

def min_x_val(arg):
    min_value = float("inf")

    for x in arg:
        if x[1] < min_value:
            min_value = x[1]

    return min_value

def min_y_val(arg):
    min_value = float("inf")

    for x in arg:
        if x[0] < min_value:
            min_value = x[0]

    return min_value

def thepos(best_winning_block, arg):
    poss = []
    stones = []

    for cc in best_winning_block:
        if arg[cc[0]][cc[1]] == 'B':
            stones.append(cc)
        else:
            poss.append(cc)

    final_pos = []
    dict = {}

    for stone in stones:
        for pos in poss:
            if (point_distance(pos, stone) == 1):
                final_pos.append(pos)

    if len(final_pos) == 0:
        #print "No winning positions to place a stone! - Bad Error."
        return None

    if len(final_pos) == 1:
        #print "Move_4"
        return final_pos[0]
    else:
        #print "Move_4"
        return tie_breaker(final_pos)


def move_four(arg, color):

    if color == 'B':
        G = numpy.zeros((7, 7))

        for i, row in enumerate(arg):
            for j, col in enumerate(row):
                if col == "R":
                    G[i][j] = 1

        all_seq_b = get_consecutive_spaces(G, 5)

        x, y, z = parse(all_seq_b)

        horiz_pos = horiz_parse(x)
        vert_pos = vert_parse(y)
        diag_pos = diag_parse(z)

        winning_blocks = horiz_pos + vert_pos + diag_pos

        if (len(winning_blocks) == 0):
            empty_pos = []
            for i, row in enumerate(arg):
                for j, col in enumerate(row):
                    if col == " ":
                        empty_pos.append((i, j))
            pos = tie_breaker(empty_pos)
            #print "Move_4"
            return pos

        dictionary = {}

        for q in winning_blocks:
            count = 0
            for iter, (aa, bb) in enumerate(q):
                if arg[aa][bb] == 'B':
                    count = count + 1
            dictionary[tuple(q)] = count

        max_block = max(dictionary, key=dictionary.get)
        max_value = dictionary[max_block]

        best_blocks = []

        for k, v in dictionary.items():
            if v == max_value:
                best_blocks.append(k)
            else:
                continue

        final_dict = {}

        # good till here

        the_positions = []
        stones = []

        for bb in best_blocks:
            for cc in bb:
                the_positions.append(cc)

        the_positions = list(set(the_positions))
        the_positions.sort(key=lambda x: x[1])
        the_positions.sort(key=lambda x: x[0])

        #print "Blue positions:"
        #print the_positions

        for cc in the_positions:
            if arg[cc[0]][cc[1]] == 'B':
                stones.append(cc)

        final_pos = []
        dict = {}

        for stone in stones:
            for pos in the_positions:
                if (point_distance(pos, stone) == 1) and (arg[pos[0]][pos[1]] != 'B'):
                    final_pos.append(pos)

        if len(final_pos) == 0:
            empty_pos = []
            for i, row in enumerate(arg):
                for j, col in enumerate(row):
                    if col == " ":
                        empty_pos.append((i, j))
            pos = tie_breaker(empty_pos)
            #print "Move_4"
            return pos

        if len(final_pos) == 1:
            #print "Move_4"
            return final_pos[0]
        else:
            #print "Move_4"
            return tie_breaker(final_pos)

    else:
        G = numpy.zeros((7, 7))

        for i, row in enumerate(arg):
            for j, col in enumerate(row):
                if col == "B":
                    G[i][j] = 1

        all_seq_r = get_consecutive_spaces(G, 5)

        x, y, z = parse(all_seq_r)

        horiz_pos = horiz_parse(x)
        vert_pos = vert_parse(y)
        diag_pos = diag_parse(z)

        winning_blocks = horiz_pos + vert_pos + diag_pos

        if (len(winning_blocks) == 0):
            empty_pos = []
            for i, row in enumerate(arg):
                for j, col in enumerate(row):
                    if col == " ":
                        empty_pos.append((i, j))
            pos = tie_breaker(empty_pos)
            #print "Move_4"
            return pos

        dictionary = {}

        for q in winning_blocks:
            count = 0
            for iter, (aa, bb) in enumerate(q):
                if arg[aa][bb] == 'R':
                    count = count + 1
            dictionary[tuple(q)] = count

        max_block = max(dictionary, key=dictionary.get)
        max_value = dictionary[max_block]

        best_blocks = []

        for k, v in dictionary.items():
            if v == max_value:
                best_blocks.append(k)
            else:
                continue

        final_dict = {}

        # good till here

        the_positions = []
        stones = []

        for bb in best_blocks:
            for cc in bb:
                the_positions.append(cc)

        the_positions = list(set(the_positions))
        the_positions.sort(key=lambda x: x[1])
        the_positions.sort(key=lambda x: x[0])

        #print "Red positions:"
        #print the_positions

        for cc in the_positions:
            if arg[cc[0]][cc[1]] == 'R':
                stones.append(cc)

        final_pos = []
        dict = {}

        for stone in stones:
            for pos in the_positions:
                if (point_distance(pos, stone) == 1) and (arg[pos[0]][pos[1]] != 'R'):
                    final_pos.append(pos)

        if len(final_pos) == 0:
            empty_pos = []
            for i, row in enumerate(arg):
                for j, col in enumerate(row):
                    if col == " ":
                        empty_pos.append((i, j))
            pos = tie_breaker(empty_pos)
            #print "Move_4"
            return pos

        if len(final_pos) == 1:
            #print "Move_4"
            return final_pos[0]
        else:
            #print "Move_4"
            return tie_breaker(final_pos)

def horiz_parse(arg):
    h_positions = []

    for i, j in arg:

        if len(i) == 7:
            for a in range(0, 3):
                y = j[0]
                temp_sev = []
                for b in range(i[a], 5 + a):
                    temp_sev.append((b, y))
                h_positions.append(temp_sev)

        elif len(i) == 6:
            for a in range(0, 2):
                y = j[0]
                temp_six = []
                for b in range(i[a], 5 + a):
                    temp_six.append((b, y))
                h_positions.append(temp_six)
        else:
            y = j[0]
            temp_five = []
            for b in i:
                temp_five.append((b, y))
            h_positions.append(temp_five)

    return h_positions


def vert_parse(arg):
    v_positions = []

    for i, j in arg:

        if len(i) == 7:
            for a in range(0, 3):
                x = i[0]
                temp_sev = []
                for b in range(j[a], 5 + a):
                    temp_sev.append((x, b))
                v_positions.append(temp_sev)

        elif len(i) == 6:
            for a in range(0, 2):
                x = i[0]
                temp_six = []
                for b in range(j[a], 5 + a):
                    temp_six.append((x, b))
                v_positions.append(temp_six)
        else:
            x = i[0]
            temp_five = []
            for b in j:
                temp_five.append((x, b))
            v_positions.append(temp_five)

    return v_positions

def diag_parse(arg):
    d_positions = []

    for i, j in arg:
        if len(i) == 7:
            temp_sev = []
            for b, c in zip(i, j):
                    temp_sev.append((b, c))
            for a in range(0, 3):
                    d_positions.append(temp_sev[a:5+a])

        elif len(i) == 6:
            temp_six = []
            for b, c in zip(i, j):
                    temp_six.append((b, c))
            for a in range(0, 2):
                    d_positions.append(temp_six[a:5+a])

        else:
            temp_five = []
            for b, c in zip(i, j):
                    temp_five.append((b, c))
            d_positions.append(temp_five)

    return d_positions


def parse(arg):

    horiz = []
    vert = []
    diag = []

    for i, j in arg:
        if (all(x == j[0] for x in j)):
            horiz.append((i, j))
        elif (all(x == i[0] for x in i)):
            vert.append((i, j))
        else:
            diag.append((i, j))

    return horiz, vert, diag


def get_consecutive_spaces(G, chain):
    sequences = []
    patterns = [scipy.ndimage.label(G == 0, structure = scipy.array([[0,0,0],
                                                                     [1,1,1],
                                                                     [0,0,0]])),
                scipy.ndimage.label(G == 0, structure = scipy.array([[0,1,0],
                                                                     [0,1,0],
                                                                     [0,1,0]])),
                scipy.ndimage.label(G == 0, structure = scipy.array([[1,0,0],
                                                                     [0,1,0],
                                                                     [0,0,1]])),
                scipy.ndimage.label(G == 0, structure = scipy.array([[0,0,1],
                                                                     [0,1,0],
                                                                     [1,0,0]]))]
    for lab_arr, n in patterns:
        for i in range(1, n+1):
            b = lab_arr == i
            b_inds = scipy.where(b)
            if len(b_inds[0]) >= chain:
                sequences.append((tuple(b_inds[0]), tuple(b_inds[1])))
            else:
                continue

    return sequences

# calculates the distance of the argument from the origin
# used in tie breakers, where more than one positions exist

def distance(arg):
    x = arg[0]
    y = arg[1]

    return math.sqrt(pow(x, 2) + pow(y, 2))

# finds the next horizontal move to make
# based on the positions of stones and current grid situation

def find_horizontal_move(arg, grid):
    arg.sort()
    first_pos = arg[0]
    last_pos = arg[-1]

    x_start = first_pos[1]
    x_last = last_pos[1]

    y = first_pos[0]

    if ((x_start - 1) < 0) and ((x_last + 1) > 6):
        return None

    if ((x_start - 1) < 0) and (grid[y][x_last + 1] == ' '):
        return (y, x_last + 1)

    if ((x_last + 1) > 6) and (grid[y][x_start - 1] == ' '):
        return (y, x_start - 1)

    if ((x_start - 1) < 0) and (grid[y][x_last + 1] != ' '):
        return None

    if ((x_last + 1) > 6) and (grid[y][x_start - 1] != ' '):
        return None

    if (grid[y][x_last + 1] == ' ') and (grid[y][x_start - 1] == ' '):
        dist_start = distance((y, x_start - 1))
        dist_last = distance((y, x_last + 1))

        if (dist_start <= dist_last):
            return (y, x_start - 1)
        else:
            return (y, x_last + 1)

    elif grid[y][x_start - 1] == ' ':
        return (y, x_start - 1)

    elif grid[y][x_last + 1] == ' ':
        return (y, x_last + 1)

    else:
        return None

# finds the next vertical move to make
# based on the positions of stones and current grid situation

def find_vertical_move(arg, grid):
    arg.sort()
    first_pos = arg[0]
    last_pos = arg[-1]

    y_start = first_pos[0]
    y_last = last_pos[0]

    x = first_pos[1]

    if ((y_start - 1) < 0) and ((y_last + 1) > 6):
        return None

    if ((y_start - 1) < 0) and (grid[y_last + 1][x] == " "):
        return (y_last + 1, x)

    if ((y_last + 1) > 6) and (grid[y_start - 1][x] == " "):
        return (y_start - 1, x)

    if ((y_start - 1) < 0) and (grid[y_last + 1][x] != ' '):
        return None

    if ((y_last + 1) > 6) and (grid[y_start - 1][x] != ' '):
        return None

    if (grid[y_start - 1][x] == " ") and (grid[y_last + 1][x] == " "):
        dist_start = distance((y_start - 1, x))
        dist_last = distance((y_last + 1, x))

        if (dist_start <= dist_last):
            return (y_start - 1, x)
        else:
            return (y_last + 1, x)

    elif grid[y_start - 1][x] == " ":
        return (y_start - 1, x)

    elif grid[y_last + 1][x] == " ":
        return (y_last + 1, x)

    else:
        return None

# finds the next diagonal move to make
# based on the positions of stones and current grid situation

def find_diagonal_move(arg, grid):
    arg.sort()
    first_pos = arg[0]
    last_pos = arg[-1]

    if (first_pos[1] < last_pos[1]):
        y1 = first_pos[0] - 1
        x1 = first_pos[1] - 1
        y2 = last_pos[0] + 1
        x2 = last_pos[1] + 1
    else:
        y1 = first_pos[0] - 1
        x1 = first_pos[1] + 1
        y2 = last_pos[0] + 1
        x2 = last_pos[1] - 1

    if ((x1 < 0) or (x1 > 6)) or ((y1 < 0) or (y1 > 6)):
        if ((x2 < 0) or (x2 > 6)) or ((y2 < 0) or (y2 > 6)):
            return None
        elif grid[y2][x2] == " ":
            return (y2,x2)
        else:
            return None

    if ((x2 < 0) or (x2 > 6)) or ((y2 < 0) or (y2 > 6)) and grid[y1][x1] == " ":
        return (y1,x1)

    if (grid[y1][x1] == " ") and (grid[y2][x2] == " "):
        dist1 = distance((y1, x1))
        dist2 = distance((y2, x2))

        if (dist1 <= dist2):
            return (y1, x1)
        else:
            return (y2, x2)

    elif grid[y1][x1] == " ":
        return (y1, x1)

    elif grid[y2][x2] == " ":
        return (y2, x2)

    else:
        return None

# arg passed in is list of positions, this function checks if they form an
# unbroken chain horizontally

def horiz_test(arg):
    arg.sort()

    for i in arg:
        if i[0] != arg[0][0]:
            return False

    l = []
    x = 1

    for j in arg:
        l.append(j[1])

    v = list(numpy.diff(l))
    result = v and all(p == x for p in v)

    if result == True:
        return True
    return False


# arg passed in is list of positions, this function checks if they form an
# unbroken chain vertically

def vert_test(arg):
    arg.sort()

    for i in arg:
        if i[1] != arg[0][1]:
            return False

    l = []
    x = 1

    for j in arg:
        l.append(j[0])

    v = list(numpy.diff(l))
    result = v and all(p == x for p in v)

    if result == True:
        return True
    return False

# arg passed in is list of positions, this function checks if they form an
# unbroken chain diagonally

def diag_test(arg):
    arg.sort()
    x = []
    y = []
    d = 1

    for i in arg:
        x.append(i[1])
        y.append(i[0])

    x.sort()
    y.sort()

    v_x = list(numpy.diff(x))
    v_y = list(numpy.diff(y))

    result_x = v_x and all(p == d for p in v_x)
    result_y = v_y and all(p == d for p in v_y)

    if (result_x and result_y):
        return True
    return False

# calculates the distance between two points, to be used by
# the evaluation function in the alpha-beta/minimax agents

def point_distance(arg1, arg2):
    x1, y1 = arg1
    x2, y2 = arg2
    return int(math.sqrt(pow((x2-x1), 2) + pow((y2-y1), 2)))

def reflex_agent(arg, color):

  if (move_one(arg, color) == None):
      if (move_two(arg, color) == None):
          if (move_three(arg, color) == None):
              if (move_four(arg, color) == None):
                  return (X, X)
              else:
                  return move_four(arg, color)
          else:
              return move_three(arg, color)
      else:
          return move_two(arg, color)
  else:
      return move_one(arg, color)


# Draws 7 x 7 board based on current positioning
# Input: Current board
# Output: N/A

def drawBoard(board):
    for i in range(7):
        print " "
        for j in range(7):
            print board[i][j],


# Updates the game board given a new stone position
# Inputs: Current board, position to place stone, color of stone
# Outputs: Updated board

def updateBoard(board, action, color):
    new_board = copy.deepcopy(board)

    if new_board[action[0]][action[1]] != ' ':
        return new_board
    elif color == 'B':
        new_board[action[0]][action[1]] = 'B'
    elif color == 'R':
        new_board[action[0]][action[1]] = 'R'

    return new_board


def checkVictory(board, color):
    for sequence in sequences():
        count = 0
        for (x, y) in sequence:
            if board[x][y] == color:
                count = count + 1

        if count == 5:
            return 1

    return 0

# Run minimax vs reflex algorithms on blank 7x7 game board
# Blue is reflex agent, Red is minimax
# Input: N/A
# Output: Consecutive actions and resulting boards

def startMatch():

    red_stones = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    blue_stones = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    game_board = [[' ' for i in range(7)] for j in range(7)]
    game_board[1][1] = 'R'
    game_board[5][5] = 'B'

    action = reflex_agent(game_board, 'R')
    print "\n", action
    new_board = updateBoard(game_board, action, 'R')
    drawBoard(new_board)

    for i in range(46):

        if i % 2 == 0:
            action = reflex_agent(new_board, 'B')
            print "\n", action
            new_board = updateBoard(new_board, action, 'B')
            drawBoard(new_board)
            if checkVictory(new_board, 'B'):
                print "Blue wins!"
                return

        else:
            action = reflex_agent(new_board, 'R')
            print "\n", action
            new_board = updateBoard(new_board, action, 'R')
            drawBoard(new_board)
            if checkVictory(new_board, 'R'):
                print "Red wins!"
                return


def chain_four(board, color):

    chains = []

    for sequence in sequences():

        chain_count = 0
        space_count = 0
        new_chain = []

        for (x, y) in sequence:

            if board[x][y] == ' ' and chain_count == 4:
                chains.append(new_chain)
                break

            if board[x][y] == color and space_count == 1 and chain_count == 3:
                chains.append(new_chain)
                break

            if board[x][y] == ' ':
                new_chain = []
                chain_count = 0
                space_count = 1
            elif board[x][y] == color:
                new_chain.append((x, y))
                chain_count = chain_count + 1
            else:
                new_chain = []
                space_count = 0
                chain_count = 0

    return chains


def chain_three(board, color):
    chains = []

    for sequence in sequences():

        chain_count = 0
        space_count = 0
        new_chain = []

        for (x, y) in sequence:

            if board[x][y] == ' ' and chain_count == 3:
                chains.append(new_chain)
                break

            if board[x][y] == ' ':
                new_chain = []
                chain_count = 0
                space_count = 1

            elif board[x][y] == color and space_count == 1:
                new_chain.append((x, y))
                chain_count = chain_count + 1

            else:
                new_chain = []
                space_count = 0
                chain_count = 0

    return chains

def goto(line) :

    global lineNumber
    line = lineNumber


def sequences():
    sequences = []

    # Rows

    sequences.append([(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)])
    sequences.append([(0, 1), (0, 2), (0, 3), (0, 4), (0, 5)])
    sequences.append([(0, 2), (0, 3), (0, 4), (0, 5), (0, 6)])

    sequences.append([(1, 0), (1, 1), (1, 2), (1, 3), (1, 4)])
    sequences.append([(1, 1), (1, 2), (1, 3), (1, 4), (1, 5)])
    sequences.append([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6)])

    sequences.append([(2, 0), (2, 1), (2, 2), (2, 3), (2, 4)])
    sequences.append([(2, 1), (2, 2), (2, 3), (2, 4), (2, 5)])
    sequences.append([(2, 2), (2, 3), (2, 4), (2, 5), (2, 6)])

    sequences.append([(3, 0), (3, 1), (3, 2), (3, 3), (3, 4)])
    sequences.append([(3, 1), (3, 2), (3, 3), (3, 4), (3, 5)])
    sequences.append([(3, 2), (3, 3), (3, 4), (3, 5), (3, 6)])

    sequences.append([(4, 0), (4, 1), (4, 2), (4, 3), (4, 4)])
    sequences.append([(4, 1), (4, 2), (4, 3), (4, 4), (4, 5)])
    sequences.append([(4, 2), (4, 3), (4, 4), (4, 5), (4, 6)])

    sequences.append([(5, 0), (5, 1), (5, 2), (5, 3), (5, 4)])
    sequences.append([(5, 1), (5, 2), (5, 3), (5, 4), (5, 5)])
    sequences.append([(5, 2), (5, 3), (5, 4), (5, 5), (5, 6)])

    sequences.append([(6, 0), (6, 1), (6, 2), (6, 3), (6, 4)])
    sequences.append([(6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    sequences.append([(6, 2), (6, 3), (6, 4), (6, 5), (6, 6)])

    # Columns

    sequences.append([(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)])
    sequences.append([(1, 0), (2, 0), (3, 0), (4, 0), (5, 0)])
    sequences.append([(2, 0), (3, 0), (4, 0), (5, 0), (6, 0)])

    sequences.append([(0, 1), (1, 1), (2, 1), (3, 1), (4, 1)])
    sequences.append([(1, 1), (2, 1), (3, 1), (4, 1), (5, 1)])
    sequences.append([(2, 1), (3, 1), (4, 1), (5, 1), (6, 1)])

    sequences.append([(0, 2), (1, 2), (2, 2), (3, 2), (4, 2)])
    sequences.append([(1, 2), (2, 2), (3, 2), (4, 2), (5, 2)])
    sequences.append([(2, 2), (3, 2), (4, 2), (5, 2), (6, 2)])

    sequences.append([(0, 3), (1, 3), (2, 3), (3, 3), (4, 3)])
    sequences.append([(1, 3), (2, 3), (3, 3), (4, 3), (5, 3)])
    sequences.append([(2, 3), (3, 3), (4, 3), (5, 3), (6, 3)])

    sequences.append([(0, 4), (1, 4), (2, 4), (3, 4), (4, 4)])
    sequences.append([(1, 4), (2, 4), (3, 4), (4, 4), (5, 4)])
    sequences.append([(2, 4), (3, 4), (4, 4), (5, 4), (6, 4)])

    sequences.append([(0, 5), (1, 5), (2, 5), (3, 5), (4, 5)])
    sequences.append([(1, 5), (2, 5), (3, 5), (4, 5), (5, 5)])
    sequences.append([(2, 5), (3, 5), (4, 5), (5, 5), (6, 5)])

    sequences.append([(0, 6), (1, 6), (2, 6), (3, 6), (4, 6)])
    sequences.append([(1, 6), (2, 6), (3, 6), (4, 6), (5, 6)])
    sequences.append([(2, 6), (3, 6), (4, 6), (5, 6), (6, 6)])

    # Diagonals

    sequences.append([(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)])
    sequences.append([(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])
    sequences.append([(2, 2), (3, 3), (4, 4), (5, 5), (6, 6)])

    sequences.append([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)])
    sequences.append([(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)])

    sequences.append([(0, 2), (1, 3), (2, 4), (3, 5), (4, 6)])

    sequences.append([(1, 0), (2, 1), (3, 2), (4, 3), (5, 4)])
    sequences.append([(2, 1), (3, 2), (4, 3), (5, 4), (6, 5)])

    sequences.append([(2, 0), (3, 1), (4, 2), (5, 3), (6, 4)])

    sequences.append([(0, 6), (1, 5), (2, 4), (3, 3), (4, 2)])
    sequences.append([(1, 5), (2, 4), (3, 3), (4, 2), (5, 1)])
    sequences.append([(2, 4), (3, 3), (4, 2), (5, 1), (6, 0)])

    sequences.append([(0, 5), (1, 4), (2, 3), (3, 2), (4, 1)])
    sequences.append([(1, 4), (2, 3), (3, 2), (4, 1), (5, 0)])

    sequences.append([(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)])

    sequences.append([(1, 6), (2, 5), (3, 4), (4, 3), (5, 2)])
    sequences.append([(2, 5), (3, 4), (4, 3), (5, 2), (6, 1)])

    sequences.append([(2, 6), (3, 5), (4, 4), (5, 3), (6, 2)])

    return sequences

startMatch()

# references:
# https://stackoverflow.com/questions/49212929/given-a-n%C3%97n-grid-compute-all-possible-sequences-of-5-consecutive-spaces/49214156#49214156

