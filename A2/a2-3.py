from flask import Flask, render_template

app = Flask(__name__)

id = [1, 2, 3, 4, 5]
name = ["りんごfes1", "りんごfes2", "りんごfes3", "りんごfes4", "りんごfes5"]
year = [2020, 2021, 2022, 2023, 2024]
place = ["青森", "青森", "青森", "青森", "青森"]


@app.route("/id<num>")
# ルートがidで始まる場合に呼び出される．idより後の部分は変数numに代入される．
def page(num):
    try:
        Name="これは{}のページです．".format(name[int(num) - 1])
        Year = "これは{}年度のページです．".format(year[int(num) - 1])
        Place = "開催地は{}です．".format(place[int(num) - 1])
    except Exception:
        # numの値が正しくない場合は例外が生じる．
        message = "ページは見つかりませんでした"
    return render_template("a2-3.html", title="表示テスト", name=Name, year=Year, place=Place)


if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost", port=5000)
