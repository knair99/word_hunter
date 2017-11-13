'''
Write a mini server to service word hunt challenge
'''

from flask import Flask, flash, redirect, render_template, request, session, abort, jsonify
import json
import hunter as wh
 
app = Flask(__name__)
 
@app.route('/')
def index():
    return render_template(
        'index.html')

#Handle post request from user here
@app.route('/post_puzzle', methods=['POST'])
def post_puzzle():
	text_area_maze = request.form['maze_text_area']
	word_maze = text_area_maze.split('\r\n') 
	word_maze = [ ''.join(x.split()) for x in word_maze]
	word_maze = [list(x) for x in word_maze]

	text_area_words = request.form['words_text_area']
	word_list = text_area_words.split('\r\n')
	word_list = [''.join(x.split()) for x in word_list]
	#now call into solver
	words_not_found, word_answers, new_maze, dir_colors = wh.start(word_maze, word_list)

	#Send data back
	web_response = {}
	web_response['words_not_found'] = words_not_found
	web_response['word_answers'] = word_answers
	web_response['new_maze'] = new_maze
	web_response['direction_colors'] = dir_colors
	return jsonify(web_response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
