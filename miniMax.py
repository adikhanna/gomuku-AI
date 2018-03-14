import sys
import time
import copy
import seq
import reflexAgent
import alphaBeta


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
		elif available and bad_count == 0: # sequence still available for opponent color
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


# Finds the maximum of min values to force the opponent to choose
# Used in recusrive minimax algorithm
# Inputs: Current board, level of tree, player color, nodes expanded thus far
# Outputs: Best action, new total of nodes expanded

def maxValue(board, level, color, explored):

	if level == 3:
		if color == 'R':
			return [evaluation(board, 'B'), explored]
		else:
			return [evaluation(board, 'R'), explored]

	if color == 'B':
		next_color = 'R'
	else:
		next_color = 'B'

	actions = []
	actions = getActions(board)

	best_score = -1

	for action in actions:
		explored = explored + 1
		new_board = updateBoard(board, action, color)
		min_val = minValue(new_board, level + 1, next_color, explored)
		score = min_val[0]
		explored = min_val[1]
		if score > best_score:
			best_action = action
			best_score = score

	return [best_score, explored]


# Finds the minimum of max values to force the opponent to choose
# Used in recusrive minimax algorithm
# Inputs: Current board, level of tree, player color, nodes expanded thus far
# Outputs: Best action, new total of nodes expanded

def minValue(board, level, color, explored):

	if level == 3:
		if color == 'R':
			return [evaluation(board, 'B'), explored]
		else:
			return [evaluation(board, 'R'), explored]

	if color == 'B':
		next_color = 'R'
	else:
		next_color = 'B'

	actions = []
	actions = getActions(board)

	best_score = 1000000

	for action in actions:
		explored = explored + 1
		new_board = updateBoard(board, action, color)
		max_val = maxValue(new_board, level + 1, next_color, explored)
		score = max_val[0]
		explored = max_val[1]
		if score < best_score:
			best_action = action
			best_score = score

	return [best_score, explored]


# Runs minimax algorithm on board to determine 'best' move
# Input: Current board
# Output: Optimal position for player to place stone

def minimax(board, color):

	actions = []
	actions = getActions(board)

	best_action = actions[0]
	best_score = -1

	explored = 0

	if color == 'B':
		next_color = 'R'
	else:
		next_color = 'B'

	for action in actions:
		explored = explored + 1
		new_board = updateBoard(board, action, color)
		min_val = minValue(new_board, 1, next_color, explored)
		score = min_val[0]
		explored = min_val[1]
		if score > best_score:
			best_action = action
			best_score = score

	return [best_action, explored]


# Runs algorithm matchup specified by command line argument
# 1 - alpha-beta vs. minimax
# 2 - minimax vs. alpha-beta
# 3 - alpha-beta vs. reflex
# 4 - reflex vs. alpha-beta
# 5 - reflex vs. minimax
# 6 - minimax vs. reflex
# Input: Matchup selection
# Output: Consecutive actions and resulting boards

