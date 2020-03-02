from flask import Flask
app = Flask(__name__)
 
@app.route("/")
def hello():
    return "Demat d'an holl, ..., kenavo !"
 
app.run()
