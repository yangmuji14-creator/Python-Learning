import urllib.request
import re


class MySpider:
    def spider(self, url):
        try:
            resp = urllib.request.urlopen(url)
            data = resp.read()
            html = data.decode()
            p = re.search(r"<tr>", html)
            q = re.search(r"</tr>", html)
            i = 0
            while p and q:
                a = p.end()
                b = q.start()
                tds = html[a:b]
                m = re.search(r"<td>", tds)
                n = re.search(r"</td>", tds)
                row = []
                while m and n:
                    u = m.end()
                    v = n.start()
                    row.append(tds[u:v].strip("\n"))
                    tds = tds[n.end():]
                    m = re.search(r"<td>", tds)
                    n = re.search(r"</td>", tds)

                i = i + 1
                # 第1行是标题，从第2行开始处理数据
                if i >= 2 and len(row) == 6:
                    Currency = row[0]
                    TSP = float(row[2])
                    CSP = float(row[3])
                    TBP = float(row[4])
                    CBP = float(row[5])
                    # 直接打印结果
                    print(f"{Currency}: TSP={TSP}, CSP={CSP}, TBP={TBP}, CBP={CBP}")
                    # print(f"{Currency}: {TSP}, {CSP}, {TBP}, {CBP}")

                html = html[q.end():]
                p = re.search(r"<tr>", html)
                q = re.search(r"</tr>", html)
        except Exception as err:
            print(err)

    def process(self):
        # 模拟执行过程
        self.spider("http://127.0.0.1:5000")


# 主程序
spider = MySpider()
spider.process()