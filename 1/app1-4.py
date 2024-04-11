from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse

with open("sample1-2.html", mode="r", encoding="utf-8") as file:
    template = file.read()


name = ["北村一輝", "高橋一生", "藤原竜介"]
# 名前のリストを初期化する．


class MyServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        _url = urlparse(self.path)
        query = parse_qs(_url.query)
        # URLからクエリパラメータを取り出す．

        try:
            id = int(query["id"][0])
            # クエリパラメータidの値を取り出す．
            if id >= 1 and id <= 3:
                # idの値の範囲が1以上3以下であれば，該当する名前を表示する．
                message = "これは{}のページです．".format(name[id - 1])
            else:
                # idの値の範囲が1以上3以下でない場合は，そのことを示すメッセージを表示する．
                message = "クエリパラメータの範囲が誤りです．"
        except ValueError:
            # idの値が整数でない場合は，ValueErrorが生じるので，そのことを示すメッセージを表示する．
            message = "クエリパラメータの値が整数ではありません．"
        except KeyError:
            # idがURLに含まれていない場合は，KeyErrorが生じるので，そのことを示すメッセージを表示する．
            message = "クエリパラメータの名前が正しくありません．"

        self.send_response(200)
        self.end_headers()
        html = template.format(title="クエリパラメータテスト", message=message)
        self.wfile.write(html.encode("utf-8"))
        return


HTTPServer(("", 8000), MyServerHandler).serve_forever()

