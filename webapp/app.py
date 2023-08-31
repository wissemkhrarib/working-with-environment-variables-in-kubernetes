import os
from flask import Flask, render_template

app = Flask(__name__)
username = os.environ.get("USERNAME")

@app.route('/')
def hello_world():
    print(username)
    return render_template('hello.html', username=username)

if __name__ == "__main__":
  app.run(debug=True, port=5000, host='0.0.0.0')