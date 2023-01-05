from flask import render_template , Flask , jsonify ,request
import sqlite3
DB_PATH='teams.db'
app = Flask(__name__, static_folder='static')
app.template_folder = 'templates'

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/api/teams')
def getteams():
    team=[{'id':1,'name':"PSG"},{'id':2,'name':"liverpool"},{'id':3,'name':"Man City"}]
    return jsonify(team)
#@app.route('/search', methods=['POST'])
#def getteam():
#    team=[{'id':1,'name':"PSG","Location":"France"},{'id':2,'name':"liverpool","Location":"England"},{'id':3,'name':"Man City","Location":"England"}]
#    result =[]
#    input_req=request.json['searchTerm']
#    for teams in team:
#        if input_req.lower() in teams['name'].lower():
#            result.append(teams)
            
 #   return result  

@app.route('/search', methods=['POST'])
def search():
  search_term = request.json['searchTerm']
  results = search_teams(search_term)
  return jsonify(results)

def search_teams(search_term):
    conn = sqlite3.connect(DB_PATH)
    c= conn.cursor()
    c.execute("SELECT * FROM teams WHERE name LIKE ?", (f'%{search_term}%',))
    results = c.fetchall()
    conn.close()
    return results
    
if __name__ == "__main__":
    app.run(host="0.0.0.0")
