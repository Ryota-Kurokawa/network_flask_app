from flask import Flask, render_template, session

app = Flask(__name__)
app.secret_key = "abc"
# セッション変数を利用するためには秘密鍵(secret_key)の登録が必要


# @app.route("/")
# def count_session():
#     if "count" in session:
#         # "count"という名前のセッション変数を探す．
#         count = session["count"]
#         # あれば変数countに代入する
#     else:
#         # なければ変数countを1に初期化する．
#         count = 1

#     message = "あなたはこのサイトに{}回アクセスしました．".format(count)
#     session["count"] = count + 1
#     # セッション変数を1増やして，更新する．
#     return render_template("a4-1.html", title="セッション変数", message=message)

# @app.route("/", methods=["POST"])
# def reset_session():
#     session.pop("count", None)
#     # セッション変数を削除する．
#     return render_template("a4-1.html", title="セッション変数", message="セッション変数を削除しました．")


# if __name__ == "__main__":
#     app.debug = True
#     app.run(host="localhost")

# import datetime

from flask import Flask, render_template, request

app = Flask(__name__)

events = {
    1: {"Id": "1", "Name": "りんごfes1", "Year": "2020", "Place": "青森"},
    2: {"Id": "2", "Name": "りんごfes2", "Year": "2021", "Place": "青森"},
    3: {"Id": "3", "Name": "りんごfes3", "Year": "2022", "Place": "青森"},
    4: {"Id": "4", "Name": "りんごfes4", "Year": "2023", "Place": "青森"},
    5: {"Id": "5", "Name": "りんごfes5", "Year": "2024", "Place": "青森"}
}

@app.route("/", methods=["GET"])
# GETメソッドでのアクセスは以下が実行される．
def input():
  serarched_id = request.cookies.get("id")
  return render_template("a2-4in.html", title="フォームの利用", id=serarched_id)


@app.route("/", methods=["POST"])
# POSTメソッドでのアクセスは以下が実行される．
def output():
    # dt = datetime.datetime.now()
    # name = request.form["name"]
    # フォームからnameデータを取得する．
    try:
        Id = int(request.form["id"])
        Name = "これは{}のページです．".format(events[int(request.form["id"])]['Name'])
        Year = "これは{}年度のページです．".format(events[int(request.form["id"])]['Year'])
        Place = "開催地は{}です．".format(events[int(request.form["id"])]['Place'])
        # # フォームからageデータを取得し，整数化して，生年を計算する．
        # message = "{}さんが生まれたのは{}年かその前の年．".format(name, birth_year)
    except Exception:
        message = "年齢が正しくありません．"
    return render_template("a2-4out.html", title="フォームの利用",id = Id, name=Name, year=Year, place=Place)
    response = make_response(render_template("a2-4out.html", title="フォームの利用",id = Id, name=Name, year=Year, place=Place))
    response.set_cookie("id", str(Id))
    return response


if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost")
