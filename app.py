from crypt import methods
import sqlite3

from flask import Flask , render_template

app = Flask(__name__)

app.secret_key = "kari-time"


@app.route("/")
def template():
    return render_template("base.html")



@app.route("/item_list" , methods = ["GET"])
def item_list():
  # DBへの接続と、データを全部取ってくる
  #conn = sqlite3に接続して
  conn = sqlite3.connect("Item.db")
  #DBを操作できるようにして
  c = conn.cursor()
  # ()内のSQL文を実行
  c.execute("SELECT item_name, explain FROM Item;")
  # タスクのデータを入れる配列を定義
  item_list = []  #配列の初期化
  for row in c.fetchall(): #row=新しく作った変数
      item_list.append({"item":row[0],"explain":row[1]})
  c.close
  print(item_list)
  return render_template("item_list.html",item_list = item_list)



@app.route("/item" , methods = ["GET"])
def item():
  # DBへの接続と、データを全部取ってくる
  #conn = sqlite3に接続して
  conn = sqlite3.connect("Item.db")
  #DBを操作できるようにして
  c = conn.cursor()
  # ()内のSQL文を実行
  c.execute("SELECT item_name, price, abv, type, explain FROM Item where id = 1;")
  # タスクのデータを入れる配列を定義
  item = []  #配列の初期化
  for row in c.fetchall(): #row=新しく作った変数
      item.append({"item":row[0],"price":row[1],"abv":row[2],"type":row[3],"explain":row[4]})
  c.close
  print(item)
  return render_template("item.html", item = item)












if __name__ == "__main__":

    app.run(debug=True)