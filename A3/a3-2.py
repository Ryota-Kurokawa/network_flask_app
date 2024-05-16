from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def table():
    schema = ["Id", "Name", "Year", "Place"]
    # 表の属性名のリスト
    table = [[1, "りんごfes1", 2020, "青森"],
            [2, "りんごfes2", 2021, "青森"],
            [3, "りんごfes3", 2022, "青森"],
            [4, "りんごfes4", 2023, "青森"],
            [5, "りんごfes5", 2024, "青森"]
            ]
    # 表の属性値のリスト
    return render_template("sample3-2.html", title="教員名簿", schema=schema, table=table)


if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost")

