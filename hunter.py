'''
Solve the word hunt challenge
'''
import sys
dir_map = {'DIAG_LEFT_DOWN': (1, -1), 'RIGHT': (0, 1), 'DIAG_RIGHT_DOWN': (1, 1), 'UP': (-1, 0), 'DOWN': (1, 0), 'DIAG_RIGHT_UP': (-1, 1), 'DIAG_LEFT_UP': (-1, -1), 'LEFT': (0, -1)}

def build_frequency_table(word_maze):
	freq_table = {}
	for row_index, row in enumerate(word_maze):
		for col_index, col in enumerate(row):
			if col not in freq_table:
				freq_table[col] = {'count' : 1, 'positions' : [(row_index, col_index)]}
			else:
				freq_table[col]['count'] += 1
				freq_table[col]['positions'].append((row_index, col_index))
	return freq_table

def get_maze_from_file(filename):
	with open(filename) as input_file:
		file_contents = input_file.readlines()
		file_contents = [x.strip() for x in file_contents]
		word_maze = []
		for each in file_contents:
			row = each.split()
			word_maze.append(row)
		SIZE = len(word_maze[0])
		return word_maze

def get_words_to_find_from_file(filename):
	with open(filename) as input_file:
		file_contents = input_file.readlines()
		words_to_find = [x.strip() for x in file_contents]
		return words_to_find

def grid_solver_impl(word_maze, word_to_find, start_position, solve_backwards):
	max_cols, max_rows = len(word_maze[0]), len(word_maze)
	if solve_backwards == True:
		word_to_find = word_to_find[::-1]
	letter = word_to_find[0]
	length_of_word = len(word_to_find) - 1
	for direction in dir_map:
		dir_offsets = dir_map[direction]
		row_offset, col_offset = dir_offsets[0], dir_offsets[1]
		cur_row, cur_col = start_position[0], start_position[1]
		for l_index, letter in enumerate(word_to_find):
			if (0 <= cur_col < max_cols) and (0 <= cur_row < max_rows):
				if letter == word_maze[cur_row][cur_col]:
					if l_index == length_of_word:
						return True, direction
					cur_row = cur_row + row_offset
					cur_col = cur_col + col_offset
				else:
					break
			else:
				break
	return False, 'NONE'

def grid_solver(word_maze, word_list, freq_table):
	word_answers = {}
	words_not_found = word_list[:]
	for word_to_find in word_list:
		solve_backwards = False
		start_letter = word_to_find[0]
		end_letter = word_to_find[-1]
		if freq_table[start_letter]['count'] > freq_table[end_letter]['count']:
			letter = end_letter
			solve_backwards = True
		else:
			letter = start_letter
		positions = freq_table[letter]['positions']
		for each_position in positions:
			found, direction = grid_solver_impl(word_maze, word_to_find, each_position, solve_backwards)
			if found == True:
				words_not_found.remove(word_to_find)
				print 'Found word', word_to_find, 'at position: ', each_position, 'in direction: ', direction
				word_to_find = word_to_find.encode('ascii', 'ignore')
				word_answers[word_to_find] = { 
					'word' : word_to_find,
					'row_position': each_position[0],
					'col_position': each_position[1],
					'direction' : direction,
					'length' : len(word_to_find),
					'letters' : list(word_to_find)
					}
				break

	return words_not_found, word_answers

def construct_new_maze(word_maze, word_answers):
	answer_list = []
	answer_dict = {}

	for each_word in word_maze:
		answer_row = []
		for each_letter in each_word:
			answer_dict = {
				'letter' : each_letter,
				'color' : 'white'
			}
			answer_row.append(answer_dict)
		answer_list.append(answer_row)


	for each_answer, each_answer_dict in word_answers.items():
		row = each_answer_dict['row_position']
		col = each_answer_dict['col_position']
		direction = each_answer_dict['direction']
		direction_offsets = dir_map[direction]
		length = each_answer_dict['length']
		row_offset, col_offset = direction_offsets[0], direction_offsets[1]
		answer_dict = answer_list[row][col]
		
		#print answer_dict
		answer_dict['color'] = 'yellow'

		#color in the direction for as long as length
		for i in range(0, length-1):
			row = row + row_offset
			col = col + col_offset
			#print row, col, direction
			answer_list[row][col]['color'] = 'yellow'
			print answer_list[row][col]
		each_answer_dict = answer_dict
		

	for a in answer_list:
		for b in a:
			print b

	# for row in answer_list:
	# 	for col in row:
	# 		for k, v in col.items():
	# 			print k
	# 			print v

	return answer_list

def start(word_maze, word_list):
		
	word_maze = get_maze_from_file('new_maze.txt')
	word_list = get_words_to_find_from_file('new_words.txt')
	freq_table = build_frequency_table(word_maze)
	words_not_found, word_answers = grid_solver(word_maze, word_list, freq_table)
	if len(words_not_found) != 0:
		print 'Words not found = ', words_not_found
	new_maze = construct_new_maze(word_maze, word_answers)
	return words_not_found, word_answers, new_maze


#start(None, None)
