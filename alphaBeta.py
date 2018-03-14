import sys
import time
import copy
import reflexAgent
import seq

# Draws 7 x 7 board based on current positioning
# Input: Current board
# Output: N/A
 
def drawBoard(board):

	for i in range(7):
		print " "
		for j in range(7):
			print board[i][j],


# Calculates evaluation value for determining optimal choice past cutoff level
# Looks through each possible winning sequence and evaluates availability for player and opponent
# Gives each sequence a weight based on this availabilty when adding to overall utility for board
# Input: Current board, player color
# Output: Evaluation value

def evaluation(board, color):

	utility = 0

	if color == 'B':
		bad_color = 'R'
	else:
		bad_color = 'B'

	for sequence in seq.sequences():

		good_count = 0
		bad_count = 0

		available = 1
		for (x, y) in sequence:
			if board[x][y] == color:
				good_count = good_count + 1
			elif board[x][y] == bad_color:
				available = 0
				break

		victory = 0
		if not(available):
			utility = utility + 0
		elif available and good_count == 0: # sequence still available for player color
			utility = utility + 16
		elif available and good_count == 1: # open sequence has one stone of player color
			utility = utility + 32
		elif available and good_count == 2: # open sequence has two stones of player color
			utility = utility + 48
		elif available and good_count == 3: # open sequence has three stones of player color
			utility = utility + 64
		elif available and good_count == 4: # open sequence has four stones of player color
			utility = utility + 10000
		elif available and good_count == 5: # a winning board
			utility = utility + 1000000

		available = 1
		for (x, y) in sequence:
			if board[x][y] == bad_color:
				bad_count = bad_count + 1
			elif board[x][y] == color:
				available = 0
				break

		defeat = 0
		if not(available):
			utility = utility + 0
		elif available and bad_count == 0: # sequence still available for player color
			utility = utility + 0
		elif available and bad_count == 1: # open sequence has one stone of player color
			utility = utility - 24
		elif available and bad_count == 2: # open sequence has two stones of player color
			utility = utility - 40
		elif available and bad_count == 3: # open sequence has three stones of player color
			utility = utility - 56
		elif available and bad_count == 4: # open sequence has four stones of player color
			utility = utility - 72
		elif available and bad_count == 5: # a losing board
			utility = utility - 1000000

	return utility


# Returns a list of actions (open spaces) available on board
# Input: Current board
# Output: List of empty coordinates

def getActions(board):

	actions = []

	for i in range(7):
		for j in range(7):
			if board[i][j] == ' ':
				actions.append([i, j])

	return actions


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


# Checks if a winning move has been made
# Inputs: Current board, player color
# Output: True or False

def checkVictory(board, color):

	for sequence in seq.sequences():

		count = 0
		for (x, y) in sequence:
			if board[x][y] == color:
				count = count + 1

		if count == 5:
			return 1

	return 0


# Finds the maximum of min values at next level in game tree
# Also updates alpha accordingly
# Inputs: Current board, level of tree, current alpha/beta, color to evaluate
# Output

def maxValue(board, level, alpha, beta, color, explored):

	if level == 3:
		if color == 'B':
			return [evaluation(board, 'R'), [0, 0], explored]
		else:
			return [evaluation(board, 'B'), [0, 0], explored]

	actions = []
	actions = getActions(board)

	best_score = -1
	best_action = actions[0]

	if color == 'B':
		next_color = 'R'
	else:
		next_color = 'B'

	for action in actions:
		explored = explored + 1
		new_board = updateBoard(board, action, color)
		old_score = best_score
		min_val =  minValue(new_board, level + 1, alpha, beta, next_color, explored)
		best_score = max(best_score, min_val[0])
		explored = min_val[2]
		if best_score != old_score:
			best_action = action
		if best_score >= beta:
			return [best_score, best_action, explored]
		alpha = max(alpha, best_score)

	return [best_score, best_action, explored]


# Finds the minimum of max values at next level in game tree
# Also updates beta accordingly
# Inputs: Current board, level of tree, current alpha/beta, color to evaluate
# Output

def minValue(board, level, alpha, beta, color, explored):

	if level == 3:
		if color == 'R':
			return [evaluation(board, 'B'), [0, 0], explored]
		else:
			return [evaluation(board, 'R'), [0, 0], explored]

	actions = []
	actions = getActions(board)

	best_score = 1000000
	best_action = actions[0]

	if color == 'B':
		next_color = 'R'
	else:
		next_color = 'B'

	for action in actions:
		explored = explored + 1
		new_board = updateBoard(board, action, color)
		old_score = best_score
		max_val = maxValue(new_board, level + 1, alpha, beta, next_color, explored)
		best_score = min(best_score, max_val[0])
		explored = max_val[2]
		if best_score != old_score:
			best_action = action
		if best_score <= alpha:
			return [best_score, best_action, explored]
		beta = min(beta, best_score)

	return [best_score, best_action, explored]


# Runs minimax algorithm (with alpha-beta pruning) on board to determine 'best' move
# Input: Current board
# Output: Optimal position for player to place stone

def minimax(board, color):

	return maxValue(board, 0, -1000000, 1000000, color, 0)
