import flask

app = flask.Flask(__name__)


@app.route("/")
def index():
    # 打开并读取 CSV 文件
    f = open("rates.csv", "r", encoding="utf-8")
    # 初始化 HTML 表格字符串
    st = "<table border='1'>"
    rows = f.readlines()

    for row in rows:
        # 去掉行尾换行符并按逗号分割
        s = row.strip().split(",")
        # 确保每行有 6 列数据
        if len(s) == 6:
            st = st + "<tr>"
            for t in s:
                st = st + "<td>" + t + "</td>"
            st = st + "</tr>"

    st = st + "</table>"
    f.close()
    return st


if __name__ == "__main__":
    app.run(debug=True)
