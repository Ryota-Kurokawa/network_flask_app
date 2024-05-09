from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route('/')

def sample():
  dt = datetime.datetime.now()
  # 秒数が偶数の際は赤色でリターンする
  if dt.second % 2 == 0:
    message = '今は{a}時{b}分{c}秒です'.format(a=dt.hour, b=dt.minute, c=dt.second)
    color = "red"
  else:
    message = '今は{a}時{b}分{c}秒です'.format(a=dt.hour, b=dt.minute, c=dt.second)
    color = "blue"

  return render_template("a2-2.html", title="時間", message=message, color=color)
# def sample():
#     dt = datetime.datetime.now()
#     if dt.second % 2 == 0:
#         message_color = 'red'
#     else:
#         message_color = 'blue'
#     message = '今は{}時{}分{}秒です'.format(dt.hour, dt.minute, dt.second)
#     return render_template("a2-2.html", title="時間", message=message, message_color=message_color)



if __name__ == "__main__":
    # このプログラムが直接起動されたものであれば以下を実行する．
    app.debug = True
    # デバッグ機能をONにする．
    app.run(host="localhost")
    # ホスト名をlocalhostにして，Webアプリケーションを起動する．
