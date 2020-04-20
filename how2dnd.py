from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def home():
	data = {}
	with open('classes.json', 'r') as f:
		data = json.loads(f.read())
	return render_template('home.html', classes=data.keys(), data=data, data_text=json.dumps(data), choice=None)

@app.route('/<choice>')
def home_choice(choice):
	data = {}
	with open('classes.json', 'r') as f:
		data = json.loads(f.read())
	return render_template('home.html', classes=data.keys(), data=data, data_text=json.dumps(data), choice=choice)

if __name__ == "__main__":
	app.run()