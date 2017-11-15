from flask import Flask, flash, redirect, render_template, request, session, abort, jsonify
import json
import hunter as wh
 
app = Flask(__name__)
 
class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv

@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

@app.route('/')
def index():
    return render_template(
        'index.html')

@app.route('/demo')
def demo():
	return render_template('demo.html')

#Handle post request from user here
@app.route('/post_puzzle', methods=['POST'])
def post_puzzle():
	text_area_maze = request.form['maze_text_area']
	if len(text_area_maze) == 0:
		raise InvalidUsage('Error - fill maze up with at least one row', status_code=410)
	word_maze = text_area_maze.split('\r\n') 
	word_maze = [ ''.join(x.split()) for x in word_maze]
	word_maze = [list(x) for x in word_maze]
	word_maze = [x for x in word_maze if len(x) != 0]

	if not all(len(i) == len(word_maze[0]) for i in word_maze):
		raise InvalidUsage('Error - not all columns have same length in word maze', status_code=410)

	text_area_words = request.form['words_text_area']
	if len(text_area_words) == 0:
		raise InvalidUsage('Error - enter at least one word to find', status_code=410)

	word_list = text_area_words.split('\r\n')
	word_list = [''.join(x.split()) for x in word_list]
	word_list = [x for x in word_list if len(x) != 0]
	#now call into solver
	words_not_found, word_answers, new_maze, dir_colors = wh.start(word_maze, word_list)
	print word_list

	#Send data back
	web_response = {}
	web_response['words_not_found'] = words_not_found
	web_response['word_answers'] = word_answers
	web_response['new_maze'] = new_maze
	web_response['dir_colors'] = json.dumps(dir_colors)
	return jsonify(web_response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
