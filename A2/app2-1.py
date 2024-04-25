from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def sample():
    return render_template("sample2-1.html")
    # templateフォルダに入っているsample2-1.htmlを表示する．


if __name__ == "__main__":
    # このプログラムが直接起動されたものであれば以下を実行する．
    app.debug = True
    # デバッグ機能をONにする．
    app.run(host="localhost")
    # ホスト名をlocalhostにして，Webアプリケーションを起動する．

