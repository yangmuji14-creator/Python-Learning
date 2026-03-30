from flask import Flask, render_template
from livereload import Server

app = Flask(__name__)

@app.route('/')
def index():
    # 渲染 templates 文件夹下的 index.html
    return render_template('index.html')

if __name__ == '__main__':
    # 实例化 Server 对象
    server = Server(app.wsgi_app)
    # 监控 templates 目录，一旦修改就触发自动刷新
    server.watch('templates/*.html')
    print("服务已启动：访问 http://127.0.0.1:5500 查看网页")
    server.serve(port=5500)