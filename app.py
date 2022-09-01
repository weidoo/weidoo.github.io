from flask import Flask,render_template,url_for

import test

app = Flask(__name__)

database = {
        'host': 'localhost',
        'port': 3306,
        'user': 'root',
        'passwd': 'Doraemon903@CN',
        'db': 'hot_top',
        'charset': 'utf8'
    }


@app.route('/')
def hello_world():
    data = test.getdata(database)
    title = []
    url = []
    style = ("ou","ji")
    for d in data:
        title.append(d[1])
        url.append(d[3])
    # print(title)
    # print(url)
    return render_template("index.html",title= title,url=url,style = style)


if __name__ == '__main__':
    app.run()
