# flask --app data_server run
from flask import Flask, render_template, request
import json

app = Flask(__name__, static_url_path='', static_folder='static')

@app.route('/')
def index():
    f = open("data/refined_data.json", "r")
    data = json.load(f)
    f.close()
    states = []
    electoral_votes = {}
    for state in data:
        states.append(state["Location"])
        electoral_votes[state["Abbreviation"]] = {
            "Total": state["Total Electoral Votes"],
            "Biden": state["Electoral Votes for Biden"],
            "Trump": state["Electoral Votes for Trump"]
        }
    return render_template('index.html', states=sorted(states), electoral_votes=electoral_votes, data=data)

@app.route('/about')
def about():
    f = open("data/refined_data.json", "r")
    data = json.load(f)
    f.close()
    states = []
    for state in data:
        states.append(state["Location"])
    return render_template('about.html', states=sorted(states))

@app.route('/state')
def state():
    location = request.args.get('name').lower()
    f = open("data/refined_data.json", "r")
    data = json.load(f)
    f.close()
    state_info = None
    states = set()
    for state in data:
        states.add(state['Location'])
        if state['Location'].lower() == location:
            state_info = state
    if not state_info:
        return "State not found.", 404
    return render_template('state.html', state=state_info, states=sorted(states))

def navbar():
    location = request.args.get('name').lower()
    f = open("data/refined_data.json", "r")
    data = json.load(f)
    f.close()
    states = set()
    for state in data:
        states.add(state["Location"])
    return render_template('navbar.html', state=location, data=data, states=sorted(states))

if __name__ == '__main__':
    app.run(debug=True)
