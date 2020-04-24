
from disaster_tweet_indentification import *

from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__, template_folder = './')
app.debug = True
app.secret_key = 'development key'

@app.route ("/disaster_tweets")
def home():
	return render_template ("home.html")

@app.route ("/get_pred", methods=["POST"])
def get_prediction():
	print (request.data)
	sent_tweet = str(request.data.decode('utf-8'))
	val = get_pred (sent_tweet)
	print (val)
	if val == [True]:
		return "yes"
	else:
		return "no"

@app.route ("/temp")
def temp():
	return render_template ("temp.html")

app.run ()