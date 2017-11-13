'''
Write a mini server to service word hunt challenge
'''

from flask import Flask, flash, redirect, render_template, request, session, abort
 
app = Flask(__name__)
 
@app.route('/')
def index():
    return render_template(
        'index.html')

#Handle post request from user here
@app.route('/post_puzzle', methods=['POST'])
def post_puzzle():
	print request.data
	print request.form
	return "hello from post_puzzle"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
