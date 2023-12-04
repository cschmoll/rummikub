import json, random
from flask import Flask, render_template, jsonify, request
from database import engine, load_jobs_from_db, load_job_from_db, Session
from models import Base, Jobs, Application

#https://careers-website-v2.cschmoll.repl.co/
app = Flask(__name__)

@app.route("/")
def hello_world():

  session = Session()

  jobs = []
  for job in session.query(Jobs).all():
    jobs.append(job.to_dict())

  #return render_template('home.html', jobs=jobs)
  return jsonify(jobs)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
  #app.run(host='0.0.0.0', port=random.randint(2000, 9000))  # Dubugger