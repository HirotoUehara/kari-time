import sqlite3

from flask import Flask , render_template

app = Flask(__name__)

app.secret_key = "kari-time"


@app.route("/kari-time")
def template():
    return render_template("base.html")





@app.route("/item_list" , methods = ["GET"])
def item():
    return render_template("item_list.html")

    #『sqlite3でItem.dbに接続する』ことを変数connに代入する
    conn = sqlite3.connect("Item.db")
    #『sqlite3に接続して、dbを操作できるようにしてね』ということを変数cに代入
    c = conn.cursor()
    #()内のSQL文を実行(execute)してね
    c.execute("SELECT * FROM Item;")
    #Item.dbとの接続を終了する
    c.close()












if __name__ == "__main__":

    app.run()