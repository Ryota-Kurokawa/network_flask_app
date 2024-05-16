from flask import Flask, render_template
import datetime

app = Flask(__name__)


@app.route("/")
def table():
    schema = ["Id", "Name", "Year", "Place", "Days"]
    # 表の属性名のリスト
    table = [
      [1, "りんごfes1", datetime.date(2020, 10, 4), "青森", datetime.date(2020, 10, 4)],
      [2, "りんごfes2", datetime.date(2021, 10, 4), "青森", datetime.date(2021, 10, 4)],
      [3, "りんごfes3", datetime.date(2022, 10, 4), "青森", datetime.date(2022, 10, 4)],
      [4, "りんごfes4", datetime.date(2023, 10, 4), "青森", datetime.date(2023, 10, 4)],
      [5, "りんごfes5", datetime.date(2024, 10, 4), "青森", datetime.date(2024, 10, 4)]
            ]
    # イベント当日までの日数を計算する
    
    # 表の属性値のリスト
    # return render_template("sample3-2.html", title="教員名簿", schema=schema, table=table)
    return render_template("a3-3.html", title="教員名簿", schema=schema, table=table)

@app.template_filter("date")
def days_left(date):
    today = datetime.date.today()
    return (date - today).days

if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost")



