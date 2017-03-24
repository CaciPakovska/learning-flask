from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
  return "Hi!"

@app.route("/about")
def about():
  return "Aloha!"

if __name__ == "__main__":
  app.run(debug=True)