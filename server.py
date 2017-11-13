'''
Write a mini server to service word hunt challenge
'''

from flask import Flask, flash, redirect, render_template, request, session, abort, jsonify
import json
 
app = Flask(__name__)
 
@app.route('/')
def index():
    return render_template(
        'index.html')

#Handle post request from user here
@app.route('/post_puzzle', methods=['POST'])
def post_puzzle():
	print request.form
	print request.data

	#Send data back
	web_response = {}
	web_response['solved'] = ['hello', 'list']
	return jsonify(web_response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
