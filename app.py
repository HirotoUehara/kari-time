import sqlite3

from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("base.html")





@app.route("/item_list")
def index():
    return render_template("item_list.html")


    












if __name__ == "__main__":

    app.run()