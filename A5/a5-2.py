import sqlite3, datetime

# sqlite用モジュールのインポート
from flask import Flask, g, render_template

# グローバル変数gのインポート


app = Flask(__name__)


def get_db():
    if "db" not in g:
        # gはリクエストごとに用意されるFlaskのオブジェクト
        # gに"db"が含まれていない場合にデータベースへの接続が行われる．
        g.db = sqlite3.connect("a5-2.db")
        # データベースへの接続
    return g.db


def close_db():
    db = g.pop("db", None)
    # gから"db"を取り出す．
    if db is not None:
        # gに"db"が含まれていた場合にはデータベースとの接続を終了する．
        db.close()
        # データベースの接続終了


@app.route("/", methods=["GET"])
def database():
    db = get_db()
    cur = db.execute("SELECT * FROM events")
    table = cur.fetchall()
    close_db()
    schema = ["ID", "name", "place"]
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    return render_template(
        "a5-2.html",
        title="DBテスト",
        schema=schema,
        table=table,
        today=today,
    )

@app.route("/", methods=["POST"])
def insert():
    db = get_db()
    name = request.form["name"]
    place = request.form["place"]
    db.execute("INSERT INTO events(name, place) VALUES(?, ?)", (name, place))
    db.commit()
    cur = db.execute("SELECT * FROM events")
    table = cur.fetchall()
    close_db()
    schema = ["ID", "name", "place"]
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    return render_template(
        "a5-2.html",
        title="DBテスト",
        schema=schema,
        table=table,
        today=today,
    )


if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost")

