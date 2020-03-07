from flask import Flask
app = Flask(__name__)
 
@app.route("/")
def hello():
    return "<h1>Demat d'an holl, ... ;<br><br>Kenavo !</h1>"
 
app.run()
