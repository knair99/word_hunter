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
				break

	return words_not_found

def main():
	print 'Usage: hunter.py [MAZE_FILENAME] [WORDS_TO_FIND_FILENAME]'
	if len(sys.argv) <= 2:
		print 'Missing input maze file and/or words file'
		print ' - using default examples'
		maze_filename, words_filename = 'maze.txt', 'words.txt'
	else:
		maze_filename, words_filename = sys.argv[1], sys.argv[2]
	
	word_maze = get_maze_from_file(maze_filename)
	word_list = get_words_to_find_from_file(words_filename)
	freq_table = build_frequency_table(word_maze)
	words_not_found = grid_solver(word_maze, word_list, freq_table)
	if len(words_not_found) != 0:
		print 'Words not found = ', words_not_found


#system
if __name__ == '__main__':
    sys.exit(main())