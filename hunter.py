'''
Solve the word hunt challenge
'''
import sys

def build_frequency_table(word_maze):
	freq_table = {}
	for row in word_maze:
		for col in row:
			if col not in freq_table:
				freq_table[col] = 1
			else:
				freq_table[col] += 1
	return freq_table

def get_maze_from_file(filename):
	with open(filename) as input_file:
		file_contents = input_file.readlines()
		#Take off new lines
		file_contents = [x.strip() for x in file_contents]
		word_maze = []
		#Convert to list of lists
		for each in file_contents:
			row = each.split()
			word_maze.append(row)
		return word_maze

def get_words_to_find_from_file(filename):
	with open(filename) as input_file:
		file_contents = input_file.readlines()
		#Take off new lines
		words_to_find = [x.strip() for x in file_contents]
		return words_to_find


def main():
	print 'Usage: word_hunter.py [MAZE_FILENAME] [WORDS_TO_FIND_FILENAME]'
	
	if len(sys.argv) <= 2:
		print 'No input given - using examples'
		maze_filename 	= 'maze.txt'
		words_filename 	= 'words.txt'

	else:
		maze_filename 	= sys.argv[1]
		words_filename 	= sys.argv[2]

	word_maze = get_maze_from_file(maze_filename)
	word_list = get_words_to_find_from_file(words_filename)
	print word_list
	freq_table = build_frequency_table(word_maze)




#system
if __name__ == '__main__':
    sys.exit(main())