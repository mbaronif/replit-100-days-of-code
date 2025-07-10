from flask import Flask
import datetime

app = Flask(__name__, static_url_path="/static")

@app.route('/')
def index():
    page = f"""<html><body>
    <p><a href="/home">Go home</a></p>
    </body></html>"""
    return page

@app.route("/home")
def home():
    today = datetime.date.today()
    page = """<html></html>""" # Add the page's HTML code between the 3 double quotes pair
    return page

app.run(host="0.0.0.0", port=81)
