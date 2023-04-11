from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
   'id' : 1,
   'title' : 'Data Analyst',
   'location': 'kigango,kenya',
   'salary': '$20000'
  },
  {
  'id' : 2,
   'title' : 'Data Science',
   'location': 'kigali,Rwanda',
   'salary': '$40000'
  },
  {'id' : 3,
   'title' : 'Frontend Engineer',
   'location': 'Remote',
   'salary': '$120000' 
  }, 

  {'id' : 4,
   'title' : 'Backend Engineer',
   'location': 'Thika,kenya',
   'salary': '$20000'
  },
]

@app.route("/")
def hello_manu():
   return render_template('home.html',jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
   return jsonify(JOBS)

if __name__=="__main__":
  app.run(host='0.0.0.0', debug=True )