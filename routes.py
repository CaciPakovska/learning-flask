from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
  return "<h2>Zdravo beeeee!!!!!</h2><br><img width=300 height=600 src='static\img\\filipche.jpg'/>"

@app.route("/about")
def about():
  return "Aloha!"

if __name__ == "__main__":
  app.run(host='0.0.0.0')