def startMatch(matchup):

	game_board = [[' ' for i in range(7)] for j in range(7)] # empty board to begin	


	if matchup == '1': # Alpha-Beta vs. Minimax
	
		game_board[3][3] = 'R' # first move by alphabeta, first choice is middle position
		game_board[6][0] = 'B' # first move by minimax, first choice is bottom left corner

		action = alphaBeta.minimax(game_board, 'R') # alphabeta first
		print "\n", action[1]
		print "Nodes expanded: ", action[2]
		new_board = updateBoard(game_board, action[1], 'R')
		drawBoard(new_board)

		for i in range(46): # take turns until a player wins

			if i % 2 == 0:
				action = minimax(new_board, 'B')
				print "\n", action[0]
				print "Nodes expanded: ", action[1]
				new_board = updateBoard(new_board, action[0], 'B')
				drawBoard(new_board)
				if checkVictory(new_board, 'B'):
					print "Second player Minimax agent (blue) wins!"
					return
			else:
				action = alphaBeta.minimax(new_board, 'R')
				print "\n", action[1]
				print "Nodes expanded: ", action[2]
				new_board = updateBoard(new_board, action[1], 'R')
				drawBoard(new_board)
				if checkVictory(new_board, 'R'):
					print "First player Alpha-Beta agent (red) wins!"
					return			

	elif matchup == '2': # Minimax vs Alpha-Beta
	
		game_board[3][3] = 'R'	# first move by minimax, first choice is middle position
		game_board[6][0] = 'B'  # first move by alphabeta, first choice is bottom left corner

		action = minimax(game_board, 'R') # minimax first
		print "\n", action[0]
		print "Nodes expanded: ", action[1]
		new_board = updateBoard(game_board, action[0], 'R')
		drawBoard(new_board)

		for i in range(46): # take turns until a player wins

			if i % 2 == 0:
				action = alphaBeta.minimax(new_board, 'B')
				print "\n", action[1]
				print "Nodes expanded: ", action[2]
				new_board = updateBoard(new_board, action[1], 'B')
				drawBoard(new_board)
				if checkVictory(new_board, 'B'):
					print "Second player Alpha-Beta agent (blue) wins!"
					return
			else:
				action = minimax(new_board, 'R')
				print "\n", action[0]
				print "Nodes expanded: ", action[1]
				new_board = updateBoard(new_board, action[0], 'R')
				drawBoard(new_board)
				if checkVictory(new_board, 'R'):
					print "First player Minimax agent (red) wins!"
					return

	elif matchup == '3': # Alpha-Beta vs Reflex

		game_board[3][3] = 'R' # first move by alphabeta, first choice is middle positon
		game_board[6][0] = 'B' # first move by reflex, first choice is bottom left corner

		action = alphaBeta.minimax(game_board, 'R') # alphabeta first
		print "\n", action[1]
		print "Nodes expanded: ", action[2]
		new_board = updateBoard(game_board, action[1], 'R')
		drawBoard(new_board)

		for i in range(46): # take turns until a player wins

			if i % 2 == 0:
				action = reflexAgent.reflex_agent(new_board, 'B')
				print "\n", action
				new_board = updateBoard(new_board, action, 'B')
				drawBoard(new_board)
				if checkVictory(new_board, 'B'):
					print "Reflex agent (blue) wins!"
					return
			else:
				action = alphaBeta.minimax(new_board, 'R')
				print "\n", action[1]
				print "Nodes expanded: ", action[2]
				new_board = updateBoard(new_board, action[1], 'R')
				drawBoard(new_board)
				if checkVictory(new_board, 'R'):
					print "Alpha-Beta agent (red) wins!"
					return			

	elif matchup == '4': # Reflex vs Alpha-Beta
		
		game_board[6][0] = 'R' # first move by reflex, first choice is bottom left corner
		game_board[3][3] = 'B' # first move by alphabeta, first choice is middle position

		action = reflexAgent.reflex_agent(game_board, 'R') # reflex first
		print "\n", action
		new_board = updateBoard(game_board, action, 'R')
		drawBoard(new_board)

		for i in range(46): # take turns until a player wins

			if i % 2 == 0:
				action = alphaBeta.minimax(new_board, 'B')
				print "\n", action[1]
				print "Nodes expanded: ", action[2]
				new_board = updateBoard(new_board, action[1], 'B')
				drawBoard(new_board)
				if checkVictory(new_board, 'B'):
					print "Alpha-Beta agent (blue) wins!"
					return
			else:
				action = reflexAgent.reflex_agent(new_board, 'R')
				print "\n", action
				new_board = updateBoard(new_board, action, 'R')
				drawBoard(new_board)
				if checkVictory(new_board, 'R'):
					print "Reflex agent (red) wins!"
					return

	elif matchup == '5': # Reflex vs Minimax

		game_board[6][0] = 'R' # first move by reflex, first choice is bottom left corner
		game_board[3][3] = 'B' # first move by minimax, first choice is middle position

		action = reflexAgent.reflex_agent(game_board, 'R') # reflex first
		print "\n", action
		new_board = updateBoard(game_board, action, 'R')
		drawBoard(new_board)

		for i in range(46): # take turns until a player wins

			if i % 2 == 0:
				action = minimax(new_board, 'B')
				print "\n", action[0]
				print "Nodes expanded: ", action[1]
				new_board = updateBoard(new_board, action[0], 'B')
				drawBoard(new_board)
				if checkVictory(new_board, 'B'):
					print "Minimax agent (blue) wins!"
					return
			else:
				action = reflexAgent.reflex_agent(new_board, 'R')
				print "\n", action
				new_board = updateBoard(new_board, action, 'R')
				drawBoard(new_board)
				if checkVictory(new_board, 'R'):
					print "Reflex agent (red) wins!"
					return

	elif matchup == '6': # Minimax vs Reflex
		
		game_board[3][3] = 'R' # first move by minimax, first choice is middle positon
		game_board[6][0] = 'B' # first move by reflex, first choice is bottom left corner

		action = minimax(game_board, 'R') # minimax first
		print "\n", action[0]
		print "Nodes expanded: ", action[1]
		new_board = updateBoard(game_board, action[0], 'R')
		drawBoard(new_board)

		for i in range(46): # take turns until a player wins

			if i % 2 == 0:
				action = reflexAgent.reflex_agent(new_board, 'B')
				print "\n", action
				new_board = updateBoard(new_board, action, 'B')
				drawBoard(new_board)
				if checkVictory(new_board, 'B'):
					print "Reflex agent (blue) wins!"
					return
			else:
				action = minimax(new_board, 'R')
				print "\n", action[0]
				print "Nodes expanded: ", action[1]
				new_board = updateBoard(new_board, action[0], 'R')
				drawBoard(new_board)
				if checkVictory(new_board, 'R'):
					print "Minimax agent (red) wins!"
					return		


startMatch(sys.argv[1])

# References:
# http://giocc.com/concise-implementation-of-minimax-through-higher-order-functions.html