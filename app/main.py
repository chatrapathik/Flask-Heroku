from flask import Flask

app = Flask(__name__)


@app.route("/")
def home_view():
    return "<h1>Welcome Chatra!!!</h1>"


@app.route("/api/chatra")
def view():
    return dict(success=True, message="Hello Chatra!!!")
